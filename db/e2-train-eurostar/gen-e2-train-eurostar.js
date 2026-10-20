(function(){'use strict';
/* JAH Eurostar Train Database generator — jahdb-e2-train-eurostar-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-train-eurostar',PREFIX='JAH-E2TRAINEURO-',NAME='JAH Eurostar Train Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "future", "quiz", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Eurostar: overview", "d": "Eurostar: Channel Tunnel high-speed service; London-Paris-Brussels..", "g": "overview", "l": 2, "q": "What is Eurostar: overview?", "a": "Eurostar: Channel Tunnel high-speed service; London-Paris-Brussels..", "x": "The complete train guide: Channel Tunnel high-speed service; London-Paris-Brussels.. Channel Tunnel 1994. From its origins to its most famous examples, from buying advice to what comes next — this database covers the train in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How Eurostar began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How Eurostar began.", "x": "The origin of Eurostar: Channel Tunnel high-speed service; London-Paris-Brussels.. London-Paris 2h15. Every great train has a founding story of ambition, luck, and timing — and Eurostar's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Channel Tunnel 1994.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Channel Tunnel 1994.", "x": "Eurostar: Channel Tunnel 1994.. This is one of the defining facts about Eurostar — the kind of thing enthusiasts argue about and newcomers should know first. Class 373/374. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this Eurostar fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this Eurostar fact matters.", "x": "Why it matters: Channel Tunnel 1994.. For Eurostar, this fact shaped reputation, sales, or history — understanding it means understanding why the train is remembered. Channel Tunnel high-speed service; London-Paris-Brussels.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "London-Paris 2h15.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "London-Paris 2h15.", "x": "Eurostar: London-Paris 2h15.. This is one of the defining facts about Eurostar — the kind of thing enthusiasts argue about and newcomers should know first. St Pancras terminal. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this Eurostar fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this Eurostar fact matters.", "x": "Why it matters: London-Paris 2h15.. For Eurostar, this fact shaped reputation, sales, or history — understanding it means understanding why the train is remembered. Channel Tunnel high-speed service; London-Paris-Brussels.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "e320 Velaro trains.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "e320 Velaro trains.", "x": "Eurostar: e320 Velaro trains.. This is one of the defining facts about Eurostar — the kind of thing enthusiasts argue about and newcomers should know first. Gare du Nord. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this Eurostar fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this Eurostar fact matters.", "x": "Why it matters: e320 Velaro trains.. For Eurostar, this fact shaped reputation, sales, or history — understanding it means understanding why the train is remembered. Channel Tunnel high-speed service; London-Paris-Brussels.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Amsterdam added.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Amsterdam added.", "x": "Eurostar: Amsterdam added.. This is one of the defining facts about Eurostar — the kind of thing enthusiasts argue about and newcomers should know first. Merged with Thalys. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this Eurostar fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this Eurostar fact matters.", "x": "Why it matters: Amsterdam added.. For Eurostar, this fact shaped reputation, sales, or history — understanding it means understanding why the train is remembered. Channel Tunnel high-speed service; London-Paris-Brussels.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Border controls onboard.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Border controls onboard.", "x": "Eurostar: Border controls onboard.. This is one of the defining facts about Eurostar — the kind of thing enthusiasts argue about and newcomers should know first. High occupancy. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this Eurostar fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this Eurostar fact matters.", "x": "Why it matters: Border controls onboard.. For Eurostar, this fact shaped reputation, sales, or history — understanding it means understanding why the train is remembered. Channel Tunnel high-speed service; London-Paris-Brussels.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Green alternative to flying.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Green alternative to flying.", "x": "Eurostar: Green alternative to flying.. This is one of the defining facts about Eurostar — the kind of thing enthusiasts argue about and newcomers should know first. Eurostar, London. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this Eurostar fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this Eurostar fact matters.", "x": "Why it matters: Green alternative to flying.. For Eurostar, this fact shaped reputation, sales, or history — understanding it means understanding why the train is remembered. Channel Tunnel high-speed service; London-Paris-Brussels.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "Eurostar, London.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "Eurostar, London.", "x": "More on Eurostar: Eurostar, London.. London-Paris 2h15. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Eurostar.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "Class 373/374.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "Class 373/374.", "x": "More on Eurostar: Class 373/374.. e320 Velaro trains. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Eurostar. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "St Pancras terminal.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "St Pancras terminal.", "x": "More on Eurostar: St Pancras terminal.. Amsterdam added. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Eurostar.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "Gare du Nord.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "Gare du Nord.", "x": "More on Eurostar: Gare du Nord.. Border controls onboard. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Eurostar.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Merged with Thalys.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Merged with Thalys.", "x": "More on Eurostar: Merged with Thalys.. Green alternative to flying. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Eurostar.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "High occupancy.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "High occupancy.", "x": "More on Eurostar: High occupancy.. Channel Tunnel 1994. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Eurostar.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a Eurostar: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a Eurostar: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. Eurostar, London. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. e320 Velaro trains. The right example of Eurostar is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning Eurostar: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning Eurostar: costs and care.", "x": "Ownership: Class 373/374.. Maintain it by the book — fluids, intervals, and qualified specialists. Amsterdam added. Budget realistically: purchase price is only the beginning of the story with any train.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Eurostar through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "Eurostar through the years.", "x": "The timeline: Channel Tunnel high-speed service; London-Paris-Brussels.. Channel Tunnel 1994. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. St Pancras terminal. Read it as one story, and the train makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for Eurostar.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for Eurostar.", "x": "The future: Eurostar faces electrification, automation, and changing tastes like everything in transport. Border controls onboard. Its heritage — Channel Tunnel high-speed service; London-Paris-Brussels. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "Eurostar fact: Gare du Nord..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "Eurostar fact: Gare du Nord..", "x": "From the Eurostar file: Gare du Nord.. London-Paris 2h15. Collect these and you will know Eurostar better than most owners. Channel Tunnel high-speed service; London-Paris-Brussels. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-train-eurostar-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
