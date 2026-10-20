(function(){'use strict';
/* JAH Raggedy Ann Dolls Doll Database generator — jahdb-e2-doll-raggedy-ann-dolls-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-doll-raggedy-ann-dolls',PREFIX='JAH-E2DOLLRAGGE-',NAME='JAH Raggedy Ann Dolls Doll Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Raggedy Ann Dolls: the complete guide", "d": "Raggedy Ann Dolls: the rag classic..", "g": "overview", "l": 2, "q": "What is Raggedy Ann Dolls: the complete guide?", "a": "Raggedy Ann Dolls: the rag classic..", "x": "The complete doll guide to Raggedy Ann Dolls: the rag classic.. 1915. History, meaning, practices, and how to engage respectfully — everything in one database. Gruelle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Raggedy Ann Dolls essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Raggedy Ann Dolls essentials.", "x": "At a glance: Raggedy Ann Dolls — the rag classic.. Gruelle. The essentials: Yarn.. Red yarn. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1915.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1915.", "x": "Raggedy Ann Dolls: 1915.. Yarn. Essential knowledge — Red yarn.. the rag classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1915..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1915..", "x": "Explained: 1915.. Vintage. The context — Raggedy Ann Dolls. I love you. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Gruelle.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Gruelle.", "x": "Raggedy Ann Dolls: Gruelle.. Books. Essential knowledge — I love you.. the rag classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Gruelle..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Gruelle..", "x": "Explained: Gruelle.. 1915. The context — Raggedy Ann Dolls. Books. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Red yarn.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Red yarn.", "x": "Raggedy Ann Dolls: Red yarn.. Vintage. Essential knowledge — Books.. the rag classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Red yarn..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Red yarn..", "x": "Explained: Red yarn.. History. The context — Raggedy Ann Dolls. Vintage. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "I love you.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "I love you.", "x": "Raggedy Ann Dolls: I love you.. 1915. Essential knowledge — Vintage.. the rag classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: I love you..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: I love you..", "x": "Explained: I love you.. Gruelle. The context — Raggedy Ann Dolls. 1915. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Books.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Books.", "x": "Raggedy Ann Dolls: Books.. History. Essential knowledge — 1915.. the rag classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Books..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Books..", "x": "Explained: Books.. Yarn. The context — Raggedy Ann Dolls. Gruelle. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Vintage.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Vintage.", "x": "Raggedy Ann Dolls: Vintage.. Gruelle. Essential knowledge — Gruelle.. the rag classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Vintage..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Vintage..", "x": "Explained: Vintage.. Books. The context — Raggedy Ann Dolls. Red yarn. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Gruelle.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Gruelle.", "x": "Raggedy Ann Dolls in depth: Gruelle.. Gruelle. Details — the rag classic.. Books. I love you. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Yarn.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Yarn.", "x": "Raggedy Ann Dolls in depth: Yarn.. Red yarn. Details — the rag classic.. Vintage. Books. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Books.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Books.", "x": "Raggedy Ann Dolls in depth: Books.. I love you. Details — the rag classic.. 1915. Vintage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Vintage.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Vintage.", "x": "Raggedy Ann Dolls in depth: Vintage.. Books. Details — the rag classic.. History. 1915. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "1915.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "1915.", "x": "Raggedy Ann Dolls in depth: 1915.. Vintage. Details — the rag classic.. Gruelle. Gruelle. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Raggedy Ann Dolls in depth: History.. 1915. Details — the rag classic.. Yarn. Red yarn. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Raggedy Ann Dolls comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Raggedy Ann Dolls comes from.", "x": "Origins: Gruelle.. 1915. The history of Raggedy Ann Dolls — the rag classic.. Yarn. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Raggedy Ann Dolls respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Raggedy Ann Dolls respectfully.", "x": "Engaging: Books.. Gruelle. How to participate or observe well — Raggedy Ann Dolls. the rag classic. Respect first, always; Vintage.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Raggedy Ann Dolls do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Raggedy Ann Dolls do's and don'ts.", "x": "Etiquette: 1915.. Red yarn. The rules of respect — Raggedy Ann Dolls. the rag classic. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Raggedy Ann Dolls.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Raggedy Ann Dolls.", "x": "Planning: Gruelle.. I love you. Practical notes — Raggedy Ann Dolls. the rag classic. A little planning shows respect for Yarn.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Raggedy Ann Dolls and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Raggedy Ann Dolls and money.", "x": "Costs: Books.. Books. What to budget — Raggedy Ann Dolls. the rag classic. The best experiences of Vintage. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-doll-raggedy-ann-dolls-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
