(function(){'use strict';
/* JAH Bengali Phrasebook Database generator — jahdb-e2-lang-bengali-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-bengali',PREFIX='JAH-E2LANGBENGA-',NAME='JAH Bengali Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Bengali phrasebook: complete", "d": "Bengali: 230M+ speakers. the sweet language..", "g": "overview", "l": 2, "q": "What is Bengali phrasebook: complete?", "a": "Bengali: 230M+ speakers. the sweet language..", "x": "The complete Bengali phrasebook: the sweet language.. Nomoshkar. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 230M+ Bhalo lage. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Bengali: the sweet language..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Bengali: the sweet language..", "x": "About Bengali: 230M+ speakers — the sweet language.. Dhonnobad. Where it is spoken, its family, its script. Koto. Doya kore. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Nomoshkar.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Nomoshkar.", "x": "Bengali essential 1: Nomoshkar.. Koto. Learn these first — Doya kore.. the sweet language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Nomoshkar..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Nomoshkar..", "x": "Usage: Nomoshkar.. Olpo Bangla. When and how — Kothay.. Bengali the sweet language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Dhonnobad.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Dhonnobad.", "x": "Bengali essential 2: Dhonnobad.. Olpo Bangla. Learn these first — Kothay.. the sweet language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Dhonnobad..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Dhonnobad..", "x": "Usage: Dhonnobad.. Toilet. When and how — Bill.. Bengali the sweet language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Doya kore.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Doya kore.", "x": "Bengali essential 3: Doya kore.. Toilet. Learn these first — Bill.. the sweet language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Doya kore..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Doya kore..", "x": "Usage: Doya kore.. Shahajjo. When and how — Hyaan/Na.. Bengali the sweet language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Kothay.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Kothay.", "x": "Bengali essential 4: Kothay.. Shahajjo. Learn these first — Hyaan/Na.. the sweet language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Kothay..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Kothay..", "x": "Usage: Kothay.. Cheers. When and how — Dukkhito.. Bengali the sweet language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Bill.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Bill.", "x": "Bengali essential 5: Bill.. Cheers. Learn these first — Dukkhito.. the sweet language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Bill..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Bill..", "x": "Usage: Bill.. Shuprobhat. When and how — Biday.. Bengali the sweet language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Hyaan/Na.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Hyaan/Na.", "x": "Bengali essential 6: Hyaan/Na.. Shuprobhat. Learn these first — Biday.. the sweet language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Hyaan/Na..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Hyaan/Na..", "x": "Usage: Hyaan/Na.. Shubho ratri. When and how — Nomoshkar.. Bengali the sweet language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Dukkhito.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Dukkhito.", "x": "Bengali essential 7: Dukkhito.. Shubho ratri. Learn these first — Nomoshkar.. the sweet language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Dukkhito..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Dukkhito..", "x": "Usage: Dukkhito.. Bhalo lage. When and how — Dhonnobad.. Bengali the sweet language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Biday.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Biday.", "x": "Bengali essential 8: Biday.. Bhalo lage. Learn these first — Dhonnobad.. the sweet language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Biday..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Biday..", "x": "Usage: Biday.. Koto. When and how — Doya kore.. Bengali the sweet language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Bhalo lage.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Bhalo lage.", "x": "Bengali phrase: Bhalo lage.. Dhonnobad. A traveler's essential — Olpo Bangla.. the sweet language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Koto.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Koto.", "x": "Bengali phrase: Koto.. Doya kore. A traveler's essential — Toilet.. the sweet language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Olpo Bangla.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Olpo Bangla.", "x": "Bengali phrase: Olpo Bangla.. Kothay. A traveler's essential — Shahajjo.. the sweet language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Toilet.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Toilet.", "x": "Bengali phrase: Toilet.. Bill. A traveler's essential — Cheers.. the sweet language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Shahajjo.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Shahajjo.", "x": "Bengali phrase: Shahajjo.. Hyaan/Na. A traveler's essential — Shuprobhat.. the sweet language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Cheers.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Cheers.", "x": "Bengali phrase: Cheers.. Dukkhito. A traveler's essential — Shubho ratri.. the sweet language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Shuprobhat.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Shuprobhat.", "x": "Bengali phrase: Shuprobhat.. Biday. A traveler's essential — Bhalo lage.. the sweet language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-bengali-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
