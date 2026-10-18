(function(){'use strict';
/* JAH Signature HTML and CSS Basics Database generator — jahdb-html-css-basics-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HTMLS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Are HTML and CSS",
  "Your First HTML Page",
  "HTML Headings and Paragraphs",
  "HTML Links and Anchors",
  "HTML Images",
  "HTML Lists",
  "HTML Tables Basics",
  "HTML Forms Basics",
  "CSS Selectors Basics",
  "CSS Box Model",
  "CSS Colors and Units"
 ],
 "Compounded": [
  "CSS Text and Typography",
  "CSS Backgrounds and Borders",
  "CSS Display and Visibility",
  "CSS Positioning",
  "CSS Flexbox",
  "CSS Grid",
  "Responsive Design Basics",
  "CSS Pseudo-classes and Pseudo-elements",
  "CSS Transitions",
  "CSS Specificity and Cascade",
  "CSS Inheritance",
  "CSS Variables Custom Properties"
 ],
 "Advanced": [
  "CSS Animations Keyframes",
  "CSS Media Queries Advanced",
  "CSS Forms Styling",
  "CSS Navigation Patterns",
  "CSS Layout Patterns",
  "CSS Accessibility Essentials",
  "CSS Performance Basics",
  "CSS Methodologies: BEM and Beyond",
  "CSS Debugging Techniques",
  "Semantic HTML5 Elements",
  "Putting It Together: A Complete Page"
 ]
};
var DEMOKIND="html-css-basics-signature-demo";
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
    name:topic+' — html and css record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A html and css record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-html-css-basics-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('html-css-basics-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();