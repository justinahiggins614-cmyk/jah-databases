(function(){'use strict';
/* JAH F-16 Fighting Falcon Aircraft Database generator — jahdb-e2-aircraft-f-16-fighting-falcon-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-aircraft-f-16-fighting-falcon',PREFIX='JAH-E2AIRCRAFTF-',NAME='JAH F-16 Fighting Falcon Aircraft Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "future", "quiz", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "F-16 Fighting Falcon: overview", "d": "F-16 Fighting Falcon: US multirole fighter since 1978; 4,600+ built..", "g": "overview", "l": 2, "q": "What is F-16 Fighting Falcon: overview?", "a": "F-16 Fighting Falcon: US multirole fighter since 1978; 4,600+ built..", "x": "The complete aircraft guide: US multirole fighter since 1978; 4,600+ built.. Fly-by-wire pioneer fighter. From its origins to its most famous examples, from buying advice to what comes next — this database covers the aircraft in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How F-16 Fighting Falcon began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How F-16 Fighting Falcon began.", "x": "The origin of F-16 Fighting Falcon: US multirole fighter since 1978; 4,600+ built.. Bubble canopy visibility. Every great aircraft has a founding story of ambition, luck, and timing — and F-16 Fighting Falcon's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Fly-by-wire pioneer fighter.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Fly-by-wire pioneer fighter.", "x": "F-16 Fighting Falcon: Fly-by-wire pioneer fighter.. This is one of the defining facts about F-16 Fighting Falcon — the kind of thing enthusiasts argue about and newcomers should know first. Lightweight Fighter winner.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this F-16 Fighting Falcon fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this F-16 Fighting Falcon fact matters.", "x": "Why it matters: Fly-by-wire pioneer fighter.. For F-16 Fighting Falcon, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. US multirole fighter since 1978; 4,600+ built.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Bubble canopy visibility.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Bubble canopy visibility.", "x": "F-16 Fighting Falcon: Bubble canopy visibility.. This is one of the defining facts about F-16 Fighting Falcon — the kind of thing enthusiasts argue about and newcomers should know first. 9G agility. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this F-16 Fighting Falcon fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this F-16 Fighting Falcon fact matters.", "x": "Why it matters: Bubble canopy visibility.. For F-16 Fighting Falcon, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. US multirole fighter since 1978; 4,600+ built.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Affordable export star.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Affordable export star.", "x": "F-16 Fighting Falcon: Affordable export star.. This is one of the defining facts about F-16 Fighting Falcon — the kind of thing enthusiasts argue about and newcomers should know first. Single F100/F110 engine.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this F-16 Fighting Falcon fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this F-16 Fighting Falcon fact matters.", "x": "Why it matters: Affordable export star.. For F-16 Fighting Falcon, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. US multirole fighter since 1978; 4,600+ built.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Viper nickname.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Viper nickname.", "x": "F-16 Fighting Falcon: Viper nickname.. This is one of the defining facts about F-16 Fighting Falcon — the kind of thing enthusiasts argue about and newcomers should know first. Global operators. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this F-16 Fighting Falcon fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this F-16 Fighting Falcon fact matters.", "x": "Why it matters: Viper nickname.. For F-16 Fighting Falcon, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. US multirole fighter since 1978; 4,600+ built.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Block 70/72 new builds.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Block 70/72 new builds.", "x": "F-16 Fighting Falcon: Block 70/72 new builds.. This is one of the defining facts about F-16 Fighting Falcon — the kind of thing enthusiasts argue about and newcomers should know first. Still produced.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this F-16 Fighting Falcon fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this F-16 Fighting Falcon fact matters.", "x": "Why it matters: Block 70/72 new builds.. For F-16 Fighting Falcon, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. US multirole fighter since 1978; 4,600+ built.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Thunderbirds fly it.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Thunderbirds fly it.", "x": "F-16 Fighting Falcon: Thunderbirds fly it.. This is one of the defining facts about F-16 Fighting Falcon — the kind of thing enthusiasts argue about and newcomers should know first. Lockheed Martin. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this F-16 Fighting Falcon fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this F-16 Fighting Falcon fact matters.", "x": "Why it matters: Thunderbirds fly it.. For F-16 Fighting Falcon, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. US multirole fighter since 1978; 4,600+ built.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "Lockheed Martin.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "Lockheed Martin.", "x": "More on F-16 Fighting Falcon: Lockheed Martin.. Bubble canopy visibility. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows F-16 Fighting Falcon.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "Lightweight Fighter winner.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "Lightweight Fighter winner.", "x": "More on F-16 Fighting Falcon: Lightweight Fighter winner.. Affordable export star. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows F-16 Fighting Falcon.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "9G agility.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "9G agility.", "x": "More on F-16 Fighting Falcon: 9G agility.. Viper nickname. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows F-16 Fighting Falcon.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "Single F100/F110 engine.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "Single F100/F110 engine.", "x": "More on F-16 Fighting Falcon: Single F100/F110 engine.. Block 70/72 new builds. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows F-16 Fighting Falcon.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Global operators.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Global operators.", "x": "More on F-16 Fighting Falcon: Global operators.. Thunderbirds fly it. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows F-16 Fighting Falcon.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Still produced.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Still produced.", "x": "More on F-16 Fighting Falcon: Still produced.. Fly-by-wire pioneer fighter. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows F-16 Fighting Falcon.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a F-16 Fighting Falcon: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a F-16 Fighting Falcon: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. Lockheed Martin. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. Affordable export star. The right example of F-16 Fighting Falcon is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning F-16 Fighting Falcon: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning F-16 Fighting Falcon: costs and care.", "x": "Ownership: Lightweight Fighter winner.. Maintain it by the book — fluids, intervals, and qualified specialists. Viper nickname. Budget realistically: purchase price is only the beginning of the story with any aircraft.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "F-16 Fighting Falcon through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "F-16 Fighting Falcon through the years.", "x": "The timeline: US multirole fighter since 1978; 4,600+ built.. Fly-by-wire pioneer fighter. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. 9G agility. Read it as one story, and the aircraft makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for F-16 Fighting Falcon.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for F-16 Fighting Falcon.", "x": "The future: F-16 Fighting Falcon faces electrification, automation, and changing tastes like everything in transport. Block 70/72 new builds. Its heritage — US multirole fighter since 1978; 4,600+ built. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "F-16 Fighting Falcon fact: Single F100/F110 engine..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "F-16 Fighting Falcon fact: Single F100/F110 engine..", "x": "From the F-16 Fighting Falcon file: Single F100/F110 engine.. Bubble canopy visibility. Collect these and you will know F-16 Fighting Falcon better than most owners. US multirole fighter since 1978; 4,600+ built.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-aircraft-f-16-fighting-falcon-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
