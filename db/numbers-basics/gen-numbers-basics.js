(function(){'use strict';
/* JAH The Numbers Basics Database generator — jahdb-numbers-basics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NUMB-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What a Number Is - Foundations",
  "Counting: The First Skill - Foundations",
  "The Number Line - Foundations",
  "Writing Numerals and Number Words - Foundations",
  "More, Less, and the Same - Foundations",
  "Ordering Numbers - Foundations",
  "Before, After, and Between - Foundations",
  "Place Value: Ones and Tens - Foundations",
  "Place Value: Hundreds, Thousands, and Beyond - Foundations",
  "Even and Odd Numbers - Foundations"
 ],
 "Compounded": [
  "Adding: Putting Together - Compounded",
  "Subtracting: Taking Away - Compounded",
  "Addition and Subtraction Facts to 10 - Compounded",
  "Adding Two-Digit Numbers - Compounded",
  "Subtracting Two-Digit Numbers - Compounded",
  "Multiplication: Groups of Equal Size - Compounded",
  "The Multiplication Facts - Compounded",
  "Division: Sharing and Grouping - Compounded",
  "Relating Multiplication and Division - Compounded",
  "Fractions: Parts of a Whole - Compounded",
  "Fractions on the Number Line - Compounded",
  "Comparing Fractions - Compounded",
  "Mixed Numbers and Whole Parts - Compounded"
 ],
 "Advanced": [
  "Decimals: Tenths and Hundredths - Advanced",
  "Money and Decimals in Daily Life - Advanced",
  "Rounding and Estimating - Advanced",
  "Patterns in Numbers - Advanced",
  "Number Families: Primes and Composites - Advanced",
  "Measuring With Numbers: Length, Weight, Capacity - Advanced",
  "Word Problems: Numbers in Stories - Advanced",
  "Negative Numbers: Below Zero - Advanced",
  "Properties of Operations - Advanced",
  "Checking Your Work - Advanced",
  "Numbers All Around Us: The Big Picture - Advanced"
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
var gen={version:'jahdb-numbers-basics-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('numbers-basics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
