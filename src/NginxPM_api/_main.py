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
            "secret": self.password
            }
        response = self.session.post(login_url, data=body)
        if response.ok:
            return (json.loads(response.text))['token']
        else:
            return print("Error: " + response.text)
        