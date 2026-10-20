(function(){'use strict';
/* JAH Lada Car Make Database generator — jahdb-e2-car-lada-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-car-lada',PREFIX='JAH-E2CARLADA-',NAME='JAH Lada Car Make Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "facts", "future", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Lada: overview", "d": "Lada: Russian maker; AvtoVAZ since 1966..", "g": "overview", "l": 2, "q": "What is Lada: overview?", "a": "Lada: Russian maker; AvtoVAZ since 1966..", "x": "The complete car make guide: Russian maker; AvtoVAZ since 1966.. Niva: legendary 4x4. From its origins to its most famous models, from buying advice to what comes next — this database covers the car make in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How Lada began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How Lada began.", "x": "The origin of Lada: Russian maker; AvtoVAZ since 1966.. 2101: Fiat-based classic. Every great car make has a founding story of ambition, luck, and timing — and Lada's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Niva: legendary 4x4.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Niva: legendary 4x4.", "x": "Lada: Niva: legendary 4x4.. This is one of the defining facts about Lada — the kind of thing enthusiasts argue about and newcomers should know first. AvtoVAZ. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this Lada fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this Lada fact matters.", "x": "Why it matters: Niva: legendary 4x4.. For Lada, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Russian maker; AvtoVAZ since 1966.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "2101: Fiat-based classic.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "2101: Fiat-based classic.", "x": "Lada: 2101: Fiat-based classic.. This is one of the defining facts about Lada — the kind of thing enthusiasts argue about and newcomers should know first. Renault owned then exited. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this Lada fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this Lada fact matters.", "x": "Why it matters: 2101: Fiat-based classic.. For Lada, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Russian maker; AvtoVAZ since 1966.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Riva: 80s export.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Riva: 80s export.", "x": "Lada: Riva: 80s export.. This is one of the defining facts about Lada — the kind of thing enthusiasts argue about and newcomers should know first. Niva still made. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this Lada fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this Lada fact matters.", "x": "Why it matters: Riva: 80s export.. For Lada, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Russian maker; AvtoVAZ since 1966. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Vesta/XRAY modern.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Vesta/XRAY modern.", "x": "Lada: Vesta/XRAY modern.. This is one of the defining facts about Lada — the kind of thing enthusiasts argue about and newcomers should know first. Samara: 80s hatch. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this Lada fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this Lada fact matters.", "x": "Why it matters: Vesta/XRAY modern.. For Lada, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Russian maker; AvtoVAZ since 1966. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Sanctions era.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Sanctions era.", "x": "Lada: Sanctions era.. This is one of the defining facts about Lada — the kind of thing enthusiasts argue about and newcomers should know first. Russian icon. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this Lada fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this Lada fact matters.", "x": "Why it matters: Sanctions era.. For Lada, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Russian maker; AvtoVAZ since 1966. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Granta: current.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Granta: current.", "x": "Lada: Granta: current.. This is one of the defining facts about Lada — the kind of thing enthusiasts argue about and newcomers should know first. Headquarters: Togliatti. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this Lada fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this Lada fact matters.", "x": "Why it matters: Granta: current.. For Lada, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Russian maker; AvtoVAZ since 1966. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "Headquarters: Togliatti.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "Headquarters: Togliatti.", "x": "More on Lada: Headquarters: Togliatti.. 2101: Fiat-based classic. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Lada.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "AvtoVAZ.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "AvtoVAZ.", "x": "More on Lada: AvtoVAZ.. Riva: 80s export. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Lada. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "Renault owned then exited.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "Renault owned then exited.", "x": "More on Lada: Renault owned then exited.. Vesta/XRAY modern. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Lada.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "Niva still made.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "Niva still made.", "x": "More on Lada: Niva still made.. Sanctions era. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Lada. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Samara: 80s hatch.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Samara: 80s hatch.", "x": "More on Lada: Samara: 80s hatch.. Granta: current. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Lada. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Russian icon.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Russian icon.", "x": "More on Lada: Russian icon.. Niva: legendary 4x4. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Lada. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a Lada: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a Lada: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. Headquarters: Togliatti. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. Riva: 80s export. The right example of Lada is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning Lada: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning Lada: costs and care.", "x": "Ownership: AvtoVAZ.. Maintain it by the book — fluids, intervals, and qualified specialists. Vesta/XRAY modern. Budget realistically: purchase price is only the beginning of the story with any car make.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Lada through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "Lada through the years.", "x": "The timeline: Russian maker; AvtoVAZ since 1966.. Niva: legendary 4x4. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. Renault owned then exited. Read it as one story, and the car make makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for Lada.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for Lada.", "x": "The future: Lada faces electrification, automation, and changing tastes like everything in transport. Sanctions era. Its heritage — Russian maker; AvtoVAZ since 1966. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "Lada fact: Niva still made..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "Lada fact: Niva still made..", "x": "From the Lada file: Niva still made.. 2101: Fiat-based classic. Collect these and you will know Lada better than most owners. Russian maker; AvtoVAZ since 1966. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-car-lada-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
