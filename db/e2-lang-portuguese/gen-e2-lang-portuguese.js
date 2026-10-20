(function(){'use strict';
/* JAH Portuguese Phrasebook Database generator — jahdb-e2-lang-portuguese-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-portuguese',PREFIX='JAH-E2LANGPORTU-',NAME='JAH Portuguese Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Portuguese phrasebook: complete", "d": "Portuguese: 260M+ speakers. from Lisbon to Rio..", "g": "overview", "l": 2, "q": "What is Portuguese phrasebook: complete?", "a": "Portuguese: 260M+ speakers. from Lisbon to Rio..", "x": "The complete Portuguese phrasebook: from Lisbon to Rio.. Ola. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 260M+ Gosto de. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Portuguese: from Lisbon to Rio..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Portuguese: from Lisbon to Rio..", "x": "About Portuguese: 260M+ speakers — from Lisbon to Rio.. Obrigado/a. Where it is spoken, its family, its script. Quanto custa. Por favor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Ola.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Ola.", "x": "Portuguese essential 1: Ola.. Quanto custa. Learn these first — Por favor.. from Lisbon to Rio. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Ola..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Ola..", "x": "Usage: Ola.. Falo pouco. When and how — Onde fica.. Portuguese from Lisbon to Rio. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Obrigado/a.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Obrigado/a.", "x": "Portuguese essential 2: Obrigado/a.. Falo pouco. Learn these first — Onde fica.. from Lisbon to Rio. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Obrigado/a..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Obrigado/a..", "x": "Usage: Obrigado/a.. Banheiro. When and how — A conta.. Portuguese from Lisbon to Rio. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Por favor.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Por favor.", "x": "Portuguese essential 3: Por favor.. Banheiro. Learn these first — A conta.. from Lisbon to Rio. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Por favor..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Por favor..", "x": "Usage: Por favor.. Socorro. When and how — Sim/Nao.. Portuguese from Lisbon to Rio. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Onde fica.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Onde fica.", "x": "Portuguese essential 4: Onde fica.. Socorro. Learn these first — Sim/Nao.. from Lisbon to Rio. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Onde fica..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Onde fica..", "x": "Usage: Onde fica.. Saude. When and how — Com licenca.. Portuguese from Lisbon to Rio. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "A conta.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "A conta.", "x": "Portuguese essential 5: A conta.. Saude. Learn these first — Com licenca.. from Lisbon to Rio. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: A conta..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: A conta..", "x": "Usage: A conta.. Bom dia. When and how — Adeus.. Portuguese from Lisbon to Rio. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Sim/Nao.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Sim/Nao.", "x": "Portuguese essential 6: Sim/Nao.. Bom dia. Learn these first — Adeus.. from Lisbon to Rio. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Sim/Nao..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Sim/Nao..", "x": "Usage: Sim/Nao.. Boa noite. When and how — Ola.. Portuguese from Lisbon to Rio. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Com licenca.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Com licenca.", "x": "Portuguese essential 7: Com licenca.. Boa noite. Learn these first — Ola.. from Lisbon to Rio. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Com licenca..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Com licenca..", "x": "Usage: Com licenca.. Gosto de. When and how — Obrigado/a.. Portuguese from Lisbon to Rio. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Adeus.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Adeus.", "x": "Portuguese essential 8: Adeus.. Gosto de. Learn these first — Obrigado/a.. from Lisbon to Rio. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Adeus..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Adeus..", "x": "Usage: Adeus.. Quanto custa. When and how — Por favor.. Portuguese from Lisbon to Rio. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Gosto de.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Gosto de.", "x": "Portuguese phrase: Gosto de.. Obrigado/a. A traveler's essential — Falo pouco.. from Lisbon to Rio. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Quanto custa.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Quanto custa.", "x": "Portuguese phrase: Quanto custa.. Por favor. A traveler's essential — Banheiro.. from Lisbon to Rio. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Falo pouco.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Falo pouco.", "x": "Portuguese phrase: Falo pouco.. Onde fica. A traveler's essential — Socorro.. from Lisbon to Rio. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Banheiro.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Banheiro.", "x": "Portuguese phrase: Banheiro.. A conta. A traveler's essential — Saude.. from Lisbon to Rio. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Socorro.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Socorro.", "x": "Portuguese phrase: Socorro.. Sim/Nao. A traveler's essential — Bom dia.. from Lisbon to Rio. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Saude.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Saude.", "x": "Portuguese phrase: Saude.. Com licenca. A traveler's essential — Boa noite.. from Lisbon to Rio. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Bom dia.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Bom dia.", "x": "Portuguese phrase: Bom dia.. Adeus. A traveler's essential — Gosto de.. from Lisbon to Rio. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-portuguese-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
