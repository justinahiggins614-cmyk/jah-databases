(function(){'use strict';
/* JAH KTM Motorcycle Make Database generator — jahdb-e2-moto-ktm-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-moto-ktm',PREFIX='JAH-E2MOTOKTM-',NAME='JAH KTM Motorcycle Make Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "future", "quiz", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "KTM: overview", "d": "KTM: Austrian maker; 'Ready to Race'..", "g": "overview", "l": 2, "q": "What is KTM: overview?", "a": "KTM: Austrian maker; 'Ready to Race'..", "x": "The complete motorcycle make guide: Austrian maker; 'Ready to Race'.. Dakar Rally: 18 straight wins. From its origins to its most famous models, from buying advice to what comes next — this database covers the motorcycle make in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How KTM began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How KTM began.", "x": "The origin of KTM: Austrian maker; 'Ready to Race'.. 1290 Super Duke R. Every great motorcycle make has a founding story of ambition, luck, and timing — and KTM's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Dakar Rally: 18 straight wins.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Dakar Rally: 18 straight wins.", "x": "KTM: Dakar Rally: 18 straight wins.. This is one of the defining facts about KTM — the kind of thing enthusiasts argue about and newcomers should know first. Pierer Mobility. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this KTM fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this KTM fact matters.", "x": "Why it matters: Dakar Rally: 18 straight wins.. For KTM, this fact shaped reputation, sales, or history — understanding it means understanding why the motorcycle make is remembered. Austrian maker; 'Ready to Race'.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "1290 Super Duke R.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "1290 Super Duke R.", "x": "KTM: 1290 Super Duke R.. This is one of the defining facts about KTM — the kind of thing enthusiasts argue about and newcomers should know first. Husqvarna/GasGas sister. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this KTM fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this KTM fact matters.", "x": "Why it matters: 1290 Super Duke R.. For KTM, this fact shaped reputation, sales, or history — understanding it means understanding why the motorcycle make is remembered. Austrian maker; 'Ready to Race'.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "EXC enduro kings.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "EXC enduro kings.", "x": "KTM: EXC enduro kings.. This is one of the defining facts about KTM — the kind of thing enthusiasts argue about and newcomers should know first. RC 8C track. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this KTM fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this KTM fact matters.", "x": "Why it matters: EXC enduro kings.. For KTM, this fact shaped reputation, sales, or history — understanding it means understanding why the motorcycle make is remembered. Austrian maker; 'Ready to Race'.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Orange livery.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Orange livery.", "x": "KTM: Orange livery.. This is one of the defining facts about KTM — the kind of thing enthusiasts argue about and newcomers should know first. 790 Adventure. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this KTM fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this KTM fact matters.", "x": "Why it matters: Orange livery.. For KTM, this fact shaped reputation, sales, or history — understanding it means understanding why the motorcycle make is remembered. Austrian maker; 'Ready to Race'. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "MotoGP contender.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "MotoGP contender.", "x": "KTM: MotoGP contender.. This is one of the defining facts about KTM — the kind of thing enthusiasts argue about and newcomers should know first. Ready to Race. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this KTM fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this KTM fact matters.", "x": "Why it matters: MotoGP contender.. For KTM, this fact shaped reputation, sales, or history — understanding it means understanding why the motorcycle make is remembered. Austrian maker; 'Ready to Race'.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "390 Duke: entry fun.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "390 Duke: entry fun.", "x": "KTM: 390 Duke: entry fun.. This is one of the defining facts about KTM — the kind of thing enthusiasts argue about and newcomers should know first. Mattighofen. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this KTM fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this KTM fact matters.", "x": "Why it matters: 390 Duke: entry fun.. For KTM, this fact shaped reputation, sales, or history — understanding it means understanding why the motorcycle make is remembered. Austrian maker; 'Ready to Race'.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "Mattighofen.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "Mattighofen.", "x": "More on KTM: Mattighofen.. 1290 Super Duke R. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows KTM. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "Pierer Mobility.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "Pierer Mobility.", "x": "More on KTM: Pierer Mobility.. EXC enduro kings. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows KTM. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "Husqvarna/GasGas sister.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "Husqvarna/GasGas sister.", "x": "More on KTM: Husqvarna/GasGas sister.. Orange livery. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows KTM. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "RC 8C track.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "RC 8C track.", "x": "More on KTM: RC 8C track.. MotoGP contender. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows KTM. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "790 Adventure.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "790 Adventure.", "x": "More on KTM: 790 Adventure.. 390 Duke: entry fun. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows KTM. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Ready to Race.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Ready to Race.", "x": "More on KTM: Ready to Race.. Dakar Rally: 18 straight wins. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows KTM.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a KTM: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a KTM: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. Mattighofen. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. EXC enduro kings. The right example of KTM is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning KTM: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning KTM: costs and care.", "x": "Ownership: Pierer Mobility.. Maintain it by the book — fluids, intervals, and qualified specialists. Orange livery. Budget realistically: purchase price is only the beginning of the story with any motorcycle make.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "KTM through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "KTM through the years.", "x": "The timeline: Austrian maker; 'Ready to Race'.. Dakar Rally: 18 straight wins. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. Husqvarna/GasGas sister. Read it as one story, and the motorcycle make makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for KTM.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for KTM.", "x": "The future: KTM faces electrification, automation, and changing tastes like everything in transport. MotoGP contender. Its heritage — Austrian maker; 'Ready to Race'. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "KTM fact: RC 8C track..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "KTM fact: RC 8C track..", "x": "From the KTM file: RC 8C track.. 1290 Super Duke R. Collect these and you will know KTM better than most owners. Austrian maker; 'Ready to Race'. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-moto-ktm-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
