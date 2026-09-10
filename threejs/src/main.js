import * as THREE from 'three';
import { create3DProgressBar } from './game/progress3d.js';
import { progressTracks, story } from './game/content.js';
import { gameArtDirection } from './game/libraryAssets.js';

const app=document.querySelector('#app');
const scene=new THREE.Scene();
scene.fog=new THREE.Fog(0x050812,18,75);
const camera=new THREE.PerspectiveCamera(55,innerWidth/innerHeight,.1,200);
camera.position.set(0,8,15);
const renderer=new THREE.WebGLRenderer({antialias:true});
renderer.setPixelRatio(Math.min(devicePixelRatio,2));
renderer.setSize(innerWidth,innerHeight); renderer.shadowMap.enabled=true; app.appendChild(renderer.domElement);

scene.add(new THREE.HemisphereLight(0x9fb8ff,0x182015,1.7));
const sun=new THREE.DirectionalLight(0xffffff,2.2); sun.position.set(8,16,5); sun.castShadow=true; scene.add(sun);
const ground=new THREE.Mesh(new THREE.PlaneGeometry(120,120),new THREE.MeshStandardMaterial({color:0x16241c,roughness:1})); ground.rotation.x=-Math.PI/2; ground.receiveShadow=true; scene.add(ground);

const frontier=new THREE.Group(); scene.add(frontier);
for(let i=0;i<34;i++){const h=1+Math.random()*5; const m=new THREE.Mesh(new THREE.BoxGeometry(.7+Math.random()*1.5,h,.7+Math.random()*1.5),new THREE.MeshStandardMaterial({color:0x26394a,roughness:.8})); m.position.set((Math.random()-.5)*48,h/2,(Math.random()-.5)*42);m.castShadow=true;frontier.add(m)}
const beacon=new THREE.Mesh(new THREE.CylinderGeometry(.45,.8,7,16),new THREE.MeshStandardMaterial({color:0x5aa8ff,emissive:0x123c80,emissiveIntensity:2})); beacon.position.set(0,3.5,-8); beacon.castShadow=true; scene.add(beacon);
const ring=new THREE.Mesh(new THREE.TorusGeometry(2.5,.08,12,64),new THREE.MeshBasicMaterial({color:0x67c8ff})); ring.rotation.x=Math.PI/2; ring.position.set(0,.15,-8); scene.add(ring);

const hud=new THREE.Group(); hud.position.set(-5.3,5.3,-8); scene.add(hud);
const bars=Object.values(progressTracks).map((track,i)=>{const bar=create3DProgressBar({width:3.7,height:.28,depth:.14,value:track.value});bar.position.y=-i*.72;hud.add(bar);return bar});

const state={screen:'play',starterGranted:true,inventory:['Frontier Outfit','Explorer Tool','Rookie Runner','Frontier Map','Supply Crate x3','Inventory +5']};
const toast=document.querySelector('#toast');
function notify(text){toast.textContent=text;toast.classList.add('show');clearTimeout(notify.t);notify.t=setTimeout(()=>toast.classList.remove('show'),2200)}
const messages={play:`Expedition started — ${story[0].title}.`,continue:`Continuing: ${story[5].title}.`,missions:'Missions: restore the beacon and decode the broken signal.',events:'Live Event: Black Aurora is approaching.',inventory:'Starter inventory loaded: '+state.inventory.length+' items.',marketplace:'Marketplace opened — purchases are optional.',wallet:'Wallet center: connect, receive, send, backup.',settings:'Settings: graphics, controls, accessibility.'};
document.querySelectorAll('[data-action]').forEach(b=>b.addEventListener('click',()=>{state.screen=b.dataset.action;notify(messages[state.screen])}));

addEventListener('resize',()=>{camera.aspect=innerWidth/innerHeight;camera.updateProjectionMatrix();renderer.setSize(innerWidth,innerHeight)});
let t=0; renderer.setAnimationLoop(time=>{t=time*.001;ring.rotation.z=t*.35;beacon.position.y=3.5+Math.sin(t*2)*.15;bars.forEach((bar,i)=>bar.userData.tick(t+i*.3));camera.position.x=Math.sin(t*.08)*1.8;camera.lookAt(0,2,-5);renderer.render(scene,camera)});
app.dataset.artPalette=gameArtDirection.palette.join(',');
