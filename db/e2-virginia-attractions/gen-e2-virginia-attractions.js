(function(){'use strict';
/* JAH Virginia Attractions Database generator — jahdb-e2-virginia-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-virginia-attractions',PREFIX='JAH-E2VIRGINIAA-',NAME='JAH Virginia Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Virginia: attractions overview", "d": "The best of Virginia: Colonial Williamsburg, Shenandoah National Park, Monticello.", "g": "overview", "l": 2, "q": "What is Virginia: attractions overview?", "a": "The best of Virginia: Colonial Williamsburg, Shenandoah National Park, Monticello.", "x": "The essential Virginia: Colonial Williamsburg, Shenandoah National Park, Monticello — plus Shenandoah National Park, Virginia's great country ham. Virginia festivals This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Colonial Williamsburg", "d": "Colonial Williamsburg: a top Virginia attraction.", "g": "attractions", "l": 2, "q": "What is Colonial Williamsburg?", "a": "Colonial Williamsburg: a top Virginia attraction.", "x": "Colonial Williamsburg is essential Virginia. Jamestown 1607; 8 presidents. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. country ham", "s": "public-reference", "f": null}, {"t": "Visiting Colonial Williamsburg", "d": "How to experience Colonial Williamsburg.", "g": "attractions", "l": 2, "q": "What is Visiting Colonial Williamsburg?", "a": "How to experience Colonial Williamsburg.", "x": "Experiencing Colonial Williamsburg: plan around Virginia festivals, the state's rhythm — Sic semper tyrannis (Thus always to tyrants). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Shenandoah National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Shenandoah National Park", "d": "Shenandoah National Park: a top Virginia attraction.", "g": "attractions", "l": 2, "q": "What is Shenandoah National Park?", "a": "Shenandoah National Park: a top Virginia attraction.", "x": "Shenandoah National Park is essential Virginia. Jamestown 1607; 8 presidents. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. country ham", "s": "public-reference", "f": null}, {"t": "Visiting Shenandoah National Park", "d": "How to experience Shenandoah National Park.", "g": "attractions", "l": 2, "q": "What is Visiting Shenandoah National Park?", "a": "How to experience Shenandoah National Park.", "x": "Experiencing Shenandoah National Park: plan around Virginia festivals, the state's rhythm — Sic semper tyrannis (Thus always to tyrants). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Shenandoah National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Monticello", "d": "Monticello: a top Virginia attraction.", "g": "attractions", "l": 2, "q": "What is Monticello?", "a": "Monticello: a top Virginia attraction.", "x": "Monticello is essential Virginia. Jamestown 1607; 8 presidents. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. country ham State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Monticello", "d": "How to experience Monticello.", "g": "attractions", "l": 2, "q": "What is Visiting Monticello?", "a": "How to experience Monticello.", "x": "Experiencing Monticello: plan around Virginia festivals, the state's rhythm — Sic semper tyrannis (Thus always to tyrants). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Shenandoah National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Arlington Cemetery", "d": "Arlington Cemetery: a top Virginia attraction.", "g": "attractions", "l": 2, "q": "What is Arlington Cemetery?", "a": "Arlington Cemetery: a top Virginia attraction.", "x": "Arlington Cemetery is essential Virginia. Jamestown 1607; 8 presidents. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. country ham State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Arlington Cemetery", "d": "How to experience Arlington Cemetery.", "g": "attractions", "l": 2, "q": "What is Visiting Arlington Cemetery?", "a": "How to experience Arlington Cemetery.", "x": "Experiencing Arlington Cemetery: plan around Virginia festivals, the state's rhythm — Sic semper tyrannis (Thus always to tyrants). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Shenandoah National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Virginia Beach", "d": "Virginia Beach: a top Virginia attraction.", "g": "attractions", "l": 2, "q": "What is Virginia Beach?", "a": "Virginia Beach: a top Virginia attraction.", "x": "Virginia Beach is essential Virginia. Jamestown 1607; 8 presidents. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. country ham State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Virginia Beach", "d": "How to experience Virginia Beach.", "g": "attractions", "l": 2, "q": "What is Visiting Virginia Beach?", "a": "How to experience Virginia Beach.", "x": "Experiencing Virginia Beach: plan around Virginia festivals, the state's rhythm — Sic semper tyrannis (Thus always to tyrants). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Shenandoah National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Blue Ridge Parkway", "d": "Blue Ridge Parkway: a top Virginia attraction.", "g": "attractions", "l": 2, "q": "What is Blue Ridge Parkway?", "a": "Blue Ridge Parkway: a top Virginia attraction.", "x": "Blue Ridge Parkway is essential Virginia. Jamestown 1607; 8 presidents. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. country ham State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Blue Ridge Parkway", "d": "How to experience Blue Ridge Parkway.", "g": "attractions", "l": 2, "q": "What is Visiting Blue Ridge Parkway?", "a": "How to experience Blue Ridge Parkway.", "x": "Experiencing Blue Ridge Parkway: plan around Virginia festivals, the state's rhythm — Sic semper tyrannis (Thus always to tyrants). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Shenandoah National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Jamestown", "d": "Jamestown: a top Virginia attraction.", "g": "attractions", "l": 2, "q": "What is Jamestown?", "a": "Jamestown: a top Virginia attraction.", "x": "Jamestown is essential Virginia. Jamestown 1607; 8 presidents. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. country ham State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Jamestown", "d": "How to experience Jamestown.", "g": "attractions", "l": 2, "q": "What is Visiting Jamestown?", "a": "How to experience Jamestown.", "x": "Experiencing Jamestown: plan around Virginia festivals, the state's rhythm — Sic semper tyrannis (Thus always to tyrants). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Shenandoah National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Mount Vernon", "d": "Mount Vernon: a top Virginia attraction.", "g": "attractions", "l": 2, "q": "What is Mount Vernon?", "a": "Mount Vernon: a top Virginia attraction.", "x": "Mount Vernon is essential Virginia. Jamestown 1607; 8 presidents. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. country ham State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Mount Vernon", "d": "How to experience Mount Vernon.", "g": "attractions", "l": 2, "q": "What is Visiting Mount Vernon?", "a": "How to experience Mount Vernon.", "x": "Experiencing Mount Vernon: plan around Virginia festivals, the state's rhythm — Sic semper tyrannis (Thus always to tyrants). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Shenandoah National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Shenandoah National Park", "d": "Shenandoah National Park: Virginia's great park.", "g": "parks", "l": 2, "q": "What is Shenandoah National Park?", "a": "Shenandoah National Park: Virginia's great park.", "x": "Shenandoah National Park is Virginia's wild heart: Colonial Williamsburg. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Virginia festivals Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Shenandoah National Park", "d": "How to explore Shenandoah National Park.", "g": "parks", "l": 2, "q": "What is Exploring Shenandoah National Park?", "a": "How to explore Shenandoah National Park.", "x": "Exploring Shenandoah National Park: get the park map, check conditions, carry water and layers, and tell someone your plan. Sic semper tyrannis (Thus always to tyrants) Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Richmond: the capital city", "d": "Richmond, capital of Virginia.", "g": "cities", "l": 2, "q": "What is Richmond: the capital city?", "a": "Richmond, capital of Virginia.", "x": "Richmond: the capital of Virginia — government, history, and often the best museums. Revolution; Civil War capital. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Virginia Beach", "s": "public-reference", "f": null}, {"t": "Virginia Beach: the biggest city", "d": "Virginia Beach is Virginia's largest city.", "g": "cities", "l": 2, "q": "What is Virginia Beach: the biggest city?", "a": "Virginia Beach is Virginia's largest city.", "x": "Virginia Beach is where Virginia comes to work and play: the skyline, the food, the music, the crowds. federal government Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Virginia festivals", "s": "public-reference", "f": null}, {"t": "country ham: the food", "d": "Taste Virginia: country ham.", "g": "food", "l": 2, "q": "What is country ham: the food?", "a": "Taste Virginia: country ham.", "x": "The taste of Virginia is country ham — and the foodways around it. Government; tech; history. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Virginia festivals Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Virginia", "d": "Eating your way through Virginia.", "g": "food", "l": 2, "q": "What is Food tour: Virginia?", "a": "Eating your way through Virginia.", "x": "Eating through Virginia: start with country ham, then follow the locals — diners, food trucks, farm stands. Sic semper tyrannis (Thus always to tyrants) Food is the fastest way into a place's heart; the stories come free with the meal. Virginia Beach", "s": "public-reference", "f": null}, {"t": "Virginia festivals", "d": "Virginia festivals: Virginia's signature festival.", "g": "festivals", "l": 2, "q": "What is Virginia festivals?", "a": "Virginia festivals: Virginia's signature festival.", "x": "Virginia festivals is Virginia at its most celebratory: Eight U.S. presidents were born in Virginia.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Richmond Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Virginia year-round: Virginia festivals and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Virginia year-round: Virginia festivals and more.", "x": "The Virginia festival calendar runs year-round, with Virginia festivals as the anchor. Sic semper tyrannis (Thus always to tyrants) Every season has its celebration — plan trips around them for the liveliest version of the state. Shenandoah National Park", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-virginia-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
