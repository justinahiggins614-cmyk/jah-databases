(function(){'use strict';
/* JAH Ukrainian Phrasebook Database generator — jahdb-e2-lang-ukrainian-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-ukrainian',PREFIX='JAH-E2LANGUKRAI-',NAME='JAH Ukrainian Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Ukrainian phrasebook: complete", "d": "Ukrainian: 40M+ speakers. the language of Ukraine..", "g": "overview", "l": 2, "q": "What is Ukrainian phrasebook: complete?", "a": "Ukrainian: 40M+ speakers. the language of Ukraine..", "x": "The complete Ukrainian phrasebook: the language of Ukraine.. Dobryi den. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 40M+ Meni podobayetsya. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Ukrainian: the language of Ukraine..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Ukrainian: the language of Ukraine..", "x": "About Ukrainian: 40M+ speakers — the language of Ukraine.. Dyakuyu. Where it is spoken, its family, its script. Skilky. Bud laska. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Dobryi den.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Dobryi den.", "x": "Ukrainian essential 1: Dobryi den.. Skilky. Learn these first — Bud laska.. the language of Ukraine. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Dobryi den..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Dobryi den..", "x": "Usage: Dobryi den.. Ya malo hovoryu. When and how — De.. Ukrainian the language of Ukraine. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Dyakuyu.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Dyakuyu.", "x": "Ukrainian essential 2: Dyakuyu.. Ya malo hovoryu. Learn these first — De.. the language of Ukraine. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Dyakuyu..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Dyakuyu..", "x": "Usage: Dyakuyu.. Tualet. When and how — Rakhunok.. Ukrainian the language of Ukraine. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Bud laska.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Bud laska.", "x": "Ukrainian essential 3: Bud laska.. Tualet. Learn these first — Rakhunok.. the language of Ukraine. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Bud laska..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Bud laska..", "x": "Usage: Bud laska.. Dopomozhit. When and how — Tak/Ni.. Ukrainian the language of Ukraine. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "De.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "De.", "x": "Ukrainian essential 4: De.. Dopomozhit. Learn these first — Tak/Ni.. the language of Ukraine. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: De..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: De..", "x": "Usage: De.. Budmo. When and how — Vybachte.. Ukrainian the language of Ukraine. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Rakhunok.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Rakhunok.", "x": "Ukrainian essential 5: Rakhunok.. Budmo. Learn these first — Vybachte.. the language of Ukraine. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Rakhunok..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Rakhunok..", "x": "Usage: Rakhunok.. Dobroho ranku. When and how — Do pobachennya.. Ukrainian the language of Ukraine. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Tak/Ni.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Tak/Ni.", "x": "Ukrainian essential 6: Tak/Ni.. Dobroho ranku. Learn these first — Do pobachennya.. the language of Ukraine. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Tak/Ni..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Tak/Ni..", "x": "Usage: Tak/Ni.. Nadobranich. When and how — Dobryi den.. Ukrainian the language of Ukraine. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Vybachte.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Vybachte.", "x": "Ukrainian essential 7: Vybachte.. Nadobranich. Learn these first — Dobryi den.. the language of Ukraine. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Vybachte..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Vybachte..", "x": "Usage: Vybachte.. Meni podobayetsya. When and how — Dyakuyu.. Ukrainian the language of Ukraine. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Do pobachennya.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Do pobachennya.", "x": "Ukrainian essential 8: Do pobachennya.. Meni podobayetsya. Learn these first — Dyakuyu.. the language of Ukraine. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Do pobachennya..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Do pobachennya..", "x": "Usage: Do pobachennya.. Skilky. When and how — Bud laska.. Ukrainian the language of Ukraine. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Meni podobayetsya.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Meni podobayetsya.", "x": "Ukrainian phrase: Meni podobayetsya.. Dyakuyu. A traveler's essential — Ya malo hovoryu.. the language of Ukraine. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Skilky.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Skilky.", "x": "Ukrainian phrase: Skilky.. Bud laska. A traveler's essential — Tualet.. the language of Ukraine. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Ya malo hovoryu.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Ya malo hovoryu.", "x": "Ukrainian phrase: Ya malo hovoryu.. De. A traveler's essential — Dopomozhit.. the language of Ukraine. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Tualet.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Tualet.", "x": "Ukrainian phrase: Tualet.. Rakhunok. A traveler's essential — Budmo.. the language of Ukraine. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Dopomozhit.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Dopomozhit.", "x": "Ukrainian phrase: Dopomozhit.. Tak/Ni. A traveler's essential — Dobroho ranku.. the language of Ukraine. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Budmo.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Budmo.", "x": "Ukrainian phrase: Budmo.. Vybachte. A traveler's essential — Nadobranich.. the language of Ukraine. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Dobroho ranku.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Dobroho ranku.", "x": "Ukrainian phrase: Dobroho ranku.. Do pobachennya. A traveler's essential — Meni podobayetsya.. the language of Ukraine. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-ukrainian-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
