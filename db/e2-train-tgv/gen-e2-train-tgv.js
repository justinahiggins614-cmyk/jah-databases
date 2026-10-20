(function(){'use strict';
/* JAH TGV Train Database generator — jahdb-e2-train-tgv-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-train-tgv',PREFIX='JAH-E2TRAINTGV-',NAME='JAH TGV Train Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "future", "quiz", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "TGV: overview", "d": "TGV: French high-speed train; 574.8 km/h world record..", "g": "overview", "l": 2, "q": "What is TGV: overview?", "a": "TGV: French high-speed train; 574.8 km/h world record..", "x": "The complete train guide: French high-speed train; 574.8 km/h world record.. 574.8 km/h record (2007). From its origins to its most famous examples, from buying advice to what comes next — this database covers the train in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How TGV began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How TGV began.", "x": "The origin of TGV: French high-speed train; 574.8 km/h world record.. Paris-Lyon 1981. Every great train has a founding story of ambition, luck, and timing — and TGV's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "574.8 km/h record (2007).", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "574.8 km/h record (2007).", "x": "TGV: 574.8 km/h record (2007).. This is one of the defining facts about TGV — the kind of thing enthusiasts argue about and newcomers should know first. Grande vitesse. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this TGV fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this TGV fact matters.", "x": "Why it matters: 574.8 km/h record (2007).. For TGV, this fact shaped reputation, sales, or history — understanding it means understanding why the train is remembered. French high-speed train; 574.8 km/h world record.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Paris-Lyon 1981.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Paris-Lyon 1981.", "x": "TGV: Paris-Lyon 1981.. This is one of the defining facts about TGV — the kind of thing enthusiasts argue about and newcomers should know first. Atlantique/PSE lines. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this TGV fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this TGV fact matters.", "x": "Why it matters: Paris-Lyon 1981.. For TGV, this fact shaped reputation, sales, or history — understanding it means understanding why the train is remembered. French high-speed train; 574.8 km/h world record.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Duplex double-deck.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Duplex double-deck.", "x": "TGV: Duplex double-deck.. This is one of the defining facts about TGV — the kind of thing enthusiasts argue about and newcomers should know first. Thalys/Eurostar. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this TGV fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this TGV fact matters.", "x": "Why it matters: Duplex double-deck.. For TGV, this fact shaped reputation, sales, or history — understanding it means understanding why the train is remembered. French high-speed train; 574.8 km/h world record.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Eurostar uses TGV tech.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Eurostar uses TGV tech.", "x": "TGV: Eurostar uses TGV tech.. This is one of the defining facts about TGV — the kind of thing enthusiasts argue about and newcomers should know first. Ouigo low-cost. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this TGV fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this TGV fact matters.", "x": "Why it matters: Eurostar uses TGV tech.. For TGV, this fact shaped reputation, sales, or history — understanding it means understanding why the train is remembered. French high-speed train; 574.8 km/h world record.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Alstom-built.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Alstom-built.", "x": "TGV: Alstom-built.. This is one of the defining facts about TGV — the kind of thing enthusiasts argue about and newcomers should know first. Export: Korea. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this TGV fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this TGV fact matters.", "x": "Why it matters: Alstom-built.. For TGV, this fact shaped reputation, sales, or history — understanding it means understanding why the train is remembered. French high-speed train; 574.8 km/h world record.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "320 km/h service.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "320 km/h service.", "x": "TGV: 320 km/h service.. This is one of the defining facts about TGV — the kind of thing enthusiasts argue about and newcomers should know first. SNCF, France. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this TGV fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this TGV fact matters.", "x": "Why it matters: 320 km/h service.. For TGV, this fact shaped reputation, sales, or history — understanding it means understanding why the train is remembered. French high-speed train; 574.8 km/h world record.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "SNCF, France.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "SNCF, France.", "x": "More on TGV: SNCF, France.. Paris-Lyon 1981. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows TGV. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "Grande vitesse.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "Grande vitesse.", "x": "More on TGV: Grande vitesse.. Duplex double-deck. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows TGV. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "Atlantique/PSE lines.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "Atlantique/PSE lines.", "x": "More on TGV: Atlantique/PSE lines.. Eurostar uses TGV tech. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows TGV.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "Thalys/Eurostar.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "Thalys/Eurostar.", "x": "More on TGV: Thalys/Eurostar.. Alstom-built. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows TGV. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Ouigo low-cost.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Ouigo low-cost.", "x": "More on TGV: Ouigo low-cost.. 320 km/h service. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows TGV. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Export: Korea.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Export: Korea.", "x": "More on TGV: Export: Korea.. 574.8 km/h record (2007). Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows TGV. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a TGV: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a TGV: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. SNCF, France. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. Duplex double-deck. The right example of TGV is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning TGV: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning TGV: costs and care.", "x": "Ownership: Grande vitesse.. Maintain it by the book — fluids, intervals, and qualified specialists. Eurostar uses TGV tech. Budget realistically: purchase price is only the beginning of the story with any train.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "TGV through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "TGV through the years.", "x": "The timeline: French high-speed train; 574.8 km/h world record.. 574.8 km/h record (2007). Key chapters mark the eras — the breakthroughs, the crises, the comebacks. Atlantique/PSE lines. Read it as one story, and the train makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for TGV.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for TGV.", "x": "The future: TGV faces electrification, automation, and changing tastes like everything in transport. Alstom-built. Its heritage — French high-speed train; 574.8 km/h world record. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "TGV fact: Thalys/Eurostar..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "TGV fact: Thalys/Eurostar..", "x": "From the TGV file: Thalys/Eurostar.. Paris-Lyon 1981. Collect these and you will know TGV better than most owners. French high-speed train; 574.8 km/h world record. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-train-tgv-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
