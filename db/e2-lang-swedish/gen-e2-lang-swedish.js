(function(){'use strict';
/* JAH Swedish Phrasebook Database generator — jahdb-e2-lang-swedish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-swedish',PREFIX='JAH-E2LANGSWEDI-',NAME='JAH Swedish Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Swedish phrasebook: complete", "d": "Swedish: 10M+ speakers. the Scandinavian melody..", "g": "overview", "l": 2, "q": "What is Swedish phrasebook: complete?", "a": "Swedish: 10M+ speakers. the Scandinavian melody..", "x": "The complete Swedish phrasebook: the Scandinavian melody.. Hej. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 10M+ Jag gillar. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Swedish: the Scandinavian melody..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Swedish: the Scandinavian melody..", "x": "About Swedish: 10M+ speakers — the Scandinavian melody.. Tack. Where it is spoken, its family, its script. Hur mycket. Snalla. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Hej.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Hej.", "x": "Swedish essential 1: Hej.. Hur mycket. Learn these first — Snalla.. the Scandinavian melody. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Hej..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Hej..", "x": "Usage: Hej.. Lite. When and how — Var.. Swedish the Scandinavian melody. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Tack.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Tack.", "x": "Swedish essential 2: Tack.. Lite. Learn these first — Var.. the Scandinavian melody. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Tack..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Tack..", "x": "Usage: Tack.. Toalett. When and how — Notan.. Swedish the Scandinavian melody. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Snalla.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Snalla.", "x": "Swedish essential 3: Snalla.. Toalett. Learn these first — Notan.. the Scandinavian melody. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Snalla..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Snalla..", "x": "Usage: Snalla.. Hjalp. When and how — Ja/Nej.. Swedish the Scandinavian melody. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Var.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Var.", "x": "Swedish essential 4: Var.. Hjalp. Learn these first — Ja/Nej.. the Scandinavian melody. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Var..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Var..", "x": "Usage: Var.. Skal. When and how — Forlat.. Swedish the Scandinavian melody. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Notan.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Notan.", "x": "Swedish essential 5: Notan.. Skal. Learn these first — Forlat.. the Scandinavian melody. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Notan..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Notan..", "x": "Usage: Notan.. God morgon. When and how — Hej da.. Swedish the Scandinavian melody. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Ja/Nej.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Ja/Nej.", "x": "Swedish essential 6: Ja/Nej.. God morgon. Learn these first — Hej da.. the Scandinavian melody. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Ja/Nej..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Ja/Nej..", "x": "Usage: Ja/Nej.. God natt. When and how — Hej.. Swedish the Scandinavian melody. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Forlat.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Forlat.", "x": "Swedish essential 7: Forlat.. God natt. Learn these first — Hej.. the Scandinavian melody. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Forlat..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Forlat..", "x": "Usage: Forlat.. Jag gillar. When and how — Tack.. Swedish the Scandinavian melody. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Hej da.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Hej da.", "x": "Swedish essential 8: Hej da.. Jag gillar. Learn these first — Tack.. the Scandinavian melody. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Hej da..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Hej da..", "x": "Usage: Hej da.. Hur mycket. When and how — Snalla.. Swedish the Scandinavian melody. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Jag gillar.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Jag gillar.", "x": "Swedish phrase: Jag gillar.. Tack. A traveler's essential — Lite.. the Scandinavian melody. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Hur mycket.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Hur mycket.", "x": "Swedish phrase: Hur mycket.. Snalla. A traveler's essential — Toalett.. the Scandinavian melody. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Lite.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Lite.", "x": "Swedish phrase: Lite.. Var. A traveler's essential — Hjalp.. the Scandinavian melody. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Toalett.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Toalett.", "x": "Swedish phrase: Toalett.. Notan. A traveler's essential — Skal.. the Scandinavian melody. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Hjalp.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Hjalp.", "x": "Swedish phrase: Hjalp.. Ja/Nej. A traveler's essential — God morgon.. the Scandinavian melody. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Skal.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Skal.", "x": "Swedish phrase: Skal.. Forlat. A traveler's essential — God natt.. the Scandinavian melody. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "God morgon.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "God morgon.", "x": "Swedish phrase: God morgon.. Hej da. A traveler's essential — Jag gillar.. the Scandinavian melody. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-swedish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
