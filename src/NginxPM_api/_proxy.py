"""
Nginx Proxy Manager python API client.
Module for proxy management.
"""

def proxy(NginxPM, action=None):
    """
    Execute Calls to the proxy endpoint
    Suported actions:
        - list:
            - list all proxies
        - get:
            - get a proxy by id
        - update:
            - update a proxy host
        - create:
            - create a new proxy
        - delete:
            - delete a proxy
        - enable:   (not implemented)
            - enable a proxy
        - disable:  (not implemented)
            - disable a proxy
    """
    _actions = ("list", "get", "create", "delete")
    _proxy_url = NginxPM.url + "/api/nginx/proxy-hosts"
    
    #------Sub Functions------
    def proxy_list():
        """
        List all proxies hosts
        """
        return NginxPM.session.get(_proxy_url).json()
    
    def proxy_get(id):
        """
        Get a proxy host by id
        """
        return NginxPM.session.get(_proxy_url + str(id)).json()
    
    def proxy_enable(id):
        """
        Enable a proxy host by id
        """
        return NginxPM.session.post(_proxy_url + str(id) + "/enable").json()
    
    def proxy_disable(id):
        """
        Disable a proxy host by id
        """
        return NginxPM.session.post(_proxy_url + str(id) + "/disable").json()
    
    def proxy_delete(id):
        """
        Delete a proxy host by id
        """
        return NginxPM.session.delete(_proxy_url + str(id)).json()

    def proxy_update(id, body):
        """
        Update a proxy host by id
        """
        return NginxPM.session.put(_proxy_url + str(id), data=body).json()

    def proxy_create(body):
        """
        Create a new proxy host
        """
        body= {
            "domain_names":["teste.home"],
            "forward_scheme":"http",
            "forward_host":"tttt",
            "forward_port":80,
            "caching_enabled":"true",
            "block_exploits":"true",
            "allow_websocket_upgrade":"true",
            "access_list_id":"0",
            "certificate_id":32,
            "ssl_forced":"true",
            "http2_support":"true",
            "meta":{
                "letsencrypt_agree":"false",
                "dns_challenge":"false"
                },
            "advanced_config":"",
            "locations":[],
            "hsts_enabled":"false",
            "hsts_subdomains":"false"
            }
        response = NginxPM.session.get(_proxy_url, data=body)
        return response.json()
    #------Sub Functions------
    #------Main Processing------
    if action not in _actions:
        raise ValueError("Action not supported")
