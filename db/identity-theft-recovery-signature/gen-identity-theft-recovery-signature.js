(function(){'use strict';
/* JAH The Identity Theft Recovery Signature Database generator — jahdb-identity-theft-recovery-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ITRS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Identity Theft Recovery (Signature): Reading Your Numbers Correctly — foundations",
  "Identity Theft Recovery (Signature): The 50/30/20 Budget Frame — foundations",
  "Identity Theft Recovery (Signature): Emergency Funds That Work — foundations",
  "Identity Theft Recovery (Signature): Comparing Costs Apples to Apples — foundations",
  "Identity Theft Recovery (Signature): Deadlines and Their Penalties — foundations",
  "Identity Theft Recovery (Signature): Paper Trails That Protect You — foundations",
  "Identity Theft Recovery (Signature): Spotting Fees and Fine Print — foundations",
  "Identity Theft Recovery (Signature): When to Pay a Professional — foundations",
  "Identity Theft Recovery (Signature): Teaching Kids About This Money Topic — foundations",
  "Identity Theft Recovery (Signature): Common Scams in This Area — foundations",
  "Identity Theft Recovery (Signature): Your Rights in Plain English — foundations",
  "Identity Theft Recovery (Signature): Building the Habit of Review — foundations"
 ],
 "compounded": [
  "Identity Theft Recovery (Signature): Negotiating Bills and Rates — compounded",
  "Identity Theft Recovery (Signature): Tax Angles You Should Know — compounded",
  "Identity Theft Recovery (Signature): Insurance Intersections — compounded",
  "Identity Theft Recovery (Signature): Digital Security for Money Matters — compounded",
  "Identity Theft Recovery (Signature): What Changes With Life Events — compounded",
  "Identity Theft Recovery (Signature): Measuring Financial Progress — compounded",
  "Identity Theft Recovery (Signature): Avoiding Lifestyle Creep — compounded",
  "Identity Theft Recovery (Signature): Community Resources for Money Help — compounded",
  "Identity Theft Recovery (Signature): Employer Benefits You May Be Missing — compounded",
  "Identity Theft Recovery (Signature): Planning for the Long Term — compounded",
  "Identity Theft Recovery (Signature): Advanced: Optimizing the Math — compounded",
  "Identity Theft Recovery (Signature): Advanced: Handling Complex Cases — compounded"
 ],
 "advanced": [
  "Identity Theft Recovery (Signature): Advanced: Dispute and Appeal Mastery — advanced",
  "Identity Theft Recovery (Signature): Advanced: Teaching Others — advanced",
  "Identity Theft Recovery (Signature): Advanced: Building Systems — advanced",
  "Identity Theft Recovery (Signature): Advanced: Generational Transfer — advanced",
  "Identity Theft Recovery (Signature): Advanced: Crisis Money Management — advanced",
  "Identity Theft Recovery (Signature): Advanced: Auditing Your Financial Life — advanced",
  "Identity Theft Recovery (Signature): Advanced: Staying Current on Rule Changes — advanced",
  "Identity Theft Recovery (Signature): Advanced: Designing Your Own Strategy — advanced",
  "Identity Theft Recovery (Signature): Advanced: Giving Wisely — advanced",
  "Identity Theft Recovery (Signature): Advanced: Legacy and Records — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Identity Theft Recovery Signature Database — structural study\n"
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
    name:topic+' — signature-original record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A signature-original record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-identity-theft-recovery-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('identity-theft-recovery-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
