"""
Nginx Proxy Manager python API client.
Module for access lists management.
"""

def accesslist(NginxPM, action=None):
    """
    Execute Calls to the access lists endpoint
    Suported actions:
        - list:
            - list all access lists
        - get:
            - get an access list by id
        - create:
            - create a new access list
        - delete:
            - delete an access list
        - update:
            - update an access list
    """
    _actions = ("list", "get", "create", "delete", "update")
    _accesslist_url = NginxPM.url + "/api/nginx/access-lists"
    
    #------Sub Functions------
    def accesslist_list():
        """
        List all access lists
        """
        return NginxPM.session.get(_accesslist_url).json()
    
    def accesslist_get(id):
        """
        Get an access list by id
        """
        return NginxPM.session.get(_accesslist_url + str(id)).json()
    
    def accesslist_delete(id):
        """
        Delete an access list by id
        """
        return NginxPM.session.delete(_accesslist_url + str(id)).json()
    
    def accesslist_update(id, body):
        """
        Update an access list by id
        """
        return NginxPM.session.put(_accesslist_url + str(id), json=body).json()
        
    def accesslist_create(name, satisfy_any, pass_auth, items, clients ):
        """
        Create a new access list
        """
        body= {
            "name": str(name),
            "satisfy_any": bool(satisfy_any),
            "pass_auth": bool(pass_auth),
            "items":[
                {"username":"teste","password":"teste"}
                ],
            "clients":[
                {"address":"192.168.100.4","directive":"allow"},
                {"address":"192.168.150.0/24","directive":"deny"}
                ]
            }
        return NginxPM.session.post(_accesslist_url, json=body).json()
    
    #------Sub Functions------
    #------Main Processing------
    if action not in _actions:
        raise ValueError("Action not supported")

    if action == "list":
        return accesslist_list()
    elif action == "get":
        return accesslist_get(id)
    elif action == "create":
        return accesslist_create(name, satisfy_any, pass_auth, items, clients )
    elif action == "delete":
        return accesslist_delete(id)
    elif action == "update":
        return accesslist_update(id, body)