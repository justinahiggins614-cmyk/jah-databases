(function(){'use strict';
/* JAH The Price and Profit Tracking Database generator — jahdb-price-profit-tracking-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PFT-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What a Price Really Is: The Anatomy of a Price Record - Foundations",
  "Nominal Versus Real: Money Across Time - Foundations",
  "Supply and Demand: Why Prices Move - Foundations",
  "The Costs Behind Every Price: Fixed, Variable, and Marginal - Foundations",
  "Markup Versus Margin: Two Languages of Profit - Foundations",
  "The Consumer Price Index: How Inflation Is Measured - Foundations",
  "Reading a Price Tag: Quotes, Units, and Terms - Foundations",
  "Break-Even: The Price That Covers the Costs - Foundations",
  "Gross, Operating, and Net: The Layers of Profit - Foundations"
 ],
 "Compounded": [
  "Gold Prices Across a Century: A Real Time Series - Compounded",
  "Oil Prices Since 1970: Boom, Bust, and Negative - Compounded",
  "American Home Prices 1975 to 2024: A Real Series - Compounded",
  "The S&P 500 as a Price Series - Compounded",
  "Time-Traveling Money: Inflation Adjustment - Compounded",
  "Depreciation: Straight-Line, Declining-Balance, Sum-of-Years - Compounded",
  "Appreciation and CAGR: Measuring Growth Honestly - Compounded",
  "Pricing by Comparison: The Comparables Approach - Compounded",
  "The Cost Approach: Replacement Less Depreciation - Compounded",
  "The Income Approach: Discounted Cash Flow - Compounded",
  "Price Elasticity: How Demand Answers Price - Compounded",
  "Profit Margins by Industry: Real Benchmarks - Compounded",
  "Unit Economics: Profit One Customer at a Time - Compounded"
 ],
 "Advanced": [
  "Building a Price Index: Laspeyres and Hedonic Methods - Advanced",
  "Time-Series Tools: Moving Averages, Volatility, and Trend - Advanced",
  "A Lifetime of Purchasing Power: Long-Horizon Math - Advanced",
  "Ballpark Estimation: The Fermi Method for New Things - Advanced",
  "Pricing the Never-Seen-Before: Analogous Estimation - Advanced",
  "Market Multiples in Practice: P/E, EV/EBITDA, and Cap Rates - Advanced",
  "Inventory Valuation: FIFO, LIFO, and Weighted Average - Advanced",
  "Price Forecasting: What Models Can and Cannot Say - Advanced",
  "Profit Attribution: Finding Where Profit Really Came From - Advanced",
  "Cost of Capital and the Hurdle Rate - Advanced",
  "Pricing Psychology: Anchoring and the Human Side of Price - Advanced",
  "The Complete Price Record: Time-Stamped Price Anatomy - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Price Profit Study — "+safe+"\n"
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
    name:topic+' — price and profit record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A price and profit record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"price-profit-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-price-profit-tracking-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('price-profit-tracking',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
