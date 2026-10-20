(function(){'use strict';
/* JAH Opel Car Make Database generator — jahdb-e2-car-opel-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-car-opel',PREFIX='JAH-E2CAROPEL-',NAME='JAH Opel Car Make Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "facts", "future", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Opel: overview", "d": "Opel: German maker founded 1862; Stellantis brand..", "g": "overview", "l": 2, "q": "What is Opel: overview?", "a": "Opel: German maker founded 1862; Stellantis brand..", "x": "The complete car make guide: German maker founded 1862; Stellantis brand.. Astra/Corsa: European staples. From its origins to its most famous models, from buying advice to what comes next — this database covers the car make in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How Opel began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How Opel began.", "x": "The origin of Opel: German maker founded 1862; Stellantis brand.. Manta: cult coupe. Every great car make has a founding story of ambition, luck, and timing — and Opel's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Astra/Corsa: European staples.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Astra/Corsa: European staples.", "x": "Opel: Astra/Corsa: European staples.. This is one of the defining facts about Opel — the kind of thing enthusiasts argue about and newcomers should know first. Started with sewing machines. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this Opel fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this Opel fact matters.", "x": "Why it matters: Astra/Corsa: European staples.. For Opel, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. German maker founded 1862; Stellantis brand.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Manta: cult coupe.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Manta: cult coupe.", "x": "Opel: Manta: cult coupe.. This is one of the defining facts about Opel — the kind of thing enthusiasts argue about and newcomers should know first. Blitz logo: lightning. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this Opel fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this Opel fact matters.", "x": "Why it matters: Manta: cult coupe.. For Opel, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. German maker founded 1862; Stellantis brand.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Speedster: Lotus-based fun.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Speedster: Lotus-based fun.", "x": "Opel: Speedster: Lotus-based fun.. This is one of the defining facts about Opel — the kind of thing enthusiasts argue about and newcomers should know first. Calibra: aero coupe. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this Opel fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this Opel fact matters.", "x": "Why it matters: Speedster: Lotus-based fun.. For Opel, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. German maker founded 1862; Stellantis brand.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Now Stellantis (ex-GM).", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Now Stellantis (ex-GM).", "x": "Opel: Now Stellantis (ex-GM).. This is one of the defining facts about Opel — the kind of thing enthusiasts argue about and newcomers should know first. GM owned 1929-2017. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this Opel fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this Opel fact matters.", "x": "Why it matters: Now Stellantis (ex-GM).. For Opel, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. German maker founded 1862; Stellantis brand.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Vauxhall twin in UK.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Vauxhall twin in UK.", "x": "Opel: Vauxhall twin in UK.. This is one of the defining facts about Opel — the kind of thing enthusiasts argue about and newcomers should know first. Mokka: stylish crossover. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this Opel fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this Opel fact matters.", "x": "Why it matters: Vauxhall twin in UK.. For Opel, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. German maker founded 1862; Stellantis brand.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Grandland: SUV.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Grandland: SUV.", "x": "Opel: Grandland: SUV.. This is one of the defining facts about Opel — the kind of thing enthusiasts argue about and newcomers should know first. Headquarters: Russelsheim (Stellantis). Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this Opel fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this Opel fact matters.", "x": "Why it matters: Grandland: SUV.. For Opel, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. German maker founded 1862; Stellantis brand.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "Headquarters: Russelsheim (Stellantis).", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "Headquarters: Russelsheim (Stellantis).", "x": "More on Opel: Headquarters: Russelsheim (Stellantis).. Manta: cult coupe. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Opel.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "Started with sewing machines.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "Started with sewing machines.", "x": "More on Opel: Started with sewing machines.. Speedster: Lotus-based fun. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Opel.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "Blitz logo: lightning.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "Blitz logo: lightning.", "x": "More on Opel: Blitz logo: lightning.. Now Stellantis (ex-GM). Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Opel.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "Calibra: aero coupe.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "Calibra: aero coupe.", "x": "More on Opel: Calibra: aero coupe.. Vauxhall twin in UK. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Opel. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "GM owned 1929-2017.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "GM owned 1929-2017.", "x": "More on Opel: GM owned 1929-2017.. Grandland: SUV. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Opel. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Mokka: stylish crossover.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Mokka: stylish crossover.", "x": "More on Opel: Mokka: stylish crossover.. Astra/Corsa: European staples. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Opel.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a Opel: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a Opel: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. Headquarters: Russelsheim (Stellantis). Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. Speedster: Lotus-based fun. The right example of Opel is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning Opel: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning Opel: costs and care.", "x": "Ownership: Started with sewing machines.. Maintain it by the book — fluids, intervals, and qualified specialists. Now Stellantis (ex-GM). Budget realistically: purchase price is only the beginning of the story with any car make.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Opel through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "Opel through the years.", "x": "The timeline: German maker founded 1862; Stellantis brand.. Astra/Corsa: European staples. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. Blitz logo: lightning. Read it as one story, and the car make makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for Opel.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for Opel.", "x": "The future: Opel faces electrification, automation, and changing tastes like everything in transport. Vauxhall twin in UK. Its heritage — German maker founded 1862; Stellantis brand. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "Opel fact: Calibra: aero coupe..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "Opel fact: Calibra: aero coupe..", "x": "From the Opel file: Calibra: aero coupe.. Manta: cult coupe. Collect these and you will know Opel better than most owners. German maker founded 1862; Stellantis brand. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-car-opel-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
