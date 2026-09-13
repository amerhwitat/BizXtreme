#!/usr/bin/env python3
import hashlib,http.server,json,mimetypes,os,pathlib,socket,urllib.parse,urllib.request
from urllib.parse import urlparse
ROOT=pathlib.Path(__file__).resolve().parents[1]; WEB=ROOT/'web'; PROVIDERS=json.loads((ROOT/'config/providers.json').read_text())
PORT=int(os.getenv('ASSET_BROWSER_PORT','8790')); STORE=pathlib.Path(os.getenv('ASSET_BROWSER_DIR',str(ROOT/'game_assets'))); STORE.mkdir(parents=True,exist_ok=True); MANIFEST=STORE/'manifest.json'; UA='BizXtreme-AssetBrowser/1.0 (+in-game asset browser)'
SAFE_EXT={'.png','.jpg','.jpeg','.webp','.gif','.wav','.ogg','.mp3','.flac','.glb','.gltf','.obj','.mtl','.hdr','.exr','.ttf','.otf','.json','.txt','.zip'}
def get(u):
 r=urllib.request.Request(u,headers={'User-Agent':UA})
 with urllib.request.urlopen(r,timeout=15) as x:return x.read()
def ok(u,p):return urlparse(u).scheme=='https' and urlparse(u).hostname in PROVIDERS[p]['download_hosts']
def mf():
 try:return json.loads(MANIFEST.read_text())
 except:return []
def save(x):MANIFEST.write_text(json.dumps(x,indent=2,ensure_ascii=False))
def first_url(x):
 if isinstance(x,dict):
  if isinstance(x.get('url'),str):return x['url']
  for v in x.values():
   u=first_url(v)
   if u:return u
 return None
def search(p,q,k):
 if p=='openverse':
  b=PROVIDERS[p]['search_audio' if k=='audio' else 'search_image']; d=json.loads(get(b+'?'+urllib.parse.urlencode({'q':q,'page_size':24})));return [{'id':x.get('id'),'title':x.get('title'),'provider':'Openverse','type':k,'license':x.get('license'),'license_url':x.get('license_url'),'creator':x.get('creator'),'source':x.get('foreign_landing_url') or x.get('url'),'preview':x.get('thumbnail') or x.get('url'),'download':x.get('url')} for x in d.get('results',[])]
 if p=='polyhaven':
  d=json.loads(get(PROVIDERS[p]['assets'])); q=q.lower(); o=[]
  for i,x in d.items():
   if not q or q in (i+' '+str(x)).lower():
    files=json.loads(get(PROVIDERS[p]['files']+urllib.parse.quote(i,safe='')));u=first_url(files);o.append({'id':i,'title':x.get('name',i),'provider':'Poly Haven','type':{0:'hdri',1:'texture',2:'model'}.get(x.get('type'),'asset'),'license':'CC0','license_url':'https://polyhaven.com/license','source':'https://polyhaven.com/a/'+i,'preview':x.get('thumbnail_url'),'download':u})
   if len(o)>=24:break
  return o
 if p=='kenney':return [{'id':'kenney-catalog','title':'Kenney official CC0 asset catalog','provider':'Kenney','type':'catalog','license':'CC0','license_url':'https://kenney.nl/support','source':'https://kenney.nl/assets','preview':None,'download':None}]
 return []
class H(http.server.BaseHTTPRequestHandler):
 def j(self,o,c=200):
  b=json.dumps(o).encode();self.send_response(c);self.send_header('Content-Type','application/json');self.send_header('Access-Control-Allow-Origin','*');self.send_header('Content-Length',str(len(b)));self.end_headers();self.wfile.write(b)
 def do_OPTIONS(self):self.send_response(204);self.send_header('Access-Control-Allow-Origin','*');self.send_header('Access-Control-Allow-Methods','GET,POST,OPTIONS');self.send_header('Access-Control-Allow-Headers','Content-Type');self.end_headers()
 def do_GET(self):
  p=urllib.parse.urlparse(self.path)
  if p.path in ('/','/index.html'):return self.file(WEB/'index.html','text/html')
  if p.path.startswith('/static/'):return self.file(WEB/p.path[8:])
  if p.path=='/api/v1/assets/providers':return self.j(PROVIDERS)
  if p.path=='/api/v1/assets/manifest':return self.j(mf())
  if p.path=='/api/v1/assets/search':
   q=urllib.parse.parse_qs(p.query);pr=q.get('provider',['openverse'])[0];term=q.get('q',[''])[0];kind=q.get('type',['image'])[0]
   try:return self.j({'results':search(pr,term,kind)})
   except Exception as e:return self.j({'error':type(e).__name__},502)
  return self.j({'error':'not_found'},404)
 def do_POST(self):
  if self.path!='/api/v1/assets/download':return self.j({'error':'not_found'},404)
  try:d=json.loads(self.rfile.read(int(self.headers.get('Content-Length','0'))));pr=d['provider'];u=d['download'];name=pathlib.Path(urlparse(u).path).name or d.get('id','asset')+'.bin'
  except:return self.j({'error':'invalid_json'},400)
  if pr not in PROVIDERS or not ok(u,pr):return self.j({'error':'download_host_not_allowed'},403)
  if pathlib.Path(name).suffix.lower() not in SAFE_EXT:return self.j({'error':'file_type_not_allowed'},415)
  try:data=get(u)
  except Exception as e:return self.j({'error':'download_failed','detail':type(e).__name__},502)
  if len(data)>250*1024*1024:return self.j({'error':'file_too_large'},413)
  sha=hashlib.sha256(data).hexdigest();safe=''.join(c for c in name if c.isalnum() or c in '._-')[:160] or 'asset.bin';dest=STORE/safe;dest.write_bytes(data)
  import datetime;rec={'file':str(dest.relative_to(STORE)),'sha256':sha,'bytes':len(data),'provider':pr,'source':d.get('source'),'license':d.get('license'),'license_url':d.get('license_url'),'downloaded_at':datetime.datetime.now(datetime.timezone.utc).isoformat()};m=mf();m.append(rec);save(m);return self.j(rec)
 def file(self,p,c=None):
  try:b=p.read_bytes();self.send_response(200);self.send_header('Content-Type',c or mimetypes.guess_type(str(p))[0] or 'application/octet-stream');self.send_header('Content-Length',str(len(b)));self.end_headers();self.wfile.write(b)
  except:self.j({'error':'not_found'},404)
 def log_message(self,*a):pass
print(f'BizXtreme Asset Browser: http://127.0.0.1:{PORT}')
http.server.ThreadingHTTPServer(('127.0.0.1',PORT),H).serve_forever()
