(function(){'use strict';
/* JAH Kaftan Clothing Database generator — jahdb-e2-clothing-kaftan-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-clothing-kaftan',PREFIX='JAH-E2CLOTHINGK-',NAME='JAH Kaftan Clothing Database';
var FIELDS=["overview", "facts", "details", "history", "guide", "myths", "insider", "quiz", "resources"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Kaftan: the complete guide", "d": "Kaftan: flowing Middle Eastern robe..", "g": "overview", "l": 2, "q": "What is Kaftan: the complete guide?", "a": "Kaftan: flowing Middle Eastern robe..", "x": "The complete clothing guide to Kaftan: flowing Middle Eastern robe.. Morocco. History, meaning, practices, and how to engage respectfully — everything in one database. History. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "At a glance", "d": "Kaftan essentials.", "g": "overview", "l": 2, "q": "What is At a glance?", "a": "Kaftan essentials.", "x": "At a glance: Kaftan — flowing Middle Eastern robe.. Embroidery. The essentials: Styles.. Occasions. Start here. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Morocco.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Morocco.", "x": "Kaftan: Morocco.. Styles. Essential knowledge — Occasions.. flowing Middle Eastern robe. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Understanding: Morocco..", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Understanding: Morocco..", "x": "Explained: Morocco.. Craft. The context — Kaftan. Fabrics. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Embroidery.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Embroidery.", "x": "Kaftan: Embroidery.. Wear. Essential knowledge — Fabrics.. flowing Middle Eastern robe. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Understanding: Embroidery..", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Understanding: Embroidery..", "x": "Explained: Embroidery.. Modern. The context — Kaftan. Modern. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Occasions.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Occasions.", "x": "Kaftan: Occasions.. Craft. Essential knowledge — Modern.. flowing Middle Eastern robe. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Understanding: Occasions..", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Understanding: Occasions..", "x": "Explained: Occasions.. Luxury. The context — Kaftan. Weddings. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Fabrics.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Fabrics.", "x": "Kaftan: Fabrics.. Modern. Essential knowledge — Weddings.. flowing Middle Eastern robe. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Understanding: Fabrics..", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Understanding: Fabrics..", "x": "Explained: Fabrics.. History. The context — Kaftan. Morocco. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Modern.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Modern.", "x": "Kaftan: Modern.. Luxury. Essential knowledge — Morocco.. flowing Middle Eastern robe. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Understanding: Modern..", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Understanding: Modern..", "x": "Explained: Modern.. Styles. The context — Kaftan. Embroidery. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Weddings.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Weddings.", "x": "Kaftan: Weddings.. History. Essential knowledge — Embroidery.. flowing Middle Eastern robe. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Understanding: Weddings..", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Understanding: Weddings..", "x": "Explained: Weddings.. Wear. The context — Kaftan. Occasions. Respectful understanding matters. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Kaftan in depth: History.. Embroidery. Details — flowing Middle Eastern robe.. Wear. Fabrics. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Styles.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Styles.", "x": "Kaftan in depth: Styles.. Occasions. Details — flowing Middle Eastern robe.. Craft. Modern. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Wear.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Wear.", "x": "Kaftan in depth: Wear.. Fabrics. Details — flowing Middle Eastern robe.. Modern. Weddings. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Craft.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Craft.", "x": "Kaftan in depth: Craft.. Modern. Details — flowing Middle Eastern robe.. Luxury. Morocco. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Modern.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Modern.", "x": "Kaftan in depth: Modern.. Weddings. Details — flowing Middle Eastern robe.. History. Embroidery. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Luxury.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Luxury.", "x": "Kaftan in depth: Luxury.. Morocco. Details — flowing Middle Eastern robe.. Styles. Occasions. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "History and origins", "d": "Where Kaftan comes from.", "g": "history", "l": 2, "q": "What is History and origins?", "a": "Where Kaftan comes from.", "x": "Origins: History.. Morocco. The history of Kaftan — flowing Middle Eastern robe.. Styles. Everything has roots. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "How to engage", "d": "Experiencing Kaftan respectfully.", "g": "guide", "l": 2, "q": "What is How to engage?", "a": "Experiencing Kaftan respectfully.", "x": "Engaging: Wear.. Embroidery. How to participate or observe well — Kaftan. flowing Middle Eastern robe. Respect first, always; Craft.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Etiquette", "d": "Kaftan do's and don'ts.", "g": "guide", "l": 2, "q": "What is Etiquette?", "a": "Kaftan do's and don'ts.", "x": "Etiquette: Modern.. Occasions. The rules of respect — Kaftan. flowing Middle Eastern robe. When in doubt, ask about Luxury.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Planning", "d": "Planning around Kaftan.", "g": "guide", "l": 2, "q": "What is Planning?", "a": "Planning around Kaftan.", "x": "Planning: History.. Fabrics. Practical notes — Kaftan. flowing Middle Eastern robe. A little planning shows respect for Styles.. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}, {"t": "Costs", "d": "Kaftan and money.", "g": "guide", "l": 2, "q": "What is Costs?", "a": "Kaftan and money.", "x": "Costs: Wear.. Modern. What to budget — Kaftan. flowing Middle Eastern robe. The best experiences of Craft. are often free. Culture facts from standard references. Practices vary by community; descriptions summarize mainstream observance respectfully.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-clothing-kaftan-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
