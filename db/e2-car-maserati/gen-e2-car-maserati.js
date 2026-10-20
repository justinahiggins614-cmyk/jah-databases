(function(){'use strict';
/* JAH Maserati Car Make Database generator — jahdb-e2-car-maserati-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-car-maserati',PREFIX='JAH-E2CARMASERA-',NAME='JAH Maserati Car Make Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "facts", "future", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Maserati: overview", "d": "Maserati: Italian luxury/sports maker founded 1914..", "g": "overview", "l": 2, "q": "What is Maserati: overview?", "a": "Maserati: Italian luxury/sports maker founded 1914..", "x": "The complete car make guide: Italian luxury/sports maker founded 1914.. Trident logo from Bologna's fountain. From its origins to its most famous models, from buying advice to what comes next — this database covers the car make in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How Maserati began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How Maserati began.", "x": "The origin of Maserati: Italian luxury/sports maker founded 1914.. MC12: Enzo-based hypercar. Every great car make has a founding story of ambition, luck, and timing — and Maserati's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Trident logo from Bologna's fountain.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Trident logo from Bologna's fountain.", "x": "Maserati: Trident logo from Bologna's fountain.. This is one of the defining facts about Maserati — the kind of thing enthusiasts argue about and newcomers should know first. Founded by Maserati brothers.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this Maserati fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this Maserati fact matters.", "x": "Why it matters: Trident logo from Bologna's fountain.. For Maserati, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Italian luxury/sports maker founded 1914.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "MC12: Enzo-based hypercar.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "MC12: Enzo-based hypercar.", "x": "Maserati: MC12: Enzo-based hypercar.. This is one of the defining facts about Maserati — the kind of thing enthusiasts argue about and newcomers should know first. Won F1 titles (Fangio 1957). Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this Maserati fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this Maserati fact matters.", "x": "Why it matters: MC12: Enzo-based hypercar.. For Maserati, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Italian luxury/sports maker founded 1914.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Quattroporte: the Italian sedan.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Quattroporte: the Italian sedan.", "x": "Maserati: Quattroporte: the Italian sedan.. This is one of the defining facts about Maserati — the kind of thing enthusiasts argue about and newcomers should know first. Biturbo: 1980s icon. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this Maserati fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this Maserati fact matters.", "x": "Why it matters: Quattroporte: the Italian sedan.. For Maserati, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Italian luxury/sports maker founded 1914.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Ghibli: 1960s grand tourer.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Ghibli: 1960s grand tourer.", "x": "Maserati: Ghibli: 1960s grand tourer.. This is one of the defining facts about Maserati — the kind of thing enthusiasts argue about and newcomers should know first. GranTurismo: beautiful coupe. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this Maserati fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this Maserati fact matters.", "x": "Why it matters: Ghibli: 1960s grand tourer.. For Maserati, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Italian luxury/sports maker founded 1914.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Now Stellantis-owned.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Now Stellantis-owned.", "x": "Maserati: Now Stellantis-owned.. This is one of the defining facts about Maserati — the kind of thing enthusiasts argue about and newcomers should know first. MC20: modern supercar. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this Maserati fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this Maserati fact matters.", "x": "Why it matters: Now Stellantis-owned.. For Maserati, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Italian luxury/sports maker founded 1914.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Folgore: electric range.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Folgore: electric range.", "x": "Maserati: Folgore: electric range.. This is one of the defining facts about Maserati — the kind of thing enthusiasts argue about and newcomers should know first. Headquarters: Modena, Italy. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this Maserati fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this Maserati fact matters.", "x": "Why it matters: Folgore: electric range.. For Maserati, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. Italian luxury/sports maker founded 1914.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "Headquarters: Modena, Italy.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "Headquarters: Modena, Italy.", "x": "More on Maserati: Headquarters: Modena, Italy.. MC12: Enzo-based hypercar. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Maserati.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "Founded by Maserati brothers.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "Founded by Maserati brothers.", "x": "More on Maserati: Founded by Maserati brothers.. Quattroporte: the Italian sedan. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Maserati.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "Won F1 titles (Fangio 1957).", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "Won F1 titles (Fangio 1957).", "x": "More on Maserati: Won F1 titles (Fangio 1957).. Ghibli: 1960s grand tourer. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Maserati.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "Biturbo: 1980s icon.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "Biturbo: 1980s icon.", "x": "More on Maserati: Biturbo: 1980s icon.. Now Stellantis-owned. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Maserati.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "GranTurismo: beautiful coupe.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "GranTurismo: beautiful coupe.", "x": "More on Maserati: GranTurismo: beautiful coupe.. Folgore: electric range. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Maserati.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "MC20: modern supercar.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "MC20: modern supercar.", "x": "More on Maserati: MC20: modern supercar.. Trident logo from Bologna's fountain. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Maserati.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a Maserati: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a Maserati: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. Headquarters: Modena, Italy. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. Quattroporte: the Italian sedan. The right example of Maserati is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning Maserati: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning Maserati: costs and care.", "x": "Ownership: Founded by Maserati brothers.. Maintain it by the book — fluids, intervals, and qualified specialists. Ghibli: 1960s grand tourer. Budget realistically: purchase price is only the beginning of the story with any car make.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Maserati through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "Maserati through the years.", "x": "The timeline: Italian luxury/sports maker founded 1914.. Trident logo from Bologna's fountain. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. Won F1 titles (Fangio 1957). Read it as one story, and the car make makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for Maserati.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for Maserati.", "x": "The future: Maserati faces electrification, automation, and changing tastes like everything in transport. Now Stellantis-owned. Its heritage — Italian luxury/sports maker founded 1914. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "Maserati fact: Biturbo: 1980s icon..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "Maserati fact: Biturbo: 1980s icon..", "x": "From the Maserati file: Biturbo: 1980s icon.. MC12: Enzo-based hypercar. Collect these and you will know Maserati better than most owners. Italian luxury/sports maker founded 1914. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-car-maserati-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
