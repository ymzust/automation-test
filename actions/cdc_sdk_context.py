import datetime
import json
import os
import urllib3
from dotmap import DotMap

from cdc_sdk_services.cdc import CDCBackendService
from cdc_sdk_services.keycloak import KeycloakService
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration

class Context:
    def __init__(self):
        self.notify('start loading...')
        self.attachInternals()
        if (self.loadSettings()):
            self.notify('settings loaded successfully')
        keycloak = self.connectToKeycloak(self.settings.keycloak)
        if (keycloak):
            self.notify('connected to keycloak')
            self.initializeServices(keycloak)
            self.client = self.setClient()
            if (self.client):
                self.notify('CDC Backend client is ready for use')
            self.notify('loading process completed')
        else:
            self.client = None

    instance = None
        
    def attachInternals(self):
        dec = json.JSONDecoder()
        enc = json.JSONEncoder()
        self.json = DotMap()
        self.json.parse = dec.decode
        self.json.strinfigy = enc.encode
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def connectToKeycloak(self, settings):
        try:
            keycloak = KeycloakService(settings.instance, settings.client.name, settings.client.secret)
            self.notify('use keycloak with impersonation')
            keycloak.withTokenExchange(settings.user)
            return keycloak
        except Exception as ex:
            self.notify('unable to establish a connection against Keycloak', ex)

    def initializeServices(self, keycloak):
        try:
            self.services = DotMap()
            self.services.keycloak = keycloak
            self.services.cdc.backend = CDCBackendService(self.settings.cdc.url + '/app', keycloak)
        except Exception as ex:
            self.notify('error during services initialization', ex)

    def loadSettings(self):
        try:
            #path = os.path.join(os.getcwd(), '.env')
            #self.notify('environment variables file location: ' + path)
            #load_dotenv(dotenv_path=path, override=False, verbose=True)
            self.settings = DotMap()
            self.settings.cdc.url = os.getenv('CDC_URL')
            self.settings.keycloak.instance = os.getenv('KEYCLOAK_URL')
            self.settings.keycloak.client.name = os.getenv('KEYCLOAK_CLIENT_ID')
            self.settings.keycloak.client.secret = os.getenv('KEYCLOAK_CLIENT_SECRET')
            self.settings.keycloak.user = os.getenv('KEYCLOAK_USER')
            self.settings.organization = os.getenv('CDC_ORGANIZATION_KEY')
            return True
        except Exception as ex:
            self.notify('error while loading settings file', ex)

    def notify(self, message, exception=None):
        sections = [ str(datetime.datetime.now()) + ' CDC Automation SDK: ' + message ]
        if (exception):
            sections.append(exception)
        print(sections)

    def setClient(self):
        try:
            config = Configuration()
            config.host = self.settings.cdc.url + '/app'
            headers = self.services.keycloak.getRequestHeaders()

            client = ApiClient(config)
            names = list(headers)
            for name in names:
                client.set_default_header(name, headers.get(name))
            return client
        except Exception as ex:
            self.notify('unable to initiate Backend client', ex)