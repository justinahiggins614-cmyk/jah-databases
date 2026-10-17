(function(){'use strict';
/* JAH The Ornithology Database generator — jahdb-ornithology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ORN-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Ornithology: The Science of Birds \u2014 Foundations",
  "Feathers: The Defining Innovation of Birds \u2014 Foundations",
  "Feather Types: Contour, Flight, Down, and More \u2014 Foundations",
  "The Bird Skeleton: Light, Rigid, and Built to Fly \u2014 Foundations",
  "Beaks: The Bird's All-Purpose Tool \u2014 Foundations",
  "Feet and Legs: Built for a Lifestyle \u2014 Foundations",
  "The Avian Respiratory System: Breathing on the Move \u2014 Foundations",
  "Bird Senses: Seeing the World Like a Bird \u2014 Foundations",
  "Staying Warm: Bird Thermoregulation \u2014 Foundations"
 ],
 "Compounded": [
  "How Birds Fly: Lift, Drag, Thrust, and Weight \u2014 Compounded",
  "Wing Shapes and Flight Styles \u2014 Compounded",
  "Flapping Flight: The Power Stroke and Recovery \u2014 Compounded",
  "Soaring and Gliding: The Free Ride \u2014 Compounded",
  "Migration I: Why Birds Travel the World \u2014 Compounded",
  "Migration II: How Birds Navigate \u2014 Compounded",
  "The Syrinx: The Bird Voice Box \u2014 Compounded",
  "Birdsong II: Learning, Dialects, and Repertoires \u2014 Compounded",
  "Calls: The Bird's Everyday Language \u2014 Compounded",
  "Breeding Systems: Monogamy, Polygyny, Leks, and More \u2014 Compounded",
  "Nests: Architecture for Eggs \u2014 Compounded",
  "Eggs, Incubation, and Parental Care \u2014 Compounded",
  "Foraging Ecology: How Birds Make a Living \u2014 Compounded",
  "Avian Taxonomy: The Orders of Birds \u2014 Compounded",
  "Molt: Replacing the Plumage \u2014 Compounded"
 ],
 "Advanced": [
  "The Energy Cost of Flight \u2014 Advanced",
  "High-Altitude Flight: Thin-Air Physiology \u2014 Advanced",
  "The Magnetic Compass: Quantum Navigation \u2014 Advanced",
  "Population Ecology: Banding, Survival, Recruitment \u2014 Advanced",
  "Conservation Ornithology: Declines and Recoveries \u2014 Advanced",
  "Climate Change and Birds \u2014 Advanced",
  "Field Methods: Counts, Transects, and Mist Nets \u2014 Advanced",
  "Bioacoustics: Recording and Analyzing Birdsong \u2014 Advanced",
  "Avian Cognition: Tool Use, Memory, and Problem Solving \u2014 Advanced",
  "Speciation in Birds: How New Species Arise \u2014 Advanced",
  "Avian Disease Ecology: Bird Flu and Beyond \u2014 Advanced",
  "Conservation Genetics: Reading Feathers for DNA \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Ornithology Study — "+safe+"\n"
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
    name:topic+' — ornithology record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A ornithology record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"ornithology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-ornithology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('ornithology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
