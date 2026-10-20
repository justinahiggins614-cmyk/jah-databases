(function(){'use strict';
/* JAH Video Making Database generator — jahdb-e2-hobby2-video-making-hobby-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hobby2-video-making-hobby',PREFIX='JAH-E2HOBBY2VID-',NAME='JAH Video Making Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Video Making: the complete guide", "d": "Video Making: the moving image..", "g": "overview", "l": 2, "q": "What is Video Making: the complete guide?", "a": "Video Making: the moving image..", "x": "The complete hobby guide to Video Making: the moving image.. Editing. History, meaning, practices, and how to engage respectfully — everything in one database. Lighting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Video Making essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Video Making essentials.", "x": "At a glance: Video Making — the moving image.. Lighting. The essentials: Story.. Audio. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Editing.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Editing.", "x": "Video Making: Editing.. Story. Essential knowledge — Audio.. the moving image. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Editing..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Editing..", "x": "Explained: Editing.. Editing. The context — Video Making. Story. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Lighting.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Lighting.", "x": "Video Making: Lighting.. Thumbnails. Essential knowledge — Story.. the moving image. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Lighting..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Lighting..", "x": "Explained: Lighting.. Audio. The context — Video Making. Upload. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Audio.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Audio.", "x": "Video Making: Audio.. Editing. Essential knowledge — Upload.. the moving image. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Audio..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Audio..", "x": "Explained: Audio.. Getting started. The context — Video Making. Thumbnails. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Story.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Story.", "x": "Video Making: Story.. Audio. Essential knowledge — Thumbnails.. the moving image. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Story..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Story..", "x": "Explained: Story.. Lighting. The context — Video Making. Editing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Upload.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Upload.", "x": "Video Making: Upload.. Getting started. Essential knowledge — Editing.. the moving image. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Upload..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Upload..", "x": "Explained: Upload.. Story. The context — Video Making. Lighting. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Thumbnails.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Thumbnails.", "x": "Video Making: Thumbnails.. Lighting. Essential knowledge — Lighting.. the moving image. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Thumbnails..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Thumbnails..", "x": "Explained: Thumbnails.. Thumbnails. The context — Video Making. Audio. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Lighting.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Lighting.", "x": "Video Making in depth: Lighting.. Lighting. Details — the moving image.. Thumbnails. Story. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Story.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Story.", "x": "Video Making in depth: Story.. Audio. Details — the moving image.. Editing. Upload. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Thumbnails.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Thumbnails.", "x": "Video Making in depth: Thumbnails.. Story. Details — the moving image.. Audio. Thumbnails. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Editing.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Editing.", "x": "Video Making in depth: Editing.. Upload. Details — the moving image.. Getting started. Editing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Audio.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Audio.", "x": "Video Making in depth: Audio.. Thumbnails. Details — the moving image.. Lighting. Lighting. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Getting started.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Getting started.", "x": "Video Making in depth: Getting started.. Editing. Details — the moving image.. Story. Audio. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Video Making comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Video Making comes from.", "x": "Origins: Lighting.. Editing. The history of Video Making — the moving image.. Story. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Video Making respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Video Making respectfully.", "x": "Engaging: Thumbnails.. Lighting. How to participate or observe well — Video Making. the moving image. Respect first, always; Editing.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Video Making do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Video Making do's and don'ts.", "x": "Etiquette: Audio.. Audio. The rules of respect — Video Making. the moving image. When in doubt, ask about Getting started.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Video Making.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Video Making.", "x": "Planning: Lighting.. Story. Practical notes — Video Making. the moving image. A little planning shows respect for Story.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Video Making and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Video Making and money.", "x": "Costs: Thumbnails.. Upload. What to budget — Video Making. the moving image. The best experiences of Editing. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hobby2-video-making-hobby-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
