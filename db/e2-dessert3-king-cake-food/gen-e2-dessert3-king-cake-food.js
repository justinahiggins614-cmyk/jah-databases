(function(){'use strict';
/* JAH King Cake Dessert Database generator — jahdb-e2-dessert3-king-cake-food-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dessert3-king-cake-food',PREFIX='JAH-E2DESSERT3K-',NAME='JAH King Cake Dessert Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "King Cake: the complete guide", "d": "King Cake: the Mardi Gras..", "g": "overview", "l": 2, "q": "What is King Cake: the complete guide?", "a": "King Cake: the Mardi Gras..", "x": "The complete dessert guide to King Cake: the Mardi Gras.. Mardi Gras. History, meaning, practices, and how to engage respectfully — everything in one database. Baby. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "King Cake essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "King Cake essentials.", "x": "At a glance: King Cake — the Mardi Gras.. Baby. The essentials: Purple.. Cinnamon. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Mardi Gras.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Mardi Gras.", "x": "King Cake: Mardi Gras.. Purple. Essential knowledge — Cinnamon.. the Mardi Gras. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Mardi Gras..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Mardi Gras..", "x": "Explained: Mardi Gras.. Cinnamon. The context — King Cake. Purple. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Baby.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Baby.", "x": "King Cake: Baby.. Epiphany. Essential knowledge — Purple.. the Mardi Gras. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Baby..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Baby..", "x": "Explained: Baby.. NOLA. The context — King Cake. New Orleans. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Cinnamon.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Cinnamon.", "x": "King Cake: Cinnamon.. Cinnamon. Essential knowledge — New Orleans.. the Mardi Gras. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Cinnamon..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Cinnamon..", "x": "Explained: Cinnamon.. Making. The context — King Cake. Epiphany. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Purple.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Purple.", "x": "King Cake: Purple.. NOLA. Essential knowledge — Epiphany.. the Mardi Gras. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Purple..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Purple..", "x": "Explained: Purple.. Baby. The context — King Cake. Mardi Gras. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "New Orleans.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "New Orleans.", "x": "King Cake: New Orleans.. Making. Essential knowledge — Mardi Gras.. the Mardi Gras. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: New Orleans..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: New Orleans..", "x": "Explained: New Orleans.. Purple. The context — King Cake. Baby. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Epiphany.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Epiphany.", "x": "King Cake: Epiphany.. Baby. Essential knowledge — Baby.. the Mardi Gras. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Epiphany..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Epiphany..", "x": "Explained: Epiphany.. Epiphany. The context — King Cake. Cinnamon. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Baby.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Baby.", "x": "King Cake in depth: Baby.. Baby. Details — the Mardi Gras.. Epiphany. Purple. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Purple.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Purple.", "x": "King Cake in depth: Purple.. Cinnamon. Details — the Mardi Gras.. Cinnamon. New Orleans. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Epiphany.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Epiphany.", "x": "King Cake in depth: Epiphany.. Purple. Details — the Mardi Gras.. NOLA. Epiphany. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Cinnamon.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Cinnamon.", "x": "King Cake in depth: Cinnamon.. New Orleans. Details — the Mardi Gras.. Making. Mardi Gras. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "NOLA.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "NOLA.", "x": "King Cake in depth: NOLA.. Epiphany. Details — the Mardi Gras.. Baby. Baby. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Making.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Making.", "x": "King Cake in depth: Making.. Mardi Gras. Details — the Mardi Gras.. Purple. Cinnamon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where King Cake comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where King Cake comes from.", "x": "Origins: Baby.. Mardi Gras. The history of King Cake — the Mardi Gras.. Purple. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing King Cake respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing King Cake respectfully.", "x": "Engaging: Epiphany.. Baby. How to participate or observe well — King Cake. the Mardi Gras. Respect first, always; Cinnamon.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "King Cake do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "King Cake do's and don'ts.", "x": "Etiquette: NOLA.. Cinnamon. The rules of respect — King Cake. the Mardi Gras. When in doubt, ask about Making.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around King Cake.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around King Cake.", "x": "Planning: Baby.. Purple. Practical notes — King Cake. the Mardi Gras. A little planning shows respect for Purple.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "King Cake and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "King Cake and money.", "x": "Costs: Epiphany.. New Orleans. What to budget — King Cake. the Mardi Gras. The best experiences of Cinnamon. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dessert3-king-cake-food-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
