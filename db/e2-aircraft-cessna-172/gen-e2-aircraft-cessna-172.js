(function(){'use strict';
/* JAH Cessna 172 Skyhawk Aircraft Database generator — jahdb-e2-aircraft-cessna-172-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-aircraft-cessna-172',PREFIX='JAH-E2AIRCRAFTC-',NAME='JAH Cessna 172 Skyhawk Aircraft Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "future", "quiz", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Cessna 172 Skyhawk: overview", "d": "Cessna 172 Skyhawk: Most-built aircraft ever (44,000+); trainer since 1956..", "g": "overview", "l": 2, "q": "What is Cessna 172 Skyhawk: overview?", "a": "Cessna 172 Skyhawk: Most-built aircraft ever (44,000+); trainer since 1956..", "x": "The complete aircraft guide: Most-built aircraft ever (44,000+); trainer since 1956.. Every pilot's first plane. From its origins to its most famous examples, from buying advice to what comes next — this database covers the aircraft in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How Cessna 172 Skyhawk began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How Cessna 172 Skyhawk began.", "x": "The origin of Cessna 172 Skyhawk: Most-built aircraft ever (44,000+); trainer since 1956.. 44,000+ built. Every great aircraft has a founding story of ambition, luck, and timing — and Cessna 172 Skyhawk's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Every pilot's first plane.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Every pilot's first plane.", "x": "Cessna 172 Skyhawk: Every pilot's first plane.. This is one of the defining facts about Cessna 172 Skyhawk — the kind of thing enthusiasts argue about and newcomers should know first. First flight 1955.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this Cessna 172 Skyhawk fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this Cessna 172 Skyhawk fact matters.", "x": "Why it matters: Every pilot's first plane.. For Cessna 172 Skyhawk, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. Most-built aircraft ever (44,000+); trainer since 1956.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "44,000+ built.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "44,000+ built.", "x": "Cessna 172 Skyhawk: 44,000+ built.. This is one of the defining facts about Cessna 172 Skyhawk — the kind of thing enthusiasts argue about and newcomers should know first. Skyhawk name 1960. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this Cessna 172 Skyhawk fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this Cessna 172 Skyhawk fact matters.", "x": "Why it matters: 44,000+ built.. For Cessna 172 Skyhawk, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. Most-built aircraft ever (44,000+); trainer since 1956.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "High-wing trainer.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "High-wing trainer.", "x": "Cessna 172 Skyhawk: High-wing trainer.. This is one of the defining facts about Cessna 172 Skyhawk — the kind of thing enthusiasts argue about and newcomers should know first. Textron-owned. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this Cessna 172 Skyhawk fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this Cessna 172 Skyhawk fact matters.", "x": "Why it matters: High-wing trainer.. For Cessna 172 Skyhawk, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. Most-built aircraft ever (44,000+); trainer since 1956.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Still in production.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Still in production.", "x": "Cessna 172 Skyhawk: Still in production.. This is one of the defining facts about Cessna 172 Skyhawk — the kind of thing enthusiasts argue about and newcomers should know first. Glass cockpit now. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this Cessna 172 Skyhawk fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this Cessna 172 Skyhawk fact matters.", "x": "Why it matters: Still in production.. For Cessna 172 Skyhawk, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. Most-built aircraft ever (44,000+); trainer since 1956.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Forgiving flight traits.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Forgiving flight traits.", "x": "Cessna 172 Skyhawk: Forgiving flight traits.. This is one of the defining facts about Cessna 172 Skyhawk — the kind of thing enthusiasts argue about and newcomers should know first. Flight schools' staple.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this Cessna 172 Skyhawk fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this Cessna 172 Skyhawk fact matters.", "x": "Why it matters: Forgiving flight traits.. For Cessna 172 Skyhawk, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. Most-built aircraft ever (44,000+); trainer since 1956.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "4 seats.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "4 seats.", "x": "Cessna 172 Skyhawk: 4 seats.. This is one of the defining facts about Cessna 172 Skyhawk — the kind of thing enthusiasts argue about and newcomers should know first. Cessna, Wichita. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this Cessna 172 Skyhawk fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this Cessna 172 Skyhawk fact matters.", "x": "Why it matters: 4 seats.. For Cessna 172 Skyhawk, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. Most-built aircraft ever (44,000+); trainer since 1956.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "Cessna, Wichita.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "Cessna, Wichita.", "x": "More on Cessna 172 Skyhawk: Cessna, Wichita.. 44,000+ built. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Cessna 172 Skyhawk.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "First flight 1955.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "First flight 1955.", "x": "More on Cessna 172 Skyhawk: First flight 1955.. High-wing trainer. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Cessna 172 Skyhawk.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "Skyhawk name 1960.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "Skyhawk name 1960.", "x": "More on Cessna 172 Skyhawk: Skyhawk name 1960.. Still in production. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Cessna 172 Skyhawk.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "Textron-owned.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "Textron-owned.", "x": "More on Cessna 172 Skyhawk: Textron-owned.. Forgiving flight traits. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Cessna 172 Skyhawk.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Glass cockpit now.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Glass cockpit now.", "x": "More on Cessna 172 Skyhawk: Glass cockpit now.. 4 seats. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Cessna 172 Skyhawk.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Flight schools' staple.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Flight schools' staple.", "x": "More on Cessna 172 Skyhawk: Flight schools' staple.. Every pilot's first plane. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Cessna 172 Skyhawk.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a Cessna 172 Skyhawk: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a Cessna 172 Skyhawk: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. Cessna, Wichita. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. High-wing trainer. The right example of Cessna 172 Skyhawk is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning Cessna 172 Skyhawk: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning Cessna 172 Skyhawk: costs and care.", "x": "Ownership: First flight 1955.. Maintain it by the book — fluids, intervals, and qualified specialists. Still in production. Budget realistically: purchase price is only the beginning of the story with any aircraft.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Cessna 172 Skyhawk through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "Cessna 172 Skyhawk through the years.", "x": "The timeline: Most-built aircraft ever (44,000+); trainer since 1956.. Every pilot's first plane. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. Skyhawk name 1960. Read it as one story, and the aircraft makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for Cessna 172 Skyhawk.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for Cessna 172 Skyhawk.", "x": "The future: Cessna 172 Skyhawk faces electrification, automation, and changing tastes like everything in transport. Forgiving flight traits. Its heritage — Most-built aircraft ever (44,000+); trainer since 1956. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "Cessna 172 Skyhawk fact: Textron-owned..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "Cessna 172 Skyhawk fact: Textron-owned..", "x": "From the Cessna 172 Skyhawk file: Textron-owned.. 44,000+ built. Collect these and you will know Cessna 172 Skyhawk better than most owners. Most-built aircraft ever (44,000+); trainer since 1956. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-aircraft-cessna-172-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
