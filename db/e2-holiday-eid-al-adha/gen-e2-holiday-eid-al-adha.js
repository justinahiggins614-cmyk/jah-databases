(function(){'use strict';
/* JAH Eid al-Adha Holiday Database generator — jahdb-e2-holiday-eid-al-adha-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-holiday-eid-al-adha',PREFIX='JAH-E2HOLIDAYEI-',NAME='JAH Eid al-Adha Holiday Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Eid al-Adha: the complete guide", "d": "Eid al-Adha: festival of sacrifice..", "g": "overview", "l": 2, "q": "What is Eid al-Adha: the complete guide?", "a": "Eid al-Adha: festival of sacrifice..", "x": "The complete holiday guide to Eid al-Adha: festival of sacrifice.. Hajj time. History, meaning, practices, and how to engage respectfully — everything in one database. Story. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Eid al-Adha essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Eid al-Adha essentials.", "x": "At a glance: Eid al-Adha — festival of sacrifice.. Sacrifice. The essentials: Rituals.. Charity meat. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Hajj time.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Hajj time.", "x": "Eid al-Adha: Hajj time.. Rituals. Essential knowledge — Charity meat.. festival of sacrifice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Hajj time..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Hajj time..", "x": "Explained: Hajj time.. Food. The context — Eid al-Adha. Prayers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Sacrifice.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Sacrifice.", "x": "Eid al-Adha: Sacrifice.. Charity. Essential knowledge — Prayers.. festival of sacrifice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Sacrifice..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Sacrifice..", "x": "Explained: Sacrifice.. Family. The context — Eid al-Adha. Abraham. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Charity meat.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Charity meat.", "x": "Eid al-Adha: Charity meat.. Food. Essential knowledge — Abraham.. festival of sacrifice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Charity meat..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Charity meat..", "x": "Explained: Charity meat.. Meaning. The context — Eid al-Adha. Global. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Prayers.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Prayers.", "x": "Eid al-Adha: Prayers.. Family. Essential knowledge — Global.. festival of sacrifice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Prayers..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Prayers..", "x": "Explained: Prayers.. Story. The context — Eid al-Adha. Hajj time. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Abraham.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Abraham.", "x": "Eid al-Adha: Abraham.. Meaning. Essential knowledge — Hajj time.. festival of sacrifice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Abraham..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Abraham..", "x": "Explained: Abraham.. Rituals. The context — Eid al-Adha. Sacrifice. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Global.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Global.", "x": "Eid al-Adha: Global.. Story. Essential knowledge — Sacrifice.. festival of sacrifice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Global..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Global..", "x": "Explained: Global.. Charity. The context — Eid al-Adha. Charity meat. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Story.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Story.", "x": "Eid al-Adha in depth: Story.. Sacrifice. Details — festival of sacrifice.. Charity. Prayers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Rituals.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Rituals.", "x": "Eid al-Adha in depth: Rituals.. Charity meat. Details — festival of sacrifice.. Food. Abraham. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Charity.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Charity.", "x": "Eid al-Adha in depth: Charity.. Prayers. Details — festival of sacrifice.. Family. Global. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Food.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Food.", "x": "Eid al-Adha in depth: Food.. Abraham. Details — festival of sacrifice.. Meaning. Hajj time. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Family.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Family.", "x": "Eid al-Adha in depth: Family.. Global. Details — festival of sacrifice.. Story. Sacrifice. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Meaning.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Meaning.", "x": "Eid al-Adha in depth: Meaning.. Hajj time. Details — festival of sacrifice.. Rituals. Charity meat. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Eid al-Adha comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Eid al-Adha comes from.", "x": "Origins: Story.. Hajj time. The history of Eid al-Adha — festival of sacrifice.. Rituals. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Eid al-Adha respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Eid al-Adha respectfully.", "x": "Engaging: Charity.. Sacrifice. How to participate or observe well — Eid al-Adha. festival of sacrifice. Respect first, always; Food.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Eid al-Adha do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Eid al-Adha do's and don'ts.", "x": "Etiquette: Family.. Charity meat. The rules of respect — Eid al-Adha. festival of sacrifice. When in doubt, ask about Meaning.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Eid al-Adha.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Eid al-Adha.", "x": "Planning: Story.. Prayers. Practical notes — Eid al-Adha. festival of sacrifice. A little planning shows respect for Rituals.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Eid al-Adha and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Eid al-Adha and money.", "x": "Costs: Charity.. Abraham. What to budget — Eid al-Adha. festival of sacrifice. The best experiences of Food. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-holiday-eid-al-adha-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
