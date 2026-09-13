import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../..');
const args = process.argv.slice(2);
const py = process.platform === 'win32' ? 'python' : 'python3';
const result = spawnSync(py, [path.join(root, 'launcher/python/main.py'), ...args], { stdio: 'inherit' });
if (result.error) {
  console.error(`Python runtime unavailable: ${result.error.message}`);
  process.exit(1);
}
process.exit(result.status ?? 1);
