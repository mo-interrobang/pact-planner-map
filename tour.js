/* Guided tour for the planner map. Self-contained, no dependencies.
   Load with <script src="tour.js"></script> just before </body>. */
(function () {
  var STEPS = [
    { title: 'Welcome to the map',
      text: 'This 2-minute tour shows you how to find your community, read what you see, and turn on extra layers. You can leave any time with Skip.' },
    { el: '#search-box', title: 'Start with search',
      text: 'Type a city, township, village, planner, or planning firm here. The list and the map narrow as you type.' },
    { el: '#muni-list-container', title: 'Pick a result',
      text: 'We searched "Allen Park" for you. Click any name in this list to zoom the map to it and open its details card.',
      before: function () { setSearch('Allen Park'); } },
    { el: '.leaflet-popup', title: 'Read the details card',
      text: 'The card shows who does the planning, which firm, any flags, data center case notes, research notes, and links to meeting documents when we have them.',
      before: function () {
        var item = document.querySelector('.muni-item');
        if (item) item.click();
      }, wait: 900 },
    { el: '#stats-bar', title: 'The counters',
      text: 'How many communities match what is showing now: total mapped, active CWA clients, data center cases, DTE builds, and battery storage (BESS) cases. They change as you filter.',
      before: function () { if (window.map && map.closePopup) map.closePopup(); setSearch(''); } },
    { el: '#filters', title: 'Filter by planning firm',
      text: 'Check or uncheck firms to show or hide the communities they serve. "All" and "None" are shortcuts.' },
    { el: '#sort-box', title: 'Sort the list',
      text: 'Sort alphabetically, or put data center cases or CWA communities at the top.' },
    { el: '#legend', title: 'What the colors and icons mean',
      text: 'Dot color = planning firm. Red outline = active CWA client. ⚡ = data center case. 🔌 = DTE build. 🔋 = battery storage case. Gray = planner not confirmed yet.' },
    { el: '#layers-panel', title: 'Add layers',
      text: 'Turn on power lines, substations, gas pipelines, proposed data center sites, and watch areas. They start off so the map stays readable. Being near a power line or on a watch list is not evidence of a project.' },
    { el: '#gap-badge', title: 'Data gaps',
      text: 'Communities where we have not confirmed the planner yet. Click it to flash them on the map. Know the answer? Send a correction.' },
    { el: '#sidebar-footer', title: 'More tools and pages',
      text: 'Export the full list as a spreadsheet, show CWA communities only, or open the deeper pages: Oakland County, CWA Timeline, connections, and the Developer Tracker.' },
    { title: 'Before you share anything',
      text: 'This is a research tool built from public records, not a verified directory. Check important details against your community’s own agendas, packets, and minutes. You can replay this tour any time with the "? Tour" button.' }
  ];

  var css = '' +
    '#pt-shade{position:fixed;inset:0;z-index:10000;background:rgba(2,6,23,.6)}' +
    '#pt-ring{position:fixed;z-index:10001;border:2px solid #60a5fa;border-radius:8px;box-shadow:0 0 0 9999px rgba(2,6,23,.6);transition:all .25s ease;pointer-events:none}' +
    '#pt-tip{position:fixed;z-index:10002;width:300px;max-width:calc(100vw - 24px);background:#0f172a;color:#cbd5e1;border:1px solid #334155;border-radius:10px;padding:14px 16px 12px;font:14px/1.5 -apple-system,"Segoe UI",Roboto,Arial,sans-serif;box-shadow:0 10px 30px rgba(0,0,0,.5);transition:top .25s ease,left .25s ease}' +
    '#pt-tip h3{margin:0 0 6px;color:#f1f5f9;font-size:15px}' +
    '#pt-tip p{margin:0 0 12px}' +
    '#pt-tip .pt-row{display:flex;align-items:center;gap:6px}' +
    '#pt-tip .pt-count{flex:1;font-size:11px;color:#64748b}' +
    '#pt-tip button{font:600 12px Arial,sans-serif;border-radius:5px;padding:6px 12px;cursor:pointer;border:1px solid #334155;background:#1e293b;color:#cbd5e1}' +
    '#pt-tip button.pt-next{background:#1d4ed8;border-color:#1d4ed8;color:#fff}' +
    '#pt-tip .pt-skip{background:none;border:none;color:#64748b;padding:6px 4px}' +
    '#pt-launch{position:fixed;left:272px;bottom:28px;z-index:9000;font:600 12px Arial,sans-serif;background:#1d4ed8;color:#fff;border:none;border-radius:16px;padding:7px 14px;cursor:pointer;box-shadow:0 2px 8px rgba(0,0,0,.4)}' +
    '#pt-offer{position:fixed;left:50%;top:18px;transform:translateX(-50%);z-index:9500;background:#0f172a;border:1px solid #334155;color:#cbd5e1;border-radius:10px;padding:10px 14px;font:13px Arial,sans-serif;display:flex;gap:10px;align-items:center;box-shadow:0 6px 20px rgba(0,0,0,.5)}' +
    '#pt-offer button{font:600 12px Arial,sans-serif;border-radius:5px;padding:5px 10px;cursor:pointer;border:1px solid #334155;background:#1e293b;color:#cbd5e1}' +
    '#pt-offer button.go{background:#1d4ed8;border-color:#1d4ed8;color:#fff}';
  var st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);

  var i = 0, ring, tip, shade;

  function setSearch(v) {
    var s = document.getElementById('search-input');
    if (!s) return;
    s.value = v;
    s.dispatchEvent(new Event('input', { bubbles: true }));
  }

  function start() {
    end();
    var offer = document.getElementById('pt-offer'); if (offer) offer.remove();
    i = 0;
    shade = document.createElement('div'); shade.id = 'pt-shade';
    ring = document.createElement('div'); ring.id = 'pt-ring';
    tip = document.createElement('div'); tip.id = 'pt-tip';
    document.body.appendChild(shade); document.body.appendChild(ring); document.body.appendChild(tip);
    document.addEventListener('keydown', onKey);
    window.addEventListener('resize', place);
    show();
  }

  function end() {
    [shade, ring, tip].forEach(function (n) { if (n && n.parentNode) n.parentNode.removeChild(n); });
    shade = ring = tip = null;
    document.removeEventListener('keydown', onKey);
    window.removeEventListener('resize', place);
  }

  function finish() { end(); setSearch(''); try { localStorage.setItem('pt-tour-seen', '1'); } catch (e) {} }

  function onKey(e) {
    if (e.key === 'Escape') finish();
    else if (e.key === 'ArrowRight') go(1);
    else if (e.key === 'ArrowLeft') go(-1);
  }

  function go(d) {
    var n = i + d;
    if (n < 0) return;
    if (n >= STEPS.length) { finish(); return; }
    i = n; show();
  }

  function show() {
    var s = STEPS[i];
    if (s.before) s.before();
    tip.innerHTML = '<h3>' + s.title + '</h3><p>' + s.text + '</p>' +
      '<div class="pt-row"><span class="pt-count">' + (i + 1) + ' of ' + STEPS.length + '</span>' +
      '<button class="pt-skip">Skip</button>' +
      (i > 0 ? '<button class="pt-back">Back</button>' : '') +
      '<button class="pt-next">' + (i === STEPS.length - 1 ? 'Done' : 'Next') + '</button></div>';
    tip.querySelector('.pt-skip').onclick = finish;
    tip.querySelector('.pt-next').onclick = function () { go(1); };
    var b = tip.querySelector('.pt-back'); if (b) b.onclick = function () { go(-1); };
    setTimeout(place, s.wait || 60);
  }

  function place() {
    if (!tip) return;
    var s = STEPS[i];
    var el = s.el ? document.querySelector(s.el) : null;
    var vw = window.innerWidth, vh = window.innerHeight;
    var tw = tip.offsetWidth, th = tip.offsetHeight;
    if (!el || !el.getBoundingClientRect().width) {
      ring.style.display = 'none'; shade.style.display = 'block';
      tip.style.left = (vw - tw) / 2 + 'px'; tip.style.top = (vh - th) / 2 + 'px';
      return;
    }
    shade.style.display = 'none'; ring.style.display = 'block';
    var r = el.getBoundingClientRect(), pad = 6;
    ring.style.left = (r.left - pad) + 'px'; ring.style.top = (r.top - pad) + 'px';
    ring.style.width = (r.width + pad * 2) + 'px'; ring.style.height = (r.height + pad * 2) + 'px';
    var gap = 16, left, top;
    if (r.right + gap + tw < vw) { left = r.right + gap; top = r.top; }
    else if (r.left - gap - tw > 0) { left = r.left - gap - tw; top = r.top; }
    else if (r.bottom + gap + th < vh) { left = r.left; top = r.bottom + gap; }
    else { left = r.left; top = r.top - gap - th; }
    left = Math.max(12, Math.min(left, vw - tw - 12));
    top = Math.max(12, Math.min(top, vh - th - 12));
    tip.style.left = left + 'px'; tip.style.top = top + 'px';
  }

  // Replay button
  var launch = document.createElement('button');
  launch.id = 'pt-launch'; launch.textContent = '? Tour'; launch.title = 'Take the guided tour';
  launch.onclick = start;
  document.body.appendChild(launch);

  // First-visit offer, shown after the disclaimer is dismissed
  function offer() {
    var seen = false; try { seen = localStorage.getItem('pt-tour-seen') === '1'; } catch (e) {}
    if (seen || document.getElementById('pt-offer')) return;
    var o = document.createElement('div'); o.id = 'pt-offer';
    o.innerHTML = '<span>New here? Take a 2-minute tour.</span><button class="go">Start tour</button><button class="no">No thanks</button>';
    o.querySelector('.go').onclick = start;
    o.querySelector('.no').onclick = function () { o.remove(); try { localStorage.setItem('pt-tour-seen', '1'); } catch (e) {} };
    document.body.appendChild(o);
  }
  var dc = document.getElementById('disclaimer-close');
  if (dc) dc.addEventListener('click', function () { setTimeout(offer, 300); });
  else offer();

  window.startMapTour = start;
})();
