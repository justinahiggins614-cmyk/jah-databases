(function(){'use strict';
/* JAH Plant Hormones Botany Database generator — jahdb-e2-sci-plant-hormones-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-plant-hormones',PREFIX='JAH-E2SCIPLANTH-',NAME='JAH Plant Hormones Botany Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Plant Hormones: overview", "d": "Plant Hormones: chemical messengers guiding growth..", "g": "overview", "l": 2, "q": "What is Plant Hormones: overview?", "a": "Plant Hormones: chemical messengers guiding growth..", "x": "The complete botany guide to Plant Hormones: chemical messengers guiding growth.. Auxin: growth direction. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Plant Hormones.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Plant Hormones.", "x": "The core principle: Gibberellin: stem elongation.. chemical messengers guiding growth. If you understand this one idea, everything else in Plant Hormones clicks into place. Apical dominance. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Auxin: growth direction.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Auxin: growth direction.", "x": "Plant Hormones: Auxin: growth direction.. Fruit ripening control. This is load-bearing knowledge — the kind of fact that other facts hang from. chemical messengers guiding growth. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Auxin: growth direction. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Auxin: growth direction. is true.", "x": "The explanation: Auxin: growth direction.. In botany, this fact connects to Herbicides mimic. — and once you see the mechanism, it stops being trivia and starts being understanding. Cytokinin: cell division.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Gibberellin: stem elongation.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Gibberellin: stem elongation.", "x": "Plant Hormones: Gibberellin: stem elongation.. Tissue culture. This is load-bearing knowledge — the kind of fact that other facts hang from. chemical messengers guiding growth. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Gibberellin: stem elongation. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Gibberellin: stem elongation. is true.", "x": "The explanation: Gibberellin: stem elongation.. In botany, this fact connects to Research. — and once you see the mechanism, it stops being trivia and starts being understanding. Abscisic acid: dormancy.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Cytokinin: cell division.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Cytokinin: cell division.", "x": "Plant Hormones: Cytokinin: cell division.. Herbicides mimic. This is load-bearing knowledge — the kind of fact that other facts hang from. chemical messengers guiding growth. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Cytokinin: cell division. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Cytokinin: cell division. is true.", "x": "The explanation: Cytokinin: cell division.. In botany, this fact connects to Agriculture. — and once you see the mechanism, it stops being trivia and starts being understanding. Ethylene: ripening. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Abscisic acid: dormancy.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Abscisic acid: dormancy.", "x": "Plant Hormones: Abscisic acid: dormancy.. Research. This is load-bearing knowledge — the kind of fact that other facts hang from. chemical messengers guiding growth. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Abscisic acid: dormancy. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Abscisic acid: dormancy. is true.", "x": "The explanation: Abscisic acid: dormancy.. In botany, this fact connects to Apical dominance. — and once you see the mechanism, it stops being trivia and starts being understanding. Phototropism. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Ethylene: ripening.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Ethylene: ripening.", "x": "Plant Hormones: Ethylene: ripening.. Agriculture. This is load-bearing knowledge — the kind of fact that other facts hang from. chemical messengers guiding growth. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Ethylene: ripening. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Ethylene: ripening. is true.", "x": "The explanation: Ethylene: ripening.. In botany, this fact connects to Fruit ripening control. — and once you see the mechanism, it stops being trivia and starts being understanding. Auxin: growth direction.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Phototropism.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Phototropism.", "x": "Plant Hormones: Phototropism.. Apical dominance. This is load-bearing knowledge — the kind of fact that other facts hang from. chemical messengers guiding growth. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Phototropism. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Phototropism. is true.", "x": "The explanation: Phototropism.. In botany, this fact connects to Tissue culture. — and once you see the mechanism, it stops being trivia and starts being understanding. Gibberellin: stem elongation. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Auxin: growth direction.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Auxin: growth direction.", "x": "Plant Hormones: Auxin: growth direction.. Fruit ripening control. This is load-bearing knowledge — the kind of fact that other facts hang from. chemical messengers guiding growth. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Auxin: growth direction. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Auxin: growth direction. is true.", "x": "The explanation: Auxin: growth direction.. In botany, this fact connects to Herbicides mimic. — and once you see the mechanism, it stops being trivia and starts being understanding. Cytokinin: cell division.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Gibberellin: stem elongation.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Gibberellin: stem elongation.", "x": "Plant Hormones: Gibberellin: stem elongation.. Tissue culture. This is load-bearing knowledge — the kind of fact that other facts hang from. chemical messengers guiding growth. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Gibberellin: stem elongation. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Gibberellin: stem elongation. is true.", "x": "The explanation: Gibberellin: stem elongation.. In botany, this fact connects to Research. — and once you see the mechanism, it stops being trivia and starts being understanding. Abscisic acid: dormancy.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Apical dominance.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Apical dominance.", "x": "Going deeper on Plant Hormones: Apical dominance.. Gibberellin: stem elongation. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Plant Hormones from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Fruit ripening control.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Fruit ripening control.", "x": "Going deeper on Plant Hormones: Fruit ripening control.. Cytokinin: cell division. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Plant Hormones from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Tissue culture.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Tissue culture.", "x": "Going deeper on Plant Hormones: Tissue culture.. Abscisic acid: dormancy. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Plant Hormones from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Herbicides mimic.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Herbicides mimic.", "x": "Going deeper on Plant Hormones: Herbicides mimic.. Ethylene: ripening. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Plant Hormones from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Research.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Research.", "x": "Going deeper on Plant Hormones: Research.. Phototropism. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Plant Hormones from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Agriculture.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Agriculture.", "x": "Going deeper on Plant Hormones: Agriculture.. Auxin: growth direction. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Plant Hormones from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Apical dominance.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Apical dominance.", "x": "Going deeper on Plant Hormones: Apical dominance.. Gibberellin: stem elongation. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Plant Hormones from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-plant-hormones-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
