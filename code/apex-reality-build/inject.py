"""Page injections for the Apex-Reality build.

- badge_patch: 'signature-concept' src gets an honest concept badge.
- inject_console: working interactive Apex-Reality console (concept simulator)
  on the apex-reality-computer pages.
- inject_registry: interactive Federation Registry (commissioning with
  uniqueness checks, blueprint, persona, comms, missions, A7 dispatch) on
  the apex-reality-federation pages.
"""


def badge_patch(page):
    old = ("  return '<div><span class=\"badge sig\">\u2733 Signature-generated sample "
           "\u2014 structural sample</span> <span class=\"badge\">labeled sample</span></div>';")
    new = ("  if(r&&r.src==='signature-concept') return '<div><span class=\"badge sig\">"
           "\u25c7 Signature concept \u2014 speculative design, not real-world fact</span></div>';\n"
           + old)
    assert old in page, "sigBadge fallback not found for badge patch"
    return page.replace(old, new, 1)


CONSOLE_TAB = '<button class="tab" data-p="chat">AI Chat</button>'
CONSOLE_PANE = """  <section class="pane" id="p-console">
    <div class="card">
      <h3>Apex-Reality Console <span class="badge sig">\u25c7 concept simulator</span></h3>
      <p class="dim"><b>CONCEPT SIMULATION</b> \u2014 this console is an interactive concept experience: it simulates the Apex-Reality design (number line, protocol, swarms, portals, warp, bridge, memory) with honest, deterministic answers. Speculative Signature design by Justin Addam Higgins \u2014 not a real starship, not proven fact. Try <span class="mono">help</span>.</p>
      <div class="chatlog" id="conlog" style="font-family:Consolas,monospace"></div>
      <div class="row"><span class="mono" style="color:#00e5a0">&gt;</span><input id="conIn" class="mono" placeholder="Type a command\u2026 (help)" style="flex:1;min-width:200px"><button class="go" id="conGo">Run</button></div>
    </div>
  </section>
"""

