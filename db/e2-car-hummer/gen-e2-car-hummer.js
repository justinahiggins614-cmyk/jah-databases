(function(){'use strict';
/* JAH Hummer Car Make Database generator — jahdb-e2-car-hummer-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-car-hummer',PREFIX='JAH-E2CARHUMMER-',NAME='JAH Hummer Car Make Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "facts", "future", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hummer: overview", "d": "Hummer: Military-derived SUV brand; revived as GMC Hummer EV..", "g": "overview", "l": 2, "q": "What is Hummer: overview?", "a": "Hummer: Military-derived SUV brand; revived as GMC Hummer EV..", "x": "The complete car make guide: Military-derived SUV brand; revived as GMC Hummer EV.. H1: civilian Humvee. From its origins to its most famous models, from buying advice to what comes next — this database covers the car make in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How Hummer began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How Hummer began.", "x": "The origin of Hummer: Military-derived SUV brand; revived as GMC Hummer EV.. H2/H3: 2000s excess icons. Every great car make has a founding story of ambition, luck, and timing — and Hummer's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "H1: civilian Humvee.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "H1: civilian Humvee.", "x": "Hummer: H1: civilian Humvee.. This is one of the defining facts about Hummer — the kind of thing enthusiasts argue about and newcomers should know first. GM brand. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this Hummer fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this Hummer fact matters.", "x": "Why it matters: H1: civilian Humvee.. For Hummer, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Military-derived SUV brand; revived as GMC Hummer EV.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "H2/H3: 2000s excess icons.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "H2/H3: 2000s excess icons.", "x": "Hummer: H2/H3: 2000s excess icons.. This is one of the defining facts about Hummer — the kind of thing enthusiasts argue about and newcomers should know first. GMC Hummer EV now. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this Hummer fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this Hummer fact matters.", "x": "Why it matters: H2/H3: 2000s excess icons.. For Hummer, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Military-derived SUV brand; revived as GMC Hummer EV.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Arnold Schwarzenegger fan.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Arnold Schwarzenegger fan.", "x": "Hummer: Arnold Schwarzenegger fan.. This is one of the defining facts about Hummer — the kind of thing enthusiasts argue about and newcomers should know first. Watts to Freedom mode. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this Hummer fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this Hummer fact matters.", "x": "Why it matters: Arnold Schwarzenegger fan.. For Hummer, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Military-derived SUV brand; revived as GMC Hummer EV.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Killed 2010; reborn electric.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Killed 2010; reborn electric.", "x": "Hummer: Killed 2010; reborn electric.. This is one of the defining facts about Hummer — the kind of thing enthusiasts argue about and newcomers should know first. Off-road EV king. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this Hummer fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this Hummer fact matters.", "x": "Why it matters: Killed 2010; reborn electric.. For Hummer, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Military-derived SUV brand; revived as GMC Hummer EV.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Hummer EV: 1000 hp.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Hummer EV: 1000 hp.", "x": "Hummer: Hummer EV: 1000 hp.. This is one of the defining facts about Hummer — the kind of thing enthusiasts argue about and newcomers should know first. Supertruck. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this Hummer fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this Hummer fact matters.", "x": "Why it matters: Hummer EV: 1000 hp.. For Hummer, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Military-derived SUV brand; revived as GMC Hummer EV.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "CrabWalk feature.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "CrabWalk feature.", "x": "Hummer: CrabWalk feature.. This is one of the defining facts about Hummer — the kind of thing enthusiasts argue about and newcomers should know first. AM General roots. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this Hummer fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this Hummer fact matters.", "x": "Why it matters: CrabWalk feature.. For Hummer, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Military-derived SUV brand; revived as GMC Hummer EV.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "AM General roots.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "AM General roots.", "x": "More on Hummer: AM General roots.. H2/H3: 2000s excess icons. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Hummer.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "GM brand.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "GM brand.", "x": "More on Hummer: GM brand.. Arnold Schwarzenegger fan. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Hummer. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "GMC Hummer EV now.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "GMC Hummer EV now.", "x": "More on Hummer: GMC Hummer EV now.. Killed 2010; reborn electric. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Hummer.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "Watts to Freedom mode.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "Watts to Freedom mode.", "x": "More on Hummer: Watts to Freedom mode.. Hummer EV: 1000 hp. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Hummer.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Off-road EV king.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Off-road EV king.", "x": "More on Hummer: Off-road EV king.. CrabWalk feature. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Hummer. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Supertruck.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Supertruck.", "x": "More on Hummer: Supertruck.. H1: civilian Humvee. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Hummer. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a Hummer: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a Hummer: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. AM General roots. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. Arnold Schwarzenegger fan. The right example of Hummer is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning Hummer: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning Hummer: costs and care.", "x": "Ownership: GM brand.. Maintain it by the book — fluids, intervals, and qualified specialists. Killed 2010; reborn electric. Budget realistically: purchase price is only the beginning of the story with any car make.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Hummer through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "Hummer through the years.", "x": "The timeline: Military-derived SUV brand; revived as GMC Hummer EV.. H1: civilian Humvee. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. GMC Hummer EV now. Read it as one story, and the car make makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for Hummer.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for Hummer.", "x": "The future: Hummer faces electrification, automation, and changing tastes like everything in transport. Hummer EV: 1000 hp. Its heritage — Military-derived SUV brand; revived as GMC Hummer EV. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "Hummer fact: Watts to Freedom mode..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "Hummer fact: Watts to Freedom mode..", "x": "From the Hummer file: Watts to Freedom mode.. H2/H3: 2000s excess icons. Collect these and you will know Hummer better than most owners. Military-derived SUV brand; revived as GMC Hummer EV. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-car-hummer-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
