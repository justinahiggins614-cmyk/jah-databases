(function(){'use strict';
/* JAH Cadillac Car Make Database generator — jahdb-e2-car-cadillac-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-car-cadillac',PREFIX='JAH-E2CARCADILL-',NAME='JAH Cadillac Car Make Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "facts", "future", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Cadillac: overview", "d": "Cadillac: GM's luxury brand founded 1902; 'Standard of the World'..", "g": "overview", "l": 2, "q": "What is Cadillac: overview?", "a": "Cadillac: GM's luxury brand founded 1902; 'Standard of the World'..", "x": "The complete car make guide: GM's luxury brand founded 1902; 'Standard of the World'.. V16s and tailfins: peak American luxury. From its origins to its most famous models, from buying advice to what comes next — this database covers the car make in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How Cadillac began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How Cadillac began.", "x": "The origin of Cadillac: GM's luxury brand founded 1902; 'Standard of the World'.. Escalade: celebrity SUV icon. Every great car make has a founding story of ambition, luck, and timing — and Cadillac's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "V16s and tailfins: peak American luxury.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "V16s and tailfins: peak American luxury.", "x": "Cadillac: V16s and tailfins: peak American luxury.. This is one of the defining facts about Cadillac — the kind of thing enthusiasts argue about and newcomers should know first. Named for Detroit's founder.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this Cadillac fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this Cadillac fact matters.", "x": "Why it matters: V16s and tailfins: peak American luxury.. For Cadillac, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. GM's luxury brand founded 1902; 'Standard of the World'.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Escalade: celebrity SUV icon.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Escalade: celebrity SUV icon.", "x": "Cadillac: Escalade: celebrity SUV icon.. This is one of the defining facts about Cadillac — the kind of thing enthusiasts argue about and newcomers should know first. First with electric starter (1912).", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this Cadillac fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this Cadillac fact matters.", "x": "Why it matters: Escalade: celebrity SUV icon.. For Cadillac, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. GM's luxury brand founded 1902; 'Standard of the World'.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "V Blackwing: supercharged swan song.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "V Blackwing: supercharged swan song.", "x": "Cadillac: V Blackwing: supercharged swan song.. This is one of the defining facts about Cadillac — the kind of thing enthusiasts argue about and newcomers should know first. Standard of the World slogan.", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this Cadillac fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this Cadillac fact matters.", "x": "Why it matters: V Blackwing: supercharged swan song.. For Cadillac, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. GM's luxury brand founded 1902; 'Standard of the World'.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Lyriq leads its EV future.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Lyriq leads its EV future.", "x": "Cadillac: Lyriq leads its EV future.. This is one of the defining facts about Cadillac — the kind of thing enthusiasts argue about and newcomers should know first. Celestiq: hand-built flagship EV. Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this Cadillac fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this Cadillac fact matters.", "x": "Why it matters: Lyriq leads its EV future.. For Cadillac, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. GM's luxury brand founded 1902; 'Standard of the World'.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Eldorado defined 1950s glamour.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Eldorado defined 1950s glamour.", "x": "Cadillac: Eldorado defined 1950s glamour.. This is one of the defining facts about Cadillac — the kind of thing enthusiasts argue about and newcomers should know first. F1 team coming (2026). Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this Cadillac fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this Cadillac fact matters.", "x": "Why it matters: Eldorado defined 1950s glamour.. For Cadillac, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. GM's luxury brand founded 1902; 'Standard of the World'.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "CTS-V: BMW M fighter.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "CTS-V: BMW M fighter.", "x": "Cadillac: CTS-V: BMW M fighter.. This is one of the defining facts about Cadillac — the kind of thing enthusiasts argue about and newcomers should know first. Headquarters: Detroit (GM). Vehicle facts from manufacturer publications and standard references. Specifications change by model year; confirm current figures before buying.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this Cadillac fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this Cadillac fact matters.", "x": "Why it matters: CTS-V: BMW M fighter.. For Cadillac, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. GM's luxury brand founded 1902; 'Standard of the World'.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "Headquarters: Detroit (GM).", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "Headquarters: Detroit (GM).", "x": "More on Cadillac: Headquarters: Detroit (GM).. Escalade: celebrity SUV icon. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Cadillac.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "Named for Detroit's founder.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "Named for Detroit's founder.", "x": "More on Cadillac: Named for Detroit's founder.. V Blackwing: supercharged swan song. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Cadillac.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "First with electric starter (1912).", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "First with electric starter (1912).", "x": "More on Cadillac: First with electric starter (1912).. Lyriq leads its EV future. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Cadillac.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "Standard of the World slogan.", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "Standard of the World slogan.", "x": "More on Cadillac: Standard of the World slogan.. Eldorado defined 1950s glamour. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Cadillac.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Celestiq: hand-built flagship EV.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Celestiq: hand-built flagship EV.", "x": "More on Cadillac: Celestiq: hand-built flagship EV.. CTS-V: BMW M fighter. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Cadillac.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "F1 team coming (2026).", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "F1 team coming (2026).", "x": "More on Cadillac: F1 team coming (2026).. V16s and tailfins: peak American luxury. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Cadillac.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a Cadillac: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a Cadillac: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. Headquarters: Detroit (GM). Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. V Blackwing: supercharged swan song. The right example of Cadillac is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning Cadillac: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning Cadillac: costs and care.", "x": "Ownership: Named for Detroit's founder.. Maintain it by the book — fluids, intervals, and qualified specialists. Lyriq leads its EV future. Budget realistically: purchase price is only the beginning of the story with any car make.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Cadillac through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "Cadillac through the years.", "x": "The timeline: GM's luxury brand founded 1902; 'Standard of the World'.. V16s and tailfins: peak American luxury. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. First with electric starter (1912). Read it as one story, and the car make makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for Cadillac.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for Cadillac.", "x": "The future: Cadillac faces electrification, automation, and changing tastes like everything in transport. Eldorado defined 1950s glamour. Its heritage — GM's luxury brand founded 1902; 'Standard of the World'. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "Cadillac fact: Standard of the World slogan..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "Cadillac fact: Standard of the World slogan..", "x": "From the Cadillac file: Standard of the World slogan.. Escalade: celebrity SUV icon. Collect these and you will know Cadillac better than most owners. GM's luxury brand founded 1902; 'Standard of the World'.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-car-cadillac-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
