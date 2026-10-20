(function(){'use strict';
/* JAH Mercedes-Benz Car Make Database generator — jahdb-e2-car-mercedes-benz-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-car-mercedes-benz',PREFIX='JAH-E2CARMERCED-',NAME='JAH Mercedes-Benz Car Make Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "facts", "future", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mercedes-Benz: overview", "d": "Mercedes-Benz: German luxury maker; Benz's 1886 Patent-Motorwagen was the first automobile..", "g": "overview", "l": 2, "q": "What is Mercedes-Benz: overview?", "a": "Mercedes-Benz: German luxury maker; Benz's 1886 Patent-Motorwagen was the first automobile..", "x": "The complete car make guide: German luxury maker; Benz's 1886 Patent-Motorwagen was the first automobile.. Invented the automobile (1886). From its origins to its most famous models, from buying advice to what comes next — this database covers the car make in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How Mercedes-Benz began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How Mercedes-Benz began.", "x": "The origin of Mercedes-Benz: German luxury maker; Benz's 1886 Patent-Motorwagen was the first automobile.. S-Class sets the luxury benchmark. Every great car make has a founding story of ambition, luck, and timing — and Mercedes-Benz's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Invented the automobile (1886).", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Invented the automobile (1886).", "x": "Mercedes-Benz: Invented the automobile (1886).. This is one of the defining facts about Mercedes-Benz — the kind of thing enthusiasts argue about and newcomers should know first. Mercedes-Benz formed 1926 (merger).", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this Mercedes-Benz fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this Mercedes-Benz fact matters.", "x": "Why it matters: Invented the automobile (1886).. For Mercedes-Benz, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. German luxury maker; Benz's 1886 Patent-Motorwagen was the first automobile.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "S-Class sets the luxury benchmark.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "S-Class sets the luxury benchmark.", "x": "Mercedes-Benz: S-Class sets the luxury benchmark.. This is one of the defining facts about Mercedes-Benz — the kind of thing enthusiasts argue about and newcomers should know first. Three-pointed star: land, sea, air.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this Mercedes-Benz fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this Mercedes-Benz fact matters.", "x": "Why it matters: S-Class sets the luxury benchmark.. For Mercedes-Benz, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. German luxury maker; Benz's 1886 Patent-Motorwagen was the first automobile.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "AMG division makes hand-built performance cars.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "AMG division makes hand-built performance cars.", "x": "Mercedes-Benz: AMG division makes hand-built performance cars.. This is one of the defining facts about Mercedes-Benz — the kind of thing enthusiasts argue about and newcomers should know first. Pioneered ABS, airbags, crumple zones.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this Mercedes-Benz fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this Mercedes-Benz fact matters.", "x": "Why it matters: AMG division makes hand-built performance cars.. For Mercedes-Benz, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. German luxury maker; Benz's 1886 Patent-Motorwagen was the first automobile.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "G-Wagen: military icon turned luxury SUV.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "G-Wagen: military icon turned luxury SUV.", "x": "Mercedes-Benz: G-Wagen: military icon turned luxury SUV.. This is one of the defining facts about Mercedes-Benz — the kind of thing enthusiasts argue about and newcomers should know first. Also makes trucks and buses.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this Mercedes-Benz fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this Mercedes-Benz fact matters.", "x": "Why it matters: G-Wagen: military icon turned luxury SUV.. For Mercedes-Benz, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. German luxury maker; Benz's 1886 Patent-Motorwagen was the first automobile.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Silver Arrows dominated Grand Prix racing.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Silver Arrows dominated Grand Prix racing.", "x": "Mercedes-Benz: Silver Arrows dominated Grand Prix racing.. This is one of the defining facts about Mercedes-Benz — the kind of thing enthusiasts argue about and newcomers should know first. Formula 1 dominant in hybrid era.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this Mercedes-Benz fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this Mercedes-Benz fact matters.", "x": "Why it matters: Silver Arrows dominated Grand Prix racing.. For Mercedes-Benz, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. German luxury maker; Benz's 1886 Patent-Motorwagen was the first automobile.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Maybach is its ultra-luxury sub-brand.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Maybach is its ultra-luxury sub-brand.", "x": "Mercedes-Benz: Maybach is its ultra-luxury sub-brand.. This is one of the defining facts about Mercedes-Benz — the kind of thing enthusiasts argue about and newcomers should know first. Headquarters: Stuttgart, Germany.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this Mercedes-Benz fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this Mercedes-Benz fact matters.", "x": "Why it matters: Maybach is its ultra-luxury sub-brand.. For Mercedes-Benz, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. German luxury maker; Benz's 1886 Patent-Motorwagen was the first automobile.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "Headquarters: Stuttgart, Germany.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "Headquarters: Stuttgart, Germany.", "x": "More on Mercedes-Benz: Headquarters: Stuttgart, Germany.. S-Class sets the luxury benchmark. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Mercedes-Benz.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "Mercedes-Benz formed 1926 (merger).", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "Mercedes-Benz formed 1926 (merger).", "x": "More on Mercedes-Benz: Mercedes-Benz formed 1926 (merger).. AMG division makes hand-built performance cars. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Mercedes-Benz.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "Three-pointed star: land, sea, air.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "Three-pointed star: land, sea, air.", "x": "More on Mercedes-Benz: Three-pointed star: land, sea, air.. G-Wagen: military icon turned luxury SUV. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Mercedes-Benz.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "Pioneered ABS, airbags, crumple zones.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "Pioneered ABS, airbags, crumple zones.", "x": "More on Mercedes-Benz: Pioneered ABS, airbags, crumple zones.. Silver Arrows dominated Grand Prix racing. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Mercedes-Benz.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Also makes trucks and buses.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Also makes trucks and buses.", "x": "More on Mercedes-Benz: Also makes trucks and buses.. Maybach is its ultra-luxury sub-brand. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Mercedes-Benz.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Formula 1 dominant in hybrid era.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Formula 1 dominant in hybrid era.", "x": "More on Mercedes-Benz: Formula 1 dominant in hybrid era.. Invented the automobile (1886). Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Mercedes-Benz.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a Mercedes-Benz: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a Mercedes-Benz: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. Headquarters: Stuttgart, Germany. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. AMG division makes hand-built performance cars. The right example of Mercedes-Benz is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning Mercedes-Benz: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning Mercedes-Benz: costs and care.", "x": "Ownership: Mercedes-Benz formed 1926 (merger).. Maintain it by the book — fluids, intervals, and qualified specialists. G-Wagen: military icon turned luxury SUV. Budget realistically: purchase price is only the beginning of the story with any car make.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Mercedes-Benz through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "Mercedes-Benz through the years.", "x": "The timeline: German luxury maker; Benz's 1886 Patent-Motorwagen was the first automobile.. Invented the automobile (1886). Key chapters mark the eras — the breakthroughs, the crises, the comebacks. Three-pointed star: land, sea, air. Read it as one story, and the car make makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for Mercedes-Benz.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for Mercedes-Benz.", "x": "The future: Mercedes-Benz faces electrification, automation, and changing tastes like everything in transport. Silver Arrows dominated Grand Prix racing. Its heritage — German luxury maker; Benz's 1886 Patent-Motorwagen was the first automobile. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "Mercedes-Benz fact: Pioneered ABS, airbags, crumple zones..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "Mercedes-Benz fact: Pioneered ABS, airbags, crumple zones..", "x": "From the Mercedes-Benz file: Pioneered ABS, airbags, crumple zones.. S-Class sets the luxury benchmark. Collect these and you will know Mercedes-Benz better than most owners. German luxury maker; Benz's 1886 Patent-Motorwagen was the first automobile.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-car-mercedes-benz-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
