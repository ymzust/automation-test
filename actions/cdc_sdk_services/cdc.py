from cdc_sdk_services.http import HttpJsonService
from cdc_sdk_services.keycloak import KeycloakService

class CDCBackendService(HttpJsonService):
    def __init__(self, path, keycloak):
        HttpJsonService.__init__(self, path)
        self.super = super(CDCBackendService, self)
        self.keycloak = keycloak

    def json(self, path, method='GET', payload=None, params={}, headers={}):
        return self.super.json(path, method, payload, params, self.headers(headers, self.keycloak.getRequestHeaders()))