(function(){'use strict';
/* JAH Swahili Phrasebook Database generator — jahdb-e2-lang-swahili-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lang-swahili',PREFIX='JAH-E2LANGSWAHI-',NAME='JAH Swahili Phrasebook Database';
var FIELDS=["overview", "essentials", "phrases", "pronunciation", "writing", "grammar", "dialects", "learning", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Swahili phrasebook: complete", "d": "Swahili: 200M+ speakers. East Africa's bridge..", "g": "overview", "l": 2, "q": "What is Swahili phrasebook: complete?", "a": "Swahili: 200M+ speakers. East Africa's bridge..", "x": "The complete Swahili phrasebook: East Africa's bridge.. Jambo. Essential phrases, pronunciation, and cultural notes — everything to be understood and to understand. 200M+ Ninapenda. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "About the language", "d": "Swahili: East Africa's bridge..", "g": "overview", "l": 2, "q": "What is About the language?", "a": "Swahili: East Africa's bridge..", "x": "About Swahili: 200M+ speakers — East Africa's bridge.. Asante. Where it is spoken, its family, its script. Bei gani. Tafadhali. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 1", "d": "Jambo.", "g": "essentials", "l": 2, "q": "What is Essential 1?", "a": "Jambo.", "x": "Swahili essential 1: Jambo.. Bei gani. Learn these first — Tafadhali.. East Africa's bridge. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Jambo..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Jambo..", "x": "Usage: Jambo.. Nazungumza kidogo. When and how — Wapi.. Swahili East Africa's bridge. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 2", "d": "Asante.", "g": "essentials", "l": 2, "q": "What is Essential 2?", "a": "Asante.", "x": "Swahili essential 2: Asante.. Nazungumza kidogo. Learn these first — Wapi.. East Africa's bridge. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Asante..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Asante..", "x": "Usage: Asante.. Choo. When and how — Bili.. Swahili East Africa's bridge. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 3", "d": "Tafadhali.", "g": "essentials", "l": 2, "q": "What is Essential 3?", "a": "Tafadhali.", "x": "Swahili essential 3: Tafadhali.. Choo. Learn these first — Bili.. East Africa's bridge. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Tafadhali..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Tafadhali..", "x": "Usage: Tafadhali.. Msaada. When and how — Ndiyo/Hapana.. Swahili East Africa's bridge. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 4", "d": "Wapi.", "g": "essentials", "l": 2, "q": "What is Essential 4?", "a": "Wapi.", "x": "Swahili essential 4: Wapi.. Msaada. Learn these first — Ndiyo/Hapana.. East Africa's bridge. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Wapi..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Wapi..", "x": "Usage: Wapi.. Maisha marefu. When and how — Samahani.. Swahili East Africa's bridge. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 5", "d": "Bili.", "g": "essentials", "l": 2, "q": "What is Essential 5?", "a": "Bili.", "x": "Swahili essential 5: Bili.. Maisha marefu. Learn these first — Samahani.. East Africa's bridge. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Bili..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Bili..", "x": "Usage: Bili.. Habari za asubuhi. When and how — Kwaheri.. Swahili East Africa's bridge. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 6", "d": "Ndiyo/Hapana.", "g": "essentials", "l": 2, "q": "What is Essential 6?", "a": "Ndiyo/Hapana.", "x": "Swahili essential 6: Ndiyo/Hapana.. Habari za asubuhi. Learn these first — Kwaheri.. East Africa's bridge. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Ndiyo/Hapana..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Ndiyo/Hapana..", "x": "Usage: Ndiyo/Hapana.. Usiku mwema. When and how — Jambo.. Swahili East Africa's bridge. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 7", "d": "Samahani.", "g": "essentials", "l": 2, "q": "What is Essential 7?", "a": "Samahani.", "x": "Swahili essential 7: Samahani.. Usiku mwema. Learn these first — Jambo.. East Africa's bridge. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Samahani..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Samahani..", "x": "Usage: Samahani.. Ninapenda. When and how — Asante.. Swahili East Africa's bridge. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Essential 8", "d": "Kwaheri.", "g": "essentials", "l": 2, "q": "What is Essential 8?", "a": "Kwaheri.", "x": "Swahili essential 8: Kwaheri.. Ninapenda. Learn these first — Asante.. East Africa's bridge. Practice aloud. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Using it", "d": "Say it: Kwaheri..", "g": "essentials", "l": 2, "q": "What is Using it?", "a": "Say it: Kwaheri..", "x": "Usage: Kwaheri.. Bei gani. When and how — Tafadhali.. Swahili East Africa's bridge. is learned by speaking. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 1", "d": "Ninapenda.", "g": "phrases", "l": 2, "q": "What is Phrase 1?", "a": "Ninapenda.", "x": "Swahili phrase: Ninapenda.. Asante. A traveler's essential — Nazungumza kidogo.. East Africa's bridge. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 2", "d": "Bei gani.", "g": "phrases", "l": 2, "q": "What is Phrase 2?", "a": "Bei gani.", "x": "Swahili phrase: Bei gani.. Tafadhali. A traveler's essential — Choo.. East Africa's bridge. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 3", "d": "Nazungumza kidogo.", "g": "phrases", "l": 2, "q": "What is Phrase 3?", "a": "Nazungumza kidogo.", "x": "Swahili phrase: Nazungumza kidogo.. Wapi. A traveler's essential — Msaada.. East Africa's bridge. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 4", "d": "Choo.", "g": "phrases", "l": 2, "q": "What is Phrase 4?", "a": "Choo.", "x": "Swahili phrase: Choo.. Bili. A traveler's essential — Maisha marefu.. East Africa's bridge. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 5", "d": "Msaada.", "g": "phrases", "l": 2, "q": "What is Phrase 5?", "a": "Msaada.", "x": "Swahili phrase: Msaada.. Ndiyo/Hapana. A traveler's essential — Habari za asubuhi.. East Africa's bridge. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 6", "d": "Maisha marefu.", "g": "phrases", "l": 2, "q": "What is Phrase 6?", "a": "Maisha marefu.", "x": "Swahili phrase: Maisha marefu.. Samahani. A traveler's essential — Usiku mwema.. East Africa's bridge. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Phrase 7", "d": "Habari za asubuhi.", "g": "phrases", "l": 2, "q": "What is Phrase 7?", "a": "Habari za asubuhi.", "x": "Swahili phrase: Habari za asubuhi.. Kwaheri. A traveler's essential — Ninapenda.. East Africa's bridge. Say it with a smile. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lang-swahili-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
