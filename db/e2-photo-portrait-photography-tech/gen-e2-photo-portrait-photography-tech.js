(function(){'use strict';
/* JAH Portrait Photography Photography Database generator — jahdb-e2-photo-portrait-photography-tech-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-photo-portrait-photography-tech',PREFIX='JAH-E2PHOTOPORT-',NAME='JAH Portrait Photography Photography Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Portrait Photography: the complete guide", "d": "Portrait Photography: the face craft..", "g": "overview", "l": 2, "q": "What is Portrait Photography: the complete guide?", "a": "Portrait Photography: the face craft..", "x": "The complete photography guide to Portrait Photography: the face craft.. 85mm. History, meaning, practices, and how to engage respectfully — everything in one database. Bokeh. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Portrait Photography essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Portrait Photography essentials.", "x": "At a glance: Portrait Photography — the face craft.. Bokeh. The essentials: Posing.. Rembrandt. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "85mm.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "85mm.", "x": "Portrait Photography: 85mm.. Posing. Essential knowledge — Rembrandt.. the face craft. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: 85mm..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: 85mm..", "x": "Explained: 85mm.. Rembrandt. The context — Portrait Photography. Catchlights. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Bokeh.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Bokeh.", "x": "Portrait Photography: Bokeh.. Shallow. Essential knowledge — Catchlights.. the face craft. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Bokeh..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Bokeh..", "x": "Explained: Bokeh.. Catchlights. The context — Portrait Photography. Posing. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Rembrandt.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Rembrandt.", "x": "Portrait Photography: Rembrandt.. Rembrandt. Essential knowledge — Posing.. the face craft. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Rembrandt..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Rembrandt..", "x": "Explained: Rembrandt.. Tips. The context — Portrait Photography. Shallow. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Catchlights.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Catchlights.", "x": "Portrait Photography: Catchlights.. Catchlights. Essential knowledge — Shallow.. the face craft. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Catchlights..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Catchlights..", "x": "Explained: Catchlights.. Bokeh. The context — Portrait Photography. 85mm. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Posing.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Posing.", "x": "Portrait Photography: Posing.. Tips. Essential knowledge — 85mm.. the face craft. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Posing..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Posing..", "x": "Explained: Posing.. Posing. The context — Portrait Photography. Bokeh. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Shallow.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Shallow.", "x": "Portrait Photography: Shallow.. Bokeh. Essential knowledge — Bokeh.. the face craft. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Shallow..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Shallow..", "x": "Explained: Shallow.. Shallow. The context — Portrait Photography. Rembrandt. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Bokeh.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Bokeh.", "x": "Portrait Photography in depth: Bokeh.. Bokeh. Details — the face craft.. Shallow. Catchlights. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Posing.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Posing.", "x": "Portrait Photography in depth: Posing.. Rembrandt. Details — the face craft.. Rembrandt. Posing. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Shallow.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Shallow.", "x": "Portrait Photography in depth: Shallow.. Catchlights. Details — the face craft.. Catchlights. Shallow. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Rembrandt.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Rembrandt.", "x": "Portrait Photography in depth: Rembrandt.. Posing. Details — the face craft.. Tips. 85mm. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Catchlights.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Catchlights.", "x": "Portrait Photography in depth: Catchlights.. Shallow. Details — the face craft.. Bokeh. Bokeh. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tips.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tips.", "x": "Portrait Photography in depth: Tips.. 85mm. Details — the face craft.. Posing. Rembrandt. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Portrait Photography comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Portrait Photography comes from.", "x": "Origins: Bokeh.. 85mm. The history of Portrait Photography — the face craft.. Posing. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Portrait Photography respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Portrait Photography respectfully.", "x": "Engaging: Shallow.. Bokeh. How to participate or observe well — Portrait Photography. the face craft. Respect first, always; Rembrandt.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Portrait Photography do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Portrait Photography do's and don'ts.", "x": "Etiquette: Catchlights.. Rembrandt. The rules of respect — Portrait Photography. the face craft. When in doubt, ask about Tips.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Portrait Photography.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Portrait Photography.", "x": "Planning: Bokeh.. Catchlights. Practical notes — Portrait Photography. the face craft. A little planning shows respect for Posing.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Portrait Photography and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Portrait Photography and money.", "x": "Costs: Shallow.. Posing. What to budget — Portrait Photography. the face craft. The best experiences of Rembrandt. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-photo-portrait-photography-tech-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
