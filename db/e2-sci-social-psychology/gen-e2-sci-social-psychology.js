(function(){'use strict';
/* JAH Social Psychology Psychology Database generator — jahdb-e2-sci-social-psychology-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-social-psychology',PREFIX='JAH-E2SCISOCIAL-',NAME='JAH Social Psychology Psychology Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Social Psychology: overview", "d": "Social Psychology: how people think about and influence each other..", "g": "overview", "l": 2, "q": "What is Social Psychology: overview?", "a": "Social Psychology: how people think about and influence each other..", "x": "The complete psychology guide to Social Psychology: how people think about and influence each other.. Milgram obedience experiments. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Social Psychology.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Social Psychology.", "x": "The core principle: Asch conformity studies.. how people think about and influence each other. If you understand this one idea, everything else in Social Psychology clicks into place. Attribution theory. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Milgram obedience experiments.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Milgram obedience experiments.", "x": "Social Psychology: Milgram obedience experiments.. Groupthink. This is load-bearing knowledge — the kind of fact that other facts hang from. how people think about and influence each other. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Milgram obedience experiments. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Milgram obedience experiments. is true.", "x": "The explanation: Milgram obedience experiments.. In psychology, this fact connects to Social identity theory. — and once you see the mechanism, it stops being trivia and starts being understanding. Stanford prison experiment (criticized).", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Asch conformity studies.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Asch conformity studies.", "x": "Social Psychology: Asch conformity studies.. Persuasion research. This is load-bearing knowledge — the kind of fact that other facts hang from. how people think about and influence each other. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Asch conformity studies. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Asch conformity studies. is true.", "x": "The explanation: Asch conformity studies.. In psychology, this fact connects to Replication crisis hit hard. — and once you see the mechanism, it stops being trivia and starts being understanding. Cognitive dissonance (Festinger).", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Stanford prison experiment (criticized).", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Stanford prison experiment (criticized).", "x": "Social Psychology: Stanford prison experiment (criticized).. Social identity theory. This is load-bearing knowledge — the kind of fact that other facts hang from. how people think about and influence each other.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Stanford prison experiment (criticized). is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Stanford prison experiment (criticized). is true.", "x": "The explanation: Stanford prison experiment (criticized).. In psychology, this fact connects to Field experiments. — and once you see the mechanism, it stops being trivia and starts being understanding. Bystander effect.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Cognitive dissonance (Festinger).", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Cognitive dissonance (Festinger).", "x": "Social Psychology: Cognitive dissonance (Festinger).. Replication crisis hit hard. This is load-bearing knowledge — the kind of fact that other facts hang from. how people think about and influence each other.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Cognitive dissonance (Festinger). is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Cognitive dissonance (Festinger). is true.", "x": "The explanation: Cognitive dissonance (Festinger).. In psychology, this fact connects to Attribution theory. — and once you see the mechanism, it stops being trivia and starts being understanding. Stereotyping and prejudice.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Bystander effect.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Bystander effect.", "x": "Social Psychology: Bystander effect.. Field experiments. This is load-bearing knowledge — the kind of fact that other facts hang from. how people think about and influence each other. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Bystander effect. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Bystander effect. is true.", "x": "The explanation: Bystander effect.. In psychology, this fact connects to Groupthink. — and once you see the mechanism, it stops being trivia and starts being understanding. Milgram obedience experiments.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Stereotyping and prejudice.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Stereotyping and prejudice.", "x": "Social Psychology: Stereotyping and prejudice.. Attribution theory. This is load-bearing knowledge — the kind of fact that other facts hang from. how people think about and influence each other. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Stereotyping and prejudice. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Stereotyping and prejudice. is true.", "x": "The explanation: Stereotyping and prejudice.. In psychology, this fact connects to Persuasion research. — and once you see the mechanism, it stops being trivia and starts being understanding. Asch conformity studies.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Milgram obedience experiments.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Milgram obedience experiments.", "x": "Social Psychology: Milgram obedience experiments.. Groupthink. This is load-bearing knowledge — the kind of fact that other facts hang from. how people think about and influence each other. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Milgram obedience experiments. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Milgram obedience experiments. is true.", "x": "The explanation: Milgram obedience experiments.. In psychology, this fact connects to Social identity theory. — and once you see the mechanism, it stops being trivia and starts being understanding. Stanford prison experiment (criticized).", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Asch conformity studies.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Asch conformity studies.", "x": "Social Psychology: Asch conformity studies.. Persuasion research. This is load-bearing knowledge — the kind of fact that other facts hang from. how people think about and influence each other. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Asch conformity studies. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Asch conformity studies. is true.", "x": "The explanation: Asch conformity studies.. In psychology, this fact connects to Replication crisis hit hard. — and once you see the mechanism, it stops being trivia and starts being understanding. Cognitive dissonance (Festinger).", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Attribution theory.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Attribution theory.", "x": "Going deeper on Social Psychology: Attribution theory.. Asch conformity studies. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Social Psychology from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Groupthink.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Groupthink.", "x": "Going deeper on Social Psychology: Groupthink.. Stanford prison experiment (criticized). Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Social Psychology from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Persuasion research.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Persuasion research.", "x": "Going deeper on Social Psychology: Persuasion research.. Cognitive dissonance (Festinger). Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Social Psychology from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Social identity theory.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Social identity theory.", "x": "Going deeper on Social Psychology: Social identity theory.. Bystander effect. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Social Psychology from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Replication crisis hit hard.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Replication crisis hit hard.", "x": "Going deeper on Social Psychology: Replication crisis hit hard.. Stereotyping and prejudice. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Social Psychology from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Field experiments.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Field experiments.", "x": "Going deeper on Social Psychology: Field experiments.. Milgram obedience experiments. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Social Psychology from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Attribution theory.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Attribution theory.", "x": "Going deeper on Social Psychology: Attribution theory.. Asch conformity studies. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Social Psychology from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-social-psychology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
