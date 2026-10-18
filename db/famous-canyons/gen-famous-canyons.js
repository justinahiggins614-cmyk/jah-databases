(function(){'use strict';
/* JAH Famous Canyons Database generator — jahdb-famous-canyons-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FCFA-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "How Canyons Form",
  "The Grand Canyon",
  "Antelope Canyon",
  "The Fish River Canyon",
  "Copper Canyon",
  "Colca Canyon",
  "Cotahuasi Canyon",
  "The Yarlung Tsangpo Grand Canyon",
  "Tiger Leaping Gorge",
  "Waimea Canyon",
  "Kings Canyon, Australia"
 ],
 "Compounded": [
  "Bryce Canyon",
  "Zion Canyon",
  "The Royal Gorge",
  "Palo Duro Canyon",
  "Hells Canyon",
  "The Black Canyon of the Gunnison",
  "Canyon de Chelly",
  "Taroko Gorge",
  "Vikos Gorge",
  "The Verdon Gorge",
  "Samaria Gorge",
  "The Todra Gorges"
 ],
 "Advanced": [
  "Blyde River Canyon",
  "Paria Canyon",
  "Submarine Canyons",
  "The Monterey Canyon",
  "Slot Canyon Hydraulics",
  "Canyon Ecosystems",
  "Desert Varnish",
  "Canyon Archaeology",
  "Canyoneering Safety",
  "The Future of Canyon Country",
  "Canyon Conservation"
 ]
};
var DEMOKIND="canyon analyzer";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Canyon depth comparator — "+safe+"\n"
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
    name:topic+' — canyon record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A canyon record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-famous-canyons-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('famous-canyons',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
