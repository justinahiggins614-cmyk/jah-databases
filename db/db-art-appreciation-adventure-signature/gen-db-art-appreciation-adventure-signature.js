(function(){'use strict';
/* JAH The Art Appreciation Adventure generator — jahdb-db-art-appreciation-adventure-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ARAAS-";
var FIELDS=["Seeing","Movements","Making"];
var TOPICS={
 "Seeing": [
  "How to Look at Art (Signature Edition) - Seeing",
  "Line: The Artist's Handwriting (Signature Edition) - Seeing",
  "Color: Emotion in Pigment (Signature Edition) - Seeing",
  "Light and Shadow (Signature Edition) - Seeing",
  "Composition: Where Things Go (Signature Edition) - Seeing",
  "Perspective: Depth on Flat (Signature Edition) - Seeing",
  "Texture: Feel With Eyes (Signature Edition) - Seeing",
  "Symbolism: Reading Pictures (Signature Edition) - Seeing",
  "Abstract Art: Feeling Without Objects (Signature Edition) - Seeing",
  "Sculpture in the Round (Signature Edition) - Seeing",
  "Photography as Art (Signature Edition) - Seeing",
  "Looking Longer: The 10-Minute Rule (Signature Edition) - Seeing"
 ],
 "Movements": [
  "Cave Paintings: The First Gallery (Signature Edition) - Movements",
  "Classical Ideals: Greece and Rome (Signature Edition) - Movements",
  "Medieval: Heaven in Gold (Signature Edition) - Movements",
  "Renaissance: Rebirth (Signature Edition) - Movements",
  "Baroque: Drama and Light (Signature Edition) - Movements",
  "Impressionism: Light Itself (Signature Edition) - Movements",
  "Modernism: Breaking Rules (Signature Edition) - Movements",
  "Contemporary: Art Now (Signature Edition) - Movements",
  "Art Across Cultures (Signature Edition) - Movements",
  "Women Artists Reclaimed (Signature Edition) - Movements",
  "Street Art: Walls That Speak (Signature Edition) - Movements"
 ],
 "Making": [
  "Your First Sketchbook (Signature Edition) - Making",
  "Drawing What You See (Signature Edition) - Making",
  "Color Mixing Basics (Signature Edition) - Making",
  "Try Watercolor (Signature Edition) - Making",
  "Try Clay (Signature Edition) - Making",
  "Photography Walks (Signature Edition) - Making",
  "Collage: Art From Scraps (Signature Edition) - Making",
  "Visit Museums Like a Pro (Signature Edition) - Making",
  "Start Collecting (Signature Edition) - Making",
  "Share Your Art (Signature Edition) - Making",
  "Try Printmaking (Signature Edition) - Making"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Art Appreciation Study — "+safe+"\n"
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
    name:topic+' — art lesson record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A art lesson record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"art-appreciation-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-art-appreciation-adventure-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-art-appreciation-adventure-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
