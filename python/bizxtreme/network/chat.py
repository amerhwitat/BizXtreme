"""Length-prefixed JSON TCP chat transport for private/LAN game sessions."""
from __future__ import annotations
import json, socket, struct
MAX_MESSAGE=64*1024

def _read(s,n):
    b=bytearray()
    while len(b)<n:
        x=s.recv(n-len(b))
        if not x: raise ConnectionError('peer disconnected')
        b.extend(x)
    return bytes(b)

def _send(s,obj):
    b=json.dumps(obj,ensure_ascii=False,separators=(',',':')).encode()
    if len(b)>MAX_MESSAGE: raise ValueError('message too large')
    s.sendall(struct.pack('!I',len(b))+b)

def _recv(s):
    n=struct.unpack('!I',_read(s,4))[0]
    if n>MAX_MESSAGE: raise ValueError('message too large')
    return json.loads(_read(s,n).decode())

class ChatPeer:
    def __init__(self,host,port,token,timeout=5): self.host,self.port,self.token,self.timeout=host,port,token,timeout
    def send(self,sender,text):
        with socket.create_connection((self.host,self.port),self.timeout) as s:
            _send(s,{'type':'hello','token':self.token})
            if _recv(s).get('type')!='ok': raise PermissionError('chat authentication failed')
            _send(s,{'type':'chat','sender':sender,'text':text[:MAX_MESSAGE]})
            return _recv(s)

class ChatServer:
    def __init__(self,host,port,token): self.address=(host,port); self.token=token
    def serve_once(self,handler):
        with socket.socket() as srv:
            srv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1); srv.bind(self.address); srv.listen(8)
            conn,_=srv.accept()
            with conn:
                if _recv(conn).get('token')!=self.token: _send(conn,{'type':'error','error':'unauthorized'}); return
                _send(conn,{'type':'ok'}); handler(_recv(conn)); _send(conn,{'type':'delivered'})
