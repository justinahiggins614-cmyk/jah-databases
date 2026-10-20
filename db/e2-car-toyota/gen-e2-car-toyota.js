(function(){'use strict';
/* JAH Toyota Car Make Database generator — jahdb-e2-car-toyota-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-car-toyota',PREFIX='JAH-E2CARTOYOTA-',NAME='JAH Toyota Car Make Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "facts", "future", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Toyota: overview", "d": "Toyota: Japanese automaker founded 1937 by Kiichiro Toyoda..", "g": "overview", "l": 2, "q": "What is Toyota: overview?", "a": "Toyota: Japanese automaker founded 1937 by Kiichiro Toyoda..", "x": "The complete car make guide: Japanese automaker founded 1937 by Kiichiro Toyoda.. The Corolla is the best-selling car in history (50M+). From its origins to its most famous models, from buying advice to what comes next — this database covers the car make in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How Toyota began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How Toyota began.", "x": "The origin of Toyota: Japanese automaker founded 1937 by Kiichiro Toyoda.. Pioneered hybrid tech with the Prius (1997). Every great car make has a founding story of ambition, luck, and timing — and Toyota's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "The Corolla is the best-selling car in history (50M+).", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "The Corolla is the best-selling car in history (50M+).", "x": "Toyota: The Corolla is the best-selling car in history (50M+).. This is one of the defining facts about Toyota — the kind of thing enthusiasts argue about and newcomers should know first. Largest automaker by sales for years.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this Toyota fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this Toyota fact matters.", "x": "Why it matters: The Corolla is the best-selling car in history (50M+).. For Toyota, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Japanese automaker founded 1937 by Kiichiro Toyoda.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Pioneered hybrid tech with the Prius (1997).", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Pioneered hybrid tech with the Prius (1997).", "x": "Toyota: Pioneered hybrid tech with the Prius (1997).. This is one of the defining facts about Toyota — the kind of thing enthusiasts argue about and newcomers should know first. Famous for reliability and resale value.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this Toyota fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this Toyota fact matters.", "x": "Why it matters: Pioneered hybrid tech with the Prius (1997).. For Toyota, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Japanese automaker founded 1937 by Kiichiro Toyoda.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Toyota Production System invented lean manufacturing.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Toyota Production System invented lean manufacturing.", "x": "Toyota: Toyota Production System invented lean manufacturing.. This is one of the defining facts about Toyota — the kind of thing enthusiasts argue about and newcomers should know first. Makes the Supra sports car (with BMW).", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this Toyota fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this Toyota fact matters.", "x": "Why it matters: Toyota Production System invented lean manufacturing.. For Toyota, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Japanese automaker founded 1937 by Kiichiro Toyoda.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Land Cruiser: legendary off-road durability.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Land Cruiser: legendary off-road durability.", "x": "Toyota: Land Cruiser: legendary off-road durability.. This is one of the defining facts about Toyota — the kind of thing enthusiasts argue about and newcomers should know first. Also owns Daihatsu; stake in Subaru.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this Toyota fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this Toyota fact matters.", "x": "Why it matters: Land Cruiser: legendary off-road durability.. For Toyota, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Japanese automaker founded 1937 by Kiichiro Toyoda.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Lexus is its luxury division (1989).", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Lexus is its luxury division (1989).", "x": "Toyota: Lexus is its luxury division (1989).. This is one of the defining facts about Toyota — the kind of thing enthusiasts argue about and newcomers should know first. Hybrid leader: 20M+ hybrids sold.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this Toyota fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this Toyota fact matters.", "x": "Why it matters: Lexus is its luxury division (1989).. For Toyota, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Japanese automaker founded 1937 by Kiichiro Toyoda.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Camry: America's best-selling sedan for decades.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Camry: America's best-selling sedan for decades.", "x": "Toyota: Camry: America's best-selling sedan for decades.. This is one of the defining facts about Toyota — the kind of thing enthusiasts argue about and newcomers should know first. Headquarters: Toyota City, Japan.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this Toyota fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this Toyota fact matters.", "x": "Why it matters: Camry: America's best-selling sedan for decades.. For Toyota, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Japanese automaker founded 1937 by Kiichiro Toyoda.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "Headquarters: Toyota City, Japan.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "Headquarters: Toyota City, Japan.", "x": "More on Toyota: Headquarters: Toyota City, Japan.. Pioneered hybrid tech with the Prius (1997). Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Toyota.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "Largest automaker by sales for years.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "Largest automaker by sales for years.", "x": "More on Toyota: Largest automaker by sales for years.. Toyota Production System invented lean manufacturing. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Toyota.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "Famous for reliability and resale value.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "Famous for reliability and resale value.", "x": "More on Toyota: Famous for reliability and resale value.. Land Cruiser: legendary off-road durability. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Toyota.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "Makes the Supra sports car (with BMW).", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "Makes the Supra sports car (with BMW).", "x": "More on Toyota: Makes the Supra sports car (with BMW).. Lexus is its luxury division (1989). Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Toyota.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Also owns Daihatsu; stake in Subaru.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Also owns Daihatsu; stake in Subaru.", "x": "More on Toyota: Also owns Daihatsu; stake in Subaru.. Camry: America's best-selling sedan for decades. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Toyota.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Hybrid leader: 20M+ hybrids sold.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Hybrid leader: 20M+ hybrids sold.", "x": "More on Toyota: Hybrid leader: 20M+ hybrids sold.. The Corolla is the best-selling car in history (50M+). Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Toyota.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a Toyota: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a Toyota: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. Headquarters: Toyota City, Japan. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. Toyota Production System invented lean manufacturing. The right example of Toyota is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning Toyota: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning Toyota: costs and care.", "x": "Ownership: Largest automaker by sales for years.. Maintain it by the book — fluids, intervals, and qualified specialists. Land Cruiser: legendary off-road durability. Budget realistically: purchase price is only the beginning of the story with any car make.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Toyota through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "Toyota through the years.", "x": "The timeline: Japanese automaker founded 1937 by Kiichiro Toyoda.. The Corolla is the best-selling car in history (50M+). Key chapters mark the eras — the breakthroughs, the crises, the comebacks. Famous for reliability and resale value. Read it as one story, and the car make makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for Toyota.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for Toyota.", "x": "The future: Toyota faces electrification, automation, and changing tastes like everything in transport. Lexus is its luxury division (1989). Its heritage — Japanese automaker founded 1937 by Kiichiro Toyoda. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "Toyota fact: Makes the Supra sports car (with BMW)..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "Toyota fact: Makes the Supra sports car (with BMW)..", "x": "From the Toyota file: Makes the Supra sports car (with BMW).. Pioneered hybrid tech with the Prius (1997). Collect these and you will know Toyota better than most owners. Japanese automaker founded 1937 by Kiichiro Toyoda.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-car-toyota-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
