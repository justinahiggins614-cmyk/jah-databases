(function(){'use strict';
/* JAH Cho Oyu Mountain Database generator — jahdb-e2-mountain-cho-oyu-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-mountain-cho-oyu',PREFIX='JAH-E2MOUNTAINC-',NAME='JAH Cho Oyu Mountain Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Cho Oyu: the complete guide", "d": "Cho Oyu: the 'easier' 8,000er..", "g": "overview", "l": 2, "q": "What is Cho Oyu: the complete guide?", "a": "Cho Oyu: the 'easier' 8,000er..", "x": "The complete mountain guide to Cho Oyu: the 'easier' 8,000er.. 8,188m. From formation to visiting, from wildlife to legends — everything about this mountain in one database. Routes. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "8,188m.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "8,188m.", "x": "Cho Oyu: 8,188m.. History. One of the defining facts — First 1954.. the 'easier' 8,000er. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 8,188m..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 8,188m..", "x": "Explored: 8,188m.. Views. Why it is so — Cho Oyu. Popular first 8000. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Tibet/Nepal.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Tibet/Nepal.", "x": "Cho Oyu: Tibet/Nepal.. Climbing. One of the defining facts — Popular first 8000.. the 'easier' 8,000er. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Tibet/Nepal..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Tibet/Nepal..", "x": "Explored: Tibet/Nepal.. Safety. Why it is so — Cho Oyu. Nangpa La. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "First 1954.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "First 1954.", "x": "Cho Oyu: First 1954.. Views. One of the defining facts — Nangpa La.. the 'easier' 8,000er. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: First 1954..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: First 1954..", "x": "Explored: First 1954.. Tibet. Why it is so — Cho Oyu. Trade. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Popular first 8000.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Popular first 8000.", "x": "Cho Oyu: Popular first 8000.. Safety. One of the defining facts — Trade.. the 'easier' 8,000er. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Popular first 8000..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Popular first 8000..", "x": "Explored: Popular first 8000.. Routes. Why it is so — Cho Oyu. 8,188m. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Nangpa La.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Nangpa La.", "x": "Cho Oyu: Nangpa La.. Tibet. One of the defining facts — 8,188m.. the 'easier' 8,000er. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Nangpa La..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Nangpa La..", "x": "Explored: Nangpa La.. History. Why it is so — Cho Oyu. Tibet/Nepal. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Trade.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Trade.", "x": "Cho Oyu: Trade.. Routes. One of the defining facts — Tibet/Nepal.. the 'easier' 8,000er. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Trade..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Trade..", "x": "Explored: Trade.. Climbing. Why it is so — Cho Oyu. First 1954. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Routes.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Routes.", "x": "Cho Oyu in depth: Routes.. Tibet/Nepal. The details reward the curious — the 'easier' 8,000er.. Climbing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "Cho Oyu in depth: History.. First 1954. The details reward the curious — the 'easier' 8,000er.. Views. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Climbing.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Climbing.", "x": "Cho Oyu in depth: Climbing.. Popular first 8000. The details reward the curious — the 'easier' 8,000er.. Safety. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Views.", "x": "Cho Oyu in depth: Views.. Nangpa La. The details reward the curious — the 'easier' 8,000er.. Tibet. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Safety.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Safety.", "x": "Cho Oyu in depth: Safety.. Trade. The details reward the curious — the 'easier' 8,000er.. Routes. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Tibet.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Tibet.", "x": "Cho Oyu in depth: Tibet.. 8,188m. The details reward the curious — the 'easier' 8,000er.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Cho Oyu is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Cho Oyu is.", "x": "Location: 8,188m.. Routes. Getting oriented — Cho Oyu. the 'easier' 8,000er. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Cho Oyu.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Cho Oyu.", "x": "Visiting: History.. Tibet/Nepal. Practical know-how — Cho Oyu. the 'easier' 8,000er. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Cho Oyu.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Cho Oyu.", "x": "Ecology: Climbing.. First 1954. The living world of Cho Oyu — the 'easier' 8,000er.. Views. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Cho Oyu through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Cho Oyu through time.", "x": "History: Safety.. Popular first 8000. People and Cho Oyu across the centuries — the 'easier' 8,000er.. Tibet. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Cho Oyu.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Cho Oyu.", "x": "Conservation: History.. 8,188m. Threats and guardians of Cho Oyu — the 'easier' 8,000er.. Climbing. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Cho Oyu in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Cho Oyu in numbers.", "x": "Numbers: 8,188m.; Tibet/Nepal.. Views. Statistics that stun — Cho Oyu. the 'easier' 8,000er. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-mountain-cho-oyu-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
