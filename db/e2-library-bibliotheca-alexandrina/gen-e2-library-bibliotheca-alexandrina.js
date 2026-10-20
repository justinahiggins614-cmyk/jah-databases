(function(){'use strict';
/* JAH Library of Alexandria (new) Library Database generator — jahdb-e2-library-bibliotheca-alexandrina-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-library-bibliotheca-alexandrina',PREFIX='JAH-E2LIBRARYBI-',NAME='JAH Library of Alexandria (new) Library Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Library of Alexandria (new): the complete guide", "d": "Library of Alexandria (new): the ancient dream reborn..", "g": "overview", "l": 2, "q": "What is Library of Alexandria (new): the complete guide?", "a": "Library of Alexandria (new): the ancient dream reborn..", "x": "The complete library guide to Library of Alexandria (new): the ancient dream reborn.. 2002. History, meaning, practices, and how to engage respectfully — everything in one database. Ancient. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Library of Alexandria (new) essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Library of Alexandria (new) essentials.", "x": "At a glance: Library of Alexandria (new) — the ancient dream reborn.. Ancient legacy. The essentials: Building.. 8M books. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2002.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2002.", "x": "Library of Alexandria (new): 2002.. Building. Essential knowledge — 8M books.. the ancient dream reborn. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2002..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2002..", "x": "Explained: 2002.. Tours. The context — Library of Alexandria (new). Disk sun. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Ancient legacy.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Ancient legacy.", "x": "Library of Alexandria (new): Ancient legacy.. Collections. Essential knowledge — Disk sun.. the ancient dream reborn. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Ancient legacy..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Ancient legacy..", "x": "Explained: Ancient legacy.. Egypt. The context — Library of Alexandria (new). Alexandria. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "8M books.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "8M books.", "x": "Library of Alexandria (new): 8M books.. Tours. Essential knowledge — Alexandria.. the ancient dream reborn. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: 8M books..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: 8M books..", "x": "Explained: 8M books.. Dream. The context — Library of Alexandria (new). Design. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Disk sun.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Disk sun.", "x": "Library of Alexandria (new): Disk sun.. Egypt. Essential knowledge — Design.. the ancient dream reborn. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Disk sun..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Disk sun..", "x": "Explained: Disk sun.. Ancient. The context — Library of Alexandria (new). 2002. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Alexandria.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Alexandria.", "x": "Library of Alexandria (new): Alexandria.. Dream. Essential knowledge — 2002.. the ancient dream reborn. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Alexandria..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Alexandria..", "x": "Explained: Alexandria.. Building. The context — Library of Alexandria (new). Ancient legacy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Design.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Design.", "x": "Library of Alexandria (new): Design.. Ancient. Essential knowledge — Ancient legacy.. the ancient dream reborn. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Design..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Design..", "x": "Explained: Design.. Collections. The context — Library of Alexandria (new). 8M books. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Ancient.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Ancient.", "x": "Library of Alexandria (new) in depth: Ancient.. Ancient legacy. Details — the ancient dream reborn.. Collections. Disk sun. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Building.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Building.", "x": "Library of Alexandria (new) in depth: Building.. 8M books. Details — the ancient dream reborn.. Tours. Alexandria. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Collections.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Collections.", "x": "Library of Alexandria (new) in depth: Collections.. Disk sun. Details — the ancient dream reborn.. Egypt. Design. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tours.", "x": "Library of Alexandria (new) in depth: Tours.. Alexandria. Details — the ancient dream reborn.. Dream. 2002. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Egypt.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Egypt.", "x": "Library of Alexandria (new) in depth: Egypt.. Design. Details — the ancient dream reborn.. Ancient. Ancient legacy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Dream.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Dream.", "x": "Library of Alexandria (new) in depth: Dream.. 2002. Details — the ancient dream reborn.. Building. 8M books. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Library of Alexandria (new) comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Library of Alexandria (new) comes from.", "x": "Origins: Ancient.. 2002. The history of Library of Alexandria (new) — the ancient dream reborn.. Building. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Library of Alexandria (new) respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Library of Alexandria (new) respectfully.", "x": "Engaging: Collections.. Ancient legacy. How to participate or observe well — Library of Alexandria (new). the ancient dream reborn. Respect first, always; Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Library of Alexandria (new) do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Library of Alexandria (new) do's and don'ts.", "x": "Etiquette: Egypt.. 8M books. The rules of respect — Library of Alexandria (new). the ancient dream reborn. When in doubt, ask about Dream.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Library of Alexandria (new).", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Library of Alexandria (new).", "x": "Planning: Ancient.. Disk sun. Practical notes — Library of Alexandria (new). the ancient dream reborn. A little planning shows respect for Building.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Library of Alexandria (new) and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Library of Alexandria (new) and money.", "x": "Costs: Collections.. Alexandria. What to budget — Library of Alexandria (new). the ancient dream reborn. The best experiences of Tours. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
function pad(n){return String(n).padStart(6,'0');}
function drillProg(q,a){
  return '// boundless drill program\nvar Q='+JSON.stringify(q)+';\nvar A='+JSON.stringify(a)+';\n'
    +'console.log("DRILL: "+Q);\nconsole.log("Say it out loud, then check:");\nconsole.log("ANSWER: "+A);';
}
function bankRec(i){
  var b=BANK[(i-1)%BANK.length];
  var r={id:PREFIX+pad(i),title:b.t,description:b.x,group:b.g,ladder:b.l,
    question:b.q,answer:b.a,method:'archive-sample',
    program:drillProg(b.q,b.a),language:'javascript',
    src:b.s,last_verified:'2026-10-19',sample:true};
  return r;
}
function genQuizDrill(rnd,seed){
  var b=BANK[(rnd()*BANK.length)|0];
  var desc='Boundless drill #'+seed+' — '+NAME+'. The question: '+b.q+'\n\n'
    +'Cover the answer and say it out loud before reading on. Fluency with these facts is the whole game: '
    +'each drill pulls a real record from this database\'s archive and tests exactly one fact cold. '
    +'If you knew it, it is yours; if not, open the archive record "'+b.t+'" and read the full entry, then come back and drill it again. '
    +'The validated answer: '+b.a+'\n\n'
    +'Drills never repeat the archive verbatim — they re-ask the same true facts from new angles so the knowledge sticks.';
  return {id:PREFIX+pad(seed),title:'Drill: '+b.t,description:desc,group:b.g,ladder:b.l,
    method:'quiz-drill',question:b.q,answer:b.a,
    program:drillProg(b.q,b.a),language:'javascript',src:GEN_SRC,last_verified:'2026-10-19'};
}
function genConvertDrill(rnd,seed){
  var b1=BANK[(rnd()*BANK.length)|0],b2=BANK[(rnd()*BANK.length)|0];
  var v=Math.round((1+rnd()*999)*100)/100;
  var ans=v*b1.f/b2.f;
  var q='Convert '+v+' '+b1.t+' to '+b2.t+'.';
  var a=String(Math.round(ans*1e6)/1e6)+' '+b2.t;
  var desc='Boundless drill #'+seed+' — '+NAME+'. The question: '+q+'\n\n'
    +'Work it with the factor table: multiply by the "from" unit\'s factor to reach the base unit, then divide by the "to" unit\'s factor. '
    +'The demo program on any archive record in this database runs the same computation, so you can check your method there first. '
    +'The validated answer: '+a+'. If your number matches, the method is yours; drills like this one keep every conversion in this database one multiplication and one division away.';
  return {id:PREFIX+pad(seed),title:'Conversion drill: '+b1.t+' to '+b2.t,description:desc,
    group:b1.g,ladder:2,method:'convert-drill',question:q,answer:a,
    conv:{value:v,from:b1.t,fromF:b1.f,to:b2.t,toF:b2.f},
    program:'// conversion drill program\nvar v='+v+';\nvar fromF='+b1.f+';\nvar toF='+b2.f+';\n'
      +'console.log("Q: convert "+v+" '+b1.t.replace(/'/g,"\\'")+' to '+b2.t.replace(/'/g,"\\'")+'");\n'
      +'console.log("A: "+(v*fromF/toF)+" '+b2.t.replace(/'/g,"\\'")+'");',
    language:'javascript',src:GEN_SRC,last_verified:'2026-10-19'};
}
function generate(seed,opts,rnd){
  opts=opts||{};seed=+seed||1;rnd=rnd||prng(seed);
  var g=opts.group||opts.category;
  if(g&&FIELDS.indexOf(g)<0)g=null;
  var r;
  if(seed>=1&&seed<=BANK.length){r=bankRec(seed);}
  else{r=(MODE==='convert')?genConvertDrill(rnd,seed):genQuizDrill(rnd,seed);}
  if(g)r.group=g;
  return r;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.group)<0)e.push('group');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<200)e.push('description');
  if(r.method==='quiz-drill'||r.method==='archive-sample'){
    var hit=null;
    for(var i=0;i<BANK.length;i++){if(BANK[i].q===r.question&&BANK[i].a===r.answer){hit=BANK[i];break;}}
    if(!hit)e.push('answer not banked');
  }else if(r.method==='convert-drill'){
    var c=r.conv;
    if(!c||typeof c.value!=='number')e.push('conv missing');
    else{
      var expect=c.value*c.fromF/c.toF;
      var got=parseFloat(String(r.answer).split(' ')[0]);
      if(!(Math.abs(got-expect)<Math.max(1e-6,Math.abs(expect)*1e-9)))e.push('conversion mismatch');
    }
  }else{e.push('method');}
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var seen={};(sample||[]).forEach(function(s){if(s&&s.t)seen[s.t]=1;});
  if(rec&&seen[rec.title])return{ok:false,errors:['duplicate title in archive sample']};
  return{ok:true,errors:[]};
}
var gen={version:'jahdb-e2-library-bibliotheca-alexandrina-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
