import { getHallOfFame, loadGame, saveGame, saveHallOfFame } from './saveGame.js';
import { searchConnectedUsers } from './peerDirectory.js';

export async function createGameDashboard(root,{getState,setState,notify}){
  const panel=document.createElement('section');
  panel.className='game-dashboard panel';
  panel.innerHTML=`<div class="dash-head"><div><strong>FRONTIER COMMAND</strong><small>Live Game Dashboard</small></div><button class="dash-close">×</button></div><div class="kpi-grid"></div><div class="dash-grid"><div><h4>Resume / Save</h4><button data-dash="save">Save game</button><button data-dash="resume">Resume latest</button><span class="save-status">No save loaded</span></div><div><h4>Hall of Fame</h4><div class="hall"></div></div><div><h4>Connected Explorers</h4><input class="peer-search" placeholder="Search opted-in users"><button data-dash="peers">Search</button><div class="peers"></div></div></div>`;
  root.appendChild(panel);
  panel.querySelector('.dash-close').onclick=()=>panel.remove();
  const kpis=panel.querySelector('.kpi-grid');
  function render(){const s=getState();kpis.innerHTML=[['Score',s.score||0],['XP',s.xp||0],['Expedition',Math.round((s.expedition||0)*100)+'%'],['Play Time',Math.round((s.playTime||0)/60)+'m'],['Peers',s.peerCount||0],['Best Rank',s.rank||'—']].map(([a,b])=>`<div class="kpi"><span>${a}</span><b>${b}</b></div>`).join('');panel.querySelector('.hall').innerHTML=getHallOfFame().slice(0,10).map((e,i)=>`<div class="hall-row"><b>#${i+1}</b><span>${escapeHtml(e.player||'Explorer')}</span><strong>${e.score||0}</strong></div>`).join('')||'<small>No records yet.</small>';}
  panel.querySelector('[data-dash="save"]').onclick=async()=>{const value=await saveGame(getState());panel.querySelector('.save-status').textContent='Saved '+new Date(value.savedAt).toLocaleString();notify('Game saved for resume.');render();};
  panel.querySelector('[data-dash="resume"]').onclick=async()=>{const saved=await loadGame();if(!saved){notify('No saved game found.');return;}setState(saved);panel.querySelector('.save-status').textContent='Resumed '+new Date(saved.savedAt).toLocaleString();notify('Saved expedition resumed.');render();};
  panel.querySelector('[data-dash="peers"]').onclick=async()=>{const q=panel.querySelector('.peer-search').value.trim();const box=panel.querySelector('.peers');try{const peers=await searchConnectedUsers(q);box.innerHTML=peers.map(p=>`<div class="peer"><span>${escapeHtml(p.displayName)}</span><small>${escapeHtml(p.networkHint)}</small></div>`).join('')||'<small>No opted-in explorers found.</small>';}catch{box.innerHTML='<small>Peer directory unavailable; local/offline mode remains active.</small>';}};
  render();return panel;
}

export function recordScore(state,player='Explorer'){const records=saveHallOfFame({player,score:state.score||0,xp:state.xp||0,chapter:state.chapter||'chapter_01'});return records;}
function escapeHtml(s){return String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
