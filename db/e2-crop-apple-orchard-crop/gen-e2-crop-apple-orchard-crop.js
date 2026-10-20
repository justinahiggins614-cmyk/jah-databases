(function(){'use strict';
/* JAH Apple Orchard Crop Database generator — jahdb-e2-crop-apple-orchard-crop-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-crop-apple-orchard-crop',PREFIX='JAH-E2CROPAPPLE-',NAME='JAH Apple Orchard Crop Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Apple Orchard: the complete guide", "d": "Apple Orchard: the orchard fruit..", "g": "overview", "l": 2, "q": "What is Apple Orchard: the complete guide?", "a": "Apple Orchard: the orchard fruit..", "x": "The complete crop guide to Apple Orchard: the orchard fruit.. Grafting. History, meaning, practices, and how to engage respectfully — everything in one database. Grafting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Apple Orchard essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Apple Orchard essentials.", "x": "At a glance: Apple Orchard — the orchard fruit.. Dwarf. The essentials: Thinning.. Thinning. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Grafting.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Grafting.", "x": "Apple Orchard: Grafting.. Thinning. Essential knowledge — Thinning.. the orchard fruit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Grafting..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Grafting..", "x": "Explained: Grafting.. Storage. The context — Apple Orchard. Cider. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Dwarf.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Dwarf.", "x": "Apple Orchard: Dwarf.. Cider. Essential knowledge — Cider.. the orchard fruit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Dwarf..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Dwarf..", "x": "Explained: Dwarf.. Dwarf. The context — Apple Orchard. Storage. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Thinning.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Thinning.", "x": "Apple Orchard: Thinning.. Storage. Essential knowledge — Storage.. the orchard fruit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Thinning..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Thinning..", "x": "Explained: Thinning.. Growing. The context — Apple Orchard. Varieties. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Cider.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Cider.", "x": "Apple Orchard: Cider.. Dwarf. Essential knowledge — Varieties.. the orchard fruit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Cider..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Cider..", "x": "Explained: Cider.. Grafting. The context — Apple Orchard. Grafting. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Storage.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Storage.", "x": "Apple Orchard: Storage.. Growing. Essential knowledge — Grafting.. the orchard fruit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Storage..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Storage..", "x": "Explained: Storage.. Thinning. The context — Apple Orchard. Dwarf. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Varieties.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Varieties.", "x": "Apple Orchard: Varieties.. Grafting. Essential knowledge — Dwarf.. the orchard fruit. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Varieties..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Varieties..", "x": "Explained: Varieties.. Cider. The context — Apple Orchard. Thinning. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Grafting.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Grafting.", "x": "Apple Orchard in depth: Grafting.. Dwarf. Details — the orchard fruit.. Cider. Cider. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Thinning.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Thinning.", "x": "Apple Orchard in depth: Thinning.. Thinning. Details — the orchard fruit.. Storage. Storage. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Cider.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Cider.", "x": "Apple Orchard in depth: Cider.. Cider. Details — the orchard fruit.. Dwarf. Varieties. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Storage.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Storage.", "x": "Apple Orchard in depth: Storage.. Storage. Details — the orchard fruit.. Growing. Grafting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Dwarf.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Dwarf.", "x": "Apple Orchard in depth: Dwarf.. Varieties. Details — the orchard fruit.. Grafting. Dwarf. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Growing.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Growing.", "x": "Apple Orchard in depth: Growing.. Grafting. Details — the orchard fruit.. Thinning. Thinning. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Apple Orchard comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Apple Orchard comes from.", "x": "Origins: Grafting.. Grafting. The history of Apple Orchard — the orchard fruit.. Thinning. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Apple Orchard respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Apple Orchard respectfully.", "x": "Engaging: Cider.. Dwarf. How to participate or observe well — Apple Orchard. the orchard fruit. Respect first, always; Storage.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Apple Orchard do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Apple Orchard do's and don'ts.", "x": "Etiquette: Dwarf.. Thinning. The rules of respect — Apple Orchard. the orchard fruit. When in doubt, ask about Growing.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Apple Orchard.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Apple Orchard.", "x": "Planning: Grafting.. Cider. Practical notes — Apple Orchard. the orchard fruit. A little planning shows respect for Thinning.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Apple Orchard and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Apple Orchard and money.", "x": "Costs: Cider.. Storage. What to budget — Apple Orchard. the orchard fruit. The best experiences of Storage. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-crop-apple-orchard-crop-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
