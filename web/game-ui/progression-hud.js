export function renderProgressionHud(root, state) {
  if (!root) return;
  root.innerHTML = '';
  const panel = document.createElement('section');
  panel.className = 'game-hud progression-hud';
  panel.setAttribute('aria-label', 'Game status');
  panel.innerHTML = `<strong>${escapeHtml(state.name || 'Player')}</strong> · Level ${Number(state.level || 0)} · ${escapeHtml(state.status || 'new')} · Score ${Number(state.score || 0)}`;
  root.appendChild(panel);
}
function escapeHtml(value) { return String(value).replace(/[&<>\"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c])); }
