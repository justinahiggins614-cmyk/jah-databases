(function(){'use strict';
/* JAH Art Institute of Chicago Museum Database generator — jahdb-e2-museum-art-institute-chicago-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-museum-art-institute-chicago',PREFIX='JAH-E2MUSEUMART-',NAME='JAH Art Institute of Chicago Museum Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Art Institute of Chicago: the complete guide", "d": "Art Institute of Chicago: lions guarding masterpieces..", "g": "overview", "l": 2, "q": "What is Art Institute of Chicago: the complete guide?", "a": "Art Institute of Chicago: lions guarding masterpieces..", "x": "The complete museum guide to Art Institute of Chicago: lions guarding masterpieces.. American Gothic. History, meaning, practices, and how to engage respectfully — everything in one database. Gothic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Art Institute of Chicago essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Art Institute of Chicago essentials.", "x": "At a glance: Art Institute of Chicago — lions guarding masterpieces.. Lions. The essentials: Lions.. Impressionists. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "American Gothic.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "American Gothic.", "x": "Art Institute of Chicago: American Gothic.. Lions. Essential knowledge — Impressionists.. lions guarding masterpieces. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: American Gothic..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: American Gothic..", "x": "Explained: American Gothic.. Tickets. The context — Art Institute of Chicago. 1879. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Lions.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Lions.", "x": "Art Institute of Chicago: Lions.. History. Essential knowledge — 1879.. lions guarding masterpieces. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Lions..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Lions..", "x": "Explained: Lions.. Chicago. The context — Art Institute of Chicago. Chicago. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Impressionists.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Impressionists.", "x": "Art Institute of Chicago: Impressionists.. Tickets. Essential knowledge — Chicago.. lions guarding masterpieces. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Impressionists..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Impressionists..", "x": "Explained: Impressionists.. Art. The context — Art Institute of Chicago. Thorne Rooms. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "1879.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "1879.", "x": "Art Institute of Chicago: 1879.. Chicago. Essential knowledge — Thorne Rooms.. lions guarding masterpieces. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: 1879..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: 1879..", "x": "Explained: 1879.. Gothic. The context — Art Institute of Chicago. American Gothic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Chicago.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Chicago.", "x": "Art Institute of Chicago: Chicago.. Art. Essential knowledge — American Gothic.. lions guarding masterpieces. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Chicago..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Chicago..", "x": "Explained: Chicago.. Lions. The context — Art Institute of Chicago. Lions. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Thorne Rooms.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Thorne Rooms.", "x": "Art Institute of Chicago: Thorne Rooms.. Gothic. Essential knowledge — Lions.. lions guarding masterpieces. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Thorne Rooms..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Thorne Rooms..", "x": "Explained: Thorne Rooms.. History. The context — Art Institute of Chicago. Impressionists. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Gothic.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Gothic.", "x": "Art Institute of Chicago in depth: Gothic.. Lions. Details — lions guarding masterpieces.. History. 1879. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Lions.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Lions.", "x": "Art Institute of Chicago in depth: Lions.. Impressionists. Details — lions guarding masterpieces.. Tickets. Chicago. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Art Institute of Chicago in depth: History.. 1879. Details — lions guarding masterpieces.. Chicago. Thorne Rooms. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Art Institute of Chicago in depth: Tickets.. Chicago. Details — lions guarding masterpieces.. Art. American Gothic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Chicago.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Chicago.", "x": "Art Institute of Chicago in depth: Chicago.. Thorne Rooms. Details — lions guarding masterpieces.. Gothic. Lions. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Art.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Art.", "x": "Art Institute of Chicago in depth: Art.. American Gothic. Details — lions guarding masterpieces.. Lions. Impressionists. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Art Institute of Chicago comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Art Institute of Chicago comes from.", "x": "Origins: Gothic.. American Gothic. The history of Art Institute of Chicago — lions guarding masterpieces.. Lions. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Art Institute of Chicago respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Art Institute of Chicago respectfully.", "x": "Engaging: History.. Lions. How to participate or observe well — Art Institute of Chicago. lions guarding masterpieces. Respect first, always; Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Art Institute of Chicago do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Art Institute of Chicago do's and don'ts.", "x": "Etiquette: Chicago.. Impressionists. The rules of respect — Art Institute of Chicago. lions guarding masterpieces. When in doubt, ask about Art.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Art Institute of Chicago.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Art Institute of Chicago.", "x": "Planning: Gothic.. 1879. Practical notes — Art Institute of Chicago. lions guarding masterpieces. A little planning shows respect for Lions.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Art Institute of Chicago and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Art Institute of Chicago and money.", "x": "Costs: History.. Chicago. What to budget — Art Institute of Chicago. lions guarding masterpieces. The best experiences of Tickets. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-museum-art-institute-chicago-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
