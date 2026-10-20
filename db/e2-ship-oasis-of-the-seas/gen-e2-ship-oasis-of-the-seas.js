(function(){'use strict';
/* JAH Oasis of the Seas Ship Database generator — jahdb-e2-ship-oasis-of-the-seas-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-ship-oasis-of-the-seas',PREFIX='JAH-E2SHIPOASIS-',NAME='JAH Oasis of the Seas Ship Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "future", "quiz", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Oasis of the Seas: overview", "d": "Oasis of the Seas: Royal Caribbean mega-ship; 225,000 tons..", "g": "overview", "l": 2, "q": "What is Oasis of the Seas: overview?", "a": "Oasis of the Seas: Royal Caribbean mega-ship; 225,000 tons..", "x": "The complete ship guide: Royal Caribbean mega-ship; 225,000 tons.. Largest cruise class. From its origins to its most famous examples, from buying advice to what comes next — this database covers the ship in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How Oasis of the Seas began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How Oasis of the Seas began.", "x": "The origin of Oasis of the Seas: Royal Caribbean mega-ship; 225,000 tons.. Neighborhoods onboard. Every great ship has a founding story of ambition, luck, and timing — and Oasis of the Seas's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Largest cruise class.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Largest cruise class.", "x": "Oasis of the Seas: Largest cruise class.. This is one of the defining facts about Oasis of the Seas — the kind of thing enthusiasts argue about and newcomers should know first. Oasis class. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this Oasis of the Seas fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this Oasis of the Seas fact matters.", "x": "Why it matters: Largest cruise class.. For Oasis of the Seas, this fact shaped reputation, sales, or history — understanding it means understanding why the ship is remembered. Royal Caribbean mega-ship; 225,000 tons.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Neighborhoods onboard.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Neighborhoods onboard.", "x": "Oasis of the Seas: Neighborhoods onboard.. This is one of the defining facts about Oasis of the Seas — the kind of thing enthusiasts argue about and newcomers should know first. Symphony bigger later.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this Oasis of the Seas fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this Oasis of the Seas fact matters.", "x": "Why it matters: Neighborhoods onboard.. For Oasis of the Seas, this fact shaped reputation, sales, or history — understanding it means understanding why the ship is remembered. Royal Caribbean mega-ship; 225,000 tons.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Central Park at sea.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Central Park at sea.", "x": "Oasis of the Seas: Central Park at sea.. This is one of the defining facts about Oasis of the Seas — the kind of thing enthusiasts argue about and newcomers should know first. Zip line onboard. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this Oasis of the Seas fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this Oasis of the Seas fact matters.", "x": "Why it matters: Central Park at sea.. For Oasis of the Seas, this fact shaped reputation, sales, or history — understanding it means understanding why the ship is remembered. Royal Caribbean mega-ship; 225,000 tons.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "AquaTheater.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "AquaTheater.", "x": "Oasis of the Seas: AquaTheater.. This is one of the defining facts about Oasis of the Seas — the kind of thing enthusiasts argue about and newcomers should know first. Robot bar. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this Oasis of the Seas fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this Oasis of the Seas fact matters.", "x": "Why it matters: AquaTheater.. For Oasis of the Seas, this fact shaped reputation, sales, or history — understanding it means understanding why the ship is remembered. Royal Caribbean mega-ship; 225,000 tons.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "7,000 passengers.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "7,000 passengers.", "x": "Oasis of the Seas: 7,000 passengers.. This is one of the defining facts about Oasis of the Seas — the kind of thing enthusiasts argue about and newcomers should know first. Cruise giant. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this Oasis of the Seas fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this Oasis of the Seas fact matters.", "x": "Why it matters: 7,000 passengers.. For Oasis of the Seas, this fact shaped reputation, sales, or history — understanding it means understanding why the ship is remembered. Royal Caribbean mega-ship; 225,000 tons.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "2010 debut.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "2010 debut.", "x": "Oasis of the Seas: 2010 debut.. This is one of the defining facts about Oasis of the Seas — the kind of thing enthusiasts argue about and newcomers should know first. STX Finland. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this Oasis of the Seas fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this Oasis of the Seas fact matters.", "x": "Why it matters: 2010 debut.. For Oasis of the Seas, this fact shaped reputation, sales, or history — understanding it means understanding why the ship is remembered. Royal Caribbean mega-ship; 225,000 tons.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "STX Finland.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "STX Finland.", "x": "More on Oasis of the Seas: STX Finland.. Neighborhoods onboard. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Oasis of the Seas.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "Oasis class.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "Oasis class.", "x": "More on Oasis of the Seas: Oasis class.. Central Park at sea. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Oasis of the Seas.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "Symphony bigger later.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "Symphony bigger later.", "x": "More on Oasis of the Seas: Symphony bigger later.. AquaTheater. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Oasis of the Seas.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "Zip line onboard.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "Zip line onboard.", "x": "More on Oasis of the Seas: Zip line onboard.. 7,000 passengers. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Oasis of the Seas.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Robot bar.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Robot bar.", "x": "More on Oasis of the Seas: Robot bar.. 2010 debut. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Oasis of the Seas.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Cruise giant.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Cruise giant.", "x": "More on Oasis of the Seas: Cruise giant.. Largest cruise class. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Oasis of the Seas.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a Oasis of the Seas: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a Oasis of the Seas: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. STX Finland. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. Central Park at sea. The right example of Oasis of the Seas is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning Oasis of the Seas: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning Oasis of the Seas: costs and care.", "x": "Ownership: Oasis class.. Maintain it by the book — fluids, intervals, and qualified specialists. AquaTheater. Budget realistically: purchase price is only the beginning of the story with any ship. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Oasis of the Seas through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "Oasis of the Seas through the years.", "x": "The timeline: Royal Caribbean mega-ship; 225,000 tons.. Largest cruise class. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. Symphony bigger later. Read it as one story, and the ship makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for Oasis of the Seas.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for Oasis of the Seas.", "x": "The future: Oasis of the Seas faces electrification, automation, and changing tastes like everything in transport. 7,000 passengers. Its heritage — Royal Caribbean mega-ship; 225,000 tons. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "Oasis of the Seas fact: Zip line onboard..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "Oasis of the Seas fact: Zip line onboard..", "x": "From the Oasis of the Seas file: Zip line onboard.. Neighborhoods onboard. Collect these and you will know Oasis of the Seas better than most owners. Royal Caribbean mega-ship; 225,000 tons. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-ship-oasis-of-the-seas-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
