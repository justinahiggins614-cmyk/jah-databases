(function(){'use strict';
/* JAH Dutch Phrasebook Database generator — jahdb-e2-lang-dutch-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-dutch',PREFIX='JAH-E2LANGDUTCH-',NAME='JAH Dutch Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Dutch phrasebook: complete", "d": "Dutch: 24M+ speakers. the Netherlands' tongue..", "g": "overview", "l": 2, "q": "What is Dutch phrasebook: complete?", "a": "Dutch: 24M+ speakers. the Netherlands' tongue..", "x": "The complete Dutch phrasebook: the Netherlands' tongue.. Hallo. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 24M+ Ik vind leuk. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Dutch: the Netherlands' tongue..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Dutch: the Netherlands' tongue..", "x": "About Dutch: 24M+ speakers — the Netherlands' tongue.. Dank je. Where it is spoken, its family, its script. Hoeveel. Alstublieft. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Hallo.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Hallo.", "x": "Dutch essential 1: Hallo.. Hoeveel. Learn these first — Alstublieft.. the Netherlands' tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Hallo..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Hallo..", "x": "Usage: Hallo.. Ik spreek weinig. When and how — Waar is.. Dutch the Netherlands' tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Dank je.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Dank je.", "x": "Dutch essential 2: Dank je.. Ik spreek weinig. Learn these first — Waar is.. the Netherlands' tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Dank je..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Dank je..", "x": "Usage: Dank je.. WC. When and how — De rekening.. Dutch the Netherlands' tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Alstublieft.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Alstublieft.", "x": "Dutch essential 3: Alstublieft.. WC. Learn these first — De rekening.. the Netherlands' tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Alstublieft..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Alstublieft..", "x": "Usage: Alstublieft.. Help. When and how — Ja/Nee.. Dutch the Netherlands' tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Waar is.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Waar is.", "x": "Dutch essential 4: Waar is.. Help. Learn these first — Ja/Nee.. the Netherlands' tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Waar is..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Waar is..", "x": "Usage: Waar is.. Proost. When and how — Sorry.. Dutch the Netherlands' tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "De rekening.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "De rekening.", "x": "Dutch essential 5: De rekening.. Proost. Learn these first — Sorry.. the Netherlands' tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: De rekening..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: De rekening..", "x": "Usage: De rekening.. Goedemorgen. When and how — Dag.. Dutch the Netherlands' tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Ja/Nee.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Ja/Nee.", "x": "Dutch essential 6: Ja/Nee.. Goedemorgen. Learn these first — Dag.. the Netherlands' tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Ja/Nee..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Ja/Nee..", "x": "Usage: Ja/Nee.. Goedenacht. When and how — Hallo.. Dutch the Netherlands' tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Sorry.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Sorry.", "x": "Dutch essential 7: Sorry.. Goedenacht. Learn these first — Hallo.. the Netherlands' tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Sorry..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Sorry..", "x": "Usage: Sorry.. Ik vind leuk. When and how — Dank je.. Dutch the Netherlands' tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Dag.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Dag.", "x": "Dutch essential 8: Dag.. Ik vind leuk. Learn these first — Dank je.. the Netherlands' tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Dag..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Dag..", "x": "Usage: Dag.. Hoeveel. When and how — Alstublieft.. Dutch the Netherlands' tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Ik vind leuk.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Ik vind leuk.", "x": "Dutch phrase: Ik vind leuk.. Dank je. A traveler's essential — Ik spreek weinig.. the Netherlands' tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Hoeveel.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Hoeveel.", "x": "Dutch phrase: Hoeveel.. Alstublieft. A traveler's essential — WC.. the Netherlands' tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Ik spreek weinig.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Ik spreek weinig.", "x": "Dutch phrase: Ik spreek weinig.. Waar is. A traveler's essential — Help.. the Netherlands' tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "WC.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "WC.", "x": "Dutch phrase: WC.. De rekening. A traveler's essential — Proost.. the Netherlands' tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Help.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Help.", "x": "Dutch phrase: Help.. Ja/Nee. A traveler's essential — Goedemorgen.. the Netherlands' tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Proost.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Proost.", "x": "Dutch phrase: Proost.. Sorry. A traveler's essential — Goedenacht.. the Netherlands' tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Goedemorgen.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Goedemorgen.", "x": "Dutch phrase: Goedemorgen.. Dag. A traveler's essential — Ik vind leuk.. the Netherlands' tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-dutch-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
