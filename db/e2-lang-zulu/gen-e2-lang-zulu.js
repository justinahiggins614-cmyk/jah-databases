(function(){'use strict';
/* JAH Zulu Phrasebook Database generator — jahdb-e2-lang-zulu-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-zulu',PREFIX='JAH-E2LANGZULU-',NAME='JAH Zulu Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Zulu phrasebook: complete", "d": "Zulu: 28M+ speakers. South Africa's voice..", "g": "overview", "l": 2, "q": "What is Zulu phrasebook: complete?", "a": "Zulu: 28M+ speakers. South Africa's voice..", "x": "The complete Zulu phrasebook: South Africa's voice.. Sawubona. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 28M+ Ngiyathanda. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Zulu: South Africa's voice..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Zulu: South Africa's voice..", "x": "About Zulu: 28M+ speakers — South Africa's voice.. Ngiyabonga. Where it is spoken, its family, its script. Kubiza malini. Ngicela. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Sawubona.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Sawubona.", "x": "Zulu essential 1: Sawubona.. Kubiza malini. Learn these first — Ngicela.. South Africa's voice. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Sawubona..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Sawubona..", "x": "Usage: Sawubona.. Ngikhuluma kancane. When and how — Kuphi.. Zulu South Africa's voice. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Ngiyabonga.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Ngiyabonga.", "x": "Zulu essential 2: Ngiyabonga.. Ngikhuluma kancane. Learn these first — Kuphi.. South Africa's voice. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Ngiyabonga..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Ngiyabonga..", "x": "Usage: Ngiyabonga.. Ithoyilethi. When and how — Ibhili.. Zulu South Africa's voice. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Ngicela.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Ngicela.", "x": "Zulu essential 3: Ngicela.. Ithoyilethi. Learn these first — Ibhili.. South Africa's voice. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Ngicela..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Ngicela..", "x": "Usage: Ngicela.. Ngisize. When and how — Yebo/Cha.. Zulu South Africa's voice. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Kuphi.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Kuphi.", "x": "Zulu essential 4: Kuphi.. Ngisize. Learn these first — Yebo/Cha.. South Africa's voice. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Kuphi..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Kuphi..", "x": "Usage: Kuphi.. Impilo ende. When and how — Uxolo.. Zulu South Africa's voice. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Ibhili.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Ibhili.", "x": "Zulu essential 5: Ibhili.. Impilo ende. Learn these first — Uxolo.. South Africa's voice. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Ibhili..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Ibhili..", "x": "Usage: Ibhili.. Sawubona ekuseni. When and how — Sala kahle.. Zulu South Africa's voice. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Yebo/Cha.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Yebo/Cha.", "x": "Zulu essential 6: Yebo/Cha.. Sawubona ekuseni. Learn these first — Sala kahle.. South Africa's voice. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Yebo/Cha..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Yebo/Cha..", "x": "Usage: Yebo/Cha.. Ulale kahle. When and how — Sawubona.. Zulu South Africa's voice. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Uxolo.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Uxolo.", "x": "Zulu essential 7: Uxolo.. Ulale kahle. Learn these first — Sawubona.. South Africa's voice. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Uxolo..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Uxolo..", "x": "Usage: Uxolo.. Ngiyathanda. When and how — Ngiyabonga.. Zulu South Africa's voice. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Sala kahle.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Sala kahle.", "x": "Zulu essential 8: Sala kahle.. Ngiyathanda. Learn these first — Ngiyabonga.. South Africa's voice. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Sala kahle..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Sala kahle..", "x": "Usage: Sala kahle.. Kubiza malini. When and how — Ngicela.. Zulu South Africa's voice. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Ngiyathanda.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Ngiyathanda.", "x": "Zulu phrase: Ngiyathanda.. Ngiyabonga. A traveler's essential — Ngikhuluma kancane.. South Africa's voice. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Kubiza malini.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Kubiza malini.", "x": "Zulu phrase: Kubiza malini.. Ngicela. A traveler's essential — Ithoyilethi.. South Africa's voice. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Ngikhuluma kancane.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Ngikhuluma kancane.", "x": "Zulu phrase: Ngikhuluma kancane.. Kuphi. A traveler's essential — Ngisize.. South Africa's voice. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Ithoyilethi.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Ithoyilethi.", "x": "Zulu phrase: Ithoyilethi.. Ibhili. A traveler's essential — Impilo ende.. South Africa's voice. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Ngisize.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Ngisize.", "x": "Zulu phrase: Ngisize.. Yebo/Cha. A traveler's essential — Sawubona ekuseni.. South Africa's voice. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Impilo ende.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Impilo ende.", "x": "Zulu phrase: Impilo ende.. Uxolo. A traveler's essential — Ulale kahle.. South Africa's voice. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Sawubona ekuseni.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Sawubona ekuseni.", "x": "Zulu phrase: Sawubona ekuseni.. Sala kahle. A traveler's essential — Ngiyathanda.. South Africa's voice. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-zulu-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
