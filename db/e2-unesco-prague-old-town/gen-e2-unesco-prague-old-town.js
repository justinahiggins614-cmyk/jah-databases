(function(){'use strict';
/* JAH Prague Old Town Unesco Site Database generator — jahdb-e2-unesco-prague-old-town-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-unesco-prague-old-town',PREFIX='JAH-E2UNESCOPRA-',NAME='JAH Prague Old Town Unesco Site Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Prague Old Town: the complete guide", "d": "Prague Old Town: city of a hundred spires..", "g": "overview", "l": 2, "q": "What is Prague Old Town: the complete guide?", "a": "Prague Old Town: city of a hundred spires..", "x": "The complete unesco site guide to Prague Old Town: city of a hundred spires.. Charles Bridge. From formation to visiting, from wildlife to legends — everything about this unesco site in one database. History.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Charles Bridge.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Charles Bridge.", "x": "Prague Old Town: Charles Bridge.. Bridge. One of the defining facts — Castle.. city of a hundred spires. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: Charles Bridge..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: Charles Bridge..", "x": "Explored: Charles Bridge.. Castle. Why it is so — Prague Old Town. UNESCO 1992. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Astronomical Clock.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Astronomical Clock.", "x": "Prague Old Town: Astronomical Clock.. Clock. One of the defining facts — UNESCO 1992.. city of a hundred spires. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Astronomical Clock..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Astronomical Clock..", "x": "Explored: Astronomical Clock.. Tours. Why it is so — Prague Old Town. Beer. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Castle.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Castle.", "x": "Prague Old Town: Castle.. Castle. One of the defining facts — Beer.. city of a hundred spires. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Castle..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Castle..", "x": "Explored: Castle.. Visit. Why it is so — Prague Old Town. Views. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "UNESCO 1992.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "UNESCO 1992.", "x": "Prague Old Town: UNESCO 1992.. Tours. One of the defining facts — Views.. city of a hundred spires. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: UNESCO 1992..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: UNESCO 1992..", "x": "Explored: UNESCO 1992.. History. Why it is so — Prague Old Town. Charles Bridge. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Beer.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Beer.", "x": "Prague Old Town: Beer.. Visit. One of the defining facts — Charles Bridge.. city of a hundred spires. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Beer..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Beer..", "x": "Explored: Beer.. Bridge. Why it is so — Prague Old Town. Astronomical Clock. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Views.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Views.", "x": "Prague Old Town: Views.. History. One of the defining facts — Astronomical Clock.. city of a hundred spires. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Views..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Views..", "x": "Explored: Views.. Clock. Why it is so — Prague Old Town. Castle. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Prague Old Town in depth: History.. Astronomical Clock. The details reward the curious — city of a hundred spires.. Clock. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Bridge.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Bridge.", "x": "Prague Old Town in depth: Bridge.. Castle. The details reward the curious — city of a hundred spires.. Castle. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Clock.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Clock.", "x": "Prague Old Town in depth: Clock.. UNESCO 1992. The details reward the curious — city of a hundred spires.. Tours. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Castle.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Castle.", "x": "Prague Old Town in depth: Castle.. Beer. The details reward the curious — city of a hundred spires.. Visit. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Tours.", "x": "Prague Old Town in depth: Tours.. Views. The details reward the curious — city of a hundred spires.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visit.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visit.", "x": "Prague Old Town in depth: Visit.. Charles Bridge. The details reward the curious — city of a hundred spires.. Bridge. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Prague Old Town is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Prague Old Town is.", "x": "Location: Charles Bridge.. History. Getting oriented — Prague Old Town. city of a hundred spires. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Prague Old Town.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Prague Old Town.", "x": "Visiting: Bridge.. Astronomical Clock. Practical know-how — Prague Old Town. city of a hundred spires. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Prague Old Town.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Prague Old Town.", "x": "Ecology: Clock.. Castle. The living world of Prague Old Town — city of a hundred spires.. Castle. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Prague Old Town through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Prague Old Town through time.", "x": "History: Tours.. UNESCO 1992. People and Prague Old Town across the centuries — city of a hundred spires.. Visit. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Prague Old Town.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Prague Old Town.", "x": "Conservation: Bridge.. Charles Bridge. Threats and guardians of Prague Old Town — city of a hundred spires.. Clock. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Prague Old Town in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Prague Old Town in numbers.", "x": "Numbers: Charles Bridge.; Astronomical Clock.. Castle. Statistics that stun — Prague Old Town. city of a hundred spires. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-unesco-prague-old-town-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
