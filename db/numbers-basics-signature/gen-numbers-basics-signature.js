(function(){'use strict';
/* JAH The Numbers Basics Signature Database generator — jahdb-numbers-basics-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NUMBS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What a Number Is (Signature Edition) - Foundations",
  "Counting: The First Skill (Signature Edition) - Foundations",
  "The Number Line (Signature Edition) - Foundations",
  "Writing Numerals and Number Words (Signature Edition) - Foundations",
  "More, Less, and the Same (Signature Edition) - Foundations",
  "Ordering Numbers (Signature Edition) - Foundations",
  "Before, After, and Between (Signature Edition) - Foundations",
  "Place Value: Ones and Tens (Signature Edition) - Foundations",
  "Place Value: Hundreds, Thousands, and Beyond (Signature Edition) - Foundations",
  "Even and Odd Numbers (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Adding: Putting Together (Signature Edition) - Compounded",
  "Subtracting: Taking Away (Signature Edition) - Compounded",
  "Addition and Subtraction Facts to 10 (Signature Edition) - Compounded",
  "Adding Two-Digit Numbers (Signature Edition) - Compounded",
  "Subtracting Two-Digit Numbers (Signature Edition) - Compounded",
  "Multiplication: Groups of Equal Size (Signature Edition) - Compounded",
  "The Multiplication Facts (Signature Edition) - Compounded",
  "Division: Sharing and Grouping (Signature Edition) - Compounded",
  "Relating Multiplication and Division (Signature Edition) - Compounded",
  "Fractions: Parts of a Whole (Signature Edition) - Compounded",
  "Fractions on the Number Line (Signature Edition) - Compounded",
  "Comparing Fractions (Signature Edition) - Compounded",
  "Mixed Numbers and Whole Parts (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Decimals: Tenths and Hundredths (Signature Edition) - Advanced",
  "Money and Decimals in Daily Life (Signature Edition) - Advanced",
  "Rounding and Estimating (Signature Edition) - Advanced",
  "Patterns in Numbers (Signature Edition) - Advanced",
  "Number Families: Primes and Composites (Signature Edition) - Advanced",
  "Measuring With Numbers: Length, Weight, Capacity (Signature Edition) - Advanced",
  "Word Problems: Numbers in Stories (Signature Edition) - Advanced",
  "Negative Numbers: Below Zero (Signature Edition) - Advanced",
  "Properties of Operations (Signature Edition) - Advanced",
  "Checking Your Work (Signature Edition) - Advanced",
  "Numbers All Around Us: The Big Picture (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Numbers Basics Study — "+safe+"\n"
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
    name:topic+' — numbers basics record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A numbers basics record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"numbers-basics-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-numbers-basics-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('numbers-basics-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
