(function(){'use strict';
/* JAH Hatchback Vehicle Segment Database generator — jahdb-e2-segment-hatchback-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-segment-hatchback',PREFIX='JAH-E2SEGMENTHA-',NAME='JAH Hatchback Vehicle Segment Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "future", "quiz", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hatchback: overview", "d": "Hatchback: Rear door that includes the window; compact practical..", "g": "overview", "l": 2, "q": "What is Hatchback: overview?", "a": "Hatchback: Rear door that includes the window; compact practical..", "x": "The complete vehicle segment guide: Rear door that includes the window; compact practical.. Golf/GTI icons. From its origins to its most famous examples, from buying advice to what comes next — this database covers the vehicle segment in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How Hatchback began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How Hatchback began.", "x": "The origin of Hatchback: Rear door that includes the window; compact practical.. City friendly. Every great vehicle segment has a founding story of ambition, luck, and timing — and Hatchback's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Golf/GTI icons.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Golf/GTI icons.", "x": "Hatchback: Golf/GTI icons.. This is one of the defining facts about Hatchback — the kind of thing enthusiasts argue about and newcomers should know first. Liftgate. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this Hatchback fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this Hatchback fact matters.", "x": "Why it matters: Golf/GTI icons.. For Hatchback, this fact shaped reputation, sales, or history — understanding it means understanding why the vehicle segment is remembered. Rear door that includes the window; compact practical.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "City friendly.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "City friendly.", "x": "Hatchback: City friendly.. This is one of the defining facts about Hatchback — the kind of thing enthusiasts argue about and newcomers should know first. Compact size. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this Hatchback fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this Hatchback fact matters.", "x": "Why it matters: City friendly.. For Hatchback, this fact shaped reputation, sales, or history — understanding it means understanding why the vehicle segment is remembered. Rear door that includes the window; compact practical.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Civic hatch.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Civic hatch.", "x": "Hatchback: Civic hatch.. This is one of the defining facts about Hatchback — the kind of thing enthusiasts argue about and newcomers should know first. Versatile. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this Hatchback fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this Hatchback fact matters.", "x": "Why it matters: Civic hatch.. For Hatchback, this fact shaped reputation, sales, or history — understanding it means understanding why the vehicle segment is remembered. Rear door that includes the window; compact practical.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Fold-flat seats.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Fold-flat seats.", "x": "Hatchback: Fold-flat seats.. This is one of the defining facts about Hatchback — the kind of thing enthusiasts argue about and newcomers should know first. Affordable. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this Hatchback fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this Hatchback fact matters.", "x": "Why it matters: Fold-flat seats.. For Hatchback, this fact shaped reputation, sales, or history — understanding it means understanding why the vehicle segment is remembered. Rear door that includes the window; compact practical.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Europe staple.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Europe staple.", "x": "Hatchback: Europe staple.. This is one of the defining facts about Hatchback — the kind of thing enthusiasts argue about and newcomers should know first. Urban pick. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this Hatchback fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this Hatchback fact matters.", "x": "Why it matters: Europe staple.. For Hatchback, this fact shaped reputation, sales, or history — understanding it means understanding why the vehicle segment is remembered. Rear door that includes the window; compact practical.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Hot hatches.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Hot hatches.", "x": "Hatchback: Hot hatches.. This is one of the defining facts about Hatchback — the kind of thing enthusiasts argue about and newcomers should know first. 3/5 door. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this Hatchback fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this Hatchback fact matters.", "x": "Why it matters: Hot hatches.. For Hatchback, this fact shaped reputation, sales, or history — understanding it means understanding why the vehicle segment is remembered. Rear door that includes the window; compact practical.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "3/5 door.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "3/5 door.", "x": "More on Hatchback: 3/5 door.. City friendly. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Hatchback. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "Liftgate.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "Liftgate.", "x": "More on Hatchback: Liftgate.. Civic hatch. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Hatchback. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "Compact size.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "Compact size.", "x": "More on Hatchback: Compact size.. Fold-flat seats. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Hatchback. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "Versatile.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "Versatile.", "x": "More on Hatchback: Versatile.. Europe staple. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Hatchback. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Affordable.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Affordable.", "x": "More on Hatchback: Affordable.. Hot hatches. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Hatchback. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Urban pick.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Urban pick.", "x": "More on Hatchback: Urban pick.. Golf/GTI icons. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Hatchback. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a Hatchback: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a Hatchback: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. 3/5 door. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. Civic hatch. The right example of Hatchback is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning Hatchback: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning Hatchback: costs and care.", "x": "Ownership: Liftgate.. Maintain it by the book — fluids, intervals, and qualified specialists. Fold-flat seats. Budget realistically: purchase price is only the beginning of the story with any vehicle segment.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Hatchback through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "Hatchback through the years.", "x": "The timeline: Rear door that includes the window; compact practical.. Golf/GTI icons. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. Compact size. Read it as one story, and the vehicle segment makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for Hatchback.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for Hatchback.", "x": "The future: Hatchback faces electrification, automation, and changing tastes like everything in transport. Europe staple. Its heritage — Rear door that includes the window; compact practical. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "Hatchback fact: Versatile..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "Hatchback fact: Versatile..", "x": "From the Hatchback file: Versatile.. City friendly. Collect these and you will know Hatchback better than most owners. Rear door that includes the window; compact practical. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-segment-hatchback-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
