(function(){'use strict';
/* JAH The Unsolved Political Science Signature Database generator — jahdb-unsolved-political-science-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USPOS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Why Do Democracies Backslide (Signature Edition) - Democracy",
  "Are Voters Rational (Signature Edition) - Behavior",
  "Why Do Parties Polarize (Signature Edition) - Behavior",
  "Why Is Turnout What It Is (Signature Edition) - Behavior",
  "Does Deliberation Change Minds (Signature Edition) - Behavior",
  "The Democratic Peace: What Is the Mechanism (Signature Edition) - Conflict",
  "Why Do Civil Wars Recur (Signature Edition) - Conflict",
  "Why Do Revolutions Succeed or Fail (Signature Edition) - Revolution",
  "Why Do Some States Fail (Signature Edition) - State",
  "The Resource Curse: Which Mechanism (Signature Edition) - Political Economy",
  "Why Does Corruption Persist (Signature Edition) - Governance"
 ],
 "Compounded": [
  "Why Do Authoritarian Regimes Survive (Signature Edition) - Authoritarianism",
  "The China Model: Generalizable (Signature Edition) - Authoritarianism",
  "Federalism Versus Unitary Performance (Signature Edition) - Institutions",
  "The Incumbency Advantage Causes (Signature Edition) - Institutions",
  "Do Electoral Systems Shape Everything (Signature Edition) - Institutions",
  "Judicial Independence: Can It Be Measured (Signature Edition) - Institutions",
  "Does Foreign Aid Work Politically (Signature Edition) - Political Economy",
  "The Middle-Income Trap: Political Roots (Signature Edition) - Political Economy",
  "Money in Politics: What Does It Buy (Signature Edition) - Political Economy",
  "Clientelism: Why Does It Persist (Signature Edition) - Political Economy",
  "The Selectorate Theory Limits (Signature Edition) - Theory",
  "Nationalism: Why Does It Persist (Signature Edition) - Theory"
 ],
 "Advanced": [
  "State Capacity: Where Does It Come From (Signature Edition) - State",
  "Measuring the Rule of Law (Signature Edition) - Governance",
  "Why Do Sanctions (Not) Work (Signature Edition) - Conflict",
  "Does Peacekeeping Work (Signature Edition) - Conflict",
  "Democratization Waves: What Drives Them (Signature Edition) - Democracy",
  "The Political Business Cycle: Real or Myth (Signature Edition) - Political Economy",
  "Gender and Representation: Does It Change Policy (Signature Edition) - Behavior",
  "Media Effects: How Much Power (Signature Edition) - Behavior",
  "Constitutional Endurance: Why Do Some Last (Signature Edition) - Institutions",
  "Decentralization: Does It Help (Signature Edition) - Governance",
  "A General Theory of Politics (Signature Edition) - Theory"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unsolved Political Science Study — "+safe+"\n"
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
    name:topic+' — unsolved problem record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A unsolved problem record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"unsolved-political-science-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-unsolved-political-science-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-political-science-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
