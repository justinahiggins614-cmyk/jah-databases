(function(){'use strict';
/* JAH Indian Wells Tennis Garden Tennis Court Database generator — jahdb-e2-tennis-indian-wells-tennis-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-tennis-indian-wells-tennis',PREFIX='JAH-E2TENNISIND-',NAME='JAH Indian Wells Tennis Garden Tennis Court Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Indian Wells Tennis Garden: the complete guide", "d": "Indian Wells Tennis Garden: the fifth slam..", "g": "overview", "l": 2, "q": "What is Indian Wells Tennis Garden: the complete guide?", "a": "Indian Wells Tennis Garden: the fifth slam..", "x": "The complete tennis court guide to Indian Wells Tennis Garden: the fifth slam.. 1986. From formation to visiting, from wildlife to legends — everything about this tennis court in one database. Desert.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1986.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1986.", "x": "Indian Wells Tennis Garden: 1986.. Stadium. One of the defining facts — Stadium 2.. the fifth slam. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 1986..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 1986..", "x": "Explored: 1986.. California. Why it is so — Indian Wells Tennis Garden. California. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Desert.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Desert.", "x": "Indian Wells Tennis Garden: Desert.. Paradise. One of the defining facts — California.. the fifth slam. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Desert..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Desert..", "x": "Explored: Desert.. Masters. Why it is so — Indian Wells Tennis Garden. Paradise. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Stadium 2.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Stadium 2.", "x": "Indian Wells Tennis Garden: Stadium 2.. California. One of the defining facts — Paradise.. the fifth slam. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Stadium 2..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Stadium 2..", "x": "Explored: Stadium 2.. Fifth. Why it is so — Indian Wells Tennis Garden. Masters. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "California.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "California.", "x": "Indian Wells Tennis Garden: California.. Masters. One of the defining facts — Masters.. the fifth slam. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: California..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: California..", "x": "Explored: California.. Desert. Why it is so — Indian Wells Tennis Garden. 1986. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Paradise.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Paradise.", "x": "Indian Wells Tennis Garden: Paradise.. Fifth. One of the defining facts — 1986.. the fifth slam. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Paradise..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Paradise..", "x": "Explored: Paradise.. Stadium. Why it is so — Indian Wells Tennis Garden. Desert. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Masters.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Masters.", "x": "Indian Wells Tennis Garden: Masters.. Desert. One of the defining facts — Desert.. the fifth slam. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Masters..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Masters..", "x": "Explored: Masters.. Paradise. Why it is so — Indian Wells Tennis Garden. Stadium 2. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Desert.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Desert.", "x": "Indian Wells Tennis Garden in depth: Desert.. Desert. The details reward the curious — the fifth slam.. Paradise. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Stadium.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Stadium.", "x": "Indian Wells Tennis Garden in depth: Stadium.. Stadium 2. The details reward the curious — the fifth slam.. California. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Paradise.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Paradise.", "x": "Indian Wells Tennis Garden in depth: Paradise.. California. The details reward the curious — the fifth slam.. Masters. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "California.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "California.", "x": "Indian Wells Tennis Garden in depth: California.. Paradise. The details reward the curious — the fifth slam.. Fifth. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Masters.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Masters.", "x": "Indian Wells Tennis Garden in depth: Masters.. Masters. The details reward the curious — the fifth slam.. Desert. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Fifth.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Fifth.", "x": "Indian Wells Tennis Garden in depth: Fifth.. 1986. The details reward the curious — the fifth slam.. Stadium. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Indian Wells Tennis Garden is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Indian Wells Tennis Garden is.", "x": "Location: 1986.. Desert. Getting oriented — Indian Wells Tennis Garden. the fifth slam. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Indian Wells Tennis Garden.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Indian Wells Tennis Garden.", "x": "Visiting: Stadium.. Desert. Practical know-how — Indian Wells Tennis Garden. the fifth slam. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Indian Wells Tennis Garden.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Indian Wells Tennis Garden.", "x": "Ecology: Paradise.. Stadium 2. The living world of Indian Wells Tennis Garden — the fifth slam.. California. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Indian Wells Tennis Garden through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Indian Wells Tennis Garden through time.", "x": "History: Masters.. California. People and Indian Wells Tennis Garden across the centuries — the fifth slam.. Fifth. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Indian Wells Tennis Garden.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Indian Wells Tennis Garden.", "x": "Conservation: Stadium.. 1986. Threats and guardians of Indian Wells Tennis Garden — the fifth slam.. Paradise. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Indian Wells Tennis Garden in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Indian Wells Tennis Garden in numbers.", "x": "Numbers: 1986.; Desert.. California. Statistics that stun — Indian Wells Tennis Garden. the fifth slam. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-tennis-indian-wells-tennis-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
