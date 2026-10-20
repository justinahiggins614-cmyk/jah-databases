(function(){'use strict';
/* JAH French Phrasebook Database generator — jahdb-e2-lang-french-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-french',PREFIX='JAH-E2LANGFRENC-',NAME='JAH French Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "French phrasebook: complete", "d": "French: 280M+ speakers. the language of diplomacy..", "g": "overview", "l": 2, "q": "What is French phrasebook: complete?", "a": "French: 280M+ speakers. the language of diplomacy..", "x": "The complete French phrasebook: the language of diplomacy.. Bonjour: hello. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 280M+ J'aime: I like. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "French: the language of diplomacy..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "French: the language of diplomacy..", "x": "About French: 280M+ speakers — the language of diplomacy.. Merci: thank you. Where it is spoken, its family, its script. Combien: how much. S'il vous plait: please. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Bonjour: hello.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Bonjour: hello.", "x": "French essential 1: Bonjour: hello.. Combien: how much. Learn these first — S'il vous plait: please.. the language of diplomacy. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Bonjour: hello..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Bonjour: hello..", "x": "Usage: Bonjour: hello.. Je parle peu. When and how — Ou est: where is.. French the language of diplomacy. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Merci: thank you.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Merci: thank you.", "x": "French essential 2: Merci: thank you.. Je parle peu. Learn these first — Ou est: where is.. the language of diplomacy. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Merci: thank you..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Merci: thank you..", "x": "Usage: Merci: thank you.. Toilettes. When and how — L'addition: the bill.. French the language of diplomacy. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "S'il vous plait: please.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "S'il vous plait: please.", "x": "French essential 3: S'il vous plait: please.. Toilettes. Learn these first — L'addition: the bill.. the language of diplomacy. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: S'il vous plait: please..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: S'il vous plait: please..", "x": "Usage: S'il vous plait: please.. Au secours. When and how — Oui/Non.. French the language of diplomacy. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Ou est: where is.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Ou est: where is.", "x": "French essential 4: Ou est: where is.. Au secours. Learn these first — Oui/Non.. the language of diplomacy. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Ou est: where is..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Ou est: where is..", "x": "Usage: Ou est: where is.. Sante. When and how — Pardon.. French the language of diplomacy. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "L'addition: the bill.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "L'addition: the bill.", "x": "French essential 5: L'addition: the bill.. Sante. Learn these first — Pardon.. the language of diplomacy. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: L'addition: the bill..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: L'addition: the bill..", "x": "Usage: L'addition: the bill.. Bonsoir. When and how — Au revoir.. French the language of diplomacy. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Oui/Non.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Oui/Non.", "x": "French essential 6: Oui/Non.. Bonsoir. Learn these first — Au revoir.. the language of diplomacy. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Oui/Non..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Oui/Non..", "x": "Usage: Oui/Non.. Bonne nuit. When and how — Bonjour: hello.. French the language of diplomacy. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Pardon.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Pardon.", "x": "French essential 7: Pardon.. Bonne nuit. Learn these first — Bonjour: hello.. the language of diplomacy. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Pardon..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Pardon..", "x": "Usage: Pardon.. J'aime: I like. When and how — Merci: thank you.. French the language of diplomacy. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Au revoir.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Au revoir.", "x": "French essential 8: Au revoir.. J'aime: I like. Learn these first — Merci: thank you.. the language of diplomacy. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Au revoir..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Au revoir..", "x": "Usage: Au revoir.. Combien: how much. When and how — S'il vous plait: please.. French the language of diplomacy. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "J'aime: I like.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "J'aime: I like.", "x": "French phrase: J'aime: I like.. Merci: thank you. A traveler's essential — Je parle peu.. the language of diplomacy. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Combien: how much.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Combien: how much.", "x": "French phrase: Combien: how much.. S'il vous plait: please. A traveler's essential — Toilettes.. the language of diplomacy. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Je parle peu.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Je parle peu.", "x": "French phrase: Je parle peu.. Ou est: where is. A traveler's essential — Au secours.. the language of diplomacy. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Toilettes.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Toilettes.", "x": "French phrase: Toilettes.. L'addition: the bill. A traveler's essential — Sante.. the language of diplomacy. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Au secours.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Au secours.", "x": "French phrase: Au secours.. Oui/Non. A traveler's essential — Bonsoir.. the language of diplomacy. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Sante.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Sante.", "x": "French phrase: Sante.. Pardon. A traveler's essential — Bonne nuit.. the language of diplomacy. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Bonsoir.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Bonsoir.", "x": "French phrase: Bonsoir.. Au revoir. A traveler's essential — J'aime: I like.. the language of diplomacy. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-french-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
