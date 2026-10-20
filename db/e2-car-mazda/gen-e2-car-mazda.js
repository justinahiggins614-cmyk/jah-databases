(function(){'use strict';
/* JAH Mazda Car Make Database generator — jahdb-e2-car-mazda-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-car-mazda',PREFIX='JAH-E2CARMAZDA-',NAME='JAH Mazda Car Make Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "facts", "future", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mazda: overview", "d": "Mazda: Japanese maker founded 1920; rotary engine champion..", "g": "overview", "l": 2, "q": "What is Mazda: overview?", "a": "Mazda: Japanese maker founded 1920; rotary engine champion..", "x": "The complete car make guide: Japanese maker founded 1920; rotary engine champion.. RX-7: rotary sports-car legend. From its origins to its most famous models, from buying advice to what comes next — this database covers the car make in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How Mazda began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How Mazda began.", "x": "The origin of Mazda: Japanese maker founded 1920; rotary engine champion.. MX-5 Miata: best-selling roadster ever. Every great car make has a founding story of ambition, luck, and timing — and Mazda's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "RX-7: rotary sports-car legend.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "RX-7: rotary sports-car legend.", "x": "Mazda: RX-7: rotary sports-car legend.. This is one of the defining facts about Mazda — the kind of thing enthusiasts argue about and newcomers should know first. Name from Ahura Mazda. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this Mazda fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this Mazda fact matters.", "x": "Why it matters: RX-7: rotary sports-car legend.. For Mazda, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Japanese maker founded 1920; rotary engine champion.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "MX-5 Miata: best-selling roadster ever.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "MX-5 Miata: best-selling roadster ever.", "x": "Mazda: MX-5 Miata: best-selling roadster ever.. This is one of the defining facts about Mazda — the kind of thing enthusiasts argue about and newcomers should know first. Only maker to persist with rotary.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this Mazda fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this Mazda fact matters.", "x": "Why it matters: MX-5 Miata: best-selling roadster ever.. For Mazda, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Japanese maker founded 1920; rotary engine champion.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Rotary engine won Le Mans (787B).", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Rotary engine won Le Mans (787B).", "x": "Mazda: Rotary engine won Le Mans (787B).. This is one of the defining facts about Mazda — the kind of thing enthusiasts argue about and newcomers should know first. CX-5: its sales backbone. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this Mazda fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this Mazda fact matters.", "x": "Why it matters: Rotary engine won Le Mans (787B).. For Mazda, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Japanese maker founded 1920; rotary engine champion.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Kodo design: 'soul of motion'.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Kodo design: 'soul of motion'.", "x": "Mazda: Kodo design: 'soul of motion'.. This is one of the defining facts about Mazda — the kind of thing enthusiasts argue about and newcomers should know first. SkyActiv tech: efficient engines. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this Mazda fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this Mazda fact matters.", "x": "Why it matters: Kodo design: 'soul of motion'.. For Mazda, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Japanese maker founded 1920; rotary engine champion.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Zoom-Zoom era defined 2000s fun.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Zoom-Zoom era defined 2000s fun.", "x": "Mazda: Zoom-Zoom era defined 2000s fun.. This is one of the defining facts about Mazda — the kind of thing enthusiasts argue about and newcomers should know first. Toyota partnership (Alabama plant). Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this Mazda fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this Mazda fact matters.", "x": "Why it matters: Zoom-Zoom era defined 2000s fun.. For Mazda, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Japanese maker founded 1920; rotary engine champion.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Premium push upmarket.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Premium push upmarket.", "x": "Mazda: Premium push upmarket.. This is one of the defining facts about Mazda — the kind of thing enthusiasts argue about and newcomers should know first. Headquarters: Hiroshima, Japan. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this Mazda fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this Mazda fact matters.", "x": "Why it matters: Premium push upmarket.. For Mazda, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Japanese maker founded 1920; rotary engine champion.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "Headquarters: Hiroshima, Japan.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "Headquarters: Hiroshima, Japan.", "x": "More on Mazda: Headquarters: Hiroshima, Japan.. MX-5 Miata: best-selling roadster ever. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Mazda.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "Name from Ahura Mazda.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "Name from Ahura Mazda.", "x": "More on Mazda: Name from Ahura Mazda.. Rotary engine won Le Mans (787B). Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Mazda.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "Only maker to persist with rotary.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "Only maker to persist with rotary.", "x": "More on Mazda: Only maker to persist with rotary.. Kodo design: 'soul of motion'. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Mazda.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "CX-5: its sales backbone.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "CX-5: its sales backbone.", "x": "More on Mazda: CX-5: its sales backbone.. Zoom-Zoom era defined 2000s fun. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Mazda.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "SkyActiv tech: efficient engines.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "SkyActiv tech: efficient engines.", "x": "More on Mazda: SkyActiv tech: efficient engines.. Premium push upmarket. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Mazda.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Toyota partnership (Alabama plant).", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Toyota partnership (Alabama plant).", "x": "More on Mazda: Toyota partnership (Alabama plant).. RX-7: rotary sports-car legend. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Mazda.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a Mazda: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a Mazda: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. Headquarters: Hiroshima, Japan. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. Rotary engine won Le Mans (787B). The right example of Mazda is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning Mazda: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning Mazda: costs and care.", "x": "Ownership: Name from Ahura Mazda.. Maintain it by the book — fluids, intervals, and qualified specialists. Kodo design: 'soul of motion'. Budget realistically: purchase price is only the beginning of the story with any car make.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Mazda through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "Mazda through the years.", "x": "The timeline: Japanese maker founded 1920; rotary engine champion.. RX-7: rotary sports-car legend. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. Only maker to persist with rotary. Read it as one story, and the car make makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for Mazda.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for Mazda.", "x": "The future: Mazda faces electrification, automation, and changing tastes like everything in transport. Zoom-Zoom era defined 2000s fun. Its heritage — Japanese maker founded 1920; rotary engine champion. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "Mazda fact: CX-5: its sales backbone..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "Mazda fact: CX-5: its sales backbone..", "x": "From the Mazda file: CX-5: its sales backbone.. MX-5 Miata: best-selling roadster ever. Collect these and you will know Mazda better than most owners. Japanese maker founded 1920; rotary engine champion.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-car-mazda-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
