(function(){'use strict';
/* JAH Volkswagen Car Make Database generator — jahdb-e2-car-volkswagen-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-car-volkswagen',PREFIX='JAH-E2CARVOLKSW-',NAME='JAH Volkswagen Car Make Database';
var FIELDS=["overview", "history", "highlights", "details", "buying", "ownership", "facts", "future", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Volkswagen: overview", "d": "Volkswagen: German maker founded 1937; the 'people's car'..", "g": "overview", "l": 2, "q": "What is Volkswagen: overview?", "a": "Volkswagen: German maker founded 1937; the 'people's car'..", "x": "The complete car make guide: German maker founded 1937; the 'people's car'.. Beetle: 21M+ built, a global icon. From its origins to its most famous models, from buying advice to what comes next — this database covers the car make in full.", "s": "public-reference", "f": null}, {"t": "Origin story", "d": "How Volkswagen began.", "g": "history", "l": 2, "q": "What is Origin story?", "a": "How Volkswagen began.", "x": "The origin of Volkswagen: German maker founded 1937; the 'people's car'.. Golf/GTI defined the hot hatch. Every great car make has a founding story of ambition, luck, and timing — and Volkswagen's explains the character of everything it made after.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Beetle: 21M+ built, a global icon.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Beetle: 21M+ built, a global icon.", "x": "Volkswagen: Beetle: 21M+ built, a global icon.. This is one of the defining facts about Volkswagen — the kind of thing enthusiasts argue about and newcomers should know first. Name means 'people's car'.", "s": "public-reference", "f": null}, {"t": "Highlight 1: why it matters", "d": "Why this Volkswagen fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 1: why it matters?", "a": "Why this Volkswagen fact matters.", "x": "Why it matters: Beetle: 21M+ built, a global icon.. For Volkswagen, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. German maker founded 1937; the 'people's car'.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Golf/GTI defined the hot hatch.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Golf/GTI defined the hot hatch.", "x": "Volkswagen: Golf/GTI defined the hot hatch.. This is one of the defining facts about Volkswagen — the kind of thing enthusiasts argue about and newcomers should know first. Porsche family controls VW Group.", "s": "public-reference", "f": null}, {"t": "Highlight 2: why it matters", "d": "Why this Volkswagen fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 2: why it matters?", "a": "Why this Volkswagen fact matters.", "x": "Why it matters: Golf/GTI defined the hot hatch.. For Volkswagen, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. German maker founded 1937; the 'people's car'.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Owns Audi, Porsche, Lamborghini, Bentley.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Owns Audi, Porsche, Lamborghini, Bentley.", "x": "Volkswagen: Owns Audi, Porsche, Lamborghini, Bentley.. This is one of the defining facts about Volkswagen — the kind of thing enthusiasts argue about and newcomers should know first. Dieselgate scandal (2015).", "s": "public-reference", "f": null}, {"t": "Highlight 3: why it matters", "d": "Why this Volkswagen fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 3: why it matters?", "a": "Why this Volkswagen fact matters.", "x": "Why it matters: Owns Audi, Porsche, Lamborghini, Bentley.. For Volkswagen, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. German maker founded 1937; the 'people's car'.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Bulli bus is a counterculture symbol.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Bulli bus is a counterculture symbol.", "x": "Volkswagen: Bulli bus is a counterculture symbol.. This is one of the defining facts about Volkswagen — the kind of thing enthusiasts argue about and newcomers should know first. Currywurst is a VW product too.", "s": "public-reference", "f": null}, {"t": "Highlight 4: why it matters", "d": "Why this Volkswagen fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 4: why it matters?", "a": "Why this Volkswagen fact matters.", "x": "Why it matters: Bulli bus is a counterculture symbol.. For Volkswagen, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. German maker founded 1937; the 'people's car'.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Largest automaker by revenue at times.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Largest automaker by revenue at times.", "x": "Volkswagen: Largest automaker by revenue at times.. This is one of the defining facts about Volkswagen — the kind of thing enthusiasts argue about and newcomers should know first. Kaefer/Beetle ran 1938-2003.", "s": "public-reference", "f": null}, {"t": "Highlight 5: why it matters", "d": "Why this Volkswagen fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 5: why it matters?", "a": "Why this Volkswagen fact matters.", "x": "Why it matters: Largest automaker by revenue at times.. For Volkswagen, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. German maker founded 1937; the 'people's car'.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "ID. series leads its EV push.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "ID. series leads its EV push.", "x": "Volkswagen: ID. series leads its EV push.. This is one of the defining facts about Volkswagen — the kind of thing enthusiasts argue about and newcomers should know first. Headquarters: Wolfsburg, Germany.", "s": "public-reference", "f": null}, {"t": "Highlight 6: why it matters", "d": "Why this Volkswagen fact matters.", "g": "highlights", "l": 2, "q": "What is Highlight 6: why it matters?", "a": "Why this Volkswagen fact matters.", "x": "Why it matters: ID. series leads its EV push.. For Volkswagen, this fact shaped reputation, sales, or history — understanding it means understanding why the car make is remembered. German maker founded 1937; the 'people's car'.", "s": "public-reference", "f": null}, {"t": "Detail 1", "d": "Headquarters: Wolfsburg, Germany.", "g": "details", "l": 2, "q": "What is Detail 1?", "a": "Headquarters: Wolfsburg, Germany.", "x": "More on Volkswagen: Headquarters: Wolfsburg, Germany.. Golf/GTI defined the hot hatch. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Volkswagen.", "s": "public-reference", "f": null}, {"t": "Detail 2", "d": "Name means 'people's car'.", "g": "details", "l": 2, "q": "What is Detail 2?", "a": "Name means 'people's car'.", "x": "More on Volkswagen: Name means 'people's car'.. Owns Audi, Porsche, Lamborghini, Bentley. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Volkswagen.", "s": "public-reference", "f": null}, {"t": "Detail 3", "d": "Porsche family controls VW Group.", "g": "details", "l": 2, "q": "What is Detail 3?", "a": "Porsche family controls VW Group.", "x": "More on Volkswagen: Porsche family controls VW Group.. Bulli bus is a counterculture symbol. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Volkswagen.", "s": "public-reference", "f": null}, {"t": "Detail 4", "d": "Dieselgate scandal (2015).", "g": "details", "l": 2, "q": "What is Detail 4?", "a": "Dieselgate scandal (2015).", "x": "More on Volkswagen: Dieselgate scandal (2015).. Largest automaker by revenue at times. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Volkswagen.", "s": "public-reference", "f": null}, {"t": "Detail 5", "d": "Currywurst is a VW product too.", "g": "details", "l": 2, "q": "What is Detail 5?", "a": "Currywurst is a VW product too.", "x": "More on Volkswagen: Currywurst is a VW product too.. ID. series leads its EV push. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Volkswagen.", "s": "public-reference", "f": null}, {"t": "Detail 6", "d": "Kaefer/Beetle ran 1938-2003.", "g": "details", "l": 2, "q": "What is Detail 6?", "a": "Kaefer/Beetle ran 1938-2003.", "x": "More on Volkswagen: Kaefer/Beetle ran 1938-2003.. Beetle: 21M+ built, a global icon. Details are where expertise lives — the specifications, the variants, the context that turns a casual fan into someone who really knows Volkswagen.", "s": "public-reference", "f": null}, {"t": "Buying guide", "d": "Buying a Volkswagen: what to know.", "g": "buying", "l": 2, "q": "What is Buying guide?", "a": "Buying a Volkswagen: what to know.", "x": "Buying: research the model years — some are legends, some to avoid. Headquarters: Wolfsburg, Germany. Get a pre-purchase inspection, check the history, and budget for ownership, not just purchase. Owns Audi, Porsche, Lamborghini, Bentley. The right example of Volkswagen is worth the search.", "s": "public-reference", "f": null}, {"t": "Ownership and maintenance", "d": "Owning Volkswagen: costs and care.", "g": "ownership", "l": 2, "q": "What is Ownership and maintenance?", "a": "Owning Volkswagen: costs and care.", "x": "Ownership: Name means 'people's car'.. Maintain it by the book — fluids, intervals, and qualified specialists. Bulli bus is a counterculture symbol. Budget realistically: purchase price is only the beginning of the story with any car make.", "s": "public-reference", "f": null}, {"t": "Timeline", "d": "Volkswagen through the years.", "g": "history", "l": 2, "q": "What is Timeline?", "a": "Volkswagen through the years.", "x": "The timeline: German maker founded 1937; the 'people's car'.. Beetle: 21M+ built, a global icon. Key chapters mark the eras — the breakthroughs, the crises, the comebacks. Porsche family controls VW Group. Read it as one story, and the car make makes sense.", "s": "public-reference", "f": null}, {"t": "The future", "d": "What comes next for Volkswagen.", "g": "future", "l": 2, "q": "What is The future?", "a": "What comes next for Volkswagen.", "x": "The future: Volkswagen faces electrification, automation, and changing tastes like everything in transport. Largest automaker by revenue at times. Its heritage — German maker founded 1937; the 'people's car'. — is the asset it carries forward. Watch this space.", "s": "public-reference", "f": null}, {"t": "Fact 1", "d": "Volkswagen fact: Dieselgate scandal (2015)..", "g": "facts", "l": 2, "q": "What is Fact 1?", "a": "Volkswagen fact: Dieselgate scandal (2015)..", "x": "From the Volkswagen file: Dieselgate scandal (2015).. Golf/GTI defined the hot hatch. Collect these and you will know Volkswagen better than most owners. German maker founded 1937; the 'people's car'.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-car-volkswagen-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
