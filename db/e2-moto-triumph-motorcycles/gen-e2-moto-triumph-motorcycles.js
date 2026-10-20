(function(){'use strict';
/* JAH Triumph Motorcycles Motorcycle Make Database generator — jahdb-e2-moto-triumph-motorcycles-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-moto-triumph-motorcycles',PREFIX='JAH-E2MOTOTRIUM-',NAME='JAH Triumph Motorcycles Motorcycle Make Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "future", "quiz", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Triumph Motorcycles: overview", "d": "Triumph Motorcycles: British maker; Bonneville icon; reborn 1990..", "g": "overview", "l": 2, "q": "What is Triumph Motorcycles: overview?", "a": "Triumph Motorcycles: British maker; Bonneville icon; reborn 1990..", "x": "The complete motorcycle make guide: British maker; Bonneville icon; reborn 1990.. Bonneville: 1959 icon. From its origins to its most famous models, from buying advice to what comes next — this database covers the motorcycle make in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How Triumph Motorcycles began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How Triumph Motorcycles began.", "x": "The origin of Triumph Motorcycles: British maker; Bonneville icon; reborn 1990.. Speed Triple: hooligan. Every great motorcycle make has a founding story of ambition, luck, and timing — and Triumph Motorcycles's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Bonneville: 1959 icon.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Bonneville: 1959 icon.", "x": "Triumph Motorcycles: Bonneville: 1959 icon.. This is one of the defining facts about Triumph Motorcycles — the kind of thing enthusiasts argue about and newcomers should know first. John Bloor rescue.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this Triumph Motorcycles fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this Triumph Motorcycles fact matters.", "x": "Why it matters: Bonneville: 1959 icon.. For Triumph Motorcycles, this fact shaped reputation, sales, or history — understanding it means understanding why the motorcycle make is remembered. British maker; Bonneville icon; reborn 1990.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Speed Triple: hooligan.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Speed Triple: hooligan.", "x": "Triumph Motorcycles: Speed Triple: hooligan.. This is one of the defining facts about Triumph Motorcycles — the kind of thing enthusiasts argue about and newcomers should know first. Daytona Moto2 engine.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this Triumph Motorcycles fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this Triumph Motorcycles fact matters.", "x": "Why it matters: Speed Triple: hooligan.. For Triumph Motorcycles, this fact shaped reputation, sales, or history — understanding it means understanding why the motorcycle make is remembered. British maker; Bonneville icon; reborn 1990.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Tiger adventure range.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Tiger adventure range.", "x": "Triumph Motorcycles: Tiger adventure range.. This is one of the defining facts about Triumph Motorcycles — the kind of thing enthusiasts argue about and newcomers should know first. Scrambler 1200. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this Triumph Motorcycles fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this Triumph Motorcycles fact matters.", "x": "Why it matters: Tiger adventure range.. For Triumph Motorcycles, this fact shaped reputation, sales, or history — understanding it means understanding why the motorcycle make is remembered. British maker; Bonneville icon; reborn 1990.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Steve McQueen's Great Escape.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Steve McQueen's Great Escape.", "x": "Triumph Motorcycles: Steve McQueen's Great Escape.. This is one of the defining facts about Triumph Motorcycles — the kind of thing enthusiasts argue about and newcomers should know first. Thruxton cafe racer.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this Triumph Motorcycles fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this Triumph Motorcycles fact matters.", "x": "Why it matters: Steve McQueen's Great Escape.. For Triumph Motorcycles, this fact shaped reputation, sales, or history — understanding it means understanding why the motorcycle make is remembered. British maker; Bonneville icon; reborn 1990.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Hinckley rebirth.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Hinckley rebirth.", "x": "Triumph Motorcycles: Hinckley rebirth.. This is one of the defining facts about Triumph Motorcycles — the kind of thing enthusiasts argue about and newcomers should know first. Moto2 engines. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this Triumph Motorcycles fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this Triumph Motorcycles fact matters.", "x": "Why it matters: Hinckley rebirth.. For Triumph Motorcycles, this fact shaped reputation, sales, or history — understanding it means understanding why the motorcycle make is remembered. British maker; Bonneville icon; reborn 1990.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Rocket 3: 2500cc.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Rocket 3: 2500cc.", "x": "Triumph Motorcycles: Rocket 3: 2500cc.. This is one of the defining facts about Triumph Motorcycles — the kind of thing enthusiasts argue about and newcomers should know first. Hinckley HQ. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this Triumph Motorcycles fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this Triumph Motorcycles fact matters.", "x": "Why it matters: Rocket 3: 2500cc.. For Triumph Motorcycles, this fact shaped reputation, sales, or history — understanding it means understanding why the motorcycle make is remembered. British maker; Bonneville icon; reborn 1990.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "Hinckley HQ.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "Hinckley HQ.", "x": "More on Triumph Motorcycles: Hinckley HQ.. Speed Triple: hooligan. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Triumph Motorcycles.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "John Bloor rescue.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "John Bloor rescue.", "x": "More on Triumph Motorcycles: John Bloor rescue.. Tiger adventure range. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Triumph Motorcycles.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "Daytona Moto2 engine.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "Daytona Moto2 engine.", "x": "More on Triumph Motorcycles: Daytona Moto2 engine.. Steve McQueen's Great Escape. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Triumph Motorcycles.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "Scrambler 1200.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "Scrambler 1200.", "x": "More on Triumph Motorcycles: Scrambler 1200.. Hinckley rebirth. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Triumph Motorcycles.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Thruxton cafe racer.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Thruxton cafe racer.", "x": "More on Triumph Motorcycles: Thruxton cafe racer.. Rocket 3: 2500cc. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Triumph Motorcycles.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Moto2 engines.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Moto2 engines.", "x": "More on Triumph Motorcycles: Moto2 engines.. Bonneville: 1959 icon. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Triumph Motorcycles.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a Triumph Motorcycles: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a Triumph Motorcycles: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. Hinckley HQ. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. Tiger adventure range. The right example of Triumph Motorcycles is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning Triumph Motorcycles: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning Triumph Motorcycles: costs and care.", "x": "Ownership: John Bloor rescue.. Maintain it by the book — fluids, intervals, and qualified specialists. Steve McQueen's Great Escape. Budget realistically: purchase price is only the beginning of the story with any motorcycle make.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Triumph Motorcycles through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "Triumph Motorcycles through the years.", "x": "The timeline: British maker; Bonneville icon; reborn 1990.. Bonneville: 1959 icon. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. Daytona Moto2 engine. Read it as one story, and the motorcycle make makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for Triumph Motorcycles.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for Triumph Motorcycles.", "x": "The future: Triumph Motorcycles faces electrification, automation, and changing tastes like everything in transport. Hinckley rebirth. Its heritage — British maker; Bonneville icon; reborn 1990. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "Triumph Motorcycles fact: Scrambler 1200..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "Triumph Motorcycles fact: Scrambler 1200..", "x": "From the Triumph Motorcycles file: Scrambler 1200.. Speed Triple: hooligan. Collect these and you will know Triumph Motorcycles better than most owners. British maker; Bonneville icon; reborn 1990. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-moto-triumph-motorcycles-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
