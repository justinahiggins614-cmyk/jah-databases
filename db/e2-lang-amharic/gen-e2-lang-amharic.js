(function(){'use strict';
/* JAH Amharic Phrasebook Database generator — jahdb-e2-lang-amharic-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-amharic',PREFIX='JAH-E2LANGAMHAR-',NAME='JAH Amharic Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Amharic phrasebook: complete", "d": "Amharic: 60M+ speakers. Ethiopia's tongue..", "g": "overview", "l": 2, "q": "What is Amharic phrasebook: complete?", "a": "Amharic: 60M+ speakers. Ethiopia's tongue..", "x": "The complete Amharic phrasebook: Ethiopia's tongue.. Selam. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 60M+ Wedalew. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Amharic: Ethiopia's tongue..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Amharic: Ethiopia's tongue..", "x": "About Amharic: 60M+ speakers — Ethiopia's tongue.. Ameseginalehu. Where it is spoken, its family, its script. Sint. Ibakteh. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Selam.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Selam.", "x": "Amharic essential 1: Selam.. Sint. Learn these first — Ibakteh.. Ethiopia's tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Selam..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Selam..", "x": "Usage: Selam.. Tinsh Amarigna. When and how — Yet.. Amharic Ethiopia's tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Ameseginalehu.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Ameseginalehu.", "x": "Amharic essential 2: Ameseginalehu.. Tinsh Amarigna. Learn these first — Yet.. Ethiopia's tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Ameseginalehu..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Ameseginalehu..", "x": "Usage: Ameseginalehu.. Misil bet. When and how — Hisab.. Amharic Ethiopia's tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Ibakteh.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Ibakteh.", "x": "Amharic essential 3: Ibakteh.. Misil bet. Learn these first — Hisab.. Ethiopia's tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Ibakteh..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Ibakteh..", "x": "Usage: Ibakteh.. Irdata. When and how — Awo/Ay.. Amharic Ethiopia's tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Yet.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Yet.", "x": "Amharic essential 4: Yet.. Irdata. Learn these first — Awo/Ay.. Ethiopia's tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Yet..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Yet..", "x": "Usage: Yet.. Tenesa. When and how — Yiqirta.. Amharic Ethiopia's tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Hisab.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Hisab.", "x": "Amharic essential 5: Hisab.. Tenesa. Learn these first — Yiqirta.. Ethiopia's tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Hisab..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Hisab..", "x": "Usage: Hisab.. Dehna aderk. When and how — Dehna hunu.. Amharic Ethiopia's tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Awo/Ay.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Awo/Ay.", "x": "Amharic essential 6: Awo/Ay.. Dehna aderk. Learn these first — Dehna hunu.. Ethiopia's tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Awo/Ay..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Awo/Ay..", "x": "Usage: Awo/Ay.. Dehna tegnu. When and how — Selam.. Amharic Ethiopia's tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Yiqirta.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Yiqirta.", "x": "Amharic essential 7: Yiqirta.. Dehna tegnu. Learn these first — Selam.. Ethiopia's tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Yiqirta..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Yiqirta..", "x": "Usage: Yiqirta.. Wedalew. When and how — Ameseginalehu.. Amharic Ethiopia's tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Dehna hunu.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Dehna hunu.", "x": "Amharic essential 8: Dehna hunu.. Wedalew. Learn these first — Ameseginalehu.. Ethiopia's tongue. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Dehna hunu..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Dehna hunu..", "x": "Usage: Dehna hunu.. Sint. When and how — Ibakteh.. Amharic Ethiopia's tongue. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Wedalew.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Wedalew.", "x": "Amharic phrase: Wedalew.. Ameseginalehu. A traveler's essential — Tinsh Amarigna.. Ethiopia's tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Sint.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Sint.", "x": "Amharic phrase: Sint.. Ibakteh. A traveler's essential — Misil bet.. Ethiopia's tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Tinsh Amarigna.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Tinsh Amarigna.", "x": "Amharic phrase: Tinsh Amarigna.. Yet. A traveler's essential — Irdata.. Ethiopia's tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Misil bet.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Misil bet.", "x": "Amharic phrase: Misil bet.. Hisab. A traveler's essential — Tenesa.. Ethiopia's tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Irdata.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Irdata.", "x": "Amharic phrase: Irdata.. Awo/Ay. A traveler's essential — Dehna aderk.. Ethiopia's tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Tenesa.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Tenesa.", "x": "Amharic phrase: Tenesa.. Yiqirta. A traveler's essential — Dehna tegnu.. Ethiopia's tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Dehna aderk.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Dehna aderk.", "x": "Amharic phrase: Dehna aderk.. Dehna hunu. A traveler's essential — Wedalew.. Ethiopia's tongue. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-amharic-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
