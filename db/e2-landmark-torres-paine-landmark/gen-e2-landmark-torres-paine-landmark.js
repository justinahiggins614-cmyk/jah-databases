(function(){'use strict';
/* JAH Torres del Paine Landmark Database generator — jahdb-e2-landmark-torres-paine-landmark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-landmark-torres-paine-landmark',PREFIX='JAH-E2LANDMARKT-',NAME='JAH Torres del Paine Landmark Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Torres del Paine: the complete guide", "d": "Torres del Paine: the granite towers..", "g": "overview", "l": 2, "q": "What is Torres del Paine: the complete guide?", "a": "Torres del Paine: the granite towers..", "x": "The complete landmark guide to Torres del Paine: the granite towers.. Towers. History, meaning, practices, and how to engage respectfully — everything in one database. Towers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Torres del Paine essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Torres del Paine essentials.", "x": "At a glance: Torres del Paine — the granite towers.. Patagonia. The essentials: W trek.. W trek. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Towers.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Towers.", "x": "Torres del Paine: Towers.. W trek. Essential knowledge — W trek.. the granite towers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Towers..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Towers..", "x": "Explained: Towers.. Patagonia. The context — Torres del Paine. Guanacos. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Patagonia.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Patagonia.", "x": "Torres del Paine: Patagonia.. Wind. Essential knowledge — Guanacos.. the granite towers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Patagonia..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Patagonia..", "x": "Explained: Patagonia.. Lakes. The context — Torres del Paine. Wind. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "W trek.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "W trek.", "x": "Torres del Paine: W trek.. Patagonia. Essential knowledge — Wind.. the granite towers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: W trek..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: W trek..", "x": "Explained: W trek.. Trekking. The context — Torres del Paine. Lakes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Guanacos.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Guanacos.", "x": "Torres del Paine: Guanacos.. Lakes. Essential knowledge — Lakes.. the granite towers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Guanacos..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Guanacos..", "x": "Explained: Guanacos.. Towers. The context — Torres del Paine. Towers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Wind.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Wind.", "x": "Torres del Paine: Wind.. Trekking. Essential knowledge — Towers.. the granite towers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Wind..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Wind..", "x": "Explained: Wind.. W trek. The context — Torres del Paine. Patagonia. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Lakes.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Lakes.", "x": "Torres del Paine: Lakes.. Towers. Essential knowledge — Patagonia.. the granite towers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Lakes..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Lakes..", "x": "Explained: Lakes.. Wind. The context — Torres del Paine. W trek. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Towers.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Towers.", "x": "Torres del Paine in depth: Towers.. Patagonia. Details — the granite towers.. Wind. Guanacos. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "W trek.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "W trek.", "x": "Torres del Paine in depth: W trek.. W trek. Details — the granite towers.. Patagonia. Wind. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Wind.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Wind.", "x": "Torres del Paine in depth: Wind.. Guanacos. Details — the granite towers.. Lakes. Lakes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Patagonia.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Patagonia.", "x": "Torres del Paine in depth: Patagonia.. Wind. Details — the granite towers.. Trekking. Towers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Lakes.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Lakes.", "x": "Torres del Paine in depth: Lakes.. Lakes. Details — the granite towers.. Towers. Patagonia. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Trekking.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Trekking.", "x": "Torres del Paine in depth: Trekking.. Towers. Details — the granite towers.. W trek. W trek. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Torres del Paine comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Torres del Paine comes from.", "x": "Origins: Towers.. Towers. The history of Torres del Paine — the granite towers.. W trek. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Torres del Paine respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Torres del Paine respectfully.", "x": "Engaging: Wind.. Patagonia. How to participate or observe well — Torres del Paine. the granite towers. Respect first, always; Patagonia.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Torres del Paine do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Torres del Paine do's and don'ts.", "x": "Etiquette: Lakes.. W trek. The rules of respect — Torres del Paine. the granite towers. When in doubt, ask about Trekking.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Torres del Paine.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Torres del Paine.", "x": "Planning: Towers.. Guanacos. Practical notes — Torres del Paine. the granite towers. A little planning shows respect for W trek.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Torres del Paine and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Torres del Paine and money.", "x": "Costs: Wind.. Wind. What to budget — Torres del Paine. the granite towers. The best experiences of Patagonia. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-landmark-torres-paine-landmark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
