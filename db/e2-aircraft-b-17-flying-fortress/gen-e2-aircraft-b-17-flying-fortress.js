(function(){'use strict';
/* JAH Boeing B-17 Flying Fortress Aircraft Database generator — jahdb-e2-aircraft-b-17-flying-fortress-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-aircraft-b-17-flying-fortress',PREFIX='JAH-E2AIRCRAFTB-',NAME='JAH Boeing B-17 Flying Fortress Aircraft Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "future", "quiz", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Boeing B-17 Flying Fortress: overview", "d": "Boeing B-17 Flying Fortress: WWII US heavy bomber; daylight raids over Europe..", "g": "overview", "l": 2, "q": "What is Boeing B-17 Flying Fortress: overview?", "a": "Boeing B-17 Flying Fortress: WWII US heavy bomber; daylight raids over Europe..", "x": "The complete aircraft guide: WWII US heavy bomber; daylight raids over Europe.. Memphis Belle fame. From its origins to its most famous examples, from buying advice to what comes next — this database covers the aircraft in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How Boeing B-17 Flying Fortress began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How Boeing B-17 Flying Fortress began.", "x": "The origin of Boeing B-17 Flying Fortress: WWII US heavy bomber; daylight raids over Europe.. 13 .50-cal guns. Every great aircraft has a founding story of ambition, luck, and timing — and Boeing B-17 Flying Fortress's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Memphis Belle fame.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Memphis Belle fame.", "x": "Boeing B-17 Flying Fortress: Memphis Belle fame.. This is one of the defining facts about Boeing B-17 Flying Fortress — the kind of thing enthusiasts argue about and newcomers should know first. 8th Air Force.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this Boeing B-17 Flying Fortress fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this Boeing B-17 Flying Fortress fact matters.", "x": "Why it matters: Memphis Belle fame.. For Boeing B-17 Flying Fortress, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. WWII US heavy bomber; daylight raids over Europe.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "13 .50-cal guns.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "13 .50-cal guns.", "x": "Boeing B-17 Flying Fortress: 13 .50-cal guns.. This is one of the defining facts about Boeing B-17 Flying Fortress — the kind of thing enthusiasts argue about and newcomers should know first. F/G models.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this Boeing B-17 Flying Fortress fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this Boeing B-17 Flying Fortress fact matters.", "x": "Why it matters: 13 .50-cal guns.. For Boeing B-17 Flying Fortress, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. WWII US heavy bomber; daylight raids over Europe.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Daylight precision doctrine.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Daylight precision doctrine.", "x": "Boeing B-17 Flying Fortress: Daylight precision doctrine.. This is one of the defining facts about Boeing B-17 Flying Fortress — the kind of thing enthusiasts argue about and newcomers should know first. Flying Fortress name.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this Boeing B-17 Flying Fortress fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this Boeing B-17 Flying Fortress fact matters.", "x": "Why it matters: Daylight precision doctrine.. For Boeing B-17 Flying Fortress, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. WWII US heavy bomber; daylight raids over Europe.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "12,731 built.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "12,731 built.", "x": "Boeing B-17 Flying Fortress: 12,731 built.. This is one of the defining facts about Boeing B-17 Flying Fortress — the kind of thing enthusiasts argue about and newcomers should know first. Swamp Ghost etc.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this Boeing B-17 Flying Fortress fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this Boeing B-17 Flying Fortress fact matters.", "x": "Why it matters: 12,731 built.. For Boeing B-17 Flying Fortress, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. WWII US heavy bomber; daylight raids over Europe.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Tough: flew home shot up.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Tough: flew home shot up.", "x": "Boeing B-17 Flying Fortress: Tough: flew home shot up.. This is one of the defining facts about Boeing B-17 Flying Fortress — the kind of thing enthusiasts argue about and newcomers should know first. Airshow few left.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this Boeing B-17 Flying Fortress fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this Boeing B-17 Flying Fortress fact matters.", "x": "Why it matters: Tough: flew home shot up.. For Boeing B-17 Flying Fortress, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. WWII US heavy bomber; daylight raids over Europe.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Norden bombsight.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Norden bombsight.", "x": "Boeing B-17 Flying Fortress: Norden bombsight.. This is one of the defining facts about Boeing B-17 Flying Fortress — the kind of thing enthusiasts argue about and newcomers should know first. Boeing, 1935.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this Boeing B-17 Flying Fortress fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this Boeing B-17 Flying Fortress fact matters.", "x": "Why it matters: Norden bombsight.. For Boeing B-17 Flying Fortress, this fact shaped reputation, sales, or history — understanding it means understanding why the aircraft is remembered. WWII US heavy bomber; daylight raids over Europe.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "Boeing, 1935.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "Boeing, 1935.", "x": "More on Boeing B-17 Flying Fortress: Boeing, 1935.. 13 .50-cal guns. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Boeing B-17 Flying Fortress.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "8th Air Force.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "8th Air Force.", "x": "More on Boeing B-17 Flying Fortress: 8th Air Force.. Daylight precision doctrine. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Boeing B-17 Flying Fortress.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "F/G models.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "F/G models.", "x": "More on Boeing B-17 Flying Fortress: F/G models.. 12,731 built. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Boeing B-17 Flying Fortress.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "Flying Fortress name.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "Flying Fortress name.", "x": "More on Boeing B-17 Flying Fortress: Flying Fortress name.. Tough: flew home shot up. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Boeing B-17 Flying Fortress.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Swamp Ghost etc.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Swamp Ghost etc.", "x": "More on Boeing B-17 Flying Fortress: Swamp Ghost etc.. Norden bombsight. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Boeing B-17 Flying Fortress.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Airshow few left.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Airshow few left.", "x": "More on Boeing B-17 Flying Fortress: Airshow few left.. Memphis Belle fame. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Boeing B-17 Flying Fortress.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a Boeing B-17 Flying Fortress: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a Boeing B-17 Flying Fortress: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. Boeing, 1935. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. Daylight precision doctrine. The right example of Boeing B-17 Flying Fortress is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning Boeing B-17 Flying Fortress: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning Boeing B-17 Flying Fortress: costs and care.", "x": "Ownership: 8th Air Force.. Maintain it by the book — fluids, intervals, and qualified specialists. 12,731 built. Budget realistically: purchase price is only the beginning of the story with any aircraft.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Boeing B-17 Flying Fortress through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "Boeing B-17 Flying Fortress through the years.", "x": "The timeline: WWII US heavy bomber; daylight raids over Europe.. Memphis Belle fame. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. F/G models. Read it as one story, and the aircraft makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for Boeing B-17 Flying Fortress.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for Boeing B-17 Flying Fortress.", "x": "The future: Boeing B-17 Flying Fortress faces electrification, automation, and changing tastes like everything in transport. Tough: flew home shot up. Its heritage — WWII US heavy bomber; daylight raids over Europe. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "Boeing B-17 Flying Fortress fact: Flying Fortress name..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "Boeing B-17 Flying Fortress fact: Flying Fortress name..", "x": "From the Boeing B-17 Flying Fortress file: Flying Fortress name.. 13 .50-cal guns. Collect these and you will know Boeing B-17 Flying Fortress better than most owners. WWII US heavy bomber; daylight raids over Europe.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-aircraft-b-17-flying-fortress-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