CONSOLE_JS = """
/* ---- Apex-Reality Console: honest concept simulator (build-injected) ---- */
var conHONEST='CONCEPT SIMULATION - speculative Signature design by Justin Addam Higgins (A7 Signature Dominion). Not a real starship. Not proven fact.';
var conLog=$('conlog'),conIn=$('conIn'),conTick=0;
function conLine(html){conLog.innerHTML+='<div>'+html+'</div>';conLog.scrollTop=conLog.scrollHeight;}
function conSay(t){conLine('<span style="color:#9fd8ff">'+esc(t)+'</span>');}
function conDim(t){conLine('<span class="dim">'+esc(t)+'</span>');}
function conOk(t){conLine('<span class="ok">'+esc(t)+'</span>');}
function conErr(t){conLine('<span class="bad">'+esc(t)+'</span>');}
function conHash(s){var h=0;for(var i=0;i<s.length;i++){h=((h<<5)-h+s.charCodeAt(i))|0;}return h>>>0;}
function conBoot(){
  conSay('APEX-REALITY CONSOLE 2.0 - concept simulator boot.');
  conDim(conHONEST);
  ['JAH-UALNS number line locked [0.0 ... 1.0]','AUA-JM2 handshake: HELLO > SYNC > READY','plasma swarm: 12/12 concept bots in lattice','light swarm: 12/12 concept bots aligned','void swarm: 12/12 concept bots holding','portal lattice: stability nominal (concept)','reality bridge: 3 anchors surveyed','memory engine: checkpoint taken at t=0'].forEach(function(s){conOk('[ok] '+s);});
  conSay('Console ready. Type "help".');
}
function conAnchor(pos){var a=[['ORIGIN',0],['HARMONY',.25],['THRESHOLD',.5],['RADIANCE',.75],['APEX',1]],b=a[0];a.forEach(function(x){if(Math.abs(x[1]-pos)<Math.abs(b[1]-pos))b=x;});return b[0];}
function conRun(raw){
  var line=String(raw||'').trim();if(!line)return;
  conTick++;
  conLine('<span class="mono" style="color:#00e5a0">&gt; '+esc(line)+'</span>');
  var parts=line.split(/\\s+/),cmd=parts[0].toLowerCase(),args=parts.slice(1);
  var C={
    help:function(){conSay('commands: boot status scan <target> numberline <0-10> protocol <message> swarm portal <dist> <stab> warp <n> bridge memory <event> registry about clear');conDim('Every answer is concept simulation - see the honesty banner.');},
    boot:function(){conBoot();},
    status:function(){conOk('core=ONLINE swarm=36/36 bridge=ANCHORED memory=t'+conTick);conDim(conHONEST);},
    scan:function(){var t=args.join(' ')||'the void';var h=conHash(t);var p=(h%1000)/1000;conSay('scan "'+t+'": position '+p.toFixed(3)+' nearest anchor '+conAnchor(p));conDim('concept reading - simulated, not measured.');},
    numberline:function(){var v=parseFloat(args[0]);if(isNaN(v)){conErr('usage: numberline <value 0-10>');return;}var p=Math.max(0,Math.min(1,v/10));conSay(v+' -> position '+p.toFixed(3)+' nearest anchor '+conAnchor(p));},
    protocol:function(){var m=args.join(' ')||'ping';var c=0,i;for(i=0;i<m.length;i++)c=(c+m.charCodeAt(i))%256;var hx=('0'+c.toString(16)).slice(-2).toUpperCase();conSay('framed: [STX]console|'+('000'+conTick).slice(-4)+'|'+m+'|'+hx+'[ETX] checksum '+hx+' ok');},
    swarm:function(){var h=conHash('swarm'+conTick);conOk('12 concept bots converged in '+(20+(h%40))+' ticks (simulated).');},
    portal:function(){var d=parseFloat(args[0]||'5'),s=parseFloat(args[1]||'0.7');if(isNaN(d)||isNaN(s)||s<=0){conErr('usage: portal <distance> <stability>');return;}var e=1.7*d*d/s;conSay('E = 1.7*'+d+'^2/'+s+' = '+e.toFixed(2)+' -> '+(e<=50?'STABLE':(e<=100?'MARGINAL':'UNSTABLE'))+' (concept equation)');},
    warp:function(){var n=Math.max(1,Math.min(12,parseInt(args[0]||'4',10)||4));var c=0,k;for(k=1;k<=n;k++)c+=(1/k)*Math.cos(0.15*k);c/=n;conSay(n+' harmonics: coherence '+(c>=0?'+':'')+c.toFixed(4)+' (concept series)');},
    bridge:function(){conSay('anchors: ALPHA(0,0) BETA(7,2) GAMMA(15,-3). Longest feasible span: ALPHA<->BETA 7.28 (concept geometry).');},
    memory:function(){var e=args.join(' ')||'operator note';conSay('recorded "'+e+'" at t='+conTick+' (concept memory).');},
    registry:function(){conSay('JAH-A7-SYS-0001 UALNS Core | 0002 AUA-JM2 Hub | 0003 Plasma Lattice | 0004 Warp Console (concept registry)');},
    about:function(){conDim(conHONEST);conDim('The Apex-Reality Computer is a Signature concept design: number line, protocol, nanobot swarms, portals, warp console, reality bridge, time-aware memory. Interactive, speculative, labeled - never a real starship.');},
    clear:function(){conLog.innerHTML='';}
  };
  if(C[cmd])C[cmd]();else conErr("unknown command '"+cmd+"' - try help (concept simulator).");
}
$('conGo').addEventListener('click',function(){conRun(conIn.value);conIn.value='';});
conIn.addEventListener('keydown',function(e){if(e.key==='Enter'){conRun(conIn.value);conIn.value='';}});
conBoot();
"""


def inject_console(page):
    assert CONSOLE_TAB in page, "chat tab button not found"
    page = page.replace(CONSOLE_TAB,
                        CONSOLE_TAB + '\n    <button class="tab" data-p="console">Console</button>', 1)
    marker = '  <section class="pane" id="p-about">'
    assert marker in page, "about pane not found"
    page = page.replace(marker, CONSOLE_PANE + marker, 1)
    tail = "})();</script>"
    assert tail in page, "script tail not found"
    page = page[:page.rfind(tail)] + CONSOLE_JS + "\n" + tail + page[page.rfind(tail) + len(tail):]
    return page


