(function(){'use strict';
/* JAH The Build a Civilization Database generator — jahdb-db-build-a-civilization-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBCD-";
var FIELDS=["Foundations","Systems","Culture"];
var TOPICS={
 "Foundations": [
  "The River Valley Civilization \u2014 Foundations",
  "The River Valley Civilization \u2014 Deep Dive \u2014 Foundations",
  "The Arcology Civilization \u2014 Foundations",
  "The Arcology Civilization \u2014 Deep Dive \u2014 Foundations",
  "The Nomadic Civilization \u2014 Foundations",
  "The Nomadic Civilization \u2014 Deep Dive \u2014 Foundations",
  "The Island Network \u2014 Foundations",
  "The Island Network \u2014 Deep Dive \u2014 Foundations",
  "The Mountain Fastness \u2014 Foundations",
  "The Mountain Fastness \u2014 Deep Dive \u2014 Foundations",
  "The Desert Oasis Chain \u2014 Foundations",
  "The Desert Oasis Chain \u2014 Deep Dive \u2014 Foundations"
 ],
 "Systems": [
  "The Forest Canopy \u2014 Systems",
  "The Forest Canopy \u2014 Deep Dive \u2014 Systems",
  "The Undercity \u2014 Systems",
  "The Undercity \u2014 Deep Dive \u2014 Systems",
  "The Floating Cities \u2014 Systems",
  "The Floating Cities \u2014 Deep Dive \u2014 Systems",
  "The Orbital Ring \u2014 Systems",
  "The Orbital Ring \u2014 Deep Dive \u2014 Systems",
  "The Digital Commonwealth \u2014 Systems",
  "The Digital Commonwealth \u2014 Deep Dive \u2014 Systems"
 ],
 "Culture": [
  "The Symbiotic Cities \u2014 Culture",
  "The Symbiotic Cities \u2014 Deep Dive \u2014 Culture",
  "The Monastic Network \u2014 Culture",
  "The Monastic Network \u2014 Deep Dive \u2014 Culture",
  "The Trader Confederacy \u2014 Culture",
  "The Trader Confederacy \u2014 Deep Dive \u2014 Culture",
  "The Scholar's Republic \u2014 Culture",
  "The Scholar's Republic \u2014 Deep Dive \u2014 Culture",
  "The Festival Circuit \u2014 Culture",
  "The Festival Circuit \u2014 Deep Dive \u2014 Culture",
  "The Civilization Engine \u2014 Culture",
  "The Civilization Engine \u2014 Deep Dive \u2014 Culture"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Civilization Design Study — "+safe+"\n"
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
    name:topic+' — civilization design record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A civilization design record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-db-build-a-civilization-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-build-a-civilization',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
