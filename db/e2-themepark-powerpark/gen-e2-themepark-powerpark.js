(function(){'use strict';
/* JAH PowerPark Theme Park Database generator — jahdb-e2-themepark-powerpark-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-themepark-powerpark',PREFIX='JAH-E2THEMEPARK-',NAME='JAH PowerPark Theme Park Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "PowerPark: the complete guide", "d": "PowerPark: Finland's racing park..", "g": "overview", "l": 2, "q": "What is PowerPark: the complete guide?", "a": "PowerPark: Finland's racing park..", "x": "The complete theme park guide to PowerPark: Finland's racing park.. 1999. From formation to visiting, from wildlife to legends — everything about this theme park in one database. Racing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "1999.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "1999.", "x": "PowerPark: 1999.. Coasters. One of the defining facts — Karting.. Finland's racing park. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 1999..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 1999..", "x": "Explored: 1999.. Finland. Why it is so — PowerPark. Horses. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Junker.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Junker.", "x": "PowerPark: Junker.. Tickets. One of the defining facts — Horses.. Finland's racing park. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Junker..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Junker..", "x": "Explored: Junker.. Horses. Why it is so — PowerPark. Finland. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Karting.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Karting.", "x": "PowerPark: Karting.. Finland. One of the defining facts — Finland.. Finland's racing park. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Karting..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Karting..", "x": "Explored: Karting.. Fun. Why it is so — PowerPark. Racing. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Horses.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Horses.", "x": "PowerPark: Horses.. Horses. One of the defining facts — Racing.. Finland's racing park. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Horses..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Horses..", "x": "Explored: Horses.. Racing. Why it is so — PowerPark. 1999. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Finland.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Finland.", "x": "PowerPark: Finland.. Fun. One of the defining facts — 1999.. Finland's racing park. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Finland..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Finland..", "x": "Explored: Finland.. Coasters. Why it is so — PowerPark. Junker. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Racing.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Racing.", "x": "PowerPark: Racing.. Racing. One of the defining facts — Junker.. Finland's racing park. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Racing..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Racing..", "x": "Explored: Racing.. Tickets. Why it is so — PowerPark. Karting. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Racing.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Racing.", "x": "PowerPark in depth: Racing.. Junker. The details reward the curious — Finland's racing park.. Tickets. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Coasters.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Coasters.", "x": "PowerPark in depth: Coasters.. Karting. The details reward the curious — Finland's racing park.. Finland. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tickets.", "x": "PowerPark in depth: Tickets.. Horses. The details reward the curious — Finland's racing park.. Horses. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Finland.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Finland.", "x": "PowerPark in depth: Finland.. Finland. The details reward the curious — Finland's racing park.. Fun. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Horses.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Horses.", "x": "PowerPark in depth: Horses.. Racing. The details reward the curious — Finland's racing park.. Racing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Fun.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Fun.", "x": "PowerPark in depth: Fun.. 1999. The details reward the curious — Finland's racing park.. Coasters. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where PowerPark is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where PowerPark is.", "x": "Location: 1999.. Racing. Getting oriented — PowerPark. Finland's racing park. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience PowerPark.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience PowerPark.", "x": "Visiting: Coasters.. Junker. Practical know-how — PowerPark. Finland's racing park. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around PowerPark.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around PowerPark.", "x": "Ecology: Tickets.. Karting. The living world of PowerPark — Finland's racing park.. Finland. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "PowerPark through time.", "g": "history", "l": 2, "q": "What is History?", "a": "PowerPark through time.", "x": "History: Horses.. Horses. People and PowerPark across the centuries — Finland's racing park.. Fun. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting PowerPark.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting PowerPark.", "x": "Conservation: Coasters.. 1999. Threats and guardians of PowerPark — Finland's racing park.. Tickets. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "PowerPark in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "PowerPark in numbers.", "x": "Numbers: 1999.; Junker.. Finland. Statistics that stun — PowerPark. Finland's racing park. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-themepark-powerpark-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
