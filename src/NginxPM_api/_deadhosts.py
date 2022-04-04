"""
Nginx Proxy Manager python API client.
Module for 404 host (Dead Host) management.
"""

def deadhosts(NginxPM, action=None):
    """
    Execute Calls to the deadhost endpoint
    Suported actions:
        - list:
            - list all 404 hosts
        - get:
            - get a 404 host by id
        - enable:   (not implemented)
            - enable a 404 host
        - disable:  (not implemented)
            - disable a 404 host
        - create: (not implemented)
            - create a new 404 host
        - delete:
            - delete a 404 host
    """
    _actions = ("list", "get", "delete", "enable", "disable", "create")
    _deadhosts_url = NginxPM.url + "/api/nginx/dead-hosts"

    
    #------Sub Functions------
    def deadhost_list():
        """
        List all dead hosts
        """
        return NginxPM.session.get(_deadhosts_url).json()
    
    def deadhost_get(id):
        """
        Get an dead host by id
        """
        return NginxPM.session.get(_deadhosts_url + str(id)).json()
    
    def deadhost_delete(id):
        """
        Delete an dead host by id
        """
        return NginxPM.session.delete(_deadhosts_url + str(id)).json()
    
    def deadhost_enable(id):
        """
        Enable an dead host by id
        """
        return NginxPM.session.post(_deadhosts_url + str(id) + "/enable").json()
    
    def deadhost_disable(id):
        """
        Disable an dead host by id
        """
        return NginxPM.session.post(_deadhosts_url + str(id) + "/disable").json()
    
    def deadhost_create(body):
        """
        Create a new dead host
        """
        _body = {
        "domain_names":["teste.home"],
        "certificate_id":0,
        "meta":{
            "letsencrypt_agree":False,
            "dns_challenge":False},
            "advanced_config":"",
            "hsts_enabled":False,
            "hsts_subdomains":False,
            "http2_support":False,
            "ssl_forced":False
        }
        return NginxPM.session.post(_deadhosts_url, body=_body).json()
    
    def deadhost_update(id, body):
        """
        Update an dead host by id
        """
        _body = {
        "domain_names":["teste.home"],
        "certificate_id":0,
        "meta":{
            "letsencrypt_agree":False,
            "dns_challenge":False},
            "advanced_config":"",
            "hsts_enabled":False,
            "hsts_subdomains":False,
            "http2_support":False,
            "ssl_forced":False
        }
        return NginxPM.session.put(_deadhosts_url + str(id), body=_body ).json()
    
    #------Sub Functions------
    #------Main Processing------
    if action not in _actions:
        raise ValueError("Action not supported")
