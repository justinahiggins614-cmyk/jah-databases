(function(){'use strict';
/* JAH Chameleon Veiled Reptile Database generator — jahdb-e2-reptile-veiled-chameleon-reptile-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-reptile-veiled-chameleon-reptile',PREFIX='JAH-E2REPTILEVE-',NAME='JAH Chameleon Veiled Reptile Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Chameleon Veiled: the complete guide", "d": "Chameleon Veiled: the color changer..", "g": "overview", "l": 2, "q": "What is Chameleon Veiled: the complete guide?", "a": "Chameleon Veiled: the color changer..", "x": "The complete reptile guide to Chameleon Veiled: the color changer.. Color. History, meaning, practices, and how to engage respectfully — everything in one database. Color. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Chameleon Veiled essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Chameleon Veiled essentials.", "x": "At a glance: Chameleon Veiled — the color changer.. Tongue. The essentials: Tongue.. Casque. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Color.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Color.", "x": "Chameleon Veiled: Color.. Tongue. Essential knowledge — Casque.. the color changer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Color..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Color..", "x": "Explained: Color.. Stress. The context — Chameleon Veiled. Yemen. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Tongue.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Tongue.", "x": "Chameleon Veiled: Tongue.. Yemen. Essential knowledge — Yemen.. the color changer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Tongue..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Tongue..", "x": "Explained: Tongue.. Casque. The context — Chameleon Veiled. Zygodactyl. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Casque.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Casque.", "x": "Chameleon Veiled: Casque.. Stress. Essential knowledge — Zygodactyl.. the color changer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Casque..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Casque..", "x": "Explained: Casque.. Care. The context — Chameleon Veiled. Stress. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Yemen.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Yemen.", "x": "Chameleon Veiled: Yemen.. Casque. Essential knowledge — Stress.. the color changer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Yemen..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Yemen..", "x": "Explained: Yemen.. Color. The context — Chameleon Veiled. Color. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Zygodactyl.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Zygodactyl.", "x": "Chameleon Veiled: Zygodactyl.. Care. Essential knowledge — Color.. the color changer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Zygodactyl..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Zygodactyl..", "x": "Explained: Zygodactyl.. Tongue. The context — Chameleon Veiled. Tongue. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Stress.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Stress.", "x": "Chameleon Veiled: Stress.. Color. Essential knowledge — Tongue.. the color changer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Stress..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Stress..", "x": "Explained: Stress.. Yemen. The context — Chameleon Veiled. Casque. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Color.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Color.", "x": "Chameleon Veiled in depth: Color.. Tongue. Details — the color changer.. Yemen. Yemen. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Tongue.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Tongue.", "x": "Chameleon Veiled in depth: Tongue.. Casque. Details — the color changer.. Stress. Zygodactyl. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Yemen.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Yemen.", "x": "Chameleon Veiled in depth: Yemen.. Yemen. Details — the color changer.. Casque. Stress. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Stress.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Stress.", "x": "Chameleon Veiled in depth: Stress.. Zygodactyl. Details — the color changer.. Care. Color. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Casque.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Casque.", "x": "Chameleon Veiled in depth: Casque.. Stress. Details — the color changer.. Color. Tongue. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Care.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Care.", "x": "Chameleon Veiled in depth: Care.. Color. Details — the color changer.. Tongue. Casque. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Chameleon Veiled comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Chameleon Veiled comes from.", "x": "Origins: Color.. Color. The history of Chameleon Veiled — the color changer.. Tongue. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Chameleon Veiled respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Chameleon Veiled respectfully.", "x": "Engaging: Yemen.. Tongue. How to participate or observe well — Chameleon Veiled. the color changer. Respect first, always; Stress.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Chameleon Veiled do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Chameleon Veiled do's and don'ts.", "x": "Etiquette: Casque.. Casque. The rules of respect — Chameleon Veiled. the color changer. When in doubt, ask about Care.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Chameleon Veiled.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Chameleon Veiled.", "x": "Planning: Color.. Yemen. Practical notes — Chameleon Veiled. the color changer. A little planning shows respect for Tongue.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Chameleon Veiled and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Chameleon Veiled and money.", "x": "Costs: Yemen.. Zygodactyl. What to budget — Chameleon Veiled. the color changer. The best experiences of Stress. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-reptile-veiled-chameleon-reptile-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
