(function(){'use strict';
/* JAH Reproductive Health Information Database generator — jahdb-reproductive-health-information-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-REPRHIS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Understanding Fertility (Signature Edition)", "Contraception Overview (Signature Edition)", "Barrier Methods (Signature Edition)", "Hormonal Contraception (Signature Edition)", "Long-Acting Methods (Signature Edition)", "Emergency Contraception (Signature Edition)", "Permanent Options (Signature Edition)", "Fertility Awareness (Signature Edition)", "Preconception Health (Signature Edition)", "Pregnancy Health Basics (Signature Edition)", "Prenatal Testing (Signature Edition)"], "Compounded": ["Labor and Delivery (Signature Edition)", "Postpartum Health (Signature Edition)", "Infertility Basics (Signature Edition)", "Assisted Reproduction (Signature Edition)", "Pregnancy Loss (Signature Edition)", "STI Information (Signature Edition)", "Regular Screenings (Signature Edition)", "Menopause Information (Signature Edition)", "Andropause and Male Health (Signature Edition)", "Endometriosis (Signature Edition)", "PCOS Information (Signature Edition)", "Finding Good Care (Signature Edition)"], "Advanced": ["Insurance and Costs (Signature Edition)", "Talking With Partners (Signature Edition)", "Talking With Teens (Signature Edition)", "LGBTQ+ Reproductive Health (Signature Edition)", "Reproductive Health Records (Signature Edition)", "Myths and Facts (Signature Edition)", "The Annual Reproductive Review (Signature Edition)", "Advocacy and Rights (Signature Edition)", "Support Resources (Signature Edition)", "Teaching Body Literacy (Signature Edition)", "Fertility Preservation (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — health guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
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
    name:topic+' — health guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A health guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"reproductive-health-information-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-reproductive-health-information-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("reproductive-health-information-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
