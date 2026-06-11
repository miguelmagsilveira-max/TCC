function toggleTheme() {
  const isDark = document.documentElement.classList.toggle('dark');
  localStorage.setItem('tema', isDark ? 'dark' : 'light');
  _syncIcons(isDark);
}

function _syncIcons(isDark) {
  const sun  = document.getElementById('icon-sun');
  const moon = document.getElementById('icon-moon');
  if (sun)  sun.style.display  = isDark ? 'none'  : 'block';
  if (moon) moon.style.display = isDark ? 'block' : 'none';
}

// Aplica o tema salvo imediatamente (executa no <head>) para evitar flash
(function () {
  const saved       = localStorage.getItem('tema');
  const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  if (saved === 'dark' || (!saved && prefersDark)) {
    document.documentElement.classList.add('dark');
  }
}());

// Sincroniza os ícones após o DOM estar pronto
document.addEventListener('DOMContentLoaded', function () {
  _syncIcons(document.documentElement.classList.contains('dark'));
});
