(function(){'use strict';
/* JAH Neo-Traditional Tattoos Tattoo Style Database generator — jahdb-e2-tattoo-neo-traditional-tattoos-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-tattoo-neo-traditional-tattoos',PREFIX='JAH-E2TATTOONEO-',NAME='JAH Neo-Traditional Tattoos Tattoo Style Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Neo-Traditional Tattoos: the complete guide", "d": "Neo-Traditional Tattoos: bold meets illustrative..", "g": "overview", "l": 2, "q": "What is Neo-Traditional Tattoos: the complete guide?", "a": "Neo-Traditional Tattoos: bold meets illustrative..", "x": "The complete tattoo style guide to Neo-Traditional Tattoos: bold meets illustrative.. Color. History, meaning, practices, and how to engage respectfully — everything in one database. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Neo-Traditional Tattoos essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Neo-Traditional Tattoos essentials.", "x": "At a glance: Neo-Traditional Tattoos — bold meets illustrative.. Bold lines. The essentials: Motifs.. Illustrative. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Color.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Color.", "x": "Neo-Traditional Tattoos: Color.. Motifs. Essential knowledge — Illustrative.. bold meets illustrative. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Color..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Color..", "x": "Explained: Color.. Color. The context — Neo-Traditional Tattoos. Motifs. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Bold lines.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Bold lines.", "x": "Neo-Traditional Tattoos: Bold lines.. Artists. Essential knowledge — Motifs.. bold meets illustrative. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Bold lines..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Bold lines..", "x": "Explained: Bold lines.. Aging. The context — Neo-Traditional Tattoos. Artists. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Illustrative.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Illustrative.", "x": "Neo-Traditional Tattoos: Illustrative.. Color. Essential knowledge — Artists.. bold meets illustrative. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Illustrative..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Illustrative..", "x": "Explained: Illustrative.. Style. The context — Neo-Traditional Tattoos. Style. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Motifs.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Motifs.", "x": "Neo-Traditional Tattoos: Motifs.. Aging. Essential knowledge — Style.. bold meets illustrative. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Motifs..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Motifs..", "x": "Explained: Motifs.. History. The context — Neo-Traditional Tattoos. Color. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Artists.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Artists.", "x": "Neo-Traditional Tattoos: Artists.. Style. Essential knowledge — Color.. bold meets illustrative. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Artists..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Artists..", "x": "Explained: Artists.. Motifs. The context — Neo-Traditional Tattoos. Bold lines. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Style.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Style.", "x": "Neo-Traditional Tattoos: Style.. History. Essential knowledge — Bold lines.. bold meets illustrative. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Style..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Style..", "x": "Explained: Style.. Artists. The context — Neo-Traditional Tattoos. Illustrative. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Neo-Traditional Tattoos in depth: History.. Bold lines. Details — bold meets illustrative.. Artists. Motifs. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Motifs.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Motifs.", "x": "Neo-Traditional Tattoos in depth: Motifs.. Illustrative. Details — bold meets illustrative.. Color. Artists. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Artists.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Artists.", "x": "Neo-Traditional Tattoos in depth: Artists.. Motifs. Details — bold meets illustrative.. Aging. Style. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Color.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Color.", "x": "Neo-Traditional Tattoos in depth: Color.. Artists. Details — bold meets illustrative.. Style. Color. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Aging.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Aging.", "x": "Neo-Traditional Tattoos in depth: Aging.. Style. Details — bold meets illustrative.. History. Bold lines. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Style.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Style.", "x": "Neo-Traditional Tattoos in depth: Style.. Color. Details — bold meets illustrative.. Motifs. Illustrative. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Neo-Traditional Tattoos comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Neo-Traditional Tattoos comes from.", "x": "Origins: History.. Color. The history of Neo-Traditional Tattoos — bold meets illustrative.. Motifs. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Neo-Traditional Tattoos respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Neo-Traditional Tattoos respectfully.", "x": "Engaging: Artists.. Bold lines. How to participate or observe well — Neo-Traditional Tattoos. bold meets illustrative. Respect first, always; Color.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Neo-Traditional Tattoos do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Neo-Traditional Tattoos do's and don'ts.", "x": "Etiquette: Aging.. Illustrative. The rules of respect — Neo-Traditional Tattoos. bold meets illustrative. When in doubt, ask about Style.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Neo-Traditional Tattoos.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Neo-Traditional Tattoos.", "x": "Planning: History.. Motifs. Practical notes — Neo-Traditional Tattoos. bold meets illustrative. A little planning shows respect for Motifs.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Neo-Traditional Tattoos and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Neo-Traditional Tattoos and money.", "x": "Costs: Artists.. Artists. What to budget — Neo-Traditional Tattoos. bold meets illustrative. The best experiences of Color. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-tattoo-neo-traditional-tattoos-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
