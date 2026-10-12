/* PVG engine — shared game engine for the Public Video Games Database.
   Property of Justin Addam Higgins (JAH). Openly licensed (MIT) with the database.
   Provides: canvas scaling, game loop, unified input (keyboard incl. numpad,
   on-screen D-pad + buttons, swipe, tap, drag), and tiny WebAudio beeps.
   Games register via PVG.register(slug, def) and run via PVG.play(canvasId, slug). */
(function(){
'use strict';
var PVG = window.PVG = {};
var REG = {};
PVG.register = function(slug, def){ REG[slug] = def; };
PVG.list = function(){ return Object.keys(REG); };

/* ---------- input ---------- */
var keys = {};          // normalized key -> bool
PVG.keys = keys;
var pressed = {};       // edge-triggered: set true on keydown, game clears each frame
PVG.pressed = pressed;

var KEYMAP = {
  ArrowLeft:'left', ArrowRight:'right', ArrowUp:'up', ArrowDown:'down',
  a:'left', d:'right', w:'up', s:'down',
  ' ':'a', z:'a', j:'a', x:'b', k:'b',
  Enter:'start', Shift:'select',
  Numpad4:'left', Numpad6:'right', Numpad8:'up', Numpad2:'down',
  Numpad5:'a', Numpad0:'b', NumpadDecimal:'b', NumpadEnter:'start',
  Numpad1:'1', Numpad2b:'2', Numpad3:'3', Numpad7:'4'
};
function normKey(e){
  if(e.code && KEYMAP[e.code]) return KEYMAP[e.code];
  if(e.code && e.code.indexOf('Numpad')===0 && /^[0-9]$/.test(e.code.slice(6))) return e.code.slice(6);
  if(e.key && e.key.length===1){
    var k = e.key.toLowerCase();
    if(KEYMAP[k]) return KEYMAP[k];
    if(/^[0-9]$/.test(k)) return k;
  }
  return null;
}
window.addEventListener('keydown', function(e){
  var k = normKey(e);
  if(k){
    if(['left','right','up','down',' '].indexOf(e.key)>=0 || k==='a' && e.key===' ') e.preventDefault();
    if(['left','right','up','down'].indexOf(k)>=0) e.preventDefault();
    if(!keys[k]) pressed[k] = true;
    keys[k] = true;
  }
});
window.addEventListener('keyup', function(e){
  var k = normKey(e);
  if(k) keys[k] = false;
});

/* tap / swipe / drag on canvas */
var tapQ = [], swipeQ = [], dragX = null;
PVG.tapQ = tapQ; PVG.swipeQ = swipeQ;
Object.defineProperty(PVG, 'dragX', { get:function(){ return dragX; } });
function canvasPos(canvas, cx, cy){
  var r = canvas.getBoundingClientRect();
  return { x:(cx-r.left)*canvas.width/r.width, y:(cy-r.top)*canvas.height/r.height };
}
function wirePointer(canvas, cfg){
  var sx=null, sy=null, dragging=false;
  function pos(e){
    var t = e.touches ? e.touches[0] : e;
    return canvasPos(canvas, t.clientX, t.clientY);
  }
  canvas.addEventListener('touchstart', function(e){
    e.preventDefault();
    var p = pos(e); sx=p.x; sy=p.y; dragging=true;
    if(cfg.tap) tapQ.push(p);
    if(cfg.dragx) dragX = p.x;
  }, {passive:false});
  canvas.addEventListener('touchmove', function(e){
    e.preventDefault();
    if(cfg.dragx && dragging) dragX = pos(e).x;
  }, {passive:false});
  canvas.addEventListener('touchend', function(e){
    e.preventDefault();
    if(cfg.swipe && sx!==null){
      var t = e.changedTouches[0], p = canvasPos(canvas, t.clientX, t.clientY);
      var dx=p.x-sx, dy=p.y-sy;
      if(Math.abs(dx)>24 || Math.abs(dy)>24)
        swipeQ.push(Math.abs(dx)>Math.abs(dy) ? (dx>0?'right':'left') : (dy>0?'down':'up'));
    }
    dragging=false; sx=null; dragX=null;
  }, {passive:false});
  canvas.addEventListener('mousedown', function(e){
    var p = pos(e);
    if(cfg.tap) tapQ.push(p);
    if(cfg.dragx){ dragging=true; dragX=p.x; }
    sx=p.x; sy=p.y;
  });
  canvas.addEventListener('mousemove', function(e){
    if(cfg.dragx && dragging) dragX = pos(e).x;
  });
  canvas.addEventListener('mouseup', function(e){
    if(cfg.swipe && sx!==null){
      var p = pos(e), dx=p.x-sx, dy=p.y-sy;
      if(Math.abs(dx)>24 || Math.abs(dy)>24)
        swipeQ.push(Math.abs(dx)>Math.abs(dy) ? (dx>0?'right':'left') : (dy>0?'down':'up'));
    }
    dragging=false; sx=null; dragX=null;
  });
}

/* ---------- audio ---------- */
var AC = null;
PVG.beep = function(freq, dur, type){
  try{
    if(!AC) AC = new (window.AudioContext||window.webkitAudioContext)();
    var o = AC.createOscillator(), g = AC.createGain();
    o.type = type||'square'; o.frequency.value = freq||440;
    g.gain.setValueAtTime(0.06, AC.currentTime);
    g.gain.exponentialRampToValueAtTime(0.0001, AC.currentTime + (dur||0.08));
    o.connect(g); g.connect(AC.destination);
    o.start(); o.stop(AC.currentTime + (dur||0.08));
  }catch(e){}
};

/* ---------- touch controls overlay ---------- */
function buildPad(host, cfg){
  var pad = document.createElement('div');
  pad.className = 'pvg-pad';
  var html = '';
  if(cfg.dpad){
    html += '<div class="pvg-dpad">'
      + '<button data-k="up" aria-label="up">▲</button>'
      + '<button data-k="left" aria-label="left">◀</button>'
      + '<button data-k="down" aria-label="down">▼</button>'
      + '<button data-k="right" aria-label="right">▶</button></div>';
  }
  if(cfg.buttons && cfg.buttons.length){
    html += '<div class="pvg-ab">';
    cfg.buttons.forEach(function(b){
      html += '<button data-k="'+b.k.toLowerCase()+'">'+b.label+'</button>';
    });
    html += '</div>';
  }
  pad.innerHTML = html;
  host.appendChild(pad);
  pad.querySelectorAll('button').forEach(function(btn){
    var k = btn.getAttribute('data-k');
    function on(e){ e.preventDefault(); if(!keys[k]) pressed[k]=true; keys[k]=true; btn.classList.add('on'); }
    function off(e){ e.preventDefault(); keys[k]=false; btn.classList.remove('on'); }
    btn.addEventListener('touchstart', on, {passive:false});
    btn.addEventListener('touchend', off, {passive:false});
    btn.addEventListener('touchcancel', off, {passive:false});
    btn.addEventListener('mousedown', on);
    btn.addEventListener('mouseup', off);
    btn.addEventListener('mouseleave', function(){ keys[k]=false; btn.classList.remove('on'); });
  });
  return pad;
}

/* ---------- main ---------- */
PVG.play = function(canvasId, slug){
  var def = REG[slug];
  var canvas = document.getElementById(canvasId);
  if(!def || !canvas) return null;
  var W = def.W||400, H = def.H||560;
  canvas.width = W; canvas.height = H;
  var ctx = canvas.getContext('2d');
  var host = canvas.parentElement;
  var cfg = def.controls || {};
  wirePointer(canvas, cfg);
  var pad = null;
  var isTouch = ('ontouchstart' in window) || (navigator.maxTouchPoints>0);
  if((cfg.dpad || cfg.buttons) && isTouch) pad = buildPad(host, cfg);

  var api = {
    W:W, H:H, ctx:ctx, canvas:canvas,
    keys:keys, pressed:pressed, tapQ:tapQ, swipeQ:swipeQ,
    beep:PVG.beep,
    get dragX(){ return dragX; },
    clearTaps:function(){ tapQ.length=0; swipeQ.length=0; },
    text:function(s,x,y,size,color,align){
      ctx.fillStyle = color||'#e8f1ff';
      ctx.font = 'bold '+(size||16)+'px Arial,Helvetica,sans-serif';
      ctx.textAlign = align||'center'; ctx.textBaseline='middle';
      ctx.fillText(s,x,y);
    }
  };
  if(def.init) def.init(api);

  var last = performance.now();
  function frame(now){
    var dt = Math.min(0.05, (now-last)/1000); last = now;
    try{
      if(def.update) def.update(api, dt);
      ctx.fillStyle = '#070b16'; ctx.fillRect(0,0,W,H);
      if(def.draw) def.draw(api, ctx);
    }catch(err){
      ctx.fillStyle='#070b16'; ctx.fillRect(0,0,W,H);
      api.text('Game error — reload to restart', W/2, H/2, 14, '#ff6b6b');
    }
    for(var k in pressed) pressed[k]=false;
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
  return api;
};
})();
