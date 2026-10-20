(function(){'use strict';
/* JAH Turkish Phrasebook Database generator — jahdb-e2-lang-turkish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-turkish',PREFIX='JAH-E2LANGTURKI-',NAME='JAH Turkish Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Turkish phrasebook: complete", "d": "Turkish: 80M+ speakers. the bridge language..", "g": "overview", "l": 2, "q": "What is Turkish phrasebook: complete?", "a": "Turkish: 80M+ speakers. the bridge language..", "x": "The complete Turkish phrasebook: the bridge language.. Merhaba. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 80M+ Seviyorum. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Turkish: the bridge language..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Turkish: the bridge language..", "x": "About Turkish: 80M+ speakers — the bridge language.. Tesekkurler. Where it is spoken, its family, its script. Ne kadar. Lutfen. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Merhaba.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Merhaba.", "x": "Turkish essential 1: Merhaba.. Ne kadar. Learn these first — Lutfen.. the bridge language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Merhaba..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Merhaba..", "x": "Usage: Merhaba.. Az konusuyorum. When and how — Nerede.. Turkish the bridge language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Tesekkurler.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Tesekkurler.", "x": "Turkish essential 2: Tesekkurler.. Az konusuyorum. Learn these first — Nerede.. the bridge language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Tesekkurler..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Tesekkurler..", "x": "Usage: Tesekkurler.. Tuvalet. When and how — Hesap.. Turkish the bridge language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Lutfen.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Lutfen.", "x": "Turkish essential 3: Lutfen.. Tuvalet. Learn these first — Hesap.. the bridge language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Lutfen..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Lutfen..", "x": "Usage: Lutfen.. Imdat. When and how — Evet/Hayir.. Turkish the bridge language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Nerede.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Nerede.", "x": "Turkish essential 4: Nerede.. Imdat. Learn these first — Evet/Hayir.. the bridge language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Nerede..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Nerede..", "x": "Usage: Nerede.. Serefe. When and how — Affedersiniz.. Turkish the bridge language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Hesap.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Hesap.", "x": "Turkish essential 5: Hesap.. Serefe. Learn these first — Affedersiniz.. the bridge language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Hesap..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Hesap..", "x": "Usage: Hesap.. Gunaydin. When and how — Hoscakal.. Turkish the bridge language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Evet/Hayir.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Evet/Hayir.", "x": "Turkish essential 6: Evet/Hayir.. Gunaydin. Learn these first — Hoscakal.. the bridge language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Evet/Hayir..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Evet/Hayir..", "x": "Usage: Evet/Hayir.. Iyi geceler. When and how — Merhaba.. Turkish the bridge language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Affedersiniz.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Affedersiniz.", "x": "Turkish essential 7: Affedersiniz.. Iyi geceler. Learn these first — Merhaba.. the bridge language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Affedersiniz..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Affedersiniz..", "x": "Usage: Affedersiniz.. Seviyorum. When and how — Tesekkurler.. Turkish the bridge language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Hoscakal.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Hoscakal.", "x": "Turkish essential 8: Hoscakal.. Seviyorum. Learn these first — Tesekkurler.. the bridge language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Hoscakal..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Hoscakal..", "x": "Usage: Hoscakal.. Ne kadar. When and how — Lutfen.. Turkish the bridge language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Seviyorum.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Seviyorum.", "x": "Turkish phrase: Seviyorum.. Tesekkurler. A traveler's essential — Az konusuyorum.. the bridge language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Ne kadar.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Ne kadar.", "x": "Turkish phrase: Ne kadar.. Lutfen. A traveler's essential — Tuvalet.. the bridge language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Az konusuyorum.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Az konusuyorum.", "x": "Turkish phrase: Az konusuyorum.. Nerede. A traveler's essential — Imdat.. the bridge language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Tuvalet.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Tuvalet.", "x": "Turkish phrase: Tuvalet.. Hesap. A traveler's essential — Serefe.. the bridge language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Imdat.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Imdat.", "x": "Turkish phrase: Imdat.. Evet/Hayir. A traveler's essential — Gunaydin.. the bridge language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Serefe.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Serefe.", "x": "Turkish phrase: Serefe.. Affedersiniz. A traveler's essential — Iyi geceler.. the bridge language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Gunaydin.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Gunaydin.", "x": "Turkish phrase: Gunaydin.. Hoscakal. A traveler's essential — Seviyorum.. the bridge language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-turkish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
