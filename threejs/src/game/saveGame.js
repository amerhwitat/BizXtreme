const DB_NAME='BizXtremeSaveDB';
const STORE='saves';
const KEY='current';

function openDb(){return new Promise((resolve,reject)=>{const r=indexedDB.open(DB_NAME,1);r.onupgradeneeded=()=>r.result.createObjectStore(STORE);r.onsuccess=()=>resolve(r.result);r.onerror=()=>reject(r.error)});}

export async function saveGame(snapshot){
  const value={...snapshot,savedAt:new Date().toISOString(),schema:1};
  // Immediate localStorage mirror makes the save resilient during page shutdown.
  localStorage.setItem('bizxtreme.save',JSON.stringify(value));
  try{const db=await openDb();await new Promise((resolve,reject)=>{const tx=db.transaction(STORE,'readwrite');tx.objectStore(STORE).put(value,KEY);tx.oncomplete=resolve;tx.onerror=()=>reject(tx.error)});db.close();}
  catch{}
  return value;
}

export async function loadGame(){
  try{const db=await openDb();const value=await new Promise((resolve,reject)=>{const tx=db.transaction(STORE,'readonly');const r=tx.objectStore(STORE).get(KEY);r.onsuccess=()=>resolve(r.result||null);r.onerror=()=>reject(r.error)});db.close();if(value)return value;}
  catch{}
  try{return JSON.parse(localStorage.getItem('bizxtreme.save')||'null')}catch{return null}
}

export function saveHallOfFame(entry){
  const list=JSON.parse(localStorage.getItem('bizxtreme.hallOfFame')||'[]');
  list.push({...entry,recordedAt:new Date().toISOString()});
  list.sort((a,b)=>(b.score||0)-(a.score||0));
  localStorage.setItem('bizxtreme.hallOfFame',JSON.stringify(list.slice(0,100)));
  return list.slice(0,100);
}

export function getHallOfFame(){return JSON.parse(localStorage.getItem('bizxtreme.hallOfFame')||'[]');}
