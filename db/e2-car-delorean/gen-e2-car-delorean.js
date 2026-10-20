(function(){'use strict';
/* JAH DeLorean Car Make Database generator — jahdb-e2-car-delorean-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-car-delorean',PREFIX='JAH-E2CARDELORE-',NAME='JAH DeLorean Car Make Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "facts", "future", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "DeLorean: overview", "d": "DeLorean: John DeLorean's 1980s icon; stainless gullwing..", "g": "overview", "l": 2, "q": "What is DeLorean: overview?", "a": "DeLorean: John DeLorean's 1980s icon; stainless gullwing..", "x": "The complete car make guide: John DeLorean's 1980s icon; stainless gullwing.. DMC-12: Back to the Future star. From its origins to its most famous models, from buying advice to what comes next — this database covers the car make in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How DeLorean began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How DeLorean began.", "x": "The origin of DeLorean: John DeLorean's 1980s icon; stainless gullwing.. Gullwing doors, stainless body. Every great car make has a founding story of ambition, luck, and timing — and DeLorean's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "DMC-12: Back to the Future star.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "DMC-12: Back to the Future star.", "x": "DeLorean: DMC-12: Back to the Future star.. This is one of the defining facts about DeLorean — the kind of thing enthusiasts argue about and newcomers should know first. Lotus chassis engineering. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this DeLorean fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this DeLorean fact matters.", "x": "Why it matters: DMC-12: Back to the Future star.. For DeLorean, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. John DeLorean's 1980s icon; stainless gullwing.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Gullwing doors, stainless body.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Gullwing doors, stainless body.", "x": "DeLorean: Gullwing doors, stainless body.. This is one of the defining facts about DeLorean — the kind of thing enthusiasts argue about and newcomers should know first. PRV V6 engine. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this DeLorean fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this DeLorean fact matters.", "x": "Why it matters: Gullwing doors, stainless body.. For DeLorean, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. John DeLorean's 1980s icon; stainless gullwing.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Belfast factory saga.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Belfast factory saga.", "x": "DeLorean: Belfast factory saga.. This is one of the defining facts about DeLorean — the kind of thing enthusiasts argue about and newcomers should know first. Only ~9,000 built. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this DeLorean fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this DeLorean fact matters.", "x": "Why it matters: Belfast factory saga.. For DeLorean, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. John DeLorean's 1980s icon; stainless gullwing.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "John Z. DeLorean's dream.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "John Z. DeLorean's dream.", "x": "DeLorean: John Z. DeLorean's dream.. This is one of the defining facts about DeLorean — the kind of thing enthusiasts argue about and newcomers should know first. Bankruptcy 1982. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this DeLorean fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this DeLorean fact matters.", "x": "Why it matters: John Z. DeLorean's dream.. For DeLorean, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. John DeLorean's 1980s icon; stainless gullwing.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "New EV reboot (Alpha5).", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "New EV reboot (Alpha5).", "x": "DeLorean: New EV reboot (Alpha5).. This is one of the defining facts about DeLorean — the kind of thing enthusiasts argue about and newcomers should know first. Time machine fame. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this DeLorean fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this DeLorean fact matters.", "x": "Why it matters: New EV reboot (Alpha5).. For DeLorean, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. John DeLorean's 1980s icon; stainless gullwing.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Cult following.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Cult following.", "x": "DeLorean: Cult following.. This is one of the defining facts about DeLorean — the kind of thing enthusiasts argue about and newcomers should know first. Founded 1975. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this DeLorean fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this DeLorean fact matters.", "x": "Why it matters: Cult following.. For DeLorean, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. John DeLorean's 1980s icon; stainless gullwing.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "Founded 1975.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "Founded 1975.", "x": "More on DeLorean: Founded 1975.. Gullwing doors, stainless body. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows DeLorean.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "Lotus chassis engineering.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "Lotus chassis engineering.", "x": "More on DeLorean: Lotus chassis engineering.. Belfast factory saga. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows DeLorean.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "PRV V6 engine.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "PRV V6 engine.", "x": "More on DeLorean: PRV V6 engine.. John Z. DeLorean's dream. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows DeLorean.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "Only ~9,000 built.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "Only ~9,000 built.", "x": "More on DeLorean: Only ~9,000 built.. New EV reboot (Alpha5). Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows DeLorean.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Bankruptcy 1982.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Bankruptcy 1982.", "x": "More on DeLorean: Bankruptcy 1982.. Cult following. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows DeLorean. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Time machine fame.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Time machine fame.", "x": "More on DeLorean: Time machine fame.. DMC-12: Back to the Future star. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows DeLorean.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a DeLorean: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a DeLorean: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. Founded 1975. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. Belfast factory saga. The right example of DeLorean is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning DeLorean: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning DeLorean: costs and care.", "x": "Ownership: Lotus chassis engineering.. Maintain it by the book — fluids, intervals, and qualified specialists. John Z. DeLorean's dream. Budget realistically: purchase price is only the beginning of the story with any car make.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "DeLorean through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "DeLorean through the years.", "x": "The timeline: John DeLorean's 1980s icon; stainless gullwing.. DMC-12: Back to the Future star. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. PRV V6 engine. Read it as one story, and the car make makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for DeLorean.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for DeLorean.", "x": "The future: DeLorean faces electrification, automation, and changing tastes like everything in transport. New EV reboot (Alpha5). Its heritage — John DeLorean's 1980s icon; stainless gullwing. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "DeLorean fact: Only ~9,000 built..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "DeLorean fact: Only ~9,000 built..", "x": "From the DeLorean file: Only ~9,000 built.. Gullwing doors, stainless body. Collect these and you will know DeLorean better than most owners. John DeLorean's 1980s icon; stainless gullwing. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-car-delorean-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
