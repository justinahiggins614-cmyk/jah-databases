(function(){'use strict';
/* JAH The Unusual Footprint Signature Database generator — jahdb-db-unusual-footprint-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MUFDS-";
var FIELDS=["Snow Tracks","Mud Tracks","Dust Tracks"];
var TOPICS={
 "Snow Tracks": [
  "Prints in Fresh Snow (Signature Edition) \u2014 Snow Tracks",
  "The Signature Method for Prints in Fresh Snow \u2014 Snow Tracks",
  "The Snowshoe Hare (Signature Edition) \u2014 Snow Tracks",
  "The Signature Method for The Snowshoe Hare \u2014 Snow Tracks",
  "The Tracker's Eye (Signature Edition) \u2014 Snow Tracks",
  "The Signature Method for The Tracker's Eye \u2014 Snow Tracks"
 ],
 "Mud Tracks": [
  "The Muddy Boot (Signature Edition) \u2014 Mud Tracks",
  "The Signature Method for The Muddy Boot \u2014 Mud Tracks",
  "The Beach at Dawn (Signature Edition) \u2014 Mud Tracks",
  "The Signature Method for The Beach at Dawn \u2014 Mud Tracks",
  "The Forest Path (Signature Edition) \u2014 Mud Tracks",
  "The Signature Method for The Forest Path \u2014 Mud Tracks",
  "The Garden Beds (Signature Edition) \u2014 Mud Tracks",
  "The Signature Method for The Garden Beds \u2014 Mud Tracks",
  "The Stream Crossing (Signature Edition) \u2014 Mud Tracks",
  "The Signature Method for The Stream Crossing \u2014 Mud Tracks",
  "The Meadow Dance (Signature Edition) \u2014 Mud Tracks",
  "The Signature Method for The Meadow Dance \u2014 Mud Tracks",
  "The Orchard Rows (Signature Edition) \u2014 Mud Tracks",
  "The Signature Method for The Orchard Rows \u2014 Mud Tracks",
  "The Marsh Crossing (Signature Edition) \u2014 Mud Tracks",
  "The Signature Method for The Marsh Crossing \u2014 Mud Tracks"
 ],
 "Dust Tracks": [
  "Dust on the Attic Floor (Signature Edition) \u2014 Dust Tracks",
  "The Signature Method for Dust on the Attic Floor \u2014 Dust Tracks",
  "Prints on the Roof (Signature Edition) \u2014 Dust Tracks",
  "The Signature Method for Prints on the Roof \u2014 Dust Tracks",
  "The Barn Floor (Signature Edition) \u2014 Dust Tracks",
  "The Signature Method for The Barn Floor \u2014 Dust Tracks",
  "The Cellar Steps (Signature Edition) \u2014 Dust Tracks",
  "The Signature Method for The Cellar Steps \u2014 Dust Tracks",
  "The Cliff Edge (Signature Edition) \u2014 Dust Tracks",
  "The Signature Method for The Cliff Edge \u2014 Dust Tracks",
  "The Cave Mouth (Signature Edition) \u2014 Dust Tracks",
  "The Signature Method for The Cave Mouth \u2014 Dust Tracks"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Tracking Study — "+safe+"\n"
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
    name:topic+' — tracking puzzle record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A tracking puzzle record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-db-unusual-footprint-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-unusual-footprint-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
