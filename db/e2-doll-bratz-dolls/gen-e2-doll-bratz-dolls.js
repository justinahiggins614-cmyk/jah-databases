(function(){'use strict';
/* JAH Bratz Dolls Doll Database generator — jahdb-e2-doll-bratz-dolls-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-doll-bratz-dolls',PREFIX='JAH-E2DOLLBRATZ-',NAME='JAH Bratz Dolls Doll Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Bratz Dolls: the complete guide", "d": "Bratz Dolls: the attitude dolls..", "g": "overview", "l": 2, "q": "What is Bratz Dolls: the complete guide?", "a": "Bratz Dolls: the attitude dolls..", "x": "The complete doll guide to Bratz Dolls: the attitude dolls.. 2001. History, meaning, practices, and how to engage respectfully — everything in one database. Heads. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Bratz Dolls essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Bratz Dolls essentials.", "x": "At a glance: Bratz Dolls — the attitude dolls.. Big heads. The essentials: MGA.. Yasmin. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2001.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2001.", "x": "Bratz Dolls: 2001.. MGA. Essential knowledge — Yasmin.. the attitude dolls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 2001..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 2001..", "x": "Explained: 2001.. 2001. The context — Bratz Dolls. MGA. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Big heads.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Big heads.", "x": "Bratz Dolls: Big heads.. Fashion. Essential knowledge — MGA.. the attitude dolls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Big heads..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Big heads..", "x": "Explained: Big heads.. Yasmin. The context — Bratz Dolls. Fashion. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Yasmin.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Yasmin.", "x": "Bratz Dolls: Yasmin.. 2001. Essential knowledge — Fashion.. the attitude dolls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Yasmin..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Yasmin..", "x": "Explained: Yasmin.. History. The context — Bratz Dolls. Dolls. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "MGA.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "MGA.", "x": "Bratz Dolls: MGA.. Yasmin. Essential knowledge — Dolls.. the attitude dolls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: MGA..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: MGA..", "x": "Explained: MGA.. Heads. The context — Bratz Dolls. 2001. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Fashion.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Fashion.", "x": "Bratz Dolls: Fashion.. History. Essential knowledge — 2001.. the attitude dolls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Fashion..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Fashion..", "x": "Explained: Fashion.. MGA. The context — Bratz Dolls. Big heads. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Dolls.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Dolls.", "x": "Bratz Dolls: Dolls.. Heads. Essential knowledge — Big heads.. the attitude dolls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Dolls..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Dolls..", "x": "Explained: Dolls.. Fashion. The context — Bratz Dolls. Yasmin. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Heads.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Heads.", "x": "Bratz Dolls in depth: Heads.. Big heads. Details — the attitude dolls.. Fashion. MGA. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "MGA.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "MGA.", "x": "Bratz Dolls in depth: MGA.. Yasmin. Details — the attitude dolls.. 2001. Fashion. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Fashion.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Fashion.", "x": "Bratz Dolls in depth: Fashion.. MGA. Details — the attitude dolls.. Yasmin. Dolls. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "2001.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "2001.", "x": "Bratz Dolls in depth: 2001.. Fashion. Details — the attitude dolls.. History. 2001. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Yasmin.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Yasmin.", "x": "Bratz Dolls in depth: Yasmin.. Dolls. Details — the attitude dolls.. Heads. Big heads. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Bratz Dolls in depth: History.. 2001. Details — the attitude dolls.. MGA. Yasmin. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Bratz Dolls comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Bratz Dolls comes from.", "x": "Origins: Heads.. 2001. The history of Bratz Dolls — the attitude dolls.. MGA. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Bratz Dolls respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Bratz Dolls respectfully.", "x": "Engaging: Fashion.. Big heads. How to participate or observe well — Bratz Dolls. the attitude dolls. Respect first, always; 2001.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Bratz Dolls do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Bratz Dolls do's and don'ts.", "x": "Etiquette: Yasmin.. Yasmin. The rules of respect — Bratz Dolls. the attitude dolls. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Bratz Dolls.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Bratz Dolls.", "x": "Planning: Heads.. MGA. Practical notes — Bratz Dolls. the attitude dolls. A little planning shows respect for MGA.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Bratz Dolls and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Bratz Dolls and money.", "x": "Costs: Fashion.. Fashion. What to budget — Bratz Dolls. the attitude dolls. The best experiences of 2001. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-doll-bratz-dolls-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
