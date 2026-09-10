const DIRECTORY_KEY='bizxtreme.peerDirectoryUrl';
const DEFAULT_DIRECTORY='';

// Privacy boundary: the client never stores or publishes raw peer IP addresses.
// Discovery uses an opt-in directory of pseudonymous peer IDs and capabilities.
export function getDirectoryUrl(){return localStorage.getItem(DIRECTORY_KEY)||DEFAULT_DIRECTORY;}
export function setDirectoryUrl(url){if(url)localStorage.setItem(DIRECTORY_KEY,url);else localStorage.removeItem(DIRECTORY_KEY);}

export async function searchConnectedUsers(query=''){
  const url=getDirectoryUrl();
  if(!url)return [];
  const endpoint=new URL(url,window.location.href);
  endpoint.searchParams.set('q',query);
  const response=await fetch(endpoint,{headers:{Accept:'application/json'}});
  if(!response.ok)throw new Error(`peer directory: HTTP ${response.status}`);
  const data=await response.json();
  return Array.isArray(data.users)?data.users.map(normalizePeer):[];
}

export function normalizePeer(peer){return{
  peerId:String(peer.peerId||''),
  displayName:String(peer.displayName||'Anonymous Explorer'),
  lastSeen:peer.lastSeen||null,
  capabilities:Array.isArray(peer.capabilities)?peer.capabilities.map(String):[],
  networkHint:String(peer.networkHint||'relay-or-direct')
};}

export function createPeerAnnouncement(profile){return{
  protocol:'bizxtreme-peer-directory-v1',
  peerId:String(profile.peerId),
  displayName:String(profile.displayName||'Explorer'),
  capabilities:Array.isArray(profile.capabilities)?profile.capabilities:[],
  online:true
};}
