(function(){'use strict';
/* JAH The Unsolved Economics Database generator — jahdb-unsolved-economics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USEC-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Why Are Some Countries Rich and Others Poor - Growth and Business Cycles",
  "What Causes the Business Cycle - Growth and Business Cycles",
  "The Equity Premium Puzzle - Finance and Asset Pricing",
  "The Stock Market Participation Puzzle - Finance and Asset Pricing",
  "The Home Bias Puzzle - Finance and Asset Pricing",
  "Why Does Productivity Growth Slow Down - Growth and Business Cycles",
  "The Flattened Phillips Curve - Money and Inflation",
  "Why Do Workers Not Move to Higher-Wage Jobs - Labor and Work",
  "The Happiness Paradox - Labor and Work",
  "Why Do Asset Price Bubbles Form - Finance and Asset Pricing",
  "The Feldstein-Horioka Puzzle - International Economics"
 ],
 "Compounded": [
  "Can Financial Crises Be Predicted - Finance and Asset Pricing",
  "The Forward Premium Puzzle - International Economics",
  "The Exchange Rate Disconnect Puzzle - International Economics",
  "The Lucas Paradox - International Economics",
  "The Dark Matter of the Current Account - International Economics",
  "Why Do Firms Differ So Much in Productivity - Labor and Work",
  "The Declining Labor Share of Income - Labor and Work",
  "Minimum Wage Effects on Employment - Labor and Work",
  "The Dynamics of Top Income Inequality - Policy and Public Finance",
  "The Unexplained Gender Wage Gap - Labor and Work",
  "Do Government Deficits Matter - Money and Inflation",
  "How Large Are Fiscal Multipliers - Policy and Public Finance"
 ],
 "Advanced": [
  "Optimal Taxation Design - Policy and Public Finance",
  "Behavioral Foundations of Economic Choice - Behavior and Expectations",
  "The Social Cost of Carbon - Climate and the Long Run",
  "Optimal Monetary Policy at the Zero Lower Bound - Money and Inflation",
  "Why Have Long-Term Interest Rates Fallen - Money and Inflation",
  "Artificial Intelligence and the Future of Work - Labor and Work",
  "Optimal Patent Length - Policy and Public Finance",
  "The Measurement and Cure of Corruption - Policy and Public Finance",
  "Platform Monopolies and Digital Market Power - Policy and Public Finance",
  "Demographics and the Global Savings Glut - International Economics",
  "How Do People Form Economic Expectations - Behavior and Expectations"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unsolved Economics Study — "+safe+"\n"
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
    demo:{kind:"unsolved-economics-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-unsolved-economics-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-economics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
