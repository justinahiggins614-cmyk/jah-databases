(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["automation", "testing", "protocol", "scraping", "load"];
var PREFIX='JAH-HEADLE-';
var GENVER='jahdb-headless-browser-simulation-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["tool", "drives", "protocol", "language"];
var DEMO_TPL="// $TITLE - headless session model\nvar S = { tool: \"$TOOL\", target: \"$DRIVES\", steps: [] };\nfunction step(name, fn) { var r = fn(); S.steps.push(name + \" -> \" + r); }\nstep(\"goto\", function() { return \"loaded \" + S.target; });\nstep(\"title\", function() { return \"Example Page\"; });\nstep(\"screenshot\", function() { return \"captured 1280x720\"; });\nconsole.log(\"Driver: \" + S.tool + \" | Target: \" + S.target);\nS.steps.forEach(function(s) { console.log(\"  \" + s); });\nconsole.log(\"Session: 3/3 steps PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["automation", "Puppeteer", "Chrome DevTools Protocol automation from Node; the reference headless Chrome driver. It drives Chromium over CDP; client language: JavaScript/TypeScript.", {"tool": "Puppeteer", "drives": "Chromium", "protocol": "CDP", "language": "JavaScript/TypeScript"}], ["automation", "Playwright", "Microsoft’s cross-browser driver for Chromium, Firefox, and WebKit with auto-waiting. It drives Chromium/Firefox/WebKit over CDP + custom; client language: JS/Python/Java/C#.", {"tool": "Playwright", "drives": "Chromium/Firefox/WebKit", "protocol": "CDP + custom", "language": "JS/Python/Java/C#"}], ["automation", "Selenium headless", "The WebDriver standard; --headless=new runs full Chrome/Firefox without a display. It drives any WebDriver browser over W3C WebDriver; client language: many.", {"tool": "Selenium", "drives": "any WebDriver browser", "protocol": "W3C WebDriver", "language": "many"}], ["protocol", "Chrome --headless", "Chrome’s native headless mode with --screenshot, --dump-dom, and --print-to-pdf flags. It drives Chromium over CLI flags; client language: any (CLI).", {"tool": "Chrome headless", "drives": "Chromium", "protocol": "CLI flags", "language": "any (CLI)"}], ["protocol", "Firefox headless", "MOZ_HEADLESS=1 runs Firefox headless with full WebDriver and CDP support. It drives Firefox over WebDriver/CDP; client language: any (CLI).", {"tool": "Firefox headless", "drives": "Firefox", "protocol": "WebDriver/CDP", "language": "any (CLI)"}], ["testing", "Cypress", "A test runner executing specs inside the browser with time-travel debugging snapshots. It drives Chromium/Firefox/WebKit over in-browser runner; client language: JavaScript.", {"tool": "Cypress", "drives": "Chromium/Firefox/WebKit", "protocol": "in-browser runner", "language": "JavaScript"}], ["automation", "WebdriverIO", "A Node WebDriver client with sync-style commands and mobile support via Appium. It drives any WebDriver browser over W3C WebDriver; client language: JavaScript.", {"tool": "WebdriverIO", "drives": "any WebDriver browser", "protocol": "W3C WebDriver", "language": "JavaScript"}], ["testing", "TestCafe", "No-driver testing injecting scripts into pages; runs against any browser including cloud farms. It drives any modern browser over proxy injection; client language: JavaScript.", {"tool": "TestCafe", "drives": "any modern browser", "protocol": "proxy injection", "language": "JavaScript"}], ["testing", "Nightwatch", "Selenium-based E2E with page objects and built-in parallel workers. It drives any WebDriver browser over W3C WebDriver; client language: JavaScript.", {"tool": "Nightwatch", "drives": "any WebDriver browser", "protocol": "W3C WebDriver", "language": "JavaScript"}], ["load", "k6 browser", "Grafana k6’s browser module runs real Chromium under load-test orchestration. It drives Chromium over CDP; client language: JavaScript.", {"tool": "k6 browser", "drives": "Chromium", "protocol": "CDP", "language": "JavaScript"}], ["scraping", "Splash", "A scriptable headless browser service with Lua scripting for scraping pipelines. It drives WebKit (Qt) over HTTP API + Lua; client language: Lua.", {"tool": "Splash", "drives": "WebKit (Qt)", "protocol": "HTTP API + Lua", "language": "Lua"}], ["scraping", "MechanicalSoup", "A Python library driving forms and navigation without JavaScript rendering overhead. It drives HTTP + forms over requests/BeautifulSoup; client language: Python.", {"tool": "MechanicalSoup", "drives": "HTTP + forms", "protocol": "requests/BeautifulSoup", "language": "Python"}], ["testing", "Zombie.js", "A lightweight Node headless browser for fast DOM-level tests without a real engine. It drives jsdom-based over in-process; client language: JavaScript.", {"tool": "Zombie.js", "drives": "jsdom-based", "protocol": "in-process", "language": "JavaScript"}], ["automation", "PhantomJS", "The original scriptable headless WebKit; retired but the pattern every later tool copied. It drives WebKit over JS API; client language: JavaScript.", {"tool": "PhantomJS (retired)", "drives": "WebKit", "protocol": "JS API", "language": "JavaScript"}], ["load", "Browserless", "Hosted headless Chrome as a service with concurrency limits and session queuing. It drives Chromium over CDP over WS; client language: any.", {"tool": "Browserless", "drives": "Chromium", "protocol": "CDP over WS", "language": "any"}]];
function demoFor(title,id,f){
  var vars={TITLE:title,ID:id};
  for(var k in f){ if(Object.prototype.hasOwnProperty.call(f,k)) vars[k.toUpperCase()]=f[k]; }
  return fillTpl(DEMO_TPL,vars);
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var fields={}; for(var k in b[3]){fields[k]=b[3][k];}
  return {id:id,t:b[1],title:b[1],g:cat,c:1,category:cat,description:b[2],fields:fields,ladder_rank:1+(seed%3),demo:demoFor(b[1],id,fields),provenance:PROV,src:SRC,last_verified:'2026-10-21',edition:EDITION,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+'JAH\\-HEADLE\\-'+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(r.t!==r.title)e.push('t');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(r.g!==r.category)e.push('g');
  if(!r.fields||typeof r.fields!=='object')e.push('fields');
  else{FIELDS.forEach(function(k){if(typeof r.fields[k]!=='string'||!r.fields[k].length)e.push('fields.'+k);});}
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('console.log')<0)e.push('demo');
  if(r.src!==SRC)e.push('src');
  if(r.edition!==EDITION)e.push('edition');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  if(typeof r.provenance!=='string'||!r.provenance.length)e.push('provenance');
  return {ok:!e.length,errors:e};
}
var gen={version:GENVER,generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('headless-browser-simulation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