REGISTRY_PANE = """  <section class="pane" id="p-registry">
    <div class="card">
      <h3>Federation Registry <span class="badge sig">\u25c7 concept experience</span></h3>
      <p class="dim"><b>CONCEPT EXPERIENCE</b> \u2014 name yourself and your starship (uniqueness-checked), enter ship parameters, and receive a patent-style blueprint, a personalized ship AI persona, and a Federation registry entry. A fictional fellowship exercise by Justin Addam Higgins \u2014 not a real registry, not a real institution.</p>
      <div class="row">
        <label>Commander name <input id="rgCommander" placeholder="e.g. Mara Voss" style="min-width:180px"></label>
        <label>Starship name <input id="rgShip" placeholder="e.g. Starweaver" style="min-width:180px"></label>
      </div>
      <div class="row" style="margin-top:8px">
        <label>Class <select id="rgClass"><option>Voyager</option><option>Harbor</option><option>Lancer</option><option>Bastion</option><option>Wayfinder</option></select></label>
        <label>Drive <select id="rgDrive"><option>plasma-sail</option><option>light-lattice</option><option>void-anchor</option><option>triad</option></select></label>
        <label>Crew <input id="rgCrew" type="number" value="12" min="1" max="5000" style="width:90px"></label>
        <label>Mission profile <select id="rgMission"><option>exploration</option><option>harbor service</option><option>cartography</option><option>festival circuit</option><option>deep veil</option></select></label>
      </div>
      <div class="row" style="margin-top:8px"><button class="go" id="rgGo">Commission Ship</button></div>
      <div id="rgOut"></div>
    </div>
    <div class="card">
      <h3>Fleet Comms <span class="badge sig">\u25c7 concept experience</span></h3>
      <div class="chatlog" id="cmLog"></div>
      <div class="row"><input id="cmIn" placeholder="Hail the fleet\u2026 (concept comms)" style="flex:1;min-width:200px"><button class="go" id="cmGo">Transmit</button></div>
    </div>
    <div class="card">
      <h3>Shared Mission Board <span class="badge sig">\u25c7 concept experience</span></h3>
      <div id="msBoard"></div>
      <div class="row" style="margin-top:8px">
        <input id="msTitle" placeholder="Mission title" style="flex:1;min-width:160px">
        <label>Region <select id="msRegion"><option>inner reach</option><option>outer reach</option><option>the veil</option><option>harbor ring</option></select></label>
        <label>Ships <input id="msShips" type="number" value="2" min="1" max="20" style="width:70px"></label>
        <button class="go" id="msGo">Propose Mission</button>
      </div>
    </div>
    <div class="card">
      <h3>A7 Control Layer <span class="badge sig">\u25c7 concept experience</span></h3>
      <p class="dim">The unified command simulator: dispatch a named order and watch the concept acknowledgements come back. Coordination, never coercion \u2014 and all of it labeled fiction.</p>
      <div class="row"><label>Order <select id="a7Order"><option>patrol</option><option>rendezvous</option><option>standby</option><option>resupply</option></select></label><button class="go" id="a7Go">Dispatch</button></div>
      <div class="chatlog" id="a7Out" style="margin-top:8px"></div>
    </div>
  </section>
"""

