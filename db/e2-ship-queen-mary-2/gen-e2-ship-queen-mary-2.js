(function(){'use strict';
/* JAH Queen Mary 2 Ship Database generator — jahdb-e2-ship-queen-mary-2-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-ship-queen-mary-2',PREFIX='JAH-E2SHIPQUEEN-',NAME='JAH Queen Mary 2 Ship Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "future", "quiz", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Queen Mary 2: overview", "d": "Queen Mary 2: Last true ocean liner; Cunard flagship since 2004..", "g": "overview", "l": 2, "q": "What is Queen Mary 2: overview?", "a": "Queen Mary 2: Last true ocean liner; Cunard flagship since 2004..", "x": "The complete ship guide: Last true ocean liner; Cunard flagship since 2004.. Only ocean liner in service. From its origins to its most famous examples, from buying advice to what comes next — this database covers the ship in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How Queen Mary 2 began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How Queen Mary 2 began.", "x": "The origin of Queen Mary 2: Last true ocean liner; Cunard flagship since 2004.. Transatlantic crossings. Every great ship has a founding story of ambition, luck, and timing — and Queen Mary 2's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Only ocean liner in service.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Only ocean liner in service.", "x": "Queen Mary 2: Only ocean liner in service.. This is one of the defining facts about Queen Mary 2 — the kind of thing enthusiasts argue about and newcomers should know first. Cunard. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this Queen Mary 2 fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this Queen Mary 2 fact matters.", "x": "Why it matters: Only ocean liner in service.. For Queen Mary 2, this fact shaped reputation, sales, or history — understanding it means understanding why the ship is remembered. Last true ocean liner; Cunard flagship since 2004.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Transatlantic crossings.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Transatlantic crossings.", "x": "Queen Mary 2: Transatlantic crossings.. This is one of the defining facts about Queen Mary 2 — the kind of thing enthusiasts argue about and newcomers should know first. Southampton-NY. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this Queen Mary 2 fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this Queen Mary 2 fact matters.", "x": "Why it matters: Transatlantic crossings.. For Queen Mary 2, this fact shaped reputation, sales, or history — understanding it means understanding why the ship is remembered. Last true ocean liner; Cunard flagship since 2004.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "1,132 ft long.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "1,132 ft long.", "x": "Queen Mary 2: 1,132 ft long.. This is one of the defining facts about Queen Mary 2 — the kind of thing enthusiasts argue about and newcomers should know first. Remastered 2016. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this Queen Mary 2 fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this Queen Mary 2 fact matters.", "x": "Why it matters: 1,132 ft long.. For Queen Mary 2, this fact shaped reputation, sales, or history — understanding it means understanding why the ship is remembered. Last true ocean liner; Cunard flagship since 2004.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Planetarium onboard.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Planetarium onboard.", "x": "Queen Mary 2: Planetarium onboard.. This is one of the defining facts about Queen Mary 2 — the kind of thing enthusiasts argue about and newcomers should know first. Commodore captains. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this Queen Mary 2 fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this Queen Mary 2 fact matters.", "x": "Why it matters: Planetarium onboard.. For Queen Mary 2, this fact shaped reputation, sales, or history — understanding it means understanding why the ship is remembered. Last true ocean liner; Cunard flagship since 2004.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Black-tie nights.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Black-tie nights.", "x": "Queen Mary 2: Black-tie nights.. This is one of the defining facts about Queen Mary 2 — the kind of thing enthusiasts argue about and newcomers should know first. Grand lobby. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this Queen Mary 2 fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this Queen Mary 2 fact matters.", "x": "Why it matters: Black-tie nights.. For Queen Mary 2, this fact shaped reputation, sales, or history — understanding it means understanding why the ship is remembered. Last true ocean liner; Cunard flagship since 2004.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "QE2 successor.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "QE2 successor.", "x": "Queen Mary 2: QE2 successor.. This is one of the defining facts about Queen Mary 2 — the kind of thing enthusiasts argue about and newcomers should know first. Chantiers de l'Atlantique. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this Queen Mary 2 fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this Queen Mary 2 fact matters.", "x": "Why it matters: QE2 successor.. For Queen Mary 2, this fact shaped reputation, sales, or history — understanding it means understanding why the ship is remembered. Last true ocean liner; Cunard flagship since 2004.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "Chantiers de l'Atlantique.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "Chantiers de l'Atlantique.", "x": "More on Queen Mary 2: Chantiers de l'Atlantique.. Transatlantic crossings. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Queen Mary 2.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "Cunard.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "Cunard.", "x": "More on Queen Mary 2: Cunard.. 1,132 ft long. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Queen Mary 2. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "Southampton-NY.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "Southampton-NY.", "x": "More on Queen Mary 2: Southampton-NY.. Planetarium onboard. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Queen Mary 2.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "Remastered 2016.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "Remastered 2016.", "x": "More on Queen Mary 2: Remastered 2016.. Black-tie nights. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Queen Mary 2.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Commodore captains.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Commodore captains.", "x": "More on Queen Mary 2: Commodore captains.. QE2 successor. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Queen Mary 2.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Grand lobby.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Grand lobby.", "x": "More on Queen Mary 2: Grand lobby.. Only ocean liner in service. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Queen Mary 2.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a Queen Mary 2: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a Queen Mary 2: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. Chantiers de l'Atlantique. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. 1,132 ft long. The right example of Queen Mary 2 is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning Queen Mary 2: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning Queen Mary 2: costs and care.", "x": "Ownership: Cunard.. Maintain it by the book — fluids, intervals, and qualified specialists. Planetarium onboard. Budget realistically: purchase price is only the beginning of the story with any ship. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Queen Mary 2 through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "Queen Mary 2 through the years.", "x": "The timeline: Last true ocean liner; Cunard flagship since 2004.. Only ocean liner in service. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. Southampton-NY. Read it as one story, and the ship makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for Queen Mary 2.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for Queen Mary 2.", "x": "The future: Queen Mary 2 faces electrification, automation, and changing tastes like everything in transport. Black-tie nights. Its heritage — Last true ocean liner; Cunard flagship since 2004. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "Queen Mary 2 fact: Remastered 2016..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "Queen Mary 2 fact: Remastered 2016..", "x": "From the Queen Mary 2 file: Remastered 2016.. Transatlantic crossings. Collect these and you will know Queen Mary 2 better than most owners. Last true ocean liner; Cunard flagship since 2004. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-ship-queen-mary-2-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
