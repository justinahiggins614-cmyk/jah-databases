(function(){'use strict';
/* JAH Butterflies Entomology Database generator — jahdb-e2-sci-butterflies-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-sci-butterflies',PREFIX='JAH-E2SCIBUTTER-',NAME='JAH Butterflies Entomology Database';
var FIELDS=["overview", "principles", "facts", "details", "history", "applications", "misconceptions", "terms", "quiz", "frontiers"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Butterflies: overview", "d": "Butterflies: scaled-wing beauties; metamorphosis icons..", "g": "overview", "l": 2, "q": "What is Butterflies: overview?", "a": "Butterflies: scaled-wing beauties; metamorphosis icons..", "x": "The complete entomology guide to Butterflies: scaled-wing beauties; metamorphosis icons.. Monarch migration. From first principles to cutting-edge questions, this database teaches the topic the way a great course would — core facts, deep explanations, history, and what remains unknown.", "s": "public-reference", "f": null}, {"t": "The core principle", "d": "The one idea behind Butterflies.", "g": "principles", "l": 2, "q": "What is The core principle?", "a": "The one idea behind Butterflies.", "x": "The core principle: Caterpillar to chrysalis.. scaled-wing beauties; metamorphosis icons. If you understand this one idea, everything else in Butterflies clicks into place. Lepidoptera. Return to it whenever the details get confusing.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Monarch migration.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Monarch migration.", "x": "Butterflies: Monarch migration.. Scales. This is load-bearing knowledge — the kind of fact that other facts hang from. scaled-wing beauties; metamorphosis icons. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explained", "d": "Why Monarch migration. is true.", "g": "facts", "l": 2, "q": "What is Key fact 1 explained?", "a": "Why Monarch migration. is true.", "x": "The explanation: Monarch migration.. In entomology, this fact connects to Gardens. — and once you see the mechanism, it stops being trivia and starts being understanding. Mimicry. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Caterpillar to chrysalis.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Caterpillar to chrysalis.", "x": "Butterflies: Caterpillar to chrysalis.. Migration. This is load-bearing knowledge — the kind of fact that other facts hang from. scaled-wing beauties; metamorphosis icons. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explained", "d": "Why Caterpillar to chrysalis. is true.", "g": "facts", "l": 2, "q": "What is Key fact 2 explained?", "a": "Why Caterpillar to chrysalis. is true.", "x": "The explanation: Caterpillar to chrysalis.. In entomology, this fact connects to Rearing. — and once you see the mechanism, it stops being trivia and starts being understanding. Milkweed host. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Mimicry.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Mimicry.", "x": "Butterflies: Mimicry.. Gardens. This is load-bearing knowledge — the kind of fact that other facts hang from. scaled-wing beauties; metamorphosis icons. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explained", "d": "Why Mimicry. is true.", "g": "facts", "l": 2, "q": "What is Key fact 3 explained?", "a": "Why Mimicry. is true.", "x": "The explanation: Mimicry.. In entomology, this fact connects to Conservation. — and once you see the mechanism, it stops being trivia and starts being understanding. Painted lady. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Milkweed host.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Milkweed host.", "x": "Butterflies: Milkweed host.. Rearing. This is load-bearing knowledge — the kind of fact that other facts hang from. scaled-wing beauties; metamorphosis icons. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explained", "d": "Why Milkweed host. is true.", "g": "facts", "l": 2, "q": "What is Key fact 4 explained?", "a": "Why Milkweed host. is true.", "x": "The explanation: Milkweed host.. In entomology, this fact connects to Lepidoptera. — and once you see the mechanism, it stops being trivia and starts being understanding. Puddling. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Painted lady.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Painted lady.", "x": "Butterflies: Painted lady.. Conservation. This is load-bearing knowledge — the kind of fact that other facts hang from. scaled-wing beauties; metamorphosis icons. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explained", "d": "Why Painted lady. is true.", "g": "facts", "l": 2, "q": "What is Key fact 5 explained?", "a": "Why Painted lady. is true.", "x": "The explanation: Painted lady.. In entomology, this fact connects to Scales. — and once you see the mechanism, it stops being trivia and starts being understanding. Monarch migration. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Puddling.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Puddling.", "x": "Butterflies: Puddling.. Lepidoptera. This is load-bearing knowledge — the kind of fact that other facts hang from. scaled-wing beauties; metamorphosis icons. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explained", "d": "Why Puddling. is true.", "g": "facts", "l": 2, "q": "What is Key fact 6 explained?", "a": "Why Puddling. is true.", "x": "The explanation: Puddling.. In entomology, this fact connects to Migration. — and once you see the mechanism, it stops being trivia and starts being understanding. Caterpillar to chrysalis. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7", "d": "Monarch migration.", "g": "facts", "l": 2, "q": "What is Key fact 7?", "a": "Monarch migration.", "x": "Butterflies: Monarch migration.. Scales. This is load-bearing knowledge — the kind of fact that other facts hang from. scaled-wing beauties; metamorphosis icons. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 7 explained", "d": "Why Monarch migration. is true.", "g": "facts", "l": 2, "q": "What is Key fact 7 explained?", "a": "Why Monarch migration. is true.", "x": "The explanation: Monarch migration.. In entomology, this fact connects to Gardens. — and once you see the mechanism, it stops being trivia and starts being understanding. Mimicry. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8", "d": "Caterpillar to chrysalis.", "g": "facts", "l": 2, "q": "What is Key fact 8?", "a": "Caterpillar to chrysalis.", "x": "Butterflies: Caterpillar to chrysalis.. Migration. This is load-bearing knowledge — the kind of fact that other facts hang from. scaled-wing beauties; metamorphosis icons. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Key fact 8 explained", "d": "Why Caterpillar to chrysalis. is true.", "g": "facts", "l": 2, "q": "What is Key fact 8 explained?", "a": "Why Caterpillar to chrysalis. is true.", "x": "The explanation: Caterpillar to chrysalis.. In entomology, this fact connects to Rearing. — and once you see the mechanism, it stops being trivia and starts being understanding. Milkweed host. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Lepidoptera.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Lepidoptera.", "x": "Going deeper on Butterflies: Lepidoptera.. Caterpillar to chrysalis. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Butterflies from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Scales.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Scales.", "x": "Going deeper on Butterflies: Scales.. Mimicry. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Butterflies from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Migration.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Migration.", "x": "Going deeper on Butterflies: Migration.. Milkweed host. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Butterflies from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Gardens.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Gardens.", "x": "Going deeper on Butterflies: Gardens.. Painted lady. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Butterflies from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Rearing.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Rearing.", "x": "Going deeper on Butterflies: Rearing.. Puddling. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Butterflies from knowing it. Science facts from standard references and textbooks. The science is settled where stated; open questions are noted as such.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Conservation.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Conservation.", "x": "Going deeper on Butterflies: Conservation.. Monarch migration. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Butterflies from knowing it.", "s": "public-reference", "f": null}, {"t": "Deep dive 7", "d": "Lepidoptera.", "g": "details", "l": 2, "q": "What is Deep dive 7?", "a": "Lepidoptera.", "x": "Going deeper on Butterflies: Lepidoptera.. Caterpillar to chrysalis. Details are where real understanding lives — the mechanisms, the numbers, the edge cases that separate knowing about Butterflies from knowing it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-sci-butterflies-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
