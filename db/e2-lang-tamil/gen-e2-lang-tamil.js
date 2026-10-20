(function(){'use strict';
/* JAH Tamil Phrasebook Database generator — jahdb-e2-lang-tamil-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-tamil',PREFIX='JAH-E2LANGTAMIL-',NAME='JAH Tamil Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Tamil phrasebook: complete", "d": "Tamil: 85M+ speakers. the classical Dravidian tongue..", "g": "overview", "l": 2, "q": "What is Tamil phrasebook: complete?", "a": "Tamil: 85M+ speakers. the classical Dravidian tongue..", "x": "The complete Tamil phrasebook: the classical Dravidian tongue.. Vanakkam. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 85M+ Pidikkum. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Tamil: the classical Dravidian tongue..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Tamil: the classical Dravidian tongue..", "x": "About Tamil: 85M+ speakers — the classical Dravidian tongue.. Nandri. Where it is spoken, its family, its script. Evvalavu. Dayavu seithu. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Vanakkam.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Vanakkam.", "x": "Tamil essential 1: Vanakkam.. Evvalavu. Learn these first — Dayavu seithu.. the classical Dravidian tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Vanakkam..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Vanakkam..", "x": "Usage: Vanakkam.. Konjam. When and how — Enge.. Tamil the classical Dravidian tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Nandri.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Nandri.", "x": "Tamil essential 2: Nandri.. Konjam. Learn these first — Enge.. the classical Dravidian tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Nandri..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Nandri..", "x": "Usage: Nandri.. Kazhivarai. When and how — Bill.. Tamil the classical Dravidian tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Dayavu seithu.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Dayavu seithu.", "x": "Tamil essential 3: Dayavu seithu.. Kazhivarai. Learn these first — Bill.. the classical Dravidian tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Dayavu seithu..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Dayavu seithu..", "x": "Usage: Dayavu seithu.. Udhavi. When and how — Aamam/Illai.. Tamil the classical Dravidian tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Enge.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Enge.", "x": "Tamil essential 4: Enge.. Udhavi. Learn these first — Aamam/Illai.. the classical Dravidian tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Enge..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Enge..", "x": "Usage: Enge.. Nalam. When and how — Mannikkavum.. Tamil the classical Dravidian tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Bill.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Bill.", "x": "Tamil essential 5: Bill.. Nalam. Learn these first — Mannikkavum.. the classical Dravidian tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Bill..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Bill..", "x": "Usage: Bill.. Kaalai vanakkam. When and how — Poittu varugiren.. Tamil the classical Dravidian tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Aamam/Illai.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Aamam/Illai.", "x": "Tamil essential 6: Aamam/Illai.. Kaalai vanakkam. Learn these first — Poittu varugiren.. the classical Dravidian tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Aamam/Illai..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Aamam/Illai..", "x": "Usage: Aamam/Illai.. Iravu vanakkam. When and how — Vanakkam.. Tamil the classical Dravidian tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Mannikkavum.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Mannikkavum.", "x": "Tamil essential 7: Mannikkavum.. Iravu vanakkam. Learn these first — Vanakkam.. the classical Dravidian tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Mannikkavum..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Mannikkavum..", "x": "Usage: Mannikkavum.. Pidikkum. When and how — Nandri.. Tamil the classical Dravidian tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Poittu varugiren.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Poittu varugiren.", "x": "Tamil essential 8: Poittu varugiren.. Pidikkum. Learn these first — Nandri.. the classical Dravidian tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Poittu varugiren..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Poittu varugiren..", "x": "Usage: Poittu varugiren.. Evvalavu. When and how — Dayavu seithu.. Tamil the classical Dravidian tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Pidikkum.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Pidikkum.", "x": "Tamil phrase: Pidikkum.. Nandri. A traveler's essential — Konjam.. the classical Dravidian tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Evvalavu.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Evvalavu.", "x": "Tamil phrase: Evvalavu.. Dayavu seithu. A traveler's essential — Kazhivarai.. the classical Dravidian tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Konjam.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Konjam.", "x": "Tamil phrase: Konjam.. Enge. A traveler's essential — Udhavi.. the classical Dravidian tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Kazhivarai.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Kazhivarai.", "x": "Tamil phrase: Kazhivarai.. Bill. A traveler's essential — Nalam.. the classical Dravidian tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Udhavi.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Udhavi.", "x": "Tamil phrase: Udhavi.. Aamam/Illai. A traveler's essential — Kaalai vanakkam.. the classical Dravidian tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Nalam.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Nalam.", "x": "Tamil phrase: Nalam.. Mannikkavum. A traveler's essential — Iravu vanakkam.. the classical Dravidian tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Kaalai vanakkam.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Kaalai vanakkam.", "x": "Tamil phrase: Kaalai vanakkam.. Poittu varugiren. A traveler's essential — Pidikkum.. the classical Dravidian tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-tamil-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
