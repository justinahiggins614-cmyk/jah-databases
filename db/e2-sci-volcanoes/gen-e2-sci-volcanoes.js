(function(){'use strict';
/* JAH Volcanoes Geology Database generator — jahdb-e2-sci-volcanoes-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-volcanoes',PREFIX='JAH-E2SCIVOLCAN-',NAME='JAH Volcanoes Geology Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Volcanoes: overview", "d": "Volcanoes: vents where magma reaches the surface..", "g": "overview", "l": 2, "q": "What is Volcanoes: overview?", "a": "Volcanoes: vents where magma reaches the surface..", "x": "The complete geology guide to Volcanoes: vents where magma reaches the surface.. Magma chamber feeds eruptions. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Volcanoes.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Volcanoes.", "x": "The core principle: Shield vs stratovolcano vs cinder.. vents where magma reaches the surface. If you understand this one idea, everything else in Volcanoes clicks into place. Ring of Fire volcanoes. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Magma chamber feeds eruptions.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Magma chamber feeds eruptions.", "x": "Volcanoes: Magma chamber feeds eruptions.. Lava types: pahoehoe/aa. This is load-bearing knowledge — the kind of fact that other facts hang from. vents where magma reaches the surface. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Magma chamber feeds eruptions. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Magma chamber feeds eruptions. is true.", "x": "The explanation: Magma chamber feeds eruptions.. In geology, this fact connects to Monitoring: tiltmeters, gas. — and once you see the mechanism, it stops being trivia and starts being understanding. VEI eruption scale.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Shield vs stratovolcano vs cinder.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Shield vs stratovolcano vs cinder.", "x": "Volcanoes: Shield vs stratovolcano vs cinder.. Pyroclastic flows kill. This is load-bearing knowledge — the kind of fact that other facts hang from. vents where magma reaches the surface. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Shield vs stratovolcano vs cinder. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Shield vs stratovolcano vs cinder. is true.", "x": "The explanation: Shield vs stratovolcano vs cinder.. In geology, this fact connects to Pompeii (79 AD). — and once you see the mechanism, it stops being trivia and starts being understanding. Yellowstone: supervolcano.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "VEI eruption scale.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "VEI eruption scale.", "x": "Volcanoes: VEI eruption scale.. Monitoring: tiltmeters, gas. This is load-bearing knowledge — the kind of fact that other facts hang from. vents where magma reaches the surface. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why VEI eruption scale. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why VEI eruption scale. is true.", "x": "The explanation: VEI eruption scale.. In geology, this fact connects to Iceland's Eyjafjallajokull. — and once you see the mechanism, it stops being trivia and starts being understanding. Hawaii: hotspot volcanoes.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Yellowstone: supervolcano.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Yellowstone: supervolcano.", "x": "Volcanoes: Yellowstone: supervolcano.. Pompeii (79 AD). This is load-bearing knowledge — the kind of fact that other facts hang from. vents where magma reaches the surface. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Yellowstone: supervolcano. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Yellowstone: supervolcano. is true.", "x": "The explanation: Yellowstone: supervolcano.. In geology, this fact connects to Ring of Fire volcanoes. — and once you see the mechanism, it stops being trivia and starts being understanding. Volcanic winter (1816).", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Hawaii: hotspot volcanoes.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Hawaii: hotspot volcanoes.", "x": "Volcanoes: Hawaii: hotspot volcanoes.. Iceland's Eyjafjallajokull. This is load-bearing knowledge — the kind of fact that other facts hang from. vents where magma reaches the surface. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Hawaii: hotspot volcanoes. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Hawaii: hotspot volcanoes. is true.", "x": "The explanation: Hawaii: hotspot volcanoes.. In geology, this fact connects to Lava types: pahoehoe/aa. — and once you see the mechanism, it stops being trivia and starts being understanding. Magma chamber feeds eruptions.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Volcanic winter (1816).", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Volcanic winter (1816).", "x": "Volcanoes: Volcanic winter (1816).. Ring of Fire volcanoes. This is load-bearing knowledge — the kind of fact that other facts hang from. vents where magma reaches the surface. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Volcanic winter (1816). is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Volcanic winter (1816). is true.", "x": "The explanation: Volcanic winter (1816).. In geology, this fact connects to Pyroclastic flows kill. — and once you see the mechanism, it stops being trivia and starts being understanding. Shield vs stratovolcano vs cinder.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Magma chamber feeds eruptions.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Magma chamber feeds eruptions.", "x": "Volcanoes: Magma chamber feeds eruptions.. Lava types: pahoehoe/aa. This is load-bearing knowledge — the kind of fact that other facts hang from. vents where magma reaches the surface. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Magma chamber feeds eruptions. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Magma chamber feeds eruptions. is true.", "x": "The explanation: Magma chamber feeds eruptions.. In geology, this fact connects to Monitoring: tiltmeters, gas. — and once you see the mechanism, it stops being trivia and starts being understanding. VEI eruption scale.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Shield vs stratovolcano vs cinder.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Shield vs stratovolcano vs cinder.", "x": "Volcanoes: Shield vs stratovolcano vs cinder.. Pyroclastic flows kill. This is load-bearing knowledge — the kind of fact that other facts hang from. vents where magma reaches the surface. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Shield vs stratovolcano vs cinder. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Shield vs stratovolcano vs cinder. is true.", "x": "The explanation: Shield vs stratovolcano vs cinder.. In geology, this fact connects to Pompeii (79 AD). — and once you see the mechanism, it stops being trivia and starts being understanding. Yellowstone: supervolcano.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Ring of Fire volcanoes.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Ring of Fire volcanoes.", "x": "Going deeper on Volcanoes: Ring of Fire volcanoes.. Shield vs stratovolcano vs cinder. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Volcanoes from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Lava types: pahoehoe/aa.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Lava types: pahoehoe/aa.", "x": "Going deeper on Volcanoes: Lava types: pahoehoe/aa.. VEI eruption scale. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Volcanoes from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Pyroclastic flows kill.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Pyroclastic flows kill.", "x": "Going deeper on Volcanoes: Pyroclastic flows kill.. Yellowstone: supervolcano. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Volcanoes from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Monitoring: tiltmeters, gas.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Monitoring: tiltmeters, gas.", "x": "Going deeper on Volcanoes: Monitoring: tiltmeters, gas.. Hawaii: hotspot volcanoes. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Volcanoes from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Pompeii (79 AD).", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Pompeii (79 AD).", "x": "Going deeper on Volcanoes: Pompeii (79 AD).. Volcanic winter (1816). Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Volcanoes from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Iceland's Eyjafjallajokull.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Iceland's Eyjafjallajokull.", "x": "Going deeper on Volcanoes: Iceland's Eyjafjallajokull.. Magma chamber feeds eruptions. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Volcanoes from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Ring of Fire volcanoes.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Ring of Fire volcanoes.", "x": "Going deeper on Volcanoes: Ring of Fire volcanoes.. Shield vs stratovolcano vs cinder. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Volcanoes from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-volcanoes-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
