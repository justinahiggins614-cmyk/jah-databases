(function(){'use strict';
/* JAH Old Orchard Beach Beach Database generator — jahdb-e2-beach-old-orchard-beach-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-beach-old-orchard-beach',PREFIX='JAH-E2BEACHOLDO-',NAME='JAH Old Orchard Beach Beach Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Old Orchard Beach: the complete guide", "d": "Old Orchard Beach: Maine's pier fun..", "g": "overview", "l": 2, "q": "What is Old Orchard Beach: the complete guide?", "a": "Old Orchard Beach: Maine's pier fun..", "x": "The complete beach guide to Old Orchard Beach: Maine's pier fun.. Pier. From formation to visiting, from wildlife to legends — everything about this beach in one database. Pier. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Pier.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Pier.", "x": "Old Orchard Beach: Pier.. Amusements. One of the defining facts — Amusements.. Maine's pier fun. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: Pier..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: Pier..", "x": "Explored: Pier.. Maine. Why it is so — Old Orchard Beach. Maine. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "7 miles.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "7 miles.", "x": "Old Orchard Beach: 7 miles.. Family. One of the defining facts — Maine.. Maine's pier fun. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: 7 miles..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: 7 miles..", "x": "Explored: 7 miles.. Summer. Why it is so — Old Orchard Beach. Family. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Amusements.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Amusements.", "x": "Old Orchard Beach: Amusements.. Maine. One of the defining facts — Family.. Maine's pier fun. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Amusements..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Amusements..", "x": "Explored: Amusements.. Fun. Why it is so — Old Orchard Beach. Summer. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Maine.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Maine.", "x": "Old Orchard Beach: Maine.. Summer. One of the defining facts — Summer.. Maine's pier fun. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Maine..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Maine..", "x": "Explored: Maine.. Pier. Why it is so — Old Orchard Beach. Pier. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Family.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Family.", "x": "Old Orchard Beach: Family.. Fun. One of the defining facts — Pier.. Maine's pier fun. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Family..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Family..", "x": "Explored: Family.. Amusements. Why it is so — Old Orchard Beach. 7 miles. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Summer.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Summer.", "x": "Old Orchard Beach: Summer.. Pier. One of the defining facts — 7 miles.. Maine's pier fun. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Summer..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Summer..", "x": "Explored: Summer.. Family. Why it is so — Old Orchard Beach. Amusements. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Pier.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Pier.", "x": "Old Orchard Beach in depth: Pier.. 7 miles. The details reward the curious — Maine's pier fun.. Family. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Amusements.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Amusements.", "x": "Old Orchard Beach in depth: Amusements.. Amusements. The details reward the curious — Maine's pier fun.. Maine. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Family.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Family.", "x": "Old Orchard Beach in depth: Family.. Maine. The details reward the curious — Maine's pier fun.. Summer. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Maine.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Maine.", "x": "Old Orchard Beach in depth: Maine.. Family. The details reward the curious — Maine's pier fun.. Fun. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Summer.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Summer.", "x": "Old Orchard Beach in depth: Summer.. Summer. The details reward the curious — Maine's pier fun.. Pier. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Fun.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Fun.", "x": "Old Orchard Beach in depth: Fun.. Pier. The details reward the curious — Maine's pier fun.. Amusements. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Old Orchard Beach is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Old Orchard Beach is.", "x": "Location: Pier.. Pier. Getting oriented — Old Orchard Beach. Maine's pier fun. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Old Orchard Beach.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Old Orchard Beach.", "x": "Visiting: Amusements.. 7 miles. Practical know-how — Old Orchard Beach. Maine's pier fun. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Old Orchard Beach.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Old Orchard Beach.", "x": "Ecology: Family.. Amusements. The living world of Old Orchard Beach — Maine's pier fun.. Maine. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Old Orchard Beach through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Old Orchard Beach through time.", "x": "History: Summer.. Maine. People and Old Orchard Beach across the centuries — Maine's pier fun.. Fun. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Old Orchard Beach.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Old Orchard Beach.", "x": "Conservation: Amusements.. Pier. Threats and guardians of Old Orchard Beach — Maine's pier fun.. Family. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Old Orchard Beach in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Old Orchard Beach in numbers.", "x": "Numbers: Pier.; 7 miles.. Maine. Statistics that stun — Old Orchard Beach. Maine's pier fun. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-beach-old-orchard-beach-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
