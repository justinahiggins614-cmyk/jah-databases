(function(){'use strict';
/* JAH The Fencing Combat Database generator — jahdb-combat-fencing-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBFEN-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Fencing Safety Gear: The Mask, Jacket, and Glove - Foundations",
  "The Three Weapons: Foil, Epee, and Sabre - Foundations",
  "The En Garde Stance - Foundations",
  "The Advance: Moving Forward - Foundations",
  "The Retreat: Moving Back - Foundations",
  "The Grip: Fingers on the Weapon - Foundations",
  "Point Control and the Target - Foundations",
  "The Lunge - Foundations",
  "The Recovery - Foundations",
  "The Straight Thrust: The Simple Attack - Foundations",
  "Parry Four: The Inside High Parry - Foundations",
  "Parry Six: The Outside High Parry - Foundations",
  "Parry Seven: The Inside Low Parry - Foundations",
  "Parry Eight: The Outside Low Parry - Foundations",
 ],
 "Compounded": [
  "Parry One (Prime): The Inside Sweep - Compounded",
  "Parry Two (Seconde): The Outside Low Line - Compounded",
  "Parry Three (Tierce): The Outside High Line - Compounded",
  "Parry Five (Quinte): The Head Parry - Compounded",
  "The Direct Riposte - Compounded",
  "The Indirect Riposte: Disengage and Cutover - Compounded",
  "The Beat: Striking the Blade - Compounded",
  "The Disengage: Evading the Parry - Compounded",
  "The Feint: The False Attack - Compounded",
  "The Counter-Attack - Compounded",
 ],
 "Advanced": [
  "The Bind (Liement): Taking the Blade - Advanced",
  "The Balestra: The Hop Lunge - Advanced",
  "The Fleche: The Running Attack - Advanced",
  "The Circular Parry (Counter-Parry) - Advanced",
  "Counter-Time: The Planned Invitation - Advanced",
  "Second Intention: The Two-Tempo Trap - Advanced",
  "Right-of-Way in Foil: Who Scores - Advanced",
  "Sabre: Target, Cuts, and Priority - Advanced",
  "Epee: The Whole Body and the Double Touch - Advanced",
  "Bout Craft: The Piste, the Clock, and Penalties - Advanced",
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
var gen={version:'jahdb-combat-fencing-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-fencing',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
