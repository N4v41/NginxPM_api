"""
Nginx Proxy Manager python API client.
Module for redirection host management.
"""

def redirhost(NginxPM, action=None):
    """
    Execute Calls to the redirhost endpoint
    Suported actions:
        - list:
            - list all redirection host
        - get:
            - get a redirection host by id
        - enable:   (not implemented)
            - enable a redirection host
        - disable:  (not implemented)
            - disable a redirection host
        - create: (not implemented)
            - create a new redirection host
        - delete:
            - delete a redirection host
    """
    _actions = ("list", "get", "create", "delete")
    _redirhost_url = NginxPM.url + "/api/nginx/redirection-hosts"
    _http_codes = [300, 301, 302, 303, 307, 308]
    _foward_schemes = ["$scheme", "http", "https"]
    
    #------Sub Functions------
    def redirhost_list():
        """
        List all redirection hosts
        """
        return NginxPM.session.get(_redirhost_url).json()
    
    def redirhost_get(id):
        """
        Get an redirection host by id
        """
        return NginxPM.session.get(_redirhost_url + str(id)).json()
    
    def redirhost_delete(id):
        """
        Delete an redirection host by id
        """
        return NginxPM.session.delete(_redirhost_url + str(id)).json()
    
    def redirhost_enable(id):
        """
        Enable an redirection host by id
        """
        return NginxPM.session.post(_redirhost_url + str(id) + "/enable").json()
    
    def redirhost_disable(id):
        """
        Disable an redirection host by id
        """
        return NginxPM.session.post(_redirhost_url + str(id) + "/disable").json()
    
    def redirhost_create(domains, forward_scheme, forward_host, foward_http_code, preserve_path, block_exploits, cert_id, adv_config , http2_support, hsts_enabled, hsts_subdomains, ssl_forced):
        """
        Create a new redirection host
        """
        if foward_http_code not in _http_codes:
            raise ValueError("Invalid HTTP code")
        if forward_scheme not in _foward_schemes:
            raise ValueError("Invalid forward scheme")
        
        _body = {
            "domain_names": domains,
            "forward_scheme": str(forward_scheme),
            "forward_domain_name":str(forward_host),
            "forward_http_code":str(foward_http_code),
            "preserve_path": bool(preserve_path),
            "block_exploits":bool(block_exploits),
            "certificate_id": int(cert_id),
            "meta":{
                "letsencrypt_agree":False,
                "dns_challenge":False
                },
            "advanced_config":str(adv_config),
            "http2_support":bool(http2_support),
            "hsts_enabled":bool(hsts_enabled),
            "hsts_subdomains":bool(hsts_subdomains),
            "ssl_forced": bool(ssl_forced),
        }
        return NginxPM.session.post(_redirhost_url, json=_body).json()
    
    def redirhost_update(id, domains, forward_scheme, forward_host, foward_http_code, preserve_path, block_exploits, cert_id, adv_config , http2_support, hsts_enabled, hsts_subdomains, ssl_forced):
        """
        Update a redirection host by id
        """
        _body = {
            "domain_names": domains,
            "forward_scheme": str(forward_scheme),
            "forward_domain_name":str(forward_host),
            "forward_http_code":str(foward_http_code),
            "preserve_path": bool(preserve_path),
            "block_exploits":bool(block_exploits),
            "certificate_id": int(cert_id),
            "meta":{
                "letsencrypt_agree":False,
                "dns_challenge":False
                },
            "advanced_config":str(adv_config),
            "http2_support":bool(http2_support),
            "hsts_enabled":bool(hsts_enabled),
            "hsts_subdomains":bool(hsts_subdomains),
            "ssl_forced": bool(ssl_forced),
        }
        return NginxPM.session.put(_redirhost_url + str(id), json=_body).json()
    
    #------Sub Functions------
    #------Main Processing------
    if action not in _actions:
        raise ValueError("Action not supported")







