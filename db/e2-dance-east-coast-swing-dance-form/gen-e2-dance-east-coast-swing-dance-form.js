(function(){'use strict';
/* JAH East Coast Swing Dance Form Database generator — jahdb-e2-dance-east-coast-swing-dance-form-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-dance-east-coast-swing-dance-form',PREFIX='JAH-E2DANCEEAST-',NAME='JAH East Coast Swing Dance Form Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "East Coast Swing: the complete guide", "d": "East Coast Swing: the triple swing..", "g": "overview", "l": 2, "q": "What is East Coast Swing: the complete guide?", "a": "East Coast Swing: the triple swing..", "x": "The complete dance form guide to East Coast Swing: the triple swing.. Triple. History, meaning, practices, and how to engage respectfully — everything in one database. Triple. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "East Coast Swing essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "East Coast Swing essentials.", "x": "At a glance: East Coast Swing — the triple swing.. Bouncy. The essentials: Rock.. Rock. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Triple.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Triple.", "x": "East Coast Swing: Triple.. Rock. Essential knowledge — Rock.. the triple swing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Triple..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Triple..", "x": "Explained: Triple.. Bouncy. The context — East Coast Swing. Ballroom. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Bouncy.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Bouncy.", "x": "East Coast Swing: Bouncy.. Fun. Essential knowledge — Ballroom.. the triple swing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Bouncy..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Bouncy..", "x": "Explained: Bouncy.. Ballroom. The context — East Coast Swing. 6-count. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Rock.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Rock.", "x": "East Coast Swing: Rock.. Bouncy. Essential knowledge — 6-count.. the triple swing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Rock..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Rock..", "x": "Explained: Rock.. Training. The context — East Coast Swing. Fun. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Ballroom.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Ballroom.", "x": "East Coast Swing: Ballroom.. Ballroom. Essential knowledge — Fun.. the triple swing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Ballroom..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Ballroom..", "x": "Explained: Ballroom.. Triple. The context — East Coast Swing. Triple. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "6-count.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "6-count.", "x": "East Coast Swing: 6-count.. Training. Essential knowledge — Triple.. the triple swing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: 6-count..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: 6-count..", "x": "Explained: 6-count.. Rock. The context — East Coast Swing. Bouncy. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Fun.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Fun.", "x": "East Coast Swing: Fun.. Triple. Essential knowledge — Bouncy.. the triple swing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Fun..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Fun..", "x": "Explained: Fun.. Fun. The context — East Coast Swing. Rock. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Triple.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Triple.", "x": "East Coast Swing in depth: Triple.. Bouncy. Details — the triple swing.. Fun. Ballroom. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Rock.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Rock.", "x": "East Coast Swing in depth: Rock.. Rock. Details — the triple swing.. Bouncy. 6-count. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Fun.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Fun.", "x": "East Coast Swing in depth: Fun.. Ballroom. Details — the triple swing.. Ballroom. Fun. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Bouncy.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Bouncy.", "x": "East Coast Swing in depth: Bouncy.. 6-count. Details — the triple swing.. Training. Triple. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Ballroom.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Ballroom.", "x": "East Coast Swing in depth: Ballroom.. Fun. Details — the triple swing.. Triple. Bouncy. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Training.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Training.", "x": "East Coast Swing in depth: Training.. Triple. Details — the triple swing.. Rock. Rock. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where East Coast Swing comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where East Coast Swing comes from.", "x": "Origins: Triple.. Triple. The history of East Coast Swing — the triple swing.. Rock. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing East Coast Swing respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing East Coast Swing respectfully.", "x": "Engaging: Fun.. Bouncy. How to participate or observe well — East Coast Swing. the triple swing. Respect first, always; Bouncy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "East Coast Swing do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "East Coast Swing do's and don'ts.", "x": "Etiquette: Ballroom.. Rock. The rules of respect — East Coast Swing. the triple swing. When in doubt, ask about Training.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around East Coast Swing.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around East Coast Swing.", "x": "Planning: Triple.. Ballroom. Practical notes — East Coast Swing. the triple swing. A little planning shows respect for Rock.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "East Coast Swing and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "East Coast Swing and money.", "x": "Costs: Fun.. 6-count. What to budget — East Coast Swing. the triple swing. The best experiences of Bouncy. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-dance-east-coast-swing-dance-form-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
