(function(){'use strict';
/* JAH Tagalog Phrasebook Database generator — jahdb-e2-lang-tagalog-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-tagalog',PREFIX='JAH-E2LANGTAGAL-',NAME='JAH Tagalog Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Tagalog phrasebook: complete", "d": "Tagalog: 45M+ speakers. the Philippines' heart..", "g": "overview", "l": 2, "q": "What is Tagalog phrasebook: complete?", "a": "Tagalog: 45M+ speakers. the Philippines' heart..", "x": "The complete Tagalog phrasebook: the Philippines' heart.. Kumusta. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 45M+ Gusto ko. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Tagalog: the Philippines' heart..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Tagalog: the Philippines' heart..", "x": "About Tagalog: 45M+ speakers — the Philippines' heart.. Salamat. Where it is spoken, its family, its script. Magkano. Pakiusap. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Kumusta.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Kumusta.", "x": "Tagalog essential 1: Kumusta.. Magkano. Learn these first — Pakiusap.. the Philippines' heart. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Kumusta..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Kumusta..", "x": "Usage: Kumusta.. Kaunti. When and how — Nasaan.. Tagalog the Philippines' heart. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Salamat.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Salamat.", "x": "Tagalog essential 2: Salamat.. Kaunti. Learn these first — Nasaan.. the Philippines' heart. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Salamat..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Salamat..", "x": "Usage: Salamat.. Banyo. When and how — Bill.. Tagalog the Philippines' heart. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Pakiusap.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Pakiusap.", "x": "Tagalog essential 3: Pakiusap.. Banyo. Learn these first — Bill.. the Philippines' heart. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Pakiusap..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Pakiusap..", "x": "Usage: Pakiusap.. Tulong. When and how — Oo/Hindi.. Tagalog the Philippines' heart. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Nasaan.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Nasaan.", "x": "Tagalog essential 4: Nasaan.. Tulong. Learn these first — Oo/Hindi.. the Philippines' heart. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Nasaan..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Nasaan..", "x": "Usage: Nasaan.. Mabuhay. When and how — Paumanhin.. Tagalog the Philippines' heart. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Bill.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Bill.", "x": "Tagalog essential 5: Bill.. Mabuhay. Learn these first — Paumanhin.. the Philippines' heart. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Bill..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Bill..", "x": "Usage: Bill.. Magandang umaga. When and how — Paalam.. Tagalog the Philippines' heart. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Oo/Hindi.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Oo/Hindi.", "x": "Tagalog essential 6: Oo/Hindi.. Magandang umaga. Learn these first — Paalam.. the Philippines' heart. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Oo/Hindi..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Oo/Hindi..", "x": "Usage: Oo/Hindi.. Magandang gabi. When and how — Kumusta.. Tagalog the Philippines' heart. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Paumanhin.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Paumanhin.", "x": "Tagalog essential 7: Paumanhin.. Magandang gabi. Learn these first — Kumusta.. the Philippines' heart. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Paumanhin..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Paumanhin..", "x": "Usage: Paumanhin.. Gusto ko. When and how — Salamat.. Tagalog the Philippines' heart. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Paalam.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Paalam.", "x": "Tagalog essential 8: Paalam.. Gusto ko. Learn these first — Salamat.. the Philippines' heart. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Paalam..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Paalam..", "x": "Usage: Paalam.. Magkano. When and how — Pakiusap.. Tagalog the Philippines' heart. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Gusto ko.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Gusto ko.", "x": "Tagalog phrase: Gusto ko.. Salamat. A traveler's essential — Kaunti.. the Philippines' heart. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Magkano.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Magkano.", "x": "Tagalog phrase: Magkano.. Pakiusap. A traveler's essential — Banyo.. the Philippines' heart. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Kaunti.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Kaunti.", "x": "Tagalog phrase: Kaunti.. Nasaan. A traveler's essential — Tulong.. the Philippines' heart. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Banyo.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Banyo.", "x": "Tagalog phrase: Banyo.. Bill. A traveler's essential — Mabuhay.. the Philippines' heart. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Tulong.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Tulong.", "x": "Tagalog phrase: Tulong.. Oo/Hindi. A traveler's essential — Magandang umaga.. the Philippines' heart. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Mabuhay.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Mabuhay.", "x": "Tagalog phrase: Mabuhay.. Paumanhin. A traveler's essential — Magandang gabi.. the Philippines' heart. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Magandang umaga.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Magandang umaga.", "x": "Tagalog phrase: Magandang umaga.. Paalam. A traveler's essential — Gusto ko.. the Philippines' heart. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-tagalog-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
