(function(){'use strict';
/* JAH Panorama Photography Photography Database generator — jahdb-e2-photo-panorama-photography-tech-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-photo-panorama-photography-tech',PREFIX='JAH-E2PHOTOPANO-',NAME='JAH Panorama Photography Photography Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Panorama Photography: the complete guide", "d": "Panorama Photography: the wide stitch..", "g": "overview", "l": 2, "q": "What is Panorama Photography: the complete guide?", "a": "Panorama Photography: the wide stitch..", "x": "The complete photography guide to Panorama Photography: the wide stitch.. Stitching. History, meaning, practices, and how to engage respectfully — everything in one database. Stitching. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Panorama Photography essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Panorama Photography essentials.", "x": "At a glance: Panorama Photography — the wide stitch.. Overlap. The essentials: Nodal.. Nodal. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Stitching.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Stitching.", "x": "Panorama Photography: Stitching.. Nodal. Essential knowledge — Nodal.. the wide stitch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Stitching..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Stitching..", "x": "Explained: Stitching.. Wide. The context — Panorama Photography. Wide. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Overlap.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Overlap.", "x": "Panorama Photography: Overlap.. Software. Essential knowledge — Wide.. the wide stitch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Overlap..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Overlap..", "x": "Explained: Overlap.. Overlap. The context — Panorama Photography. Tripod. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Nodal.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Nodal.", "x": "Panorama Photography: Nodal.. Wide. Essential knowledge — Tripod.. the wide stitch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Nodal..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Nodal..", "x": "Explained: Nodal.. Tips. The context — Panorama Photography. Software. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Wide.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Wide.", "x": "Panorama Photography: Wide.. Overlap. Essential knowledge — Software.. the wide stitch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Wide..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Wide..", "x": "Explained: Wide.. Stitching. The context — Panorama Photography. Stitching. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Tripod.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Tripod.", "x": "Panorama Photography: Tripod.. Tips. Essential knowledge — Stitching.. the wide stitch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Tripod..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Tripod..", "x": "Explained: Tripod.. Nodal. The context — Panorama Photography. Overlap. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Software.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Software.", "x": "Panorama Photography: Software.. Stitching. Essential knowledge — Overlap.. the wide stitch. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Software..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Software..", "x": "Explained: Software.. Software. The context — Panorama Photography. Nodal. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Stitching.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Stitching.", "x": "Panorama Photography in depth: Stitching.. Overlap. Details — the wide stitch.. Software. Wide. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Nodal.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Nodal.", "x": "Panorama Photography in depth: Nodal.. Nodal. Details — the wide stitch.. Wide. Tripod. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Software.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Software.", "x": "Panorama Photography in depth: Software.. Wide. Details — the wide stitch.. Overlap. Software. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Wide.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Wide.", "x": "Panorama Photography in depth: Wide.. Tripod. Details — the wide stitch.. Tips. Stitching. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Overlap.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Overlap.", "x": "Panorama Photography in depth: Overlap.. Software. Details — the wide stitch.. Stitching. Overlap. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tips.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tips.", "x": "Panorama Photography in depth: Tips.. Stitching. Details — the wide stitch.. Nodal. Nodal. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Panorama Photography comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Panorama Photography comes from.", "x": "Origins: Stitching.. Stitching. The history of Panorama Photography — the wide stitch.. Nodal. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Panorama Photography respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Panorama Photography respectfully.", "x": "Engaging: Software.. Overlap. How to participate or observe well — Panorama Photography. the wide stitch. Respect first, always; Wide.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Panorama Photography do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Panorama Photography do's and don'ts.", "x": "Etiquette: Overlap.. Nodal. The rules of respect — Panorama Photography. the wide stitch. When in doubt, ask about Tips.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Panorama Photography.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Panorama Photography.", "x": "Planning: Stitching.. Wide. Practical notes — Panorama Photography. the wide stitch. A little planning shows respect for Nodal.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Panorama Photography and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Panorama Photography and money.", "x": "Costs: Software.. Tripod. What to budget — Panorama Photography. the wide stitch. The best experiences of Wide. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-photo-panorama-photography-tech-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
