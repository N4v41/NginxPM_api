"""
Nginx Proxy Manager python API client.
Module for proxy management.
"""

def proxy(self, action=None):
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
    _proxy_url = self.url + "/api/nginx/proxy-hosts"
    _foward_scheme = ("http", "https")
    
    #------Sub Functions------
    def proxy_list():
        """
        List all proxies hosts
        """
        return self.session.get(_proxy_url, verify=False).json()

    def proxy_get(id):
        """
        Get a proxy host by id
        """
        return self.session.get(_proxy_url + str(id)).json()
    
    def proxy_enable(id):
        """
        Enable a proxy host by id
        """
        return self.session.post(_proxy_url + str(id) + "/enable").json()
    
    def proxy_disable(id):
        """
        Disable a proxy host by id
        """
        return self.session.post(_proxy_url + str(id) + "/disable").json()
    
    def proxy_delete(id):
        """
        Delete a proxy host by id
        """
        return self.session.delete(_proxy_url + str(id)).json()

    def proxy_update(id):
        """
        Update a proxy host by id
        """
        return self.session.put(_proxy_url + str(id), data=_body).json()

    def proxy_create(domains, fwd_scheme, fwd_host, fwd_port, cache_enabled, blk_exploits, ws_upgrade, \
        acss_list_id, cert_id, ssl_forced, http2_support, adv_config, hsts_enabled, hsts_subdomains):
        """
        Create a new proxy host
        """
        _body= {
            "domain_names":list(domains),
            "forward_scheme":str(fwd_scheme),
            "forward_host":str(fwd_host),
            "forward_port":int(fwd_port),
            "caching_enabled":bool(cache_enabled),
            "block_exploits":bool(blk_exploits),
            "allow_websocket_upgrade":bool(ws_upgrade),
            "access_list_id":str(acss_list_id),
            "certificate_id":int(cert_id),
            "ssl_forced":bool(ssl_forced),
            "http2_support":bool(http2_support),
            "meta":{
                "letsencrypt_agree":"false",
                "dns_challenge":"false"
                },
            "advanced_config":str(adv_config),
            "locations":[
                {"path":"/teste",
                "advanced_config":"#asda",
                "forward_scheme":"http",
                "forward_host":"192.168.100.2",
                "forward_port":"80"}],
            "hsts_enabled":bool(hsts_enabled),
            "hsts_subdomains":bool(hsts_subdomains)
            }
        response = self.session.post(_proxy_url, data=_body)
        return response.json()
    #------Sub Functions------
    #------Main Processing------
    if action not in _actions:
        raise ValueError("Action not supported")
    
    if action == "list":
        return proxy_list()
    elif action == "get":
        return proxy_get(id)
    elif action == "update":
        return proxy_update(id)
    elif action == "create":
        return proxy_create(domains, fwd_scheme, fwd_host, fwd_port, cache_enabled, blk_exploits, ws_upgrade, \
        acss_list_id, cert_id, ssl_forced, http2_support, adv_config, hsts_enabled, hsts_subdomains)
    elif action == "delete":
        return proxy_delete(id)
    elif action == "enable":
        return proxy_enable(id)
    elif action == "disable":
        return proxy_disable(id)
    
    #------Main Processing------