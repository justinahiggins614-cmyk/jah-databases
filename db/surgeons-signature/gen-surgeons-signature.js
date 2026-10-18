(function(){'use strict';
/* JAH Signature Surgeons Database generator — jahdb-surgeons-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SRGNS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Signature Pre-Op Pause",
  "Signature Scenario: The Bleeding You Cannot See",
  "The Signature Instrument Naming Game",
  "Signature Knot-Tying Ladder",
  "Signature Scrub Ritual Teaching",
  "Signature Hemostasis Drill",
  "Signature Timeout Song",
  "Signature Recovery Coaching Cards",
  "Signature Consent Conversation Map",
  "Signature Surgical Timeline Wall",
  "Signature First-Assist Training",
 ],
 "Compounded": [
  "Signature Complex Abdomen Workshop",
  "Signature Bypass Simulation Lab",
  "Signature Aneurysm Decision Board",
  "Signature Saw-Bone Bootcamp",
  "Signature Flap Design Studio",
  "Signature Limb Salvage Pathway",
  "Signature Neonatal OR Setup",
  "Signature Tumor Board Simulation",
  "Signature Massive Transfusion Drill",
  "Signature Skills Decathlon",
  "Signature Checklist Champion Program",
  "Signature Complication Conversation Training",
 ],
 "Advanced": [
  "Signature Beating-Heart Masterclass",
  "Signature Skull-Base Lab",
  "Signature Revision Joint Symposium",
  "Signature Supermicrosurgery Course",
  "Signature Complex Aorta Program",
  "Signature Fetal Surgery Pathway",
  "Signature Cytoreduction Fellowship",
  "Signature Trauma Systems Design",
  "Signature Scarless Surgery Lab",
  "Signature Surgeon Legacy Lectures",
  "Signature Surgical Innovation Incubator",
 ],
};
var DEMOKIND="surgical calculation";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Surgical calculator — "+safe+"\n"
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
    name:topic+' — surgeon profession record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A miners profession record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-surgeons-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('surgeons-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
