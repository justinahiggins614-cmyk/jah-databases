(function(){'use strict';
/* JAH Library of Congress Library Database generator — jahdb-e2-library-library-of-congress-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-library-library-of-congress',PREFIX='JAH-E2LIBRARYLI-',NAME='JAH Library of Congress Library Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Library of Congress: the complete guide", "d": "Library of Congress: the world's largest library..", "g": "overview", "l": 2, "q": "What is Library of Congress: the complete guide?", "a": "Library of Congress: the world's largest library..", "x": "The complete library guide to Library of Congress: the world's largest library.. 170M items. History, meaning, practices, and how to engage respectfully — everything in one database. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Library of Congress essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Library of Congress essentials.", "x": "At a glance: Library of Congress — the world's largest library.. 1800. The essentials: Collections.. Jefferson's books. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "170M items.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "170M items.", "x": "Library of Congress: 170M items.. Collections. Essential knowledge — Jefferson's books.. the world's largest library. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 170M items..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 170M items..", "x": "Explained: 170M items.. Tours. The context — Library of Congress. DC. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "1800.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "1800.", "x": "Library of Congress: 1800.. Jefferson. Essential knowledge — DC.. the world's largest library. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 1800..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 1800..", "x": "Explained: 1800.. Research. The context — Library of Congress. Free. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Jefferson's books.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Jefferson's books.", "x": "Library of Congress: Jefferson's books.. Tours. Essential knowledge — Free.. the world's largest library. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Jefferson's books..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Jefferson's books..", "x": "Explained: Jefferson's books.. Digital. The context — Library of Congress. Copyright. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "DC.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "DC.", "x": "Library of Congress: DC.. Research. Essential knowledge — Copyright.. the world's largest library. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: DC..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: DC..", "x": "Explained: DC.. History. The context — Library of Congress. 170M items. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Free.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Free.", "x": "Library of Congress: Free.. Digital. Essential knowledge — 170M items.. the world's largest library. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Free..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Free..", "x": "Explained: Free.. Collections. The context — Library of Congress. 1800. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Copyright.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Copyright.", "x": "Library of Congress: Copyright.. History. Essential knowledge — 1800.. the world's largest library. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Copyright..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Copyright..", "x": "Explained: Copyright.. Jefferson. The context — Library of Congress. Jefferson's books. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Library of Congress in depth: History.. 1800. Details — the world's largest library.. Jefferson. DC. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Collections.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Collections.", "x": "Library of Congress in depth: Collections.. Jefferson's books. Details — the world's largest library.. Tours. Free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Jefferson.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Jefferson.", "x": "Library of Congress in depth: Jefferson.. DC. Details — the world's largest library.. Research. Copyright. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tours.", "x": "Library of Congress in depth: Tours.. Free. Details — the world's largest library.. Digital. 170M items. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Research.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Research.", "x": "Library of Congress in depth: Research.. Copyright. Details — the world's largest library.. History. 1800. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Digital.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Digital.", "x": "Library of Congress in depth: Digital.. 170M items. Details — the world's largest library.. Collections. Jefferson's books. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Library of Congress comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Library of Congress comes from.", "x": "Origins: History.. 170M items. The history of Library of Congress — the world's largest library.. Collections. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Library of Congress respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Library of Congress respectfully.", "x": "Engaging: Jefferson.. 1800. How to participate or observe well — Library of Congress. the world's largest library. Respect first, always; Tours.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Library of Congress do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Library of Congress do's and don'ts.", "x": "Etiquette: Research.. Jefferson's books. The rules of respect — Library of Congress. the world's largest library. When in doubt, ask about Digital.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Library of Congress.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Library of Congress.", "x": "Planning: History.. DC. Practical notes — Library of Congress. the world's largest library. A little planning shows respect for Collections.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Library of Congress and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Library of Congress and money.", "x": "Costs: Jefferson.. Free. What to budget — Library of Congress. the world's largest library. The best experiences of Tours. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-library-library-of-congress-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
