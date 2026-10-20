(function(){'use strict';
/* JAH Semi Truck Truck Type Database generator — jahdb-e2-truck-semi-truck-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-truck-semi-truck',PREFIX='JAH-E2TRUCKSEMI-',NAME='JAH Semi Truck Truck Type Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "future", "quiz", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Semi Truck: overview", "d": "Semi Truck: Class 8 tractor-trailer hauling freight..", "g": "overview", "l": 2, "q": "What is Semi Truck: overview?", "a": "Semi Truck: Class 8 tractor-trailer hauling freight..", "x": "The complete truck type guide: Class 8 tractor-trailer hauling freight.. 18-wheelers. From its origins to its most famous examples, from buying advice to what comes next — this database covers the truck type in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How Semi Truck began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How Semi Truck began.", "x": "The origin of Semi Truck: Class 8 tractor-trailer hauling freight.. Sleeper cabs. Every great truck type has a founding story of ambition, luck, and timing — and Semi Truck's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "18-wheelers.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "18-wheelers.", "x": "Semi Truck: 18-wheelers.. This is one of the defining facts about Semi Truck — the kind of thing enthusiasts argue about and newcomers should know first. 80,000 lb GVW. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this Semi Truck fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this Semi Truck fact matters.", "x": "Why it matters: 18-wheelers.. For Semi Truck, this fact shaped reputation, sales, or history — understanding it means understanding why the truck type is remembered. Class 8 tractor-trailer hauling freight.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Sleeper cabs.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Sleeper cabs.", "x": "Semi Truck: Sleeper cabs.. This is one of the defining facts about Semi Truck — the kind of thing enthusiasts argue about and newcomers should know first. ELD mandates. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this Semi Truck fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this Semi Truck fact matters.", "x": "Why it matters: Sleeper cabs.. For Semi Truck, this fact shaped reputation, sales, or history — understanding it means understanding why the truck type is remembered. Class 8 tractor-trailer hauling freight.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "500+ hp diesels.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "500+ hp diesels.", "x": "Semi Truck: 500+ hp diesels.. This is one of the defining facts about Semi Truck — the kind of thing enthusiasts argue about and newcomers should know first. Truck stops. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this Semi Truck fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this Semi Truck fact matters.", "x": "Why it matters: 500+ hp diesels.. For Semi Truck, this fact shaped reputation, sales, or history — understanding it means understanding why the truck type is remembered. Class 8 tractor-trailer hauling freight.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Logistics backbone.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Logistics backbone.", "x": "Semi Truck: Logistics backbone.. This is one of the defining facts about Semi Truck — the kind of thing enthusiasts argue about and newcomers should know first. CDL license. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this Semi Truck fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this Semi Truck fact matters.", "x": "Why it matters: Logistics backbone.. For Semi Truck, this fact shaped reputation, sales, or history — understanding it means understanding why the truck type is remembered. Class 8 tractor-trailer hauling freight.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Owner-operators.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Owner-operators.", "x": "Semi Truck: Owner-operators.. This is one of the defining facts about Semi Truck — the kind of thing enthusiasts argue about and newcomers should know first. Freight rates. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this Semi Truck fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this Semi Truck fact matters.", "x": "Why it matters: Owner-operators.. For Semi Truck, this fact shaped reputation, sales, or history — understanding it means understanding why the truck type is remembered. Class 8 tractor-trailer hauling freight.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Electric semis coming.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Electric semis coming.", "x": "Semi Truck: Electric semis coming.. This is one of the defining facts about Semi Truck — the kind of thing enthusiasts argue about and newcomers should know first. Fifth wheel. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this Semi Truck fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this Semi Truck fact matters.", "x": "Why it matters: Electric semis coming.. For Semi Truck, this fact shaped reputation, sales, or history — understanding it means understanding why the truck type is remembered. Class 8 tractor-trailer hauling freight.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "Fifth wheel.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "Fifth wheel.", "x": "More on Semi Truck: Fifth wheel.. Sleeper cabs. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Semi Truck. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "80,000 lb GVW.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "80,000 lb GVW.", "x": "More on Semi Truck: 80,000 lb GVW.. 500+ hp diesels. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Semi Truck.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "ELD mandates.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "ELD mandates.", "x": "More on Semi Truck: ELD mandates.. Logistics backbone. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Semi Truck.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "Truck stops.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "Truck stops.", "x": "More on Semi Truck: Truck stops.. Owner-operators. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Semi Truck. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "CDL license.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "CDL license.", "x": "More on Semi Truck: CDL license.. Electric semis coming. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Semi Truck.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Freight rates.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Freight rates.", "x": "More on Semi Truck: Freight rates.. 18-wheelers. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Semi Truck. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a Semi Truck: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a Semi Truck: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. Fifth wheel. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. 500+ hp diesels. The right example of Semi Truck is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning Semi Truck: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning Semi Truck: costs and care.", "x": "Ownership: 80,000 lb GVW.. Maintain it by the book — fluids, intervals, and qualified specialists. Logistics backbone. Budget realistically: purchase price is only the beginning of the story with any truck type.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Semi Truck through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "Semi Truck through the years.", "x": "The timeline: Class 8 tractor-trailer hauling freight.. 18-wheelers. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. ELD mandates. Read it as one story, and the truck type makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for Semi Truck.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for Semi Truck.", "x": "The future: Semi Truck faces electrification, automation, and changing tastes like everything in transport. Owner-operators. Its heritage — Class 8 tractor-trailer hauling freight. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "Semi Truck fact: Truck stops..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "Semi Truck fact: Truck stops..", "x": "From the Semi Truck file: Truck stops.. Sleeper cabs. Collect these and you will know Semi Truck better than most owners. Class 8 tractor-trailer hauling freight. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-truck-semi-truck-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
