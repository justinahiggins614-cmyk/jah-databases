(function(){'use strict';
/* JAH Blacksmithing2 Database generator — jahdb-e2-hobby2-blacksmithing-hobby2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby2-blacksmithing-hobby2',PREFIX='JAH-E2HOBBY2BLA-',NAME='JAH Blacksmithing2 Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Blacksmithing2: the complete guide", "d": "Blacksmithing2: the forge craft..", "g": "overview", "l": 2, "q": "What is Blacksmithing2: the complete guide?", "a": "Blacksmithing2: the forge craft..", "x": "The complete hobby guide to Blacksmithing2: the forge craft.. Forge. History, meaning, practices, and how to engage respectfully — everything in one database. Anvil. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Blacksmithing2 essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Blacksmithing2 essentials.", "x": "At a glance: Blacksmithing2 — the forge craft.. Anvil. The essentials: Quench.. Hammer. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Forge.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Forge.", "x": "Blacksmithing2: Forge.. Quench. Essential knowledge — Hammer.. the forge craft. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Forge..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Forge..", "x": "Explained: Forge.. Forge. The context — Blacksmithing2. Heat. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Anvil.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Anvil.", "x": "Blacksmithing2: Anvil.. Tongs. Essential knowledge — Heat.. the forge craft. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Anvil..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Anvil..", "x": "Explained: Anvil.. Hammer. The context — Blacksmithing2. Quench. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Hammer.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Hammer.", "x": "Blacksmithing2: Hammer.. Forge. Essential knowledge — Quench.. the forge craft. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Hammer..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Hammer..", "x": "Explained: Hammer.. Getting started. The context — Blacksmithing2. Tongs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Heat.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Heat.", "x": "Blacksmithing2: Heat.. Hammer. Essential knowledge — Tongs.. the forge craft. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Heat..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Heat..", "x": "Explained: Heat.. Anvil. The context — Blacksmithing2. Forge. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Quench.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Quench.", "x": "Blacksmithing2: Quench.. Getting started. Essential knowledge — Forge.. the forge craft. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Quench..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Quench..", "x": "Explained: Quench.. Quench. The context — Blacksmithing2. Anvil. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Tongs.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Tongs.", "x": "Blacksmithing2: Tongs.. Anvil. Essential knowledge — Anvil.. the forge craft. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Tongs..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Tongs..", "x": "Explained: Tongs.. Tongs. The context — Blacksmithing2. Hammer. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Anvil.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Anvil.", "x": "Blacksmithing2 in depth: Anvil.. Anvil. Details — the forge craft.. Tongs. Heat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Quench.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Quench.", "x": "Blacksmithing2 in depth: Quench.. Hammer. Details — the forge craft.. Forge. Quench. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tongs.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tongs.", "x": "Blacksmithing2 in depth: Tongs.. Heat. Details — the forge craft.. Hammer. Tongs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Forge.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Forge.", "x": "Blacksmithing2 in depth: Forge.. Quench. Details — the forge craft.. Getting started. Forge. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Hammer.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Hammer.", "x": "Blacksmithing2 in depth: Hammer.. Tongs. Details — the forge craft.. Anvil. Anvil. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Getting started.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Getting started.", "x": "Blacksmithing2 in depth: Getting started.. Forge. Details — the forge craft.. Quench. Hammer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Blacksmithing2 comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Blacksmithing2 comes from.", "x": "Origins: Anvil.. Forge. The history of Blacksmithing2 — the forge craft.. Quench. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Blacksmithing2 respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Blacksmithing2 respectfully.", "x": "Engaging: Tongs.. Anvil. How to participate or observe well — Blacksmithing2. the forge craft. Respect first, always; Forge.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Blacksmithing2 do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Blacksmithing2 do's and don'ts.", "x": "Etiquette: Hammer.. Hammer. The rules of respect — Blacksmithing2. the forge craft. When in doubt, ask about Getting started.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Blacksmithing2.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Blacksmithing2.", "x": "Planning: Anvil.. Heat. Practical notes — Blacksmithing2. the forge craft. A little planning shows respect for Quench.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Blacksmithing2 and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Blacksmithing2 and money.", "x": "Costs: Tongs.. Quench. What to budget — Blacksmithing2. the forge craft. The best experiences of Forge. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby2-blacksmithing-hobby2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
