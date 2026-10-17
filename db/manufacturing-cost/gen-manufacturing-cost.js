(function(){'use strict';
/* JAH The Manufacturing Cost Database generator — jahdb-manufacturing-cost-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MFG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is a Manufacturing Cost - Foundations",
  "The Bill of Materials - Foundations",
  "Direct Material Costing - Foundations",
  "Direct Labor Costing - Foundations",
  "Manufacturing Overhead: What It Is - Foundations",
  "The Standard Cost Stack - Foundations",
  "Cost of Goods Sold vs Unit Cost - Foundations",
  "Landed Cost: Freight, Duty, and Currency - Foundations",
  "Reading a Supplier Quotation - Foundations",
  "Make vs Buy: The First Question - Foundations"
 ],
 "Compounded": [
  "Multilevel BOM Rollups - Compounded",
  "Labor Standards and Time Studies - Compounded",
  "Machine-Hour Overhead Rates - Compounded",
  "Tooling and NRE Amortization - Compounded",
  "Injection Molding Cost Anatomy - Compounded",
  "Machining Cost Anatomy - Compounded",
  "Electronics Assembly Costing - Compounded",
  "Yield, Scrap, and Rework Costing - Compounded",
  "Economies of Scale - Compounded",
  "Activity-Based Costing - Compounded",
  "Should-Cost Analysis - Compounded",
  "Target Costing and Design-to-Cost - Compounded"
 ],
 "Advanced": [
  "Margin Math: Unit Cost vs Wholesale vs Retail - Advanced",
  "Contribution Margin and Break-Even - Advanced",
  "Make vs Buy: Total Cost of Ownership - Advanced",
  "Parametric Cost Estimation - Advanced",
  "Cost of Poor Quality - Advanced",
  "Lifecycle Costing - Advanced",
  "Transfer Pricing Between Plants - Advanced",
  "Design-for-Manufacturing Cost Decisions - Advanced",
  "Supply-Chain Disruption Costing - Advanced",
  "Environmental and Compliance Cost - Advanced",
  "The 20-Cent Lesson: Cost Differentiation at Scale - Advanced",
  "Cost Audit: Verifying What a Thing Really Costs - Advanced"
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
var gen={version:'jahdb-manufacturing-cost-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('manufacturing-cost',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
