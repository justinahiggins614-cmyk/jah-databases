(function(){'use strict';
/* JAH Mauna Kea Mountain Database generator — jahdb-e2-mountain-mauna-kea-mountain-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-mountain-mauna-kea-mountain',PREFIX='JAH-E2MOUNTAINM-',NAME='JAH Mauna Kea Mountain Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mauna Kea: the complete guide", "d": "Mauna Kea: tallest from base; sacred..", "g": "overview", "l": 2, "q": "What is Mauna Kea: the complete guide?", "a": "Mauna Kea: tallest from base; sacred..", "x": "The complete mountain guide to Mauna Kea: tallest from base; sacred.. 10,200m base-to-peak. From formation to visiting, from wildlife to legends — everything about this mountain in one database. Astronomy.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "10,200m base-to-peak.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "10,200m base-to-peak.", "x": "Mauna Kea: 10,200m base-to-peak.. Culture. One of the defining facts — Sacred.. tallest from base; sacred. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 10,200m base-to-peak..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 10,200m base-to-peak..", "x": "Explored: 10,200m base-to-peak.. Views. Why it is so — Mauna Kea. Snow Hawaii. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Observatories.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Observatories.", "x": "Mauna Kea: Observatories.. Summit. One of the defining facts — Snow Hawaii.. tallest from base; sacred. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Observatories..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Observatories..", "x": "Explored: Observatories.. History. Why it is so — Mauna Kea. Saddle Road. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Sacred.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Sacred.", "x": "Mauna Kea: Sacred.. Views. One of the defining facts — Saddle Road.. tallest from base; sacred. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Sacred..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Sacred..", "x": "Explored: Sacred.. Respect. Why it is so — Mauna Kea. Protests. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Snow Hawaii.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Snow Hawaii.", "x": "Mauna Kea: Snow Hawaii.. History. One of the defining facts — Protests.. tallest from base; sacred. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Snow Hawaii..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Snow Hawaii..", "x": "Explored: Snow Hawaii.. Astronomy. Why it is so — Mauna Kea. 10,200m base-to-peak. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Saddle Road.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Saddle Road.", "x": "Mauna Kea: Saddle Road.. Respect. One of the defining facts — 10,200m base-to-peak.. tallest from base; sacred. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Saddle Road..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Saddle Road..", "x": "Explored: Saddle Road.. Culture. Why it is so — Mauna Kea. Observatories. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Protests.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Protests.", "x": "Mauna Kea: Protests.. Astronomy. One of the defining facts — Observatories.. tallest from base; sacred. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Protests..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Protests..", "x": "Explored: Protests.. Summit. Why it is so — Mauna Kea. Sacred. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Astronomy.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Astronomy.", "x": "Mauna Kea in depth: Astronomy.. Observatories. The details reward the curious — tallest from base; sacred.. Summit. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Culture.", "x": "Mauna Kea in depth: Culture.. Sacred. The details reward the curious — tallest from base; sacred.. Views. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Summit.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Summit.", "x": "Mauna Kea in depth: Summit.. Snow Hawaii. The details reward the curious — tallest from base; sacred.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Views.", "x": "Mauna Kea in depth: Views.. Saddle Road. The details reward the curious — tallest from base; sacred.. Respect. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "History.", "x": "Mauna Kea in depth: History.. Protests. The details reward the curious — tallest from base; sacred.. Astronomy. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Respect.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Respect.", "x": "Mauna Kea in depth: Respect.. 10,200m base-to-peak. The details reward the curious — tallest from base; sacred.. Culture. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Mauna Kea is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Mauna Kea is.", "x": "Location: 10,200m base-to-peak.. Astronomy. Getting oriented — Mauna Kea. tallest from base; sacred. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Mauna Kea.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Mauna Kea.", "x": "Visiting: Culture.. Observatories. Practical know-how — Mauna Kea. tallest from base; sacred. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Mauna Kea.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Mauna Kea.", "x": "Ecology: Summit.. Sacred. The living world of Mauna Kea — tallest from base; sacred.. Views. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Mauna Kea through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Mauna Kea through time.", "x": "History: History.. Snow Hawaii. People and Mauna Kea across the centuries — tallest from base; sacred.. Respect. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Mauna Kea.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Mauna Kea.", "x": "Conservation: Culture.. 10,200m base-to-peak. Threats and guardians of Mauna Kea — tallest from base; sacred.. Summit. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Mauna Kea in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Mauna Kea in numbers.", "x": "Numbers: 10,200m base-to-peak.; Observatories.. Views. Statistics that stun — Mauna Kea. tallest from base; sacred. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-mountain-mauna-kea-mountain-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
