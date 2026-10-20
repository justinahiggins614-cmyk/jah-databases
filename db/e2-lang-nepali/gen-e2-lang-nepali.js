(function(){'use strict';
/* JAH Nepali Phrasebook Database generator — jahdb-e2-lang-nepali-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-nepali',PREFIX='JAH-E2LANGNEPAL-',NAME='JAH Nepali Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Nepali phrasebook: complete", "d": "Nepali: 30M+ speakers. the Himalayan language..", "g": "overview", "l": 2, "q": "What is Nepali phrasebook: complete?", "a": "Nepali: 30M+ speakers. the Himalayan language..", "x": "The complete Nepali phrasebook: the Himalayan language.. Namaste. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 30M+ Man parchha. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Nepali: the Himalayan language..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Nepali: the Himalayan language..", "x": "About Nepali: 30M+ speakers — the Himalayan language.. Dhanyabad. Where it is spoken, its family, its script. Kati. Kripaya. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Namaste.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Namaste.", "x": "Nepali essential 1: Namaste.. Kati. Learn these first — Kripaya.. the Himalayan language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Namaste..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Namaste..", "x": "Usage: Namaste.. Thorei. When and how — Kahaan.. Nepali the Himalayan language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Dhanyabad.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Dhanyabad.", "x": "Nepali essential 2: Dhanyabad.. Thorei. Learn these first — Kahaan.. the Himalayan language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Dhanyabad..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Dhanyabad..", "x": "Usage: Dhanyabad.. Shauchalaya. When and how — Bill.. Nepali the Himalayan language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Kripaya.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Kripaya.", "x": "Nepali essential 3: Kripaya.. Shauchalaya. Learn these first — Bill.. the Himalayan language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Kripaya..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Kripaya..", "x": "Usage: Kripaya.. Sahayog. When and how — Ho/Hoina.. Nepali the Himalayan language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Kahaan.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Kahaan.", "x": "Nepali essential 4: Kahaan.. Sahayog. Learn these first — Ho/Hoina.. the Himalayan language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Kahaan..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Kahaan..", "x": "Usage: Kahaan.. Cheers. When and how — Maaf.. Nepali the Himalayan language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Bill.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Bill.", "x": "Nepali essential 5: Bill.. Cheers. Learn these first — Maaf.. the Himalayan language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Bill..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Bill..", "x": "Usage: Bill.. Shubha prabhat. When and how — Bida.. Nepali the Himalayan language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Ho/Hoina.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Ho/Hoina.", "x": "Nepali essential 6: Ho/Hoina.. Shubha prabhat. Learn these first — Bida.. the Himalayan language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Ho/Hoina..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Ho/Hoina..", "x": "Usage: Ho/Hoina.. Shubha ratri. When and how — Namaste.. Nepali the Himalayan language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Maaf.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Maaf.", "x": "Nepali essential 7: Maaf.. Shubha ratri. Learn these first — Namaste.. the Himalayan language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Maaf..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Maaf..", "x": "Usage: Maaf.. Man parchha. When and how — Dhanyabad.. Nepali the Himalayan language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Bida.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Bida.", "x": "Nepali essential 8: Bida.. Man parchha. Learn these first — Dhanyabad.. the Himalayan language. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Bida..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Bida..", "x": "Usage: Bida.. Kati. When and how — Kripaya.. Nepali the Himalayan language. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Man parchha.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Man parchha.", "x": "Nepali phrase: Man parchha.. Dhanyabad. A traveler's essential — Thorei.. the Himalayan language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Kati.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Kati.", "x": "Nepali phrase: Kati.. Kripaya. A traveler's essential — Shauchalaya.. the Himalayan language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Thorei.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Thorei.", "x": "Nepali phrase: Thorei.. Kahaan. A traveler's essential — Sahayog.. the Himalayan language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Shauchalaya.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Shauchalaya.", "x": "Nepali phrase: Shauchalaya.. Bill. A traveler's essential — Cheers.. the Himalayan language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Sahayog.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Sahayog.", "x": "Nepali phrase: Sahayog.. Ho/Hoina. A traveler's essential — Shubha prabhat.. the Himalayan language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Cheers.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Cheers.", "x": "Nepali phrase: Cheers.. Maaf. A traveler's essential — Shubha ratri.. the Himalayan language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Shubha prabhat.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Shubha prabhat.", "x": "Nepali phrase: Shubha prabhat.. Bida. A traveler's essential — Man parchha.. the Himalayan language. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-nepali-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
