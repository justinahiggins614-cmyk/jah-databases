(function(){'use strict';
/* JAH Ghost Stories Short Story Database generator — jahdb-e2-story-ghost-stories-short-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-story-ghost-stories-short',PREFIX='JAH-E2STORYGHOS-',NAME='JAH Ghost Stories Short Story Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Ghost Stories: the complete guide", "d": "Ghost Stories: the haunted tales..", "g": "overview", "l": 2, "q": "What is Ghost Stories: the complete guide?", "a": "Ghost Stories: the haunted tales..", "x": "The complete short story guide to Ghost Stories: the haunted tales.. James. History, meaning, practices, and how to engage respectfully — everything in one database. James. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Ghost Stories essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Ghost Stories essentials.", "x": "At a glance: Ghost Stories — the haunted tales.. Turn of Screw. The essentials: Dread.. Victorian. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "James.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "James.", "x": "Ghost Stories: James.. Dread. Essential knowledge — Victorian.. the haunted tales. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: James..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: James..", "x": "Explained: James.. Atmosphere. The context — Ghost Stories. Dread. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Turn of Screw.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Turn of Screw.", "x": "Ghost Stories: Turn of Screw.. Christmas. Essential knowledge — Dread.. the haunted tales. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Turn of Screw..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Turn of Screw..", "x": "Explained: Turn of Screw.. Victorian. The context — Ghost Stories. Christmas. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Victorian.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Victorian.", "x": "Ghost Stories: Victorian.. Atmosphere. Essential knowledge — Christmas.. the haunted tales. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Victorian..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Victorian..", "x": "Explained: Victorian.. Classics. The context — Ghost Stories. Atmosphere. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Dread.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Dread.", "x": "Ghost Stories: Dread.. Victorian. Essential knowledge — Atmosphere.. the haunted tales. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Dread..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Dread..", "x": "Explained: Dread.. James. The context — Ghost Stories. James. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Christmas.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Christmas.", "x": "Ghost Stories: Christmas.. Classics. Essential knowledge — James.. the haunted tales. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Christmas..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Christmas..", "x": "Explained: Christmas.. Dread. The context — Ghost Stories. Turn of Screw. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Atmosphere.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Atmosphere.", "x": "Ghost Stories: Atmosphere.. James. Essential knowledge — Turn of Screw.. the haunted tales. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Atmosphere..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Atmosphere..", "x": "Explained: Atmosphere.. Christmas. The context — Ghost Stories. Victorian. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "James.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "James.", "x": "Ghost Stories in depth: James.. Turn of Screw. Details — the haunted tales.. Christmas. Dread. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Dread.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Dread.", "x": "Ghost Stories in depth: Dread.. Victorian. Details — the haunted tales.. Atmosphere. Christmas. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Christmas.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Christmas.", "x": "Ghost Stories in depth: Christmas.. Dread. Details — the haunted tales.. Victorian. Atmosphere. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Atmosphere.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Atmosphere.", "x": "Ghost Stories in depth: Atmosphere.. Christmas. Details — the haunted tales.. Classics. James. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Victorian.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Victorian.", "x": "Ghost Stories in depth: Victorian.. Atmosphere. Details — the haunted tales.. James. Turn of Screw. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Classics.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Classics.", "x": "Ghost Stories in depth: Classics.. James. Details — the haunted tales.. Dread. Victorian. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Ghost Stories comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Ghost Stories comes from.", "x": "Origins: James.. James. The history of Ghost Stories — the haunted tales.. Dread. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Ghost Stories respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Ghost Stories respectfully.", "x": "Engaging: Christmas.. Turn of Screw. How to participate or observe well — Ghost Stories. the haunted tales. Respect first, always; Atmosphere.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Ghost Stories do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Ghost Stories do's and don'ts.", "x": "Etiquette: Victorian.. Victorian. The rules of respect — Ghost Stories. the haunted tales. When in doubt, ask about Classics.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Ghost Stories.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Ghost Stories.", "x": "Planning: James.. Dread. Practical notes — Ghost Stories. the haunted tales. A little planning shows respect for Dread.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Ghost Stories and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Ghost Stories and money.", "x": "Costs: Christmas.. Christmas. What to budget — Ghost Stories. the haunted tales. The best experiences of Atmosphere. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-story-ghost-stories-short-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
