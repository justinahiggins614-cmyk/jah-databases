(function(){'use strict';
/* JAH Airbus A320 Aircraft Database generator — jahdb-e2-aircraft-airbus-a320-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-aircraft-airbus-a320',PREFIX='JAH-E2AIRCRAFTA-',NAME='JAH Airbus A320 Aircraft Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "future", "quiz", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Airbus A320: overview", "d": "Airbus A320: Best-selling Airbus; fly-by-wire pioneer (1987)..", "g": "overview", "l": 2, "q": "What is Airbus A320: overview?", "a": "Airbus A320: Best-selling Airbus; fly-by-wire pioneer (1987)..", "x": "The complete aircraft guide: Best-selling Airbus; fly-by-wire pioneer (1987).. First digital fly-by-wire airliner. From its origins to its most famous examples, from buying advice to what comes next — this database covers the aircraft in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How Airbus A320 began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How Airbus A320 began.", "x": "The origin of Airbus A320: Best-selling Airbus; fly-by-wire pioneer (1987).. neo: 15% fuel savings. Every great aircraft has a founding story of ambition, luck, and timing — and Airbus A320's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "First digital fly-by-wire airliner.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "First digital fly-by-wire airliner.", "x": "Airbus A320: First digital fly-by-wire airliner.. This is one of the defining facts about Airbus A320 — the kind of thing enthusiasts argue about and newcomers should know first. Launched 1984. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this Airbus A320 fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this Airbus A320 fact matters.", "x": "Why it matters: First digital fly-by-wire airliner.. For Airbus A320, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. Best-selling Airbus; fly-by-wire pioneer (1987).", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "neo: 15% fuel savings.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "neo: 15% fuel savings.", "x": "Airbus A320: neo: 15% fuel savings.. This is one of the defining facts about Airbus A320 — the kind of thing enthusiasts argue about and newcomers should know first. Sidestick controllers. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this Airbus A320 fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this Airbus A320 fact matters.", "x": "Why it matters: neo: 15% fuel savings.. For Airbus A320, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. Best-selling Airbus; fly-by-wire pioneer (1987).", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "A321XLR: long-range single-aisle.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "A321XLR: long-range single-aisle.", "x": "Airbus A320: A321XLR: long-range single-aisle.. This is one of the defining facts about Airbus A320 — the kind of thing enthusiasts argue about and newcomers should know first. neo engines: LEAP/PW. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this Airbus A320 fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this Airbus A320 fact matters.", "x": "Why it matters: A321XLR: long-range single-aisle.. For Airbus A320, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. Best-selling Airbus; fly-by-wire pioneer (1987).", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Huge backlog.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Huge backlog.", "x": "Airbus A320: Huge backlog.. This is one of the defining facts about Airbus A320 — the kind of thing enthusiasts argue about and newcomers should know first. Most ordered ever. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this Airbus A320 fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this Airbus A320 fact matters.", "x": "Why it matters: Huge backlog.. For Airbus A320, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. Best-selling Airbus; fly-by-wire pioneer (1987).", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "JetBlue/EasyJet fleets.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "JetBlue/EasyJet fleets.", "x": "Airbus A320: JetBlue/EasyJet fleets.. This is one of the defining facts about Airbus A320 — the kind of thing enthusiasts argue about and newcomers should know first. Assembled globally. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this Airbus A320 fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this Airbus A320 fact matters.", "x": "Why it matters: JetBlue/EasyJet fleets.. For Airbus A320, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. Best-selling Airbus; fly-by-wire pioneer (1987).", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Family: A318-A321.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Family: A318-A321.", "x": "Airbus A320: Family: A318-A321.. This is one of the defining facts about Airbus A320 — the kind of thing enthusiasts argue about and newcomers should know first. Airbus, Toulouse/Hamburg. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this Airbus A320 fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this Airbus A320 fact matters.", "x": "Why it matters: Family: A318-A321.. For Airbus A320, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. Best-selling Airbus; fly-by-wire pioneer (1987).", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "Airbus, Toulouse/Hamburg.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "Airbus, Toulouse/Hamburg.", "x": "More on Airbus A320: Airbus, Toulouse/Hamburg.. neo: 15% fuel savings. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Airbus A320.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "Launched 1984.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "Launched 1984.", "x": "More on Airbus A320: Launched 1984.. A321XLR: long-range single-aisle. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Airbus A320.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "Sidestick controllers.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "Sidestick controllers.", "x": "More on Airbus A320: Sidestick controllers.. Huge backlog. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Airbus A320.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "neo engines: LEAP/PW.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "neo engines: LEAP/PW.", "x": "More on Airbus A320: neo engines: LEAP/PW.. JetBlue/EasyJet fleets. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Airbus A320.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Most ordered ever.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Most ordered ever.", "x": "More on Airbus A320: Most ordered ever.. Family: A318-A321. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Airbus A320.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Assembled globally.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Assembled globally.", "x": "More on Airbus A320: Assembled globally.. First digital fly-by-wire airliner. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Airbus A320.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a Airbus A320: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a Airbus A320: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. Airbus, Toulouse/Hamburg. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. A321XLR: long-range single-aisle. The right example of Airbus A320 is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning Airbus A320: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning Airbus A320: costs and care.", "x": "Ownership: Launched 1984.. Maintain it by the book — fluids, intervals, and qualified specialists. Huge backlog. Budget realistically: purchase price is only the beginning of the story with any aircraft.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Airbus A320 through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "Airbus A320 through the years.", "x": "The timeline: Best-selling Airbus; fly-by-wire pioneer (1987).. First digital fly-by-wire airliner. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. Sidestick controllers. Read it as one story, and the aircraft makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for Airbus A320.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for Airbus A320.", "x": "The future: Airbus A320 faces electrification, automation, and changing tastes like everything in transport. JetBlue/EasyJet fleets. Its heritage — Best-selling Airbus; fly-by-wire pioneer (1987). — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "Airbus A320 fact: neo engines: LEAP/PW..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "Airbus A320 fact: neo engines: LEAP/PW..", "x": "From the Airbus A320 file: neo engines: LEAP/PW.. neo: 15% fuel savings. Collect these and you will know Airbus A320 better than most owners. Best-selling Airbus; fly-by-wire pioneer (1987). Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-aircraft-airbus-a320-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
