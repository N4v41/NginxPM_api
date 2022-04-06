"""
Nginx Proxy Manager python API client.
Module for streams management.
"""

def streams(NginxPM, action=None):
    """
    Execute Calls to the stream endpoint
    Suported actions:
        - list:
            - list all stream
        - get:
            - get a stream by id
        - enable:   (not implemented)
            - enable a stream
        - disable:  (not implemented)
            - disable a stream
        - create: (not implemented)
            - create a new stream
        - update: (not implemented)
            - update a stream
        - delete:
            - delete a stream
    """
    _actions = ("list", "get", "delete", "enable", "disable")
    _stream_url = NginxPM.url + "/api/nginx/streams"
    
    #------Sub Functions------
    def stream_list():
        """
        List all streams
        """
        return NginxPM.session.get(_stream_url).json()
    
    def stream_get(id):
        """
        Get an stream by id
        """
        return NginxPM.session.get(_stream_url + str(id)).json()
    
    def stream_delete(id):
        """
        Delete an stream by id
        """
        return NginxPM.session.delete(_stream_url + str(id)).json()
    
    def stream_disable(id):
        """
        Disable an stream by id
        """
        return NginxPM.session.post(_stream_url + str(id) + "/disable").json()
    
    def stream_enable(id):
        """
        Enable an stream by id
        """
        return NginxPM.session.post(_stream_url + str(id) + "/enable").json()
    
    def stream_create(inc_port, fwd_host, fwd_port, tcp_fwd, udp_fwd):
        """
        Create a new stream
        """
        _body = {
            "incoming_port": int(inc_port),
            "forwarding_host": fwd_host,
            "forwarding_port": int(fwd_port),
            "tcp_forwarding": bool(tcp_fwd),
            "udp_forwarding": bool(udp_fwd)
        }
        return NginxPM.session.post(_stream_url, data=_body).json()
    
    def stream_update(id, inc_port, fwd_host, fwd_port, tcp_fwd, udp_fwd):
        """
        Update an stream by id
        """
        _body = {
            "incoming_port": int(inc_port),
            "forwarding_host": fwd_host,
            "forwarding_port": int(fwd_port),
            "tcp_forwarding": bool(tcp_fwd),
            "udp_forwarding": bool(udp_fwd)
        }
        return NginxPM.session.put(_stream_url + str(id), data=_body).json()

    #------Sub Functions------
    #------Main Processing------
    if action not in _actions:
        raise ValueError("Action not supported")
    
    if action == "list":
        return stream_list()
    elif action == "get":
        return stream_get(id)
    elif action == "delete":
        return stream_delete(id)
    elif action == "enable":
        return stream_enable(id)
    elif action == "disable":    
        return stream_disable(id)
    elif action == "create":
        return stream_create(inc_port, fwd_host, fwd_port, tcp_fwd, udp_fwd)
    elif action == "update":
        return stream_update(id, inc_port, fwd_host, fwd_port, tcp_fwd, udp_fwd)
    #------Main Processing------



