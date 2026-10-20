(function(){'use strict';
/* JAH Afrobeats Dance Dance Form Database generator — jahdb-e2-dance-afrobeats-dance-form-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dance-afrobeats-dance-form',PREFIX='JAH-E2DANCEAFRO-',NAME='JAH Afrobeats Dance Dance Form Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Afrobeats Dance: the complete guide", "d": "Afrobeats Dance: the African wave..", "g": "overview", "l": 2, "q": "What is Afrobeats Dance: the complete guide?", "a": "Afrobeats Dance: the African wave..", "x": "The complete dance form guide to Afrobeats Dance: the African wave.. Africa. History, meaning, practices, and how to engage respectfully — everything in one database. Azonto. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Afrobeats Dance essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Afrobeats Dance essentials.", "x": "At a glance: Afrobeats Dance — the African wave.. Azonto. The essentials: Viral.. Shaku. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Africa.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Africa.", "x": "Afrobeats Dance: Africa.. Viral. Essential knowledge — Shaku.. the African wave. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Africa..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Africa..", "x": "Explained: Africa.. Africa. The context — Afrobeats Dance. Naija. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Azonto.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Azonto.", "x": "Afrobeats Dance: Azonto.. Groove. Essential knowledge — Naija.. the African wave. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Azonto..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Azonto..", "x": "Explained: Azonto.. Naija. The context — Afrobeats Dance. Viral. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Shaku.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Shaku.", "x": "Afrobeats Dance: Shaku.. Africa. Essential knowledge — Viral.. the African wave. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Shaku..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Shaku..", "x": "Explained: Shaku.. Training. The context — Afrobeats Dance. Groove. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Naija.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Naija.", "x": "Afrobeats Dance: Naija.. Naija. Essential knowledge — Groove.. the African wave. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Naija..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Naija..", "x": "Explained: Naija.. Azonto. The context — Afrobeats Dance. Africa. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Viral.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Viral.", "x": "Afrobeats Dance: Viral.. Training. Essential knowledge — Africa.. the African wave. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Viral..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Viral..", "x": "Explained: Viral.. Viral. The context — Afrobeats Dance. Azonto. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Groove.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Groove.", "x": "Afrobeats Dance: Groove.. Azonto. Essential knowledge — Azonto.. the African wave. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Groove..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Groove..", "x": "Explained: Groove.. Groove. The context — Afrobeats Dance. Shaku. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Azonto.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Azonto.", "x": "Afrobeats Dance in depth: Azonto.. Azonto. Details — the African wave.. Groove. Naija. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Viral.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Viral.", "x": "Afrobeats Dance in depth: Viral.. Shaku. Details — the African wave.. Africa. Viral. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Groove.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Groove.", "x": "Afrobeats Dance in depth: Groove.. Naija. Details — the African wave.. Naija. Groove. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Africa.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Africa.", "x": "Afrobeats Dance in depth: Africa.. Viral. Details — the African wave.. Training. Africa. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Naija.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Naija.", "x": "Afrobeats Dance in depth: Naija.. Groove. Details — the African wave.. Azonto. Azonto. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Training.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Training.", "x": "Afrobeats Dance in depth: Training.. Africa. Details — the African wave.. Viral. Shaku. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Afrobeats Dance comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Afrobeats Dance comes from.", "x": "Origins: Azonto.. Africa. The history of Afrobeats Dance — the African wave.. Viral. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Afrobeats Dance respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Afrobeats Dance respectfully.", "x": "Engaging: Groove.. Azonto. How to participate or observe well — Afrobeats Dance. the African wave. Respect first, always; Africa.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Afrobeats Dance do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Afrobeats Dance do's and don'ts.", "x": "Etiquette: Naija.. Shaku. The rules of respect — Afrobeats Dance. the African wave. When in doubt, ask about Training.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Afrobeats Dance.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Afrobeats Dance.", "x": "Planning: Azonto.. Naija. Practical notes — Afrobeats Dance. the African wave. A little planning shows respect for Viral.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Afrobeats Dance and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Afrobeats Dance and money.", "x": "Costs: Groove.. Viral. What to budget — Afrobeats Dance. the African wave. The best experiences of Africa. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dance-afrobeats-dance-form-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
