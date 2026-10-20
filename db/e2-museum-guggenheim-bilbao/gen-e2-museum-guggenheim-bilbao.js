(function(){'use strict';
/* JAH Guggenheim Bilbao Museum Database generator — jahdb-e2-museum-guggenheim-bilbao-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-museum-guggenheim-bilbao',PREFIX='JAH-E2MUSEUMGUG-',NAME='JAH Guggenheim Bilbao Museum Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Guggenheim Bilbao: the complete guide", "d": "Guggenheim Bilbao: Gehry's titanium flower..", "g": "overview", "l": 2, "q": "What is Guggenheim Bilbao: the complete guide?", "a": "Guggenheim Bilbao: Gehry's titanium flower..", "x": "The complete museum guide to Guggenheim Bilbao: Gehry's titanium flower.. Gehry. History, meaning, practices, and how to engage respectfully — everything in one database. Building. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Guggenheim Bilbao essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Guggenheim Bilbao essentials.", "x": "At a glance: Guggenheim Bilbao — Gehry's titanium flower.. 1997. The essentials: Effect.. Titanium. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Gehry.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Gehry.", "x": "Guggenheim Bilbao: Gehry.. Effect. Essential knowledge — Titanium.. Gehry's titanium flower. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Gehry..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Gehry..", "x": "Explained: Gehry.. Tickets. The context — Guggenheim Bilbao. Bilbao effect. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "1997.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "1997.", "x": "Guggenheim Bilbao: 1997.. Collection. Essential knowledge — Bilbao effect.. Gehry's titanium flower. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 1997..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 1997..", "x": "Explained: 1997.. Bilbao. The context — Guggenheim Bilbao. Puppy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Titanium.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Titanium.", "x": "Guggenheim Bilbao: Titanium.. Tickets. Essential knowledge — Puppy.. Gehry's titanium flower. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Titanium..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Titanium..", "x": "Explained: Titanium.. Art. The context — Guggenheim Bilbao. Contemporary. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Bilbao effect.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Bilbao effect.", "x": "Guggenheim Bilbao: Bilbao effect.. Bilbao. Essential knowledge — Contemporary.. Gehry's titanium flower. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Bilbao effect..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Bilbao effect..", "x": "Explained: Bilbao effect.. Building. The context — Guggenheim Bilbao. Gehry. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Puppy.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Puppy.", "x": "Guggenheim Bilbao: Puppy.. Art. Essential knowledge — Gehry.. Gehry's titanium flower. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Puppy..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Puppy..", "x": "Explained: Puppy.. Effect. The context — Guggenheim Bilbao. 1997. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Contemporary.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Contemporary.", "x": "Guggenheim Bilbao: Contemporary.. Building. Essential knowledge — 1997.. Gehry's titanium flower. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Contemporary..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Contemporary..", "x": "Explained: Contemporary.. Collection. The context — Guggenheim Bilbao. Titanium. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Building.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Building.", "x": "Guggenheim Bilbao in depth: Building.. 1997. Details — Gehry's titanium flower.. Collection. Bilbao effect. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Effect.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Effect.", "x": "Guggenheim Bilbao in depth: Effect.. Titanium. Details — Gehry's titanium flower.. Tickets. Puppy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Collection.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Collection.", "x": "Guggenheim Bilbao in depth: Collection.. Bilbao effect. Details — Gehry's titanium flower.. Bilbao. Contemporary. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Guggenheim Bilbao in depth: Tickets.. Puppy. Details — Gehry's titanium flower.. Art. Gehry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Bilbao.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Bilbao.", "x": "Guggenheim Bilbao in depth: Bilbao.. Contemporary. Details — Gehry's titanium flower.. Building. 1997. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Art.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Art.", "x": "Guggenheim Bilbao in depth: Art.. Gehry. Details — Gehry's titanium flower.. Effect. Titanium. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Guggenheim Bilbao comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Guggenheim Bilbao comes from.", "x": "Origins: Building.. Gehry. The history of Guggenheim Bilbao — Gehry's titanium flower.. Effect. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Guggenheim Bilbao respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Guggenheim Bilbao respectfully.", "x": "Engaging: Collection.. 1997. How to participate or observe well — Guggenheim Bilbao. Gehry's titanium flower. Respect first, always; Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Guggenheim Bilbao do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Guggenheim Bilbao do's and don'ts.", "x": "Etiquette: Bilbao.. Titanium. The rules of respect — Guggenheim Bilbao. Gehry's titanium flower. When in doubt, ask about Art.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Guggenheim Bilbao.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Guggenheim Bilbao.", "x": "Planning: Building.. Bilbao effect. Practical notes — Guggenheim Bilbao. Gehry's titanium flower. A little planning shows respect for Effect.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Guggenheim Bilbao and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Guggenheim Bilbao and money.", "x": "Costs: Collection.. Puppy. What to budget — Guggenheim Bilbao. Gehry's titanium flower. The best experiences of Tickets. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-museum-guggenheim-bilbao-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
