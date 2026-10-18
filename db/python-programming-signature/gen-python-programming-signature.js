(function(){'use strict';
/* JAH Signature Python Programming Database generator — jahdb-python-programming-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PYS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Installing Python and Using the REPL",
  "Python Variables and Assignment",
  "Python Numbers and Arithmetic",
  "Python Strings",
  "Python Booleans and Comparisons",
  "Python Lists",
  "Python Tuples",
  "Python Dictionaries",
  "Python Sets",
  "Python if elif else",
  "Python while Loops"
 ],
 "Compounded": [
  "Python for Loops and range",
  "Python List Comprehensions",
  "Python Functions and Arguments",
  "Python args and kwargs",
  "Python f-strings and Formatting",
  "Python File Input and Output",
  "Python Exception Handling",
  "Python Modules and Imports",
  "Python Virtual Environments and pip",
  "Python Slicing",
  "Python Dictionaries in Depth",
  "Python Lambda Functions"
 ],
 "Advanced": [
  "Python Decorators",
  "Python Generators and yield",
  "Python Context Managers",
  "Python Classes and Objects",
  "Python Inheritance",
  "Python Dunder Methods",
  "Python Regular Expressions",
  "Python Standard Library Tour",
  "Python Testing with pytest",
  "Python Type Hints",
  "Python Asyncio Basics"
 ]
};
var DEMOKIND="python-programming-signature-demo";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\');
  return 'console.log('+JSON.stringify('Topic: '+safe)+');\n'
       + 'console.log('+JSON.stringify('Field: '+field)+');\n'
       + 'console.log("Sample record - structural sample, not an archive entry.");\n';
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — python programming record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A python programming record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    signature_label:'Signature-generated original - authored in the Signature system. Property of Justin Addam Higgins (JAH).',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'javascript',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-python-programming-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('python-programming-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();