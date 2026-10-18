(function(){'use strict';
/* JAH The Mysterious Photograph Signature Database generator — jahdb-db-mysterious-photograph-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MMPDS-";
var FIELDS=["Street Scenes","Interiors","Landscapes"];
var TOPICS={
 "Street Scenes": [
  "The Empty Street (Signature Edition) \u2014 Street Scenes",
  "The Signature Method for The Empty Street \u2014 Street Scenes",
  "The Wrong Shadow (Signature Edition) \u2014 Street Scenes",
  "The Signature Method for The Wrong Shadow \u2014 Street Scenes",
  "The Crowd With One Face (Signature Edition) \u2014 Street Scenes",
  "The Signature Method for The Crowd With One Face \u2014 Street Scenes",
  "The Fireworks in Daylight (Signature Edition) \u2014 Street Scenes",
  "The Signature Method for The Fireworks in Daylight \u2014 Street Scenes",
  "The Photographer's Notebook (Signature Edition) \u2014 Street Scenes",
  "The Signature Method for The Photographer's Notebook \u2014 Street Scenes"
 ],
 "Interiors": [
  "The Window Reflection (Signature Edition) \u2014 Interiors",
  "The Signature Method for The Window Reflection \u2014 Interiors",
  "The Two Clocks (Signature Edition) \u2014 Interiors",
  "The Signature Method for The Two Clocks \u2014 Interiors",
  "The Mirror With No Photographer (Signature Edition) \u2014 Interiors",
  "The Signature Method for The Mirror With No Photographer \u2014 Interiors",
  "The Set Table (Signature Edition) \u2014 Interiors",
  "The Signature Method for The Set Table \u2014 Interiors",
  "The Endless Staircase (Signature Edition) \u2014 Interiors",
  "The Signature Method for The Endless Staircase \u2014 Interiors",
  "The Portrait's Eyes (Signature Edition) \u2014 Interiors",
  "The Signature Method for The Portrait's Eyes \u2014 Interiors",
  "The Developing Tray (Signature Edition) \u2014 Interiors",
  "The Signature Method for The Developing Tray \u2014 Interiors"
 ],
 "Landscapes": [
  "The Footprints (Signature Edition) \u2014 Landscapes",
  "The Signature Method for The Footprints \u2014 Landscapes",
  "The Frozen Birds (Signature Edition) \u2014 Landscapes",
  "The Signature Method for The Frozen Birds \u2014 Landscapes",
  "The Lighthouse With No Light (Signature Edition) \u2014 Landscapes",
  "The Signature Method for The Lighthouse With No Light \u2014 Landscapes",
  "The Train With No Tracks (Signature Edition) \u2014 Landscapes",
  "The Signature Method for The Train With No Tracks \u2014 Landscapes",
  "The Harbor at Low Tide (Signature Edition) \u2014 Landscapes",
  "The Signature Method for The Harbor at Low Tide \u2014 Landscapes"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Mysterious Photograph Study — "+safe+"\n"
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
    name:topic+' — mysterious photograph record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A mysterious photograph record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-db-mysterious-photograph-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-mysterious-photograph-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
