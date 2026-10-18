(function(){'use strict';
/* JAH The Unsolved Political Science Database generator — jahdb-unsolved-political-science-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USPO-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Why Do Democracies Backslide - Democracy",
  "Are Voters Rational - Behavior",
  "Why Do Parties Polarize - Behavior",
  "Why Is Turnout What It Is - Behavior",
  "Does Deliberation Change Minds - Behavior",
  "The Democratic Peace: What Is the Mechanism - Conflict",
  "Why Do Civil Wars Recur - Conflict",
  "Why Do Revolutions Succeed or Fail - Revolution",
  "Why Do Some States Fail - State",
  "The Resource Curse: Which Mechanism - Political Economy",
  "Why Does Corruption Persist - Governance"
 ],
 "Compounded": [
  "Why Do Authoritarian Regimes Survive - Authoritarianism",
  "The China Model: Generalizable - Authoritarianism",
  "Federalism Versus Unitary Performance - Institutions",
  "The Incumbency Advantage Causes - Institutions",
  "Do Electoral Systems Shape Everything - Institutions",
  "Judicial Independence: Can It Be Measured - Institutions",
  "Does Foreign Aid Work Politically - Political Economy",
  "The Middle-Income Trap: Political Roots - Political Economy",
  "Money in Politics: What Does It Buy - Political Economy",
  "Clientelism: Why Does It Persist - Political Economy",
  "The Selectorate Theory Limits - Theory",
  "Nationalism: Why Does It Persist - Theory"
 ],
 "Advanced": [
  "State Capacity: Where Does It Come From - State",
  "Measuring the Rule of Law - Governance",
  "Why Do Sanctions (Not) Work - Conflict",
  "Does Peacekeeping Work - Conflict",
  "Democratization Waves: What Drives Them - Democracy",
  "The Political Business Cycle: Real or Myth - Political Economy",
  "Gender and Representation: Does It Change Policy - Behavior",
  "Media Effects: How Much Power - Behavior",
  "Constitutional Endurance: Why Do Some Last - Institutions",
  "Decentralization: Does It Help - Governance",
  "A General Theory of Politics - Theory"
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
var gen={version:'jahdb-unsolved-political-science-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-political-science',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
