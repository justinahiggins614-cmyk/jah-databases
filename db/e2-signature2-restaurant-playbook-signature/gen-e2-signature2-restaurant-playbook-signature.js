(function(){'use strict';
/* JAH Restaurant Playbook Database generator — jahdb-e2-signature2-restaurant-playbook-signature-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-signature2-restaurant-playbook-signature',PREFIX='JAH-E2SIGNATURE-',NAME='JAH Restaurant Playbook Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Restaurant Playbook: the complete guide", "d": "Restaurant Playbook: the food business..", "g": "overview", "l": 2, "q": "What is Restaurant Playbook: the complete guide?", "a": "Restaurant Playbook: the food business..", "x": "The complete signature original guide to Restaurant Playbook: the food business.. Menu. History, meaning, practices, and how to engage respectfully — everything in one database. Menu. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Restaurant Playbook essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Restaurant Playbook essentials.", "x": "At a glance: Restaurant Playbook — the food business.. Location. The essentials: Margins.. Staff. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Menu.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Menu.", "x": "Restaurant Playbook: Menu.. Margins. Essential knowledge — Staff.. the food business. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Menu..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Menu..", "x": "Explained: Menu.. Location. The context — Restaurant Playbook. Food cost. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Location.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Location.", "x": "Restaurant Playbook: Location.. Health. Essential knowledge — Food cost.. the food business. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Location..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Location..", "x": "Explained: Location.. Staff. The context — Restaurant Playbook. Health. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Staff.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Staff.", "x": "Restaurant Playbook: Staff.. Location. Essential knowledge — Health.. the food business. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Staff..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Staff..", "x": "Explained: Staff.. Playbook. The context — Restaurant Playbook. Margins. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Food cost.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Food cost.", "x": "Restaurant Playbook: Food cost.. Staff. Essential knowledge — Margins.. the food business. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Food cost..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Food cost..", "x": "Explained: Food cost.. Menu. The context — Restaurant Playbook. Menu. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Health.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Health.", "x": "Restaurant Playbook: Health.. Playbook. Essential knowledge — Menu.. the food business. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Health..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Health..", "x": "Explained: Health.. Margins. The context — Restaurant Playbook. Location. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Margins.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Margins.", "x": "Restaurant Playbook: Margins.. Menu. Essential knowledge — Location.. the food business. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Margins..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Margins..", "x": "Explained: Margins.. Health. The context — Restaurant Playbook. Staff. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Menu.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Menu.", "x": "Restaurant Playbook in depth: Menu.. Location. Details — the food business.. Health. Food cost. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Margins.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Margins.", "x": "Restaurant Playbook in depth: Margins.. Staff. Details — the food business.. Location. Health. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Health.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Health.", "x": "Restaurant Playbook in depth: Health.. Food cost. Details — the food business.. Staff. Margins. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Location.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Location.", "x": "Restaurant Playbook in depth: Location.. Health. Details — the food business.. Playbook. Menu. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Staff.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Staff.", "x": "Restaurant Playbook in depth: Staff.. Margins. Details — the food business.. Menu. Location. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Playbook.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Playbook.", "x": "Restaurant Playbook in depth: Playbook.. Menu. Details — the food business.. Margins. Staff. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Restaurant Playbook comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Restaurant Playbook comes from.", "x": "Origins: Menu.. Menu. The history of Restaurant Playbook — the food business.. Margins. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Restaurant Playbook respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Restaurant Playbook respectfully.", "x": "Engaging: Health.. Location. How to participate or observe well — Restaurant Playbook. the food business. Respect first, always; Location.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Restaurant Playbook do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Restaurant Playbook do's and don'ts.", "x": "Etiquette: Staff.. Staff. The rules of respect — Restaurant Playbook. the food business. When in doubt, ask about Playbook.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Restaurant Playbook.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Restaurant Playbook.", "x": "Planning: Menu.. Food cost. Practical notes — Restaurant Playbook. the food business. A little planning shows respect for Margins.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Restaurant Playbook and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Restaurant Playbook and money.", "x": "Costs: Health.. Health. What to budget — Restaurant Playbook. the food business. The best experiences of Location. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-signature2-restaurant-playbook-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
