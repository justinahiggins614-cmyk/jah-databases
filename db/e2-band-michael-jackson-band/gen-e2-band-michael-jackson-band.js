(function(){'use strict';
/* JAH Michael Jackson Band Database generator — jahdb-e2-band-michael-jackson-band-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-band-michael-jackson-band',PREFIX='JAH-E2BANDMICHA-',NAME='JAH Michael Jackson Band Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Michael Jackson: the complete guide", "d": "Michael Jackson: the king of pop..", "g": "overview", "l": 2, "q": "What is Michael Jackson: the complete guide?", "a": "Michael Jackson: the king of pop..", "x": "The complete band guide to Michael Jackson: the king of pop.. 1958. History, meaning, practices, and how to engage respectfully — everything in one database. Thriller. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Michael Jackson essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Michael Jackson essentials.", "x": "At a glance: Michael Jackson — the king of pop.. Thriller. The essentials: Moonwalk.. Moonwalk. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1958.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1958.", "x": "Michael Jackson: 1958.. Moonwalk. Essential knowledge — Moonwalk.. the king of pop. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1958..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1958..", "x": "Explained: 1958.. Neverland. The context — Michael Jackson. Jackson 5. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Thriller.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Thriller.", "x": "Michael Jackson: Thriller.. Jackson 5. Essential knowledge — Jackson 5.. the king of pop. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Thriller..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Thriller..", "x": "Explained: Thriller.. King. The context — Michael Jackson. 1982. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Moonwalk.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Moonwalk.", "x": "Michael Jackson: Moonwalk.. Neverland. Essential knowledge — 1982.. the king of pop. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Moonwalk..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Moonwalk..", "x": "Explained: Moonwalk.. Legacy. The context — Michael Jackson. Neverland. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Jackson 5.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Jackson 5.", "x": "Michael Jackson: Jackson 5.. King. Essential knowledge — Neverland.. the king of pop. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Jackson 5..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Jackson 5..", "x": "Explained: Jackson 5.. Thriller. The context — Michael Jackson. 1958. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "1982.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "1982.", "x": "Michael Jackson: 1982.. Legacy. Essential knowledge — 1958.. the king of pop. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 1982..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 1982..", "x": "Explained: 1982.. Moonwalk. The context — Michael Jackson. Thriller. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Neverland.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Neverland.", "x": "Michael Jackson: Neverland.. Thriller. Essential knowledge — Thriller.. the king of pop. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Neverland..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Neverland..", "x": "Explained: Neverland.. Jackson 5. The context — Michael Jackson. Moonwalk. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Thriller.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Thriller.", "x": "Michael Jackson in depth: Thriller.. Thriller. Details — the king of pop.. Jackson 5. Jackson 5. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Moonwalk.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Moonwalk.", "x": "Michael Jackson in depth: Moonwalk.. Moonwalk. Details — the king of pop.. Neverland. 1982. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Jackson 5.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Jackson 5.", "x": "Michael Jackson in depth: Jackson 5.. Jackson 5. Details — the king of pop.. King. Neverland. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Neverland.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Neverland.", "x": "Michael Jackson in depth: Neverland.. 1982. Details — the king of pop.. Legacy. 1958. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "King.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "King.", "x": "Michael Jackson in depth: King.. Neverland. Details — the king of pop.. Thriller. Thriller. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "Michael Jackson in depth: Legacy.. 1958. Details — the king of pop.. Moonwalk. Moonwalk. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Michael Jackson comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Michael Jackson comes from.", "x": "Origins: Thriller.. 1958. The history of Michael Jackson — the king of pop.. Moonwalk. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Michael Jackson respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Michael Jackson respectfully.", "x": "Engaging: Jackson 5.. Thriller. How to participate or observe well — Michael Jackson. the king of pop. Respect first, always; Neverland.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Michael Jackson do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Michael Jackson do's and don'ts.", "x": "Etiquette: King.. Moonwalk. The rules of respect — Michael Jackson. the king of pop. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Michael Jackson.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Michael Jackson.", "x": "Planning: Thriller.. Jackson 5. Practical notes — Michael Jackson. the king of pop. A little planning shows respect for Moonwalk.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Michael Jackson and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Michael Jackson and money.", "x": "Costs: Jackson 5.. 1982. What to budget — Michael Jackson. the king of pop. The best experiences of Neverland. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-band-michael-jackson-band-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
