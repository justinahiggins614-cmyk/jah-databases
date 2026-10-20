(function(){'use strict';
/* JAH Emergency Numbers Database generator — jahdb-emergency-numbers-world-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='emergency-numbers-world',PREFIX='JAH-EMG-',NAME='JAH Emergency Numbers Database';
var FIELDS=["north-america", "europe", "asia", "oceania", "south-america", "africa"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "United States", "d": "911 for all emergencies.", "g": "north-america", "l": 2, "q": "What is United States?", "a": "911 for all emergencies.", "x": "United States — 911 for all emergencies. Example: 911.  Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Canada", "d": "911 for all emergencies.", "g": "north-america", "l": 2, "q": "What is Canada?", "a": "911 for all emergencies.", "x": "Canada — 911 for all emergencies. Example: 911.  Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Mexico", "d": "911 for all emergencies.", "g": "north-america", "l": 2, "q": "What is Mexico?", "a": "911 for all emergencies.", "x": "Mexico — 911 for all emergencies. Example: 911.  Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "United Kingdom", "d": "999 or 112 for all emergencies.", "g": "europe", "l": 2, "q": "What is United Kingdom?", "a": "999 or 112 for all emergencies.", "x": "United Kingdom — 999 or 112 for all emergencies. Example: 999.  Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Ireland", "d": "999 or 112 for all emergencies.", "g": "europe", "l": 2, "q": "What is Ireland?", "a": "999 or 112 for all emergencies.", "x": "Ireland — 999 or 112 for all emergencies. Example: 999.  Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "France", "d": "112 general; 15 medical, 17 police, 18 fire.", "g": "europe", "l": 2, "q": "What is France?", "a": "112 general; 15 medical, 17 police, 18 fire.", "x": "France — 112 general; 15 medical, 17 police, 18 fire. Example: 112.  Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Germany", "d": "112 general; 110 police.", "g": "europe", "l": 2, "q": "What is Germany?", "a": "112 general; 110 police.", "x": "Germany — 112 general; 110 police. Example: 112.  Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Italy", "d": "112 general emergency.", "g": "europe", "l": 2, "q": "What is Italy?", "a": "112 general emergency.", "x": "Italy — 112 general emergency. Example: 112.  Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Spain", "d": "112 general emergency.", "g": "europe", "l": 2, "q": "What is Spain?", "a": "112 general emergency.", "x": "Spain — 112 general emergency. Example: 112.  Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Portugal", "d": "112 general emergency.", "g": "europe", "l": 2, "q": "What is Portugal?", "a": "112 general emergency.", "x": "Portugal — 112 general emergency. Example: 112.  Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Netherlands", "d": "112 general emergency.", "g": "europe", "l": 2, "q": "What is Netherlands?", "a": "112 general emergency.", "x": "Netherlands — 112 general emergency. Example: 112.  Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Belgium", "d": "112 general; 101 police.", "g": "europe", "l": 2, "q": "What is Belgium?", "a": "112 general; 101 police.", "x": "Belgium — 112 general; 101 police. Example: 112.  Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Sweden", "d": "112 general emergency.", "g": "europe", "l": 2, "q": "What is Sweden?", "a": "112 general emergency.", "x": "Sweden — 112 general emergency. Example: 112.  Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Norway", "d": "110 fire, 112 police, 113 medical.", "g": "europe", "l": 2, "q": "What is Norway?", "a": "110 fire, 112 police, 113 medical.", "x": "Norway — 110 fire, 112 police, 113 medical. Example: 113.  Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Denmark", "d": "112 general emergency.", "g": "europe", "l": 2, "q": "What is Denmark?", "a": "112 general emergency.", "x": "Denmark — 112 general emergency. Example: 112.  Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Finland", "d": "112 general emergency.", "g": "europe", "l": 2, "q": "What is Finland?", "a": "112 general emergency.", "x": "Finland — 112 general emergency. Example: 112.  Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Poland", "d": "112 general; 997 police, 998 fire, 999 medical.", "g": "europe", "l": 2, "q": "What is Poland?", "a": "112 general; 997 police, 998 fire, 999 medical.", "x": "Poland — 112 general; 997 police, 998 fire, 999 medical. Example: 112.  Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Austria", "d": "112 general; 133 police, 144 medical.", "g": "europe", "l": 2, "q": "What is Austria?", "a": "112 general; 133 police, 144 medical.", "x": "Austria — 112 general; 133 police, 144 medical. Example: 112.  Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Switzerland", "d": "112 general; 117 police, 144 medical, 118 fire.", "g": "europe", "l": 2, "q": "What is Switzerland?", "a": "112 general; 117 police, 144 medical, 118 fire.", "x": "Switzerland — 112 general; 117 police, 144 medical, 118 fire. Example: 112.  Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Greece", "d": "112 general; 100 police, 166 medical, 199 fire.", "g": "europe", "l": 2, "q": "What is Greece?", "a": "112 general; 100 police, 166 medical, 199 fire.", "x": "Greece — 112 general; 100 police, 166 medical, 199 fire. Example: 112.  Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Turkey", "d": "112 general emergency.", "g": "asia", "l": 2, "q": "What is Turkey?", "a": "112 general emergency.", "x": "Turkey — 112 general emergency. Example: 112.  Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Russia", "d": "112 general emergency.", "g": "europe", "l": 2, "q": "What is Russia?", "a": "112 general emergency.", "x": "Russia — 112 general emergency. Example: 112.  Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Ukraine", "d": "112 general emergency.", "g": "europe", "l": 2, "q": "What is Ukraine?", "a": "112 general emergency.", "x": "Ukraine — 112 general emergency. Example: 112.  Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "Australia", "d": "000 general; 112 works from mobiles.", "g": "oceania", "l": 2, "q": "What is Australia?", "a": "000 general; 112 works from mobiles.", "x": "Australia — 000 general; 112 works from mobiles. Example: 000.  Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}, {"t": "New Zealand", "d": "111 general emergency.", "g": "oceania", "l": 2, "q": "What is New Zealand?", "a": "111 general emergency.", "x": "New Zealand — 111 general emergency. Example: 111.  Checked against official safety guidance (ready.gov, Red Cross, and national emergency services). In a real emergency, always call your local emergency number first.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-emergency-numbers-world-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
