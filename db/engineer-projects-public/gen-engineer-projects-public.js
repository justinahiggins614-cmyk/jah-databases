(function(){'use strict';
/* JAH The Engineer Projects Public Database generator — jahdb-engineer-projects-public-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ENPP-";
var FIELDS=["Dams","Bridges","Tunnels","Buildings","Transport","Energy","Water","Space","Flood Defense","Research","Land Reclamation","Waterways","Habitats"];
var TOPICS={
 "Dams": [
  "Hoover Dam - Dams",
  "Three Gorges Dam - Dams",
  "Itaipu Dam - Dams",
  "Grand Coulee Dam - Dams",
  "Aswan High Dam - Dams"
 ],
 "Bridges": [
  "Golden Gate Bridge - Bridges",
  "Brooklyn Bridge - Bridges",
  "Millau Viaduct - Bridges",
  "Akashi Kaikyo Bridge - Bridges",
  "Oresund Bridge - Bridges",
  "Hong Kong-Zhuhai-Macau Bridge - Bridges"
 ],
 "Tunnels": [
  "Channel Tunnel - Tunnels",
  "Gotthard Base Tunnel - Tunnels"
 ],
 "Buildings": [
  "Burj Khalifa - Buildings",
  "Eiffel Tower (Plan 2) - Buildings",
  "Empire State Building (Plan 2) - Buildings",
  "Sydney Opera House (Plan 2) - Buildings",
  "The Pentagon - Buildings",
  "Taipei 101 - Buildings",
  "One World Trade Center - Buildings"
 ],
 "Transport": [
  "Transcontinental Railroad (Plan 2) - Transport",
  "Interstate Highway System - Transport",
  "London Underground - Transport",
  "Denver International Airport - Transport",
  "Tokaido Shinkansen - Transport"
 ],
 "Energy": [

 ],
 "Water": [

 ],
 "Space": [
  "Saturn V / Apollo - Space",
  "International Space Station (Plan 2) - Space"
 ],
 "Flood Defense": [
  "Thames Barrier - Flood Defense",
  "Delta Works - Flood Defense"
 ],
 "Research": [
  "Large Hadron Collider - Research"
 ],
 "Land Reclamation": [
  "Palm Jumeirah - Land Reclamation"
 ],
 "Waterways": [
  "Panama Canal - Waterways",
  "Suez Canal - Waterways",
  "Falkirk Wheel - Waterways"
 ],
 "Habitats": [

 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Engpub Blueprint Study — "+safe+"\n"
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
    name:topic+' — engineering project record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A engineering project record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"blueprint-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-engineer-projects-public-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('engineer-projects-public',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
