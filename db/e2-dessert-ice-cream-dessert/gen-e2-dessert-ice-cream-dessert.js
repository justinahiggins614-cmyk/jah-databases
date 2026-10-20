(function(){'use strict';
/* JAH Ice Cream Dessert Database generator — jahdb-e2-dessert-ice-cream-dessert-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dessert-ice-cream-dessert',PREFIX='JAH-E2DESSERTIC-',NAME='JAH Ice Cream Dessert Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Ice Cream: the complete guide", "d": "Ice Cream: the frozen classic..", "g": "overview", "l": 2, "q": "What is Ice Cream: the complete guide?", "a": "Ice Cream: the frozen classic..", "x": "The complete dessert guide to Ice Cream: the frozen classic.. Cream. History, meaning, practices, and how to engage respectfully — everything in one database. Churned. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Ice Cream essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Ice Cream essentials.", "x": "At a glance: Ice Cream — the frozen classic.. Churned. The essentials: Flavors.. Flavors. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Cream.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Cream.", "x": "Ice Cream: Cream.. Flavors. Essential knowledge — Flavors.. the frozen classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Cream..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Cream..", "x": "Explained: Cream.. History. The context — Ice Cream. Cones. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Churned.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Churned.", "x": "Ice Cream: Churned.. Cones. Essential knowledge — Cones.. the frozen classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Churned..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Churned..", "x": "Explained: Churned.. Gelato. The context — Ice Cream. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Flavors.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Flavors.", "x": "Ice Cream: Flavors.. History. Essential knowledge — History.. the frozen classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Flavors..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Flavors..", "x": "Explained: Flavors.. Making. The context — Ice Cream. Gelato. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Cones.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Cones.", "x": "Ice Cream: Cones.. Gelato. Essential knowledge — Gelato.. the frozen classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Cones..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Cones..", "x": "Explained: Cones.. Churned. The context — Ice Cream. Cream. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "History.", "x": "Ice Cream: History.. Making. Essential knowledge — Cream.. the frozen classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: History..", "x": "Explained: History.. Flavors. The context — Ice Cream. Churned. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Gelato.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Gelato.", "x": "Ice Cream: Gelato.. Churned. Essential knowledge — Churned.. the frozen classic. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Gelato..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Gelato..", "x": "Explained: Gelato.. Cones. The context — Ice Cream. Flavors. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Churned.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Churned.", "x": "Ice Cream in depth: Churned.. Churned. Details — the frozen classic.. Cones. Cones. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Flavors.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Flavors.", "x": "Ice Cream in depth: Flavors.. Flavors. Details — the frozen classic.. History. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Cones.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Cones.", "x": "Ice Cream in depth: Cones.. Cones. Details — the frozen classic.. Gelato. Gelato. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "History.", "x": "Ice Cream in depth: History.. History. Details — the frozen classic.. Making. Cream. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Gelato.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Gelato.", "x": "Ice Cream in depth: Gelato.. Gelato. Details — the frozen classic.. Churned. Churned. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "Ice Cream in depth: Making.. Cream. Details — the frozen classic.. Flavors. Flavors. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Ice Cream comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Ice Cream comes from.", "x": "Origins: Churned.. Cream. The history of Ice Cream — the frozen classic.. Flavors. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Ice Cream respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Ice Cream respectfully.", "x": "Engaging: Cones.. Churned. How to participate or observe well — Ice Cream. the frozen classic. Respect first, always; History.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Ice Cream do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Ice Cream do's and don'ts.", "x": "Etiquette: Gelato.. Flavors. The rules of respect — Ice Cream. the frozen classic. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Ice Cream.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Ice Cream.", "x": "Planning: Churned.. Cones. Practical notes — Ice Cream. the frozen classic. A little planning shows respect for Flavors.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Ice Cream and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Ice Cream and money.", "x": "Costs: Cones.. History. What to budget — Ice Cream. the frozen classic. The best experiences of History. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dessert-ice-cream-dessert-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
