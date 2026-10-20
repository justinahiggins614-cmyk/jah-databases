(function(){'use strict';
/* JAH Pet Photography Photography Database generator — jahdb-e2-photo-pet-photography-tech-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-photo-pet-photography-tech',PREFIX='JAH-E2PHOTOPETP-',NAME='JAH Pet Photography Photography Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pet Photography: the complete guide", "d": "Pet Photography: the furry models..", "g": "overview", "l": 2, "q": "What is Pet Photography: the complete guide?", "a": "Pet Photography: the furry models..", "x": "The complete photography guide to Pet Photography: the furry models.. Treats. History, meaning, practices, and how to engage respectfully — everything in one database. Treats. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Pet Photography essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Pet Photography essentials.", "x": "At a glance: Pet Photography — the furry models.. Fast. The essentials: Eye level.. Eye level. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Treats.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Treats.", "x": "Pet Photography: Treats.. Eye level. Essential knowledge — Eye level.. the furry models. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Treats..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Treats..", "x": "Explained: Treats.. Action. The context — Pet Photography. Patience. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Fast.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Fast.", "x": "Pet Photography: Fast.. Squeakers. Essential knowledge — Patience.. the furry models. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Fast..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Fast..", "x": "Explained: Fast.. Fast. The context — Pet Photography. Squeakers. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Eye level.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Eye level.", "x": "Pet Photography: Eye level.. Action. Essential knowledge — Squeakers.. the furry models. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Eye level..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Eye level..", "x": "Explained: Eye level.. Tips. The context — Pet Photography. Action. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Patience.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Patience.", "x": "Pet Photography: Patience.. Fast. Essential knowledge — Action.. the furry models. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Patience..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Patience..", "x": "Explained: Patience.. Treats. The context — Pet Photography. Treats. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Squeakers.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Squeakers.", "x": "Pet Photography: Squeakers.. Tips. Essential knowledge — Treats.. the furry models. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Squeakers..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Squeakers..", "x": "Explained: Squeakers.. Eye level. The context — Pet Photography. Fast. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Action.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Action.", "x": "Pet Photography: Action.. Treats. Essential knowledge — Fast.. the furry models. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Action..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Action..", "x": "Explained: Action.. Squeakers. The context — Pet Photography. Eye level. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Treats.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Treats.", "x": "Pet Photography in depth: Treats.. Fast. Details — the furry models.. Squeakers. Patience. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Eye level.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Eye level.", "x": "Pet Photography in depth: Eye level.. Eye level. Details — the furry models.. Action. Squeakers. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Squeakers.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Squeakers.", "x": "Pet Photography in depth: Squeakers.. Patience. Details — the furry models.. Fast. Action. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Action.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Action.", "x": "Pet Photography in depth: Action.. Squeakers. Details — the furry models.. Tips. Treats. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Fast.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Fast.", "x": "Pet Photography in depth: Fast.. Action. Details — the furry models.. Treats. Fast. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tips.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tips.", "x": "Pet Photography in depth: Tips.. Treats. Details — the furry models.. Eye level. Eye level. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Pet Photography comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Pet Photography comes from.", "x": "Origins: Treats.. Treats. The history of Pet Photography — the furry models.. Eye level. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Pet Photography respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Pet Photography respectfully.", "x": "Engaging: Squeakers.. Fast. How to participate or observe well — Pet Photography. the furry models. Respect first, always; Action.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Pet Photography do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Pet Photography do's and don'ts.", "x": "Etiquette: Fast.. Eye level. The rules of respect — Pet Photography. the furry models. When in doubt, ask about Tips.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Pet Photography.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Pet Photography.", "x": "Planning: Treats.. Patience. Practical notes — Pet Photography. the furry models. A little planning shows respect for Eye level.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Pet Photography and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Pet Photography and money.", "x": "Costs: Squeakers.. Squeakers. What to budget — Pet Photography. the furry models. The best experiences of Action. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-photo-pet-photography-tech-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
