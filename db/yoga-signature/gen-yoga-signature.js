(function(){'use strict';
/* JAH The Yoga Signature Database generator — jahdb-yoga-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-YOGAS-";
var FIELDS=["Foundations","Standing Poses","Seated & Floor Poses","Breathing","Sequences & Flows","Styles","Meditation & Mindfulness"];
var TOPICS={
 "Foundations": [
  "Yoga Fundamentals: What It Is and Is Not (Signature Edition) - Foundations",
  "Essential Gear and Setting Up Space (Signature Edition) - Foundations",
  "Alignment Principles for Safe Practice (Signature Edition) - Foundations",
  "Yoga Etiquette and Studio Basics (Signature Edition) - Foundations",
  "Building a Home Practice (Signature Edition) - Foundations"
 ],
 "Standing Poses": [
  "Mountain Pose and Standing Foundations (Signature Edition) - Standing Poses",
  "Warrior Poses: I, II, and III (Signature Edition) - Standing Poses",
  "Triangle and Extended Side Angle (Signature Edition) - Standing Poses",
  "Chair Pose and Standing Strength (Signature Edition) - Standing Poses",
  "Balancing Poses: Tree and Eagle (Signature Edition) - Standing Poses",
  "Standing Forward Folds and Halfway Lift (Signature Edition) - Standing Poses"
 ],
 "Seated & Floor Poses": [
  "Seated Posture: Easy Pose and Staff Pose (Signature Edition) - Seated & Floor Poses",
  "Seated Forward Folds and Hip Openers (Signature Edition) - Seated & Floor Poses",
  "Backbends: Cobra, Bridge, and Beyond (Signature Edition) - Seated & Floor Poses",
  "Twists: Seated and Supine (Signature Edition) - Seated & Floor Poses",
  "Restorative Poses and Savasana (Signature Edition) - Seated & Floor Poses"
 ],
 "Breathing": [
  "Breath Awareness: The Foundation (Signature Edition) - Breathing",
  "Ujjayi Breath: The Ocean Sound (Signature Edition) - Breathing",
  "Calming Breaths: 4-7-8 and Box Breathing (Signature Edition) - Breathing",
  "Energizing Breaths: Kapalabhati Basics (Signature Edition) - Breathing"
 ],
 "Sequences & Flows": [
  "Sun Salutations: Surya Namaskar (Signature Edition) - Sequences & Flows",
  "Building Your Own Vinyasa Flow (Signature Edition) - Sequences & Flows",
  "Morning Energizing Sequence (Signature Edition) - Sequences & Flows",
  "Evening Wind-Down Sequence (Signature Edition) - Sequences & Flows",
  "Yoga for Desk Workers (Signature Edition) - Sequences & Flows"
 ],
 "Styles": [
  "Hatha Yoga: The Classic Foundation (Signature Edition) - Styles",
  "Vinyasa and Power Yoga (Signature Edition) - Styles",
  "Yin and Restorative Yoga (Signature Edition) - Styles",
  "Choosing Your Yoga Style (Signature Edition) - Styles"
 ],
 "Meditation & Mindfulness": [
  "Meditation Basics for Beginners (Signature Edition) - Meditation & Mindfulness",
  "Body Scan Meditation (Signature Edition) - Meditation & Mindfulness",
  "Mindfulness in Daily Life (Signature Edition) - Meditation & Mindfulness",
  "Yoga Nidra: Yogic Sleep (Signature Edition) - Meditation & Mindfulness",
  "Building a Sustainable Contemplative Practice (Signature Edition) - Meditation & Mindfulness"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Yoga Study — "+safe+"\n"
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
    name:topic+' — yoga guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A yoga guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"yoga-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-yoga-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('yoga-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
