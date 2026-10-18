(function(){'use strict';
/* JAH Signature Social Bingo Database generator — jahdb-db-social-bingo-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SBSOS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "First Cards",
  "Easy Mixers",
  "Warm-Up Mingles",
  "Gentle Gatherings",
  "Bingo Rookie Pack",
  "Mixer Basics",
  "Friendly Faces",
  "Quick Cards",
  "Bingo Primer",
  "First Ten Cards",
  "Hello Starts"
 ],
 "Compounded": [
  "Deeper Mixers",
  "Bingo Builders",
  "Mingle Stretchers",
  "Real Conversations",
  "Blackout Practice",
  "Connection Training",
  "Skilled Minglers",
  "Bingo Drills",
  "Mixer Practice",
  "Bingo Workshop",
  "Blackout Practice Rounds",
  "Championship Bingo"
 ],
 "Advanced": [
  "Blackout Elite",
  "Grand Bingo Finals",
  "Signature Mingler Night",
  "Ultimate Social Bingo",
  "Bingo All-Stars",
  "Pro Minglers Pack",
  "Hall of Fame Cards",
  "The Final Card",
  "Bingo Masters Set",
  "Signature Showdown Bingo",
  "The Thousand-Card Finale"
 ]
};
var DEMOKIND="pack-simulator";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Social Bingo simulator — "+safe+"\n"
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
    name:topic+' — bingo pack',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A bingo pack of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'signature',
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
var gen={version:'jahdb-db-social-bingo-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-social-bingo-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
