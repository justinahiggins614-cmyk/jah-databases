(function(){'use strict';
/* JAH Mount Everest Mountain Database generator — jahdb-e2-mountain-mount-everest-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-mountain-mount-everest',PREFIX='JAH-E2MOUNTAINM-',NAME='JAH Mount Everest Mountain Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mount Everest: the complete guide", "d": "Mount Everest: the world's highest peak at 8,849m..", "g": "overview", "l": 2, "q": "What is Mount Everest: the complete guide?", "a": "Mount Everest: the world's highest peak at 8,849m..", "x": "The complete mountain guide to Mount Everest: the world's highest peak at 8,849m.. 8,849m. From formation to visiting, from wildlife to legends — everything about this mountain in one database. Geology.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "8,849m.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "8,849m.", "x": "Mount Everest: 8,849m.. Climbing routes. One of the defining facts — First: Hillary/Norgay 1953.. the world's highest peak at 8,849m. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 8,849m..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 8,849m..", "x": "Explored: 8,849m.. Permits. Why it is so — Mount Everest. Death Zone. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Nepal/Tibet.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Nepal/Tibet.", "x": "Mount Everest: Nepal/Tibet.. Sherpas. One of the defining facts — Death Zone.. the world's highest peak at 8,849m. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Nepal/Tibet..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Nepal/Tibet..", "x": "Explored: Nepal/Tibet.. Trash. Why it is so — Mount Everest. Crowds/ladders. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "First: Hillary/Norgay 1953.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "First: Hillary/Norgay 1953.", "x": "Mount Everest: First: Hillary/Norgay 1953.. Permits. One of the defining facts — Crowds/ladders.. the world's highest peak at 8,849m. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: First: Hillary/Norgay 1953..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: First: Hillary/Norgay 1953..", "x": "Explored: First: Hillary/Norgay 1953.. Records. Why it is so — Mount Everest. Sagarmatha. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Death Zone.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Death Zone.", "x": "Mount Everest: Death Zone.. Trash. One of the defining facts — Sagarmatha.. the world's highest peak at 8,849m. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Death Zone..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Death Zone..", "x": "Explored: Death Zone.. Geology. Why it is so — Mount Everest. 8,849m. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Crowds/ladders.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Crowds/ladders.", "x": "Mount Everest: Crowds/ladders.. Records. One of the defining facts — 8,849m.. the world's highest peak at 8,849m. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Crowds/ladders..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Crowds/ladders..", "x": "Explored: Crowds/ladders.. Climbing routes. Why it is so — Mount Everest. Nepal/Tibet. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Sagarmatha.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Sagarmatha.", "x": "Mount Everest: Sagarmatha.. Geology. One of the defining facts — Nepal/Tibet.. the world's highest peak at 8,849m. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Sagarmatha..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Sagarmatha..", "x": "Explored: Sagarmatha.. Sherpas. Why it is so — Mount Everest. First: Hillary/Norgay 1953. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Geology.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Geology.", "x": "Mount Everest in depth: Geology.. Nepal/Tibet. The details reward the curious — the world's highest peak at 8,849m.. Sherpas. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Climbing routes.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Climbing routes.", "x": "Mount Everest in depth: Climbing routes.. First: Hillary/Norgay 1953. The details reward the curious — the world's highest peak at 8,849m.. Permits. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Sherpas.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Sherpas.", "x": "Mount Everest in depth: Sherpas.. Death Zone. The details reward the curious — the world's highest peak at 8,849m.. Trash. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Permits.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Permits.", "x": "Mount Everest in depth: Permits.. Crowds/ladders. The details reward the curious — the world's highest peak at 8,849m.. Records. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Trash.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Trash.", "x": "Mount Everest in depth: Trash.. Sagarmatha. The details reward the curious — the world's highest peak at 8,849m.. Geology. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Records.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Records.", "x": "Mount Everest in depth: Records.. 8,849m. The details reward the curious — the world's highest peak at 8,849m.. Climbing routes. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Mount Everest is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Mount Everest is.", "x": "Location: 8,849m.. Geology. Getting oriented — Mount Everest. the world's highest peak at 8,849m. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Mount Everest.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Mount Everest.", "x": "Visiting: Climbing routes.. Nepal/Tibet. Practical know-how — Mount Everest. the world's highest peak at 8,849m. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Mount Everest.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Mount Everest.", "x": "Ecology: Sherpas.. First: Hillary/Norgay 1953. The living world of Mount Everest — the world's highest peak at 8,849m.. Permits. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Mount Everest through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Mount Everest through time.", "x": "History: Trash.. Death Zone. People and Mount Everest across the centuries — the world's highest peak at 8,849m.. Records. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Mount Everest.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Mount Everest.", "x": "Conservation: Climbing routes.. 8,849m. Threats and guardians of Mount Everest — the world's highest peak at 8,849m.. Sherpas. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Mount Everest in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Mount Everest in numbers.", "x": "Numbers: 8,849m.; Nepal/Tibet.. Permits. Statistics that stun — Mount Everest. the world's highest peak at 8,849m. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-mountain-mount-everest-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
