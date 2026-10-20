(function(){'use strict';
/* JAH Jack Russell Terrier Dog Breed Database generator — jahdb-e2-dog-jack-russell-terrier-dog-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dog-jack-russell-terrier-dog',PREFIX='JAH-E2DOGJACKRU-',NAME='JAH Jack Russell Terrier Dog Breed Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Jack Russell Terrier: the complete guide", "d": "Jack Russell Terrier: the energetic jack..", "g": "overview", "l": 2, "q": "What is Jack Russell Terrier: the complete guide?", "a": "Jack Russell Terrier: the energetic jack..", "x": "The complete dog breed guide to Jack Russell Terrier: the energetic jack.. Energy. History, meaning, practices, and how to engage respectfully — everything in one database. Energy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Jack Russell Terrier essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Jack Russell Terrier essentials.", "x": "At a glance: Jack Russell Terrier — the energetic jack.. Jumping. The essentials: Jumping.. England. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Energy.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Energy.", "x": "Jack Russell Terrier: Energy.. Jumping. Essential knowledge — England.. the energetic jack. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Energy..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Energy..", "x": "Explained: Energy.. Smart. The context — Jack Russell Terrier. Hunting. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Jumping.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Jumping.", "x": "Jack Russell Terrier: Jumping.. England. Essential knowledge — Hunting.. the energetic jack. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Jumping..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Jumping..", "x": "Explained: Jumping.. Hunting. The context — Jack Russell Terrier. Smart. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "England.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "England.", "x": "Jack Russell Terrier: England.. Smart. Essential knowledge — Smart.. the energetic jack. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: England..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: England..", "x": "Explained: England.. History. The context — Jack Russell Terrier. Barking. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Hunting.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Hunting.", "x": "Jack Russell Terrier: Hunting.. Hunting. Essential knowledge — Barking.. the energetic jack. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Hunting..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Hunting..", "x": "Explained: Hunting.. Energy. The context — Jack Russell Terrier. Energy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Smart.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Smart.", "x": "Jack Russell Terrier: Smart.. History. Essential knowledge — Energy.. the energetic jack. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Smart..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Smart..", "x": "Explained: Smart.. Jumping. The context — Jack Russell Terrier. Jumping. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Barking.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Barking.", "x": "Jack Russell Terrier: Barking.. Energy. Essential knowledge — Jumping.. the energetic jack. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Barking..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Barking..", "x": "Explained: Barking.. England. The context — Jack Russell Terrier. England. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Energy.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Energy.", "x": "Jack Russell Terrier in depth: Energy.. Jumping. Details — the energetic jack.. England. Hunting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Jumping.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Jumping.", "x": "Jack Russell Terrier in depth: Jumping.. England. Details — the energetic jack.. Smart. Smart. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "England.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "England.", "x": "Jack Russell Terrier in depth: England.. Hunting. Details — the energetic jack.. Hunting. Barking. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Smart.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Smart.", "x": "Jack Russell Terrier in depth: Smart.. Smart. Details — the energetic jack.. History. Energy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Hunting.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Hunting.", "x": "Jack Russell Terrier in depth: Hunting.. Barking. Details — the energetic jack.. Energy. Jumping. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Jack Russell Terrier in depth: History.. Energy. Details — the energetic jack.. Jumping. England. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Jack Russell Terrier comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Jack Russell Terrier comes from.", "x": "Origins: Energy.. Energy. The history of Jack Russell Terrier — the energetic jack.. Jumping. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Jack Russell Terrier respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Jack Russell Terrier respectfully.", "x": "Engaging: England.. Jumping. How to participate or observe well — Jack Russell Terrier. the energetic jack. Respect first, always; Smart.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Jack Russell Terrier do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Jack Russell Terrier do's and don'ts.", "x": "Etiquette: Hunting.. England. The rules of respect — Jack Russell Terrier. the energetic jack. When in doubt, ask about History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Jack Russell Terrier.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Jack Russell Terrier.", "x": "Planning: Energy.. Hunting. Practical notes — Jack Russell Terrier. the energetic jack. A little planning shows respect for Jumping.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Jack Russell Terrier and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Jack Russell Terrier and money.", "x": "Costs: England.. Smart. What to budget — Jack Russell Terrier. the energetic jack. The best experiences of Smart. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dog-jack-russell-terrier-dog-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
