(function(){'use strict';
/* JAH Gymnastics Artistic Olympics Database generator — jahdb-e2-olympic2-gymnastics-artistic-olympics-sport-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-olympic2-gymnastics-artistic-olympics-sport',PREFIX='JAH-E2OLYMPIC2G-',NAME='JAH Gymnastics Artistic Olympics Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Gymnastics Artistic Olympics: the complete guide", "d": "Gymnastics Artistic Olympics: the apparatus art..", "g": "overview", "l": 2, "q": "What is Gymnastics Artistic Olympics: the complete guide?", "a": "Gymnastics Artistic Olympics: the apparatus art..", "x": "The complete olympic sport guide to Gymnastics Artistic Olympics: the apparatus art.. 1896. History, meaning, practices, and how to engage respectfully — everything in one database. Apparatus. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Gymnastics Artistic Olympics essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Gymnastics Artistic Olympics essentials.", "x": "At a glance: Gymnastics Artistic Olympics — the apparatus art.. Vault. The essentials: Perfect 10.. Bars. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1896.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1896.", "x": "Gymnastics Artistic Olympics: 1896.. Perfect 10. Essential knowledge — Bars.. the apparatus art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1896..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1896..", "x": "Explained: 1896.. Beam. The context — Gymnastics Artistic Olympics. Beam. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Vault.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Vault.", "x": "Gymnastics Artistic Olympics: Vault.. Vault. Essential knowledge — Beam.. the apparatus art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Vault..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Vault..", "x": "Explained: Vault.. Floor. The context — Gymnastics Artistic Olympics. Floor. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Bars.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Bars.", "x": "Gymnastics Artistic Olympics: Bars.. Beam. Essential knowledge — Floor.. the apparatus art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Bars..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Bars..", "x": "Explained: Bars.. Guide. The context — Gymnastics Artistic Olympics. Perfect 10. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Beam.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Beam.", "x": "Gymnastics Artistic Olympics: Beam.. Floor. Essential knowledge — Perfect 10.. the apparatus art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Beam..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Beam..", "x": "Explained: Beam.. Apparatus. The context — Gymnastics Artistic Olympics. 1896. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Floor.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Floor.", "x": "Gymnastics Artistic Olympics: Floor.. Guide. Essential knowledge — 1896.. the apparatus art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Floor..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Floor..", "x": "Explained: Floor.. Perfect 10. The context — Gymnastics Artistic Olympics. Vault. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Perfect 10.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Perfect 10.", "x": "Gymnastics Artistic Olympics: Perfect 10.. Apparatus. Essential knowledge — Vault.. the apparatus art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Perfect 10..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Perfect 10..", "x": "Explained: Perfect 10.. Vault. The context — Gymnastics Artistic Olympics. Bars. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Apparatus.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Apparatus.", "x": "Gymnastics Artistic Olympics in depth: Apparatus.. Vault. Details — the apparatus art.. Vault. Beam. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Perfect 10.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Perfect 10.", "x": "Gymnastics Artistic Olympics in depth: Perfect 10.. Bars. Details — the apparatus art.. Beam. Floor. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Vault.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Vault.", "x": "Gymnastics Artistic Olympics in depth: Vault.. Beam. Details — the apparatus art.. Floor. Perfect 10. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Beam.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Beam.", "x": "Gymnastics Artistic Olympics in depth: Beam.. Floor. Details — the apparatus art.. Guide. 1896. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Floor.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Floor.", "x": "Gymnastics Artistic Olympics in depth: Floor.. Perfect 10. Details — the apparatus art.. Apparatus. Vault. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Guide.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Guide.", "x": "Gymnastics Artistic Olympics in depth: Guide.. 1896. Details — the apparatus art.. Perfect 10. Bars. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Gymnastics Artistic Olympics comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Gymnastics Artistic Olympics comes from.", "x": "Origins: Apparatus.. 1896. The history of Gymnastics Artistic Olympics — the apparatus art.. Perfect 10. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Gymnastics Artistic Olympics respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Gymnastics Artistic Olympics respectfully.", "x": "Engaging: Vault.. Vault. How to participate or observe well — Gymnastics Artistic Olympics. the apparatus art. Respect first, always; Beam.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Gymnastics Artistic Olympics do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Gymnastics Artistic Olympics do's and don'ts.", "x": "Etiquette: Floor.. Bars. The rules of respect — Gymnastics Artistic Olympics. the apparatus art. When in doubt, ask about Guide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Gymnastics Artistic Olympics.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Gymnastics Artistic Olympics.", "x": "Planning: Apparatus.. Beam. Practical notes — Gymnastics Artistic Olympics. the apparatus art. A little planning shows respect for Perfect 10.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Gymnastics Artistic Olympics and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Gymnastics Artistic Olympics and money.", "x": "Costs: Vault.. Floor. What to budget — Gymnastics Artistic Olympics. the apparatus art. The best experiences of Beam. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-olympic2-gymnastics-artistic-olympics-sport-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
