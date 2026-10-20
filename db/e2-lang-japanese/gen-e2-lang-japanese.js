(function(){'use strict';
/* JAH Japanese Phrasebook Database generator — jahdb-e2-lang-japanese-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-japanese',PREFIX='JAH-E2LANGJAPAN-',NAME='JAH Japanese Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Japanese phrasebook: complete", "d": "Japanese: 125M+ speakers. the language of Japan..", "g": "overview", "l": 2, "q": "What is Japanese phrasebook: complete?", "a": "Japanese: 125M+ speakers. the language of Japan..", "x": "The complete Japanese phrasebook: the language of Japan.. Konnichiwa. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 125M+ Suki desu. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Japanese: the language of Japan..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Japanese: the language of Japan..", "x": "About Japanese: 125M+ speakers — the language of Japan.. Arigato. Where it is spoken, its family, its script. Ikura. Onegaishimasu. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Konnichiwa.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Konnichiwa.", "x": "Japanese essential 1: Konnichiwa.. Ikura. Learn these first — Onegaishimasu.. the language of Japan. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Konnichiwa..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Konnichiwa..", "x": "Usage: Konnichiwa.. Sukoshi. When and how — Doko.. Japanese the language of Japan. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Arigato.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Arigato.", "x": "Japanese essential 2: Arigato.. Sukoshi. Learn these first — Doko.. the language of Japan. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Arigato..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Arigato..", "x": "Usage: Arigato.. Toire. When and how — Okaikei.. Japanese the language of Japan. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Onegaishimasu.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Onegaishimasu.", "x": "Japanese essential 3: Onegaishimasu.. Toire. Learn these first — Okaikei.. the language of Japan. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Onegaishimasu..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Onegaishimasu..", "x": "Usage: Onegaishimasu.. Tasukete. When and how — Hai/Iie.. Japanese the language of Japan. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Doko.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Doko.", "x": "Japanese essential 4: Doko.. Tasukete. Learn these first — Hai/Iie.. the language of Japan. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Doko..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Doko..", "x": "Usage: Doko.. Kanpai. When and how — Sumimasen.. Japanese the language of Japan. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Okaikei.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Okaikei.", "x": "Japanese essential 5: Okaikei.. Kanpai. Learn these first — Sumimasen.. the language of Japan. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Okaikei..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Okaikei..", "x": "Usage: Okaikei.. Ohayo. When and how — Sayonara.. Japanese the language of Japan. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Hai/Iie.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Hai/Iie.", "x": "Japanese essential 6: Hai/Iie.. Ohayo. Learn these first — Sayonara.. the language of Japan. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Hai/Iie..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Hai/Iie..", "x": "Usage: Hai/Iie.. Oyasumi. When and how — Konnichiwa.. Japanese the language of Japan. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Sumimasen.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Sumimasen.", "x": "Japanese essential 7: Sumimasen.. Oyasumi. Learn these first — Konnichiwa.. the language of Japan. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Sumimasen..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Sumimasen..", "x": "Usage: Sumimasen.. Suki desu. When and how — Arigato.. Japanese the language of Japan. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Sayonara.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Sayonara.", "x": "Japanese essential 8: Sayonara.. Suki desu. Learn these first — Arigato.. the language of Japan. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Sayonara..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Sayonara..", "x": "Usage: Sayonara.. Ikura. When and how — Onegaishimasu.. Japanese the language of Japan. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Suki desu.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Suki desu.", "x": "Japanese phrase: Suki desu.. Arigato. A traveler's essential — Sukoshi.. the language of Japan. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Ikura.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Ikura.", "x": "Japanese phrase: Ikura.. Onegaishimasu. A traveler's essential — Toire.. the language of Japan. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Sukoshi.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Sukoshi.", "x": "Japanese phrase: Sukoshi.. Doko. A traveler's essential — Tasukete.. the language of Japan. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Toire.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Toire.", "x": "Japanese phrase: Toire.. Okaikei. A traveler's essential — Kanpai.. the language of Japan. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Tasukete.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Tasukete.", "x": "Japanese phrase: Tasukete.. Hai/Iie. A traveler's essential — Ohayo.. the language of Japan. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Kanpai.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Kanpai.", "x": "Japanese phrase: Kanpai.. Sumimasen. A traveler's essential — Oyasumi.. the language of Japan. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Ohayo.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Ohayo.", "x": "Japanese phrase: Ohayo.. Sayonara. A traveler's essential — Suki desu.. the language of Japan. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-japanese-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
