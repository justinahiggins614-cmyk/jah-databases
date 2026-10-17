(function(){'use strict';
/* Tiger Kung Fu Combat Signature Database generator — jahdb-combat-tiger-kung-fu-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBTGRS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Signature Claw Formation (Signature Edition)",
  "The Signature Root Stance (Signature Edition)",
  "Signature Fingertip Presses (Signature Edition)",
  "The Signature Sand Dialogue (Signature Edition)",
  "Signature Stalking Steps (Signature Edition)",
  "The Signature Inner Roar (Signature Edition)",
  "Signature Crouch of the Spring (Signature Edition)",
  "The Signature First Rake (Signature Edition)",
  "Signature Catch Without Eyes (Signature Edition)",
  "The Signature Silent Pounce (Signature Edition)",
  "Signature Bridge Listening (Signature Edition)",
  "The Signature Ground Return (Signature Edition)"
 ],
 "Compounded": [
  "Signature Twin Rake Synchronization (Signature Edition)",
  "The Signature Divided Mind (Signature Edition)",
  "Signature Heart of the Technique (Signature Edition)",
  "The Signature Borrowed Grip (Signature Edition)",
  "Signature Pounce With a Witness (Signature Edition)",
  "The Signature Open Hand (Signature Edition)",
  "Signature Tail in the Dark (Signature Edition)",
  "The Signature Quiet Elbow (Signature Edition)",
  "Signature Taming in Silence (Signature Edition)",
  "The Signature Changing Animal (Signature Edition)",
  "Signature Counter in a Phone Booth (Signature Edition)",
  "The Signature Endless Exchange (Signature Edition)"
 ],
 "Advanced": [
  "Signature Hands of Stone, Heart of Water (Signature Edition)",
  "The Signature Unbreakable Thread (Signature Edition)",
  "Signature Tendons of the Bowstring (Signature Edition)",
  "The Signature Circle of Eyes (Signature Edition)",
  "Signature Black Tiger in the Mirror (Signature Edition)",
  "The Signature Small Tiger (Signature Edition)",
  "Signature Tearing of Paper Tigers (Signature Edition)",
  "The Signature One Breath Form (Signature Edition)",
  "Signature Knowledge With a Lock (Signature Edition)",
  "The Signature Living Form (Signature Edition)"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Tiger Kung Fu Study — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "import math\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "claw_rake_m = 0.55\n"
   + "reps = 10\n"
   + "print('Claw travel for %d rakes: %.1f m' % (reps, claw_rake_m * reps))\n"
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
    demo:{kind:"tiger-kung-fu-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-combat-tiger-kung-fu-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-tiger-kung-fu-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
