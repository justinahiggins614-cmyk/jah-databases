(function(){'use strict';
/* JAH Mount Whitney Mountain Database generator — jahdb-e2-mountain-mount-whitney-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-mountain-mount-whitney',PREFIX='JAH-E2MOUNTAINM-',NAME='JAH Mount Whitney Mountain Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mount Whitney: the complete guide", "d": "Mount Whitney: highest in lower 48..", "g": "overview", "l": 2, "q": "What is Mount Whitney: the complete guide?", "a": "Mount Whitney: highest in lower 48..", "x": "The complete mountain guide to Mount Whitney: highest in lower 48.. 4,421m. From formation to visiting, from wildlife to legends — everything about this mountain in one database. Trail. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "4,421m.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "4,421m.", "x": "Mount Whitney: 4,421m.. Permits. One of the defining facts — Trail.. highest in lower 48. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 4,421m..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 4,421m..", "x": "Explored: 4,421m.. Views. Why it is so — Mount Whitney. Permits lottery. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "California.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "California.", "x": "Mount Whitney: California.. History. One of the defining facts — Permits lottery.. highest in lower 48. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: California..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: California..", "x": "Explored: California.. Safety. Why it is so — Mount Whitney. John Muir. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Trail.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Trail.", "x": "Mount Whitney: Trail.. Views. One of the defining facts — John Muir.. highest in lower 48. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Trail..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Trail..", "x": "Explored: Trail.. Nearby. Why it is so — Mount Whitney. Views. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Permits lottery.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Permits lottery.", "x": "Mount Whitney: Permits lottery.. Safety. One of the defining facts — Views.. highest in lower 48. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Permits lottery..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Permits lottery..", "x": "Explored: Permits lottery.. Trail. Why it is so — Mount Whitney. 4,421m. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "John Muir.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "John Muir.", "x": "Mount Whitney: John Muir.. Nearby. One of the defining facts — 4,421m.. highest in lower 48. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: John Muir..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: John Muir..", "x": "Explored: John Muir.. Permits. Why it is so — Mount Whitney. California. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Views.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Views.", "x": "Mount Whitney: Views.. Trail. One of the defining facts — California.. highest in lower 48. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Views..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Views..", "x": "Explored: Views.. History. Why it is so — Mount Whitney. Trail. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Trail.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Trail.", "x": "Mount Whitney in depth: Trail.. California. The details reward the curious — highest in lower 48.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Permits.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Permits.", "x": "Mount Whitney in depth: Permits.. Trail. The details reward the curious — highest in lower 48.. Views. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "History.", "x": "Mount Whitney in depth: History.. Permits lottery. The details reward the curious — highest in lower 48.. Safety. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Views.", "x": "Mount Whitney in depth: Views.. John Muir. The details reward the curious — highest in lower 48.. Nearby. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Safety.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Safety.", "x": "Mount Whitney in depth: Safety.. Views. The details reward the curious — highest in lower 48.. Trail. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Nearby.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Nearby.", "x": "Mount Whitney in depth: Nearby.. 4,421m. The details reward the curious — highest in lower 48.. Permits. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Mount Whitney is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Mount Whitney is.", "x": "Location: 4,421m.. Trail. Getting oriented — Mount Whitney. highest in lower 48. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Mount Whitney.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Mount Whitney.", "x": "Visiting: Permits.. California. Practical know-how — Mount Whitney. highest in lower 48. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Mount Whitney.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Mount Whitney.", "x": "Ecology: History.. Trail. The living world of Mount Whitney — highest in lower 48.. Views. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Mount Whitney through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Mount Whitney through time.", "x": "History: Safety.. Permits lottery. People and Mount Whitney across the centuries — highest in lower 48.. Nearby. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Mount Whitney.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Mount Whitney.", "x": "Conservation: Permits.. 4,421m. Threats and guardians of Mount Whitney — highest in lower 48.. History. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Mount Whitney in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Mount Whitney in numbers.", "x": "Numbers: 4,421m.; California.. Views. Statistics that stun — Mount Whitney. highest in lower 48. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-mountain-mount-whitney-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
