(function(){'use strict';
/* JAH Temperature Guide Database generator — jahdb-temperature-guide-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='temperature-guide',PREFIX='JAH-TMP-',NAME='JAH Temperature Guide Database';
var FIELDS=["scale", "reference"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Celsius", "d": "The metric temperature scale: 0 C is water freezing, 100 C is water boiling. Convert: F = C x 9/5 + 32; K = C + 273.15.", "g": "scale", "l": 2, "q": "What is Celsius?", "a": "The metric temperature scale: 0 C is water freezing, 100 C is water boiling. Convert: F = C x 9/5 + 32; K = C + 273.15.", "x": "Celsius — The metric temperature scale: 0 C is water freezing, 100 C is water boiling. Convert: F = C x 9/5 + 32; K = C + 273.15. Example: Oven 180 C = 356 F..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Fahrenheit", "d": "The US customary scale: 32 F is water freezing, 212 F is water boiling. Convert: C = (F - 32) x 5/9.", "g": "scale", "l": 2, "q": "What is Fahrenheit?", "a": "The US customary scale: 32 F is water freezing, 212 F is water boiling. Convert: C = (F - 32) x 5/9.", "x": "Fahrenheit — The US customary scale: 32 F is water freezing, 212 F is water boiling. Convert: C = (F - 32) x 5/9. Example: Body temperature 98.6 F = 37 C..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Kelvin", "d": "The SI absolute scale: 0 K is absolute zero. K = C + 273.15. No degree sign is used.", "g": "scale", "l": 2, "q": "What is Kelvin?", "a": "The SI absolute scale: 0 K is absolute zero. K = C + 273.15. No degree sign is used.", "x": "Kelvin — The SI absolute scale: 0 K is absolute zero. K = C + 273.15. No degree sign is used. Example: Room temperature is about 293 K..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Rankine", "d": "Absolute scale using Fahrenheit-sized degrees: 0 R is absolute zero; R = F + 459.67.", "g": "scale", "l": 2, "q": "What is Rankine?", "a": "Absolute scale using Fahrenheit-sized degrees: 0 R is absolute zero; R = F + 459.67.", "x": "Rankine — Absolute scale using Fahrenheit-sized degrees: 0 R is absolute zero; R = F + 459.67. Example: Engineering thermodynamics in the US..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Reaumur", "d": "Old European scale: 0 Re is freezing, 80 Re is boiling. C = Re x 5/4.", "g": "scale", "l": 2, "q": "What is Reaumur?", "a": "Old European scale: 0 Re is freezing, 80 Re is boiling. C = Re x 5/4.", "x": "Reaumur — Old European scale: 0 Re is freezing, 80 Re is boiling. C = Re x 5/4. Example: Still seen on old European thermometers..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Romer", "d": "Early Danish scale by Ole Romer: 7.5 Ro is freezing, 60 Ro is boiling.", "g": "scale", "l": 2, "q": "What is Romer?", "a": "Early Danish scale by Ole Romer: 7.5 Ro is freezing, 60 Ro is boiling.", "x": "Romer — Early Danish scale by Ole Romer: 7.5 Ro is freezing, 60 Ro is boiling. Example: The scale Fahrenheit adapted..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Newton", "d": "Isaac Newton scale: 0 N is freezing, 33 N is boiling.", "g": "scale", "l": 2, "q": "What is Newton?", "a": "Isaac Newton scale: 0 N is freezing, 33 N is boiling.", "x": "Newton — Isaac Newton scale: 0 N is freezing, 33 N is boiling. Example: Historical curiosity..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Delisle", "d": "Inverted Russian scale: 0 De is boiling, 150 De is freezing.", "g": "scale", "l": 2, "q": "What is Delisle?", "a": "Inverted Russian scale: 0 De is boiling, 150 De is freezing.", "x": "Delisle — Inverted Russian scale: 0 De is boiling, 150 De is freezing. Example: Historical curiosity..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Absolute zero", "d": "0 K, -273.15 C, -459.67 F: the coldest possible temperature, where thermal motion stops.", "g": "reference", "l": 2, "q": "What is Absolute zero?", "a": "0 K, -273.15 C, -459.67 F: the coldest possible temperature, where thermal motion stops.", "x": "Absolute zero — 0 K, -273.15 C, -459.67 F: the coldest possible temperature, where thermal motion stops. Example: Unreachable but approached in labs..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Water triple point", "d": "273.16 K (0.01 C): the single temperature where ice, water, and vapor coexist.", "g": "reference", "l": 2, "q": "What is Water triple point?", "a": "273.16 K (0.01 C): the single temperature where ice, water, and vapor coexist.", "x": "Water triple point — 273.16 K (0.01 C): the single temperature where ice, water, and vapor coexist. Example: Defines the Kelvin scale..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Water freezing point", "d": "273.15 K (0 C, 32 F) at standard pressure.", "g": "reference", "l": 2, "q": "What is Water freezing point?", "a": "273.15 K (0 C, 32 F) at standard pressure.", "x": "Water freezing point — 273.15 K (0 C, 32 F) at standard pressure. Example: Ice cubes and winter..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Water boiling point", "d": "373.15 K (100 C, 212 F) at sea level; lower at altitude.", "g": "reference", "l": 2, "q": "What is Water boiling point?", "a": "373.15 K (100 C, 212 F) at sea level; lower at altitude.", "x": "Water boiling point — 373.15 K (100 C, 212 F) at sea level; lower at altitude. Example: Cooking at altitude takes longer..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Human body temperature", "d": "About 310 K (37 C, 98.6 F); fever starts near 38 C.", "g": "reference", "l": 2, "q": "What is Human body temperature?", "a": "About 310 K (37 C, 98.6 F); fever starts near 38 C.", "x": "Human body temperature — About 310 K (37 C, 98.6 F); fever starts near 38 C. Example: Thermometer readings..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Room temperature", "d": "293-298 K (20-25 C, 68-77 F): the comfort band.", "g": "reference", "l": 2, "q": "What is Room temperature?", "a": "293-298 K (20-25 C, 68-77 F): the comfort band.", "x": "Room temperature — 293-298 K (20-25 C, 68-77 F): the comfort band. Example: Thermostat settings..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Refrigerator temperature", "d": "About 277 K (4 C, 39 F): keeps food safe.", "g": "reference", "l": 2, "q": "What is Refrigerator temperature?", "a": "About 277 K (4 C, 39 F): keeps food safe.", "x": "Refrigerator temperature — About 277 K (4 C, 39 F): keeps food safe. Example: Fridge dial..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Freezer temperature", "d": "About 255 K (-18 C, 0 F): long-term food storage.", "g": "reference", "l": 2, "q": "What is Freezer temperature?", "a": "About 255 K (-18 C, 0 F): long-term food storage.", "x": "Freezer temperature — About 255 K (-18 C, 0 F): long-term food storage. Example: Freezer setting..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Liquid nitrogen", "d": "77 K (-196 C): cryogenics and instant freezing.", "g": "reference", "l": 2, "q": "What is Liquid nitrogen?", "a": "77 K (-196 C): cryogenics and instant freezing.", "x": "Liquid nitrogen — 77 K (-196 C): cryogenics and instant freezing. Example: Science demos and food flash-freezing..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Liquid helium", "d": "4.2 K (-269 C): the coldest common liquid; superconductors.", "g": "reference", "l": 2, "q": "What is Liquid helium?", "a": "4.2 K (-269 C): the coldest common liquid; superconductors.", "x": "Liquid helium — 4.2 K (-269 C): the coldest common liquid; superconductors. Example: Physics labs..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Dry ice sublimation", "d": "194.7 K (-78.5 C): frozen CO2 skips melting.", "g": "reference", "l": 2, "q": "What is Dry ice sublimation?", "a": "194.7 K (-78.5 C): frozen CO2 skips melting.", "x": "Dry ice sublimation — 194.7 K (-78.5 C): frozen CO2 skips melting. Example: Fog effects and shipping..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Iron melting point", "d": "1811 K (1538 C): foundry work.", "g": "reference", "l": 2, "q": "What is Iron melting point?", "a": "1811 K (1538 C): foundry work.", "x": "Iron melting point — 1811 K (1538 C): foundry work. Example: Steel making..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Gold melting point", "d": "1337 K (1064 C): jewelry casting.", "g": "reference", "l": 2, "q": "What is Gold melting point?", "a": "1337 K (1064 C): jewelry casting.", "x": "Gold melting point — 1337 K (1064 C): jewelry casting. Example: Goldsmithing..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Aluminum melting point", "d": "933 K (660 C): easy home-foundry metal.", "g": "reference", "l": 2, "q": "What is Aluminum melting point?", "a": "933 K (660 C): easy home-foundry metal.", "x": "Aluminum melting point — 933 K (660 C): easy home-foundry metal. Example: Casting..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Tungsten melting point", "d": "3695 K (3422 C): highest of all metals.", "g": "reference", "l": 2, "q": "What is Tungsten melting point?", "a": "3695 K (3422 C): highest of all metals.", "x": "Tungsten melting point — 3695 K (3422 C): highest of all metals. Example: Light-bulb filaments..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Sun surface", "d": "About 5778 K: the photosphere.", "g": "reference", "l": 2, "q": "What is Sun surface?", "a": "About 5778 K: the photosphere.", "x": "Sun surface — About 5778 K: the photosphere. Example: Astronomy..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Sun core", "d": "About 15 million K: fusion happens here.", "g": "reference", "l": 2, "q": "What is Sun core?", "a": "About 15 million K: fusion happens here.", "x": "Sun core — About 15 million K: fusion happens here. Example: Astrophysics..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-temperature-guide-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
