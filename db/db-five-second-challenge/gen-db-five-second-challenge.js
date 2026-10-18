(function(){'use strict';
/* JAH The Five-Second Challenge Database generator — jahdb-db-five-second-challenge-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FSC-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Speedy Starters",
  "Quick-Think Warm-Ups",
  "First Five Seconds",
  "Rapid Basics",
  "Fast & Friendly",
  "Tempo Trainers",
  "Zippy Round One",
  "Quickfire Classics",
  "Starter Sprints",
  "Easy-Peasy Pace",
  "Gentle Lightning"
 ],
 "Compounded": [
  "Quicker Wits",
  "Tempo Risers",
  "Swift Thinkers",
  "Rapid Recallers",
  "Speed Demons Practice",
  "Quick-Draw Dozen",
  "Fast Talkers Set",
  "Blink-and-Answer",
  "High-Tempo Tens",
  "Turbo Thinkers",
  "Lightning Learners",
  "Championship Countdown"
 ],
 "Advanced": [
  "Sudden Death Elite",
  "Grand Timer Finals",
  "Signature Stopwatch Round",
  "Five-Second Masters",
  "Ultimate Rapid Fire",
  "Pro Pace Pack",
  "Hall of Fame Hurry",
  "The Final Countdown",
  "Speed Champions Set",
  "Signature Showdown Sprint",
  "The Thousand-Tick Finale"
 ]
};
var DEMOKIND="pack-simulator";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Five-Second Challenge simulator — "+safe+"\n"
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
    name:topic+' — challenge pack',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A challenge pack of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-db-five-second-challenge-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-five-second-challenge',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
