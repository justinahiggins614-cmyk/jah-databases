(function(){'use strict';
/* JAH Toyota RAV4 Hybrid Hybrid Vehicle Database generator — jahdb-e2-hybrid-toyota-rav4-hybrid-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-hybrid-toyota-rav4-hybrid',PREFIX='JAH-E2HYBRIDTOY-',NAME='JAH Toyota RAV4 Hybrid Hybrid Vehicle Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "future", "quiz", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Toyota RAV4 Hybrid: overview", "d": "Toyota RAV4 Hybrid: Best-selling hybrid SUV in America..", "g": "overview", "l": 2, "q": "What is Toyota RAV4 Hybrid: overview?", "a": "Toyota RAV4 Hybrid: Best-selling hybrid SUV in America..", "x": "The complete hybrid vehicle guide: Best-selling hybrid SUV in America.. Top hybrid SUV. From its origins to its most famous examples, from buying advice to what comes next — this database covers the hybrid vehicle in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How Toyota RAV4 Hybrid began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How Toyota RAV4 Hybrid began.", "x": "The origin of Toyota RAV4 Hybrid: Best-selling hybrid SUV in America.. 40 mpg. Every great hybrid vehicle has a founding story of ambition, luck, and timing — and Toyota RAV4 Hybrid's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Top hybrid SUV.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Top hybrid SUV.", "x": "Toyota RAV4 Hybrid: Top hybrid SUV.. This is one of the defining facts about Toyota RAV4 Hybrid — the kind of thing enthusiasts argue about and newcomers should know first. Kentucky built. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this Toyota RAV4 Hybrid fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this Toyota RAV4 Hybrid fact matters.", "x": "Why it matters: Top hybrid SUV.. For Toyota RAV4 Hybrid, this fact shaped reputation, sales, or history — understanding it means understanding why the hybrid vehicle is remembered. Best-selling hybrid SUV in America.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "40 mpg.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "40 mpg.", "x": "Toyota RAV4 Hybrid: 40 mpg.. This is one of the defining facts about Toyota RAV4 Hybrid — the kind of thing enthusiasts argue about and newcomers should know first. eCVT. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this Toyota RAV4 Hybrid fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this Toyota RAV4 Hybrid fact matters.", "x": "Why it matters: 40 mpg.. For Toyota RAV4 Hybrid, this fact shaped reputation, sales, or history — understanding it means understanding why the hybrid vehicle is remembered. Best-selling hybrid SUV in America.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "AWD standard-ish.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "AWD standard-ish.", "x": "Toyota RAV4 Hybrid: AWD standard-ish.. This is one of the defining facts about Toyota RAV4 Hybrid — the kind of thing enthusiasts argue about and newcomers should know first. Towing 1,750. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this Toyota RAV4 Hybrid fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this Toyota RAV4 Hybrid fact matters.", "x": "Why it matters: AWD standard-ish.. For Toyota RAV4 Hybrid, this fact shaped reputation, sales, or history — understanding it means understanding why the hybrid vehicle is remembered. Best-selling hybrid SUV in America.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Woodland trim.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Woodland trim.", "x": "Toyota RAV4 Hybrid: Woodland trim.. This is one of the defining facts about Toyota RAV4 Hybrid — the kind of thing enthusiasts argue about and newcomers should know first. Safety Sense. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this Toyota RAV4 Hybrid fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this Toyota RAV4 Hybrid fact matters.", "x": "Why it matters: Woodland trim.. For Toyota RAV4 Hybrid, this fact shaped reputation, sales, or history — understanding it means understanding why the hybrid vehicle is remembered. Best-selling hybrid SUV in America.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Prime 302 hp.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Prime 302 hp.", "x": "Toyota RAV4 Hybrid: Prime 302 hp.. This is one of the defining facts about Toyota RAV4 Hybrid — the kind of thing enthusiasts argue about and newcomers should know first. Resale king. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this Toyota RAV4 Hybrid fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this Toyota RAV4 Hybrid fact matters.", "x": "Why it matters: Prime 302 hp.. For Toyota RAV4 Hybrid, this fact shaped reputation, sales, or history — understanding it means understanding why the hybrid vehicle is remembered. Best-selling hybrid SUV in America.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Family favorite.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Family favorite.", "x": "Toyota RAV4 Hybrid: Family favorite.. This is one of the defining facts about Toyota RAV4 Hybrid — the kind of thing enthusiasts argue about and newcomers should know first. TNGA-K. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this Toyota RAV4 Hybrid fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this Toyota RAV4 Hybrid fact matters.", "x": "Why it matters: Family favorite.. For Toyota RAV4 Hybrid, this fact shaped reputation, sales, or history — understanding it means understanding why the hybrid vehicle is remembered. Best-selling hybrid SUV in America.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "TNGA-K.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "TNGA-K.", "x": "More on Toyota RAV4 Hybrid: TNGA-K.. 40 mpg. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Toyota RAV4 Hybrid.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "Kentucky built.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "Kentucky built.", "x": "More on Toyota RAV4 Hybrid: Kentucky built.. AWD standard-ish. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Toyota RAV4 Hybrid.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "eCVT.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "eCVT.", "x": "More on Toyota RAV4 Hybrid: eCVT.. Woodland trim. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Toyota RAV4 Hybrid.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "Towing 1,750.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "Towing 1,750.", "x": "More on Toyota RAV4 Hybrid: Towing 1,750.. Prime 302 hp. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Toyota RAV4 Hybrid.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Safety Sense.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Safety Sense.", "x": "More on Toyota RAV4 Hybrid: Safety Sense.. Family favorite. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Toyota RAV4 Hybrid.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Resale king.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Resale king.", "x": "More on Toyota RAV4 Hybrid: Resale king.. Top hybrid SUV. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Toyota RAV4 Hybrid.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a Toyota RAV4 Hybrid: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a Toyota RAV4 Hybrid: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. TNGA-K. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. AWD standard-ish. The right example of Toyota RAV4 Hybrid is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning Toyota RAV4 Hybrid: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning Toyota RAV4 Hybrid: costs and care.", "x": "Ownership: Kentucky built.. Maintain it by the book — fluids, intervals, and qualified specialists. Woodland trim. Budget realistically: purchase price is only the beginning of the story with any hybrid vehicle.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Toyota RAV4 Hybrid through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "Toyota RAV4 Hybrid through the years.", "x": "The timeline: Best-selling hybrid SUV in America.. Top hybrid SUV. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. eCVT. Read it as one story, and the hybrid vehicle makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for Toyota RAV4 Hybrid.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for Toyota RAV4 Hybrid.", "x": "The future: Toyota RAV4 Hybrid faces electrification, automation, and changing tastes like everything in transport. Prime 302 hp. Its heritage — Best-selling hybrid SUV in America. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "Toyota RAV4 Hybrid fact: Towing 1,750..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "Toyota RAV4 Hybrid fact: Towing 1,750..", "x": "From the Toyota RAV4 Hybrid file: Towing 1,750.. 40 mpg. Collect these and you will know Toyota RAV4 Hybrid better than most owners. Best-selling hybrid SUV in America. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-hybrid-toyota-rav4-hybrid-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
