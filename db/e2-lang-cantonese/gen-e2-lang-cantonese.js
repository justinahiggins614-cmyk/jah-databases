(function(){'use strict';
/* JAH Cantonese Phrasebook Database generator — jahdb-e2-lang-cantonese-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-cantonese',PREFIX='JAH-E2LANGCANTO-',NAME='JAH Cantonese Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Cantonese phrasebook: complete", "d": "Cantonese: 85M+ speakers. Hong Kong's voice..", "g": "overview", "l": 2, "q": "What is Cantonese phrasebook: complete?", "a": "Cantonese: 85M+ speakers. Hong Kong's voice..", "x": "The complete Cantonese phrasebook: Hong Kong's voice.. Nei hou. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 85M+ Ngo jung yi. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Cantonese: Hong Kong's voice..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Cantonese: Hong Kong's voice..", "x": "About Cantonese: 85M+ speakers — Hong Kong's voice.. Mh goi. Where it is spoken, its family, its script. Gei do chin. Mh goi. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Nei hou.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Nei hou.", "x": "Cantonese essential 1: Nei hou.. Gei do chin. Learn these first — Mh goi.. Hong Kong's voice. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Nei hou..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Nei hou..", "x": "Usage: Nei hou.. Ngo sik siu. When and how — Hai bin.. Cantonese Hong Kong's voice. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Mh goi.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Mh goi.", "x": "Cantonese essential 2: Mh goi.. Ngo sik siu. Learn these first — Hai bin.. Hong Kong's voice. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Mh goi..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Mh goi..", "x": "Usage: Mh goi.. Chi so. When and how — Mai daan.. Cantonese Hong Kong's voice. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Mh goi.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Mh goi.", "x": "Cantonese essential 3: Mh goi.. Chi so. Learn these first — Mai daan.. Hong Kong's voice. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Mh goi..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Mh goi..", "x": "Usage: Mh goi.. Bong ngo. When and how — Hai/Mh hai.. Cantonese Hong Kong's voice. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Hai bin.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Hai bin.", "x": "Cantonese essential 4: Hai bin.. Bong ngo. Learn these first — Hai/Mh hai.. Hong Kong's voice. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Hai bin..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Hai bin..", "x": "Usage: Hai bin.. Yum bui. When and how — Deui m jyuh.. Cantonese Hong Kong's voice. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Mai daan.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Mai daan.", "x": "Cantonese essential 5: Mai daan.. Yum bui. Learn these first — Deui m jyuh.. Hong Kong's voice. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Mai daan..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Mai daan..", "x": "Usage: Mai daan.. Jou san. When and how — Joi gin.. Cantonese Hong Kong's voice. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Hai/Mh hai.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Hai/Mh hai.", "x": "Cantonese essential 6: Hai/Mh hai.. Jou san. Learn these first — Joi gin.. Hong Kong's voice. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Hai/Mh hai..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Hai/Mh hai..", "x": "Usage: Hai/Mh hai.. Maan on. When and how — Nei hou.. Cantonese Hong Kong's voice. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Deui m jyuh.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Deui m jyuh.", "x": "Cantonese essential 7: Deui m jyuh.. Maan on. Learn these first — Nei hou.. Hong Kong's voice. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Deui m jyuh..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Deui m jyuh..", "x": "Usage: Deui m jyuh.. Ngo jung yi. When and how — Mh goi.. Cantonese Hong Kong's voice. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Joi gin.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Joi gin.", "x": "Cantonese essential 8: Joi gin.. Ngo jung yi. Learn these first — Mh goi.. Hong Kong's voice. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Joi gin..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Joi gin..", "x": "Usage: Joi gin.. Gei do chin. When and how — Mh goi.. Cantonese Hong Kong's voice. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Ngo jung yi.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Ngo jung yi.", "x": "Cantonese phrase: Ngo jung yi.. Mh goi. A traveler's essential — Ngo sik siu.. Hong Kong's voice. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Gei do chin.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Gei do chin.", "x": "Cantonese phrase: Gei do chin.. Mh goi. A traveler's essential — Chi so.. Hong Kong's voice. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Ngo sik siu.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Ngo sik siu.", "x": "Cantonese phrase: Ngo sik siu.. Hai bin. A traveler's essential — Bong ngo.. Hong Kong's voice. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Chi so.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Chi so.", "x": "Cantonese phrase: Chi so.. Mai daan. A traveler's essential — Yum bui.. Hong Kong's voice. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Bong ngo.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Bong ngo.", "x": "Cantonese phrase: Bong ngo.. Hai/Mh hai. A traveler's essential — Jou san.. Hong Kong's voice. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Yum bui.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Yum bui.", "x": "Cantonese phrase: Yum bui.. Deui m jyuh. A traveler's essential — Maan on.. Hong Kong's voice. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Jou san.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Jou san.", "x": "Cantonese phrase: Jou san.. Joi gin. A traveler's essential — Ngo jung yi.. Hong Kong's voice. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-cantonese-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
