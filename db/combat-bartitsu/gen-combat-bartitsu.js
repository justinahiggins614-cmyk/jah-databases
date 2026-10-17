(function(){'use strict';
/* JAH Bartitsu Combat Database generator — jahdb-combat-bartitsu-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBBA-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Bartitsu: The Victorian Art of Self-Defense - Foundations",
  "The Bartitsu Guard Stance - Foundations",
  "Bartitsu Footwork: Advance, Retreat, and Side Step - Foundations",
  "The Vigny Cane Grip and Basic Portes - Foundations",
  "Ukemi: How to Fall Safely - Foundations",
  "The Straight Blow: Bartitsu Boxing Basics - Foundations",
  "The Savate Front Kick - Foundations",
  "Cane Guards: Tierce and Quarte - Foundations",
  "Distance and Timing: The Measure of the Fight - Foundations",
  "Basic Cane Parries - Foundations"
 ],
 "Compounded": [
  "The Vigny Overhead Cut - Compounded",
  "The Moulinet: Figure-of-Eight Cane Strike - Compounded",
  "O Goshi: The Cross Buttock Hip Throw - Compounded",
  "The Hook Punch - Compounded",
  "The Savate Low Kick: Coup de Pied Bas - Compounded",
  "The Cane Thrust - Compounded",
  "Kotegaeshi: The Standing Wrist Lock - Compounded",
  "The Chasse: Savate Side Kick - Compounded",
  "The Uppercut and Body Blow - Compounded",
  "The Cane Hook Disarm - Compounded",
  "The Hip Throw with Cane Assist - Compounded",
  "Combination Striking: Punch-Kick Flow - Compounded",
  "Seoi Nage: The Shoulder Throw - Compounded",
  "Balayage: The Savate Foot Sweep - Compounded"
 ],
 "Advanced": [
  "Juji Gatame: The Straight Armlock - Advanced",
  "Defending Against a Knife Attack - Advanced",
  "The Flying Mare Throw - Advanced",
  "Counter-Punching and the Riposte - Advanced",
  "Awareness Against Multiple Opponents - Advanced",
  "The Two-Handed Cane Trap - Advanced",
  "Hadaka Jime: The Rear Choke and Its Defense - Advanced",
  "Randori: Bartitsu Freestyle Sparring - Advanced",
  "The Grand Combination: The Complete Bartitsu Sequence - Advanced",
  "Preserving the Art: Teaching Bartitsu - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Bartitsu Study — "+safe+"\n"
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
    demo:{kind:"bartitsu-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-combat-bartitsu-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-bartitsu',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
