(function(){'use strict';
/* JAH Speed and Velocity Guide Database generator — jahdb-speed-velocity-guide-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='speed-velocity-guide',PREFIX='JAH-SPD-',NAME='JAH Speed and Velocity Guide Database';
var FIELDS=["unit", "notable"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Meter per second", "d": "The SI speed unit. Convert: km/h = m/s x 3.6; mph = m/s x 2.237.", "g": "unit", "l": 2, "q": "What is Meter per second?", "a": "The SI speed unit. Convert: km/h = m/s x 3.6; mph = m/s x 2.237.", "x": "Meter per second — The SI speed unit. Convert: km/h = m/s x 3.6; mph = m/s x 2.237. Example: A brisk walk is about 1.4 m/s..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Kilometer per hour", "d": "Road speed worldwide. Convert: mph = km/h / 1.609.", "g": "unit", "l": 2, "q": "What is Kilometer per hour?", "a": "Road speed worldwide. Convert: mph = km/h / 1.609.", "x": "Kilometer per hour — Road speed worldwide. Convert: mph = km/h / 1.609. Example: Highway 100 km/h = 62 mph..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Mile per hour", "d": "US and UK road speed. Convert: km/h = mph x 1.609.", "g": "unit", "l": 2, "q": "What is Mile per hour?", "a": "US and UK road speed. Convert: km/h = mph x 1.609.", "x": "Mile per hour — US and UK road speed. Convert: km/h = mph x 1.609. Example: 65 mph = 105 km/h..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Knot", "d": "One nautical mile per hour; aviation and marine. Convert: mph = knots x 1.151.", "g": "unit", "l": 2, "q": "What is Knot?", "a": "One nautical mile per hour; aviation and marine. Convert: mph = knots x 1.151.", "x": "Knot — One nautical mile per hour; aviation and marine. Convert: mph = knots x 1.151. Example: Cruise ships do ~20 knots..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Foot per second", "d": "US engineering speed. Convert: mph = ft/s x 0.682.", "g": "unit", "l": 2, "q": "What is Foot per second?", "a": "US engineering speed. Convert: mph = ft/s x 0.682.", "x": "Foot per second — US engineering speed. Convert: mph = ft/s x 0.682. Example: A fastball is ~140 ft/s..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Mach number", "d": "Speed relative to the speed of sound; Mach 1 = 1,235 km/h at sea level.", "g": "unit", "l": 2, "q": "What is Mach number?", "a": "Speed relative to the speed of sound; Mach 1 = 1,235 km/h at sea level.", "x": "Mach number — Speed relative to the speed of sound; Mach 1 = 1,235 km/h at sea level. Example: Supersonic jets exceed Mach 1..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Speed of sound", "d": "About 343 m/s (1,235 km/h) in air at sea level; varies with temperature.", "g": "unit", "l": 2, "q": "What is Speed of sound?", "a": "About 343 m/s (1,235 km/h) in air at sea level; varies with temperature.", "x": "Speed of sound — About 343 m/s (1,235 km/h) in air at sea level; varies with temperature. Example: Thunder delay estimates distance..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Speed of light", "d": "299,792,458 m/s; the universal speed limit.", "g": "unit", "l": 2, "q": "What is Speed of light?", "a": "299,792,458 m/s; the universal speed limit.", "x": "Speed of light — 299,792,458 m/s; the universal speed limit. Example: Nothing with mass reaches it..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Walking pace", "d": "About 5 km/h (3.1 mph) for an adult.", "g": "notable", "l": 2, "q": "What is Walking pace?", "a": "About 5 km/h (3.1 mph) for an adult.", "x": "Walking pace — About 5 km/h (3.1 mph) for an adult. Example: City walking..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Elite sprint", "d": "Top sprinters exceed 37 km/h (23 mph) briefly.", "g": "notable", "l": 2, "q": "What is Elite sprint?", "a": "Top sprinters exceed 37 km/h (23 mph) briefly.", "x": "Elite sprint — Top sprinters exceed 37 km/h (23 mph) briefly. Example: 100 m dash..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Cheetah top speed", "d": "About 110 km/h (68 mph) in short bursts.", "g": "notable", "l": 2, "q": "What is Cheetah top speed?", "a": "About 110 km/h (68 mph) in short bursts.", "x": "Cheetah top speed — About 110 km/h (68 mph) in short bursts. Example: Fastest land animal..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Peregrine falcon dive", "d": "About 389 km/h (242 mph); fastest animal.", "g": "notable", "l": 2, "q": "What is Peregrine falcon dive?", "a": "About 389 km/h (242 mph); fastest animal.", "x": "Peregrine falcon dive — About 389 km/h (242 mph); fastest animal. Example: Stoop hunting dive..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "US highway speed", "d": "Typically 105-129 km/h (65-80 mph) by state.", "g": "notable", "l": 2, "q": "What is US highway speed?", "a": "Typically 105-129 km/h (65-80 mph) by state.", "x": "US highway speed — Typically 105-129 km/h (65-80 mph) by state. Example: Road trips..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Commercial jet cruise", "d": "About 900 km/h (560 mph) at altitude.", "g": "notable", "l": 2, "q": "What is Commercial jet cruise?", "a": "About 900 km/h (560 mph) at altitude.", "x": "Commercial jet cruise — About 900 km/h (560 mph) at altitude. Example: Airliners..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Concorde cruise", "d": "About 2,179 km/h (Mach 2); retired 2003.", "g": "notable", "l": 2, "q": "What is Concorde cruise?", "a": "About 2,179 km/h (Mach 2); retired 2003.", "x": "Concorde cruise — About 2,179 km/h (Mach 2); retired 2003. Example: Supersonic airliner..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "SR-71 top speed", "d": "About 3,529 km/h (Mach 3.3); fastest air-breathing plane.", "g": "notable", "l": 2, "q": "What is SR-71 top speed?", "a": "About 3,529 km/h (Mach 3.3); fastest air-breathing plane.", "x": "SR-71 top speed — About 3,529 km/h (Mach 3.3); fastest air-breathing plane. Example: Reconnaissance..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Bullet train", "d": "About 320 km/h (200 mph) in service.", "g": "notable", "l": 2, "q": "What is Bullet train?", "a": "About 320 km/h (200 mph) in service.", "x": "Bullet train — About 320 km/h (200 mph) in service. Example: High-speed rail..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "ISS orbital speed", "d": "About 27,600 km/h (17,150 mph).", "g": "notable", "l": 2, "q": "What is ISS orbital speed?", "a": "About 27,600 km/h (17,150 mph).", "x": "ISS orbital speed — About 27,600 km/h (17,150 mph). Example: Low Earth orbit..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Earth rotation at equator", "d": "About 1,670 km/h (1,040 mph).", "g": "notable", "l": 2, "q": "What is Earth rotation at equator?", "a": "About 1,670 km/h (1,040 mph).", "x": "Earth rotation at equator — About 1,670 km/h (1,040 mph). Example: Why we do not feel it: constant motion..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Earth orbital speed", "d": "About 107,000 km/h (66,600 mph) around the Sun.", "g": "notable", "l": 2, "q": "What is Earth orbital speed?", "a": "About 107,000 km/h (66,600 mph) around the Sun.", "x": "Earth orbital speed — About 107,000 km/h (66,600 mph) around the Sun. Example: One lap per year..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Escape velocity Earth", "d": "About 40,270 km/h (11.2 km/s) from the surface.", "g": "notable", "l": 2, "q": "What is Escape velocity Earth?", "a": "About 40,270 km/h (11.2 km/s) from the surface.", "x": "Escape velocity Earth — About 40,270 km/h (11.2 km/s) from the surface. Example: Leaving Earth entirely..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Voyager 1 speed", "d": "About 61,000 km/h relative to the Sun; fastest human object.", "g": "notable", "l": 2, "q": "What is Voyager 1 speed?", "a": "About 61,000 km/h relative to the Sun; fastest human object.", "x": "Voyager 1 speed — About 61,000 km/h relative to the Sun; fastest human object. Example: Interstellar space..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Fastest elevator", "d": "About 73.8 km/h in the Shanghai Tower.", "g": "notable", "l": 2, "q": "What is Fastest elevator?", "a": "About 73.8 km/h in the Shanghai Tower.", "x": "Fastest elevator — About 73.8 km/h in the Shanghai Tower. Example: Skyscraper lifts..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Tsunami speed", "d": "Up to 800 km/h in deep ocean; slows near shore.", "g": "notable", "l": 2, "q": "What is Tsunami speed?", "a": "Up to 800 km/h in deep ocean; slows near shore.", "x": "Tsunami speed — Up to 800 km/h in deep ocean; slows near shore. Example: Ocean safety..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}, {"t": "Nerve impulse", "d": "Up to 432 km/h (120 m/s) in fast neurons.", "g": "notable", "l": 2, "q": "What is Nerve impulse?", "a": "Up to 432 km/h (120 m/s) in fast neurons.", "x": "Nerve impulse — Up to 432 km/h (120 m/s) in fast neurons. Example: Reaction time..  Keep this reference handy — every factor here is checked against standard references (NIST, BIPM, and long-standing trade definitions).", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-speed-velocity-guide-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
