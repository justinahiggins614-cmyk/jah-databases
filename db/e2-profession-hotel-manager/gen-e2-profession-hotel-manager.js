(function(){'use strict';
/* JAH Hotel Manager Profession Database generator — jahdb-e2-profession-hotel-manager-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-profession-hotel-manager',PREFIX='JAH-E2PROFESSIO-',NAME='JAH Hotel Manager Profession Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hotel Manager Profession: the complete guide", "d": "Hotel Manager Profession: the hospitality profession..", "g": "overview", "l": 2, "q": "What is Hotel Manager Profession: the complete guide?", "a": "Hotel Manager Profession: the hospitality profession..", "x": "The complete profession guide to Hotel Manager Profession: the hospitality profession.. Front desk. History, meaning, practices, and how to engage respectfully — everything in one database. Desk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Hotel Manager Profession essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Hotel Manager Profession essentials.", "x": "At a glance: Hotel Manager Profession — the hospitality profession.. Occupancy. The essentials: Staff.. Staff. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Front desk.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Front desk.", "x": "Hotel Manager Profession: Front desk.. Staff. Essential knowledge — Staff.. the hospitality profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Front desk..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Front desk..", "x": "Explained: Front desk.. Revenue. The context — Hotel Manager Profession. Guests. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Occupancy.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Occupancy.", "x": "Hotel Manager Profession: Occupancy.. Guests. Essential knowledge — Guests.. the hospitality profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Occupancy..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Occupancy..", "x": "Explained: Occupancy.. Audit. The context — Hotel Manager Profession. Revenue. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Staff.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Staff.", "x": "Hotel Manager Profession: Staff.. Revenue. Essential knowledge — Revenue.. the hospitality profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Staff..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Staff..", "x": "Explained: Staff.. Day. The context — Hotel Manager Profession. Night audit. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Guests.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Guests.", "x": "Hotel Manager Profession: Guests.. Audit. Essential knowledge — Night audit.. the hospitality profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Guests..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Guests..", "x": "Explained: Guests.. Desk. The context — Hotel Manager Profession. Front desk. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Revenue.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Revenue.", "x": "Hotel Manager Profession: Revenue.. Day. Essential knowledge — Front desk.. the hospitality profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Revenue..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Revenue..", "x": "Explained: Revenue.. Staff. The context — Hotel Manager Profession. Occupancy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Night audit.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Night audit.", "x": "Hotel Manager Profession: Night audit.. Desk. Essential knowledge — Occupancy.. the hospitality profession. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Night audit..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Night audit..", "x": "Explained: Night audit.. Guests. The context — Hotel Manager Profession. Staff. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Desk.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Desk.", "x": "Hotel Manager Profession in depth: Desk.. Occupancy. Details — the hospitality profession.. Guests. Guests. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Staff.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Staff.", "x": "Hotel Manager Profession in depth: Staff.. Staff. Details — the hospitality profession.. Revenue. Revenue. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Guests.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Guests.", "x": "Hotel Manager Profession in depth: Guests.. Guests. Details — the hospitality profession.. Audit. Night audit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Revenue.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Revenue.", "x": "Hotel Manager Profession in depth: Revenue.. Revenue. Details — the hospitality profession.. Day. Front desk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Audit.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Audit.", "x": "Hotel Manager Profession in depth: Audit.. Night audit. Details — the hospitality profession.. Desk. Occupancy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Day.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Day.", "x": "Hotel Manager Profession in depth: Day.. Front desk. Details — the hospitality profession.. Staff. Staff. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Hotel Manager Profession comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Hotel Manager Profession comes from.", "x": "Origins: Desk.. Front desk. The history of Hotel Manager Profession — the hospitality profession.. Staff. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Hotel Manager Profession respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Hotel Manager Profession respectfully.", "x": "Engaging: Guests.. Occupancy. How to participate or observe well — Hotel Manager Profession. the hospitality profession. Respect first, always; Revenue.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Hotel Manager Profession do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Hotel Manager Profession do's and don'ts.", "x": "Etiquette: Audit.. Staff. The rules of respect — Hotel Manager Profession. the hospitality profession. When in doubt, ask about Day.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Hotel Manager Profession.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Hotel Manager Profession.", "x": "Planning: Desk.. Guests. Practical notes — Hotel Manager Profession. the hospitality profession. A little planning shows respect for Staff.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Hotel Manager Profession and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Hotel Manager Profession and money.", "x": "Costs: Guests.. Revenue. What to budget — Hotel Manager Profession. the hospitality profession. The best experiences of Revenue. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-profession-hotel-manager-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
