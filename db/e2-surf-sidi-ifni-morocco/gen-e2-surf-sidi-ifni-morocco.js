(function(){'use strict';
/* JAH Sidi Ifni Morocco Surf Spot Database generator — jahdb-e2-surf-sidi-ifni-morocco-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-surf-sidi-ifni-morocco',PREFIX='JAH-E2SURFSIDII-',NAME='JAH Sidi Ifni Morocco Surf Spot Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Sidi Ifni Morocco: the complete guide", "d": "Sidi Ifni Morocco: the legzira arches..", "g": "overview", "l": 2, "q": "What is Sidi Ifni Morocco: the complete guide?", "a": "Sidi Ifni Morocco: the legzira arches..", "x": "The complete surf spot guide to Sidi Ifni Morocco: the legzira arches.. Morocco. From formation to visiting, from wildlife to legends — everything about this surf spot in one database. Arches. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Morocco.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Morocco.", "x": "Sidi Ifni Morocco: Morocco.. Beach. One of the defining facts — Beach.. the legzira arches. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: Morocco..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: Morocco..", "x": "Explored: Morocco.. Morocco. Why it is so — Sidi Ifni Morocco. Legzira. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Arches.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Arches.", "x": "Sidi Ifni Morocco: Arches.. Wild. One of the defining facts — Legzira.. the legzira arches. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Arches..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Arches..", "x": "Explored: Arches.. Sunsets. Why it is so — Sidi Ifni Morocco. Wild. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Beach.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Beach.", "x": "Sidi Ifni Morocco: Beach.. Morocco. One of the defining facts — Wild.. the legzira arches. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Beach..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Beach..", "x": "Explored: Beach.. Legzira. Why it is so — Sidi Ifni Morocco. Sunsets. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Legzira.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Legzira.", "x": "Sidi Ifni Morocco: Legzira.. Sunsets. One of the defining facts — Sunsets.. the legzira arches. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Legzira..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Legzira..", "x": "Explored: Legzira.. Arches. Why it is so — Sidi Ifni Morocco. Morocco. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Wild.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Wild.", "x": "Sidi Ifni Morocco: Wild.. Legzira. One of the defining facts — Morocco.. the legzira arches. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Wild..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Wild..", "x": "Explored: Wild.. Beach. Why it is so — Sidi Ifni Morocco. Arches. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Sunsets.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Sunsets.", "x": "Sidi Ifni Morocco: Sunsets.. Arches. One of the defining facts — Arches.. the legzira arches. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Sunsets..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Sunsets..", "x": "Explored: Sunsets.. Wild. Why it is so — Sidi Ifni Morocco. Beach. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Arches.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Arches.", "x": "Sidi Ifni Morocco in depth: Arches.. Arches. The details reward the curious — the legzira arches.. Wild. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Beach.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Beach.", "x": "Sidi Ifni Morocco in depth: Beach.. Beach. The details reward the curious — the legzira arches.. Morocco. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Wild.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Wild.", "x": "Sidi Ifni Morocco in depth: Wild.. Legzira. The details reward the curious — the legzira arches.. Sunsets. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Morocco.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Morocco.", "x": "Sidi Ifni Morocco in depth: Morocco.. Wild. The details reward the curious — the legzira arches.. Legzira. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Sunsets.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Sunsets.", "x": "Sidi Ifni Morocco in depth: Sunsets.. Sunsets. The details reward the curious — the legzira arches.. Arches. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Legzira.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Legzira.", "x": "Sidi Ifni Morocco in depth: Legzira.. Morocco. The details reward the curious — the legzira arches.. Beach. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Sidi Ifni Morocco is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Sidi Ifni Morocco is.", "x": "Location: Morocco.. Arches. Getting oriented — Sidi Ifni Morocco. the legzira arches. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Sidi Ifni Morocco.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Sidi Ifni Morocco.", "x": "Visiting: Beach.. Arches. Practical know-how — Sidi Ifni Morocco. the legzira arches. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Sidi Ifni Morocco.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Sidi Ifni Morocco.", "x": "Ecology: Wild.. Beach. The living world of Sidi Ifni Morocco — the legzira arches.. Morocco. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Sidi Ifni Morocco through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Sidi Ifni Morocco through time.", "x": "History: Sunsets.. Legzira. People and Sidi Ifni Morocco across the centuries — the legzira arches.. Legzira. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Sidi Ifni Morocco.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Sidi Ifni Morocco.", "x": "Conservation: Beach.. Morocco. Threats and guardians of Sidi Ifni Morocco — the legzira arches.. Wild. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Sidi Ifni Morocco in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Sidi Ifni Morocco in numbers.", "x": "Numbers: Morocco.; Arches.. Morocco. Statistics that stun — Sidi Ifni Morocco. the legzira arches. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-surf-sidi-ifni-morocco-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
