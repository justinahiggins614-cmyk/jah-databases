(function(){'use strict';
/* JAH The Charitable Giving Evaluation Database generator — jahdb-charitable-giving-evaluation-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CGE-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Charitable Giving Evaluation: Reading Your Numbers Correctly — foundations",
  "Charitable Giving Evaluation: The 50/30/20 Budget Frame — foundations",
  "Charitable Giving Evaluation: Emergency Funds That Work — foundations",
  "Charitable Giving Evaluation: Comparing Costs Apples to Apples — foundations",
  "Charitable Giving Evaluation: Deadlines and Their Penalties — foundations",
  "Charitable Giving Evaluation: Paper Trails That Protect You — foundations",
  "Charitable Giving Evaluation: Spotting Fees and Fine Print — foundations",
  "Charitable Giving Evaluation: When to Pay a Professional — foundations",
  "Charitable Giving Evaluation: Teaching Kids About This Money Topic — foundations",
  "Charitable Giving Evaluation: Common Scams in This Area — foundations",
  "Charitable Giving Evaluation: Your Rights in Plain English — foundations",
  "Charitable Giving Evaluation: Building the Habit of Review — foundations"
 ],
 "compounded": [
  "Charitable Giving Evaluation: Negotiating Bills and Rates — compounded",
  "Charitable Giving Evaluation: Tax Angles You Should Know — compounded",
  "Charitable Giving Evaluation: Insurance Intersections — compounded",
  "Charitable Giving Evaluation: Digital Security for Money Matters — compounded",
  "Charitable Giving Evaluation: What Changes With Life Events — compounded",
  "Charitable Giving Evaluation: Measuring Financial Progress — compounded",
  "Charitable Giving Evaluation: Avoiding Lifestyle Creep — compounded",
  "Charitable Giving Evaluation: Community Resources for Money Help — compounded",
  "Charitable Giving Evaluation: Employer Benefits You May Be Missing — compounded",
  "Charitable Giving Evaluation: Planning for the Long Term — compounded",
  "Charitable Giving Evaluation: Advanced: Optimizing the Math — compounded",
  "Charitable Giving Evaluation: Advanced: Handling Complex Cases — compounded"
 ],
 "advanced": [
  "Charitable Giving Evaluation: Advanced: Dispute and Appeal Mastery — advanced",
  "Charitable Giving Evaluation: Advanced: Teaching Others — advanced",
  "Charitable Giving Evaluation: Advanced: Building Systems — advanced",
  "Charitable Giving Evaluation: Advanced: Generational Transfer — advanced",
  "Charitable Giving Evaluation: Advanced: Crisis Money Management — advanced",
  "Charitable Giving Evaluation: Advanced: Auditing Your Financial Life — advanced",
  "Charitable Giving Evaluation: Advanced: Staying Current on Rule Changes — advanced",
  "Charitable Giving Evaluation: Advanced: Designing Your Own Strategy — advanced",
  "Charitable Giving Evaluation: Advanced: Giving Wisely — advanced",
  "Charitable Giving Evaluation: Advanced: Legacy and Records — advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Charitable Giving Evaluation Database — structural study\n"
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
    name:topic+' — practical guidance record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A practical guidance record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest-sample',
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
var gen={version:'jahdb-charitable-giving-evaluation-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('charitable-giving-evaluation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
