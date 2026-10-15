(function(){'use strict';
/* JAH The Network Protocols Database generator — jahdb-network-protocols-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NP-";
var FIELDS=["protocol"];
var TOPICS={
 "protocol": [
  "Packet Crafters \u2014 protocol",
  "Packet Analyzers \u2014 protocol",
  "Protocol Decoders \u2014 protocol",
  "Traffic Shapers \u2014 protocol",
  "Traffic Generators \u2014 protocol",
  "Network Taps \u2014 protocol",
  "Port Scanners \u2014 protocol",
  "Socket Listeners \u2014 protocol",
  "TUN/TAP Drivers \u2014 protocol",
  "DNS Sinkholes \u2014 protocol",
  "Reverse Tunnels \u2014 protocol",
  "STUN Servers \u2014 protocol",
  "TURN Servers \u2014 protocol",
  "ICE Agents \u2014 protocol",
  "eBPF Programs \u2014 protocol",
  "XDP Drivers \u2014 protocol",
  "TC Filters \u2014 protocol",
  "NetFlow Collectors \u2014 protocol",
  "sFlow Agents \u2014 protocol",
  "SNMP Managers \u2014 protocol",
  "SNMP Agents \u2014 protocol",
  "Syslog Servers \u2014 protocol",
  "Netconf Clients \u2014 protocol",
  "Restconf APIs \u2014 protocol",
  "gNMI Clients \u2014 protocol",
  "OpenFlow Controllers \u2014 protocol",
  "P4 Programs \u2014 protocol",
  "BGP Daemons \u2014 protocol",
  "OSPF Daemons \u2014 protocol",
  "IS-IS Daemons \u2014 protocol",
  "RIP Daemons \u2014 protocol",
  "VRRP Daemons \u2014 protocol",
  "DHCP Servers \u2014 protocol",
  "DHCP Relays \u2014 protocol",
  "DNS Resolvers \u2014 protocol",
  "DNS Authoritatives \u2014 protocol",
  "NTP Servers \u2014 protocol",
  "PTP Grandmasters \u2014 protocol",
  "LDAP Servers \u2014 protocol",
  "Kerberos KDCs \u2014 protocol",
  "RADIUS Servers \u2014 protocol",
  "TACACS+ Servers \u2014 protocol",
  "SAML IdPs \u2014 protocol",
  "OAuth Servers \u2014 protocol",
  "OIDC Providers \u2014 protocol",
  "MQTT Brokers \u2014 protocol",
  "CoAP Servers \u2014 protocol",
  "AMQP Brokers \u2014 protocol",
  "ZeroMQ Patterns \u2014 protocol",
  "NATS Servers \u2014 protocol",
  "gRPC Servers \u2014 protocol",
  "Thrift Servers \u2014 protocol",
  "WebSocket Servers \u2014 protocol",
  "SSE Servers \u2014 protocol",
  "QUIC Servers \u2014 protocol",
  "HTTP/3 Servers \u2014 protocol",
  "DoH Resolvers \u2014 protocol",
  "DoT Servers \u2014 protocol",
  "WireGuard Peers \u2014 protocol",
  "OpenVPN Servers \u2014 protocol",
  "IPsec Gateways \u2014 protocol"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Network Protocols — "+safe+"\n"
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
    name:topic+' — network protocol record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A network protocol record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-network-protocols-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('network-protocols',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
