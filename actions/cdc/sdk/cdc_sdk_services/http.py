import json
import requests

from bson.objectid import ObjectId

class HttpService(object):
    def __init__(self, path):
        self.basePath = path

    def fullPath(self, path):
        return self.basePath + path

    def headers(self, *sources):
        headers = dict()
        for source in sources:
            headers.update(source)
        return headers
    
    def request(self, path, method='GET', payload=None, params={}, headers={}):
        return requests.request(method, self.fullPath(path), data=payload, params=params, headers=headers, verify=False)


class HttpJsonService(HttpService):
    def __init__(self, path):
        HttpService.__init__(self, path)
        self.encoder = json.JSONEncoder()

    def encode(self, payload):
        return self.encoder.encode(payload)
 
    def json(self, path, method='GET', payload=None, params={}, headers={}):
        response = self.request(path, method, payload, params, headers)
        return json.loads(response.content)