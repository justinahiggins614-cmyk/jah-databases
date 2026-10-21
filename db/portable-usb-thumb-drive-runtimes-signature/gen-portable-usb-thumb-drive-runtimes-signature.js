(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["apps", "os", "devtools", "rescue", "browser"];
var PREFIX='JAH-PUT-S-';
var GENVER='jahdb-portable-usb-thumb-drive-runtimes-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["runtime", "carries", "runs_from", "size"];
var DEMO_TPL="// $TITLE - portable manifest demo\nvar M = { runtime: \"$RUNTIME\", carries: \"$CARRIES\", from: \"$RUNS_FROM\", size: \"$SIZE\" };\nconsole.log(\"Portable runtime: \" + M.runtime);\nconsole.log(\"Carries: \" + M.carries);\nconsole.log(\"Runs from: \" + M.from + \" | Size: \" + M.size);\nvar files = [\"app.exe\", \"data/\", \"config.ini\"];\nconsole.log(\"Manifest: \" + files.join(\", \"));\nconsole.log(\"Host writes required: 0 -> PORTABLE PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["os", "SigStick-OS", "Signature-original: a live OS booting the full Signature workstation from any USB. It carries Signature workstation, runs from bootable USB, at about ~2 GB.", {"runtime": "SigStick-OS", "carries": "Signature workstation", "runs_from": "bootable USB", "size": "~2 GB"}], ["devtools", "SigStick-Dev", "Signature-original: portable dev environment with toolchains and the Sig SDK. It carries compilers + Sig SDK, runs from USB stick, at about ~1 GB.", {"runtime": "SigStick-Dev", "carries": "compilers + Sig SDK", "runs_from": "USB stick", "size": "~1 GB"}], ["rescue", "SigStick-Rescue", "Signature-original: rescue stick that can reimage and verify any Sig host. It carries recovery tools, runs from bootable USB, at about ~600 MB.", {"runtime": "SigStick-Rescue", "carries": "recovery tools", "runs_from": "bootable USB", "size": "~600 MB"}], ["apps", "SigStick-Mesh", "Signature-original: mesh node on a stick — plug in and join the peer network. It carries mesh node, runs from USB stick, at about ~150 MB.", {"runtime": "SigStick-Mesh", "carries": "mesh node", "runs_from": "USB stick", "size": "~150 MB"}], ["apps", "SigStick-Vault", "Signature-original: hardware-backed vault stick with duress PIN support. It carries secret vault, runs from USB stick, at about ~80 MB.", {"runtime": "SigStick-Vault", "carries": "secret vault", "runs_from": "USB stick", "size": "~80 MB"}], ["browser", "SigStick-Browse", "Signature-original: private browser with mesh routing and no host traces. It carries private browser, runs from USB stick, at about ~140 MB.", {"runtime": "SigStick-Browse", "carries": "private browser", "runs_from": "USB stick", "size": "~140 MB"}], ["devtools", "SigStick-DB", "Signature-original: portable database lab with 1,000 sample databases. It carries DB lab, runs from USB stick, at about ~4 GB.", {"runtime": "SigStick-DB", "carries": "DB lab", "runs_from": "USB stick", "size": "~4 GB"}], ["apps", "SigStick-AI", "Signature-original: on-stick AI runtime running Sig models fully offline. It carries offline AI, runs from USB stick, at about ~5 GB.", {"runtime": "SigStick-AI", "carries": "offline AI", "runs_from": "USB stick", "size": "~5 GB"}], ["devtools", "SigStick-Build", "Signature-original: hermetic build farm image producing reproducible artifacts. It carries build farm, runs from bootable USB, at about ~3 GB.", {"runtime": "SigStick-Build", "carries": "build farm", "runs_from": "bootable USB", "size": "~3 GB"}], ["devtools", "SigStick-Test", "Signature-original: test lab booting ephemeral cells for integration suites. It carries test cells, runs from bootable USB, at about ~1 GB.", {"runtime": "SigStick-Test", "carries": "test cells", "runs_from": "bootable USB", "size": "~1 GB"}], ["apps", "SigStick-Media", "Signature-original: media studio with encoders and editors, project files on-stick. It carries media studio, runs from USB stick, at about ~2 GB.", {"runtime": "SigStick-Media", "carries": "media studio", "runs_from": "USB stick", "size": "~2 GB"}], ["rescue", "SigStick-Forensics", "Signature-original: forensics toolkit with write-blocked imaging built in. It carries forensics kit, runs from bootable USB, at about ~1 GB.", {"runtime": "SigStick-Forensics", "carries": "forensics kit", "runs_from": "bootable USB", "size": "~1 GB"}], ["os", "SigStick-Kiosk", "Signature-original: locked-down kiosk OS resetting to gold image on reboot. It carries kiosk OS, runs from bootable USB, at about ~900 MB.", {"runtime": "SigStick-Kiosk", "carries": "kiosk OS", "runs_from": "bootable USB", "size": "~900 MB"}], ["apps", "SigStick-Sync", "Signature-original: sync stick carrying encrypted deltas between air-gapped sites. It carries sync courier, runs from USB stick, at about ~100 MB.", {"runtime": "SigStick-Sync", "carries": "sync courier", "runs_from": "USB stick", "size": "~100 MB"}], ["os", "SigStick-One", "Signature-original: the united portable image — pick a profile at boot, everything included. It carries all profiles, runs from bootable USB, at about ~8 GB.", {"runtime": "SigStick-One", "carries": "all profiles", "runs_from": "bootable USB", "size": "~8 GB"}]];
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
  if(!new RegExp('^'+'JAH\\-PUT\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('portable-usb-thumb-drive-runtimes-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
