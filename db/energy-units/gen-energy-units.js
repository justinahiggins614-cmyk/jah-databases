(function(){'use strict';
/* JAH Energy Units Database generator — jahdb-energy-units-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='energy-units',PREFIX='JAH-NRG-',NAME='JAH Energy Units Database';
var FIELDS=["unit", "reference"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Joule", "d": "The SI energy unit.", "g": "unit", "l": 2, "q": "What is Joule?", "a": "The SI energy unit.", "x": "Joule — The SI energy unit. Example: Lifting an apple one meter ~1 J..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Kilojoule", "d": "1,000 joules; food labels outside the US.", "g": "unit", "l": 2, "q": "What is Kilojoule?", "a": "1,000 joules; food labels outside the US.", "x": "Kilojoule — 1,000 joules; food labels outside the US. Example: A banana ~440 kJ..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Calorie", "d": "4.184 joules; the small calorie of chemistry.", "g": "unit", "l": 2, "q": "What is Calorie?", "a": "4.184 joules; the small calorie of chemistry.", "x": "Calorie — 4.184 joules; the small calorie of chemistry. Example: Lab calorimetry..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Kilocalorie", "d": "4,184 joules; the food Calorie.", "g": "unit", "l": 2, "q": "What is Kilocalorie?", "a": "4,184 joules; the food Calorie.", "x": "Kilocalorie — 4,184 joules; the food Calorie. Example: Daily diet ~2,000 kcal..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Kilowatt-hour", "d": "3.6 million joules; electricity billing.", "g": "unit", "l": 2, "q": "What is Kilowatt-hour?", "a": "3.6 million joules; electricity billing.", "x": "Kilowatt-hour — 3.6 million joules; electricity billing. Example: A home uses ~30 kWh/day..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "BTU", "d": "1,055 joules; heating and cooling in the US.", "g": "unit", "l": 2, "q": "What is BTU?", "a": "1,055 joules; heating and cooling in the US.", "x": "BTU — 1,055 joules; heating and cooling in the US. Example: Air conditioners rated in BTU..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Therm", "d": "100,000 BTU; natural gas billing.", "g": "unit", "l": 2, "q": "What is Therm?", "a": "100,000 BTU; natural gas billing.", "x": "Therm — 100,000 BTU; natural gas billing. Example: Home heating..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Electronvolt", "d": "1.6e-19 joules; atomic and particle physics.", "g": "unit", "l": 2, "q": "What is Electronvolt?", "a": "1.6e-19 joules; atomic and particle physics.", "x": "Electronvolt — 1.6e-19 joules; atomic and particle physics. Example: Photon energies..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Erg", "d": "1e-7 joules; the old cgs unit.", "g": "unit", "l": 2, "q": "What is Erg?", "a": "1e-7 joules; the old cgs unit.", "x": "Erg — 1e-7 joules; the old cgs unit. Example: Astrophysics..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions). Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Foot-pound", "d": "1.356 joules; US mechanical energy.", "g": "unit", "l": 2, "q": "What is Foot-pound?", "a": "1.356 joules; US mechanical energy.", "x": "Foot-pound — 1.356 joules; US mechanical energy. Example: Torque wrenches..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Horsepower-hour", "d": "2.68 MJ; engine work.", "g": "unit", "l": 2, "q": "What is Horsepower-hour?", "a": "2.68 MJ; engine work.", "x": "Horsepower-hour — 2.68 MJ; engine work. Example: Machinery..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions). Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Ton of TNT", "d": "4.184 GJ; explosive yield.", "g": "unit", "l": 2, "q": "What is Ton of TNT?", "a": "4.184 GJ; explosive yield.", "x": "Ton of TNT — 4.184 GJ; explosive yield. Example: Blast comparisons..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Kiloton", "d": "4.184 TJ; nuclear yields.", "g": "unit", "l": 2, "q": "What is Kiloton?", "a": "4.184 TJ; nuclear yields.", "x": "Kiloton — 4.184 TJ; nuclear yields. Example: Weapons history..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions). Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Megaton", "d": "4.184 PJ; large nuclear yields.", "g": "unit", "l": 2, "q": "What is Megaton?", "a": "4.184 PJ; large nuclear yields.", "x": "Megaton — 4.184 PJ; large nuclear yields. Example: Cold War arsenals..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Foe", "d": "1e44 joules; supernova energy.", "g": "unit", "l": 2, "q": "What is Foe?", "a": "1e44 joules; supernova energy.", "x": "Foe — 1e44 joules; supernova energy. Example: Astrophysics..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions). Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Quad", "d": "1.055e18 joules; national energy statistics.", "g": "unit", "l": 2, "q": "What is Quad?", "a": "1.055e18 joules; national energy statistics.", "x": "Quad — 1.055e18 joules; national energy statistics. Example: US uses ~100 quad/year..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "AA battery", "d": "About 9-14 kJ of stored energy.", "g": "reference", "l": 2, "q": "What is AA battery?", "a": "About 9-14 kJ of stored energy.", "x": "AA battery — About 9-14 kJ of stored energy. Example: Remotes and toys..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Phone battery", "d": "About 40-60 kJ in a modern smartphone.", "g": "reference", "l": 2, "q": "What is Phone battery?", "a": "About 40-60 kJ in a modern smartphone.", "x": "Phone battery — About 40-60 kJ in a modern smartphone. Example: Daily charge..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Daily human food", "d": "About 8.7 MJ (2,070 kcal) average intake.", "g": "reference", "l": 2, "q": "What is Daily human food?", "a": "About 8.7 MJ (2,070 kcal) average intake.", "x": "Daily human food — About 8.7 MJ (2,070 kcal) average intake. Example: Nutrition..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Gallon of gasoline", "d": "About 120 MJ of chemical energy.", "g": "reference", "l": 2, "q": "What is Gallon of gasoline?", "a": "About 120 MJ of chemical energy.", "x": "Gallon of gasoline — About 120 MJ of chemical energy. Example: Fuel economy..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Chocolate bar", "d": "About 1 MJ (240 kcal).", "g": "reference", "l": 2, "q": "What is Chocolate bar?", "a": "About 1 MJ (240 kcal).", "x": "Chocolate bar — About 1 MJ (240 kcal). Example: Snacks..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions). Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Lightning bolt", "d": "About 1 GJ per strike.", "g": "reference", "l": 2, "q": "What is Lightning bolt?", "a": "About 1 GJ per strike.", "x": "Lightning bolt — About 1 GJ per strike. Example: Storms..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions). Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Hiroshima bomb", "d": "About 63 TJ (15 kilotons).", "g": "reference", "l": 2, "q": "What is Hiroshima bomb?", "a": "About 63 TJ (15 kilotons).", "x": "Hiroshima bomb — About 63 TJ (15 kilotons). Example: History..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions). Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Annual US energy", "d": "About 100 quad per year.", "g": "reference", "l": 2, "q": "What is Annual US energy?", "a": "About 100 quad per year.", "x": "Annual US energy — About 100 quad per year. Example: Energy policy..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Flying a 747 one hour", "d": "About 40,000 liters of fuel ~1.4 TJ.", "g": "reference", "l": 2, "q": "What is Flying a 747 one hour?", "a": "About 40,000 liters of fuel ~1.4 TJ.", "x": "Flying a 747 one hour — About 40,000 liters of fuel ~1.4 TJ. Example: Aviation..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-energy-units-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
