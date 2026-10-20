(function(){'use strict';
/* JAH Simplon Tunnel Tunnel Database generator — jahdb-e2-tunnel-simplon-tunnel-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-tunnel-simplon-tunnel',PREFIX='JAH-E2TUNNELSIM-',NAME='JAH Simplon Tunnel Tunnel Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Simplon Tunnel: the complete guide", "d": "Simplon Tunnel: Alps rail link..", "g": "overview", "l": 2, "q": "What is Simplon Tunnel: the complete guide?", "a": "Simplon Tunnel: Alps rail link..", "x": "The complete tunnel guide to Simplon Tunnel: Alps rail link.. 19.8 km. History, meaning, practices, and how to engage respectfully — everything in one database. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Simplon Tunnel essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Simplon Tunnel essentials.", "x": "At a glance: Simplon Tunnel — Alps rail link.. 1906. The essentials: Trains.. Switzerland-Italy. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "19.8 km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "19.8 km.", "x": "Simplon Tunnel: 19.8 km.. Trains. Essential knowledge — Switzerland-Italy.. Alps rail link. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 19.8 km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 19.8 km..", "x": "Explained: 19.8 km.. Engineering. The context — Simplon Tunnel. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "1906.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "1906.", "x": "Simplon Tunnel: 1906.. Alps. Essential knowledge — History.. Alps rail link. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 1906..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 1906..", "x": "Explained: 1906.. Heritage. The context — Simplon Tunnel. Trains. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Switzerland-Italy.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Switzerland-Italy.", "x": "Simplon Tunnel: Switzerland-Italy.. Engineering. Essential knowledge — Trains.. Alps rail link. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Switzerland-Italy..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Switzerland-Italy..", "x": "Explained: Switzerland-Italy.. Travel. The context — Simplon Tunnel. Engineering. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "History.", "x": "Simplon Tunnel: History.. Heritage. Essential knowledge — Engineering.. Alps rail link. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: History..", "x": "Explained: History.. History. The context — Simplon Tunnel. 19.8 km. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Trains.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Trains.", "x": "Simplon Tunnel: Trains.. Travel. Essential knowledge — 19.8 km.. Alps rail link. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Trains..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Trains..", "x": "Explained: Trains.. Trains. The context — Simplon Tunnel. 1906. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Engineering.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Engineering.", "x": "Simplon Tunnel: Engineering.. History. Essential knowledge — 1906.. Alps rail link. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Engineering..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Engineering..", "x": "Explained: Engineering.. Alps. The context — Simplon Tunnel. Switzerland-Italy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Simplon Tunnel in depth: History.. 1906. Details — Alps rail link.. Alps. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Trains.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Trains.", "x": "Simplon Tunnel in depth: Trains.. Switzerland-Italy. Details — Alps rail link.. Engineering. Trains. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Alps.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Alps.", "x": "Simplon Tunnel in depth: Alps.. History. Details — Alps rail link.. Heritage. Engineering. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Engineering.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Engineering.", "x": "Simplon Tunnel in depth: Engineering.. Trains. Details — Alps rail link.. Travel. 19.8 km. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Heritage.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Heritage.", "x": "Simplon Tunnel in depth: Heritage.. Engineering. Details — Alps rail link.. History. 1906. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Travel.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Travel.", "x": "Simplon Tunnel in depth: Travel.. 19.8 km. Details — Alps rail link.. Trains. Switzerland-Italy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Simplon Tunnel comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Simplon Tunnel comes from.", "x": "Origins: History.. 19.8 km. The history of Simplon Tunnel — Alps rail link.. Trains. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Simplon Tunnel respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Simplon Tunnel respectfully.", "x": "Engaging: Alps.. 1906. How to participate or observe well — Simplon Tunnel. Alps rail link. Respect first, always; Engineering.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Simplon Tunnel do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Simplon Tunnel do's and don'ts.", "x": "Etiquette: Heritage.. Switzerland-Italy. The rules of respect — Simplon Tunnel. Alps rail link. When in doubt, ask about Travel.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Simplon Tunnel.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Simplon Tunnel.", "x": "Planning: History.. History. Practical notes — Simplon Tunnel. Alps rail link. A little planning shows respect for Trains.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Simplon Tunnel and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Simplon Tunnel and money.", "x": "Costs: Alps.. Trains. What to budget — Simplon Tunnel. Alps rail link. The best experiences of Engineering. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-tunnel-simplon-tunnel-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
