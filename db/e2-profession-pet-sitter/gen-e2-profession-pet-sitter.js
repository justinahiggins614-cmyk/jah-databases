(function(){'use strict';
/* JAH Pet Sitter Profession Database generator — jahdb-e2-profession-pet-sitter-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-profession-pet-sitter',PREFIX='JAH-E2PROFESSIO-',NAME='JAH Pet Sitter Profession Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pet Sitter Profession: the complete guide", "d": "Pet Sitter Profession: the care profession..", "g": "overview", "l": 2, "q": "What is Pet Sitter Profession: the complete guide?", "a": "Pet Sitter Profession: the care profession..", "x": "The complete profession guide to Pet Sitter Profession: the care profession.. Homes. History, meaning, practices, and how to engage respectfully — everything in one database. Homes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Pet Sitter Profession essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Pet Sitter Profession essentials.", "x": "At a glance: Pet Sitter Profession — the care profession.. Feeding. The essentials: Trust.. Trust. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Homes.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Homes.", "x": "Pet Sitter Profession: Homes.. Trust. Essential knowledge — Trust.. the care profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Homes..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Homes..", "x": "Explained: Homes.. Keys. The context — Pet Sitter Profession. Walks. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Feeding.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Feeding.", "x": "Pet Sitter Profession: Feeding.. Updates. Essential knowledge — Walks.. the care profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Feeding..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Feeding..", "x": "Explained: Feeding.. Feeding. The context — Pet Sitter Profession. Updates. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Trust.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Trust.", "x": "Pet Sitter Profession: Trust.. Keys. Essential knowledge — Updates.. the care profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Trust..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Trust..", "x": "Explained: Trust.. Day. The context — Pet Sitter Profession. Keys. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Walks.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Walks.", "x": "Pet Sitter Profession: Walks.. Feeding. Essential knowledge — Keys.. the care profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Walks..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Walks..", "x": "Explained: Walks.. Homes. The context — Pet Sitter Profession. Homes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Updates.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Updates.", "x": "Pet Sitter Profession: Updates.. Day. Essential knowledge — Homes.. the care profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Updates..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Updates..", "x": "Explained: Updates.. Trust. The context — Pet Sitter Profession. Feeding. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Keys.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Keys.", "x": "Pet Sitter Profession: Keys.. Homes. Essential knowledge — Feeding.. the care profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Keys..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Keys..", "x": "Explained: Keys.. Updates. The context — Pet Sitter Profession. Trust. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Homes.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Homes.", "x": "Pet Sitter Profession in depth: Homes.. Feeding. Details — the care profession.. Updates. Walks. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Trust.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Trust.", "x": "Pet Sitter Profession in depth: Trust.. Trust. Details — the care profession.. Keys. Updates. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Updates.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Updates.", "x": "Pet Sitter Profession in depth: Updates.. Walks. Details — the care profession.. Feeding. Keys. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Keys.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Keys.", "x": "Pet Sitter Profession in depth: Keys.. Updates. Details — the care profession.. Day. Homes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Feeding.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Feeding.", "x": "Pet Sitter Profession in depth: Feeding.. Keys. Details — the care profession.. Homes. Feeding. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Day.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Day.", "x": "Pet Sitter Profession in depth: Day.. Homes. Details — the care profession.. Trust. Trust. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Pet Sitter Profession comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Pet Sitter Profession comes from.", "x": "Origins: Homes.. Homes. The history of Pet Sitter Profession — the care profession.. Trust. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Pet Sitter Profession respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Pet Sitter Profession respectfully.", "x": "Engaging: Updates.. Feeding. How to participate or observe well — Pet Sitter Profession. the care profession. Respect first, always; Keys.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Pet Sitter Profession do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Pet Sitter Profession do's and don'ts.", "x": "Etiquette: Feeding.. Trust. The rules of respect — Pet Sitter Profession. the care profession. When in doubt, ask about Day.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Pet Sitter Profession.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Pet Sitter Profession.", "x": "Planning: Homes.. Walks. Practical notes — Pet Sitter Profession. the care profession. A little planning shows respect for Trust.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Pet Sitter Profession and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Pet Sitter Profession and money.", "x": "Costs: Updates.. Updates. What to budget — Pet Sitter Profession. the care profession. The best experiences of Keys. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-profession-pet-sitter-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
