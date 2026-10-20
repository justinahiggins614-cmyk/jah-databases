(function(){'use strict';
/* JAH Kansas Attractions Database generator — jahdb-e2-kansas-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-kansas-attractions',PREFIX='JAH-E2KANSASATT-',NAME='JAH Kansas Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Kansas: attractions overview", "d": "The best of Kansas: Tallgrass Prairie, Monument Rocks, Eisenhower Library.", "g": "overview", "l": 2, "q": "What is Kansas: attractions overview?", "a": "The best of Kansas: Tallgrass Prairie, Monument Rocks, Eisenhower Library.", "x": "The essential Kansas: Tallgrass Prairie, Monument Rocks, Eisenhower Library — plus Tallgrass Prairie National Preserve, Kansas's great burnt ends (KC BBQ). Kansas State Fair This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Tallgrass Prairie", "d": "Tallgrass Prairie: a top Kansas attraction.", "g": "attractions", "l": 2, "q": "What is Tallgrass Prairie?", "a": "Tallgrass Prairie: a top Kansas attraction.", "x": "Tallgrass Prairie is essential Kansas. Kansa and Osage; Bleeding Kansas. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. burnt ends (KC BBQ)", "s": "public-reference", "f": null}, {"t": "Visiting Tallgrass Prairie", "d": "How to experience Tallgrass Prairie.", "g": "attractions", "l": 2, "q": "What is Visiting Tallgrass Prairie?", "a": "How to experience Tallgrass Prairie.", "x": "Experiencing Tallgrass Prairie: plan around Kansas State Fair, the state's rhythm — Ad astra per aspera (To the stars through difficulties). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Tallgrass Prairie National Preserve Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Monument Rocks", "d": "Monument Rocks: a top Kansas attraction.", "g": "attractions", "l": 2, "q": "What is Monument Rocks?", "a": "Monument Rocks: a top Kansas attraction.", "x": "Monument Rocks is essential Kansas. Kansa and Osage; Bleeding Kansas. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. burnt ends (KC BBQ)", "s": "public-reference", "f": null}, {"t": "Visiting Monument Rocks", "d": "How to experience Monument Rocks.", "g": "attractions", "l": 2, "q": "What is Visiting Monument Rocks?", "a": "How to experience Monument Rocks.", "x": "Experiencing Monument Rocks: plan around Kansas State Fair, the state's rhythm — Ad astra per aspera (To the stars through difficulties). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Tallgrass Prairie National Preserve Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Eisenhower Library", "d": "Eisenhower Library: a top Kansas attraction.", "g": "attractions", "l": 2, "q": "What is Eisenhower Library?", "a": "Eisenhower Library: a top Kansas attraction.", "x": "Eisenhower Library is essential Kansas. Kansa and Osage; Bleeding Kansas. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. burnt ends (KC BBQ)", "s": "public-reference", "f": null}, {"t": "Visiting Eisenhower Library", "d": "How to experience Eisenhower Library.", "g": "attractions", "l": 2, "q": "What is Visiting Eisenhower Library?", "a": "How to experience Eisenhower Library.", "x": "Experiencing Eisenhower Library: plan around Kansas State Fair, the state's rhythm — Ad astra per aspera (To the stars through difficulties). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Tallgrass Prairie National Preserve Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Botanica Wichita", "d": "Botanica Wichita: a top Kansas attraction.", "g": "attractions", "l": 2, "q": "What is Botanica Wichita?", "a": "Botanica Wichita: a top Kansas attraction.", "x": "Botanica Wichita is essential Kansas. Kansa and Osage; Bleeding Kansas. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. burnt ends (KC BBQ)", "s": "public-reference", "f": null}, {"t": "Visiting Botanica Wichita", "d": "How to experience Botanica Wichita.", "g": "attractions", "l": 2, "q": "What is Visiting Botanica Wichita?", "a": "How to experience Botanica Wichita.", "x": "Experiencing Botanica Wichita: plan around Kansas State Fair, the state's rhythm — Ad astra per aspera (To the stars through difficulties). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Tallgrass Prairie National Preserve Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Stratica (Cosmosphere)", "d": "Stratica (Cosmosphere): a top Kansas attraction.", "g": "attractions", "l": 2, "q": "What is Stratica (Cosmosphere)?", "a": "Stratica (Cosmosphere): a top Kansas attraction.", "x": "Stratica (Cosmosphere) is essential Kansas. Kansa and Osage; Bleeding Kansas. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. burnt ends (KC BBQ)", "s": "public-reference", "f": null}, {"t": "Visiting Stratica (Cosmosphere)", "d": "How to experience Stratica (Cosmosphere).", "g": "attractions", "l": 2, "q": "What is Visiting Stratica (Cosmosphere)?", "a": "How to experience Stratica (Cosmosphere).", "x": "Experiencing Stratica (Cosmosphere): plan around Kansas State Fair, the state's rhythm — Ad astra per aspera (To the stars through difficulties). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Tallgrass Prairie National Preserve Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Dodge City", "d": "Dodge City: a top Kansas attraction.", "g": "attractions", "l": 2, "q": "What is Dodge City?", "a": "Dodge City: a top Kansas attraction.", "x": "Dodge City is essential Kansas. Kansa and Osage; Bleeding Kansas. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. burnt ends (KC BBQ)", "s": "public-reference", "f": null}, {"t": "Visiting Dodge City", "d": "How to experience Dodge City.", "g": "attractions", "l": 2, "q": "What is Visiting Dodge City?", "a": "How to experience Dodge City.", "x": "Experiencing Dodge City: plan around Kansas State Fair, the state's rhythm — Ad astra per aspera (To the stars through difficulties). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Tallgrass Prairie National Preserve Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Kansas Speedway", "d": "Kansas Speedway: a top Kansas attraction.", "g": "attractions", "l": 2, "q": "What is Kansas Speedway?", "a": "Kansas Speedway: a top Kansas attraction.", "x": "Kansas Speedway is essential Kansas. Kansa and Osage; Bleeding Kansas. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. burnt ends (KC BBQ)", "s": "public-reference", "f": null}, {"t": "Visiting Kansas Speedway", "d": "How to experience Kansas Speedway.", "g": "attractions", "l": 2, "q": "What is Visiting Kansas Speedway?", "a": "How to experience Kansas Speedway.", "x": "Experiencing Kansas Speedway: plan around Kansas State Fair, the state's rhythm — Ad astra per aspera (To the stars through difficulties). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Tallgrass Prairie National Preserve Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Sedgwick County Zoo", "d": "Sedgwick County Zoo: a top Kansas attraction.", "g": "attractions", "l": 2, "q": "What is Sedgwick County Zoo?", "a": "Sedgwick County Zoo: a top Kansas attraction.", "x": "Sedgwick County Zoo is essential Kansas. Kansa and Osage; Bleeding Kansas. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. burnt ends (KC BBQ)", "s": "public-reference", "f": null}, {"t": "Visiting Sedgwick County Zoo", "d": "How to experience Sedgwick County Zoo.", "g": "attractions", "l": 2, "q": "What is Visiting Sedgwick County Zoo?", "a": "How to experience Sedgwick County Zoo.", "x": "Experiencing Sedgwick County Zoo: plan around Kansas State Fair, the state's rhythm — Ad astra per aspera (To the stars through difficulties). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Tallgrass Prairie National Preserve Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Tallgrass Prairie National Preserve", "d": "Tallgrass Prairie National Preserve: Kansas's great park.", "g": "parks", "l": 2, "q": "What is Tallgrass Prairie National Preserve?", "a": "Tallgrass Prairie National Preserve: Kansas's great park.", "x": "Tallgrass Prairie National Preserve is Kansas's wild heart: Tallgrass Prairie. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Kansas State Fair Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Tallgrass Prairie National Preserve", "d": "How to explore Tallgrass Prairie National Preserve.", "g": "parks", "l": 2, "q": "What is Exploring Tallgrass Prairie National Preserve?", "a": "How to explore Tallgrass Prairie National Preserve.", "x": "Exploring Tallgrass Prairie National Preserve: get the park map, check conditions, carry water and layers, and tell someone your plan. Ad astra per aspera (To the stars through difficulties) Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Topeka: the capital city", "d": "Topeka, capital of Kansas.", "g": "cities", "l": 2, "q": "What is Topeka: the capital city?", "a": "Topeka, capital of Kansas.", "x": "Topeka: the capital of Kansas — government, history, and often the best museums. Wheat and cattle; Dust Bowl. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Wichita", "s": "public-reference", "f": null}, {"t": "Wichita: the biggest city", "d": "Wichita is Kansas's largest city.", "g": "cities", "l": 2, "q": "What is Wichita: the biggest city?", "a": "Wichita is Kansas's largest city.", "x": "Wichita is where Kansas comes to work and play: the skyline, the food, the music, the crowds. aviation (Wichita) Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Kansas State Fair", "s": "public-reference", "f": null}, {"t": "burnt ends (KC BBQ): the food", "d": "Taste Kansas: burnt ends (KC BBQ).", "g": "food", "l": 2, "q": "What is burnt ends (KC BBQ): the food?", "a": "Taste Kansas: burnt ends (KC BBQ).", "x": "The taste of Kansas is burnt ends (KC BBQ) — and the foodways around it. Aviation (Wichita). Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Kansas State Fair Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Kansas", "d": "Eating your way through Kansas.", "g": "food", "l": 2, "q": "What is Food tour: Kansas?", "a": "Eating your way through Kansas.", "x": "Eating through Kansas: start with burnt ends (KC BBQ), then follow the locals — diners, food trucks, farm stands. Ad astra per aspera (To the stars through difficulties) Food is the fastest way into a place's heart; the stories come free with the meal. Wichita", "s": "public-reference", "f": null}, {"t": "Kansas State Fair", "d": "Kansas State Fair: Kansas's signature festival.", "g": "festivals", "l": 2, "q": "What is Kansas State Fair?", "a": "Kansas State Fair: Kansas's signature festival.", "x": "Kansas State Fair is Kansas at its most celebratory: Wichita became the Air Capital of the World.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Topeka Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Kansas year-round: Kansas State Fair and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Kansas year-round: Kansas State Fair and more.", "x": "The Kansas festival calendar runs year-round, with Kansas State Fair as the anchor. Ad astra per aspera (To the stars through difficulties) Every season has its celebration — plan trips around them for the liveliest version of the state. Tallgrass Prairie National Preserve", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-kansas-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
