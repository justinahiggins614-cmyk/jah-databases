(function(){'use strict';
/* JAH The JAH Signature Number Line Database generator — jahdb-jah-number-line-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NLN-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Counting Numbers on the Line - Foundations",
  "Zero and the Origin - Foundations",
  "Negative Numbers and Direction - Foundations",
  "The Integers on the Line - Foundations",
  "Ordering Numbers: Less Than and Greater Than - Foundations",
  "Addition as Steps to the Right - Foundations",
  "Subtraction as Steps to the Left - Foundations",
  "Between the Integers: Halves and Quarters - Foundations",
  "Opposites and Symmetry About Zero - Foundations",
  "The Ruler: Measuring Distance on the Line - Foundations",
  "Reading and Marking Points on the Line - Foundations"
 ],
 "Compounded": [
  "Fractions on the Line - Compounded",
  "Decimals on the Line - Compounded",
  "Rational Numbers: Dense but Not Complete - Compounded",
  "Absolute Value as Distance from Zero - Compounded",
  "Intervals: Segments of the Number Line - Compounded",
  "Graphing Inequalities on the Line - Compounded",
  "The Midpoint of Two Numbers - Compounded",
  "Multiplication as Scaling on the Line - Compounded",
  "Division as Reverse Scaling - Compounded",
  "Square Roots on the Line - Compounded",
  "The Line as a Coordinate Axis - Compounded",
  "Benchmarks: Estimating Positions on the Line - Compounded"
 ],
 "Advanced": [
  "The Irrational Numbers on the Line - Advanced",
  "The Real Number Line: Completeness - Advanced",
  "Interval Notation and Set Notation - Advanced",
  "Interval Arithmetic - Advanced",
  "Absolute Value Inequalities as Intervals - Advanced",
  "The Number Line in the Cartesian Plane - Advanced",
  "Number Lines in Measurement: Timelines, Scales, and Gauges - Advanced",
  "Limits: Approaching a Point on the Line - Advanced",
  "Functions as Mappings Along the Line - Advanced",
  "Infinite Intervals and the Idea of Infinity - Advanced",
  "The Number Line as a Model of Continuity - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Number Line Study — "+safe+"\n"
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
    name:topic+' — number line record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A number line record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"number-line-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-jah-number-line-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('jah-number-line',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
