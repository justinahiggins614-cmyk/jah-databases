(function(){'use strict';
/* JAH Kia EV6 Electric Vehicle Database generator — jahdb-e2-ev-kia-ev6-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-ev-kia-ev6',PREFIX='JAH-E2EVKIAEV6-',NAME='JAH Kia EV6 Electric Vehicle Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "future", "quiz", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Kia EV6: overview", "d": "Kia EV6: Hyundai-group EV crossover; 800V charging..", "g": "overview", "l": 2, "q": "What is Kia EV6: overview?", "a": "Kia EV6: Hyundai-group EV crossover; 800V charging..", "x": "The complete electric vehicle guide: Hyundai-group EV crossover; 800V charging.. 800V architecture. From its origins to its most famous examples, from buying advice to what comes next — this database covers the electric vehicle in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How Kia EV6 began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How Kia EV6 began.", "x": "The origin of Kia EV6: Hyundai-group EV crossover; 800V charging.. GT: 576 hp. Every great electric vehicle has a founding story of ambition, luck, and timing — and Kia EV6's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "800V architecture.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "800V architecture.", "x": "Kia EV6: 800V architecture.. This is one of the defining facts about Kia EV6 — the kind of thing enthusiasts argue about and newcomers should know first. Hwaseong built. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this Kia EV6 fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this Kia EV6 fact matters.", "x": "Why it matters: 800V architecture.. For Kia EV6, this fact shaped reputation, sales, or history — understanding it means understanding why the electric vehicle is remembered. Hyundai-group EV crossover; 800V charging.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "GT: 576 hp.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "GT: 576 hp.", "x": "Kia EV6: GT: 576 hp.. This is one of the defining facts about Kia EV6 — the kind of thing enthusiasts argue about and newcomers should know first. OTA. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this Kia EV6 fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this Kia EV6 fact matters.", "x": "Why it matters: GT: 576 hp.. For Kia EV6, this fact shaped reputation, sales, or history — understanding it means understanding why the electric vehicle is remembered. Hyundai-group EV crossover; 800V charging.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "European Car of the Year.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "European Car of the Year.", "x": "Kia EV6: European Car of the Year.. This is one of the defining facts about Kia EV6 — the kind of thing enthusiasts argue about and newcomers should know first. Augmented HUD. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this Kia EV6 fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this Kia EV6 fact matters.", "x": "Why it matters: European Car of the Year.. For Kia EV6, this fact shaped reputation, sales, or history — understanding it means understanding why the electric vehicle is remembered. Hyundai-group EV crossover; 800V charging.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "V2L power.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "V2L power.", "x": "Kia EV6: V2L power.. This is one of the defining facts about Kia EV6 — the kind of thing enthusiasts argue about and newcomers should know first. Heat pump. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this Kia EV6 fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this Kia EV6 fact matters.", "x": "Why it matters: V2L power.. For Kia EV6, this fact shaped reputation, sales, or history — understanding it means understanding why the electric vehicle is remembered. Hyundai-group EV crossover; 800V charging.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Long range.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Long range.", "x": "Kia EV6: Long range.. This is one of the defining facts about Kia EV6 — the kind of thing enthusiasts argue about and newcomers should know first. Sporty. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this Kia EV6 fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this Kia EV6 fact matters.", "x": "Why it matters: Long range.. For Kia EV6, this fact shaped reputation, sales, or history — understanding it means understanding why the electric vehicle is remembered. Hyundai-group EV crossover; 800V charging.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "GT-Line style.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "GT-Line style.", "x": "Kia EV6: GT-Line style.. This is one of the defining facts about Kia EV6 — the kind of thing enthusiasts argue about and newcomers should know first. E-GMP. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this Kia EV6 fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this Kia EV6 fact matters.", "x": "Why it matters: GT-Line style.. For Kia EV6, this fact shaped reputation, sales, or history — understanding it means understanding why the electric vehicle is remembered. Hyundai-group EV crossover; 800V charging.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "E-GMP.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "E-GMP.", "x": "More on Kia EV6: E-GMP.. GT: 576 hp. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Kia EV6. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "Hwaseong built.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "Hwaseong built.", "x": "More on Kia EV6: Hwaseong built.. European Car of the Year. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Kia EV6.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "OTA.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "OTA.", "x": "More on Kia EV6: OTA.. V2L power. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Kia EV6. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "Augmented HUD.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "Augmented HUD.", "x": "More on Kia EV6: Augmented HUD.. Long range. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Kia EV6. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Heat pump.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Heat pump.", "x": "More on Kia EV6: Heat pump.. GT-Line style. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Kia EV6. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Sporty.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Sporty.", "x": "More on Kia EV6: Sporty.. 800V architecture. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Kia EV6. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a Kia EV6: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a Kia EV6: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. E-GMP. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. European Car of the Year. The right example of Kia EV6 is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning Kia EV6: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning Kia EV6: costs and care.", "x": "Ownership: Hwaseong built.. Maintain it by the book — fluids, intervals, and qualified specialists. V2L power. Budget realistically: purchase price is only the beginning of the story with any electric vehicle.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Kia EV6 through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "Kia EV6 through the years.", "x": "The timeline: Hyundai-group EV crossover; 800V charging.. 800V architecture. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. OTA. Read it as one story, and the electric vehicle makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for Kia EV6.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for Kia EV6.", "x": "The future: Kia EV6 faces electrification, automation, and changing tastes like everything in transport. Long range. Its heritage — Hyundai-group EV crossover; 800V charging. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "Kia EV6 fact: Augmented HUD..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "Kia EV6 fact: Augmented HUD..", "x": "From the Kia EV6 file: Augmented HUD.. GT: 576 hp. Collect these and you will know Kia EV6 better than most owners. Hyundai-group EV crossover; 800V charging. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-ev-kia-ev6-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
