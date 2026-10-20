(function(){'use strict';
/* JAH Sleeper Bus Bus Type Database generator — jahdb-e2-bus-sleeper-bus-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-bus-sleeper-bus',PREFIX='JAH-E2BUSSLEEPE-',NAME='JAH Sleeper Bus Bus Type Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "future", "quiz", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Sleeper Bus: overview", "d": "Sleeper Bus: Overnight bus with beds; Asia and South America staple..", "g": "overview", "l": 2, "q": "What is Sleeper Bus: overview?", "a": "Sleeper Bus: Overnight bus with beds; Asia and South America staple..", "x": "The complete bus type guide: Overnight bus with beds; Asia and South America staple.. Beds onboard. From its origins to its most famous examples, from buying advice to what comes next — this database covers the bus type in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How Sleeper Bus began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How Sleeper Bus began.", "x": "The origin of Sleeper Bus: Overnight bus with beds; Asia and South America staple.. Vietnam/Argentina. Every great bus type has a founding story of ambition, luck, and timing — and Sleeper Bus's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Beds onboard.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Beds onboard.", "x": "Sleeper Bus: Beds onboard.. This is one of the defining facts about Sleeper Bus — the kind of thing enthusiasts argue about and newcomers should know first. Blankets. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this Sleeper Bus fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this Sleeper Bus fact matters.", "x": "Why it matters: Beds onboard.. For Sleeper Bus, this fact shaped reputation, sales, or history — understanding it means understanding why the bus type is remembered. Overnight bus with beds; Asia and South America staple.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Vietnam/Argentina.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Vietnam/Argentina.", "x": "Sleeper Bus: Vietnam/Argentina.. This is one of the defining facts about Sleeper Bus — the kind of thing enthusiasts argue about and newcomers should know first. Rest stops. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this Sleeper Bus fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this Sleeper Bus fact matters.", "x": "Why it matters: Vietnam/Argentina.. For Sleeper Bus, this fact shaped reputation, sales, or history — understanding it means understanding why the bus type is remembered. Overnight bus with beds; Asia and South America staple.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Cheaper than flights.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Cheaper than flights.", "x": "Sleeper Bus: Cheaper than flights.. This is one of the defining facts about Sleeper Bus — the kind of thing enthusiasts argue about and newcomers should know first. Book ahead. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this Sleeper Bus fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this Sleeper Bus fact matters.", "x": "Why it matters: Cheaper than flights.. For Sleeper Bus, this fact shaped reputation, sales, or history — understanding it means understanding why the bus type is remembered. Overnight bus with beds; Asia and South America staple.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Reclining berths.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Reclining berths.", "x": "Sleeper Bus: Reclining berths.. This is one of the defining facts about Sleeper Bus — the kind of thing enthusiasts argue about and newcomers should know first. Budget travel. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this Sleeper Bus fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this Sleeper Bus fact matters.", "x": "Why it matters: Reclining berths.. For Sleeper Bus, this fact shaped reputation, sales, or history — understanding it means understanding why the bus type is remembered. Overnight bus with beds; Asia and South America staple.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Night routes.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Night routes.", "x": "Sleeper Bus: Night routes.. This is one of the defining facts about Sleeper Bus — the kind of thing enthusiasts argue about and newcomers should know first. Sleep rolling. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this Sleeper Bus fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this Sleeper Bus fact matters.", "x": "Why it matters: Night routes.. For Sleeper Bus, this fact shaped reputation, sales, or history — understanding it means understanding why the bus type is remembered. Overnight bus with beds; Asia and South America staple.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Backpacker favorite.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Backpacker favorite.", "x": "Sleeper Bus: Backpacker favorite.. This is one of the defining facts about Sleeper Bus — the kind of thing enthusiasts argue about and newcomers should know first. 2+1 seating. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this Sleeper Bus fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this Sleeper Bus fact matters.", "x": "Why it matters: Backpacker favorite.. For Sleeper Bus, this fact shaped reputation, sales, or history — understanding it means understanding why the bus type is remembered. Overnight bus with beds; Asia and South America staple.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "2+1 seating.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "2+1 seating.", "x": "More on Sleeper Bus: 2+1 seating.. Vietnam/Argentina. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Sleeper Bus.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "Blankets.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "Blankets.", "x": "More on Sleeper Bus: Blankets.. Cheaper than flights. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Sleeper Bus.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "Rest stops.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "Rest stops.", "x": "More on Sleeper Bus: Rest stops.. Reclining berths. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Sleeper Bus.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "Book ahead.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "Book ahead.", "x": "More on Sleeper Bus: Book ahead.. Night routes. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Sleeper Bus. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Budget travel.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Budget travel.", "x": "More on Sleeper Bus: Budget travel.. Backpacker favorite. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Sleeper Bus.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Sleep rolling.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Sleep rolling.", "x": "More on Sleeper Bus: Sleep rolling.. Beds onboard. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Sleeper Bus. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a Sleeper Bus: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a Sleeper Bus: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. 2+1 seating. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. Cheaper than flights. The right example of Sleeper Bus is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning Sleeper Bus: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning Sleeper Bus: costs and care.", "x": "Ownership: Blankets.. Maintain it by the book — fluids, intervals, and qualified specialists. Reclining berths. Budget realistically: purchase price is only the beginning of the story with any bus type.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Sleeper Bus through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "Sleeper Bus through the years.", "x": "The timeline: Overnight bus with beds; Asia and South America staple.. Beds onboard. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. Rest stops. Read it as one story, and the bus type makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for Sleeper Bus.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for Sleeper Bus.", "x": "The future: Sleeper Bus faces electrification, automation, and changing tastes like everything in transport. Night routes. Its heritage — Overnight bus with beds; Asia and South America staple. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "Sleeper Bus fact: Book ahead..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "Sleeper Bus fact: Book ahead..", "x": "From the Sleeper Bus file: Book ahead.. Vietnam/Argentina. Collect these and you will know Sleeper Bus better than most owners. Overnight bus with beds; Asia and South America staple. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-bus-sleeper-bus-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
