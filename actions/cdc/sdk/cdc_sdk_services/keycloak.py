from cdc.sdk.cdc_sdk_services.http import HttpJsonService

class KeycloakService:
    def __init__(self, url, clientId, clientSecret):
        self.headers = { 'Content-Type': 'application/x-www-form-urlencoded' }
        self.clientConfig = '&client_id=' + clientId + '&client_secret=' + clientSecret
        self.http = HttpJsonService(url + '/protocol/openid-connect/')
    
    def buildAuthParameters(self, user, password, grantType):
        return 'username=' + user + '&password=' + password + '&grant_type=' + grantType + self.clientConfig

    def withClientCredentials(self, user, password):
        self.payload = self.buildAuthParameters(user, password, 'client_credentials')

    def withUserCredentials(self, user, password):
        self.payload = self.buildAuthParameters(user, password, 'password')

    def withTokenExchange(self, user):
        self.payload = 'grant_type=urn:ietf:params:oauth:grant-type:token-exchange&requested_subject=' + user + self.clientConfig
        
    def getAccessToken(self):
        try:
            grant = self.http.json('token', 'POST', self.payload, headers=self.headers)
            return grant.get('access_token') or None
        except Exception as ex:
            print('Keycload: failed to retrieve access token', ex)
            return None

    def getRequestHeaders(self):
        token = self.getAccessToken()
        if token is None:
            return {}
        return { 'Authorization': 'Bearer ' + token, 'Cache-Control': 'no-cache' }

    def getUserInfo(self, username):
        try:
            headers = self.http.headers(self.headers, self.getRequestHeaders())
            return requests.request('userinfo', 'POST', headers=headers)
        except Exception as ex:
            print('Keycload: failed to retrieve user info', ex)

