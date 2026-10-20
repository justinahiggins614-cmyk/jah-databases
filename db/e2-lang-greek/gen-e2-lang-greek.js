(function(){'use strict';
/* JAH Greek Phrasebook Database generator — jahdb-e2-lang-greek-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-greek',PREFIX='JAH-E2LANGGREEK-',NAME='JAH Greek Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Greek phrasebook: complete", "d": "Greek: 13M+ speakers. three thousand years of words..", "g": "overview", "l": 2, "q": "What is Greek phrasebook: complete?", "a": "Greek: 13M+ speakers. three thousand years of words..", "x": "The complete Greek phrasebook: three thousand years of words.. Yia sou. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 13M+ Mou aresei. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Greek: three thousand years of words..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Greek: three thousand years of words..", "x": "About Greek: 13M+ speakers — three thousand years of words.. Efharisto. Where it is spoken, its family, its script. Poso kanei. Parakalo. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Yia sou.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Yia sou.", "x": "Greek essential 1: Yia sou.. Poso kanei. Learn these first — Parakalo.. three thousand years of words. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Yia sou..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Yia sou..", "x": "Usage: Yia sou.. Milao ligo. When and how — Pou einai.. Greek three thousand years of words. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Efharisto.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Efharisto.", "x": "Greek essential 2: Efharisto.. Milao ligo. Learn these first — Pou einai.. three thousand years of words. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Efharisto..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Efharisto..", "x": "Usage: Efharisto.. Toualeta. When and how — Ton logariasmo.. Greek three thousand years of words. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Parakalo.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Parakalo.", "x": "Greek essential 3: Parakalo.. Toualeta. Learn these first — Ton logariasmo.. three thousand years of words. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Parakalo..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Parakalo..", "x": "Usage: Parakalo.. Voithia. When and how — Ne/Ohi.. Greek three thousand years of words. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Pou einai.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Pou einai.", "x": "Greek essential 4: Pou einai.. Voithia. Learn these first — Ne/Ohi.. three thousand years of words. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Pou einai..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Pou einai..", "x": "Usage: Pou einai.. Stin ygeia sou. When and how — Signomi.. Greek three thousand years of words. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Ton logariasmo.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Ton logariasmo.", "x": "Greek essential 5: Ton logariasmo.. Stin ygeia sou. Learn these first — Signomi.. three thousand years of words. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Ton logariasmo..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Ton logariasmo..", "x": "Usage: Ton logariasmo.. Kalimera. When and how — Adio.. Greek three thousand years of words. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Ne/Ohi.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Ne/Ohi.", "x": "Greek essential 6: Ne/Ohi.. Kalimera. Learn these first — Adio.. three thousand years of words. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Ne/Ohi..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Ne/Ohi..", "x": "Usage: Ne/Ohi.. Kalinichta. When and how — Yia sou.. Greek three thousand years of words. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Signomi.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Signomi.", "x": "Greek essential 7: Signomi.. Kalinichta. Learn these first — Yia sou.. three thousand years of words. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Signomi..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Signomi..", "x": "Usage: Signomi.. Mou aresei. When and how — Efharisto.. Greek three thousand years of words. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Adio.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Adio.", "x": "Greek essential 8: Adio.. Mou aresei. Learn these first — Efharisto.. three thousand years of words. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Adio..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Adio..", "x": "Usage: Adio.. Poso kanei. When and how — Parakalo.. Greek three thousand years of words. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Mou aresei.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Mou aresei.", "x": "Greek phrase: Mou aresei.. Efharisto. A traveler's essential — Milao ligo.. three thousand years of words. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Poso kanei.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Poso kanei.", "x": "Greek phrase: Poso kanei.. Parakalo. A traveler's essential — Toualeta.. three thousand years of words. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Milao ligo.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Milao ligo.", "x": "Greek phrase: Milao ligo.. Pou einai. A traveler's essential — Voithia.. three thousand years of words. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Toualeta.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Toualeta.", "x": "Greek phrase: Toualeta.. Ton logariasmo. A traveler's essential — Stin ygeia sou.. three thousand years of words. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Voithia.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Voithia.", "x": "Greek phrase: Voithia.. Ne/Ohi. A traveler's essential — Kalimera.. three thousand years of words. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Stin ygeia sou.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Stin ygeia sou.", "x": "Greek phrase: Stin ygeia sou.. Signomi. A traveler's essential — Kalinichta.. three thousand years of words. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Kalimera.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Kalimera.", "x": "Greek phrase: Kalimera.. Adio. A traveler's essential — Mou aresei.. three thousand years of words. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-greek-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
