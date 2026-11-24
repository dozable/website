/* Theme button. The inline script in <head> applies a saved choice before paint and
   adds html.js-theme, which is what shows this button. With JavaScript off there is
   no saved choice and no button: the page follows the system. */
(function () {
  'use strict';
  var KEY = 'doz-theme';
  var root = document.documentElement;

  function systemDark() {
    return window.matchMedia && matchMedia('(prefers-color-scheme: dark)').matches;
  }
  function theme() {
    var t = root.getAttribute('data-theme');
    if (t === 'dark' || t === 'light') return t;
    return systemDark() ? 'dark' : 'light';
  }
  function paint(btn, mode) {
    var dark = mode === 'dark';
    btn.setAttribute('aria-pressed', dark ? 'true' : 'false');
    btn.setAttribute('aria-label', dark ? 'Switch to light mode' : 'Switch to dark mode');
    var c = dark ? '#000000' : '#ffffff';
    var metas = document.querySelectorAll('meta[name="theme-color"]');
    for (var i = 0; i < metas.length; i++) metas[i].setAttribute('content', c);
  }
  function init() {
    var btn = document.querySelector('.theme-toggle');
    if (!btn) return;
    paint(btn, theme());
    btn.addEventListener('click', function () {
      var next = theme() === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      try { localStorage.setItem(KEY, next); } catch (e) {}
      paint(btn, next);
    });
    if (window.matchMedia) {
      var mq = matchMedia('(prefers-color-scheme: dark)');
      var follow = function () { if (!root.getAttribute('data-theme')) paint(btn, theme()); };
      if (mq.addEventListener) mq.addEventListener('change', follow);
      else if (mq.addListener) mq.addListener(follow);
    }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
