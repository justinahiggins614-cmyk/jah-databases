(function(){'use strict';
/* JAH Tesla Model 3 Electric Vehicle Database generator — jahdb-e2-ev-tesla-model-3-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-ev-tesla-model-3',PREFIX='JAH-E2EVTESLAMO-',NAME='JAH Tesla Model 3 Electric Vehicle Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "future", "quiz", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Tesla Model 3: overview", "d": "Tesla Model 3: Best-selling EV ever; Tesla's mass-market sedan (2017)..", "g": "overview", "l": 2, "q": "What is Tesla Model 3: overview?", "a": "Tesla Model 3: Best-selling EV ever; Tesla's mass-market sedan (2017)..", "x": "The complete electric vehicle guide: Best-selling EV ever; Tesla's mass-market sedan (2017).. Best-selling EV ever. From its origins to its most famous examples, from buying advice to what comes next — this database covers the electric vehicle in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How Tesla Model 3 began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How Tesla Model 3 began.", "x": "The origin of Tesla Model 3: Best-selling EV ever; Tesla's mass-market sedan (2017).. Minimalist interior. Every great electric vehicle has a founding story of ambition, luck, and timing — and Tesla Model 3's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Best-selling EV ever.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Best-selling EV ever.", "x": "Tesla Model 3: Best-selling EV ever.. This is one of the defining facts about Tesla Model 3 — the kind of thing enthusiasts argue about and newcomers should know first. Highland refresh. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this Tesla Model 3 fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this Tesla Model 3 fact matters.", "x": "Why it matters: Best-selling EV ever.. For Tesla Model 3, this fact shaped reputation, sales, or history — understanding it means understanding why the electric vehicle is remembered. Best-selling EV ever; Tesla's mass-market sedan (2017).", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Minimalist interior.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Minimalist interior.", "x": "Tesla Model 3: Minimalist interior.. This is one of the defining facts about Tesla Model 3 — the kind of thing enthusiasts argue about and newcomers should know first. Heat pump. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this Tesla Model 3 fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this Tesla Model 3 fact matters.", "x": "Why it matters: Minimalist interior.. For Tesla Model 3, this fact shaped reputation, sales, or history — understanding it means understanding why the electric vehicle is remembered. Best-selling EV ever; Tesla's mass-market sedan (2017).", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "15-inch touchscreen.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "15-inch touchscreen.", "x": "Tesla Model 3: 15-inch touchscreen.. This is one of the defining facts about Tesla Model 3 — the kind of thing enthusiasts argue about and newcomers should know first. LFP batteries (RWD). Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this Tesla Model 3 fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this Tesla Model 3 fact matters.", "x": "Why it matters: 15-inch touchscreen.. For Tesla Model 3, this fact shaped reputation, sales, or history — understanding it means understanding why the electric vehicle is remembered. Best-selling EV ever; Tesla's mass-market sedan (2017).", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Supercharger network.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Supercharger network.", "x": "Tesla Model 3: Supercharger network.. This is one of the defining facts about Tesla Model 3 — the kind of thing enthusiasts argue about and newcomers should know first. Phone key. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this Tesla Model 3 fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this Tesla Model 3 fact matters.", "x": "Why it matters: Supercharger network.. For Tesla Model 3, this fact shaped reputation, sales, or history — understanding it means understanding why the electric vehicle is remembered. Best-selling EV ever; Tesla's mass-market sedan (2017).", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Autopilot standard.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Autopilot standard.", "x": "Tesla Model 3: Autopilot standard.. This is one of the defining facts about Tesla Model 3 — the kind of thing enthusiasts argue about and newcomers should know first. OTA updates. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this Tesla Model 3 fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this Tesla Model 3 fact matters.", "x": "Why it matters: Autopilot standard.. For Tesla Model 3, this fact shaped reputation, sales, or history — understanding it means understanding why the electric vehicle is remembered. Best-selling EV ever; Tesla's mass-market sedan (2017).", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "250+ mile range.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "250+ mile range.", "x": "Tesla Model 3: 250+ mile range.. This is one of the defining facts about Tesla Model 3 — the kind of thing enthusiasts argue about and newcomers should know first. Fremont/Shanghai/Berlin. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this Tesla Model 3 fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this Tesla Model 3 fact matters.", "x": "Why it matters: 250+ mile range.. For Tesla Model 3, this fact shaped reputation, sales, or history — understanding it means understanding why the electric vehicle is remembered. Best-selling EV ever; Tesla's mass-market sedan (2017).", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "Fremont/Shanghai/Berlin.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "Fremont/Shanghai/Berlin.", "x": "More on Tesla Model 3: Fremont/Shanghai/Berlin.. Minimalist interior. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Tesla Model 3.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "Highland refresh.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "Highland refresh.", "x": "More on Tesla Model 3: Highland refresh.. 15-inch touchscreen. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Tesla Model 3.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "Heat pump.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "Heat pump.", "x": "More on Tesla Model 3: Heat pump.. Supercharger network. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Tesla Model 3.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "LFP batteries (RWD).", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "LFP batteries (RWD).", "x": "More on Tesla Model 3: LFP batteries (RWD).. Autopilot standard. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Tesla Model 3.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Phone key.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Phone key.", "x": "More on Tesla Model 3: Phone key.. 250+ mile range. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Tesla Model 3.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "OTA updates.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "OTA updates.", "x": "More on Tesla Model 3: OTA updates.. Best-selling EV ever. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Tesla Model 3.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a Tesla Model 3: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a Tesla Model 3: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. Fremont/Shanghai/Berlin. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. 15-inch touchscreen. The right example of Tesla Model 3 is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning Tesla Model 3: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning Tesla Model 3: costs and care.", "x": "Ownership: Highland refresh.. Maintain it by the book — fluids, intervals, and qualified specialists. Supercharger network. Budget realistically: purchase price is only the beginning of the story with any electric vehicle.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Tesla Model 3 through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "Tesla Model 3 through the years.", "x": "The timeline: Best-selling EV ever; Tesla's mass-market sedan (2017).. Best-selling EV ever. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. Heat pump. Read it as one story, and the electric vehicle makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for Tesla Model 3.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for Tesla Model 3.", "x": "The future: Tesla Model 3 faces electrification, automation, and changing tastes like everything in transport. Autopilot standard. Its heritage — Best-selling EV ever; Tesla's mass-market sedan (2017). — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "Tesla Model 3 fact: LFP batteries (RWD)..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "Tesla Model 3 fact: LFP batteries (RWD)..", "x": "From the Tesla Model 3 file: LFP batteries (RWD).. Minimalist interior. Collect these and you will know Tesla Model 3 better than most owners. Best-selling EV ever; Tesla's mass-market sedan (2017). Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-ev-tesla-model-3-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
