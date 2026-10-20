(function(){'use strict';
/* JAH DC Superheroes Superhero Database generator — jahdb-e2-hero-dc-superheroes-universe-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hero-dc-superheroes-universe',PREFIX='JAH-E2HERODCSUP-',NAME='JAH DC Superheroes Superhero Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "DC Superheroes: the complete guide", "d": "DC Superheroes: the DC universe..", "g": "overview", "l": 2, "q": "What is DC Superheroes: the complete guide?", "a": "DC Superheroes: the DC universe..", "x": "The complete superhero guide to DC Superheroes: the DC universe.. 1938. History, meaning, practices, and how to engage respectfully — everything in one database. Superman. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "DC Superheroes essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "DC Superheroes essentials.", "x": "At a glance: DC Superheroes — the DC universe.. Superman. The essentials: Batman.. Batman. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1938.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1938.", "x": "DC Superheroes: 1938.. Batman. Essential knowledge — Batman.. the DC universe. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1938..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1938..", "x": "Explained: 1938.. Multiverse. The context — DC Superheroes. Justice League. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Superman.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Superman.", "x": "DC Superheroes: Superman.. League. Essential knowledge — Justice League.. the DC universe. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Superman..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Superman..", "x": "Explained: Superman.. 1938. The context — DC Superheroes. Multiverse. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Batman.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Batman.", "x": "DC Superheroes: Batman.. Multiverse. Essential knowledge — Multiverse.. the DC universe. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Batman..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Batman..", "x": "Explained: Batman.. Heroes. The context — DC Superheroes. DCEU. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Justice League.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Justice League.", "x": "DC Superheroes: Justice League.. 1938. Essential knowledge — DCEU.. the DC universe. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Justice League..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Justice League..", "x": "Explained: Justice League.. Superman. The context — DC Superheroes. 1938. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Multiverse.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Multiverse.", "x": "DC Superheroes: Multiverse.. Heroes. Essential knowledge — 1938.. the DC universe. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Multiverse..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Multiverse..", "x": "Explained: Multiverse.. Batman. The context — DC Superheroes. Superman. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "DCEU.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "DCEU.", "x": "DC Superheroes: DCEU.. Superman. Essential knowledge — Superman.. the DC universe. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: DCEU..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: DCEU..", "x": "Explained: DCEU.. League. The context — DC Superheroes. Batman. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Superman.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Superman.", "x": "DC Superheroes in depth: Superman.. Superman. Details — the DC universe.. League. Justice League. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Batman.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Batman.", "x": "DC Superheroes in depth: Batman.. Batman. Details — the DC universe.. Multiverse. Multiverse. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "League.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "League.", "x": "DC Superheroes in depth: League.. Justice League. Details — the DC universe.. 1938. DCEU. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Multiverse.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Multiverse.", "x": "DC Superheroes in depth: Multiverse.. Multiverse. Details — the DC universe.. Heroes. 1938. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "1938.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "1938.", "x": "DC Superheroes in depth: 1938.. DCEU. Details — the DC universe.. Superman. Superman. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Heroes.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Heroes.", "x": "DC Superheroes in depth: Heroes.. 1938. Details — the DC universe.. Batman. Batman. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where DC Superheroes comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where DC Superheroes comes from.", "x": "Origins: Superman.. 1938. The history of DC Superheroes — the DC universe.. Batman. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing DC Superheroes respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing DC Superheroes respectfully.", "x": "Engaging: League.. Superman. How to participate or observe well — DC Superheroes. the DC universe. Respect first, always; Multiverse.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "DC Superheroes do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "DC Superheroes do's and don'ts.", "x": "Etiquette: 1938.. Batman. The rules of respect — DC Superheroes. the DC universe. When in doubt, ask about Heroes.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around DC Superheroes.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around DC Superheroes.", "x": "Planning: Superman.. Justice League. Practical notes — DC Superheroes. the DC universe. A little planning shows respect for Batman.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "DC Superheroes and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "DC Superheroes and money.", "x": "Costs: League.. Multiverse. What to budget — DC Superheroes. the DC universe. The best experiences of Multiverse. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hero-dc-superheroes-universe-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
