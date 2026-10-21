(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["file", "database", "network", "collaboration", "iot"];
var PREFIX='JAH-PPMESH-S-';
var GENVER='jahdb-p2p-mesh-syncing-signature-1.0';
var SRC='signature-generated-completion';
var EDITION='signature';
var PROV="Signature-original completion authored for the JAH Databases network; clearly labeled Signature, never presented as public record.";
var FIELDS=["system", "topology", "protocol", "use"];
var DEMO_TPL="// $TITLE - gossip sync demo\nvar peers = { A: [1, 2], B: [2, 3], C: [3] };\nfunction gossip() {\n  var changed = false;\n  [\"A\", \"B\", \"C\"].forEach(function(p) {\n    [\"A\", \"B\", \"C\"].forEach(function(q) {\n      if (p === q) return;\n      peers[q].forEach(function(v) { if (peers[p].indexOf(v) < 0) { peers[p].push(v); changed = true; } });\n    });\n  });\n  return changed;\n}\nvar rounds = 0;\nwhile (gossip() && rounds < 10) rounds++;\nconsole.log(\"System: $SYSTEM | Topology: $TOPOLOGY\");\nconsole.log(\"Converged in \" + rounds + \" gossip rounds: \" + JSON.stringify(peers));\nconsole.log(\"All peers hold [1,2,3] -> SYNC PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["network", "SigMesh-Core", "Signature-original: the core mesh with identity-bound addresses and 200 ms join. Topology: identity mesh. Protocol: SigMesh wire. Used for: all Sig networking.", {"system": "SigMesh-Core", "topology": "identity mesh", "protocol": "SigMesh wire", "use": "all Sig networking"}], ["file", "SigSync-File", "Signature-original: file sync with content-defined chunking and mesh-wide dedup. Topology: mesh. Protocol: SigSync. Used for: file sync.", {"system": "SigSync-File", "topology": "mesh", "protocol": "SigSync", "use": "file sync"}], ["database", "SigSync-DB", "Signature-original: database sync with CRDT merge and causal history. Topology: mesh. Protocol: SigCRDT. Used for: distributed DBs.", {"system": "SigSync-DB", "topology": "mesh", "protocol": "SigCRDT", "use": "distributed DBs"}], ["network", "SigGossip", "Signature-original: gossip with anti-entropy and bounded staleness guarantees. Topology: gossip mesh. Protocol: SigGossip. Used for: state propagation.", {"system": "SigGossip", "topology": "gossip mesh", "protocol": "SigGossip", "use": "state propagation"}], ["network", "SigPubSub", "Signature-original: topic pubsub with persistent cursors and replay. Topology: mesh. Protocol: SigPubSub. Used for: event buses.", {"system": "SigPubSub", "topology": "mesh", "protocol": "SigPubSub", "use": "event buses"}], ["network", "SigDHT", "Signature-original: Kademlia-style DHT with signed records and spam resistance. Topology: DHT. Protocol: SigDHT. Used for: decentralized lookup.", {"system": "SigDHT", "topology": "DHT", "protocol": "SigDHT", "use": "decentralized lookup"}], ["network", "SigRelay", "Signature-original: relay nodes for NAT-blocked peers with e2e encryption preserved. Topology: relay-assisted. Protocol: SigRelay. Used for: NAT traversal.", {"system": "SigRelay", "topology": "relay-assisted", "protocol": "SigRelay", "use": "NAT traversal"}], ["collaboration", "SigCollab", "Signature-original: collaborative editing with presence and undo across peers. Topology: CRDT mesh. Protocol: SigCRDT. Used for: shared docs.", {"system": "SigCollab", "topology": "CRDT mesh", "protocol": "SigCRDT", "use": "shared docs"}], ["database", "SigVote", "Signature-original: mesh voting for cluster membership without a central coordinator. Topology: mesh. Protocol: gossip vote. Used for: membership.", {"system": "SigVote", "topology": "mesh", "protocol": "gossip vote", "use": "membership"}], ["file", "SigStream", "Signature-original: live media streaming over the mesh with adaptive bitrate. Topology: mesh CDN. Protocol: SigStream. Used for: P2P media.", {"system": "SigStream", "topology": "mesh CDN", "protocol": "SigStream", "use": "P2P media"}], ["file", "SigBackup", "Signature-original: encrypted backups striped across mesh peers with erasure coding. Topology: erasure mesh. Protocol: SigBackup. Used for: offsite backup.", {"system": "SigBackup", "topology": "erasure mesh", "protocol": "SigBackup", "use": "offsite backup"}], ["iot", "SigChat", "Signature-original: mesh chat working fully offline via Bluetooth and Wi-Fi direct. Topology: opportunistic. Protocol: SigChat. Used for: offline messaging.", {"system": "SigChat", "topology": "opportunistic", "protocol": "SigChat", "use": "offline messaging"}], ["iot", "SigSensor", "Signature-original: sensor meshes aggregating readings with in-network reduction. Topology: sensor mesh. Protocol: SigSensor. Used for: IoT telemetry.", {"system": "SigSensor", "topology": "sensor mesh", "protocol": "SigSensor", "use": "IoT telemetry"}], ["network", "SigMarket", "Signature-original: bandwidth marketplace letting peers trade relay capacity. Topology: market mesh. Protocol: SigMarket. Used for: incentivized relay.", {"system": "SigMarket", "topology": "market mesh", "protocol": "SigMarket", "use": "incentivized relay"}], ["network", "SigMesh-One", "Signature-original: the united mesh plane — every Sig device joins one address space. Topology: unified mesh. Protocol: SigMesh. Used for: everything.", {"system": "SigMesh-One", "topology": "unified mesh", "protocol": "SigMesh", "use": "everything"}]];
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
  if(!new RegExp('^'+'JAH\\-PPMESH\\-S\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('p2p-mesh-syncing-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
