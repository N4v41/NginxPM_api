"""
Nginx Proxy Manager python API client.
Module for certificate management.
"""

def certificates(NginxPM, action=None):
    """
    Execute Calls to the certificate endpoint
    Suported actions:
        - list:
            - list all certificates
        - get:
            - get a cerficate by id
        - create: (not implemented)
            - create a new certificate
        - delete:
            - delete a certificate
        - renew:
            - renew a certificate
        - download: (not implemented)
            - download a certificate
    """
    _actions = ("list", "get", "create", "delete")
    _certificates_url = NginxPM.url + "/api/nginx/certificates"
    
    #------Sub Functions------
    def certificate_list():
        """
        List all certificates
        """
        return NginxPM.session.get(_certificates_url).json()
    
    def certificate_get(id):
        """
        Get a certificate by id
        """
        return NginxPM.session.get(_certificates_url + str(id)).json()
    
    def certificate_delete(id):
        """
        Delete a certificate by id
        """
        return NginxPM.session.delete(_certificates_url + str(id)).json()
    
    def certificate_renew(id):
        """
        Renew a certificate by id
        """
        return NginxPM.session.post(_certificates_url + str(id) + "/renew").json()
    
    def certificate_create(domains, letsencrypt_email, cloudlare_api_key):
        """
        Create a new certificate
        """
        body = {
            "domain_names": list(domains),
            "meta":{
                "letsencrypt_email": str(letsencrypt_email),
                "dns_challenge":True,
                "dns_provider":"cloudflare",
                "dns_provider_credentials":f"# Cloudflare API token\r\ndns_cloudflare_api_token = {cloudlare_api_key}",
                "letsencrypt_agree":True
                },
            "provider":"letsencrypt"}
        return NginxPM.session.post(_certificates_url, data=body).json()
    
    def certificate_download(id):
        """
        Download a certificate by id
        """
        return NginxPM.session.get(_certificates_url + str(id) + "/download").json()
    
    #------Sub Functions------
    #------Main Processing------
    if action not in _actions:
        raise ValueError("Action not supported")

    if action == "list":
        return certificate_list()
    elif action == "get":
        return certificate_get(id)
    elif action == "create":
        return certificate_create(domains, letsencrypt_email, cloudlare_api_key)
    elif action == "delete":
        return certificate_delete(id)
    elif action == "renew":
        return certificate_renew(id)
    elif action == "download":
        return certificate_download(id)
    #------Main Processing------
