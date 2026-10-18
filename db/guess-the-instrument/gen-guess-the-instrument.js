(function(){'use strict';
/* JAH The Guess the Instrument Database generator — jahdb-guess-the-instrument-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GTIN-";
var FIELDS=["Listening Foundations", "Quiz Rounds", "Quiz Mastery"];
var TOPICS={
 "Listening Foundations": [
  "The Four Families",
  "Strings: Bowed vs Plucked",
  "Winds: Wood vs Brass",
  "The Piano Paradox",
  "High Strings",
  "Low Strings",
  "The Flute Family",
  "The Clarinet vs Oboe",
  "Brass: Trumpet vs Trombone",
  "The Drum Kit Voices"
 ],
 "Quiz Rounds": [
  "The Saxophone Family",
  "The Guitar Cousins",
  "The Keyboard Cousins",
  "World Winds",
  "World Strings",
  "World Percussion",
  "The Electronic Impostors",
  "The Hybrid Challenge",
  "The Blindfold Round",
  "The Speed Round",
  "The Harp vs Piano",
  "The Accordion Family",
  "The Organ Cousins",
  "The Mallet Family",
  "The Hand Drum Circle"
 ],
 "Quiz Mastery": [
  "The Stumpers",
  "The Orchestra Map",
  "The Ensemble Ear",
  "The Solo Spotlight",
  "Your Listening Legacy",
  "The Quiz Master",
  "The Listening Party",
  "The Tournament",
  "Your Recognition Legacy"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# guess — "+safe+"\n"
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
    name:topic+' — guess the instrument record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A guess the instrument record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"guess-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-guess-the-instrument-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('guess-the-instrument',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
