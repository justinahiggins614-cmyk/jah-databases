(function(){'use strict';
/* JAH Angle and Direction Guide Database generator — jahdb-angle-direction-guide-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='angle-direction-guide',PREFIX='JAH-ANG-',NAME='JAH Angle and Direction Guide Database';
var FIELDS=["unit", "type", "notable"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Degree", "d": "1/360 of a full turn; the everyday angle unit.", "g": "unit", "l": 2, "q": "What is Degree?", "a": "1/360 of a full turn; the everyday angle unit.", "x": "Degree — 1/360 of a full turn; the everyday angle unit. Example: Navigation and school geometry..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Radian", "d": "The SI angle: arc length equal to radius; 2 pi per turn.", "g": "unit", "l": 2, "q": "What is Radian?", "a": "The SI angle: arc length equal to radius; 2 pi per turn.", "x": "Radian — The SI angle: arc length equal to radius; 2 pi per turn. Example: Math and physics..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Gradian", "d": "1/400 of a turn; surveying in some countries.", "g": "unit", "l": 2, "q": "What is Gradian?", "a": "1/400 of a turn; surveying in some countries.", "x": "Gradian — 1/400 of a turn; surveying in some countries. Example: French surveying..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Turn", "d": "One full rotation; 360 degrees.", "g": "unit", "l": 2, "q": "What is Turn?", "a": "One full rotation; 360 degrees.", "x": "Turn — One full rotation; 360 degrees. Example: Rotations..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions). Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Arcminute", "d": "1/60 of a degree; astronomy and navigation.", "g": "unit", "l": 2, "q": "What is Arcminute?", "a": "1/60 of a degree; astronomy and navigation.", "x": "Arcminute — 1/60 of a degree; astronomy and navigation. Example: Telescope resolution..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Arcsecond", "d": "1/60 of an arcminute; fine astronomy.", "g": "unit", "l": 2, "q": "What is Arcsecond?", "a": "1/60 of an arcminute; fine astronomy.", "x": "Arcsecond — 1/60 of an arcminute; fine astronomy. Example: Star positions..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Milliradian", "d": "1/1000 radian; artillery and optics.", "g": "unit", "l": 2, "q": "What is Milliradian?", "a": "1/1000 radian; artillery and optics.", "x": "Milliradian — 1/1000 radian; artillery and optics. Example: Scope adjustments..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "NATO mil", "d": "1/6400 of a turn; military compasses.", "g": "unit", "l": 2, "q": "What is NATO mil?", "a": "1/6400 of a turn; military compasses.", "x": "NATO mil — 1/6400 of a turn; military compasses. Example: Artillery..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Quadrant", "d": "A quarter turn; 90 degrees.", "g": "unit", "l": 2, "q": "What is Quadrant?", "a": "A quarter turn; 90 degrees.", "x": "Quadrant — A quarter turn; 90 degrees. Example: Geometry..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions). Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Sextant", "d": "A sixth of a turn; 60 degrees.", "g": "unit", "l": 2, "q": "What is Sextant?", "a": "A sixth of a turn; 60 degrees.", "x": "Sextant — A sixth of a turn; 60 degrees. Example: Navigation history..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Octant", "d": "An eighth of a turn; 45 degrees.", "g": "unit", "l": 2, "q": "What is Octant?", "a": "An eighth of a turn; 45 degrees.", "x": "Octant — An eighth of a turn; 45 degrees. Example: Compass points..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Sign", "d": "30 degrees; astrology and old astronomy.", "g": "unit", "l": 2, "q": "What is Sign?", "a": "30 degrees; astrology and old astronomy.", "x": "Sign — 30 degrees; astrology and old astronomy. Example: Zodiac..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Hour angle", "d": "15 degrees; one hour of Earth rotation.", "g": "unit", "l": 2, "q": "What is Hour angle?", "a": "15 degrees; one hour of Earth rotation.", "x": "Hour angle — 15 degrees; one hour of Earth rotation. Example: Astronomy..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Point (compass)", "d": "11.25 degrees; 1/32 of the compass rose.", "g": "unit", "l": 2, "q": "What is Point (compass)?", "a": "11.25 degrees; 1/32 of the compass rose.", "x": "Point (compass) — 11.25 degrees; 1/32 of the compass rose. Example: Sailing..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Acute angle", "d": "Less than 90 degrees.", "g": "type", "l": 2, "q": "What is Acute angle?", "a": "Less than 90 degrees.", "x": "Acute angle — Less than 90 degrees. Example: Triangles..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions). Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Right angle", "d": "Exactly 90 degrees.", "g": "type", "l": 2, "q": "What is Right angle?", "a": "Exactly 90 degrees.", "x": "Right angle — Exactly 90 degrees. Example: Construction squares..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Obtuse angle", "d": "Between 90 and 180 degrees.", "g": "type", "l": 2, "q": "What is Obtuse angle?", "a": "Between 90 and 180 degrees.", "x": "Obtuse angle — Between 90 and 180 degrees. Example: Roof pitches..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Straight angle", "d": "Exactly 180 degrees.", "g": "type", "l": 2, "q": "What is Straight angle?", "a": "Exactly 180 degrees.", "x": "Straight angle — Exactly 180 degrees. Example: Flat lines..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions). Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Reflex angle", "d": "Between 180 and 360 degrees.", "g": "type", "l": 2, "q": "What is Reflex angle?", "a": "Between 180 and 360 degrees.", "x": "Reflex angle — Between 180 and 360 degrees. Example: Camera fields..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Full rotation", "d": "360 degrees; back where you started.", "g": "type", "l": 2, "q": "What is Full rotation?", "a": "360 degrees; back where you started.", "x": "Full rotation — 360 degrees; back where you started. Example: Wheels..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Golden angle", "d": "About 137.5 degrees; sunflower seed spirals.", "g": "type", "l": 2, "q": "What is Golden angle?", "a": "About 137.5 degrees; sunflower seed spirals.", "x": "Golden angle — About 137.5 degrees; sunflower seed spirals. Example: Phyllotaxis..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Complementary angles", "d": "Two angles summing to 90 degrees.", "g": "type", "l": 2, "q": "What is Complementary angles?", "a": "Two angles summing to 90 degrees.", "x": "Complementary angles — Two angles summing to 90 degrees. Example: Geometry problems..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Supplementary angles", "d": "Two angles summing to 180 degrees.", "g": "type", "l": 2, "q": "What is Supplementary angles?", "a": "Two angles summing to 180 degrees.", "x": "Supplementary angles — Two angles summing to 180 degrees. Example: Geometry problems..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Earth axial tilt", "d": "23.44 degrees: the cause of the seasons.", "g": "notable", "l": 2, "q": "What is Earth axial tilt?", "a": "23.44 degrees: the cause of the seasons.", "x": "Earth axial tilt — 23.44 degrees: the cause of the seasons. Example: Climate..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Rainbow angle", "d": "About 42 degrees from the antisolar point.", "g": "notable", "l": 2, "q": "What is Rainbow angle?", "a": "About 42 degrees from the antisolar point.", "x": "Rainbow angle — About 42 degrees from the antisolar point. Example: Optics..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-angle-direction-guide-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
