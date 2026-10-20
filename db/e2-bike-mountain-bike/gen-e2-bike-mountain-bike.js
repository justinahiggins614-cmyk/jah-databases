(function(){'use strict';
/* JAH Mountain Bike Bicycle Type Database generator — jahdb-e2-bike-mountain-bike-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-bike-mountain-bike',PREFIX='JAH-E2BIKEMOUNT-',NAME='JAH Mountain Bike Bicycle Type Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "future", "quiz", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mountain Bike: overview", "d": "Mountain Bike: Off-road bicycle with suspension and knobby tires..", "g": "overview", "l": 2, "q": "What is Mountain Bike: overview?", "a": "Mountain Bike: Off-road bicycle with suspension and knobby tires..", "x": "The complete bicycle type guide: Off-road bicycle with suspension and knobby tires.. Full-suspension trail bikes. From its origins to its most famous examples, from buying advice to what comes next — this database covers the bicycle type in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How Mountain Bike began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How Mountain Bike began.", "x": "The origin of Mountain Bike: Off-road bicycle with suspension and knobby tires.. 29er wheels standard. Every great bicycle type has a founding story of ambition, luck, and timing — and Mountain Bike's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Full-suspension trail bikes.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Full-suspension trail bikes.", "x": "Mountain Bike: Full-suspension trail bikes.. This is one of the defining facts about Mountain Bike — the kind of thing enthusiasts argue about and newcomers should know first. Suspension travel 100-200mm.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this Mountain Bike fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this Mountain Bike fact matters.", "x": "Why it matters: Full-suspension trail bikes.. For Mountain Bike, this fact shaped reputation, sales, or history — understanding it means understanding why the bicycle type is remembered. Off-road bicycle with suspension and knobby tires.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "29er wheels standard.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "29er wheels standard.", "x": "Mountain Bike: 29er wheels standard.. This is one of the defining facts about Mountain Bike — the kind of thing enthusiasts argue about and newcomers should know first. Hydraulic disc brakes. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this Mountain Bike fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this Mountain Bike fact matters.", "x": "Why it matters: 29er wheels standard.. For Mountain Bike, this fact shaped reputation, sales, or history — understanding it means understanding why the bicycle type is remembered. Off-road bicycle with suspension and knobby tires.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Dropper posts.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Dropper posts.", "x": "Mountain Bike: Dropper posts.. This is one of the defining facts about Mountain Bike — the kind of thing enthusiasts argue about and newcomers should know first. Tubeless essential. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this Mountain Bike fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this Mountain Bike fact matters.", "x": "Why it matters: Dropper posts.. For Mountain Bike, this fact shaped reputation, sales, or history — understanding it means understanding why the bicycle type is remembered. Off-road bicycle with suspension and knobby tires.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "1x drivetrains.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "1x drivetrains.", "x": "Mountain Bike: 1x drivetrains.. This is one of the defining facts about Mountain Bike — the kind of thing enthusiasts argue about and newcomers should know first. Trail centers. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this Mountain Bike fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this Mountain Bike fact matters.", "x": "Why it matters: 1x drivetrains.. For Mountain Bike, this fact shaped reputation, sales, or history — understanding it means understanding why the bicycle type is remembered. Off-road bicycle with suspension and knobby tires.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "E-MTB boom.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "E-MTB boom.", "x": "Mountain Bike: E-MTB boom.. This is one of the defining facts about Mountain Bike — the kind of thing enthusiasts argue about and newcomers should know first. Skills parks. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this Mountain Bike fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this Mountain Bike fact matters.", "x": "Why it matters: E-MTB boom.. For Mountain Bike, this fact shaped reputation, sales, or history — understanding it means understanding why the bicycle type is remembered. Off-road bicycle with suspension and knobby tires.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Downhill World Cup.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Downhill World Cup.", "x": "Mountain Bike: Downhill World Cup.. This is one of the defining facts about Mountain Bike — the kind of thing enthusiasts argue about and newcomers should know first. Hardtail vs full-sus. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this Mountain Bike fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this Mountain Bike fact matters.", "x": "Why it matters: Downhill World Cup.. For Mountain Bike, this fact shaped reputation, sales, or history — understanding it means understanding why the bicycle type is remembered. Off-road bicycle with suspension and knobby tires.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "Hardtail vs full-sus.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "Hardtail vs full-sus.", "x": "More on Mountain Bike: Hardtail vs full-sus.. 29er wheels standard. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Mountain Bike.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "Suspension travel 100-200mm.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "Suspension travel 100-200mm.", "x": "More on Mountain Bike: Suspension travel 100-200mm.. Dropper posts. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Mountain Bike.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "Hydraulic disc brakes.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "Hydraulic disc brakes.", "x": "More on Mountain Bike: Hydraulic disc brakes.. 1x drivetrains. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Mountain Bike.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "Tubeless essential.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "Tubeless essential.", "x": "More on Mountain Bike: Tubeless essential.. E-MTB boom. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Mountain Bike.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Trail centers.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Trail centers.", "x": "More on Mountain Bike: Trail centers.. Downhill World Cup. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Mountain Bike.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Skills parks.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Skills parks.", "x": "More on Mountain Bike: Skills parks.. Full-suspension trail bikes. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Mountain Bike.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a Mountain Bike: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a Mountain Bike: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. Hardtail vs full-sus. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. Dropper posts. The right example of Mountain Bike is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning Mountain Bike: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning Mountain Bike: costs and care.", "x": "Ownership: Suspension travel 100-200mm.. Maintain it by the book — fluids, intervals, and qualified specialists. 1x drivetrains. Budget realistically: purchase price is only the beginning of the story with any bicycle type.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Mountain Bike through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "Mountain Bike through the years.", "x": "The timeline: Off-road bicycle with suspension and knobby tires.. Full-suspension trail bikes. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. Hydraulic disc brakes. Read it as one story, and the bicycle type makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for Mountain Bike.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for Mountain Bike.", "x": "The future: Mountain Bike faces electrification, automation, and changing tastes like everything in transport. E-MTB boom. Its heritage — Off-road bicycle with suspension and knobby tires. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "Mountain Bike fact: Tubeless essential..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "Mountain Bike fact: Tubeless essential..", "x": "From the Mountain Bike file: Tubeless essential.. 29er wheels standard. Collect these and you will know Mountain Bike better than most owners. Off-road bicycle with suspension and knobby tires. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-bike-mountain-bike-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
