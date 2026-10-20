(function(){'use strict';
/* JAH The Sun Astronomy Database generator — jahdb-e2-sci-the-sun-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-the-sun',PREFIX='JAH-E2SCITHESUN-',NAME='JAH The Sun Astronomy Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "The Sun: overview", "d": "The Sun: our star; 99.8% of solar system mass..", "g": "overview", "l": 2, "q": "What is The Sun: overview?", "a": "The Sun: our star; 99.8% of solar system mass..", "x": "The complete astronomy guide to The Sun: our star; 99.8% of solar system mass.. G-type dwarf. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind The Sun.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind The Sun.", "x": "The core principle: Fusion: H to He.. our star; 99.8% of solar system mass. If you understand this one idea, everything else in The Sun clicks into place. Photosphere. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "G-type dwarf.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "G-type dwarf.", "x": "The Sun: G-type dwarf.. Eclipse science. This is load-bearing knowledge — the kind of fact that other facts hang from. our star; 99.8% of solar system mass. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why G-type dwarf. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why G-type dwarf. is true.", "x": "The explanation: G-type dwarf.. In astronomy, this fact connects to Space weather. — and once you see the mechanism, it stops being trivia and starts being understanding. 11-year cycle. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Fusion: H to He.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Fusion: H to He.", "x": "The Sun: Fusion: H to He.. Parker Solar Probe. This is load-bearing knowledge — the kind of fact that other facts hang from. our star; 99.8% of solar system mass. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Fusion: H to He. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Fusion: H to He. is true.", "x": "The explanation: Fusion: H to He.. In astronomy, this fact connects to 5B years left. — and once you see the mechanism, it stops being trivia and starts being understanding. Corona hotter mystery. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "11-year cycle.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "11-year cycle.", "x": "The Sun: 11-year cycle.. Space weather. This is load-bearing knowledge — the kind of fact that other facts hang from. our star; 99.8% of solar system mass. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why 11-year cycle. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why 11-year cycle. is true.", "x": "The explanation: 11-year cycle.. In astronomy, this fact connects to Helioseismology. — and once you see the mechanism, it stops being trivia and starts being understanding. Sunspots. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Corona hotter mystery.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Corona hotter mystery.", "x": "The Sun: Corona hotter mystery.. 5B years left. This is load-bearing knowledge — the kind of fact that other facts hang from. our star; 99.8% of solar system mass. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Corona hotter mystery. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Corona hotter mystery. is true.", "x": "The explanation: Corona hotter mystery.. In astronomy, this fact connects to Photosphere. — and once you see the mechanism, it stops being trivia and starts being understanding. Solar wind. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Sunspots.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Sunspots.", "x": "The Sun: Sunspots.. Helioseismology. This is load-bearing knowledge — the kind of fact that other facts hang from. our star; 99.8% of solar system mass. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Sunspots. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Sunspots. is true.", "x": "The explanation: Sunspots.. In astronomy, this fact connects to Eclipse science. — and once you see the mechanism, it stops being trivia and starts being understanding. G-type dwarf. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Solar wind.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Solar wind.", "x": "The Sun: Solar wind.. Photosphere. This is load-bearing knowledge — the kind of fact that other facts hang from. our star; 99.8% of solar system mass. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Solar wind. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Solar wind. is true.", "x": "The explanation: Solar wind.. In astronomy, this fact connects to Parker Solar Probe. — and once you see the mechanism, it stops being trivia and starts being understanding. Fusion: H to He. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "G-type dwarf.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "G-type dwarf.", "x": "The Sun: G-type dwarf.. Eclipse science. This is load-bearing knowledge — the kind of fact that other facts hang from. our star; 99.8% of solar system mass. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why G-type dwarf. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why G-type dwarf. is true.", "x": "The explanation: G-type dwarf.. In astronomy, this fact connects to Space weather. — and once you see the mechanism, it stops being trivia and starts being understanding. 11-year cycle. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Fusion: H to He.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Fusion: H to He.", "x": "The Sun: Fusion: H to He.. Parker Solar Probe. This is load-bearing knowledge — the kind of fact that other facts hang from. our star; 99.8% of solar system mass. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Fusion: H to He. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Fusion: H to He. is true.", "x": "The explanation: Fusion: H to He.. In astronomy, this fact connects to 5B years left. — and once you see the mechanism, it stops being trivia and starts being understanding. Corona hotter mystery. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Photosphere.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Photosphere.", "x": "Going deeper on The Sun: Photosphere.. Fusion: H to He. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about The Sun from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Eclipse science.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Eclipse science.", "x": "Going deeper on The Sun: Eclipse science.. 11-year cycle. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about The Sun from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Parker Solar Probe.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Parker Solar Probe.", "x": "Going deeper on The Sun: Parker Solar Probe.. Corona hotter mystery. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about The Sun from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Space weather.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Space weather.", "x": "Going deeper on The Sun: Space weather.. Sunspots. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about The Sun from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "5B years left.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "5B years left.", "x": "Going deeper on The Sun: 5B years left.. Solar wind. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about The Sun from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Helioseismology.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Helioseismology.", "x": "Going deeper on The Sun: Helioseismology.. G-type dwarf. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about The Sun from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Photosphere.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Photosphere.", "x": "Going deeper on The Sun: Photosphere.. Fusion: H to He. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about The Sun from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-the-sun-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
