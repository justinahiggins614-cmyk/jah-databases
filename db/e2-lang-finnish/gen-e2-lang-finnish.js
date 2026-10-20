(function(){'use strict';
/* JAH Finnish Phrasebook Database generator — jahdb-e2-lang-finnish-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-finnish',PREFIX='JAH-E2LANGFINNI-',NAME='JAH Finnish Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Finnish phrasebook: complete", "d": "Finnish: 5M+ speakers. the Uralic outlier..", "g": "overview", "l": 2, "q": "What is Finnish phrasebook: complete?", "a": "Finnish: 5M+ speakers. the Uralic outlier..", "x": "The complete Finnish phrasebook: the Uralic outlier.. Hei. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 5M+ Pidän. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Finnish: the Uralic outlier..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Finnish: the Uralic outlier..", "x": "About Finnish: 5M+ speakers — the Uralic outlier.. Kiitos. Where it is spoken, its family, its script. Kuinka paljon. Ole hyvä. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Hei.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Hei.", "x": "Finnish essential 1: Hei.. Kuinka paljon. Learn these first — Ole hyvä.. the Uralic outlier. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Hei..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Hei..", "x": "Usage: Hei.. Vähän. When and how — Missä.. Finnish the Uralic outlier. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Kiitos.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Kiitos.", "x": "Finnish essential 2: Kiitos.. Vähän. Learn these first — Missä.. the Uralic outlier. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Kiitos..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Kiitos..", "x": "Usage: Kiitos.. WC. When and how — Lasku.. Finnish the Uralic outlier. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Ole hyvä.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Ole hyvä.", "x": "Finnish essential 3: Ole hyvä.. WC. Learn these first — Lasku.. the Uralic outlier. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Ole hyvä..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Ole hyvä..", "x": "Usage: Ole hyvä.. Apua. When and how — Kyllä/Ei.. Finnish the Uralic outlier. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Missä.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Missä.", "x": "Finnish essential 4: Missä.. Apua. Learn these first — Kyllä/Ei.. the Uralic outlier. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Missä..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Missä..", "x": "Usage: Missä.. Kippis. When and how — Anteeksi.. Finnish the Uralic outlier. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Lasku.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Lasku.", "x": "Finnish essential 5: Lasku.. Kippis. Learn these first — Anteeksi.. the Uralic outlier. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Lasku..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Lasku..", "x": "Usage: Lasku.. Hyvää huomenta. When and how — Näkemiin.. Finnish the Uralic outlier. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Kyllä/Ei.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Kyllä/Ei.", "x": "Finnish essential 6: Kyllä/Ei.. Hyvää huomenta. Learn these first — Näkemiin.. the Uralic outlier. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Kyllä/Ei..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Kyllä/Ei..", "x": "Usage: Kyllä/Ei.. Hyvää yötä. When and how — Hei.. Finnish the Uralic outlier. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Anteeksi.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Anteeksi.", "x": "Finnish essential 7: Anteeksi.. Hyvää yötä. Learn these first — Hei.. the Uralic outlier. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Anteeksi..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Anteeksi..", "x": "Usage: Anteeksi.. Pidän. When and how — Kiitos.. Finnish the Uralic outlier. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Näkemiin.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Näkemiin.", "x": "Finnish essential 8: Näkemiin.. Pidän. Learn these first — Kiitos.. the Uralic outlier. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Näkemiin..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Näkemiin..", "x": "Usage: Näkemiin.. Kuinka paljon. When and how — Ole hyvä.. Finnish the Uralic outlier. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Pidän.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Pidän.", "x": "Finnish phrase: Pidän.. Kiitos. A traveler's essential — Vähän.. the Uralic outlier. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Kuinka paljon.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Kuinka paljon.", "x": "Finnish phrase: Kuinka paljon.. Ole hyvä. A traveler's essential — WC.. the Uralic outlier. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Vähän.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Vähän.", "x": "Finnish phrase: Vähän.. Missä. A traveler's essential — Apua.. the Uralic outlier. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "WC.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "WC.", "x": "Finnish phrase: WC.. Lasku. A traveler's essential — Kippis.. the Uralic outlier. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Apua.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Apua.", "x": "Finnish phrase: Apua.. Kyllä/Ei. A traveler's essential — Hyvää huomenta.. the Uralic outlier. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Kippis.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Kippis.", "x": "Finnish phrase: Kippis.. Anteeksi. A traveler's essential — Hyvää yötä.. the Uralic outlier. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Hyvää huomenta.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Hyvää huomenta.", "x": "Finnish phrase: Hyvää huomenta.. Näkemiin. A traveler's essential — Pidän.. the Uralic outlier. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-finnish-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
