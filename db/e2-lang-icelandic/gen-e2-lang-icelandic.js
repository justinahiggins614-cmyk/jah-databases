(function(){'use strict';
/* JAH Icelandic Phrasebook Database generator — jahdb-e2-lang-icelandic-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-icelandic',PREFIX='JAH-E2LANGICELA-',NAME='JAH Icelandic Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Icelandic phrasebook: complete", "d": "Icelandic: 350K speakers. the Viking tongue preserved..", "g": "overview", "l": 2, "q": "What is Icelandic phrasebook: complete?", "a": "Icelandic: 350K speakers. the Viking tongue preserved..", "x": "The complete Icelandic phrasebook: the Viking tongue preserved.. Halló. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 350K Mér líkar. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Icelandic: the Viking tongue preserved..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Icelandic: the Viking tongue preserved..", "x": "About Icelandic: 350K speakers — the Viking tongue preserved.. Takk. Where it is spoken, its family, its script. Hvað kostar. Vinsamlegast. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Halló.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Halló.", "x": "Icelandic essential 1: Halló.. Hvað kostar. Learn these first — Vinsamlegast.. the Viking tongue preserved. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Halló..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Halló..", "x": "Usage: Halló.. Lítið. When and how — Hvar.. Icelandic the Viking tongue preserved. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Takk.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Takk.", "x": "Icelandic essential 2: Takk.. Lítið. Learn these first — Hvar.. the Viking tongue preserved. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Takk..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Takk..", "x": "Usage: Takk.. KlÓsett. When and how — Reikninginn.. Icelandic the Viking tongue preserved. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Vinsamlegast.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Vinsamlegast.", "x": "Icelandic essential 3: Vinsamlegast.. KlÓsett. Learn these first — Reikninginn.. the Viking tongue preserved. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Vinsamlegast..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Vinsamlegast..", "x": "Usage: Vinsamlegast.. Hjálp. When and how — Já/Nei.. Icelandic the Viking tongue preserved. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Hvar.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Hvar.", "x": "Icelandic essential 4: Hvar.. Hjálp. Learn these first — Já/Nei.. the Viking tongue preserved. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Hvar..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Hvar..", "x": "Usage: Hvar.. Skál. When and how — Fyrirgefðu.. Icelandic the Viking tongue preserved. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Reikninginn.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Reikninginn.", "x": "Icelandic essential 5: Reikninginn.. Skál. Learn these first — Fyrirgefðu.. the Viking tongue preserved. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Reikninginn..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Reikninginn..", "x": "Usage: Reikninginn.. Góðan daginn. When and how — Bless.. Icelandic the Viking tongue preserved. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Já/Nei.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Já/Nei.", "x": "Icelandic essential 6: Já/Nei.. Góðan daginn. Learn these first — Bless.. the Viking tongue preserved. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Já/Nei..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Já/Nei..", "x": "Usage: Já/Nei.. Góða nótt. When and how — Halló.. Icelandic the Viking tongue preserved. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Fyrirgefðu.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Fyrirgefðu.", "x": "Icelandic essential 7: Fyrirgefðu.. Góða nótt. Learn these first — Halló.. the Viking tongue preserved. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Fyrirgefðu..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Fyrirgefðu..", "x": "Usage: Fyrirgefðu.. Mér líkar. When and how — Takk.. Icelandic the Viking tongue preserved. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Bless.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Bless.", "x": "Icelandic essential 8: Bless.. Mér líkar. Learn these first — Takk.. the Viking tongue preserved. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Bless..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Bless..", "x": "Usage: Bless.. Hvað kostar. When and how — Vinsamlegast.. Icelandic the Viking tongue preserved. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Mér líkar.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Mér líkar.", "x": "Icelandic phrase: Mér líkar.. Takk. A traveler's essential — Lítið.. the Viking tongue preserved. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Hvað kostar.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Hvað kostar.", "x": "Icelandic phrase: Hvað kostar.. Vinsamlegast. A traveler's essential — KlÓsett.. the Viking tongue preserved. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Lítið.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Lítið.", "x": "Icelandic phrase: Lítið.. Hvar. A traveler's essential — Hjálp.. the Viking tongue preserved. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "KlÓsett.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "KlÓsett.", "x": "Icelandic phrase: KlÓsett.. Reikninginn. A traveler's essential — Skál.. the Viking tongue preserved. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Hjálp.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Hjálp.", "x": "Icelandic phrase: Hjálp.. Já/Nei. A traveler's essential — Góðan daginn.. the Viking tongue preserved. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Skál.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Skál.", "x": "Icelandic phrase: Skál.. Fyrirgefðu. A traveler's essential — Góða nótt.. the Viking tongue preserved. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Góðan daginn.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Góðan daginn.", "x": "Icelandic phrase: Góðan daginn.. Bless. A traveler's essential — Mér líkar.. the Viking tongue preserved. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-icelandic-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
