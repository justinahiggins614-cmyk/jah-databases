(function(){'use strict';
/* JAH The Sambo Combat Signature Database generator — jahdb-combat-sambo-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBSAMS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Sambo Stance and Base (Signature Edition) - Foundations",
  "Breakfalls: Sambo Ukemi (Signature Edition) - Foundations",
  "The Sambo Jacket Grips (Signature Edition) - Foundations",
  "Sambo Footwork (Signature Edition) - Foundations",
  "Kuzushi: Breaking Balance (Signature Edition) - Foundations",
  "The Sambo Tie-Up and Clinch Entry (Signature Edition) - Foundations",
  "Posture and Frame in the Clinch (Signature Edition) - Foundations",
  "Hip Escape and Shrimping (Signature Edition) - Foundations",
  "Bridging and Rolling Escapes (Signature Edition) - Foundations",
  "Sambo Rules and Scoring Basics (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "O Soto Gari: Major Outer Reap (Signature Edition) - Compounded",
  "De Ashi Harai: Advancing Foot Sweep (Signature Edition) - Compounded",
  "Ko Uchi Gari: Minor Inner Reap (Signature Edition) - Compounded",
  "Seoi Nage: Shoulder Throw (Signature Edition) - Compounded",
  "Harai Goshi: Sweeping Hip Throw (Signature Edition) - Compounded",
  "Uchi Mata: Inner Thigh Throw (Signature Edition) - Compounded",
  "Morote Gari: Double Leg Takedown (Signature Edition) - Compounded",
  "Sprawl and Takedown Defense (Signature Edition) - Compounded",
  "Side Control: Kesa Gatame (Signature Edition) - Compounded",
  "Mount Control: Tate Shiho Gatame (Signature Edition) - Compounded",
  "Back Control and the Rear Choke (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Juji Gatame: Straight Armbar (Signature Edition) - Advanced",
  "Ude Garami: Kimura (Signature Edition) - Advanced",
  "Achilles Lock: Straight Ankle Lock (Signature Edition) - Advanced",
  "Knee Bar: Leg Bar Submission (Signature Edition) - Advanced",
  "Toe Hold: Foot Lock (Signature Edition) - Advanced",
  "Throwing Combinations: Renzoku Waza (Signature Edition) - Advanced",
  "Counter Throwing: Kaeshi Waza (Signature Edition) - Advanced",
  "Combat Sambo Striking Entries (Signature Edition) - Advanced",
  "Combat Sambo Clinch Striking (Signature Edition) - Advanced",
  "Combat Sambo Kick Defense and Counters (Signature Edition) - Advanced",
  "Ground Striking Defense in Combat Sambo (Signature Edition) - Advanced",
  "Ura Nage: Rear Throw (Signature Edition) - Advanced",
  "Sambo Fight Strategy: Game Planning (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Sambo Technique Study — "+safe+"\n"
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
    name:topic+' — combat technique record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A combat technique record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"sambo-technique-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-combat-sambo-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-sambo-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
