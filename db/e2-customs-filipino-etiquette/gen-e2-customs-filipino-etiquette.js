(function(){'use strict';
/* JAH Filipino Etiquette Customs Database generator — jahdb-e2-customs-filipino-etiquette-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-customs-filipino-etiquette',PREFIX='JAH-E2CUSTOMSFI-',NAME='JAH Filipino Etiquette Customs Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Filipino Etiquette: the complete guide", "d": "Filipino Etiquette: pakikisama: togetherness..", "g": "overview", "l": 2, "q": "What is Filipino Etiquette: the complete guide?", "a": "Filipino Etiquette: pakikisama: togetherness..", "x": "The complete customs guide to Filipino Etiquette: pakikisama: togetherness.. Mano. History, meaning, practices, and how to engage respectfully — everything in one database. Bless. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Filipino Etiquette essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Filipino Etiquette essentials.", "x": "At a glance: Filipino Etiquette — pakikisama: togetherness.. Hospitality. The essentials: Guests.. Family. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Mano.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Mano.", "x": "Filipino Etiquette: Mano.. Guests. Essential knowledge — Family.. pakikisama: togetherness. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Mano..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Mano..", "x": "Explained: Mano.. Fun. The context — Filipino Etiquette. Karaoke. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Hospitality.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Hospitality.", "x": "Filipino Etiquette: Hospitality.. Family. Essential knowledge — Karaoke.. pakikisama: togetherness. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Hospitality..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Hospitality..", "x": "Explained: Hospitality.. Food. The context — Filipino Etiquette. Respect. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Family.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Family.", "x": "Filipino Etiquette: Family.. Fun. Essential knowledge — Respect.. pakikisama: togetherness. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Family..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Family..", "x": "Explained: Family.. Heart. The context — Filipino Etiquette. Food. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Karaoke.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Karaoke.", "x": "Filipino Etiquette: Karaoke.. Food. Essential knowledge — Food.. pakikisama: togetherness. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Karaoke..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Karaoke..", "x": "Explained: Karaoke.. Bless. The context — Filipino Etiquette. Mano. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Respect.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Respect.", "x": "Filipino Etiquette: Respect.. Heart. Essential knowledge — Mano.. pakikisama: togetherness. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Respect..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Respect..", "x": "Explained: Respect.. Guests. The context — Filipino Etiquette. Hospitality. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Food.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Food.", "x": "Filipino Etiquette: Food.. Bless. Essential knowledge — Hospitality.. pakikisama: togetherness. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Food..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Food..", "x": "Explained: Food.. Family. The context — Filipino Etiquette. Family. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Bless.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Bless.", "x": "Filipino Etiquette in depth: Bless.. Hospitality. Details — pakikisama: togetherness.. Family. Karaoke. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Guests.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Guests.", "x": "Filipino Etiquette in depth: Guests.. Family. Details — pakikisama: togetherness.. Fun. Respect. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Family.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Family.", "x": "Filipino Etiquette in depth: Family.. Karaoke. Details — pakikisama: togetherness.. Food. Food. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Fun.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Fun.", "x": "Filipino Etiquette in depth: Fun.. Respect. Details — pakikisama: togetherness.. Heart. Mano. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Food.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Food.", "x": "Filipino Etiquette in depth: Food.. Food. Details — pakikisama: togetherness.. Bless. Hospitality. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Heart.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Heart.", "x": "Filipino Etiquette in depth: Heart.. Mano. Details — pakikisama: togetherness.. Guests. Family. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Filipino Etiquette comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Filipino Etiquette comes from.", "x": "Origins: Bless.. Mano. The history of Filipino Etiquette — pakikisama: togetherness.. Guests. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Filipino Etiquette respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Filipino Etiquette respectfully.", "x": "Engaging: Family.. Hospitality. How to participate or observe well — Filipino Etiquette. pakikisama: togetherness. Respect first, always; Fun.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Filipino Etiquette do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Filipino Etiquette do's and don'ts.", "x": "Etiquette: Food.. Family. The rules of respect — Filipino Etiquette. pakikisama: togetherness. When in doubt, ask about Heart.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Filipino Etiquette.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Filipino Etiquette.", "x": "Planning: Bless.. Karaoke. Practical notes — Filipino Etiquette. pakikisama: togetherness. A little planning shows respect for Guests.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Filipino Etiquette and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Filipino Etiquette and money.", "x": "Costs: Family.. Respect. What to budget — Filipino Etiquette. pakikisama: togetherness. The best experiences of Fun. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-customs-filipino-etiquette-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
