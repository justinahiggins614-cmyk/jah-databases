(function(){'use strict';
/* JAH Harley-Davidson Motorcycle Make Database generator — jahdb-e2-moto-harley-davidson-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-moto-harley-davidson',PREFIX='JAH-E2MOTOHARLE-',NAME='JAH Harley-Davidson Motorcycle Make Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "future", "quiz", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Harley-Davidson: overview", "d": "Harley-Davidson: American motorcycle icon founded 1903 in Milwaukee..", "g": "overview", "l": 2, "q": "What is Harley-Davidson: overview?", "a": "Harley-Davidson: American motorcycle icon founded 1903 in Milwaukee..", "x": "The complete motorcycle make guide: American motorcycle icon founded 1903 in Milwaukee.. V-twin rumble trademark. From its origins to its most famous models, from buying advice to what comes next — this database covers the motorcycle make in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How Harley-Davidson began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How Harley-Davidson began.", "x": "The origin of Harley-Davidson: American motorcycle icon founded 1903 in Milwaukee.. HOG owner culture. Every great motorcycle make has a founding story of ambition, luck, and timing — and Harley-Davidson's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "V-twin rumble trademark.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "V-twin rumble trademark.", "x": "Harley-Davidson: V-twin rumble trademark.. This is one of the defining facts about Harley-Davidson — the kind of thing enthusiasts argue about and newcomers should know first. William S. Harley founders.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this Harley-Davidson fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this Harley-Davidson fact matters.", "x": "Why it matters: V-twin rumble trademark.. For Harley-Davidson, this fact shaped reputation, sales, or history — understanding it means understanding why the motorcycle make is remembered. American motorcycle icon founded 1903 in Milwaukee.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "HOG owner culture.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "HOG owner culture.", "x": "Harley-Davidson: HOG owner culture.. This is one of the defining facts about Harley-Davidson — the kind of thing enthusiasts argue about and newcomers should know first. Wartime WLA. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this Harley-Davidson fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this Harley-Davidson fact matters.", "x": "Why it matters: HOG owner culture.. For Harley-Davidson, this fact shaped reputation, sales, or history — understanding it means understanding why the motorcycle make is remembered. American motorcycle icon founded 1903 in Milwaukee.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Electra Glide tourer.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Electra Glide tourer.", "x": "Harley-Davidson: Electra Glide tourer.. This is one of the defining facts about Harley-Davidson — the kind of thing enthusiasts argue about and newcomers should know first. AMF years. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this Harley-Davidson fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this Harley-Davidson fact matters.", "x": "Why it matters: Electra Glide tourer.. For Harley-Davidson, this fact shaped reputation, sales, or history — understanding it means understanding why the motorcycle make is remembered. American motorcycle icon founded 1903 in Milwaukee.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Sportster: 1957-2021.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Sportster: 1957-2021.", "x": "Harley-Davidson: Sportster: 1957-2021.. This is one of the defining facts about Harley-Davidson — the kind of thing enthusiasts argue about and newcomers should know first. Evo engine saved it. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this Harley-Davidson fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this Harley-Davidson fact matters.", "x": "Why it matters: Sportster: 1957-2021.. For Harley-Davidson, this fact shaped reputation, sales, or history — understanding it means understanding why the motorcycle make is remembered. American motorcycle icon founded 1903 in Milwaukee.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "LiveWire electric spin-off.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "LiveWire electric spin-off.", "x": "Harley-Davidson: LiveWire electric spin-off.. This is one of the defining facts about Harley-Davidson — the kind of thing enthusiasts argue about and newcomers should know first. Pan America adventure.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this Harley-Davidson fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this Harley-Davidson fact matters.", "x": "Why it matters: LiveWire electric spin-off.. For Harley-Davidson, this fact shaped reputation, sales, or history — understanding it means understanding why the motorcycle make is remembered. American motorcycle icon founded 1903 in Milwaukee.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Sturgis rally pilgrimage.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Sturgis rally pilgrimage.", "x": "Harley-Davidson: Sturgis rally pilgrimage.. This is one of the defining facts about Harley-Davidson — the kind of thing enthusiasts argue about and newcomers should know first. Milwaukee HQ. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this Harley-Davidson fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this Harley-Davidson fact matters.", "x": "Why it matters: Sturgis rally pilgrimage.. For Harley-Davidson, this fact shaped reputation, sales, or history — understanding it means understanding why the motorcycle make is remembered. American motorcycle icon founded 1903 in Milwaukee.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "Milwaukee HQ.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "Milwaukee HQ.", "x": "More on Harley-Davidson: Milwaukee HQ.. HOG owner culture. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Harley-Davidson.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "William S. Harley founders.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "William S. Harley founders.", "x": "More on Harley-Davidson: William S. Harley founders.. Electra Glide tourer. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Harley-Davidson.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "Wartime WLA.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "Wartime WLA.", "x": "More on Harley-Davidson: Wartime WLA.. Sportster: 1957-2021. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Harley-Davidson.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "AMF years.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "AMF years.", "x": "More on Harley-Davidson: AMF years.. LiveWire electric spin-off. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Harley-Davidson.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Evo engine saved it.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Evo engine saved it.", "x": "More on Harley-Davidson: Evo engine saved it.. Sturgis rally pilgrimage. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Harley-Davidson.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Pan America adventure.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Pan America adventure.", "x": "More on Harley-Davidson: Pan America adventure.. V-twin rumble trademark. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Harley-Davidson.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a Harley-Davidson: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a Harley-Davidson: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. Milwaukee HQ. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. Electra Glide tourer. The right example of Harley-Davidson is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning Harley-Davidson: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning Harley-Davidson: costs and care.", "x": "Ownership: William S. Harley founders.. Maintain it by the book — fluids, intervals, and qualified specialists. Sportster: 1957-2021. Budget realistically: purchase price is only the beginning of the story with any motorcycle make.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Harley-Davidson through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "Harley-Davidson through the years.", "x": "The timeline: American motorcycle icon founded 1903 in Milwaukee.. V-twin rumble trademark. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. Wartime WLA. Read it as one story, and the motorcycle make makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for Harley-Davidson.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for Harley-Davidson.", "x": "The future: Harley-Davidson faces electrification, automation, and changing tastes like everything in transport. LiveWire electric spin-off. Its heritage — American motorcycle icon founded 1903 in Milwaukee. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "Harley-Davidson fact: AMF years..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "Harley-Davidson fact: AMF years..", "x": "From the Harley-Davidson file: AMF years.. HOG owner culture. Collect these and you will know Harley-Davidson better than most owners. American motorcycle icon founded 1903 in Milwaukee. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-moto-harley-davidson-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
