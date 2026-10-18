(function(){'use strict';
/* JAH Public Design Patterns Database generator — jahdb-design-patterns-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DP-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Are Design Patterns",
  "Why Design Patterns Matter",
  "Creational Patterns Overview",
  "Structural Patterns Overview",
  "Behavioral Patterns Overview",
  "UML Basics for Patterns",
  "SOLID: Single Responsibility Principle",
  "SOLID: Open Closed Principle",
  "SOLID: Liskov Substitution Principle",
  "SOLID: Interface Segregation Principle",
  "SOLID: Dependency Inversion Principle"
 ],
 "Compounded": [
  "Singleton Pattern",
  "Factory Method Pattern",
  "Abstract Factory Pattern",
  "Builder Pattern",
  "Prototype Pattern",
  "Adapter Pattern",
  "Decorator Pattern",
  "Facade Pattern",
  "Proxy Pattern",
  "Composite Pattern",
  "Strategy Pattern",
  "Observer Pattern"
 ],
 "Advanced": [
  "Command Pattern",
  "State Pattern",
  "Template Method Pattern",
  "Iterator Pattern",
  "Mediator Pattern",
  "Memento Pattern",
  "Chain of Responsibility Pattern",
  "Visitor Pattern",
  "Flyweight Pattern",
  "Anti-Patterns to Avoid",
  "Choosing Patterns Wisely"
 ]
};
var DEMOKIND="design-patterns-demo";
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
    name:topic+' — design pattern record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A design pattern record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-design-patterns-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('design-patterns',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();