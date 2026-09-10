import * as THREE from 'three';

export function create3DProgressBar({width=4,height=.34,depth=.16,value=.72}={}){
  const group=new THREE.Group();
  const initial=THREE.MathUtils.clamp(value,0,1);
  const shell=new THREE.Mesh(new THREE.BoxGeometry(width,height,depth),new THREE.MeshStandardMaterial({color:0x081525,metalness:.65,roughness:.28,transparent:true,opacity:.94}));
  group.add(shell);
  const fill=new THREE.Mesh(new THREE.BoxGeometry(width*Math.max(initial,.01),height*.62,depth*1.08),new THREE.MeshStandardMaterial({color:0x43d7ff,emissive:0x0d5c86,emissiveIntensity:1.6,metalness:.35,roughness:.2}));
  fill.position.x=-width*(1-initial)/2; group.add(fill);
  const glow=new THREE.Mesh(new THREE.BoxGeometry(width*Math.max(initial,.01),height*.22,depth*1.25),new THREE.MeshBasicMaterial({color:0x9eeeff,transparent:true,opacity:.65}));
  glow.position.set(fill.position.x,0,depth*.62); group.add(glow);
  group.userData.value=initial;
  group.userData.setValue=(next)=>{const p=THREE.MathUtils.clamp(next,0,1);const scale=Math.max(p,.01)/Math.max(initial,.01);fill.scale.x=scale;glow.scale.x=scale;fill.position.x=-width*(1-p)/2;glow.position.x=fill.position.x;group.userData.value=p};
  group.userData.tick=(time)=>{const pulse=1+Math.sin(time*3.2)*.035;glow.scale.y=pulse;glow.material.opacity=.48+Math.sin(time*2.4)*.12};
  return group;
}
