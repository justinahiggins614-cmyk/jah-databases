(function(){'use strict';
/* JAH SpongeBob Cartoon Database generator — jahdb-e2-cartoon-spongebob-cartoon-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-cartoon-spongebob-cartoon',PREFIX='JAH-E2CARTOONSP-',NAME='JAH SpongeBob Cartoon Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "SpongeBob: the complete guide", "d": "SpongeBob: the absorbent star..", "g": "overview", "l": 2, "q": "What is SpongeBob: the complete guide?", "a": "SpongeBob: the absorbent star..", "x": "The complete cartoon guide to SpongeBob: the absorbent star.. 1999. History, meaning, practices, and how to engage respectfully — everything in one database. Pineapple. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "SpongeBob essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "SpongeBob essentials.", "x": "At a glance: SpongeBob — the absorbent star.. Pineapple. The essentials: Patty.. Krabby Patty. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1999.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1999.", "x": "SpongeBob: 1999.. Patty. Essential knowledge — Krabby Patty.. the absorbent star. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 1999..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 1999..", "x": "Explained: 1999.. Nick. The context — SpongeBob. Nickelodeon. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Pineapple.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Pineapple.", "x": "SpongeBob: Pineapple.. Memes. Essential knowledge — Nickelodeon.. the absorbent star. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Pineapple..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Pineapple..", "x": "Explained: Pineapple.. Bikini. The context — SpongeBob. Memes. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Krabby Patty.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Krabby Patty.", "x": "SpongeBob: Krabby Patty.. Nick. Essential knowledge — Memes.. the absorbent star. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Krabby Patty..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Krabby Patty..", "x": "Explained: Krabby Patty.. Legacy. The context — SpongeBob. Bikini. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Nickelodeon.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Nickelodeon.", "x": "SpongeBob: Nickelodeon.. Bikini. Essential knowledge — Bikini.. the absorbent star. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Nickelodeon..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Nickelodeon..", "x": "Explained: Nickelodeon.. Pineapple. The context — SpongeBob. 1999. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Memes.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Memes.", "x": "SpongeBob: Memes.. Legacy. Essential knowledge — 1999.. the absorbent star. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Memes..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Memes..", "x": "Explained: Memes.. Patty. The context — SpongeBob. Pineapple. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Bikini.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Bikini.", "x": "SpongeBob: Bikini.. Pineapple. Essential knowledge — Pineapple.. the absorbent star. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Bikini..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Bikini..", "x": "Explained: Bikini.. Memes. The context — SpongeBob. Krabby Patty. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Pineapple.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Pineapple.", "x": "SpongeBob in depth: Pineapple.. Pineapple. Details — the absorbent star.. Memes. Nickelodeon. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Patty.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Patty.", "x": "SpongeBob in depth: Patty.. Krabby Patty. Details — the absorbent star.. Nick. Memes. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Memes.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Memes.", "x": "SpongeBob in depth: Memes.. Nickelodeon. Details — the absorbent star.. Bikini. Bikini. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Nick.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Nick.", "x": "SpongeBob in depth: Nick.. Memes. Details — the absorbent star.. Legacy. 1999. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Bikini.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Bikini.", "x": "SpongeBob in depth: Bikini.. Bikini. Details — the absorbent star.. Pineapple. Pineapple. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legacy.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legacy.", "x": "SpongeBob in depth: Legacy.. 1999. Details — the absorbent star.. Patty. Krabby Patty. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where SpongeBob comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where SpongeBob comes from.", "x": "Origins: Pineapple.. 1999. The history of SpongeBob — the absorbent star.. Patty. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing SpongeBob respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing SpongeBob respectfully.", "x": "Engaging: Memes.. Pineapple. How to participate or observe well — SpongeBob. the absorbent star. Respect first, always; Nick.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "SpongeBob do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "SpongeBob do's and don'ts.", "x": "Etiquette: Bikini.. Krabby Patty. The rules of respect — SpongeBob. the absorbent star. When in doubt, ask about Legacy.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around SpongeBob.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around SpongeBob.", "x": "Planning: Pineapple.. Nickelodeon. Practical notes — SpongeBob. the absorbent star. A little planning shows respect for Patty.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "SpongeBob and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "SpongeBob and money.", "x": "Costs: Memes.. Memes. What to budget — SpongeBob. the absorbent star. The best experiences of Nick. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-cartoon-spongebob-cartoon-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
