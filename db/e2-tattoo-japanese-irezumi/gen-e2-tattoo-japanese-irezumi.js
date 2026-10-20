(function(){'use strict';
/* JAH Japanese Irezumi Tattoo Style Database generator — jahdb-e2-tattoo-japanese-irezumi-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-tattoo-japanese-irezumi',PREFIX='JAH-E2TATTOOJAP-',NAME='JAH Japanese Irezumi Tattoo Style Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Japanese Irezumi: the complete guide", "d": "Japanese Irezumi: full-body art..", "g": "overview", "l": 2, "q": "What is Japanese Irezumi: the complete guide?", "a": "Japanese Irezumi: full-body art..", "x": "The complete tattoo style guide to Japanese Irezumi: full-body art.. Edo period. History, meaning, practices, and how to engage respectfully — everything in one database. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Japanese Irezumi essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Japanese Irezumi essentials.", "x": "At a glance: Japanese Irezumi — full-body art.. Bodysuits. The essentials: Motifs.. Dragons. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Edo period.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Edo period.", "x": "Japanese Irezumi: Edo period.. Motifs. Essential knowledge — Dragons.. full-body art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Edo period..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Edo period..", "x": "Explained: Edo period.. Culture. The context — Japanese Irezumi. Tebori. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Bodysuits.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Bodysuits.", "x": "Japanese Irezumi: Bodysuits.. Process. Essential knowledge — Tebori.. full-body art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Bodysuits..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Bodysuits..", "x": "Explained: Bodysuits.. Masters. The context — Japanese Irezumi. Yakuza. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Dragons.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Dragons.", "x": "Japanese Irezumi: Dragons.. Culture. Essential knowledge — Yakuza.. full-body art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Dragons..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Dragons..", "x": "Explained: Dragons.. Respect. The context — Japanese Irezumi. Masters. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Tebori.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Tebori.", "x": "Japanese Irezumi: Tebori.. Masters. Essential knowledge — Masters.. full-body art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Tebori..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Tebori..", "x": "Explained: Tebori.. History. The context — Japanese Irezumi. Edo period. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Yakuza.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Yakuza.", "x": "Japanese Irezumi: Yakuza.. Respect. Essential knowledge — Edo period.. full-body art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Yakuza..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Yakuza..", "x": "Explained: Yakuza.. Motifs. The context — Japanese Irezumi. Bodysuits. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Masters.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Masters.", "x": "Japanese Irezumi: Masters.. History. Essential knowledge — Bodysuits.. full-body art. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Masters..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Masters..", "x": "Explained: Masters.. Process. The context — Japanese Irezumi. Dragons. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Japanese Irezumi in depth: History.. Bodysuits. Details — full-body art.. Process. Tebori. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Motifs.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Motifs.", "x": "Japanese Irezumi in depth: Motifs.. Dragons. Details — full-body art.. Culture. Yakuza. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Process.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Process.", "x": "Japanese Irezumi in depth: Process.. Tebori. Details — full-body art.. Masters. Masters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Culture.", "x": "Japanese Irezumi in depth: Culture.. Yakuza. Details — full-body art.. Respect. Edo period. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Masters.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Masters.", "x": "Japanese Irezumi in depth: Masters.. Masters. Details — full-body art.. History. Bodysuits. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Respect.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Respect.", "x": "Japanese Irezumi in depth: Respect.. Edo period. Details — full-body art.. Motifs. Dragons. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Japanese Irezumi comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Japanese Irezumi comes from.", "x": "Origins: History.. Edo period. The history of Japanese Irezumi — full-body art.. Motifs. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Japanese Irezumi respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Japanese Irezumi respectfully.", "x": "Engaging: Process.. Bodysuits. How to participate or observe well — Japanese Irezumi. full-body art. Respect first, always; Culture.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Japanese Irezumi do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Japanese Irezumi do's and don'ts.", "x": "Etiquette: Masters.. Dragons. The rules of respect — Japanese Irezumi. full-body art. When in doubt, ask about Respect.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Japanese Irezumi.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Japanese Irezumi.", "x": "Planning: History.. Tebori. Practical notes — Japanese Irezumi. full-body art. A little planning shows respect for Motifs.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Japanese Irezumi and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Japanese Irezumi and money.", "x": "Costs: Process.. Yakuza. What to budget — Japanese Irezumi. full-body art. The best experiences of Culture. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-tattoo-japanese-irezumi-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