REGISTRY_JS = """
/* ---- Federation Registry: concept experience (build-injected) ---- */
var RG_RESERVED=['apex one','dominion prime','signature dawn'];
var RG_KEY='jahFedRegV1',CM_KEY='jahFedCommsV1',MS_KEY='jahFedMissionsV1';
function rgLoad(k,d){try{var v=JSON.parse(localStorage.getItem(k));return v==null?d:v;}catch(e){return d;}}
function rgSave(k,v){try{localStorage.setItem(k,JSON.stringify(v));}catch(e){}}
function rgShips(){return rgLoad(RG_KEY,[]);}
function rgScreen(s){return !/\\b(hate|kill|slur)\\b/i.test(s||'');}
function rgPersona(ship){
  var h=0,i;for(i=0;i<ship.length;i++){h=((h<<5)-h+ship.charCodeAt(i))|0;}h>>>=0;
  var traits=['steady','wry','precise','warm','bold','patient','curious','dry-witted'];
  var voices=['measured baritone','bright alto','soft tenor','gravelly bass'];
  var core=ship.replace(/\\s+/g,'');
  var nm=((core.length>2?core.charAt(0).toUpperCase()+'ex':(core+'ex')).toUpperCase())+'-P';
  return {name:nm,trait:traits[h%traits.length],voice:voices[(h>>8)%voices.length]};
}
function rgBlueprint(e){
  return ['CONCEPT BLUEPRINT - not a real patent, not a real starship',
  'Title: Starship '+e.ship+' ('+e.klass+' class)',
  'Designer of record: '+e.commander+', A7 Signature Dominion (concept)',
  'Registry: '+e.id+' | Persona: '+e.persona,
  '',
  '[1] FIELD: speculative starship concept design.',
  '[2] BACKGROUND: the Federation needs one shared blueprint language so every',
  '    commander\\'s ship can be described, compared, and role-played consistently.',
  '[3] SUMMARY: a '+e.klass+'-class vessel, '+e.drive+' drive, crew of '+e.crew+',',
  '    mission profile '+e.mission+', registered to Commander '+e.commander+'.',
  '[4] DESCRIPTION: hull lines follow the '+e.klass+'-class concept template; the',
  '    '+e.drive+' drive is drawn from the concept propulsion catalog; crew',
  '    stations scale with complement; the persona '+e.persona+' speaks for the ship.',
  '[5] CLAIMS (concept): 1) a shared blueprint format; 2) a registry entry per',
  '    ship; 3) honest speculative labeling on every artifact.'].join('\\n');
}
function rgCommission(){
  var out=$('rgOut');
  var commander=$('rgCommander').value.trim(),ship=$('rgShip').value.trim();
  var klass=$('rgClass').value,drive=$('rgDrive').value;
  var crew=parseInt($('rgCrew').value,10)||12,mission=$('rgMission').value;
  function fail(m){out.innerHTML='<p class="bad">'+esc(m)+'</p>';}
  if(!commander||!ship){fail('Name yourself and your starship - both are required.');return;}
  if(!rgScreen(commander+' '+ship)){fail('That name does not meet registry screening. Choose another.');return;}
  var key=ship.toLowerCase(),ships=rgShips();
  if(RG_RESERVED.indexOf(key)>=0){fail('"'+ship+'" is a reserved name of the fiction. Choose a unique starship name.');return;}
  if(ships.some(function(s){return s.ship.toLowerCase()===key;})){fail('There is already a "'+ship+'" in the registry. Ship names must be unique - choose another.');return;}
  var p=rgPersona(ship);
  var e={id:'JAH-FED-REG-'+('0000'+(ships.length+1)).slice(-4),commander:commander,ship:ship,klass:klass,drive:drive,crew:crew,mission:mission,persona:p.name};
  ships.push(e);rgSave(RG_KEY,ships);
  out.innerHTML='<div class="card"><h3>\\u25c7 Commissioned: '+esc(e.ship)+'</h3>'
    +'<dl class="kv"><dt>Registry ID</dt><dd class="mono">'+esc(e.id)+'</dd>'
    +'<dt>Commander</dt><dd>'+esc(e.commander)+'</dd>'
    +'<dt>Ship</dt><dd>'+esc(e.ship)+' <span class="dim">('+esc(e.klass)+' class, '+esc(e.drive)+' drive, crew '+e.crew+')</span></dd>'
    +'<dt>Ship AI persona</dt><dd><b>'+esc(p.name)+'</b> <span class="dim">('+esc(p.trait)+', '+esc(p.voice)+')</span><br>&ldquo;This is '+esc(p.name)+', ship intelligence of the '+esc(e.ship)+'. Commander '+esc(e.commander)+', all concept systems nominal. (I am a fictional persona for a concept experience.)&rdquo;</dd></dl>'
    +'<h4>Patent-style blueprint</h4><pre class="codeblock">'+esc(rgBlueprint(e))+'</pre>'
    +'<p class="dim">CONCEPT EXPERIENCE - this registry entry, blueprint, and persona are fiction, honestly labeled.</p></div>';
}
function cmRender(){
  var log=rgLoad(CM_KEY,[]);
  $('cmLog').innerHTML=log.map(function(m){return '<div class="msg a"><div class="b"><b>'+esc(m.ship)+'</b> <span class="dim">'+esc(m.at)+'</span><br>'+esc(m.text)+'</div></div>';}).join('')||'<p class="dim">No transmissions yet. The fleet is listening.</p>';
  $('cmLog').scrollTop=$('cmLog').scrollHeight;
}
function cmSend(){
  var t=$('cmIn').value.trim();if(!t)return;
  if(!rgScreen(t)){$('cmIn').value='';return;}
  var ships=rgShips(),me=ships.length?ships[ships.length-1]:null;
  var from=me?(me.ship+' / '+me.commander):'Unregistered visitor';
  var log=rgLoad(CM_KEY,[]);
  var d=new Date();
  log.push({ship:from,text:t,at:d.toISOString().slice(0,16).replace('T',' ')});
  rgSave(CM_KEY,log.slice(-50));$('cmIn').value='';cmRender();
}
var MS_SEED=[{id:'JAH-FED-MSN-001',title:'Beacon 7 resupply run',region:'inner reach',ships:2,joined:[],status:'open'},{id:'JAH-FED-MSN-002',title:'Cartograph the Veil',region:'outer reach',ships:4,joined:[],status:'open'}];
function msList(){var l=rgLoad(MS_KEY,null);if(!l){l=MS_SEED;rgSave(MS_KEY,l);}return l;}
function msRender(){
  var ships=rgShips(),me=ships.length?ships[ships.length-1].ship:null;
  $('msBoard').innerHTML=msList().map(function(m,i){
    var j=m.joined.map(function(x){return '<span class="badge">'+esc(x)+'</span>';}).join(' ');
    return '<div class="card"><b>'+esc(m.id)+' - '+esc(m.title)+'</b> <span class="badge">'+esc(m.region)+'</span> <span class="badge">ships '+m.joined.length+'/'+m.ships+'</span> <span class="badge">'+esc(m.status)+'</span><div style="margin-top:6px">'+(j||'<span class="dim">no ships joined yet</span>')+'</div>'+(me&&m.joined.indexOf(me)<0&&m.joined.length<m.ships?'<div style="margin-top:6px"><button data-msjoin="'+i+'">Join with '+esc(me)+'</button></div>':'')+'</div>';
  }).join('');
}
function msPropose(){
  var t=$('msTitle').value.trim();if(!t)return;
  var l=msList();
  l.push({id:'JAH-FED-MSN-'+('000'+(l.length+1)).slice(-3),title:t,region:$('msRegion').value,ships:Math.max(1,parseInt($('msShips').value,10)||2),joined:[],status:'open'});
  rgSave(MS_KEY,l);$('msTitle').value='';msRender();
}
document.addEventListener('click',function(e){
  var b=e.target&&e.target.closest?e.target.closest('[data-msjoin]'):null;
  if(!b)return;
  var ships=rgShips();if(!ships.length)return;
  var me=ships[ships.length-1].ship,l=msList(),m=l[parseInt(b.getAttribute('data-msjoin'),10)];
  if(m&&m.joined.indexOf(me)<0&&m.joined.length<m.ships){m.joined.push(me);if(m.joined.length>=m.ships)m.status='underway';rgSave(MS_KEY,l);msRender();}
});
var A7_ORDERS={patrol:'Patrol route acknowledged',rendezvous:'Course laid in',standby:'Standing by',resupply:'Resupply queued'};
function a7Dispatch(){
  var o=$('a7Order').value,ships=rgShips(),out=$('a7Out');
  var ack=A7_ORDERS[o]||'Order refused: unknown order';
  var targets=ships.length?ships.map(function(s){return s.ship;}):['(no ships commissioned yet - the order echoes across an empty harbor)'];
  out.innerHTML='<div><span class="dim">A7-COMMAND dispatching "'+esc(o)+'" (concept simulation)</span></div>'+targets.map(function(s){return '<div><span class="mono">A7-COMMAND -&gt; '+esc(s)+'</span>: '+esc(ships.length?(s+': '+ack+' (concept)'):ack+' (concept)')+'</div>';}).join('');
  out.scrollTop=out.scrollHeight;
}
$('rgGo').addEventListener('click',rgCommission);
$('cmGo').addEventListener('click',cmSend);
$('cmIn').addEventListener('keydown',function(e){if(e.key==='Enter')cmSend();});
$('msGo').addEventListener('click',msPropose);
$('a7Go').addEventListener('click',a7Dispatch);
cmRender();msRender();
"""


def inject_registry(page):
    assert CONSOLE_TAB in page, "chat tab button not found"
    page = page.replace(CONSOLE_TAB,
                        CONSOLE_TAB + '\n    <button class="tab" data-p="registry">Registry</button>', 1)
    marker = '  <section class="pane" id="p-about">'
    assert marker in page, "about pane not found"
    page = page.replace(marker, REGISTRY_PANE + marker, 1)
    tail = "})();</script>"
    assert tail in page, "script tail not found"
    page = page[:page.rfind(tail)] + REGISTRY_JS + "\n" + tail + page[page.rfind(tail) + len(tail):]
    return page
