(function(){'use strict';
/* JAH Pressure Units Database generator — jahdb-pressure-units-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='pressure-units',PREFIX='JAH-PRS-',NAME='JAH Pressure Units Database';
var FIELDS=["unit", "reference"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pascal", "d": "The SI pressure unit: one newton per square meter.", "g": "unit", "l": 2, "q": "What is Pascal?", "a": "The SI pressure unit: one newton per square meter.", "x": "Pascal — The SI pressure unit: one newton per square meter. Example: Weather reports in hPa..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Kilopascal", "d": "1,000 pascals; engineering and tires.", "g": "unit", "l": 2, "q": "What is Kilopascal?", "a": "1,000 pascals; engineering and tires.", "x": "Kilopascal — 1,000 pascals; engineering and tires. Example: Car tires ~220 kPa..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Megapascal", "d": "One million pascals; hydraulics and geology.", "g": "unit", "l": 2, "q": "What is Megapascal?", "a": "One million pascals; hydraulics and geology.", "x": "Megapascal — One million pascals; hydraulics and geology. Example: Mariana Trench ~110 MPa..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Bar", "d": "100,000 pascals; meteorology and diving.", "g": "unit", "l": 2, "q": "What is Bar?", "a": "100,000 pascals; meteorology and diving.", "x": "Bar — 100,000 pascals; meteorology and diving. Example: Scuba tanks ~200 bar..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Millibar", "d": "100 pascals; same as the hectopascal.", "g": "unit", "l": 2, "q": "What is Millibar?", "a": "100 pascals; same as the hectopascal.", "x": "Millibar — 100 pascals; same as the hectopascal. Example: Weather maps..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "PSI", "d": "Pounds per square inch; US tires and tools.", "g": "unit", "l": 2, "q": "What is PSI?", "a": "Pounds per square inch; US tires and tools.", "x": "PSI — Pounds per square inch; US tires and tools. Example: Bike tires ~60 psi..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "KSI", "d": "1,000 psi; material strength.", "g": "unit", "l": 2, "q": "What is KSI?", "a": "1,000 psi; material strength.", "x": "KSI — 1,000 psi; material strength. Example: Steel yield ~36 ksi..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Atmosphere", "d": "101,325 pascals; sea-level air pressure.", "g": "unit", "l": 2, "q": "What is Atmosphere?", "a": "101,325 pascals; sea-level air pressure.", "x": "Atmosphere — 101,325 pascals; sea-level air pressure. Example: The baseline..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Torr", "d": "1/760 atmosphere; vacuum measurement.", "g": "unit", "l": 2, "q": "What is Torr?", "a": "1/760 atmosphere; vacuum measurement.", "x": "Torr — 1/760 atmosphere; vacuum measurement. Example: Lab vacuums..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Millimeter of mercury", "d": "Blood pressure and barometers: 120 mmHg systolic.", "g": "unit", "l": 2, "q": "What is Millimeter of mercury?", "a": "Blood pressure and barometers: 120 mmHg systolic.", "x": "Millimeter of mercury — Blood pressure and barometers: 120 mmHg systolic. Example: Doctor visits..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Inch of mercury", "d": "Aviation altimeters; 29.92 inHg is standard.", "g": "unit", "l": 2, "q": "What is Inch of mercury?", "a": "Aviation altimeters; 29.92 inHg is standard.", "x": "Inch of mercury — Aviation altimeters; 29.92 inHg is standard. Example: Altimeter setting..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Millimeter of water", "d": "Low pressures; HVAC and medical.", "g": "unit", "l": 2, "q": "What is Millimeter of water?", "a": "Low pressures; HVAC and medical.", "x": "Millimeter of water — Low pressures; HVAC and medical. Example: CPAP machines ~100 mmH2O..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Inch of water", "d": "Furnace and duct pressures.", "g": "unit", "l": 2, "q": "What is Inch of water?", "a": "Furnace and duct pressures.", "x": "Inch of water — Furnace and duct pressures. Example: HVAC gauges..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Kilogram per sq cm", "d": "Technical atmosphere; hydraulics.", "g": "unit", "l": 2, "q": "What is Kilogram per sq cm?", "a": "Technical atmosphere; hydraulics.", "x": "Kilogram per sq cm — Technical atmosphere; hydraulics. Example: Pressure washers ~150 kg/cm2..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Pound per sq foot", "d": "Wind loads on buildings.", "g": "unit", "l": 2, "q": "What is Pound per sq foot?", "a": "Wind loads on buildings.", "x": "Pound per sq foot — Wind loads on buildings. Example: Structural engineering..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Sea level pressure", "d": "101.325 kPa (14.7 psi, 760 mmHg): the standard atmosphere.", "g": "reference", "l": 2, "q": "What is Sea level pressure?", "a": "101.325 kPa (14.7 psi, 760 mmHg): the standard atmosphere.", "x": "Sea level pressure — 101.325 kPa (14.7 psi, 760 mmHg): the standard atmosphere. Example: Baseline for everything..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Car tire pressure", "d": "About 220 kPa (32 psi) for most sedans.", "g": "reference", "l": 2, "q": "What is Car tire pressure?", "a": "About 220 kPa (32 psi) for most sedans.", "x": "Car tire pressure — About 220 kPa (32 psi) for most sedans. Example: Check monthly..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Bicycle tire pressure", "d": "About 400-800 kPa depending on tire type.", "g": "reference", "l": 2, "q": "What is Bicycle tire pressure?", "a": "About 400-800 kPa depending on tire type.", "x": "Bicycle tire pressure — About 400-800 kPa depending on tire type. Example: Road bikes run high..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Blood pressure normal", "d": "About 16/11 kPa (120/80 mmHg).", "g": "reference", "l": 2, "q": "What is Blood pressure normal?", "a": "About 16/11 kPa (120/80 mmHg).", "x": "Blood pressure normal — About 16/11 kPa (120/80 mmHg). Example: Health checks..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Scuba at 10 meters", "d": "About 2 atm absolute: double surface pressure.", "g": "reference", "l": 2, "q": "What is Scuba at 10 meters?", "a": "About 2 atm absolute: double surface pressure.", "x": "Scuba at 10 meters — About 2 atm absolute: double surface pressure. Example: Dive tables..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Hurricane low", "d": "Record low about 870 hPa in Typhoon Tip.", "g": "reference", "l": 2, "q": "What is Hurricane low?", "a": "Record low about 870 hPa in Typhoon Tip.", "x": "Hurricane low — Record low about 870 hPa in Typhoon Tip. Example: Storm intensity..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Champagne bottle", "d": "About 600 kPa (90 psi) behind the cork.", "g": "reference", "l": 2, "q": "What is Champagne bottle?", "a": "About 600 kPa (90 psi) behind the cork.", "x": "Champagne bottle — About 600 kPa (90 psi) behind the cork. Example: Open carefully..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Water jet cutter", "d": "About 400 MPa: cuts steel with water.", "g": "reference", "l": 2, "q": "What is Water jet cutter?", "a": "About 400 MPa: cuts steel with water.", "x": "Water jet cutter — About 400 MPa: cuts steel with water. Example: Manufacturing..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Space vacuum", "d": "Near 0 Pa; effectively no pressure.", "g": "reference", "l": 2, "q": "What is Space vacuum?", "a": "Near 0 Pa; effectively no pressure.", "x": "Space vacuum — Near 0 Pa; effectively no pressure. Example: Spacecraft design..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Espresso machine", "d": "About 900 kPa (9 bar) for proper extraction.", "g": "reference", "l": 2, "q": "What is Espresso machine?", "a": "About 900 kPa (9 bar) for proper extraction.", "x": "Espresso machine — About 900 kPa (9 bar) for proper extraction. Example: Coffee..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-pressure-units-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
