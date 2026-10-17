(function(){'use strict';
/* JAH The Fencing Combat Signature Database generator — jahdb-combat-fencing-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBFENS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Signature Mask and Jacket: The Armor of the Oath (Signature Edition) - Foundations",
  "The Three Signature Blades: Foil, Epee, Sabre in the Signature System (Signature Edition) - Foundations",
  "The Signature En Garde: The Covenant Stance (Signature Edition) - Foundations",
  "The Signature Advance: Ground Taken by Oath (Signature Edition) - Foundations",
  "The Signature Retreat: Ground Held, Not Lost (Signature Edition) - Foundations",
  "The Signature Grip: The Hand That Signs (Signature Edition) - Foundations",
  "Signature Point Control: The Line That Never Wavers (Signature Edition) - Foundations",
  "The Signature Lunge: The Signed Strike (Signature Edition) - Foundations",
  "The Signature Recovery: Return to the Line (Signature Edition) - Foundations",
  "The Signature Thrust: The First True Attack (Signature Edition) - Foundations",
  "Signature Parry Four: The Inner Gate (Signature Edition) - Foundations",
  "Signature Parry Six: The Outer Gate (Signature Edition) - Foundations",
  "Signature Parry Seven: The Low Inner Wall (Signature Edition) - Foundations",
  "Signature Parry Eight: The Low Outer Wall (Signature Edition) - Foundations",
 ],
 "Compounded": [
  "Signature Prime: The Sweeping Seal (Signature Edition) - Compounded",
  "Signature Seconde: The Low Ward (Signature Edition) - Compounded",
  "Signature Tierce: The High Ward (Signature Edition) - Compounded",
  "Signature Quinte: The Crown Guard (Signature Edition) - Compounded",
  "The Signature Riposte: The Answered Oath (Signature Edition) - Compounded",
  "The Signature Indirect Answer: The Hidden Reply (Signature Edition) - Compounded",
  "The Signature Beat: The Knocking Blow (Signature Edition) - Compounded",
  "The Signature Disengage: The Slipping Line (Signature Edition) - Compounded",
  "The Signature Feint: The False Signature (Signature Edition) - Compounded",
  "The Signature Counter-Attack: The Bold Interception (Signature Edition) - Compounded",
 ],
 "Advanced": [
  "The Signature Bind: The Taken Blade (Signature Edition) - Advanced",
  "The Signature Balestra: The Leaping Oath (Signature Edition) - Advanced",
  "The Signature Fleche: The Arrow Cast (Signature Edition) - Advanced",
  "The Signature Circle: The Unbroken Ring (Signature Edition) - Advanced",
  "Signature Counter-Time: The Set Snare (Signature Edition) - Advanced",
  "Signature Second Intention: The Double-Sealed Plan (Signature Edition) - Advanced",
  "Signature Priority: The Law of the First Line (Signature Edition) - Advanced",
  "Signature Sabre: The Cutting Covenant (Signature Edition) - Advanced",
  "Signature Epee: The Whole-Body Ledger (Signature Edition) - Advanced",
  "Signature Bout Craft: The Piste as Proving Ground (Signature Edition) - Advanced",
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Fencing Technique Study \u2014 "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {\"title\": \""+safe+"\", \"field\": \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r[\"title\"] + \" [\" + r[\"field\"] + \"]\"\n"
   + "print(summarize(record))\n"
   + "print(\"Sample record - structural sample, not an archive entry.\")\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' \u2014 combat technique record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A combat technique record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"fencing-technique-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-combat-fencing-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-fencing-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
