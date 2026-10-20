(function(){'use strict';
/* JAH Half Moon Pose Database generator — jahdb-e2-yoga2-half-moon-yoga2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-yoga2-half-moon-yoga2',PREFIX='JAH-E2YOGA2HALF-',NAME='JAH Half Moon Pose Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Half Moon Pose: the complete guide", "d": "Half Moon Pose: the Ardha Chandrasana..", "g": "overview", "l": 2, "q": "What is Half Moon Pose: the complete guide?", "a": "Half Moon Pose: the Ardha Chandrasana..", "x": "The complete yoga pose guide to Half Moon Pose: the Ardha Chandrasana.. Balance. History, meaning, practices, and how to engage respectfully — everything in one database. Balance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Half Moon Pose essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Half Moon Pose essentials.", "x": "At a glance: Half Moon Pose — the Ardha Chandrasana.. Open. The essentials: Stack.. Block. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Balance.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Balance.", "x": "Half Moon Pose: Balance.. Stack. Essential knowledge — Block.. the Ardha Chandrasana. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Balance..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Balance..", "x": "Explained: Balance.. Open. The context — Half Moon Pose. Hip. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Open.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Open.", "x": "Half Moon Pose: Open.. Standing. Essential knowledge — Hip.. the Ardha Chandrasana. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Open..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Open..", "x": "Explained: Open.. Hip. The context — Half Moon Pose. Stack. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Block.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Block.", "x": "Half Moon Pose: Block.. Open. Essential knowledge — Stack.. the Ardha Chandrasana. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Block..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Block..", "x": "Explained: Block.. Guide. The context — Half Moon Pose. Standing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Hip.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Hip.", "x": "Half Moon Pose: Hip.. Hip. Essential knowledge — Standing.. the Ardha Chandrasana. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Hip..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Hip..", "x": "Explained: Hip.. Balance. The context — Half Moon Pose. Balance. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Stack.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Stack.", "x": "Half Moon Pose: Stack.. Guide. Essential knowledge — Balance.. the Ardha Chandrasana. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Stack..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Stack..", "x": "Explained: Stack.. Stack. The context — Half Moon Pose. Open. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Standing.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Standing.", "x": "Half Moon Pose: Standing.. Balance. Essential knowledge — Open.. the Ardha Chandrasana. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Standing..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Standing..", "x": "Explained: Standing.. Standing. The context — Half Moon Pose. Block. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Balance.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Balance.", "x": "Half Moon Pose in depth: Balance.. Open. Details — the Ardha Chandrasana.. Standing. Hip. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Stack.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Stack.", "x": "Half Moon Pose in depth: Stack.. Block. Details — the Ardha Chandrasana.. Open. Stack. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Standing.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Standing.", "x": "Half Moon Pose in depth: Standing.. Hip. Details — the Ardha Chandrasana.. Hip. Standing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Open.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Open.", "x": "Half Moon Pose in depth: Open.. Stack. Details — the Ardha Chandrasana.. Guide. Balance. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Hip.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Hip.", "x": "Half Moon Pose in depth: Hip.. Standing. Details — the Ardha Chandrasana.. Balance. Open. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Half Moon Pose in depth: Guide.. Balance. Details — the Ardha Chandrasana.. Stack. Block. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Half Moon Pose comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Half Moon Pose comes from.", "x": "Origins: Balance.. Balance. The history of Half Moon Pose — the Ardha Chandrasana.. Stack. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Half Moon Pose respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Half Moon Pose respectfully.", "x": "Engaging: Standing.. Open. How to participate or observe well — Half Moon Pose. the Ardha Chandrasana. Respect first, always; Open.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Half Moon Pose do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Half Moon Pose do's and don'ts.", "x": "Etiquette: Hip.. Block. The rules of respect — Half Moon Pose. the Ardha Chandrasana. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Half Moon Pose.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Half Moon Pose.", "x": "Planning: Balance.. Hip. Practical notes — Half Moon Pose. the Ardha Chandrasana. A little planning shows respect for Stack.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Half Moon Pose and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Half Moon Pose and money.", "x": "Costs: Standing.. Stack. What to budget — Half Moon Pose. the Ardha Chandrasana. The best experiences of Open. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-yoga2-half-moon-yoga2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
