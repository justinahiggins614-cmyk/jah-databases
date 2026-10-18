(function(){'use strict';
/* JAH The Spot the Difference Database Database generator — jahdb-db-spot-the-difference-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SPOTHEDI-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Differences: Two sunny park scenes...",
  "Differences: Two cozy living rooms...",
  "Differences: Two beach scenes...",
  "Differences: Two classrooms...",
  "Differences: Two kitchens...",
  "Differences: Two gardens...",
  "Differences: Two toy rooms...",
  "Differences: Two snowy yards...",
  "Differences: Two libraries...",
  "Differences: Two farms...",
  "Differences: Two campsites..."
 ],
 "Compounded": [
  "Differences: Two market streets...",
  "Differences: Two museum halls...",
  "Differences: Two jungle clearings...",
  "Differences: Two train stations...",
  "Differences: Two attics...",
  "Differences: Two harbors...",
  "Differences: Two bakeries...",
  "Differences: Two construction sites...",
  "Differences: Two aquarium tunnels...",
  "Differences: Two festival nights...",
  "Differences: Two mountain lodges...",
  "Differences: Two greenhouses..."
 ],
 "Advanced": [
  "Differences: Two old master banquet paintings...",
  "Differences: Two space station interiors...",
  "Differences: Two rainy city streets...",
  "Differences: Two rare book rooms...",
  "Differences: Two glacier fields...",
  "Differences: Two coral reefs...",
  "Differences: Two detective evidence walls...",
  "Differences: Two desert nights...",
  "Differences: Two foggy harbors...",
  "Differences: Two magic stages...",
  "Differences: Two libraries at dusk..."
 ]
};
var DEMOKIND="difference-proof";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Spot the Difference Study — "+safe+"\n"
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
    name:topic+' — difference scene record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A difference scene record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-db-spot-the-difference-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-spot-the-difference',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
