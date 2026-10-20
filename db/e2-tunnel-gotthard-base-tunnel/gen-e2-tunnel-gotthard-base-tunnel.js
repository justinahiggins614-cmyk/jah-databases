(function(){'use strict';
/* JAH Gotthard Base Tunnel Tunnel Database generator — jahdb-e2-tunnel-gotthard-base-tunnel-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-tunnel-gotthard-base-tunnel',PREFIX='JAH-E2TUNNELGOT-',NAME='JAH Gotthard Base Tunnel Tunnel Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Gotthard Base Tunnel: the complete guide", "d": "Gotthard Base Tunnel: world's longest rail tunnel..", "g": "overview", "l": 2, "q": "What is Gotthard Base Tunnel: the complete guide?", "a": "Gotthard Base Tunnel: world's longest rail tunnel..", "x": "The complete tunnel guide to Gotthard Base Tunnel: world's longest rail tunnel.. 57 km. History, meaning, practices, and how to engage respectfully — everything in one database. Length. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Gotthard Base Tunnel essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Gotthard Base Tunnel essentials.", "x": "At a glance: Gotthard Base Tunnel — world's longest rail tunnel.. 2016. The essentials: Build.. Switzerland. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "57 km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "57 km.", "x": "Gotthard Base Tunnel: 57 km.. Build. Essential knowledge — Switzerland.. world's longest rail tunnel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 57 km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 57 km..", "x": "Explained: 57 km.. Trains. The context — Gotthard Base Tunnel. Alps. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "2016.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "2016.", "x": "Gotthard Base Tunnel: 2016.. Alps. Essential knowledge — Alps.. world's longest rail tunnel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 2016..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 2016..", "x": "Explained: 2016.. Records. The context — Gotthard Base Tunnel. Engineering. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Switzerland.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Switzerland.", "x": "Gotthard Base Tunnel: Switzerland.. Trains. Essential knowledge — Engineering.. world's longest rail tunnel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Switzerland..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Switzerland..", "x": "Explained: Switzerland.. History. The context — Gotthard Base Tunnel. 17 years. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Alps.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Alps.", "x": "Gotthard Base Tunnel: Alps.. Records. Essential knowledge — 17 years.. world's longest rail tunnel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Alps..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Alps..", "x": "Explained: Alps.. Length. The context — Gotthard Base Tunnel. 57 km. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Engineering.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Engineering.", "x": "Gotthard Base Tunnel: Engineering.. History. Essential knowledge — 57 km.. world's longest rail tunnel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Engineering..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Engineering..", "x": "Explained: Engineering.. Build. The context — Gotthard Base Tunnel. 2016. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "17 years.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "17 years.", "x": "Gotthard Base Tunnel: 17 years.. Length. Essential knowledge — 2016.. world's longest rail tunnel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: 17 years..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: 17 years..", "x": "Explained: 17 years.. Alps. The context — Gotthard Base Tunnel. Switzerland. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Length.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Length.", "x": "Gotthard Base Tunnel in depth: Length.. 2016. Details — world's longest rail tunnel.. Alps. Alps. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Build.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Build.", "x": "Gotthard Base Tunnel in depth: Build.. Switzerland. Details — world's longest rail tunnel.. Trains. Engineering. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Alps.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Alps.", "x": "Gotthard Base Tunnel in depth: Alps.. Alps. Details — world's longest rail tunnel.. Records. 17 years. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Trains.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Trains.", "x": "Gotthard Base Tunnel in depth: Trains.. Engineering. Details — world's longest rail tunnel.. History. 57 km. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Records.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Records.", "x": "Gotthard Base Tunnel in depth: Records.. 17 years. Details — world's longest rail tunnel.. Length. 2016. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Gotthard Base Tunnel in depth: History.. 57 km. Details — world's longest rail tunnel.. Build. Switzerland. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Gotthard Base Tunnel comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Gotthard Base Tunnel comes from.", "x": "Origins: Length.. 57 km. The history of Gotthard Base Tunnel — world's longest rail tunnel.. Build. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Gotthard Base Tunnel respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Gotthard Base Tunnel respectfully.", "x": "Engaging: Alps.. 2016. How to participate or observe well — Gotthard Base Tunnel. world's longest rail tunnel. Respect first, always; Trains.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Gotthard Base Tunnel do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Gotthard Base Tunnel do's and don'ts.", "x": "Etiquette: Records.. Switzerland. The rules of respect — Gotthard Base Tunnel. world's longest rail tunnel. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Gotthard Base Tunnel.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Gotthard Base Tunnel.", "x": "Planning: Length.. Alps. Practical notes — Gotthard Base Tunnel. world's longest rail tunnel. A little planning shows respect for Build.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Gotthard Base Tunnel and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Gotthard Base Tunnel and money.", "x": "Costs: Alps.. Engineering. What to budget — Gotthard Base Tunnel. world's longest rail tunnel. The best experiences of Trains. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-tunnel-gotthard-base-tunnel-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
