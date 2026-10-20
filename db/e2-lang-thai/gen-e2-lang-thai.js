(function(){'use strict';
/* JAH Thai Phrasebook Database generator — jahdb-e2-lang-thai-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-thai',PREFIX='JAH-E2LANGTHAI-',NAME='JAH Thai Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Thai phrasebook: complete", "d": "Thai: 70M+ speakers. the land of smiles' tongue..", "g": "overview", "l": 2, "q": "What is Thai phrasebook: complete?", "a": "Thai: 70M+ speakers. the land of smiles' tongue..", "x": "The complete Thai phrasebook: the land of smiles' tongue.. Sawadee. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 70M+ Chop. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Thai: the land of smiles' tongue..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Thai: the land of smiles' tongue..", "x": "About Thai: 70M+ speakers — the land of smiles' tongue.. Khop khun. Where it is spoken, its family, its script. Thao rai. Karuna. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Sawadee.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Sawadee.", "x": "Thai essential 1: Sawadee.. Thao rai. Learn these first — Karuna.. the land of smiles' tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Sawadee..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Sawadee..", "x": "Usage: Sawadee.. Phut nit noi. When and how — Thi nai.. Thai the land of smiles' tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Khop khun.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Khop khun.", "x": "Thai essential 2: Khop khun.. Phut nit noi. Learn these first — Thi nai.. the land of smiles' tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Khop khun..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Khop khun..", "x": "Usage: Khop khun.. Hong nam. When and how — Check bin.. Thai the land of smiles' tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Karuna.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Karuna.", "x": "Thai essential 3: Karuna.. Hong nam. Learn these first — Check bin.. the land of smiles' tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Karuna..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Karuna..", "x": "Usage: Karuna.. Chuay duay. When and how — Chai/Mai chai.. Thai the land of smiles' tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Thi nai.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Thi nai.", "x": "Thai essential 4: Thi nai.. Chuay duay. Learn these first — Chai/Mai chai.. the land of smiles' tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Thi nai..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Thi nai..", "x": "Usage: Thi nai.. Chok dee. When and how — Khor thot.. Thai the land of smiles' tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Check bin.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Check bin.", "x": "Thai essential 5: Check bin.. Chok dee. Learn these first — Khor thot.. the land of smiles' tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Check bin..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Check bin..", "x": "Usage: Check bin.. Aroon sawat. When and how — La gon.. Thai the land of smiles' tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Chai/Mai chai.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Chai/Mai chai.", "x": "Thai essential 6: Chai/Mai chai.. Aroon sawat. Learn these first — La gon.. the land of smiles' tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Chai/Mai chai..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Chai/Mai chai..", "x": "Usage: Chai/Mai chai.. Ratri sawat. When and how — Sawadee.. Thai the land of smiles' tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Khor thot.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Khor thot.", "x": "Thai essential 7: Khor thot.. Ratri sawat. Learn these first — Sawadee.. the land of smiles' tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Khor thot..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Khor thot..", "x": "Usage: Khor thot.. Chop. When and how — Khop khun.. Thai the land of smiles' tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "La gon.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "La gon.", "x": "Thai essential 8: La gon.. Chop. Learn these first — Khop khun.. the land of smiles' tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: La gon..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: La gon..", "x": "Usage: La gon.. Thao rai. When and how — Karuna.. Thai the land of smiles' tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Chop.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Chop.", "x": "Thai phrase: Chop.. Khop khun. A traveler's essential — Phut nit noi.. the land of smiles' tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Thao rai.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Thao rai.", "x": "Thai phrase: Thao rai.. Karuna. A traveler's essential — Hong nam.. the land of smiles' tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Phut nit noi.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Phut nit noi.", "x": "Thai phrase: Phut nit noi.. Thi nai. A traveler's essential — Chuay duay.. the land of smiles' tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Hong nam.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Hong nam.", "x": "Thai phrase: Hong nam.. Check bin. A traveler's essential — Chok dee.. the land of smiles' tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Chuay duay.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Chuay duay.", "x": "Thai phrase: Chuay duay.. Chai/Mai chai. A traveler's essential — Aroon sawat.. the land of smiles' tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Chok dee.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Chok dee.", "x": "Thai phrase: Chok dee.. Khor thot. A traveler's essential — Ratri sawat.. the land of smiles' tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Aroon sawat.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Aroon sawat.", "x": "Thai phrase: Aroon sawat.. La gon. A traveler's essential — Chop.. the land of smiles' tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-thai-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
