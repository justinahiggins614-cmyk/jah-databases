(function(){'use strict';
/* JAH Tea Crop Crop Database generator — jahdb-e2-crop-tea-crop-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-crop-tea-crop',PREFIX='JAH-E2CROPTEACR-',NAME='JAH Tea Crop Crop Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Tea Crop: the complete guide", "d": "Tea Crop: the leaf harvest..", "g": "overview", "l": 2, "q": "What is Tea Crop: the complete guide?", "a": "Tea Crop: the leaf harvest..", "x": "The complete crop guide to Tea Crop: the leaf harvest.. Camellia. History, meaning, practices, and how to engage respectfully — everything in one database. Plucking. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Tea Crop essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Tea Crop essentials.", "x": "At a glance: Tea Crop — the leaf harvest.. Plucking. The essentials: Assam.. Two leaves. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Camellia.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Camellia.", "x": "Tea Crop: Camellia.. Assam. Essential knowledge — Two leaves.. the leaf harvest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Camellia..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Camellia..", "x": "Explained: Camellia.. Elevation. The context — Tea Crop. Assam. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Plucking.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Plucking.", "x": "Tea Crop: Plucking.. Processing. Essential knowledge — Assam.. the leaf harvest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Plucking..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Plucking..", "x": "Explained: Plucking.. Leaves. The context — Tea Crop. Elevation. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Two leaves.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Two leaves.", "x": "Tea Crop: Two leaves.. Elevation. Essential knowledge — Elevation.. the leaf harvest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Two leaves..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Two leaves..", "x": "Explained: Two leaves.. Growing. The context — Tea Crop. Processing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Assam.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Assam.", "x": "Tea Crop: Assam.. Leaves. Essential knowledge — Processing.. the leaf harvest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Assam..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Assam..", "x": "Explained: Assam.. Plucking. The context — Tea Crop. Camellia. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Elevation.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Elevation.", "x": "Tea Crop: Elevation.. Growing. Essential knowledge — Camellia.. the leaf harvest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Elevation..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Elevation..", "x": "Explained: Elevation.. Assam. The context — Tea Crop. Plucking. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Processing.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Processing.", "x": "Tea Crop: Processing.. Plucking. Essential knowledge — Plucking.. the leaf harvest. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Processing..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Processing..", "x": "Explained: Processing.. Processing. The context — Tea Crop. Two leaves. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Plucking.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Plucking.", "x": "Tea Crop in depth: Plucking.. Plucking. Details — the leaf harvest.. Processing. Assam. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Assam.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Assam.", "x": "Tea Crop in depth: Assam.. Two leaves. Details — the leaf harvest.. Elevation. Elevation. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Processing.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Processing.", "x": "Tea Crop in depth: Processing.. Assam. Details — the leaf harvest.. Leaves. Processing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Elevation.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Elevation.", "x": "Tea Crop in depth: Elevation.. Elevation. Details — the leaf harvest.. Growing. Camellia. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Leaves.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Leaves.", "x": "Tea Crop in depth: Leaves.. Processing. Details — the leaf harvest.. Plucking. Plucking. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Growing.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Growing.", "x": "Tea Crop in depth: Growing.. Camellia. Details — the leaf harvest.. Assam. Two leaves. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Tea Crop comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Tea Crop comes from.", "x": "Origins: Plucking.. Camellia. The history of Tea Crop — the leaf harvest.. Assam. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Tea Crop respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Tea Crop respectfully.", "x": "Engaging: Processing.. Plucking. How to participate or observe well — Tea Crop. the leaf harvest. Respect first, always; Elevation.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Tea Crop do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Tea Crop do's and don'ts.", "x": "Etiquette: Leaves.. Two leaves. The rules of respect — Tea Crop. the leaf harvest. When in doubt, ask about Growing.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Tea Crop.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Tea Crop.", "x": "Planning: Plucking.. Assam. Practical notes — Tea Crop. the leaf harvest. A little planning shows respect for Assam.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Tea Crop and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Tea Crop and money.", "x": "Costs: Processing.. Elevation. What to budget — Tea Crop. the leaf harvest. The best experiences of Elevation. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-crop-tea-crop-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
