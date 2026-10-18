(function(){'use strict';
/* JAH Public C Programming Database generator — jahdb-c-programming-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CLG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "C History and the Toolchain",
  "C Hello World and Compilation",
  "C Variables and Data Types",
  "C Operators",
  "C printf and scanf",
  "C if else",
  "C Loops",
  "C Functions",
  "C Arrays",
  "C Strings as Character Arrays",
  "C Pointers Introduction"
 ],
 "Compounded": [
  "C Pointer Arithmetic",
  "C Structs",
  "C Unions and Enums",
  "C Dynamic Memory: malloc and free",
  "C const and Storage Classes",
  "C Header Files",
  "C Preprocessor",
  "C File IO",
  "C Command Line Arguments",
  "C Recursion",
  "C Multidimensional Arrays",
  "C Bitwise Operators"
 ],
 "Advanced": [
  "C Function Pointers",
  "C Linked Lists",
  "C Memory Layout: Stack Versus Heap",
  "C Undefined Behavior",
  "C Debugging with gdb",
  "C Makefiles",
  "C Signals",
  "C System Calls Intro",
  "C Volatile and Atomics",
  "C Performance Optimization",
  "C Standards: C89 to C23"
 ]
};
var DEMOKIND="c-programming-demo";
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
    name:topic+' — c programming record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A c programming record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
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
var gen={version:'jahdb-c-programming-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('c-programming',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();