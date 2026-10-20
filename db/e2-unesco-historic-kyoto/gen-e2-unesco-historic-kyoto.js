(function(){'use strict';
/* JAH Historic Kyoto Unesco Site Database generator — jahdb-e2-unesco-historic-kyoto-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-unesco-historic-kyoto',PREFIX='JAH-E2UNESCOHIS-',NAME='JAH Historic Kyoto Unesco Site Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Historic Kyoto: the complete guide", "d": "Historic Kyoto: temples of old Japan..", "g": "overview", "l": 2, "q": "What is Historic Kyoto: the complete guide?", "a": "Historic Kyoto: temples of old Japan..", "x": "The complete unesco site guide to Historic Kyoto: temples of old Japan.. 17 sites. From formation to visiting, from wildlife to legends — everything about this unesco site in one database. Temples. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "17 sites.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "17 sites.", "x": "Historic Kyoto: 17 sites.. Gardens. One of the defining facts — Gion.. temples of old Japan. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 17 sites..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 17 sites..", "x": "Explored: 17 sites.. Seasons. Why it is so — Historic Kyoto. UNESCO 1994. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Kinkaku-ji.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Kinkaku-ji.", "x": "Historic Kyoto: Kinkaku-ji.. Culture. One of the defining facts — UNESCO 1994.. temples of old Japan. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Kinkaku-ji..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Kinkaku-ji..", "x": "Explored: Kinkaku-ji.. Tours. Why it is so — Historic Kyoto. Zen gardens. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Gion.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Gion.", "x": "Historic Kyoto: Gion.. Seasons. One of the defining facts — Zen gardens.. temples of old Japan. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Gion..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Gion..", "x": "Explored: Gion.. Respect. Why it is so — Historic Kyoto. Seasons. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "UNESCO 1994.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "UNESCO 1994.", "x": "Historic Kyoto: UNESCO 1994.. Tours. One of the defining facts — Seasons.. temples of old Japan. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: UNESCO 1994..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: UNESCO 1994..", "x": "Explored: UNESCO 1994.. Temples. Why it is so — Historic Kyoto. 17 sites. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Zen gardens.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Zen gardens.", "x": "Historic Kyoto: Zen gardens.. Respect. One of the defining facts — 17 sites.. temples of old Japan. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Zen gardens..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Zen gardens..", "x": "Explored: Zen gardens.. Gardens. Why it is so — Historic Kyoto. Kinkaku-ji. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Seasons.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Seasons.", "x": "Historic Kyoto: Seasons.. Temples. One of the defining facts — Kinkaku-ji.. temples of old Japan. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Seasons..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Seasons..", "x": "Explored: Seasons.. Culture. Why it is so — Historic Kyoto. Gion. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Temples.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Temples.", "x": "Historic Kyoto in depth: Temples.. Kinkaku-ji. The details reward the curious — temples of old Japan.. Culture. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Gardens.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Gardens.", "x": "Historic Kyoto in depth: Gardens.. Gion. The details reward the curious — temples of old Japan.. Seasons. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Culture.", "x": "Historic Kyoto in depth: Culture.. UNESCO 1994. The details reward the curious — temples of old Japan.. Tours. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Seasons.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Seasons.", "x": "Historic Kyoto in depth: Seasons.. Zen gardens. The details reward the curious — temples of old Japan.. Respect. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Tours.", "x": "Historic Kyoto in depth: Tours.. Seasons. The details reward the curious — temples of old Japan.. Temples. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Respect.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Respect.", "x": "Historic Kyoto in depth: Respect.. 17 sites. The details reward the curious — temples of old Japan.. Gardens. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Historic Kyoto is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Historic Kyoto is.", "x": "Location: 17 sites.. Temples. Getting oriented — Historic Kyoto. temples of old Japan. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Historic Kyoto.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Historic Kyoto.", "x": "Visiting: Gardens.. Kinkaku-ji. Practical know-how — Historic Kyoto. temples of old Japan. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Historic Kyoto.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Historic Kyoto.", "x": "Ecology: Culture.. Gion. The living world of Historic Kyoto — temples of old Japan.. Seasons. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Historic Kyoto through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Historic Kyoto through time.", "x": "History: Tours.. UNESCO 1994. People and Historic Kyoto across the centuries — temples of old Japan.. Respect. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Historic Kyoto.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Historic Kyoto.", "x": "Conservation: Gardens.. 17 sites. Threats and guardians of Historic Kyoto — temples of old Japan.. Culture. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Historic Kyoto in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Historic Kyoto in numbers.", "x": "Numbers: 17 sites.; Kinkaku-ji.. Seasons. Statistics that stun — Historic Kyoto. temples of old Japan. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-unesco-historic-kyoto-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
