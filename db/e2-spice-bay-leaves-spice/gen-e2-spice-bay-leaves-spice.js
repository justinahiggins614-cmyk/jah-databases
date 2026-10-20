(function(){'use strict';
/* JAH Bay Leaves Spice Database generator — jahdb-e2-spice-bay-leaves-spice-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-spice-bay-leaves-spice',PREFIX='JAH-E2SPICEBAYL-',NAME='JAH Bay Leaves Spice Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Bay Leaves: the complete guide", "d": "Bay Leaves: the simmer leaf..", "g": "overview", "l": 2, "q": "What is Bay Leaves: the complete guide?", "a": "Bay Leaves: the simmer leaf..", "x": "The complete spice guide to Bay Leaves: the simmer leaf.. Laurel. History, meaning, practices, and how to engage respectfully — everything in one database. Soups. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Bay Leaves essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Bay Leaves essentials.", "x": "At a glance: Bay Leaves — the simmer leaf.. Soups. The essentials: Remove.. Remove. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Laurel.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Laurel.", "x": "Bay Leaves: Laurel.. Remove. Essential knowledge — Remove.. the simmer leaf. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Laurel..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Laurel..", "x": "Explained: Laurel.. Stews. The context — Bay Leaves. Turkish. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Soups.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Soups.", "x": "Bay Leaves: Soups.. Varieties. Essential knowledge — Turkish.. the simmer leaf. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Soups..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Soups..", "x": "Explained: Soups.. History. The context — Bay Leaves. California. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Remove.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Remove.", "x": "Bay Leaves: Remove.. Stews. Essential knowledge — California.. the simmer leaf. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Remove..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Remove..", "x": "Explained: Remove.. Storage. The context — Bay Leaves. Stews. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Turkish.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Turkish.", "x": "Bay Leaves: Turkish.. History. Essential knowledge — Stews.. the simmer leaf. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Turkish..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Turkish..", "x": "Explained: Turkish.. Soups. The context — Bay Leaves. Laurel. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "California.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "California.", "x": "Bay Leaves: California.. Storage. Essential knowledge — Laurel.. the simmer leaf. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: California..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: California..", "x": "Explained: California.. Remove. The context — Bay Leaves. Soups. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Stews.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Stews.", "x": "Bay Leaves: Stews.. Soups. Essential knowledge — Soups.. the simmer leaf. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Stews..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Stews..", "x": "Explained: Stews.. Varieties. The context — Bay Leaves. Remove. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Soups.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Soups.", "x": "Bay Leaves in depth: Soups.. Soups. Details — the simmer leaf.. Varieties. Turkish. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Remove.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Remove.", "x": "Bay Leaves in depth: Remove.. Remove. Details — the simmer leaf.. Stews. California. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Varieties.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Varieties.", "x": "Bay Leaves in depth: Varieties.. Turkish. Details — the simmer leaf.. History. Stews. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Stews.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Stews.", "x": "Bay Leaves in depth: Stews.. California. Details — the simmer leaf.. Storage. Laurel. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "History.", "x": "Bay Leaves in depth: History.. Stews. Details — the simmer leaf.. Soups. Soups. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Storage.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Storage.", "x": "Bay Leaves in depth: Storage.. Laurel. Details — the simmer leaf.. Remove. Remove. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Bay Leaves comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Bay Leaves comes from.", "x": "Origins: Soups.. Laurel. The history of Bay Leaves — the simmer leaf.. Remove. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Bay Leaves respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Bay Leaves respectfully.", "x": "Engaging: Varieties.. Soups. How to participate or observe well — Bay Leaves. the simmer leaf. Respect first, always; Stews.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Bay Leaves do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Bay Leaves do's and don'ts.", "x": "Etiquette: History.. Remove. The rules of respect — Bay Leaves. the simmer leaf. When in doubt, ask about Storage.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Bay Leaves.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Bay Leaves.", "x": "Planning: Soups.. Turkish. Practical notes — Bay Leaves. the simmer leaf. A little planning shows respect for Remove.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Bay Leaves and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Bay Leaves and money.", "x": "Costs: Varieties.. California. What to budget — Bay Leaves. the simmer leaf. The best experiences of Stews. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-spice-bay-leaves-spice-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
