(function(){'use strict';
/* JAH The Network Devices Database generator — jahdb-network-devices-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NET-";
var FIELDS=["device"];
var TOPICS={
 "device": [
  "Network Bridges \u2014 device",
  "Tunnels \u2014 device",
  "VPN Tunnels \u2014 device",
  "SSH Tunnels \u2014 device",
  "Gateways \u2014 device",
  "API Gateways \u2014 device",
  "Network Gateways \u2014 device",
  "Edge Gateways \u2014 device",
  "Routers \u2014 device",
  "Core Routers \u2014 device",
  "Edge Routers \u2014 device",
  "Virtual Routers \u2014 device",
  "Proxies \u2014 device",
  "Forward Proxies \u2014 device",
  "Reverse Proxies \u2014 device",
  "Transparent Proxies \u2014 device",
  "Load Balancers \u2014 device",
  "Application Load Balancers \u2014 device",
  "Network Load Balancers \u2014 device",
  "Global Load Balancers \u2014 device",
  "Relays \u2014 device",
  "Message Relays \u2014 device",
  "Network Sockets \u2014 device",
  "Listening Sockets \u2014 device",
  "Raw Sockets \u2014 device",
  "Ports \u2014 device",
  "Firewalls \u2014 device",
  "Next-Gen Firewalls \u2014 device",
  "Web Application Firewalls \u2014 device",
  "Intrusion Prevention \u2014 device",
  "Intrusion Detection \u2014 device",
  "NAT Devices \u2014 device",
  "DHCP Servers \u2014 device",
  "DNS Servers \u2014 device",
  "NTP Servers \u2014 device",
  "Switches \u2014 device",
  "Managed Switches \u2014 device",
  "Unmanaged Switches \u2014 device",
  "Hubs \u2014 device",
  "Repeaters \u2014 device",
  "Modems \u2014 device",
  "Access Points \u2014 device",
  "Wireless Controllers \u2014 device",
  "Mesh Nodes \u2014 device",
  "Range Extenders \u2014 device",
  "Powerline Adapters \u2014 device",
  "Media Converters \u2014 device",
  "Terminal Servers \u2014 device",
  "KVM Switches \u2014 device",
  "Console Servers \u2014 device",
  "Packet Brokers \u2014 device",
  "Network Taps \u2014 device",
  "Bypass Switches \u2014 device"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Network Devices — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — network device record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A network device record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-network-devices-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('network-devices',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
