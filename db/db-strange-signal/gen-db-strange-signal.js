(function(){'use strict';
/* JAH The Strange Signal Database generator — jahdb-db-strange-signal-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MSSD-";
var FIELDS=["From Space","From Earth","From the Sea"];
var TOPICS={
 "From Space": [
  "The Wow! Signal \u2014 From Space",
  "The Wow! Signal \u2014 Deep Dive \u2014 From Space",
  "The First Pulsar (LGM-1) \u2014 From Space",
  "The First Pulsar (LGM-1) \u2014 Deep Dive \u2014 From Space",
  "Fast Radio Bursts \u2014 From Space",
  "Fast Radio Bursts \u2014 Deep Dive \u2014 From Space",
  "Jupiter's Radio Voice \u2014 From Space",
  "Jupiter's Radio Voice \u2014 Deep Dive \u2014 From Space",
  "'Oumuamua's Signal \u2014 From Space",
  "'Oumuamua's Signal \u2014 Deep Dive \u2014 From Space",
  "How to Read a Signal \u2014 From Space",
  "How to Read a Signal \u2014 Deep Dive \u2014 From Space"
 ],
 "From Earth": [
  "UVB-76 (The Buzzer) \u2014 From Earth",
  "UVB-76 (The Buzzer) \u2014 Deep Dive \u2014 From Earth",
  "Numbers Stations \u2014 From Earth",
  "Numbers Stations \u2014 Deep Dive \u2014 From Earth",
  "The Perytons \u2014 From Earth",
  "The Perytons \u2014 Deep Dive \u2014 From Earth",
  "The Schumann Resonances \u2014 From Earth",
  "The Schumann Resonances \u2014 Deep Dive \u2014 From Earth",
  "Skyquakes \u2014 From Earth",
  "Skyquakes \u2014 Deep Dive \u2014 From Earth"
 ],
 "From the Sea": [
  "The Bloop \u2014 From the Sea",
  "The Bloop \u2014 Deep Dive \u2014 From the Sea",
  "The 52-Hertz Whale \u2014 From the Sea",
  "The 52-Hertz Whale \u2014 Deep Dive \u2014 From the Sea",
  "Upsweep and Slow Down \u2014 From the Sea",
  "Upsweep and Slow Down \u2014 Deep Dive \u2014 From the Sea",
  "Julia \u2014 From the Sea",
  "Julia \u2014 Deep Dive \u2014 From the Sea",
  "The Train \u2014 From the Sea",
  "The Train \u2014 Deep Dive \u2014 From the Sea",
  "The Whistle \u2014 From the Sea",
  "The Whistle \u2014 Deep Dive \u2014 From the Sea"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Strange Signal Study — "+safe+"\n"
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
    name:topic+' — strange signal record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A strange signal record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-db-strange-signal-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-strange-signal',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
