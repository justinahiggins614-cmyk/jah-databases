(function(){'use strict';
/* JAH Sports Medicine Injuries Signature Database generator — jahdb-sports-medicine-injuries-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SPORTMEDS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The RICE and POLICE Protocols (Signature Edition)", "Sprains vs Strains (Signature Edition)", "Contusions (Bruises) (Signature Edition)", "Muscle Cramps (Signature Edition)", "Blisters and Skin Care (Signature Edition)", "Dehydration Signs (Signature Edition)", "Heat Exhaustion vs Heat Stroke (Signature Edition)", "Concussion Recognition Basics (Signature Edition)", "When to See a Doctor (Signature Edition)", "The Athlete First-Aid Kit (Signature Edition)", "Safe Return-to-Play Principles (Signature Edition)"], "Compounded": ["ACL Tears (Mechanism and Rehab) (Signature Edition)", "Meniscus Injuries (Signature Edition)", "Ankle Sprain Grading (Signature Edition)", "Tennis Elbow vs Golfer's Elbow (Signature Edition)", "Rotator Cuff Injuries (Signature Edition)", "Shin Splints (Signature Edition)", "Stress Fractures (Signature Edition)", "Hamstring Strains (Signature Edition)", "Groin Pulls (Adductor Strains) (Signature Edition)", "Lower Back Pain in Athletes (Signature Edition)", "Shoulder Dislocation (Signature Edition)", "Achilles Tendinopathy (Signature Edition)"], "Advanced": ["Concussion Protocols and Graduated Return (Signature Edition)", "Tommy John Surgery (UCL Reconstruction) (Signature Edition)", "Cartilage Restoration Options (Signature Edition)", "PRP and Biologics Evidence (Signature Edition)", "Load Management Science (Signature Edition)", "RED-S (Relative Energy Deficiency in Sport) (Signature Edition)", "Cardiac Screening in Athletes (Signature Edition)", "Mental Health in Injury Rehab (Signature Edition)", "Youth Growth-Plate Injuries (Signature Edition)", "Surgical vs Conservative Decisions (Signature Edition)", "Long-Term Joint Health After Sport (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# rehab-timeline-demo \u2014 "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record \u2014 structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' \u2014 sports medicine record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A sports medicine record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"rehab-timeline-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-sports-medicine-injuries-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('sports-medicine-injuries-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
