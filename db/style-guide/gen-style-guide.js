(function(){'use strict';
/* JAH The Style Guide Database generator — jahdb-style-guide-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-STGU-";
var FIELDS=["Style Foundations", "Building a Wardrobe", "Style Mastery"];
var TOPICS={
 "Style Foundations": [
  "What Is Personal Style",
  "Fit First",
  "The Silhouette",
  "Proportion Play",
  "The Capsule Idea",
  "Dressing for You",
  "The Style Icons",
  "The Uniform Trick",
  "Texture Mixing",
  "The Third Piece",
  "The Mirror Check",
  "The Comfort Rule",
  "The Color First Step"
 ],
 "Building a Wardrobe": [
  "The Wardrobe Audit",
  "The Shopping List",
  "Investment Pieces",
  "The Tailor Relationship",
  "Care and Repair",
  "The Style Journal",
  "Seasonal Swaps",
  "The Travel Wardrobe",
  "The Style Rut Rescue",
  "Dressing with Intention",
  "The Borrowed Trick",
  "The Statement Piece",
  "The Quiet Luxury"
 ],
 "Style Mastery": [
  "The Signature Look",
  "Style and Confidence",
  "The Evolving Style",
  "Your Style Legacy",
  "The Style Mentor",
  "The Style Experiment",
  "The Photographed Self",
  "The Style Decade"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# style — "+safe+"\n"
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
    name:topic+' — style guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A style guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"style-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-style-guide-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('style-guide',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
