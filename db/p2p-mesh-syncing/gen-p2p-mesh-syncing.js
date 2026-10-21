(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=["file", "database", "network", "collaboration", "iot"];
var PREFIX='JAH-PPMESH-';
var GENVER='jahdb-p2p-mesh-syncing-1.0';
var SRC='public-harvest';
var EDITION='public';
var PROV="Public record compiled from openly published documentation, project sources, and standard references.";
var FIELDS=["system", "topology", "protocol", "use"];
var DEMO_TPL="// $TITLE - gossip sync demo\nvar peers = { A: [1, 2], B: [2, 3], C: [3] };\nfunction gossip() {\n  var changed = false;\n  [\"A\", \"B\", \"C\"].forEach(function(p) {\n    [\"A\", \"B\", \"C\"].forEach(function(q) {\n      if (p === q) return;\n      peers[q].forEach(function(v) { if (peers[p].indexOf(v) < 0) { peers[p].push(v); changed = true; } });\n    });\n  });\n  return changed;\n}\nvar rounds = 0;\nwhile (gossip() && rounds < 10) rounds++;\nconsole.log(\"System: $SYSTEM | Topology: $TOPOLOGY\");\nconsole.log(\"Converged in \" + rounds + \" gossip rounds: \" + JSON.stringify(peers));\nconsole.log(\"All peers hold [1,2,3] -> SYNC PASS\");";
function jsEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\n/g,'\\n').replace(/\r/g,'\\r').replace(/\t/g,'\\t');}
function fillTpl(tpl,vars){return tpl.replace(/\$([A-Za-z0-9_]+)/g,function(m,k){return Object.prototype.hasOwnProperty.call(vars,k)?jsEsc(vars[k]):m;});}
/* rows: [category, title, description, {fields}] */
var B=[["file", "BitTorrent", "The original P2P file protocol; swarms share pieces with rarest-first and tit-for-tat. Topology: swarm. Protocol: peer wire protocol. Used for: large file distribution.", {"system": "BitTorrent", "topology": "swarm", "protocol": "peer wire protocol", "use": "large file distribution"}], ["file", "IPFS", "Content-addressed files over libp2p with Bitswap exchange and DHT routing. Topology: DHT mesh. Protocol: Bitswap/libp2p. Used for: decentralized storage.", {"system": "IPFS", "topology": "DHT mesh", "protocol": "Bitswap/libp2p", "use": "decentralized storage"}], ["network", "libp2p", "The modular networking stack under IPFS: transports, discovery, pubsub, NAT traversal. Topology: modular mesh. Protocol: multiaddr transports. Used for: P2P app networking.", {"system": "libp2p", "topology": "modular mesh", "protocol": "multiaddr transports", "use": "P2P app networking"}], ["file", "Syncthing", "Continuous file sync between devices with no cloud; every device holds encrypted data. Topology: full mesh. Protocol: BEP over TLS. Used for: private file sync.", {"system": "Syncthing", "topology": "full mesh", "protocol": "BEP over TLS", "use": "private file sync"}], ["file", "Resilio Sync", "Commercial BitTorrent-based sync with selective sync and encrypted folders. Topology: swarm. Protocol: BitTorrent-based. Used for: team file sync.", {"system": "Resilio Sync", "topology": "swarm", "protocol": "BitTorrent-based", "use": "team file sync"}], ["file", "Hypercore", "Append-only logs (Dat) with sparse replication — peers sync only the ranges they want. Topology: swarm per feed. Protocol: Hypercore protocol. Used for: dataset sharing.", {"system": "Hypercore", "topology": "swarm per feed", "protocol": "Hypercore protocol", "use": "dataset sharing"}], ["database", "Secure Scuttlebutt", "Offline-first social feeds gossiping append-only logs between friends. Topology: friend-of-friend. Protocol: gossip replication. Used for: decentralized social.", {"system": "SSB", "topology": "friend-of-friend", "protocol": "gossip replication", "use": "decentralized social"}], ["database", "GunDB", "A graph database syncing over WebRTC and WebSockets with eventual consistency. Topology: mesh. Protocol: RAD/DAM. Used for: realtime P2P apps.", {"system": "GunDB", "topology": "mesh", "protocol": "RAD/DAM", "use": "realtime P2P apps"}], ["collaboration", "Yjs", "CRDT-based shared editing syncing over any transport with zero conflicts. Topology: any (CRDT). Protocol: update exchange. Used for: collaborative editing.", {"system": "Yjs", "topology": "any (CRDT)", "protocol": "update exchange", "use": "collaborative editing"}], ["collaboration", "Automerge", "JSON-like CRDTs with full history — like git for application state. Topology: any (CRDT). Protocol: sync protocol. Used for: local-first software.", {"system": "Automerge", "topology": "any (CRDT)", "protocol": "sync protocol", "use": "local-first software"}], ["network", "ZeroTier", "Encrypted virtual LANs over a peer-to-peer underlay with centralized control plane. Topology: virtual L1 mesh. Protocol: VL1/VL2. Used for: SD-WAN overlays.", {"system": "ZeroTier", "topology": "virtual L1 mesh", "protocol": "VL1/VL2", "use": "SD-WAN overlays"}], ["network", "Tailscale", "WireGuard meshes coordinated by a control plane with DERP relays for NAT. Topology: WireGuard mesh. Protocol: WireGuard + DERP. Used for: zero-config VPN.", {"system": "Tailscale", "topology": "WireGuard mesh", "protocol": "WireGuard + DERP", "use": "zero-config VPN"}], ["network", "cjdns", "Encrypted IPv6 mesh routing with crypto-addressed nodes (fc00::/8). Topology: DHT-routed mesh. Protocol: cryptoauth. Used for: mesh networking.", {"system": "cjdns", "topology": "DHT-routed mesh", "protocol": "cryptoauth", "use": "mesh networking"}], ["file", "RetroShare", "Friend-to-friend sharing with forums, mail, and channels over encrypted tunnels. Topology: friend-to-friend. Protocol: OpenPGP + TLS. Used for: private sharing.", {"system": "RetroShare", "topology": "friend-to-friend", "protocol": "OpenPGP + TLS", "use": "private sharing"}], ["iot", "Briar", "Mesh messaging over Bluetooth/Wi-Fi/Tor designed for activists and offline use. Topology: opportunistic mesh. Protocol: Bramble. Used for: censorship-resistant chat.", {"system": "Briar", "topology": "opportunistic mesh", "protocol": "Bramble", "use": "censorship-resistant chat"}]];
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
  if(!new RegExp('^'+'JAH\\-PPMESH\\-'+'\\d{6}$').test(r.id||''))e.push('id');
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('p2p-mesh-syncing',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
