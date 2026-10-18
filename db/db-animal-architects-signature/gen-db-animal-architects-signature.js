(function(){'use strict';
/* JAH The Animal Architects Database Signature Database generator — jahdb-db-animal-architects-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AARS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Why Animals Build",
  "Beaver Dams",
  "Termite Mounds",
  "Weaver Bird Nests",
  "Bowerbirds",
  "Spider Webs Revisited",
  "Ant Nests",
  "Bird Nests 101",
  "The Pufferfish Circles",
  "Caddisfly Cases",
  "Burrow Systems"
 ],
 "Compounded": [
  "The Edible-Nest Swiftlet",
  "Honeycomb Geometry",
  "The Ovenbird Nest",
  "Coral Reefs",
  "The Sociable Weaver",
  "Trap Architecture",
  "The Megapode Mound",
  "Dam Builders Compared",
  "The Tailor Bird",
  "The Mud Dauber",
  "The Bagworm",
  "The Village Weaver City"
 ],
 "Advanced": [
  "Advanced: Biomimetic Buildings",
  "Advanced: The Architecture Awards",
  "Advanced: Your Backyard Builders",
  "Advanced: The Future Builders",
  "Advanced: The Nest Box Program",
  "Advanced: Beaver Restoration",
  "Advanced: The Termite Algorithm",
  "Advanced: Architecture Photography",
  "Advanced: Your Build Challenge",
  "Advanced: The Architect's Tour",
  "The Animal Architects Encyclopedia"
 ]
};
var DEMOKIND="animals-lab-demo";
var SAMPLEDESC="Sample records are complete real builder entries with real measurement math.";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Nature Lab Demo — "+safe+"\n"
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
    name:topic+' — animal architecture record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A animal architecture record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'signature',
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
var gen={version:'jahdb-db-animal-architects-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-animal-architects-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
