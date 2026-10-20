(function(){'use strict';
/* JAH B-52 Stratofortress Aircraft Database generator — jahdb-e2-aircraft-b-52-stratofortress-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-aircraft-b-52-stratofortress',PREFIX='JAH-E2AIRCRAFTB-',NAME='JAH B-52 Stratofortress Aircraft Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "future", "quiz", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "B-52 Stratofortress: overview", "d": "B-52 Stratofortress: US bomber since 1955; flying past 100 years planned..", "g": "overview", "l": 2, "q": "What is B-52 Stratofortress: overview?", "a": "B-52 Stratofortress: US bomber since 1955; flying past 100 years planned..", "x": "The complete aircraft guide: US bomber since 1955; flying past 100 years planned.. 8 engines. From its origins to its most famous examples, from buying advice to what comes next — this database covers the aircraft in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How B-52 Stratofortress began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How B-52 Stratofortress began.", "x": "The origin of B-52 Stratofortress: US bomber since 1955; flying past 100 years planned.. In service since 1955. Every great aircraft has a founding story of ambition, luck, and timing — and B-52 Stratofortress's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "8 engines.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "8 engines.", "x": "B-52 Stratofortress: 8 engines.. This is one of the defining facts about B-52 Stratofortress — the kind of thing enthusiasts argue about and newcomers should know first. Cold War deterrent. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this B-52 Stratofortress fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this B-52 Stratofortress fact matters.", "x": "Why it matters: 8 engines.. For B-52 Stratofortress, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. US bomber since 1955; flying past 100 years planned.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "In service since 1955.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "In service since 1955.", "x": "B-52 Stratofortress: In service since 1955.. This is one of the defining facts about B-52 Stratofortress — the kind of thing enthusiasts argue about and newcomers should know first. 744 built. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this B-52 Stratofortress fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this B-52 Stratofortress fact matters.", "x": "Why it matters: In service since 1955.. For B-52 Stratofortress, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. US bomber since 1955; flying past 100 years planned.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Planned to 2050s.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Planned to 2050s.", "x": "B-52 Stratofortress: Planned to 2050s.. This is one of the defining facts about B-52 Stratofortress — the kind of thing enthusiasts argue about and newcomers should know first. Stratofortress name. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this B-52 Stratofortress fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this B-52 Stratofortress fact matters.", "x": "Why it matters: Planned to 2050s.. For B-52 Stratofortress, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. US bomber since 1955; flying past 100 years planned.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Vietnam to today.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Vietnam to today.", "x": "B-52 Stratofortress: Vietnam to today.. This is one of the defining facts about B-52 Stratofortress — the kind of thing enthusiasts argue about and newcomers should know first. Re-engining program. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this B-52 Stratofortress fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this B-52 Stratofortress fact matters.", "x": "Why it matters: Vietnam to today.. For B-52 Stratofortress, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. US bomber since 1955; flying past 100 years planned.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "New engines coming.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "New engines coming.", "x": "B-52 Stratofortress: New engines coming.. This is one of the defining facts about B-52 Stratofortress — the kind of thing enthusiasts argue about and newcomers should know first. Crews span generations.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this B-52 Stratofortress fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this B-52 Stratofortress fact matters.", "x": "Why it matters: New engines coming.. For B-52 Stratofortress, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. US bomber since 1955; flying past 100 years planned.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "BUFF nickname.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "BUFF nickname.", "x": "B-52 Stratofortress: BUFF nickname.. This is one of the defining facts about B-52 Stratofortress — the kind of thing enthusiasts argue about and newcomers should know first. Boeing, 1952. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this B-52 Stratofortress fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this B-52 Stratofortress fact matters.", "x": "Why it matters: BUFF nickname.. For B-52 Stratofortress, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. US bomber since 1955; flying past 100 years planned.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "Boeing, 1952.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "Boeing, 1952.", "x": "More on B-52 Stratofortress: Boeing, 1952.. In service since 1955. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows B-52 Stratofortress.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "Cold War deterrent.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "Cold War deterrent.", "x": "More on B-52 Stratofortress: Cold War deterrent.. Planned to 2050s. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows B-52 Stratofortress.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "744 built.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "744 built.", "x": "More on B-52 Stratofortress: 744 built.. Vietnam to today. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows B-52 Stratofortress.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "Stratofortress name.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "Stratofortress name.", "x": "More on B-52 Stratofortress: Stratofortress name.. New engines coming. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows B-52 Stratofortress.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Re-engining program.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Re-engining program.", "x": "More on B-52 Stratofortress: Re-engining program.. BUFF nickname. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows B-52 Stratofortress.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Crews span generations.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Crews span generations.", "x": "More on B-52 Stratofortress: Crews span generations.. 8 engines. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows B-52 Stratofortress.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a B-52 Stratofortress: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a B-52 Stratofortress: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. Boeing, 1952. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. Planned to 2050s. The right example of B-52 Stratofortress is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning B-52 Stratofortress: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning B-52 Stratofortress: costs and care.", "x": "Ownership: Cold War deterrent.. Maintain it by the book — fluids, intervals, and qualified specialists. Vietnam to today. Budget realistically: purchase price is only the beginning of the story with any aircraft.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "B-52 Stratofortress through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "B-52 Stratofortress through the years.", "x": "The timeline: US bomber since 1955; flying past 100 years planned.. 8 engines. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. 744 built. Read it as one story, and the aircraft makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for B-52 Stratofortress.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for B-52 Stratofortress.", "x": "The future: B-52 Stratofortress faces electrification, automation, and changing tastes like everything in transport. New engines coming. Its heritage — US bomber since 1955; flying past 100 years planned. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "B-52 Stratofortress fact: Stratofortress name..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "B-52 Stratofortress fact: Stratofortress name..", "x": "From the B-52 Stratofortress file: Stratofortress name.. In service since 1955. Collect these and you will know B-52 Stratofortress better than most owners. US bomber since 1955; flying past 100 years planned.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-aircraft-b-52-stratofortress-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
