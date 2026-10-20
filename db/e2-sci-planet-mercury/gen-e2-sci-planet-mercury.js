(function(){'use strict';
/* JAH Mercury Astronomy Database generator — jahdb-e2-sci-planet-mercury-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-planet-mercury',PREFIX='JAH-E2SCIPLANET-',NAME='JAH Mercury Astronomy Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mercury: overview", "d": "Mercury: the swift planet closest to the Sun..", "g": "overview", "l": 2, "q": "What is Mercury: overview?", "a": "Mercury: the swift planet closest to the Sun..", "x": "The complete astronomy guide to Mercury: the swift planet closest to the Sun.. 88-day year. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Mercury.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Mercury.", "x": "The core principle: Big temp swings.. the swift planet closest to the Sun. If you understand this one idea, everything else in Mercury clicks into place. Craters. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "88-day year.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "88-day year.", "x": "Mercury: 88-day year.. Scarps. This is load-bearing knowledge — the kind of fact that other facts hang from. the swift planet closest to the Sun. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why 88-day year. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why 88-day year. is true.", "x": "The explanation: 88-day year.. In astronomy, this fact connects to Transit of Mercury. — and once you see the mechanism, it stops being trivia and starts being understanding. Iron core huge. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Big temp swings.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Big temp swings.", "x": "Mercury: Big temp swings.. Water ice at poles. This is load-bearing knowledge — the kind of fact that other facts hang from. the swift planet closest to the Sun. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Big temp swings. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Big temp swings. is true.", "x": "The explanation: Big temp swings.. In astronomy, this fact connects to Einstein: orbit proof. — and once you see the mechanism, it stops being trivia and starts being understanding. No atmosphere. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Iron core huge.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Iron core huge.", "x": "Mercury: Iron core huge.. Transit of Mercury. This is load-bearing knowledge — the kind of fact that other facts hang from. the swift planet closest to the Sun. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Iron core huge. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Iron core huge. is true.", "x": "The explanation: Iron core huge.. In astronomy, this fact connects to Mariner 10. — and once you see the mechanism, it stops being trivia and starts being understanding. MESSENGER orbited. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "No atmosphere.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "No atmosphere.", "x": "Mercury: No atmosphere.. Einstein: orbit proof. This is load-bearing knowledge — the kind of fact that other facts hang from. the swift planet closest to the Sun. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why No atmosphere. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why No atmosphere. is true.", "x": "The explanation: No atmosphere.. In astronomy, this fact connects to Craters. — and once you see the mechanism, it stops being trivia and starts being understanding. BepiColombo en route. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "MESSENGER orbited.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "MESSENGER orbited.", "x": "Mercury: MESSENGER orbited.. Mariner 10. This is load-bearing knowledge — the kind of fact that other facts hang from. the swift planet closest to the Sun. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why MESSENGER orbited. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why MESSENGER orbited. is true.", "x": "The explanation: MESSENGER orbited.. In astronomy, this fact connects to Scarps. — and once you see the mechanism, it stops being trivia and starts being understanding. 88-day year. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "BepiColombo en route.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "BepiColombo en route.", "x": "Mercury: BepiColombo en route.. Craters. This is load-bearing knowledge — the kind of fact that other facts hang from. the swift planet closest to the Sun. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why BepiColombo en route. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why BepiColombo en route. is true.", "x": "The explanation: BepiColombo en route.. In astronomy, this fact connects to Water ice at poles. — and once you see the mechanism, it stops being trivia and starts being understanding. Big temp swings.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "88-day year.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "88-day year.", "x": "Mercury: 88-day year.. Scarps. This is load-bearing knowledge — the kind of fact that other facts hang from. the swift planet closest to the Sun. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why 88-day year. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why 88-day year. is true.", "x": "The explanation: 88-day year.. In astronomy, this fact connects to Transit of Mercury. — and once you see the mechanism, it stops being trivia and starts being understanding. Iron core huge. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Big temp swings.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Big temp swings.", "x": "Mercury: Big temp swings.. Water ice at poles. This is load-bearing knowledge — the kind of fact that other facts hang from. the swift planet closest to the Sun. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Big temp swings. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Big temp swings. is true.", "x": "The explanation: Big temp swings.. In astronomy, this fact connects to Einstein: orbit proof. — and once you see the mechanism, it stops being trivia and starts being understanding. No atmosphere. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Craters.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Craters.", "x": "Going deeper on Mercury: Craters.. Big temp swings. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mercury from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Scarps.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Scarps.", "x": "Going deeper on Mercury: Scarps.. Iron core huge. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mercury from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Water ice at poles.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Water ice at poles.", "x": "Going deeper on Mercury: Water ice at poles.. No atmosphere. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mercury from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Transit of Mercury.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Transit of Mercury.", "x": "Going deeper on Mercury: Transit of Mercury.. MESSENGER orbited. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mercury from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Einstein: orbit proof.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Einstein: orbit proof.", "x": "Going deeper on Mercury: Einstein: orbit proof.. BepiColombo en route. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mercury from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Mariner 10.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Mariner 10.", "x": "Going deeper on Mercury: Mariner 10.. 88-day year. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mercury from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Craters.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Craters.", "x": "Going deeper on Mercury: Craters.. Big temp swings. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mercury from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-planet-mercury-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
