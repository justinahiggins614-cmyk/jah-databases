(function(){'use strict';
/* JAH Public React Basics Database generator — jahdb-react-basics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RCT-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is React",
  "Setting Up a React Project",
  "JSX Syntax",
  "Components and Props",
  "State with useState",
  "Handling Events in React",
  "Conditional Rendering in React",
  "Lists and Keys in React",
  "Styling React Components",
  "React DevTools",
  "The Virtual DOM Explained"
 ],
 "Compounded": [
  "useEffect Basics",
  "useEffect Dependency Arrays",
  "Fetching Data in React",
  "Forms in React Advanced",
  "Lifting State Up",
  "Context API",
  "useRef Hook",
  "useMemo and useCallback",
  "Custom Hooks",
  "React Router Basics",
  "Component Composition Patterns",
  "Thinking in React"
 ],
 "Advanced": [
  "Error Boundaries in React",
  "React Performance Optimization",
  "React Testing Basics",
  "React Deployment",
  "State Management Libraries",
  "React Server Components Intro",
  "React Accessibility",
  "React Code Splitting",
  "React StrictMode and Concurrency",
  "Migrating to React 19 and Beyond",
  "React Project Capstone"
 ]
};
var DEMOKIND="react-basics-demo";
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
    name:topic+' — react record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A react record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-react-basics-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('react-basics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();