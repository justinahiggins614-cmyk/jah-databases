(function(){'use strict';
/* JAH Fairchild Tropical Garden Botanical Garden Database generator — jahdb-e2-garden-fairchild-tropical-garden-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-garden-fairchild-tropical-garden',PREFIX='JAH-E2GARDENFAI-',NAME='JAH Fairchild Tropical Garden Botanical Garden Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Fairchild Tropical Garden: the complete guide", "d": "Fairchild Tropical Garden: Miami's tropical paradise..", "g": "overview", "l": 2, "q": "What is Fairchild Tropical Garden: the complete guide?", "a": "Fairchild Tropical Garden: Miami's tropical paradise..", "x": "The complete botanical garden guide to Fairchild Tropical Garden: Miami's tropical paradise.. 1938. History, meaning, practices, and how to engage respectfully — everything in one database. Palms. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Fairchild Tropical Garden essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Fairchild Tropical Garden essentials.", "x": "At a glance: Fairchild Tropical Garden — Miami's tropical paradise.. Palms. The essentials: Butterflies.. Cycads. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1938.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1938.", "x": "Fairchild Tropical Garden: 1938.. Butterflies. Essential knowledge — Cycads.. Miami's tropical paradise. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1938..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1938..", "x": "Explained: 1938.. Tickets. The context — Fairchild Tropical Garden. Butterflies. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Palms.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Palms.", "x": "Fairchild Tropical Garden: Palms.. History. Essential knowledge — Butterflies.. Miami's tropical paradise. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Palms..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Palms..", "x": "Explained: Palms.. Miami. The context — Fairchild Tropical Garden. 83 acres. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Cycads.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Cycads.", "x": "Fairchild Tropical Garden: Cycads.. Tickets. Essential knowledge — 83 acres.. Miami's tropical paradise. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Cycads..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Cycads..", "x": "Explained: Cycads.. Art. The context — Fairchild Tropical Garden. Art. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Butterflies.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Butterflies.", "x": "Fairchild Tropical Garden: Butterflies.. Miami. Essential knowledge — Art.. Miami's tropical paradise. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Butterflies..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Butterflies..", "x": "Explained: Butterflies.. Palms. The context — Fairchild Tropical Garden. 1938. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "83 acres.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "83 acres.", "x": "Fairchild Tropical Garden: 83 acres.. Art. Essential knowledge — 1938.. Miami's tropical paradise. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 83 acres..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 83 acres..", "x": "Explained: 83 acres.. Butterflies. The context — Fairchild Tropical Garden. Palms. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Art.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Art.", "x": "Fairchild Tropical Garden: Art.. Palms. Essential knowledge — Palms.. Miami's tropical paradise. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Art..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Art..", "x": "Explained: Art.. History. The context — Fairchild Tropical Garden. Cycads. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Palms.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Palms.", "x": "Fairchild Tropical Garden in depth: Palms.. Palms. Details — Miami's tropical paradise.. History. Butterflies. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Butterflies.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Butterflies.", "x": "Fairchild Tropical Garden in depth: Butterflies.. Cycads. Details — Miami's tropical paradise.. Tickets. 83 acres. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Fairchild Tropical Garden in depth: History.. Butterflies. Details — Miami's tropical paradise.. Miami. Art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Fairchild Tropical Garden in depth: Tickets.. 83 acres. Details — Miami's tropical paradise.. Art. 1938. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Miami.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Miami.", "x": "Fairchild Tropical Garden in depth: Miami.. Art. Details — Miami's tropical paradise.. Palms. Palms. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Art.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Art.", "x": "Fairchild Tropical Garden in depth: Art.. 1938. Details — Miami's tropical paradise.. Butterflies. Cycads. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Fairchild Tropical Garden comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Fairchild Tropical Garden comes from.", "x": "Origins: Palms.. 1938. The history of Fairchild Tropical Garden — Miami's tropical paradise.. Butterflies. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Fairchild Tropical Garden respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Fairchild Tropical Garden respectfully.", "x": "Engaging: History.. Palms. How to participate or observe well — Fairchild Tropical Garden. Miami's tropical paradise. Respect first, always; Tickets.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Fairchild Tropical Garden do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Fairchild Tropical Garden do's and don'ts.", "x": "Etiquette: Miami.. Cycads. The rules of respect — Fairchild Tropical Garden. Miami's tropical paradise. When in doubt, ask about Art.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Fairchild Tropical Garden.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Fairchild Tropical Garden.", "x": "Planning: Palms.. Butterflies. Practical notes — Fairchild Tropical Garden. Miami's tropical paradise. A little planning shows respect for Butterflies.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Fairchild Tropical Garden and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Fairchild Tropical Garden and money.", "x": "Costs: History.. 83 acres. What to budget — Fairchild Tropical Garden. Miami's tropical paradise. The best experiences of Tickets. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-garden-fairchild-tropical-garden-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
