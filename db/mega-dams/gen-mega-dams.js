(function(){'use strict';
/* JAH Mega Dams Database generator — jahdb-mega-dams-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MDME-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Mega Dams Are",
  "The Three Gorges Dam",
  "The Itaipu Dam",
  "Hoover Dam",
  "The Aswan High Dam",
  "The Grand Coulee Dam",
  "The Nurek Dam",
  "The Jinping-I Dam",
  "The Xiaowan Dam",
  "The Tehri Dam",
  "The Bhakra Dam"
 ],
 "Compounded": [
  "The Kariba Dam",
  "The Cahora Bassa Dam",
  "The Grand Ethiopian Renaissance Dam",
  "The Belo Monte Dam",
  "The Tucurui Dam",
  "The Guri Dam",
  "The Bratsk Dam",
  "The Krasnoyarsk Dam",
  "The Sayano-Shushenskaya Dam",
  "The Rogun Dam",
  "The Tarbela Dam",
  "The Mangla Dam"
 ],
 "Advanced": [
  "Dam Engineering: Gravity Versus Arch Versus Embankment",
  "Spillways",
  "Reservoir Sedimentation",
  "Dam Safety",
  "The Banqiao Lesson",
  "Environmental Costs of Dams",
  "Dam Removal",
  "Hydropower and Climate",
  "The Future of Big Dams",
  "Pumped-Storage Hybrids",
  "Hydropower Turbines"
 ]
};
var DEMOKIND="dam analyzer";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Hydropower output calculator — "+safe+"\n"
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
    name:topic+' — mega dam record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A mega dam record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-mega-dams-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('mega-dams',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
