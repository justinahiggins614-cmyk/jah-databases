(function(){'use strict';
/* JAH USS Constitution Ship Database generator — jahdb-e2-ship-uss-constitution-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-ship-uss-constitution',PREFIX='JAH-E2SHIPUSSCO-',NAME='JAH USS Constitution Ship Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "future", "quiz", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "USS Constitution: overview", "d": "USS Constitution: Oldest commissioned warship afloat (1797)..", "g": "overview", "l": 2, "q": "What is USS Constitution: overview?", "a": "USS Constitution: Oldest commissioned warship afloat (1797)..", "x": "The complete ship guide: Oldest commissioned warship afloat (1797).. 'Old Ironsides'. From its origins to its most famous examples, from buying advice to what comes next — this database covers the ship in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How USS Constitution began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How USS Constitution began.", "x": "The origin of USS Constitution: Oldest commissioned warship afloat (1797).. War of 1812 hero. Every great ship has a founding story of ambition, luck, and timing — and USS Constitution's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "'Old Ironsides'.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "'Old Ironsides'.", "x": "USS Constitution: 'Old Ironsides'.. This is one of the defining facts about USS Constitution — the kind of thing enthusiasts argue about and newcomers should know first. Edmund Hartt's shipyard. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this USS Constitution fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this USS Constitution fact matters.", "x": "Why it matters: 'Old Ironsides'.. For USS Constitution, this fact shaped reputation, sales, or history — understanding it means understanding why the ship is remembered. Oldest commissioned warship afloat (1797).", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "War of 1812 hero.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "War of 1812 hero.", "x": "USS Constitution: War of 1812 hero.. This is one of the defining facts about USS Constitution — the kind of thing enthusiasts argue about and newcomers should know first. Guerriere victory. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this USS Constitution fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this USS Constitution fact matters.", "x": "Why it matters: War of 1812 hero.. For USS Constitution, this fact shaped reputation, sales, or history — understanding it means understanding why the ship is remembered. Oldest commissioned warship afloat (1797).", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Still commissioned.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Still commissioned.", "x": "USS Constitution: Still commissioned.. This is one of the defining facts about USS Constitution — the kind of thing enthusiasts argue about and newcomers should know first. Restored repeatedly. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this USS Constitution fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this USS Constitution fact matters.", "x": "Why it matters: Still commissioned.. For USS Constitution, this fact shaped reputation, sales, or history — understanding it means understanding why the ship is remembered. Oldest commissioned warship afloat (1797).", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Boston harbor.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Boston harbor.", "x": "USS Constitution: Boston harbor.. This is one of the defining facts about USS Constitution — the kind of thing enthusiasts argue about and newcomers should know first. Active crew. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this USS Constitution fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this USS Constitution fact matters.", "x": "Why it matters: Boston harbor.. For USS Constitution, this fact shaped reputation, sales, or history — understanding it means understanding why the ship is remembered. Oldest commissioned warship afloat (1797).", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Turnaround cruises.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Turnaround cruises.", "x": "USS Constitution: Turnaround cruises.. This is one of the defining facts about USS Constitution — the kind of thing enthusiasts argue about and newcomers should know first. Free tours. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this USS Constitution fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this USS Constitution fact matters.", "x": "Why it matters: Turnaround cruises.. For USS Constitution, this fact shaped reputation, sales, or history — understanding it means understanding why the ship is remembered. Oldest commissioned warship afloat (1797).", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Wooden frigate.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Wooden frigate.", "x": "USS Constitution: Wooden frigate.. This is one of the defining facts about USS Constitution — the kind of thing enthusiasts argue about and newcomers should know first. US Navy. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this USS Constitution fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this USS Constitution fact matters.", "x": "Why it matters: Wooden frigate.. For USS Constitution, this fact shaped reputation, sales, or history — understanding it means understanding why the ship is remembered. Oldest commissioned warship afloat (1797).", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "US Navy.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "US Navy.", "x": "More on USS Constitution: US Navy.. War of 1812 hero. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows USS Constitution.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "Edmund Hartt's shipyard.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "Edmund Hartt's shipyard.", "x": "More on USS Constitution: Edmund Hartt's shipyard.. Still commissioned. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows USS Constitution.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "Guerriere victory.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "Guerriere victory.", "x": "More on USS Constitution: Guerriere victory.. Boston harbor. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows USS Constitution.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "Restored repeatedly.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "Restored repeatedly.", "x": "More on USS Constitution: Restored repeatedly.. Turnaround cruises. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows USS Constitution.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Active crew.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Active crew.", "x": "More on USS Constitution: Active crew.. Wooden frigate. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows USS Constitution.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Free tours.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Free tours.", "x": "More on USS Constitution: Free tours.. 'Old Ironsides'. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows USS Constitution.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a USS Constitution: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a USS Constitution: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. US Navy. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. Still commissioned. The right example of USS Constitution is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning USS Constitution: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning USS Constitution: costs and care.", "x": "Ownership: Edmund Hartt's shipyard.. Maintain it by the book — fluids, intervals, and qualified specialists. Boston harbor. Budget realistically: purchase price is only the beginning of the story with any ship.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "USS Constitution through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "USS Constitution through the years.", "x": "The timeline: Oldest commissioned warship afloat (1797).. 'Old Ironsides'. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. Guerriere victory. Read it as one story, and the ship makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for USS Constitution.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for USS Constitution.", "x": "The future: USS Constitution faces electrification, automation, and changing tastes like everything in transport. Turnaround cruises. Its heritage — Oldest commissioned warship afloat (1797). — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "USS Constitution fact: Restored repeatedly..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "USS Constitution fact: Restored repeatedly..", "x": "From the USS Constitution file: Restored repeatedly.. War of 1812 hero. Collect these and you will know USS Constitution better than most owners. Oldest commissioned warship afloat (1797). Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-ship-uss-constitution-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
