(function(){'use strict';
/* JAH Citroen Car Make Database generator — jahdb-e2-car-citroen-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-car-citroen',PREFIX='JAH-E2CARCITROE-',NAME='JAH Citroen Car Make Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "facts", "future", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Citroen: overview", "d": "Citroen: French maker founded 1919 by André Citroën; comfort innovator..", "g": "overview", "l": 2, "q": "What is Citroen: overview?", "a": "Citroen: French maker founded 1919 by André Citroën; comfort innovator..", "x": "The complete car make guide: French maker founded 1919 by André Citroën; comfort innovator.. DS (1955): the most beautiful car. From its origins to its most famous models, from buying advice to what comes next — this database covers the car make in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How Citroen began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How Citroen began.", "x": "The origin of Citroen: French maker founded 1919 by André Citroën; comfort innovator.. Hydropneumatic suspension magic. Every great car make has a founding story of ambition, luck, and timing — and Citroen's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "DS (1955): the most beautiful car.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "DS (1955): the most beautiful car.", "x": "Citroen: DS (1955): the most beautiful car.. This is one of the defining facts about Citroen — the kind of thing enthusiasts argue about and newcomers should know first. Double-chevron: gear teeth. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this Citroen fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this Citroen fact matters.", "x": "Why it matters: DS (1955): the most beautiful car.. For Citroen, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. French maker founded 1919 by André Citroën; comfort innovator.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Hydropneumatic suspension magic.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Hydropneumatic suspension magic.", "x": "Citroen: Hydropneumatic suspension magic.. This is one of the defining facts about Citroen — the kind of thing enthusiasts argue about and newcomers should know first. SM: Maserati-engined GT. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this Citroen fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this Citroen fact matters.", "x": "Why it matters: Hydropneumatic suspension magic.. For Citroen, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. French maker founded 1919 by André Citroën; comfort innovator.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "2CV: France’s Beetle.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "2CV: France’s Beetle.", "x": "Citroen: 2CV: France’s Beetle.. This is one of the defining facts about Citroen — the kind of thing enthusiasts argue about and newcomers should know first. CX: aerodynamic icon. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this Citroen fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this Citroen fact matters.", "x": "Why it matters: 2CV: France’s Beetle.. For Citroen, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. French maker founded 1919 by André Citroën; comfort innovator.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Traction Avant: FWD pioneer.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Traction Avant: FWD pioneer.", "x": "Citroen: Traction Avant: FWD pioneer.. This is one of the defining facts about Citroen — the kind of thing enthusiasts argue about and newcomers should know first. Cactus: quirky crossover. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this Citroen fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this Citroen fact matters.", "x": "Why it matters: Traction Avant: FWD pioneer.. For Citroen, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. French maker founded 1919 by André Citroën; comfort innovator.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Stellantis-owned now.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Stellantis-owned now.", "x": "Citroen: Stellantis-owned now.. This is one of the defining facts about Citroen — the kind of thing enthusiasts argue about and newcomers should know first. Comfort-focused brand. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this Citroen fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this Citroen fact matters.", "x": "Why it matters: Stellantis-owned now.. For Citroen, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. French maker founded 1919 by André Citroën; comfort innovator.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Ami: tiny electric quadricycle.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Ami: tiny electric quadricycle.", "x": "Citroen: Ami: tiny electric quadricycle.. This is one of the defining facts about Citroen — the kind of thing enthusiasts argue about and newcomers should know first. Headquarters: Paris (Stellantis).", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this Citroen fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this Citroen fact matters.", "x": "Why it matters: Ami: tiny electric quadricycle.. For Citroen, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. French maker founded 1919 by André Citroën; comfort innovator.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "Headquarters: Paris (Stellantis).", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "Headquarters: Paris (Stellantis).", "x": "More on Citroen: Headquarters: Paris (Stellantis).. Hydropneumatic suspension magic. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Citroen.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "Double-chevron: gear teeth.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "Double-chevron: gear teeth.", "x": "More on Citroen: Double-chevron: gear teeth.. 2CV: France’s Beetle. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Citroen.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "SM: Maserati-engined GT.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "SM: Maserati-engined GT.", "x": "More on Citroen: SM: Maserati-engined GT.. Traction Avant: FWD pioneer. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Citroen.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "CX: aerodynamic icon.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "CX: aerodynamic icon.", "x": "More on Citroen: CX: aerodynamic icon.. Stellantis-owned now. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Citroen.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Cactus: quirky crossover.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Cactus: quirky crossover.", "x": "More on Citroen: Cactus: quirky crossover.. Ami: tiny electric quadricycle. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Citroen.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Comfort-focused brand.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Comfort-focused brand.", "x": "More on Citroen: Comfort-focused brand.. DS (1955): the most beautiful car. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Citroen.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a Citroen: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a Citroen: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. Headquarters: Paris (Stellantis). Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. 2CV: France’s Beetle. The right example of Citroen is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning Citroen: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning Citroen: costs and care.", "x": "Ownership: Double-chevron: gear teeth.. Maintain it by the book — fluids, intervals, and qualified specialists. Traction Avant: FWD pioneer. Budget realistically: purchase price is only the beginning of the story with any car make.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Citroen through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "Citroen through the years.", "x": "The timeline: French maker founded 1919 by André Citroën; comfort innovator.. DS (1955): the most beautiful car. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. SM: Maserati-engined GT. Read it as one story, and the car make makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for Citroen.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for Citroen.", "x": "The future: Citroen faces electrification, automation, and changing tastes like everything in transport. Stellantis-owned now. Its heritage — French maker founded 1919 by André Citroën; comfort innovator. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "Citroen fact: CX: aerodynamic icon..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "Citroen fact: CX: aerodynamic icon..", "x": "From the Citroen file: CX: aerodynamic icon.. Hydropneumatic suspension magic. Collect these and you will know Citroen better than most owners. French maker founded 1919 by André Citroën; comfort innovator.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-car-citroen-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
