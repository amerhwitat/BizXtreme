#!/usr/bin/env python3
import http.server,json,os,socket,ipaddress
PORT=int(os.getenv('NETWORK_API_PORT','8787')); ALLOW=set(filter(None,os.getenv('NETWORK_API_ALLOWLIST','').split(',')))
CAT={'schema':'bizxtreme.network.api.v1','implementation':'python','endpoints':['GET /api/v1','GET /api/v1/health','GET /api/v1/config','POST /api/v1/classify','POST /api/v1/authorize','POST /api/v1/tcp-check','GET /api/v1/interfaces']}
def classify(x):
 a=ipaddress.ip_address(x); return 'local/intranet' if a.is_private or a.is_loopback or a.is_link_local else 'public'
def allowed(x): return classify(x)!='public' or x in ALLOW
class H(http.server.BaseHTTPRequestHandler):
 def out(self,o,code=200):
  b=json.dumps(o).encode();self.send_response(code);self.send_header('Content-Type','application/json');self.send_header('Access-Control-Allow-Origin','*');self.send_header('Content-Length',str(len(b)));self.end_headers();self.wfile.write(b)
 def do_OPTIONS(self): self.send_response(204);self.send_header('Access-Control-Allow-Origin','*');self.send_header('Access-Control-Allow-Methods','GET,POST,OPTIONS');self.send_header('Access-Control-Allow-Headers','Content-Type');self.end_headers()
 def do_GET(self):
  if self.path=='/api/v1':return self.out(CAT)
  if self.path=='/api/v1/health':return self.out({'status':'ok','implementation':'python'})
  if self.path=='/api/v1/config':return self.out({'authorizedOnly':True,'allowlistCount':len(ALLOW),'port':PORT})
  if self.path=='/api/v1/interfaces':return self.out({'hostname':socket.gethostname(),'addresses':list({x[4][0] for x in socket.getaddrinfo(socket.gethostname(),None)})})
  return self.out({'error':'not_found'},404)
 def do_POST(self):
  try:d=json.loads(self.rfile.read(int(self.headers.get('Content-Length','0')) or 0) or b'{}')
  except:return self.out({'error':'invalid_json'},400)
  x=d.get('ip') or d.get('host')
  if self.path=='/api/v1/classify':
   try:return self.out({'target':x,'scope':classify(x)})
   except:return self.out({'error':'invalid_ip'},400)
  if self.path=='/api/v1/authorize':
   try:return self.out({'target':x,'scope':classify(x),'authorized':allowed(x)})
   except:return self.out({'error':'invalid_ip'},400)
  if self.path=='/api/v1/tcp-check':
   if not x:return self.out({'error':'target_required'},400)
   try:
    if not allowed(x):return self.out({'error':'public_target_not_allowlisted'},403)
    p=int(d.get('port',80));s=socket.create_connection((x,p),timeout=min(float(d.get('timeout',1)),3));s.close();return self.out({'target':x,'port':p,'reachable':True})
   except Exception as e:return self.out({'target':x,'port':d.get('port',80),'reachable':False,'error':type(e).__name__})
  return self.out({'error':'not_found'},404)
 def log_message(self,*a):pass
print(f'BizXtreme Network API (python) listening on 127.0.0.1:{PORT}')
http.server.ThreadingHTTPServer(('127.0.0.1',PORT),H).serve_forever()
