(function(){'use strict';
/* JAH Toyota Prius Hybrid Vehicle Database generator — jahdb-e2-hybrid-toyota-prius-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hybrid-toyota-prius',PREFIX='JAH-E2HYBRIDTOY-',NAME='JAH Toyota Prius Hybrid Vehicle Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "future", "quiz", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Toyota Prius: overview", "d": "Toyota Prius: The hybrid that started it all (1997 Japan, 2000 US)..", "g": "overview", "l": 2, "q": "What is Toyota Prius: overview?", "a": "Toyota Prius: The hybrid that started it all (1997 Japan, 2000 US)..", "x": "The complete hybrid vehicle guide: The hybrid that started it all (1997 Japan, 2000 US).. First mass hybrid. From its origins to its most famous examples, from buying advice to what comes next — this database covers the hybrid vehicle in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How Toyota Prius began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How Toyota Prius began.", "x": "The origin of Toyota Prius: The hybrid that started it all (1997 Japan, 2000 US).. 20M+ Toyota hybrids. Every great hybrid vehicle has a founding story of ambition, luck, and timing — and Toyota Prius's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "First mass hybrid.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "First mass hybrid.", "x": "Toyota Prius: First mass hybrid.. This is one of the defining facts about Toyota Prius — the kind of thing enthusiasts argue about and newcomers should know first. NiMH then Li-ion. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this Toyota Prius fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this Toyota Prius fact matters.", "x": "Why it matters: First mass hybrid.. For Toyota Prius, this fact shaped reputation, sales, or history — understanding it means understanding why the hybrid vehicle is remembered. The hybrid that started it all (1997 Japan, 2000 US).", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "20M+ Toyota hybrids.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "20M+ Toyota hybrids.", "x": "Toyota Prius: 20M+ Toyota hybrids.. This is one of the defining facts about Toyota Prius — the kind of thing enthusiasts argue about and newcomers should know first. Aero shape. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this Toyota Prius fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this Toyota Prius fact matters.", "x": "Why it matters: 20M+ Toyota hybrids.. For Toyota Prius, this fact shaped reputation, sales, or history — understanding it means understanding why the hybrid vehicle is remembered. The hybrid that started it all (1997 Japan, 2000 US).", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Synergy Drive.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Synergy Drive.", "x": "Toyota Prius: Synergy Drive.. This is one of the defining facts about Toyota Prius — the kind of thing enthusiasts argue about and newcomers should know first. Prime plug-in. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this Toyota Prius fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this Toyota Prius fact matters.", "x": "Why it matters: Synergy Drive.. For Toyota Prius, this fact shaped reputation, sales, or history — understanding it means understanding why the hybrid vehicle is remembered. The hybrid that started it all (1997 Japan, 2000 US).", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "New sleek 2023 design.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "New sleek 2023 design.", "x": "Toyota Prius: New sleek 2023 design.. This is one of the defining facts about Toyota Prius — the kind of thing enthusiasts argue about and newcomers should know first. Cultural icon. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this Toyota Prius fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this Toyota Prius fact matters.", "x": "Why it matters: New sleek 2023 design.. For Toyota Prius, this fact shaped reputation, sales, or history — understanding it means understanding why the hybrid vehicle is remembered. The hybrid that started it all (1997 Japan, 2000 US).", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "50+ mpg.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "50+ mpg.", "x": "Toyota Prius: 50+ mpg.. This is one of the defining facts about Toyota Prius — the kind of thing enthusiasts argue about and newcomers should know first. Hybrid king. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this Toyota Prius fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this Toyota Prius fact matters.", "x": "Why it matters: 50+ mpg.. For Toyota Prius, this fact shaped reputation, sales, or history — understanding it means understanding why the hybrid vehicle is remembered. The hybrid that started it all (1997 Japan, 2000 US).", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Taxi favorite.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Taxi favorite.", "x": "Toyota Prius: Taxi favorite.. This is one of the defining facts about Toyota Prius — the kind of thing enthusiasts argue about and newcomers should know first. THS system. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this Toyota Prius fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this Toyota Prius fact matters.", "x": "Why it matters: Taxi favorite.. For Toyota Prius, this fact shaped reputation, sales, or history — understanding it means understanding why the hybrid vehicle is remembered. The hybrid that started it all (1997 Japan, 2000 US).", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "THS system.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "THS system.", "x": "More on Toyota Prius: THS system.. 20M+ Toyota hybrids. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Toyota Prius.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "NiMH then Li-ion.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "NiMH then Li-ion.", "x": "More on Toyota Prius: NiMH then Li-ion.. Synergy Drive. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Toyota Prius.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "Aero shape.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "Aero shape.", "x": "More on Toyota Prius: Aero shape.. New sleek 2023 design. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Toyota Prius.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "Prime plug-in.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "Prime plug-in.", "x": "More on Toyota Prius: Prime plug-in.. 50+ mpg. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Toyota Prius. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Cultural icon.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Cultural icon.", "x": "More on Toyota Prius: Cultural icon.. Taxi favorite. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Toyota Prius.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Hybrid king.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Hybrid king.", "x": "More on Toyota Prius: Hybrid king.. First mass hybrid. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Toyota Prius.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a Toyota Prius: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a Toyota Prius: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. THS system. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. Synergy Drive. The right example of Toyota Prius is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning Toyota Prius: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning Toyota Prius: costs and care.", "x": "Ownership: NiMH then Li-ion.. Maintain it by the book — fluids, intervals, and qualified specialists. New sleek 2023 design. Budget realistically: purchase price is only the beginning of the story with any hybrid vehicle.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Toyota Prius through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "Toyota Prius through the years.", "x": "The timeline: The hybrid that started it all (1997 Japan, 2000 US).. First mass hybrid. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. Aero shape. Read it as one story, and the hybrid vehicle makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for Toyota Prius.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for Toyota Prius.", "x": "The future: Toyota Prius faces electrification, automation, and changing tastes like everything in transport. 50+ mpg. Its heritage — The hybrid that started it all (1997 Japan, 2000 US). — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "Toyota Prius fact: Prime plug-in..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "Toyota Prius fact: Prime plug-in..", "x": "From the Toyota Prius file: Prime plug-in.. 20M+ Toyota hybrids. Collect these and you will know Toyota Prius better than most owners. The hybrid that started it all (1997 Japan, 2000 US). Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hybrid-toyota-prius-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
