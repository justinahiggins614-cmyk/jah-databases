(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["apps", "os", "devtools", "rescue", "browser"];
var PREFIX='JAH-PUT-';
var GENVER='jahdb-portable-usb-thumb-drive-runtimes-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["runtime", "carries", "runs_from", "size"];
var DEMO_TPL="// $TITLE - portable manifest demo\nvar M = { runtime: \"$RUNTIME\", carries: \"$CARRIES\", from: \"$RUNS_FROM\", size: \"$SIZE\" };\nconsole.log(\"Portable runtime: \" + M.runtime);\nconsole.log(\"Carries: \" + M.carries);\nconsole.log(\"Runs from: \" + M.from + \" | Size: \" + M.size);\nvar files = [\"app.exe\", \"data/\", \"config.ini\"];\nconsole.log(\"Manifest: \" + files.join(\", \"));\nconsole.log(\"Host writes required: 0 -> PORTABLE PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["apps", "PortableApps.com", "The classic portable app platform with 400+ apps and a launcher that keeps everything on the stick. It carries 400+ portable apps, runs from USB stick, at about varies.", {"runtime": "PortableApps", "carries": "400+ portable apps", "runs_from": "USB stick", "size": "varies"}], ["apps", "LiberKey", "A French portable suite with automatic app updates and categorized menus. It carries 300 portable apps, runs from USB stick, at about varies.", {"runtime": "LiberKey", "carries": "300 portable apps", "runs_from": "USB stick", "size": "varies"}], ["devtools", "Portable Python", "Python distributions that run from a folder with pip and virtualenvs intact. It carries Python + scientific stack, runs from USB/folder, at about ~3 GB.", {"runtime": "WinPython / portable Python", "carries": "Python + scientific stack", "runs_from": "USB/folder", "size": "~3 GB"}], ["devtools", "XAMPP portable", "Apache + MySQL + PHP stack that runs from USB for demos and classrooms. It carries LAMP stack, runs from USB stick, at about ~500 MB.", {"runtime": "XAMPP portable", "carries": "LAMP stack", "runs_from": "USB stick", "size": "~500 MB"}], ["devtools", "VS Code Portable", "VS Code’s portable mode keeps settings and extensions inside the data folder. It carries editor + extensions, runs from USB/folder, at about ~400 MB.", {"runtime": "VS Code Portable", "carries": "editor + extensions", "runs_from": "USB/folder", "size": "~400 MB"}], ["browser", "Tor Browser", "A hardened Firefox that routes through Tor and leaves no trace on the host. It carries private browser, runs from USB stick, at about ~120 MB.", {"runtime": "Tor Browser", "carries": "private browser", "runs_from": "USB stick", "size": "~120 MB"}], ["os", "Tails", "The amnesic live OS routing everything through Tor, booting from USB with no persistence by default. It carries full Debian-based OS, runs from bootable USB, at about ~1.5 GB.", {"runtime": "Tails", "carries": "full Debian-based OS", "runs_from": "bootable USB", "size": "~1.5 GB"}], ["os", "Ventoy", "Boot any number of ISOs from one USB stick — just copy the ISO files on. It carries multi-ISO boot menu, runs from bootable USB, at about ~50 MB + ISOs.", {"runtime": "Ventoy", "carries": "multi-ISO boot menu", "runs_from": "bootable USB", "size": "~50 MB + ISOs"}], ["os", "Knoppix", "The original live-CD Linux that pioneered running an OS without installing. It carries Debian live OS, runs from USB/DVD, at about ~4 GB.", {"runtime": "Knoppix", "carries": "Debian live OS", "runs_from": "USB/DVD", "size": "~4 GB"}], ["rescue", "SystemRescue", "A Linux rescue toolkit for disk repair, imaging, and data recovery from USB. It carries rescue tools, runs from bootable USB, at about ~800 MB.", {"runtime": "SystemRescue", "carries": "rescue tools", "runs_from": "bootable USB", "size": "~800 MB"}], ["rescue", "Hiren’s BootCD PE", "A Windows PE rescue environment with disk, password, and recovery tools. It carries Windows PE rescue, runs from bootable USB, at about ~3 GB.", {"runtime": "Hiren’s BootCD PE", "carries": "Windows PE rescue", "runs_from": "bootable USB", "size": "~3 GB"}], ["devtools", "Portable Git", "Git for Windows in portable form with bash included — full VCS from a stick. It carries git + bash, runs from USB/folder, at about ~300 MB.", {"runtime": "Portable Git", "carries": "git + bash", "runs_from": "USB/folder", "size": "~300 MB"}], ["devtools", "Node portable", "Node.js ships as a zip; extract anywhere and it runs with npm included. It carries Node.js + npm, runs from any folder, at about ~100 MB.", {"runtime": "node portable zip", "carries": "Node.js + npm", "runs_from": "any folder", "size": "~100 MB"}], ["devtools", "QEMU portable", "QEMU binaries run VMs from a folder with disk images on the same stick. It carries machine emulator, runs from USB/folder, at about ~200 MB.", {"runtime": "QEMU portable", "carries": "machine emulator", "runs_from": "USB/folder", "size": "~200 MB"}], ["apps", "ClamWin portable", "Portable antivirus scanning from USB without installing anything on the host. It carries AV scanner, runs from USB stick, at about ~300 MB.", {"runtime": "ClamWin Portable", "carries": "AV scanner", "runs_from": "USB stick", "size": "~300 MB"}]];
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
  if(!new RegExp('^'+'JAH\\-PUT\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('portable-usb-thumb-drive-runtimes',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
