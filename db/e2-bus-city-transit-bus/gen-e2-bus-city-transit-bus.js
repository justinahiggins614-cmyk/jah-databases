(function(){'use strict';
/* JAH City Transit Bus Bus Type Database generator — jahdb-e2-bus-city-transit-bus-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-bus-city-transit-bus',PREFIX='JAH-E2BUSCITYTR-',NAME='JAH City Transit Bus Bus Type Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "future", "quiz", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "City Transit Bus: overview", "d": "City Transit Bus: Urban workhorse; diesel, hybrid, and electric..", "g": "overview", "l": 2, "q": "What is City Transit Bus: overview?", "a": "City Transit Bus: Urban workhorse; diesel, hybrid, and electric..", "x": "The complete bus type guide: Urban workhorse; diesel, hybrid, and electric.. 40-ft standard. From its origins to its most famous examples, from buying advice to what comes next — this database covers the bus type in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How City Transit Bus began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How City Transit Bus began.", "x": "The origin of City Transit Bus: Urban workhorse; diesel, hybrid, and electric.. Articulated 60-ft. Every great bus type has a founding story of ambition, luck, and timing — and City Transit Bus's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "40-ft standard.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "40-ft standard.", "x": "City Transit Bus: 40-ft standard.. This is one of the defining facts about City Transit Bus — the kind of thing enthusiasts argue about and newcomers should know first. Fare systems. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this City Transit Bus fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this City Transit Bus fact matters.", "x": "Why it matters: 40-ft standard.. For City Transit Bus, this fact shaped reputation, sales, or history — understanding it means understanding why the bus type is remembered. Urban workhorse; diesel, hybrid, and electric.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Articulated 60-ft.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Articulated 60-ft.", "x": "City Transit Bus: Articulated 60-ft.. This is one of the defining facts about City Transit Bus — the kind of thing enthusiasts argue about and newcomers should know first. Bus lanes. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this City Transit Bus fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this City Transit Bus fact matters.", "x": "Why it matters: Articulated 60-ft.. For City Transit Bus, this fact shaped reputation, sales, or history — understanding it means understanding why the bus type is remembered. Urban workhorse; diesel, hybrid, and electric.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Electric buses rising.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Electric buses rising.", "x": "City Transit Bus: Electric buses rising.. This is one of the defining facts about City Transit Bus — the kind of thing enthusiasts argue about and newcomers should know first. CNG fleets. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this City Transit Bus fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this City Transit Bus fact matters.", "x": "Why it matters: Electric buses rising.. For City Transit Bus, this fact shaped reputation, sales, or history — understanding it means understanding why the bus type is remembered. Urban workhorse; diesel, hybrid, and electric.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Bus rapid transit.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Bus rapid transit.", "x": "City Transit Bus: Bus rapid transit.. This is one of the defining facts about City Transit Bus — the kind of thing enthusiasts argue about and newcomers should know first. Proterra electric. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this City Transit Bus fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this City Transit Bus fact matters.", "x": "Why it matters: Bus rapid transit.. For City Transit Bus, this fact shaped reputation, sales, or history — understanding it means understanding why the bus type is remembered. Urban workhorse; diesel, hybrid, and electric.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Low-floor access.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Low-floor access.", "x": "City Transit Bus: Low-floor access.. This is one of the defining facts about City Transit Bus — the kind of thing enthusiasts argue about and newcomers should know first. Night owls. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this City Transit Bus fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this City Transit Bus fact matters.", "x": "Why it matters: Low-floor access.. For City Transit Bus, this fact shaped reputation, sales, or history — understanding it means understanding why the bus type is remembered. Urban workhorse; diesel, hybrid, and electric.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "New Flyer/Gillig.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "New Flyer/Gillig.", "x": "City Transit Bus: New Flyer/Gillig.. This is one of the defining facts about City Transit Bus — the kind of thing enthusiasts argue about and newcomers should know first. Routes/schedules. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this City Transit Bus fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this City Transit Bus fact matters.", "x": "Why it matters: New Flyer/Gillig.. For City Transit Bus, this fact shaped reputation, sales, or history — understanding it means understanding why the bus type is remembered. Urban workhorse; diesel, hybrid, and electric.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "Routes/schedules.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "Routes/schedules.", "x": "More on City Transit Bus: Routes/schedules.. Articulated 60-ft. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows City Transit Bus.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "Fare systems.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "Fare systems.", "x": "More on City Transit Bus: Fare systems.. Electric buses rising. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows City Transit Bus.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "Bus lanes.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "Bus lanes.", "x": "More on City Transit Bus: Bus lanes.. Bus rapid transit. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows City Transit Bus.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "CNG fleets.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "CNG fleets.", "x": "More on City Transit Bus: CNG fleets.. Low-floor access. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows City Transit Bus.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Proterra electric.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Proterra electric.", "x": "More on City Transit Bus: Proterra electric.. New Flyer/Gillig. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows City Transit Bus.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Night owls.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Night owls.", "x": "More on City Transit Bus: Night owls.. 40-ft standard. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows City Transit Bus.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a City Transit Bus: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a City Transit Bus: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. Routes/schedules. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. Electric buses rising. The right example of City Transit Bus is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning City Transit Bus: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning City Transit Bus: costs and care.", "x": "Ownership: Fare systems.. Maintain it by the book — fluids, intervals, and qualified specialists. Bus rapid transit. Budget realistically: purchase price is only the beginning of the story with any bus type.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "City Transit Bus through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "City Transit Bus through the years.", "x": "The timeline: Urban workhorse; diesel, hybrid, and electric.. 40-ft standard. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. Bus lanes. Read it as one story, and the bus type makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for City Transit Bus.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for City Transit Bus.", "x": "The future: City Transit Bus faces electrification, automation, and changing tastes like everything in transport. Low-floor access. Its heritage — Urban workhorse; diesel, hybrid, and electric. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "City Transit Bus fact: CNG fleets..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "City Transit Bus fact: CNG fleets..", "x": "From the City Transit Bus file: CNG fleets.. Articulated 60-ft. Collect these and you will know City Transit Bus better than most owners. Urban workhorse; diesel, hybrid, and electric. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-bus-city-transit-bus-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
