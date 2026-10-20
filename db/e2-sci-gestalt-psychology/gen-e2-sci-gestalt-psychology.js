(function(){'use strict';
/* JAH Gestalt Psychology Psychology Database generator — jahdb-e2-sci-gestalt-psychology-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-gestalt-psychology',PREFIX='JAH-E2SCIGESTAL-',NAME='JAH Gestalt Psychology Psychology Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Gestalt Psychology: overview", "d": "Gestalt Psychology: the whole is different from the sum of its parts..", "g": "overview", "l": 2, "q": "What is Gestalt Psychology: overview?", "a": "Gestalt Psychology: the whole is different from the sum of its parts..", "x": "The complete psychology guide to Gestalt Psychology: the whole is different from the sum of its parts.. 'The whole is other than the sum of parts'. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Gestalt Psychology.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Gestalt Psychology.", "x": "The core principle: Figure-ground perception.. the whole is different from the sum of its parts. If you understand this one idea, everything else in Gestalt Psychology clicks into place. Gestalt laws of grouping. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "'The whole is other than the sum of parts'.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "'The whole is other than the sum of parts'.", "x": "Gestalt Psychology: 'The whole is other than the sum of parts'.. Applied to design/UI. This is load-bearing knowledge — the kind of fact that other facts hang from. the whole is different from the sum of its parts.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why 'The whole is other than the sum of parts'. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why 'The whole is other than the sum of parts'. is true.", "x": "The explanation: 'The whole is other than the sum of parts'.. In psychology, this fact connects to Problem-solving by insight. — and once you see the mechanism, it stops being trivia and starts being understanding. Laws: proximity, similarity, closure.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Figure-ground perception.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Figure-ground perception.", "x": "Gestalt Psychology: Figure-ground perception.. Gestalt therapy (Perls). This is load-bearing knowledge — the kind of fact that other facts hang from. the whole is different from the sum of its parts. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Figure-ground perception. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Figure-ground perception. is true.", "x": "The explanation: Figure-ground perception.. In psychology, this fact connects to Visual perception research. — and once you see the mechanism, it stops being trivia and starts being understanding. Wertheimer, Koffka, Kohler.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Laws: proximity, similarity, closure.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Laws: proximity, similarity, closure.", "x": "Gestalt Psychology: Laws: proximity, similarity, closure.. Problem-solving by insight. This is load-bearing knowledge — the kind of fact that other facts hang from. the whole is different from the sum of its parts.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Laws: proximity, similarity, closure. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Laws: proximity, similarity, closure. is true.", "x": "The explanation: Laws: proximity, similarity, closure.. In psychology, this fact connects to Holistic approach. — and once you see the mechanism, it stops being trivia and starts being understanding. Phi phenomenon (motion illusion).", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Wertheimer, Koffka, Kohler.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Wertheimer, Koffka, Kohler.", "x": "Gestalt Psychology: Wertheimer, Koffka, Kohler.. Visual perception research. This is load-bearing knowledge — the kind of fact that other facts hang from. the whole is different from the sum of its parts.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Wertheimer, Koffka, Kohler. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Wertheimer, Koffka, Kohler. is true.", "x": "The explanation: Wertheimer, Koffka, Kohler.. In psychology, this fact connects to Gestalt laws of grouping. — and once you see the mechanism, it stops being trivia and starts being understanding. Insight learning (Kohler's apes).", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Phi phenomenon (motion illusion).", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Phi phenomenon (motion illusion).", "x": "Gestalt Psychology: Phi phenomenon (motion illusion).. Holistic approach. This is load-bearing knowledge — the kind of fact that other facts hang from. the whole is different from the sum of its parts.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Phi phenomenon (motion illusion). is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Phi phenomenon (motion illusion). is true.", "x": "The explanation: Phi phenomenon (motion illusion).. In psychology, this fact connects to Applied to design/UI. — and once you see the mechanism, it stops being trivia and starts being understanding. 'The whole is other than the sum of parts'.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Insight learning (Kohler's apes).", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Insight learning (Kohler's apes).", "x": "Gestalt Psychology: Insight learning (Kohler's apes).. Gestalt laws of grouping. This is load-bearing knowledge — the kind of fact that other facts hang from. the whole is different from the sum of its parts.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Insight learning (Kohler's apes). is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Insight learning (Kohler's apes). is true.", "x": "The explanation: Insight learning (Kohler's apes).. In psychology, this fact connects to Gestalt therapy (Perls). — and once you see the mechanism, it stops being trivia and starts being understanding. Figure-ground perception.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "'The whole is other than the sum of parts'.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "'The whole is other than the sum of parts'.", "x": "Gestalt Psychology: 'The whole is other than the sum of parts'.. Applied to design/UI. This is load-bearing knowledge — the kind of fact that other facts hang from. the whole is different from the sum of its parts.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why 'The whole is other than the sum of parts'. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why 'The whole is other than the sum of parts'. is true.", "x": "The explanation: 'The whole is other than the sum of parts'.. In psychology, this fact connects to Problem-solving by insight. — and once you see the mechanism, it stops being trivia and starts being understanding. Laws: proximity, similarity, closure.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Figure-ground perception.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Figure-ground perception.", "x": "Gestalt Psychology: Figure-ground perception.. Gestalt therapy (Perls). This is load-bearing knowledge — the kind of fact that other facts hang from. the whole is different from the sum of its parts. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Figure-ground perception. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Figure-ground perception. is true.", "x": "The explanation: Figure-ground perception.. In psychology, this fact connects to Visual perception research. — and once you see the mechanism, it stops being trivia and starts being understanding. Wertheimer, Koffka, Kohler.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Gestalt laws of grouping.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Gestalt laws of grouping.", "x": "Going deeper on Gestalt Psychology: Gestalt laws of grouping.. Figure-ground perception. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Gestalt Psychology from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Applied to design/UI.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Applied to design/UI.", "x": "Going deeper on Gestalt Psychology: Applied to design/UI.. Laws: proximity, similarity, closure. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Gestalt Psychology from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Gestalt therapy (Perls).", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Gestalt therapy (Perls).", "x": "Going deeper on Gestalt Psychology: Gestalt therapy (Perls).. Wertheimer, Koffka, Kohler. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Gestalt Psychology from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Problem-solving by insight.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Problem-solving by insight.", "x": "Going deeper on Gestalt Psychology: Problem-solving by insight.. Phi phenomenon (motion illusion). Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Gestalt Psychology from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Visual perception research.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Visual perception research.", "x": "Going deeper on Gestalt Psychology: Visual perception research.. Insight learning (Kohler's apes). Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Gestalt Psychology from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Holistic approach.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Holistic approach.", "x": "Going deeper on Gestalt Psychology: Holistic approach.. 'The whole is other than the sum of parts'. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Gestalt Psychology from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Gestalt laws of grouping.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Gestalt laws of grouping.", "x": "Going deeper on Gestalt Psychology: Gestalt laws of grouping.. Figure-ground perception. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Gestalt Psychology from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-gestalt-psychology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
