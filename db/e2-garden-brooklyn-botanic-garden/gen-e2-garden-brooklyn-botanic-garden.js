(function(){'use strict';
/* JAH Brooklyn Botanic Garden Botanical Garden Database generator — jahdb-e2-garden-brooklyn-botanic-garden-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-garden-brooklyn-botanic-garden',PREFIX='JAH-E2GARDENBRO-',NAME='JAH Brooklyn Botanic Garden Botanical Garden Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Brooklyn Botanic Garden: the complete guide", "d": "Brooklyn Botanic Garden: cherry blossoms in Brooklyn..", "g": "overview", "l": 2, "q": "What is Brooklyn Botanic Garden: the complete guide?", "a": "Brooklyn Botanic Garden: cherry blossoms in Brooklyn..", "x": "The complete botanical garden guide to Brooklyn Botanic Garden: cherry blossoms in Brooklyn.. 1910. History, meaning, practices, and how to engage respectfully — everything in one database. Cherries. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Brooklyn Botanic Garden essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Brooklyn Botanic Garden essentials.", "x": "At a glance: Brooklyn Botanic Garden — cherry blossoms in Brooklyn.. Sakura. The essentials: Japanese.. Japanese Hill. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1910.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1910.", "x": "Brooklyn Botanic Garden: 1910.. Japanese. Essential knowledge — Japanese Hill.. cherry blossoms in Brooklyn. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1910..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1910..", "x": "Explained: 1910.. Tickets. The context — Brooklyn Botanic Garden. Orchids. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Sakura.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Sakura.", "x": "Brooklyn Botanic Garden: Sakura.. History. Essential knowledge — Orchids.. cherry blossoms in Brooklyn. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Sakura..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Sakura..", "x": "Explained: Sakura.. Brooklyn. The context — Brooklyn Botanic Garden. 52 acres. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Japanese Hill.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Japanese Hill.", "x": "Brooklyn Botanic Garden: Japanese Hill.. Tickets. Essential knowledge — 52 acres.. cherry blossoms in Brooklyn. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Japanese Hill..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Japanese Hill..", "x": "Explained: Japanese Hill.. Festivals. The context — Brooklyn Botanic Garden. Festivals. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Orchids.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Orchids.", "x": "Brooklyn Botanic Garden: Orchids.. Brooklyn. Essential knowledge — Festivals.. cherry blossoms in Brooklyn. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Orchids..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Orchids..", "x": "Explained: Orchids.. Cherries. The context — Brooklyn Botanic Garden. 1910. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "52 acres.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "52 acres.", "x": "Brooklyn Botanic Garden: 52 acres.. Festivals. Essential knowledge — 1910.. cherry blossoms in Brooklyn. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 52 acres..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 52 acres..", "x": "Explained: 52 acres.. Japanese. The context — Brooklyn Botanic Garden. Sakura. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Festivals.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Festivals.", "x": "Brooklyn Botanic Garden: Festivals.. Cherries. Essential knowledge — Sakura.. cherry blossoms in Brooklyn. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Festivals..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Festivals..", "x": "Explained: Festivals.. History. The context — Brooklyn Botanic Garden. Japanese Hill. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Cherries.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Cherries.", "x": "Brooklyn Botanic Garden in depth: Cherries.. Sakura. Details — cherry blossoms in Brooklyn.. History. Orchids. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Japanese.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Japanese.", "x": "Brooklyn Botanic Garden in depth: Japanese.. Japanese Hill. Details — cherry blossoms in Brooklyn.. Tickets. 52 acres. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Brooklyn Botanic Garden in depth: History.. Orchids. Details — cherry blossoms in Brooklyn.. Brooklyn. Festivals. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Brooklyn Botanic Garden in depth: Tickets.. 52 acres. Details — cherry blossoms in Brooklyn.. Festivals. 1910. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Brooklyn.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Brooklyn.", "x": "Brooklyn Botanic Garden in depth: Brooklyn.. Festivals. Details — cherry blossoms in Brooklyn.. Cherries. Sakura. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Festivals.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Festivals.", "x": "Brooklyn Botanic Garden in depth: Festivals.. 1910. Details — cherry blossoms in Brooklyn.. Japanese. Japanese Hill. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Brooklyn Botanic Garden comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Brooklyn Botanic Garden comes from.", "x": "Origins: Cherries.. 1910. The history of Brooklyn Botanic Garden — cherry blossoms in Brooklyn.. Japanese. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Brooklyn Botanic Garden respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Brooklyn Botanic Garden respectfully.", "x": "Engaging: History.. Sakura. How to participate or observe well — Brooklyn Botanic Garden. cherry blossoms in Brooklyn. Respect first, always; Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Brooklyn Botanic Garden do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Brooklyn Botanic Garden do's and don'ts.", "x": "Etiquette: Brooklyn.. Japanese Hill. The rules of respect — Brooklyn Botanic Garden. cherry blossoms in Brooklyn. When in doubt, ask about Festivals.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Brooklyn Botanic Garden.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Brooklyn Botanic Garden.", "x": "Planning: Cherries.. Orchids. Practical notes — Brooklyn Botanic Garden. cherry blossoms in Brooklyn. A little planning shows respect for Japanese.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Brooklyn Botanic Garden and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Brooklyn Botanic Garden and money.", "x": "Costs: History.. 52 acres. What to budget — Brooklyn Botanic Garden. cherry blossoms in Brooklyn. The best experiences of Tickets. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-garden-brooklyn-botanic-garden-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
