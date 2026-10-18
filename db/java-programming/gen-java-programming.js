(function(){'use strict';
/* JAH Public Java Programming Database generator — jahdb-java-programming-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-JAVA-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Java JDK JVM and JRE Explained",
  "Java First Program Anatomy",
  "Java Variables and Primitive Types",
  "Java Operators",
  "Java Strings",
  "Java if else and switch",
  "Java Loops",
  "Java Arrays",
  "Java Methods",
  "Java Classes and Objects",
  "Java Packages and Imports"
 ],
 "Compounded": [
  "Java Constructors",
  "Java Inheritance",
  "Java Polymorphism",
  "Java Encapsulation and Access Modifiers",
  "Java Abstract Classes",
  "Java Interfaces",
  "Java Exception Handling",
  "Java Collections: ArrayList",
  "Java Collections: HashMap",
  "Java StringBuilder",
  "Java Static Members",
  "Java Enums"
 ],
 "Advanced": [
  "Java Generics",
  "Java Lambda Expressions",
  "Java Streams API",
  "Java File IO with NIO",
  "Java Multithreading Basics",
  "Java Synchronization",
  "Java Annotations",
  "Java JUnit Testing",
  "Java Build Tools: Maven and Gradle",
  "Java JVM Memory Model",
  "Java Garbage Collection"
 ]
};
var DEMOKIND="java-programming-demo";
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
    name:topic+' — java programming record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A java programming record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-java-programming-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('java-programming',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();