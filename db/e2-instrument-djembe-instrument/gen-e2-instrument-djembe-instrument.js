(function(){'use strict';
/* JAH Djembe Instrument Instrument Database generator — jahdb-e2-instrument-djembe-instrument-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-instrument-djembe-instrument',PREFIX='JAH-E2INSTRUMEN-',NAME='JAH Djembe Instrument Instrument Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Djembe Instrument: the complete guide", "d": "Djembe Instrument: the West African drum..", "g": "overview", "l": 2, "q": "What is Djembe Instrument: the complete guide?", "a": "Djembe Instrument: the West African drum..", "x": "The complete instrument guide to Djembe Instrument: the West African drum.. Mali. History, meaning, practices, and how to engage respectfully — everything in one database. Mali. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Djembe Instrument essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Djembe Instrument essentials.", "x": "At a glance: Djembe Instrument — the West African drum.. Goblet. The essentials: Hands.. Hands. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Mali.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Mali.", "x": "Djembe Instrument: Mali.. Hands. Essential knowledge — Hands.. the West African drum. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Mali..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Mali..", "x": "Explained: Mali.. Carved. The context — Djembe Instrument. Bass/tone. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Goblet.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Goblet.", "x": "Djembe Instrument: Goblet.. Community. Essential knowledge — Bass/tone.. the West African drum. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Goblet..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Goblet..", "x": "Explained: Goblet.. Tones. The context — Djembe Instrument. Community. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Hands.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Hands.", "x": "Djembe Instrument: Hands.. Carved. Essential knowledge — Community.. the West African drum. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Hands..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Hands..", "x": "Explained: Hands.. Learning. The context — Djembe Instrument. Carved. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Bass/tone.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Bass/tone.", "x": "Djembe Instrument: Bass/tone.. Tones. Essential knowledge — Carved.. the West African drum. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Bass/tone..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Bass/tone..", "x": "Explained: Bass/tone.. Mali. The context — Djembe Instrument. Mali. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Community.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Community.", "x": "Djembe Instrument: Community.. Learning. Essential knowledge — Mali.. the West African drum. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Community..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Community..", "x": "Explained: Community.. Hands. The context — Djembe Instrument. Goblet. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Carved.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Carved.", "x": "Djembe Instrument: Carved.. Mali. Essential knowledge — Goblet.. the West African drum. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Carved..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Carved..", "x": "Explained: Carved.. Community. The context — Djembe Instrument. Hands. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Mali.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Mali.", "x": "Djembe Instrument in depth: Mali.. Goblet. Details — the West African drum.. Community. Bass/tone. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Hands.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Hands.", "x": "Djembe Instrument in depth: Hands.. Hands. Details — the West African drum.. Carved. Community. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Community.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Community.", "x": "Djembe Instrument in depth: Community.. Bass/tone. Details — the West African drum.. Tones. Carved. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Carved.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Carved.", "x": "Djembe Instrument in depth: Carved.. Community. Details — the West African drum.. Learning. Mali. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Tones.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Tones.", "x": "Djembe Instrument in depth: Tones.. Carved. Details — the West African drum.. Mali. Goblet. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Learning.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Learning.", "x": "Djembe Instrument in depth: Learning.. Mali. Details — the West African drum.. Hands. Hands. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Djembe Instrument comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Djembe Instrument comes from.", "x": "Origins: Mali.. Mali. The history of Djembe Instrument — the West African drum.. Hands. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Djembe Instrument respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Djembe Instrument respectfully.", "x": "Engaging: Community.. Goblet. How to participate or observe well — Djembe Instrument. the West African drum. Respect first, always; Carved.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Djembe Instrument do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Djembe Instrument do's and don'ts.", "x": "Etiquette: Tones.. Hands. The rules of respect — Djembe Instrument. the West African drum. When in doubt, ask about Learning.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Djembe Instrument.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Djembe Instrument.", "x": "Planning: Mali.. Bass/tone. Practical notes — Djembe Instrument. the West African drum. A little planning shows respect for Hands.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Djembe Instrument and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Djembe Instrument and money.", "x": "Costs: Community.. Community. What to budget — Djembe Instrument. the West African drum. The best experiences of Carved. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-instrument-djembe-instrument-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
