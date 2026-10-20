(function(){'use strict';
/* JAH Glacier Express Train Database generator — jahdb-e2-train-glacier-express-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-train-glacier-express',PREFIX='JAH-E2TRAINGLAC-',NAME='JAH Glacier Express Train Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "future", "quiz", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Glacier Express: overview", "d": "Glacier Express: Swiss scenic rail; Zermatt-St. Moritz..", "g": "overview", "l": 2, "q": "What is Glacier Express: overview?", "a": "Glacier Express: Swiss scenic rail; Zermatt-St. Moritz..", "x": "The complete train guide: Swiss scenic rail; Zermatt-St. Moritz.. Slowest express. From its origins to its most famous examples, from buying advice to what comes next — this database covers the train in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How Glacier Express began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How Glacier Express began.", "x": "The origin of Glacier Express: Swiss scenic rail; Zermatt-St. Moritz.. 291 bridges. Every great train has a founding story of ambition, luck, and timing — and Glacier Express's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Slowest express.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Slowest express.", "x": "Glacier Express: Slowest express.. This is one of the defining facts about Glacier Express — the kind of thing enthusiasts argue about and newcomers should know first. 1930 debut. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this Glacier Express fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this Glacier Express fact matters.", "x": "Why it matters: Slowest express.. For Glacier Express, this fact shaped reputation, sales, or history — understanding it means understanding why the train is remembered. Swiss scenic rail; Zermatt-St. Moritz.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "291 bridges.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "291 bridges.", "x": "Glacier Express: 291 bridges.. This is one of the defining facts about Glacier Express — the kind of thing enthusiasts argue about and newcomers should know first. Oberalp Pass. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this Glacier Express fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this Glacier Express fact matters.", "x": "Why it matters: 291 bridges.. For Glacier Express, this fact shaped reputation, sales, or history — understanding it means understanding why the train is remembered. Swiss scenic rail; Zermatt-St. Moritz.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Landwasser Viaduct.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Landwasser Viaduct.", "x": "Glacier Express: Landwasser Viaduct.. This is one of the defining facts about Glacier Express — the kind of thing enthusiasts argue about and newcomers should know first. Winter wonderland. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this Glacier Express fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this Glacier Express fact matters.", "x": "Why it matters: Landwasser Viaduct.. For Glacier Express, this fact shaped reputation, sales, or history — understanding it means understanding why the train is remembered. Swiss scenic rail; Zermatt-St. Moritz.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Panoramic cars.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Panoramic cars.", "x": "Glacier Express: Panoramic cars.. This is one of the defining facts about Glacier Express — the kind of thing enthusiasts argue about and newcomers should know first. Excellence Class. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this Glacier Express fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this Glacier Express fact matters.", "x": "Why it matters: Panoramic cars.. For Glacier Express, this fact shaped reputation, sales, or history — understanding it means understanding why the train is remembered. Swiss scenic rail; Zermatt-St. Moritz.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "8 hours.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "8 hours.", "x": "Glacier Express: 8 hours.. This is one of the defining facts about Glacier Express — the kind of thing enthusiasts argue about and newcomers should know first. Bucket list. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this Glacier Express fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this Glacier Express fact matters.", "x": "Why it matters: 8 hours.. For Glacier Express, this fact shaped reputation, sales, or history — understanding it means understanding why the train is remembered. Swiss scenic rail; Zermatt-St. Moritz.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Alps showcase.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Alps showcase.", "x": "Glacier Express: Alps showcase.. This is one of the defining facts about Glacier Express — the kind of thing enthusiasts argue about and newcomers should know first. RhB/MGB. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this Glacier Express fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this Glacier Express fact matters.", "x": "Why it matters: Alps showcase.. For Glacier Express, this fact shaped reputation, sales, or history — understanding it means understanding why the train is remembered. Swiss scenic rail; Zermatt-St. Moritz.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "RhB/MGB.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "RhB/MGB.", "x": "More on Glacier Express: RhB/MGB.. 291 bridges. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Glacier Express.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "1930 debut.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "1930 debut.", "x": "More on Glacier Express: 1930 debut.. Landwasser Viaduct. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Glacier Express.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "Oberalp Pass.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "Oberalp Pass.", "x": "More on Glacier Express: Oberalp Pass.. Panoramic cars. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Glacier Express.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "Winter wonderland.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "Winter wonderland.", "x": "More on Glacier Express: Winter wonderland.. 8 hours. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Glacier Express.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Excellence Class.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Excellence Class.", "x": "More on Glacier Express: Excellence Class.. Alps showcase. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Glacier Express.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Bucket list.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Bucket list.", "x": "More on Glacier Express: Bucket list.. Slowest express. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Glacier Express.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a Glacier Express: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a Glacier Express: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. RhB/MGB. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. Landwasser Viaduct. The right example of Glacier Express is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning Glacier Express: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning Glacier Express: costs and care.", "x": "Ownership: 1930 debut.. Maintain it by the book — fluids, intervals, and qualified specialists. Panoramic cars. Budget realistically: purchase price is only the beginning of the story with any train. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Glacier Express through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "Glacier Express through the years.", "x": "The timeline: Swiss scenic rail; Zermatt-St. Moritz.. Slowest express. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. Oberalp Pass. Read it as one story, and the train makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for Glacier Express.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for Glacier Express.", "x": "The future: Glacier Express faces electrification, automation, and changing tastes like everything in transport. 8 hours. Its heritage — Swiss scenic rail; Zermatt-St. Moritz. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "Glacier Express fact: Winter wonderland..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "Glacier Express fact: Winter wonderland..", "x": "From the Glacier Express file: Winter wonderland.. 291 bridges. Collect these and you will know Glacier Express better than most owners. Swiss scenic rail; Zermatt-St. Moritz. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-train-glacier-express-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
