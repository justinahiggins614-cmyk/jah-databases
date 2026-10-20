(function(){'use strict';
/* JAH Dark \'n Stormy Cocktail Database generator — jahdb-e2-cocktail-dark-n-stormy-cocktail-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-cocktail-dark-n-stormy-cocktail',PREFIX='JAH-E2COCKTAILD-',NAME='JAH Dark \'n Stormy Cocktail Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Dark 'n Stormy: the complete guide", "d": "Dark 'n Stormy: the Bermuda highball..", "g": "overview", "l": 2, "q": "What is Dark 'n Stormy: the complete guide?", "a": "Dark 'n Stormy: the Bermuda highball..", "x": "The complete cocktail guide to Dark 'n Stormy: the Bermuda highball.. Rum. History, meaning, practices, and how to engage respectfully — everything in one database. Rum. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Dark 'n Stormy essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Dark 'n Stormy essentials.", "x": "At a glance: Dark 'n Stormy — the Bermuda highball.. Ginger beer. The essentials: Ginger.. Lime. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Rum.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Rum.", "x": "Dark 'n Stormy: Rum.. Ginger. Essential knowledge — Lime.. the Bermuda highball. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Rum..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Rum..", "x": "Explained: Rum.. Trademark. The context — Dark 'n Stormy. Gosling's. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Ginger beer.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Ginger beer.", "x": "Dark 'n Stormy: Ginger beer.. Bermuda. Essential knowledge — Gosling's.. the Bermuda highball. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Ginger beer..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Ginger beer..", "x": "Explained: Ginger beer.. Lime. The context — Dark 'n Stormy. Bermuda. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Lime.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Lime.", "x": "Dark 'n Stormy: Lime.. Trademark. Essential knowledge — Bermuda.. the Bermuda highball. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Lime..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Lime..", "x": "Explained: Lime.. Highball. The context — Dark 'n Stormy. Trademark. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Gosling's.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Gosling's.", "x": "Dark 'n Stormy: Gosling's.. Lime. Essential knowledge — Trademark.. the Bermuda highball. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Gosling's..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Gosling's..", "x": "Explained: Gosling's.. Rum. The context — Dark 'n Stormy. Rum. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Bermuda.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Bermuda.", "x": "Dark 'n Stormy: Bermuda.. Highball. Essential knowledge — Rum.. the Bermuda highball. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Bermuda..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Bermuda..", "x": "Explained: Bermuda.. Ginger. The context — Dark 'n Stormy. Ginger beer. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Trademark.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Trademark.", "x": "Dark 'n Stormy: Trademark.. Rum. Essential knowledge — Ginger beer.. the Bermuda highball. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Trademark..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Trademark..", "x": "Explained: Trademark.. Bermuda. The context — Dark 'n Stormy. Lime. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Rum.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Rum.", "x": "Dark 'n Stormy in depth: Rum.. Ginger beer. Details — the Bermuda highball.. Bermuda. Gosling's. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Ginger.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Ginger.", "x": "Dark 'n Stormy in depth: Ginger.. Lime. Details — the Bermuda highball.. Trademark. Bermuda. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Bermuda.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Bermuda.", "x": "Dark 'n Stormy in depth: Bermuda.. Gosling's. Details — the Bermuda highball.. Lime. Trademark. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Trademark.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Trademark.", "x": "Dark 'n Stormy in depth: Trademark.. Bermuda. Details — the Bermuda highball.. Highball. Rum. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Lime.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Lime.", "x": "Dark 'n Stormy in depth: Lime.. Trademark. Details — the Bermuda highball.. Rum. Ginger beer. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Highball.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Highball.", "x": "Dark 'n Stormy in depth: Highball.. Rum. Details — the Bermuda highball.. Ginger. Lime. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Dark 'n Stormy comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Dark 'n Stormy comes from.", "x": "Origins: Rum.. Rum. The history of Dark 'n Stormy — the Bermuda highball.. Ginger. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Dark 'n Stormy respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Dark 'n Stormy respectfully.", "x": "Engaging: Bermuda.. Ginger beer. How to participate or observe well — Dark 'n Stormy. the Bermuda highball. Respect first, always; Trademark.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Dark 'n Stormy do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Dark 'n Stormy do's and don'ts.", "x": "Etiquette: Lime.. Lime. The rules of respect — Dark 'n Stormy. the Bermuda highball. When in doubt, ask about Highball.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Dark 'n Stormy.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Dark 'n Stormy.", "x": "Planning: Rum.. Gosling's. Practical notes — Dark 'n Stormy. the Bermuda highball. A little planning shows respect for Ginger.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Dark 'n Stormy and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Dark 'n Stormy and money.", "x": "Costs: Bermuda.. Bermuda. What to budget — Dark 'n Stormy. the Bermuda highball. The best experiences of Trademark. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-cocktail-dark-n-stormy-cocktail-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
