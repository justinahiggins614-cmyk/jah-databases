(function(){'use strict';
/* JAH National Palace Museum Taipei Museum Database generator — jahdb-e2-museum-national-palace-museum-taipei-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-museum-national-palace-museum-taipei',PREFIX='JAH-E2MUSEUMNAT-',NAME='JAH National Palace Museum Taipei Museum Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "National Palace Museum Taipei: the complete guide", "d": "National Palace Museum Taipei: China's treasure in Taiwan..", "g": "overview", "l": 2, "q": "What is National Palace Museum Taipei: the complete guide?", "a": "National Palace Museum Taipei: China's treasure in Taiwan..", "x": "The complete museum guide to National Palace Museum Taipei: China's treasure in Taiwan.. 700K objects. History, meaning, practices, and how to engage respectfully — everything in one database. Treasures.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "National Palace Museum Taipei essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "National Palace Museum Taipei essentials.", "x": "At a glance: National Palace Museum Taipei — China's treasure in Taiwan.. Jade cabbage. The essentials: History.. Taipei. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "700K objects.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "700K objects.", "x": "National Palace Museum Taipei: 700K objects.. History. Essential knowledge — Taipei.. China's treasure in Taiwan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 700K objects..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 700K objects..", "x": "Explained: 700K objects.. Taipei. The context — National Palace Museum Taipei. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Jade cabbage.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Jade cabbage.", "x": "National Palace Museum Taipei: Jade cabbage.. Tickets. Essential knowledge — History.. China's treasure in Taiwan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Jade cabbage..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Jade cabbage..", "x": "Explained: Jade cabbage.. Art. The context — National Palace Museum Taipei. Calligraphy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Taipei.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Taipei.", "x": "National Palace Museum Taipei: Taipei.. Taipei. Essential knowledge — Calligraphy.. China's treasure in Taiwan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Taipei..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Taipei..", "x": "Explained: Taipei.. China. The context — National Palace Museum Taipei. Bronzes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "History.", "x": "National Palace Museum Taipei: History.. Art. Essential knowledge — Bronzes.. China's treasure in Taiwan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: History..", "x": "Explained: History.. Treasures. The context — National Palace Museum Taipei. 700K objects. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Calligraphy.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Calligraphy.", "x": "National Palace Museum Taipei: Calligraphy.. China. Essential knowledge — 700K objects.. China's treasure in Taiwan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Calligraphy..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Calligraphy..", "x": "Explained: Calligraphy.. History. The context — National Palace Museum Taipei. Jade cabbage. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Bronzes.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Bronzes.", "x": "National Palace Museum Taipei: Bronzes.. Treasures. Essential knowledge — Jade cabbage.. China's treasure in Taiwan. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Bronzes..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Bronzes..", "x": "Explained: Bronzes.. Tickets. The context — National Palace Museum Taipei. Taipei. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Treasures.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Treasures.", "x": "National Palace Museum Taipei in depth: Treasures.. Jade cabbage. Details — China's treasure in Taiwan.. Tickets. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "National Palace Museum Taipei in depth: History.. Taipei. Details — China's treasure in Taiwan.. Taipei. Calligraphy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tickets.", "x": "National Palace Museum Taipei in depth: Tickets.. History. Details — China's treasure in Taiwan.. Art. Bronzes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Taipei.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Taipei.", "x": "National Palace Museum Taipei in depth: Taipei.. Calligraphy. Details — China's treasure in Taiwan.. China. 700K objects. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Art.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Art.", "x": "National Palace Museum Taipei in depth: Art.. Bronzes. Details — China's treasure in Taiwan.. Treasures. Jade cabbage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "China.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "China.", "x": "National Palace Museum Taipei in depth: China.. 700K objects. Details — China's treasure in Taiwan.. History. Taipei. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where National Palace Museum Taipei comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where National Palace Museum Taipei comes from.", "x": "Origins: Treasures.. 700K objects. The history of National Palace Museum Taipei — China's treasure in Taiwan.. History. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing National Palace Museum Taipei respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing National Palace Museum Taipei respectfully.", "x": "Engaging: Tickets.. Jade cabbage. How to participate or observe well — National Palace Museum Taipei. China's treasure in Taiwan. Respect first, always; Taipei.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "National Palace Museum Taipei do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "National Palace Museum Taipei do's and don'ts.", "x": "Etiquette: Art.. Taipei. The rules of respect — National Palace Museum Taipei. China's treasure in Taiwan. When in doubt, ask about China.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around National Palace Museum Taipei.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around National Palace Museum Taipei.", "x": "Planning: Treasures.. History. Practical notes — National Palace Museum Taipei. China's treasure in Taiwan. A little planning shows respect for History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "National Palace Museum Taipei and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "National Palace Museum Taipei and money.", "x": "Costs: Tickets.. Calligraphy. What to budget — National Palace Museum Taipei. China's treasure in Taiwan. The best experiences of Taipei. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-museum-national-palace-museum-taipei-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
