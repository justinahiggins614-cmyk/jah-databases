(function(){'use strict';
/* JAH Disability Benefits Navigation Database generator — jahdb-disability-benefits-navigation-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DISABNS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["SSDI vs SSI (Signature Edition)", "Disability Definition (Signature Edition)", "Work Credits (Signature Edition)", "Medical Evidence (Signature Edition)", "The Application (Signature Edition)", "Function Reports (Signature Edition)", "Consultative Exams (Signature Edition)", "Initial Denial (Signature Edition)", "Reconsideration (Signature Edition)", "The Hearing (Signature Edition)", "Vocational Experts (Signature Edition)"], "Compounded": ["Working While Applying (Signature Edition)", "Back Pay (Signature Edition)", "Continuing Reviews (Signature Edition)", "Ticket to Work (Signature Edition)", "Overpayments (Signature Edition)", "Representatives (Signature Edition)", "Mental Health Claims (Signature Edition)", "Children's SSI (Signature Edition)", "Expedited Claims (Signature Edition)", "State Supplements (Signature Edition)", "Healthcare With Benefits (Signature Edition)", "Housing and Benefits (Signature Edition)"], "Advanced": ["Family Benefits (Signature Edition)", "Teaching Navigation (Signature Edition)", "The Annual Benefits Review (Signature Edition)", "Record Keeping (Signature Edition)", "The Representative Payee (Signature Edition)", "Expedited Reinstatement (Signature Edition)", "PASS Plans (Signature Edition)", "Impairment-Related Work Expenses (Signature Edition)", "Section 1619 Provisions (Signature Edition)", "The Disability Starter Kit (Signature Edition)", "ALJ Hearing Tips (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — benefits guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — benefits guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A benefits guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"disability-benefits-navigation-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-disability-benefits-navigation-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("disability-benefits-navigation-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
