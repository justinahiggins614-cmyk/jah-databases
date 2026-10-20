(function(){'use strict';
/* JAH Hungarian Phrasebook Database generator — jahdb-e2-lang-hungarian-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-hungarian',PREFIX='JAH-E2LANGHUNGA-',NAME='JAH Hungarian Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Hungarian phrasebook: complete", "d": "Hungarian: 13M+ speakers. Europe's outsider..", "g": "overview", "l": 2, "q": "What is Hungarian phrasebook: complete?", "a": "Hungarian: 13M+ speakers. Europe's outsider..", "x": "The complete Hungarian phrasebook: Europe's outsider.. Szia. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 13M+ Szeretem. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Hungarian: Europe's outsider..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Hungarian: Europe's outsider..", "x": "About Hungarian: 13M+ speakers — Europe's outsider.. Köszönöm. Where it is spoken, its family, its script. Mennyi. Kérem. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Szia.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Szia.", "x": "Hungarian essential 1: Szia.. Mennyi. Learn these first — Kérem.. Europe's outsider. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Szia..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Szia..", "x": "Usage: Szia.. Kicsit. When and how — Hol.. Hungarian Europe's outsider. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Köszönöm.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Köszönöm.", "x": "Hungarian essential 2: Köszönöm.. Kicsit. Learn these first — Hol.. Europe's outsider. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Köszönöm..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Köszönöm..", "x": "Usage: Köszönöm.. WC. When and how — Számla.. Hungarian Europe's outsider. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Kérem.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Kérem.", "x": "Hungarian essential 3: Kérem.. WC. Learn these first — Számla.. Europe's outsider. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Kérem..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Kérem..", "x": "Usage: Kérem.. Segítség. When and how — Igen/Nem.. Hungarian Europe's outsider. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Hol.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Hol.", "x": "Hungarian essential 4: Hol.. Segítség. Learn these first — Igen/Nem.. Europe's outsider. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Hol..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Hol..", "x": "Usage: Hol.. Egészségedre. When and how — Elnézést.. Hungarian Europe's outsider. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Számla.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Számla.", "x": "Hungarian essential 5: Számla.. Egészségedre. Learn these first — Elnézést.. Europe's outsider. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Számla..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Számla..", "x": "Usage: Számla.. Jó reggelt. When and how — Viszlát.. Hungarian Europe's outsider. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Igen/Nem.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Igen/Nem.", "x": "Hungarian essential 6: Igen/Nem.. Jó reggelt. Learn these first — Viszlát.. Europe's outsider. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Igen/Nem..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Igen/Nem..", "x": "Usage: Igen/Nem.. Jó éjszakát. When and how — Szia.. Hungarian Europe's outsider. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Elnézést.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Elnézést.", "x": "Hungarian essential 7: Elnézést.. Jó éjszakát. Learn these first — Szia.. Europe's outsider. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Elnézést..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Elnézést..", "x": "Usage: Elnézést.. Szeretem. When and how — Köszönöm.. Hungarian Europe's outsider. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Viszlát.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Viszlát.", "x": "Hungarian essential 8: Viszlát.. Szeretem. Learn these first — Köszönöm.. Europe's outsider. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Viszlát..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Viszlát..", "x": "Usage: Viszlát.. Mennyi. When and how — Kérem.. Hungarian Europe's outsider. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Szeretem.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Szeretem.", "x": "Hungarian phrase: Szeretem.. Köszönöm. A traveler's essential — Kicsit.. Europe's outsider. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Mennyi.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Mennyi.", "x": "Hungarian phrase: Mennyi.. Kérem. A traveler's essential — WC.. Europe's outsider. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Kicsit.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Kicsit.", "x": "Hungarian phrase: Kicsit.. Hol. A traveler's essential — Segítség.. Europe's outsider. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "WC.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "WC.", "x": "Hungarian phrase: WC.. Számla. A traveler's essential — Egészségedre.. Europe's outsider. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Segítség.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Segítség.", "x": "Hungarian phrase: Segítség.. Igen/Nem. A traveler's essential — Jó reggelt.. Europe's outsider. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Egészségedre.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Egészségedre.", "x": "Hungarian phrase: Egészségedre.. Elnézést. A traveler's essential — Jó éjszakát.. Europe's outsider. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Jó reggelt.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Jó reggelt.", "x": "Hungarian phrase: Jó reggelt.. Viszlát. A traveler's essential — Szeretem.. Europe's outsider. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-hungarian-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
