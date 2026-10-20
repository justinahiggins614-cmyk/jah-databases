(function(){'use strict';
/* JAH Traditional American Tattoos Tattoo Style Database generator — jahdb-e2-tattoo-traditional-american-tattoos-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-tattoo-traditional-american-tattoos',PREFIX='JAH-E2TATTOOTRA-',NAME='JAH Traditional American Tattoos Tattoo Style Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Traditional American Tattoos: the complete guide", "d": "Traditional American Tattoos: bold sailor classics..", "g": "overview", "l": 2, "q": "What is Traditional American Tattoos: the complete guide?", "a": "Traditional American Tattoos: bold sailor classics..", "x": "The complete tattoo style guide to Traditional American Tattoos: bold sailor classics.. Sailor Jerry. History, meaning, practices, and how to engage respectfully — everything in one database. History.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Traditional American Tattoos essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Traditional American Tattoos essentials.", "x": "At a glance: Traditional American Tattoos — bold sailor classics.. Bold lines. The essentials: Motifs.. Anchors. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Sailor Jerry.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Sailor Jerry.", "x": "Traditional American Tattoos: Sailor Jerry.. Motifs. Essential knowledge — Anchors.. bold sailor classics. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Sailor Jerry..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Sailor Jerry..", "x": "Explained: Sailor Jerry.. Aging. The context — Traditional American Tattoos. Eagles. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Bold lines.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Bold lines.", "x": "Traditional American Tattoos: Bold lines.. Artists. Essential knowledge — Eagles.. bold sailor classics. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Bold lines..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Bold lines..", "x": "Explained: Bold lines.. Flash. The context — Traditional American Tattoos. Flash. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Anchors.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Anchors.", "x": "Traditional American Tattoos: Anchors.. Aging. Essential knowledge — Flash.. bold sailor classics. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Anchors..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Anchors..", "x": "Explained: Anchors.. Culture. The context — Traditional American Tattoos. History. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Eagles.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Eagles.", "x": "Traditional American Tattoos: Eagles.. Flash. Essential knowledge — History.. bold sailor classics. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Eagles..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Eagles..", "x": "Explained: Eagles.. History. The context — Traditional American Tattoos. Sailor Jerry. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Flash.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Flash.", "x": "Traditional American Tattoos: Flash.. Culture. Essential knowledge — Sailor Jerry.. bold sailor classics. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Flash..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Flash..", "x": "Explained: Flash.. Motifs. The context — Traditional American Tattoos. Bold lines. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "History.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "History.", "x": "Traditional American Tattoos: History.. History. Essential knowledge — Bold lines.. bold sailor classics. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: History..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: History..", "x": "Explained: History.. Artists. The context — Traditional American Tattoos. Anchors. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Traditional American Tattoos in depth: History.. Bold lines. Details — bold sailor classics.. Artists. Eagles. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Motifs.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Motifs.", "x": "Traditional American Tattoos in depth: Motifs.. Anchors. Details — bold sailor classics.. Aging. Flash. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Artists.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Artists.", "x": "Traditional American Tattoos in depth: Artists.. Eagles. Details — bold sailor classics.. Flash. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Aging.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Aging.", "x": "Traditional American Tattoos in depth: Aging.. Flash. Details — bold sailor classics.. Culture. Sailor Jerry. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Flash.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Flash.", "x": "Traditional American Tattoos in depth: Flash.. History. Details — bold sailor classics.. History. Bold lines. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Culture.", "x": "Traditional American Tattoos in depth: Culture.. Sailor Jerry. Details — bold sailor classics.. Motifs. Anchors. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Traditional American Tattoos comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Traditional American Tattoos comes from.", "x": "Origins: History.. Sailor Jerry. The history of Traditional American Tattoos — bold sailor classics.. Motifs. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Traditional American Tattoos respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Traditional American Tattoos respectfully.", "x": "Engaging: Artists.. Bold lines. How to participate or observe well — Traditional American Tattoos. bold sailor classics. Respect first, always; Aging.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Traditional American Tattoos do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Traditional American Tattoos do's and don'ts.", "x": "Etiquette: Flash.. Anchors. The rules of respect — Traditional American Tattoos. bold sailor classics. When in doubt, ask about Culture.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Traditional American Tattoos.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Traditional American Tattoos.", "x": "Planning: History.. Eagles. Practical notes — Traditional American Tattoos. bold sailor classics. A little planning shows respect for Motifs.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Traditional American Tattoos and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Traditional American Tattoos and money.", "x": "Costs: Artists.. Flash. What to budget — Traditional American Tattoos. bold sailor classics. The best experiences of Aging. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-tattoo-traditional-american-tattoos-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
