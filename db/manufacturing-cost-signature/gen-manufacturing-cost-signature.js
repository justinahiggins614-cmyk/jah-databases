(function(){'use strict';
/* JAH The Manufacturing Cost Signature Database generator — jahdb-manufacturing-cost-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MFGS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is a Manufacturing Cost (Signature Edition) - Foundations",
  "The Bill of Materials (Signature Edition) - Foundations",
  "Direct Material Costing (Signature Edition) - Foundations",
  "Direct Labor Costing (Signature Edition) - Foundations",
  "Manufacturing Overhead: What It Is (Signature Edition) - Foundations",
  "The Standard Cost Stack (Signature Edition) - Foundations",
  "Cost of Goods Sold vs Unit Cost (Signature Edition) - Foundations",
  "Landed Cost: Freight, Duty, and Currency (Signature Edition) - Foundations",
  "Reading a Supplier Quotation (Signature Edition) - Foundations",
  "Make vs Buy: The First Question (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Multilevel BOM Rollups (Signature Edition) - Compounded",
  "Labor Standards and Time Studies (Signature Edition) - Compounded",
  "Machine-Hour Overhead Rates (Signature Edition) - Compounded",
  "Tooling and NRE Amortization (Signature Edition) - Compounded",
  "Injection Molding Cost Anatomy (Signature Edition) - Compounded",
  "Machining Cost Anatomy (Signature Edition) - Compounded",
  "Electronics Assembly Costing (Signature Edition) - Compounded",
  "Yield, Scrap, and Rework Costing (Signature Edition) - Compounded",
  "Economies of Scale (Signature Edition) - Compounded",
  "Activity-Based Costing (Signature Edition) - Compounded",
  "Should-Cost Analysis (Signature Edition) - Compounded",
  "Target Costing and Design-to-Cost (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Margin Math: Unit Cost vs Wholesale vs Retail (Signature Edition) - Advanced",
  "Contribution Margin and Break-Even (Signature Edition) - Advanced",
  "Make vs Buy: Total Cost of Ownership (Signature Edition) - Advanced",
  "Parametric Cost Estimation (Signature Edition) - Advanced",
  "Cost of Poor Quality (Signature Edition) - Advanced",
  "Lifecycle Costing (Signature Edition) - Advanced",
  "Transfer Pricing Between Plants (Signature Edition) - Advanced",
  "Design-for-Manufacturing Cost Decisions (Signature Edition) - Advanced",
  "Supply-Chain Disruption Costing (Signature Edition) - Advanced",
  "Environmental and Compliance Cost (Signature Edition) - Advanced",
  "The 20-Cent Lesson: Cost Differentiation at Scale (Signature Edition) - Advanced",
  "Cost Audit: Verifying What a Thing Really Costs (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Manufacturing Cost Study — "+safe+"\n"
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
    name:topic+' — manufacturing cost record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A manufacturing cost record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"manufacturing-cost-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-manufacturing-cost-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('manufacturing-cost-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
