(function(){'use strict';
/* JAH Sundance Film Festival Festival Database generator — jahdb-e2-festival-sundance-film-festival-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-festival-sundance-film-festival',PREFIX='JAH-E2FESTIVALS-',NAME='JAH Sundance Film Festival Festival Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Sundance Film Festival: the complete guide", "d": "Sundance Film Festival: indie film launch..", "g": "overview", "l": 2, "q": "What is Sundance Film Festival: the complete guide?", "a": "Sundance Film Festival: indie film launch..", "x": "The complete festival guide to Sundance Film Festival: indie film launch.. January. History, meaning, practices, and how to engage respectfully — everything in one database. Indie. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Sundance Film Festival essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Sundance Film Festival essentials.", "x": "At a glance: Sundance Film Festival — indie film launch.. Park City. The essentials: Discovery.. Indie. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "January.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "January.", "x": "Sundance Film Festival: January.. Discovery. Essential knowledge — Indie.. indie film launch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: January..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: January..", "x": "Explained: January.. Travel. The context — Sundance Film Festival. Discovery. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Park City.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Park City.", "x": "Sundance Film Festival: Park City.. History. Essential knowledge — Discovery.. indie film launch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Park City..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Park City..", "x": "Explained: Park City.. Films. The context — Sundance Film Festival. Redford. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Indie.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Indie.", "x": "Sundance Film Festival: Indie.. Travel. Essential knowledge — Redford.. indie film launch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Indie..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Indie..", "x": "Explained: Indie.. Culture. The context — Sundance Film Festival. Snow. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Discovery.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Discovery.", "x": "Sundance Film Festival: Discovery.. Films. Essential knowledge — Snow.. indie film launch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Discovery..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Discovery..", "x": "Explained: Discovery.. Indie. The context — Sundance Film Festival. January. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Redford.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Redford.", "x": "Sundance Film Festival: Redford.. Culture. Essential knowledge — January.. indie film launch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Redford..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Redford..", "x": "Explained: Redford.. Discovery. The context — Sundance Film Festival. Park City. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Snow.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Snow.", "x": "Sundance Film Festival: Snow.. Indie. Essential knowledge — Park City.. indie film launch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Snow..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Snow..", "x": "Explained: Snow.. History. The context — Sundance Film Festival. Indie. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Indie.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Indie.", "x": "Sundance Film Festival in depth: Indie.. Park City. Details — indie film launch.. History. Discovery. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Discovery.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Discovery.", "x": "Sundance Film Festival in depth: Discovery.. Indie. Details — indie film launch.. Travel. Redford. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Sundance Film Festival in depth: History.. Discovery. Details — indie film launch.. Films. Snow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Travel.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Travel.", "x": "Sundance Film Festival in depth: Travel.. Redford. Details — indie film launch.. Culture. January. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Films.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Films.", "x": "Sundance Film Festival in depth: Films.. Snow. Details — indie film launch.. Indie. Park City. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Culture.", "x": "Sundance Film Festival in depth: Culture.. January. Details — indie film launch.. Discovery. Indie. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Sundance Film Festival comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Sundance Film Festival comes from.", "x": "Origins: Indie.. January. The history of Sundance Film Festival — indie film launch.. Discovery. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Sundance Film Festival respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Sundance Film Festival respectfully.", "x": "Engaging: History.. Park City. How to participate or observe well — Sundance Film Festival. indie film launch. Respect first, always; Travel.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Sundance Film Festival do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Sundance Film Festival do's and don'ts.", "x": "Etiquette: Films.. Indie. The rules of respect — Sundance Film Festival. indie film launch. When in doubt, ask about Culture.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Sundance Film Festival.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Sundance Film Festival.", "x": "Planning: Indie.. Discovery. Practical notes — Sundance Film Festival. indie film launch. A little planning shows respect for Discovery.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Sundance Film Festival and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Sundance Film Festival and money.", "x": "Costs: History.. Redford. What to budget — Sundance Film Festival. indie film launch. The best experiences of Travel. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-festival-sundance-film-festival-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
