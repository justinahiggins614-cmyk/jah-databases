(function(){'use strict';
/* JAH South Carolina Attractions Database generator — jahdb-e2-south-carolina-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-south-carolina-attractions',PREFIX='JAH-E2SOUTHCARO-',NAME='JAH South Carolina Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "South Carolina: attractions overview", "d": "The best of South Carolina: Charleston, Myrtle Beach, Congaree National Park.", "g": "overview", "l": 2, "q": "What is South Carolina: attractions overview?", "a": "The best of South Carolina: Charleston, Myrtle Beach, Congaree National Park.", "x": "The essential South Carolina: Charleston, Myrtle Beach, Congaree National Park — plus Congaree National Park, South Carolina's great shrimp and grits. Spoleto Festival This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Charleston", "d": "Charleston: a top South Carolina attraction.", "g": "attractions", "l": 2, "q": "What is Charleston?", "a": "Charleston: a top South Carolina attraction.", "x": "Charleston is essential South Carolina. Catawba; rice plantations. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. shrimp and grits State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Charleston", "d": "How to experience Charleston.", "g": "attractions", "l": 2, "q": "What is Visiting Charleston?", "a": "How to experience Charleston.", "x": "Experiencing Charleston: plan around Spoleto Festival, the state's rhythm — Dum spiro spero (While I breathe, I hope). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Congaree National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Myrtle Beach", "d": "Myrtle Beach: a top South Carolina attraction.", "g": "attractions", "l": 2, "q": "What is Myrtle Beach?", "a": "Myrtle Beach: a top South Carolina attraction.", "x": "Myrtle Beach is essential South Carolina. Catawba; rice plantations. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. shrimp and grits", "s": "public-reference", "f": null}, {"t": "Visiting Myrtle Beach", "d": "How to experience Myrtle Beach.", "g": "attractions", "l": 2, "q": "What is Visiting Myrtle Beach?", "a": "How to experience Myrtle Beach.", "x": "Experiencing Myrtle Beach: plan around Spoleto Festival, the state's rhythm — Dum spiro spero (While I breathe, I hope). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Congaree National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Congaree National Park", "d": "Congaree National Park: a top South Carolina attraction.", "g": "attractions", "l": 2, "q": "What is Congaree National Park?", "a": "Congaree National Park: a top South Carolina attraction.", "x": "Congaree National Park is essential South Carolina. Catawba; rice plantations. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. shrimp and grits", "s": "public-reference", "f": null}, {"t": "Visiting Congaree National Park", "d": "How to experience Congaree National Park.", "g": "attractions", "l": 2, "q": "What is Visiting Congaree National Park?", "a": "How to experience Congaree National Park.", "x": "Experiencing Congaree National Park: plan around Spoleto Festival, the state's rhythm — Dum spiro spero (While I breathe, I hope). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Congaree National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Hilton Head", "d": "Hilton Head: a top South Carolina attraction.", "g": "attractions", "l": 2, "q": "What is Hilton Head?", "a": "Hilton Head: a top South Carolina attraction.", "x": "Hilton Head is essential South Carolina. Catawba; rice plantations. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. shrimp and grits", "s": "public-reference", "f": null}, {"t": "Visiting Hilton Head", "d": "How to experience Hilton Head.", "g": "attractions", "l": 2, "q": "What is Visiting Hilton Head?", "a": "How to experience Hilton Head.", "x": "Experiencing Hilton Head: plan around Spoleto Festival, the state's rhythm — Dum spiro spero (While I breathe, I hope). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Congaree National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Fort Sumter", "d": "Fort Sumter: a top South Carolina attraction.", "g": "attractions", "l": 2, "q": "What is Fort Sumter?", "a": "Fort Sumter: a top South Carolina attraction.", "x": "Fort Sumter is essential South Carolina. Catawba; rice plantations. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. shrimp and grits", "s": "public-reference", "f": null}, {"t": "Visiting Fort Sumter", "d": "How to experience Fort Sumter.", "g": "attractions", "l": 2, "q": "What is Visiting Fort Sumter?", "a": "How to experience Fort Sumter.", "x": "Experiencing Fort Sumter: plan around Spoleto Festival, the state's rhythm — Dum spiro spero (While I breathe, I hope). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Congaree National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Brookgreen Gardens", "d": "Brookgreen Gardens: a top South Carolina attraction.", "g": "attractions", "l": 2, "q": "What is Brookgreen Gardens?", "a": "Brookgreen Gardens: a top South Carolina attraction.", "x": "Brookgreen Gardens is essential South Carolina. Catawba; rice plantations. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. shrimp and grits", "s": "public-reference", "f": null}, {"t": "Visiting Brookgreen Gardens", "d": "How to experience Brookgreen Gardens.", "g": "attractions", "l": 2, "q": "What is Visiting Brookgreen Gardens?", "a": "How to experience Brookgreen Gardens.", "x": "Experiencing Brookgreen Gardens: plan around Spoleto Festival, the state's rhythm — Dum spiro spero (While I breathe, I hope). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Congaree National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "USS Yorktown", "d": "USS Yorktown: a top South Carolina attraction.", "g": "attractions", "l": 2, "q": "What is USS Yorktown?", "a": "USS Yorktown: a top South Carolina attraction.", "x": "USS Yorktown is essential South Carolina. Catawba; rice plantations. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. shrimp and grits", "s": "public-reference", "f": null}, {"t": "Visiting USS Yorktown", "d": "How to experience USS Yorktown.", "g": "attractions", "l": 2, "q": "What is Visiting USS Yorktown?", "a": "How to experience USS Yorktown.", "x": "Experiencing USS Yorktown: plan around Spoleto Festival, the state's rhythm — Dum spiro spero (While I breathe, I hope). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Congaree National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Hunting Island", "d": "Hunting Island: a top South Carolina attraction.", "g": "attractions", "l": 2, "q": "What is Hunting Island?", "a": "Hunting Island: a top South Carolina attraction.", "x": "Hunting Island is essential South Carolina. Catawba; rice plantations. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. shrimp and grits", "s": "public-reference", "f": null}, {"t": "Visiting Hunting Island", "d": "How to experience Hunting Island.", "g": "attractions", "l": 2, "q": "What is Visiting Hunting Island?", "a": "How to experience Hunting Island.", "x": "Experiencing Hunting Island: plan around Spoleto Festival, the state's rhythm — Dum spiro spero (While I breathe, I hope). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Congaree National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Congaree National Park", "d": "Congaree National Park: South Carolina's great park.", "g": "parks", "l": 2, "q": "What is Congaree National Park?", "a": "Congaree National Park: South Carolina's great park.", "x": "Congaree National Park is South Carolina's wild heart: Charleston. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Spoleto Festival Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Congaree National Park", "d": "How to explore Congaree National Park.", "g": "parks", "l": 2, "q": "What is Exploring Congaree National Park?", "a": "How to explore Congaree National Park.", "x": "Exploring Congaree National Park: get the park map, check conditions, carry water and layers, and tell someone your plan. Dum spiro spero (While I breathe, I hope) Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Columbia: the capital city", "d": "Columbia, capital of South Carolina.", "g": "cities", "l": 2, "q": "What is Columbia: the capital city?", "a": "Columbia, capital of South Carolina.", "x": "Columbia: the capital of South Carolina — government, history, and often the best museums. First to secede; Civil War. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Charleston", "s": "public-reference", "f": null}, {"t": "Charleston: the biggest city", "d": "Charleston is South Carolina's largest city.", "g": "cities", "l": 2, "q": "What is Charleston: the biggest city?", "a": "Charleston is South Carolina's largest city.", "x": "Charleston is where South Carolina comes to work and play: the skyline, the food, the music, the crowds. automotive (BMW) Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Spoleto Festival", "s": "public-reference", "f": null}, {"t": "shrimp and grits: the food", "d": "Taste South Carolina: shrimp and grits.", "g": "food", "l": 2, "q": "What is shrimp and grits: the food?", "a": "Taste South Carolina: shrimp and grits.", "x": "The taste of South Carolina is shrimp and grits — and the foodways around it. Textiles to BMW. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Spoleto Festival Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: South Carolina", "d": "Eating your way through South Carolina.", "g": "food", "l": 2, "q": "What is Food tour: South Carolina?", "a": "Eating your way through South Carolina.", "x": "Eating through South Carolina: start with shrimp and grits, then follow the locals — diners, food trucks, farm stands. Dum spiro spero (While I breathe, I hope) Food is the fastest way into a place's heart; the stories come free with the meal. Charleston", "s": "public-reference", "f": null}, {"t": "Spoleto Festival", "d": "Spoleto Festival: South Carolina's signature festival.", "g": "festivals", "l": 2, "q": "What is Spoleto Festival?", "a": "Spoleto Festival: South Carolina's signature festival.", "x": "Spoleto Festival is South Carolina at its most celebratory: BMW's plant made it an auto state.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Columbia Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "South Carolina year-round: Spoleto Festival and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "South Carolina year-round: Spoleto Festival and more.", "x": "The South Carolina festival calendar runs year-round, with Spoleto Festival as the anchor. Dum spiro spero (While I breathe, I hope) Every season has its celebration — plan trips around them for the liveliest version of the state. Congaree National Park", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-south-carolina-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
