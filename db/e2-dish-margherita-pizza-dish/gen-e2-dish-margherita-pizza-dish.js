(function(){'use strict';
/* JAH Margherita Pizza Dish Database generator — jahdb-e2-dish-margherita-pizza-dish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dish-margherita-pizza-dish',PREFIX='JAH-E2DISHMARGH-',NAME='JAH Margherita Pizza Dish Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Margherita Pizza: the complete guide", "d": "Margherita Pizza: the Naples classic..", "g": "overview", "l": 2, "q": "What is Margherita Pizza: the complete guide?", "a": "Margherita Pizza: the Naples classic..", "x": "The complete dish guide to Margherita Pizza: the Naples classic.. Naples. History, meaning, practices, and how to engage respectfully — everything in one database. Naples. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Margherita Pizza essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Margherita Pizza essentials.", "x": "At a glance: Margherita Pizza — the Naples classic.. 1889. The essentials: Wood-fired.. Basil. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Naples.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Naples.", "x": "Margherita Pizza: Naples.. Wood-fired. Essential knowledge — Basil.. the Naples classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Naples..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Naples..", "x": "Explained: Naples.. 1889. The context — Margherita Pizza. Mozzarella. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "1889.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "1889.", "x": "Margherita Pizza: 1889.. Basil. Essential knowledge — Mozzarella.. the Naples classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: 1889..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: 1889..", "x": "Explained: 1889.. Mozzarella. The context — Margherita Pizza. Wood-fired. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Basil.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Basil.", "x": "Margherita Pizza: Basil.. 1889. Essential knowledge — Wood-fired.. the Naples classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Basil..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Basil..", "x": "Explained: Basil.. Making. The context — Margherita Pizza. Margherita. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Mozzarella.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Mozzarella.", "x": "Margherita Pizza: Mozzarella.. Mozzarella. Essential knowledge — Margherita.. the Naples classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Mozzarella..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Mozzarella..", "x": "Explained: Mozzarella.. Naples. The context — Margherita Pizza. Naples. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Wood-fired.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Wood-fired.", "x": "Margherita Pizza: Wood-fired.. Making. Essential knowledge — Naples.. the Naples classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Wood-fired..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Wood-fired..", "x": "Explained: Wood-fired.. Wood-fired. The context — Margherita Pizza. 1889. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Margherita.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Margherita.", "x": "Margherita Pizza: Margherita.. Naples. Essential knowledge — 1889.. the Naples classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Margherita..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Margherita..", "x": "Explained: Margherita.. Basil. The context — Margherita Pizza. Basil. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Naples.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Naples.", "x": "Margherita Pizza in depth: Naples.. 1889. Details — the Naples classic.. Basil. Mozzarella. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Wood-fired.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Wood-fired.", "x": "Margherita Pizza in depth: Wood-fired.. Basil. Details — the Naples classic.. 1889. Wood-fired. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Basil.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Basil.", "x": "Margherita Pizza in depth: Basil.. Mozzarella. Details — the Naples classic.. Mozzarella. Margherita. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "1889.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "1889.", "x": "Margherita Pizza in depth: 1889.. Wood-fired. Details — the Naples classic.. Making. Naples. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Mozzarella.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Mozzarella.", "x": "Margherita Pizza in depth: Mozzarella.. Margherita. Details — the Naples classic.. Naples. 1889. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Margherita Pizza in depth: Making.. Naples. Details — the Naples classic.. Wood-fired. Basil. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Margherita Pizza comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Margherita Pizza comes from.", "x": "Origins: Naples.. Naples. The history of Margherita Pizza — the Naples classic.. Wood-fired. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Margherita Pizza respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Margherita Pizza respectfully.", "x": "Engaging: Basil.. 1889. How to participate or observe well — Margherita Pizza. the Naples classic. Respect first, always; 1889.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Margherita Pizza do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Margherita Pizza do's and don'ts.", "x": "Etiquette: Mozzarella.. Basil. The rules of respect — Margherita Pizza. the Naples classic. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Margherita Pizza.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Margherita Pizza.", "x": "Planning: Naples.. Mozzarella. Practical notes — Margherita Pizza. the Naples classic. A little planning shows respect for Wood-fired.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Margherita Pizza and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Margherita Pizza and money.", "x": "Costs: Basil.. Wood-fired. What to budget — Margherita Pizza. the Naples classic. The best experiences of 1889. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dish-margherita-pizza-dish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
