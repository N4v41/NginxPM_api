"""
Nginx Proxy Manager python API client.
Module for access lists management.
"""

def accesslist(self, action=None, **kwargs):
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
    Body: 
        {
        "name": str(name),
        "satisfy_any": bool(satisfy_any),
        "pass_auth": bool(pass_auth),
        "items":[
            {"username":"test","password":"test"}
            ],
        "clients":[
            {"address":"192.168.180.4/32","directive":"allow"},
            {"address":"192.168.150.0/24","directive":"deny"}
            ]
        }

    """
    _actions = ("list", "get", "create", "delete", "update")
    _accesslist_url = self.url + "/api/nginx/access-lists"
    
    #------Sub Functions------
    def accesslist_list():
        """
        List all access lists
        """
        return self.session.get(_accesslist_url).json()
    
    def accesslist_get(id):
        """
        Get an access list by id
        """
        return self.session.get(_accesslist_url + str(id)).json()
    
    def accesslist_delete(id):
        """
        Delete an access list by id
        """
        return self.session.delete(_accesslist_url + str(id)).json()
    
    def accesslist_update(id, body):
        """
        Update an access list by id
        """
        return self.session.put(_accesslist_url + str(id), json=body).json()
        
    def accesslist_create(name, satisfy_any, pass_auth, users, clients ):
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
        return self.session.post(_accesslist_url, json=body).json()
    
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