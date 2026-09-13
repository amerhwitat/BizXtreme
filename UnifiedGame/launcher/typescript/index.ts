import { spawnSync } from 'node:child_process';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const root = resolve(here, '../..');
const python = process.platform === 'win32' ? 'python' : 'python3';
const launcher = resolve(root, 'launcher/python/main.py');

const result = spawnSync(python, [launcher, ...process.argv.slice(2)], {
  stdio: 'inherit',
});

if (result.error) {
  console.error(`Unable to start Python runtime: ${result.error.message}`);
  process.exit(1);
}

process.exit(result.status ?? 1);
