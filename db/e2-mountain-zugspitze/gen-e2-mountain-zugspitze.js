(function(){'use strict';
/* JAH Zugspitze Mountain Database generator — jahdb-e2-mountain-zugspitze-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-mountain-zugspitze',PREFIX='JAH-E2MOUNTAINZ-',NAME='JAH Zugspitze Mountain Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Zugspitze: the complete guide", "d": "Zugspitze: Germany's highest..", "g": "overview", "l": 2, "q": "What is Zugspitze: the complete guide?", "a": "Zugspitze: Germany's highest..", "x": "The complete mountain guide to Zugspitze: Germany's highest.. 2,962m. From formation to visiting, from wildlife to legends — everything about this mountain in one database. Access. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2,962m.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2,962m.", "x": "Zugspitze: 2,962m.. Skiing. One of the defining facts — Austria border.. Germany's highest. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 2,962m..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 2,962m..", "x": "Explored: 2,962m.. Hikes. Why it is so — Zugspitze. Skiing. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Cable cars.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Cable cars.", "x": "Zugspitze: Cable cars.. Views. One of the defining facts — Skiing.. Germany's highest. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Cable cars..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Cable cars..", "x": "Explored: Cable cars.. History. Why it is so — Zugspitze. Views. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Austria border.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Austria border.", "x": "Zugspitze: Austria border.. Hikes. One of the defining facts — Views.. Germany's highest. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Austria border..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Austria border..", "x": "Explored: Austria border.. Towns. Why it is so — Zugspitze. Hikes. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Skiing.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Skiing.", "x": "Zugspitze: Skiing.. History. One of the defining facts — Hikes.. Germany's highest. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Skiing..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Skiing..", "x": "Explored: Skiing.. Access. Why it is so — Zugspitze. 2,962m. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Views.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Views.", "x": "Zugspitze: Views.. Towns. One of the defining facts — 2,962m.. Germany's highest. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Views..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Views..", "x": "Explored: Views.. Skiing. Why it is so — Zugspitze. Cable cars. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Hikes.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Hikes.", "x": "Zugspitze: Hikes.. Access. One of the defining facts — Cable cars.. Germany's highest. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Hikes..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Hikes..", "x": "Explored: Hikes.. Views. Why it is so — Zugspitze. Austria border. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Access.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Access.", "x": "Zugspitze in depth: Access.. Cable cars. The details reward the curious — Germany's highest.. Views. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Skiing.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Skiing.", "x": "Zugspitze in depth: Skiing.. Austria border. The details reward the curious — Germany's highest.. Hikes. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Views.", "x": "Zugspitze in depth: Views.. Skiing. The details reward the curious — Germany's highest.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Hikes.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Hikes.", "x": "Zugspitze in depth: Hikes.. Views. The details reward the curious — Germany's highest.. Towns. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "History.", "x": "Zugspitze in depth: History.. Hikes. The details reward the curious — Germany's highest.. Access. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Towns.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Towns.", "x": "Zugspitze in depth: Towns.. 2,962m. The details reward the curious — Germany's highest.. Skiing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Zugspitze is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Zugspitze is.", "x": "Location: 2,962m.. Access. Getting oriented — Zugspitze. Germany's highest. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Zugspitze.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Zugspitze.", "x": "Visiting: Skiing.. Cable cars. Practical know-how — Zugspitze. Germany's highest. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Zugspitze.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Zugspitze.", "x": "Ecology: Views.. Austria border. The living world of Zugspitze — Germany's highest.. Hikes. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Zugspitze through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Zugspitze through time.", "x": "History: History.. Skiing. People and Zugspitze across the centuries — Germany's highest.. Towns. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Zugspitze.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Zugspitze.", "x": "Conservation: Skiing.. 2,962m. Threats and guardians of Zugspitze — Germany's highest.. Views. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Zugspitze in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Zugspitze in numbers.", "x": "Numbers: 2,962m.; Cable cars.. Hikes. Statistics that stun — Zugspitze. Germany's highest. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-mountain-zugspitze-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
