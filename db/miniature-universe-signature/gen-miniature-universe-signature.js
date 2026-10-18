(function(){'use strict';
/* JAH The Miniature Universe Database generator — jahdb-miniature-universe-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MUNVS-";
var FIELDS=["Small-Scale Foundations", "Scene Building", "Master Worlds"];
var TOPICS={
 "Small-Scale Foundations": [
  "What Is a Miniature Universe",
  "Scale Ratios Explained",
  "Choosing Your First Scale",
  "Tools of the Miniaturist",
  "Materials: Balsa to Brass",
  "Painting Tiny Surfaces",
  "Lighting a Tiny World",
  "Bases and Display Cases",
  "The 1:12 Dollhouse Standard",
  "Model Railroad Scales",
  "Forced Perspective Basics",
  "Tiny Text and Signage"
 ],
 "Scene Building": [
  "A Tiny Kitchen",
  "A Miniature Library",
  "A Corner Bookshop",
  "A Tiny Greenhouse",
  "A Miniature Workshop",
  "A Tiny Cafe Interior",
  "A Miniature Garden",
  "A Tiny Train Station",
  "A Miniature Harbor",
  "A Tiny Observatory",
  "A Miniature Theater Stage"
 ],
 "Master Worlds": [
  "The Floating Island Diorama",
  "The Tiny City Block",
  "A Miniature Desert Canyon",
  "The Underwater Reef in a Jar",
  "A Tiny Winter Village",
  "The Miniature Space Station",
  "A Tiny Medieval Market",
  "The Miniature Jungle Canopy",
  "A Tiny Lighthouse Coast",
  "The Miniature Volcano Island",
  "The Living Ecosystem Terrarium"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# miniature — "+safe+"\n"
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
    name:topic+' — miniature universe concept record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A miniature universe concept record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"miniature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-miniature-universe-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('miniature-universe-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
