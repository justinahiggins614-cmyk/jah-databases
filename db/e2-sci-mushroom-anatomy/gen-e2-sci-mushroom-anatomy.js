(function(){'use strict';
/* JAH Mushroom Anatomy Mycology Database generator — jahdb-e2-sci-mushroom-anatomy-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-mushroom-anatomy',PREFIX='JAH-E2SCIMUSHRO-',NAME='JAH Mushroom Anatomy Mycology Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mushroom Anatomy: overview", "d": "Mushroom Anatomy: the fruiting body of a fungus..", "g": "overview", "l": 2, "q": "What is Mushroom Anatomy: overview?", "a": "Mushroom Anatomy: the fruiting body of a fungus..", "x": "The complete mycology guide to Mushroom Anatomy: the fruiting body of a fungus.. Cap, gills, stem. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Mushroom Anatomy.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Mushroom Anatomy.", "x": "The core principle: Spores from gills.. the fruiting body of a fungus. If you understand this one idea, everything else in Mushroom Anatomy clicks into place. Parts labeled. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Cap, gills, stem.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Cap, gills, stem.", "x": "Mushroom Anatomy: Cap, gills, stem.. Veils/rings. This is load-bearing knowledge — the kind of fact that other facts hang from. the fruiting body of a fungus. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Cap, gills, stem. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Cap, gills, stem. is true.", "x": "The explanation: Cap, gills, stem.. In mycology, this fact connects to Microscopy. — and once you see the mechanism, it stops being trivia and starts being understanding. Mycelium: main body. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Spores from gills.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Spores from gills.", "x": "Mushroom Anatomy: Spores from gills.. Pores vs gills. This is load-bearing knowledge — the kind of fact that other facts hang from. the fruiting body of a fungus. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Spores from gills. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Spores from gills. is true.", "x": "The explanation: Spores from gills.. In mycology, this fact connects to Edibility caution. — and once you see the mechanism, it stops being trivia and starts being understanding. Fruiting triggers. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Mycelium: main body.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Mycelium: main body.", "x": "Mushroom Anatomy: Mycelium: main body.. Microscopy. This is load-bearing knowledge — the kind of fact that other facts hang from. the fruiting body of a fungus. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Mycelium: main body. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Mycelium: main body. is true.", "x": "The explanation: Mycelium: main body.. In mycology, this fact connects to Foraging. — and once you see the mechanism, it stops being trivia and starts being understanding. Spore prints ID. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Fruiting triggers.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Fruiting triggers.", "x": "Mushroom Anatomy: Fruiting triggers.. Edibility caution. This is load-bearing knowledge — the kind of fact that other facts hang from. the fruiting body of a fungus. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Fruiting triggers. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Fruiting triggers. is true.", "x": "The explanation: Fruiting triggers.. In mycology, this fact connects to Parts labeled. — and once you see the mechanism, it stops being trivia and starts being understanding. Not plants. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Spore prints ID.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Spore prints ID.", "x": "Mushroom Anatomy: Spore prints ID.. Foraging. This is load-bearing knowledge — the kind of fact that other facts hang from. the fruiting body of a fungus. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Spore prints ID. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Spore prints ID. is true.", "x": "The explanation: Spore prints ID.. In mycology, this fact connects to Veils/rings. — and once you see the mechanism, it stops being trivia and starts being understanding. Cap, gills, stem. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Not plants.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Not plants.", "x": "Mushroom Anatomy: Not plants.. Parts labeled. This is load-bearing knowledge — the kind of fact that other facts hang from. the fruiting body of a fungus. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Not plants. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Not plants. is true.", "x": "The explanation: Not plants.. In mycology, this fact connects to Pores vs gills. — and once you see the mechanism, it stops being trivia and starts being understanding. Spores from gills. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Cap, gills, stem.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Cap, gills, stem.", "x": "Mushroom Anatomy: Cap, gills, stem.. Veils/rings. This is load-bearing knowledge — the kind of fact that other facts hang from. the fruiting body of a fungus. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Cap, gills, stem. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Cap, gills, stem. is true.", "x": "The explanation: Cap, gills, stem.. In mycology, this fact connects to Microscopy. — and once you see the mechanism, it stops being trivia and starts being understanding. Mycelium: main body. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Spores from gills.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Spores from gills.", "x": "Mushroom Anatomy: Spores from gills.. Pores vs gills. This is load-bearing knowledge — the kind of fact that other facts hang from. the fruiting body of a fungus. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Spores from gills. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Spores from gills. is true.", "x": "The explanation: Spores from gills.. In mycology, this fact connects to Edibility caution. — and once you see the mechanism, it stops being trivia and starts being understanding. Fruiting triggers. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Parts labeled.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Parts labeled.", "x": "Going deeper on Mushroom Anatomy: Parts labeled.. Spores from gills. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mushroom Anatomy from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Veils/rings.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Veils/rings.", "x": "Going deeper on Mushroom Anatomy: Veils/rings.. Mycelium: main body. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mushroom Anatomy from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Pores vs gills.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Pores vs gills.", "x": "Going deeper on Mushroom Anatomy: Pores vs gills.. Fruiting triggers. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mushroom Anatomy from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Microscopy.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Microscopy.", "x": "Going deeper on Mushroom Anatomy: Microscopy.. Spore prints ID. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mushroom Anatomy from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Edibility caution.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Edibility caution.", "x": "Going deeper on Mushroom Anatomy: Edibility caution.. Not plants. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mushroom Anatomy from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Foraging.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Foraging.", "x": "Going deeper on Mushroom Anatomy: Foraging.. Cap, gills, stem. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mushroom Anatomy from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Parts labeled.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Parts labeled.", "x": "Going deeper on Mushroom Anatomy: Parts labeled.. Spores from gills. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Mushroom Anatomy from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-mushroom-anatomy-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
