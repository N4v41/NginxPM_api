"""
Nginx Proxy Manager python API client.
Permit send commands to npm server via http calls
"""
import requests
import json


from ._certificates import certificates
from ._access_lists import accesslist
from ._proxy import proxy
from ._redir import redirhost
from ._deadhosts import deadhosts
from ._streams import streams

class NginxPM:
    """
    NginxPM class.
    Require:
        - url: npm server url
        - user: npm user
        - passwd: npm password
    """
    def __init__(self, url, user, passwd):
        self.url = url
        self.user = user
        self.passwd = passwd
        self.session = requests.Session()
        self.token = self._authenticate()
        self.auth_header = {'Authorization': 'Bearer ' + self.token}
        self.session.headers.update(self.auth_header)


    def _authenticate(self):
        """
        Create session token
        """
        login_url = self.url + "/api/tokens"
        body = {
            "identity": self.user,
            "secret": self.passwd
            }
        response = self.session.post(login_url, data=body, verify=False)
        if response.ok:
            return (json.loads(response.text))['token']
        else:
            return print("Error: " + response.text)
        
    def proxy(self, action=None):
        """
        call the proxy module
        """
        return proxy(self, action)

    def accesslist(self, action=None):
        """
        call the accesslist module
        """
        return accesslist(self, action)

    def redirhost(self, action=None):
        """
        call the redirhost module
        """
        return redirhost(self, action)

    def deadhosts(self, action=None):
        """
        call the deadhosts module
        """
        return deadhosts(self, action)

    def streams(self, action=None):
        """
        call the streams module
        """
        return streams(self, action)

    def certificates(self, action=None):
        """
        call the certificates module
        """
        return certificates(self, action)

    def __str__(self):
        return "NginxPM class"   
        