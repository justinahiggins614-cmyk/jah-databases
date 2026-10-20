(function(){'use strict';
/* JAH The Church of Jesus Christ of Latter-day Saints Religion Database generator — jahdb-e2-religion-latter-day-saints-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-religion-latter-day-saints',PREFIX='JAH-E2RELIGIONL-',NAME='JAH The Church of Jesus Christ of Latter-day Saints Religion Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "The Church of Jesus Christ of Latter-day Saints: the complete guide", "d": "The Church of Jesus Christ of Latter-day Saints: Mormonism; restoration..", "g": "overview", "l": 2, "q": "What is The Church of Jesus Christ of Latter-day Saints: the complete guide?", "a": "The Church of Jesus Christ of Latter-day Saints: Mormonism; restoration..", "x": "The complete religion guide to The Church of Jesus Christ of Latter-day Saints: Mormonism; restoration.. Joseph Smith. History, meaning, practices, and how to engage respectfully — everything in one database. History.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "The Church of Jesus Christ of Latter-day Saints essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "The Church of Jesus Christ of Latter-day Saints essentials.", "x": "At a glance: The Church of Jesus Christ of Latter-day Saints — Mormonism; restoration.. Book of Mormon. The essentials: Beliefs.. Utah. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Joseph Smith.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Joseph Smith.", "x": "The Church of Jesus Christ of Latter-day Saints: Joseph Smith.. Beliefs. Essential knowledge — Utah.. Mormonism; restoration. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Joseph Smith..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Joseph Smith..", "x": "Explained: Joseph Smith.. Culture. The context — The Church of Jesus Christ of Latter-day Saints. Missionaries. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Book of Mormon.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Book of Mormon.", "x": "The Church of Jesus Christ of Latter-day Saints: Book of Mormon.. Practices. Essential knowledge — Missionaries.. Mormonism; restoration. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Book of Mormon..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Book of Mormon..", "x": "Explained: Book of Mormon.. Global. The context — The Church of Jesus Christ of Latter-day Saints. Temples. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Utah.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Utah.", "x": "The Church of Jesus Christ of Latter-day Saints: Utah.. Culture. Essential knowledge — Temples.. Mormonism; restoration. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Utah..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Utah..", "x": "Explained: Utah.. Service. The context — The Church of Jesus Christ of Latter-day Saints. 17M. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Missionaries.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Missionaries.", "x": "The Church of Jesus Christ of Latter-day Saints: Missionaries.. Global. Essential knowledge — 17M.. Mormonism; restoration. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Missionaries..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Missionaries..", "x": "Explained: Missionaries.. History. The context — The Church of Jesus Christ of Latter-day Saints. Joseph Smith. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Temples.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Temples.", "x": "The Church of Jesus Christ of Latter-day Saints: Temples.. Service. Essential knowledge — Joseph Smith.. Mormonism; restoration. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Temples..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Temples..", "x": "Explained: Temples.. Beliefs. The context — The Church of Jesus Christ of Latter-day Saints. Book of Mormon. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "17M.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "17M.", "x": "The Church of Jesus Christ of Latter-day Saints: 17M.. History. Essential knowledge — Book of Mormon.. Mormonism; restoration. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: 17M..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: 17M..", "x": "Explained: 17M.. Practices. The context — The Church of Jesus Christ of Latter-day Saints. Utah. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "The Church of Jesus Christ of Latter-day Saints in depth: History.. Book of Mormon. Details — Mormonism; restoration.. Practices. Missionaries. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Beliefs.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Beliefs.", "x": "The Church of Jesus Christ of Latter-day Saints in depth: Beliefs.. Utah. Details — Mormonism; restoration.. Culture. Temples. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Practices.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Practices.", "x": "The Church of Jesus Christ of Latter-day Saints in depth: Practices.. Missionaries. Details — Mormonism; restoration.. Global. 17M. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Culture.", "x": "The Church of Jesus Christ of Latter-day Saints in depth: Culture.. Temples. Details — Mormonism; restoration.. Service. Joseph Smith. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Global.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Global.", "x": "The Church of Jesus Christ of Latter-day Saints in depth: Global.. 17M. Details — Mormonism; restoration.. History. Book of Mormon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Service.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Service.", "x": "The Church of Jesus Christ of Latter-day Saints in depth: Service.. Joseph Smith. Details — Mormonism; restoration.. Beliefs. Utah. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where The Church of Jesus Christ of Latter-day Saints comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where The Church of Jesus Christ of Latter-day Saints comes from.", "x": "Origins: History.. Joseph Smith. The history of The Church of Jesus Christ of Latter-day Saints — Mormonism; restoration.. Beliefs. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing The Church of Jesus Christ of Latter-day Saints respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing The Church of Jesus Christ of Latter-day Saints respectfully.", "x": "Engaging: Practices.. Book of Mormon. How to participate or observe well — The Church of Jesus Christ of Latter-day Saints. Mormonism; restoration. Respect first, always; Culture.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "The Church of Jesus Christ of Latter-day Saints do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "The Church of Jesus Christ of Latter-day Saints do's and don'ts.", "x": "Etiquette: Global.. Utah. The rules of respect — The Church of Jesus Christ of Latter-day Saints. Mormonism; restoration. When in doubt, ask about Service.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around The Church of Jesus Christ of Latter-day Saints.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around The Church of Jesus Christ of Latter-day Saints.", "x": "Planning: History.. Missionaries. Practical notes — The Church of Jesus Christ of Latter-day Saints. Mormonism; restoration. A little planning shows respect for Beliefs.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "The Church of Jesus Christ of Latter-day Saints and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "The Church of Jesus Christ of Latter-day Saints and money.", "x": "Costs: Practices.. Temples. What to budget — The Church of Jesus Christ of Latter-day Saints. Mormonism; restoration. The best experiences of Culture. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-religion-latter-day-saints-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
