import { spawnSync } from 'node:child_process';
import { resolve } from 'node:path';
const root=resolve(import.meta.dirname,'../..');
const r=spawnSync(process.platform==='win32'?'python':'python3',[resolve(root,'launcher/python/main.py'),...process.argv.slice(2)],{stdio:'inherit'});
process.exit(r.status??1);
