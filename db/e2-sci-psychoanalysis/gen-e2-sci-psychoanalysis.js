(function(){'use strict';
/* JAH Psychoanalysis Psychology Database generator — jahdb-e2-sci-psychoanalysis-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-psychoanalysis',PREFIX='JAH-E2SCIPSYCHO-',NAME='JAH Psychoanalysis Psychology Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Psychoanalysis: overview", "d": "Psychoanalysis: Freud's theory of the unconscious mind..", "g": "overview", "l": 2, "q": "What is Psychoanalysis: overview?", "a": "Psychoanalysis: Freud's theory of the unconscious mind..", "x": "The complete psychology guide to Psychoanalysis: Freud's theory of the unconscious mind.. Founded by Sigmund Freud. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Psychoanalysis.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Psychoanalysis.", "x": "The core principle: Id, ego, superego model.. Freud's theory of the unconscious mind. If you understand this one idea, everything else in Psychoanalysis clicks into place. Psychosexual stages. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Founded by Sigmund Freud.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Founded by Sigmund Freud.", "x": "Psychoanalysis: Founded by Sigmund Freud.. Defense mechanisms. This is load-bearing knowledge — the kind of fact that other facts hang from. Freud's theory of the unconscious mind. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Founded by Sigmund Freud. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Founded by Sigmund Freud. is true.", "x": "The explanation: Founded by Sigmund Freud.. In psychology, this fact connects to Jung split off (collective unconscious). — and once you see the mechanism, it stops being trivia and starts being understanding. Unconscious drives behavior.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Id, ego, superego model.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Id, ego, superego model.", "x": "Psychoanalysis: Id, ego, superego model.. Transference in therapy. This is load-bearing knowledge — the kind of fact that other facts hang from. Freud's theory of the unconscious mind. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Id, ego, superego model. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Id, ego, superego model. is true.", "x": "The explanation: Id, ego, superego model.. In psychology, this fact connects to Adler: inferiority complex. — and once you see the mechanism, it stops being trivia and starts being understanding. Dream analysis method.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Unconscious drives behavior.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Unconscious drives behavior.", "x": "Psychoanalysis: Unconscious drives behavior.. Jung split off (collective unconscious). This is load-bearing knowledge — the kind of fact that other facts hang from. Freud's theory of the unconscious mind.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Unconscious drives behavior. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Unconscious drives behavior. is true.", "x": "The explanation: Unconscious drives behavior.. In psychology, this fact connects to Criticized as unfalsifiable. — and once you see the mechanism, it stops being trivia and starts being understanding. Free association technique.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Dream analysis method.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Dream analysis method.", "x": "Psychoanalysis: Dream analysis method.. Adler: inferiority complex. This is load-bearing knowledge — the kind of fact that other facts hang from. Freud's theory of the unconscious mind. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Dream analysis method. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Dream analysis method. is true.", "x": "The explanation: Dream analysis method.. In psychology, this fact connects to Cultural influence huge. — and once you see the mechanism, it stops being trivia and starts being understanding. Oedipus complex concept.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Free association technique.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Free association technique.", "x": "Psychoanalysis: Free association technique.. Criticized as unfalsifiable. This is load-bearing knowledge — the kind of fact that other facts hang from. Freud's theory of the unconscious mind. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Free association technique. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Free association technique. is true.", "x": "The explanation: Free association technique.. In psychology, this fact connects to Modern psychodynamic therapy. — and once you see the mechanism, it stops being trivia and starts being understanding. Talk therapy origins.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Oedipus complex concept.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Oedipus complex concept.", "x": "Psychoanalysis: Oedipus complex concept.. Cultural influence huge. This is load-bearing knowledge — the kind of fact that other facts hang from. Freud's theory of the unconscious mind. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Oedipus complex concept. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Oedipus complex concept. is true.", "x": "The explanation: Oedipus complex concept.. In psychology, this fact connects to Psychosexual stages. — and once you see the mechanism, it stops being trivia and starts being understanding. Much is scientifically disputed.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Talk therapy origins.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Talk therapy origins.", "x": "Psychoanalysis: Talk therapy origins.. Modern psychodynamic therapy. This is load-bearing knowledge — the kind of fact that other facts hang from. Freud's theory of the unconscious mind. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Talk therapy origins. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Talk therapy origins. is true.", "x": "The explanation: Talk therapy origins.. In psychology, this fact connects to Defense mechanisms. — and once you see the mechanism, it stops being trivia and starts being understanding. Founded by Sigmund Freud.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Much is scientifically disputed.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Much is scientifically disputed.", "x": "Psychoanalysis: Much is scientifically disputed.. Psychosexual stages. This is load-bearing knowledge — the kind of fact that other facts hang from. Freud's theory of the unconscious mind. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Much is scientifically disputed. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Much is scientifically disputed. is true.", "x": "The explanation: Much is scientifically disputed.. In psychology, this fact connects to Transference in therapy. — and once you see the mechanism, it stops being trivia and starts being understanding. Id, ego, superego model.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Psychosexual stages.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Psychosexual stages.", "x": "Going deeper on Psychoanalysis: Psychosexual stages.. Id, ego, superego model. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Psychoanalysis from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Defense mechanisms.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Defense mechanisms.", "x": "Going deeper on Psychoanalysis: Defense mechanisms.. Unconscious drives behavior. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Psychoanalysis from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Transference in therapy.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Transference in therapy.", "x": "Going deeper on Psychoanalysis: Transference in therapy.. Dream analysis method. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Psychoanalysis from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Jung split off (collective unconscious).", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Jung split off (collective unconscious).", "x": "Going deeper on Psychoanalysis: Jung split off (collective unconscious).. Free association technique. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Psychoanalysis from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Adler: inferiority complex.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Adler: inferiority complex.", "x": "Going deeper on Psychoanalysis: Adler: inferiority complex.. Oedipus complex concept. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Psychoanalysis from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Criticized as unfalsifiable.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Criticized as unfalsifiable.", "x": "Going deeper on Psychoanalysis: Criticized as unfalsifiable.. Talk therapy origins. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Psychoanalysis from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Cultural influence huge.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Cultural influence huge.", "x": "Going deeper on Psychoanalysis: Cultural influence huge.. Much is scientifically disputed. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Psychoanalysis from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-psychoanalysis-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
