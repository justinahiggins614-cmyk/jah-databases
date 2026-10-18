(function(){'use strict';
/* JAH The Minute-to-Win-It Database generator — jahdb-db-minute-to-win-it-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MTWI-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "First Stunts",
  "Easy Wins",
  "Warm-Up Minute Wonders",
  "Gentle Challenges",
  "Stunt Rookie Pack",
  "Stunt Basics",
  "Friendly Feats",
  "Quick Stunts",
  "Stunt Primer",
  "First Ten Stunts",
  "Confident Starts"
 ],
 "Compounded": [
  "Trickier Stunts",
  "Stunt Builders",
  "Feat Stretchers",
  "Real Stunt Work",
  "Gauntlet Practice",
  "Skill Training",
  "Steady Hands",
  "Stunt Drills",
  "Precision Practice",
  "Stunt Workshop",
  "Gauntlet Minute Practice Rounds",
  "Championship Stunts"
 ],
 "Advanced": [
  "Gauntlet Minute Elite",
  "Grand Stunt Finals",
  "Signature Stopwatch Night",
  "Ultimate Minute to Win It",
  "Stunt All-Stars",
  "Pro Stunters Pack",
  "Hall of Fame Stunts",
  "The Final Second",
  "Stunt Masters Set",
  "Signature Showdown Stunts",
  "The Thousand-Second Finale"
 ]
};
var DEMOKIND="pack-simulator";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Minute to Win It simulator — "+safe+"\n"
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
    name:topic+' — stunt pack',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A stunt pack of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-db-minute-to-win-it-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-minute-to-win-it',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
