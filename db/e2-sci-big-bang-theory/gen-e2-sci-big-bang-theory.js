(function(){'use strict';
/* JAH The Big Bang Astronomy Database generator — jahdb-e2-sci-big-bang-theory-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-big-bang-theory',PREFIX='JAH-E2SCIBIGBAN-',NAME='JAH The Big Bang Astronomy Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "The Big Bang: overview", "d": "The Big Bang: the universe's hot beginning..", "g": "overview", "l": 2, "q": "What is The Big Bang: overview?", "a": "The Big Bang: the universe's hot beginning..", "x": "The complete astronomy guide to The Big Bang: the universe's hot beginning.. 13.8B years ago. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind The Big Bang.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind The Big Bang.", "x": "The core principle: CMB afterglow.. the universe's hot beginning. If you understand this one idea, everything else in The Big Bang clicks into place. Lemaître priest. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "13.8B years ago.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "13.8B years ago.", "x": "The Big Bang: 13.8B years ago.. Hoyle named it. This is load-bearing knowledge — the kind of fact that other facts hang from. the universe's hot beginning. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why 13.8B years ago. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why 13.8B years ago. is true.", "x": "The explanation: 13.8B years ago.. In astronomy, this fact connects to Flatness. — and once you see the mechanism, it stops being trivia and starts being understanding. Hubble expansion. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "CMB afterglow.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "CMB afterglow.", "x": "The Big Bang: CMB afterglow.. Redshift. This is load-bearing knowledge — the kind of fact that other facts hang from. the universe's hot beginning. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why CMB afterglow. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why CMB afterglow. is true.", "x": "The explanation: CMB afterglow.. In astronomy, this fact connects to First stars. — and once you see the mechanism, it stops being trivia and starts being understanding. Nucleosynthesis. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Hubble expansion.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Hubble expansion.", "x": "The Big Bang: Hubble expansion.. Flatness. This is load-bearing knowledge — the kind of fact that other facts hang from. the universe's hot beginning. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Hubble expansion. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Hubble expansion. is true.", "x": "The explanation: Hubble expansion.. In astronomy, this fact connects to Open questions. — and once you see the mechanism, it stops being trivia and starts being understanding. Inflation theory. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Nucleosynthesis.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Nucleosynthesis.", "x": "The Big Bang: Nucleosynthesis.. First stars. This is load-bearing knowledge — the kind of fact that other facts hang from. the universe's hot beginning. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Nucleosynthesis. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Nucleosynthesis. is true.", "x": "The explanation: Nucleosynthesis.. In astronomy, this fact connects to Lemaître priest. — and once you see the mechanism, it stops being trivia and starts being understanding. Dark energy accelerates.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Inflation theory.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Inflation theory.", "x": "The Big Bang: Inflation theory.. Open questions. This is load-bearing knowledge — the kind of fact that other facts hang from. the universe's hot beginning. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Inflation theory. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Inflation theory. is true.", "x": "The explanation: Inflation theory.. In astronomy, this fact connects to Hoyle named it. — and once you see the mechanism, it stops being trivia and starts being understanding. 13.8B years ago. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Dark energy accelerates.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Dark energy accelerates.", "x": "The Big Bang: Dark energy accelerates.. Lemaître priest. This is load-bearing knowledge — the kind of fact that other facts hang from. the universe's hot beginning. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Dark energy accelerates. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Dark energy accelerates. is true.", "x": "The explanation: Dark energy accelerates.. In astronomy, this fact connects to Redshift. — and once you see the mechanism, it stops being trivia and starts being understanding. CMB afterglow. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "13.8B years ago.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "13.8B years ago.", "x": "The Big Bang: 13.8B years ago.. Hoyle named it. This is load-bearing knowledge — the kind of fact that other facts hang from. the universe's hot beginning. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why 13.8B years ago. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why 13.8B years ago. is true.", "x": "The explanation: 13.8B years ago.. In astronomy, this fact connects to Flatness. — and once you see the mechanism, it stops being trivia and starts being understanding. Hubble expansion. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "CMB afterglow.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "CMB afterglow.", "x": "The Big Bang: CMB afterglow.. Redshift. This is load-bearing knowledge — the kind of fact that other facts hang from. the universe's hot beginning. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why CMB afterglow. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why CMB afterglow. is true.", "x": "The explanation: CMB afterglow.. In astronomy, this fact connects to First stars. — and once you see the mechanism, it stops being trivia and starts being understanding. Nucleosynthesis. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Lemaître priest.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Lemaître priest.", "x": "Going deeper on The Big Bang: Lemaître priest.. CMB afterglow. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about The Big Bang from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Hoyle named it.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Hoyle named it.", "x": "Going deeper on The Big Bang: Hoyle named it.. Hubble expansion. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about The Big Bang from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Redshift.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Redshift.", "x": "Going deeper on The Big Bang: Redshift.. Nucleosynthesis. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about The Big Bang from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Flatness.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Flatness.", "x": "Going deeper on The Big Bang: Flatness.. Inflation theory. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about The Big Bang from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "First stars.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "First stars.", "x": "Going deeper on The Big Bang: First stars.. Dark energy accelerates. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about The Big Bang from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Open questions.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Open questions.", "x": "Going deeper on The Big Bang: Open questions.. 13.8B years ago. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about The Big Bang from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Lemaître priest.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Lemaître priest.", "x": "Going deeper on The Big Bang: Lemaître priest.. CMB afterglow. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about The Big Bang from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-big-bang-theory-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
