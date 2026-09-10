export function startGame(options = {}) {
  const title = options.title ?? 'BizXtreme';
  const mode = options.mode ?? 'default';
  return { title, mode, status: 'started', runtime: 'node' };
}

export function main(argv = process.argv.slice(2)) {
  const result = startGame({ mode: argv[0] ?? 'default' });
  console.log(`${result.title} game starting (${result.mode})`);
  return result;
}

if (import.meta.url === `file://${process.argv[1]}`) main();
