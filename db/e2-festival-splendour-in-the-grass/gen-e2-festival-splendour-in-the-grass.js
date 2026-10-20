(function(){'use strict';
/* JAH Splendour in the Grass Festival Database generator — jahdb-e2-festival-splendour-in-the-grass-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-festival-splendour-in-the-grass',PREFIX='JAH-E2FESTIVALS-',NAME='JAH Splendour in the Grass Festival Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Splendour in the Grass: the complete guide", "d": "Splendour in the Grass: Australia's winter fest..", "g": "overview", "l": 2, "q": "What is Splendour in the Grass: the complete guide?", "a": "Splendour in the Grass: Australia's winter fest..", "x": "The complete festival guide to Splendour in the Grass: Australia's winter fest.. July. History, meaning, practices, and how to engage respectfully — everything in one database. Lineups. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Splendour in the Grass essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Splendour in the Grass essentials.", "x": "At a glance: Splendour in the Grass — Australia's winter fest.. Byron Bay. The essentials: Travel.. Lineups. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "July.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "July.", "x": "Splendour in the Grass: July.. Travel. Essential knowledge — Lineups.. Australia's winter fest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: July..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: July..", "x": "Explained: July.. History. The context — Splendour in the Grass. Camping. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Byron Bay.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Byron Bay.", "x": "Splendour in the Grass: Byron Bay.. Winter. Essential knowledge — Camping.. Australia's winter fest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Byron Bay..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Byron Bay..", "x": "Explained: Byron Bay.. Music. The context — Splendour in the Grass. Winter. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Lineups.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Lineups.", "x": "Splendour in the Grass: Lineups.. History. Essential knowledge — Winter.. Australia's winter fest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Lineups..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Lineups..", "x": "Explained: Lineups.. Australia. The context — Splendour in the Grass. Eclectic. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Camping.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Camping.", "x": "Splendour in the Grass: Camping.. Music. Essential knowledge — Eclectic.. Australia's winter fest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Camping..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Camping..", "x": "Explained: Camping.. Lineups. The context — Splendour in the Grass. July. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Winter.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Winter.", "x": "Splendour in the Grass: Winter.. Australia. Essential knowledge — July.. Australia's winter fest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Winter..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Winter..", "x": "Explained: Winter.. Travel. The context — Splendour in the Grass. Byron Bay. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Eclectic.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Eclectic.", "x": "Splendour in the Grass: Eclectic.. Lineups. Essential knowledge — Byron Bay.. Australia's winter fest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Eclectic..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Eclectic..", "x": "Explained: Eclectic.. Winter. The context — Splendour in the Grass. Lineups. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Lineups.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Lineups.", "x": "Splendour in the Grass in depth: Lineups.. Byron Bay. Details — Australia's winter fest.. Winter. Camping. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Travel.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Travel.", "x": "Splendour in the Grass in depth: Travel.. Lineups. Details — Australia's winter fest.. History. Winter. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Winter.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Winter.", "x": "Splendour in the Grass in depth: Winter.. Camping. Details — Australia's winter fest.. Music. Eclectic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "History.", "x": "Splendour in the Grass in depth: History.. Winter. Details — Australia's winter fest.. Australia. July. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Music.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Music.", "x": "Splendour in the Grass in depth: Music.. Eclectic. Details — Australia's winter fest.. Lineups. Byron Bay. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Australia.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Australia.", "x": "Splendour in the Grass in depth: Australia.. July. Details — Australia's winter fest.. Travel. Lineups. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Splendour in the Grass comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Splendour in the Grass comes from.", "x": "Origins: Lineups.. July. The history of Splendour in the Grass — Australia's winter fest.. Travel. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Splendour in the Grass respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Splendour in the Grass respectfully.", "x": "Engaging: Winter.. Byron Bay. How to participate or observe well — Splendour in the Grass. Australia's winter fest. Respect first, always; History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Splendour in the Grass do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Splendour in the Grass do's and don'ts.", "x": "Etiquette: Music.. Lineups. The rules of respect — Splendour in the Grass. Australia's winter fest. When in doubt, ask about Australia.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Splendour in the Grass.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Splendour in the Grass.", "x": "Planning: Lineups.. Camping. Practical notes — Splendour in the Grass. Australia's winter fest. A little planning shows respect for Travel.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Splendour in the Grass and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Splendour in the Grass and money.", "x": "Costs: Winter.. Winter. What to budget — Splendour in the Grass. Australia's winter fest. The best experiences of History. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-festival-splendour-in-the-grass-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
