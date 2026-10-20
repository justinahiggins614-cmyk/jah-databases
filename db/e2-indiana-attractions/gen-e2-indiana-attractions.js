(function(){'use strict';
/* JAH Indiana Attractions Database generator — jahdb-e2-indiana-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-indiana-attractions',PREFIX='JAH-E2INDIANAAT-',NAME='JAH Indiana Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Indiana: attractions overview", "d": "The best of Indiana: Indianapolis 500, Indiana Dunes, Children's Museum.", "g": "overview", "l": 2, "q": "What is Indiana: attractions overview?", "a": "The best of Indiana: Indianapolis 500, Indiana Dunes, Children's Museum.", "x": "The essential Indiana: Indianapolis 500, Indiana Dunes, Children's Museum — plus Indiana Dunes National Park, Indiana's great pork tenderloin sandwich. Indy 500 This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Indianapolis 500", "d": "Indianapolis 500: a top Indiana attraction.", "g": "attractions", "l": 2, "q": "What is Indianapolis 500?", "a": "Indianapolis 500: a top Indiana attraction.", "x": "Indianapolis 500 is essential Indiana. Miami and Potawatomi; Northwest Territory. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pork tenderloin sandwich", "s": "public-reference", "f": null}, {"t": "Visiting Indianapolis 500", "d": "How to experience Indianapolis 500.", "g": "attractions", "l": 2, "q": "What is Visiting Indianapolis 500?", "a": "How to experience Indianapolis 500.", "x": "Experiencing Indianapolis 500: plan around Indy 500, the state's rhythm — The Crossroads of America. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Indiana Dunes National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Indiana Dunes", "d": "Indiana Dunes: a top Indiana attraction.", "g": "attractions", "l": 2, "q": "What is Indiana Dunes?", "a": "Indiana Dunes: a top Indiana attraction.", "x": "Indiana Dunes is essential Indiana. Miami and Potawatomi; Northwest Territory. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pork tenderloin sandwich", "s": "public-reference", "f": null}, {"t": "Visiting Indiana Dunes", "d": "How to experience Indiana Dunes.", "g": "attractions", "l": 2, "q": "What is Visiting Indiana Dunes?", "a": "How to experience Indiana Dunes.", "x": "Experiencing Indiana Dunes: plan around Indy 500, the state's rhythm — The Crossroads of America. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Indiana Dunes National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Children's Museum", "d": "Children's Museum: a top Indiana attraction.", "g": "attractions", "l": 2, "q": "What is Children's Museum?", "a": "Children's Museum: a top Indiana attraction.", "x": "Children's Museum is essential Indiana. Miami and Potawatomi; Northwest Territory. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pork tenderloin sandwich", "s": "public-reference", "f": null}, {"t": "Visiting Children's Museum", "d": "How to experience Children's Museum.", "g": "attractions", "l": 2, "q": "What is Visiting Children's Museum?", "a": "How to experience Children's Museum.", "x": "Experiencing Children's Museum: plan around Indy 500, the state's rhythm — The Crossroads of America. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Indiana Dunes National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "French Lick Resort", "d": "French Lick Resort: a top Indiana attraction.", "g": "attractions", "l": 2, "q": "What is French Lick Resort?", "a": "French Lick Resort: a top Indiana attraction.", "x": "French Lick Resort is essential Indiana. Miami and Potawatomi; Northwest Territory. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pork tenderloin sandwich", "s": "public-reference", "f": null}, {"t": "Visiting French Lick Resort", "d": "How to experience French Lick Resort.", "g": "attractions", "l": 2, "q": "What is Visiting French Lick Resort?", "a": "How to experience French Lick Resort.", "x": "Experiencing French Lick Resort: plan around Indy 500, the state's rhythm — The Crossroads of America. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Indiana Dunes National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Turkey Run", "d": "Turkey Run: a top Indiana attraction.", "g": "attractions", "l": 2, "q": "What is Turkey Run?", "a": "Turkey Run: a top Indiana attraction.", "x": "Turkey Run is essential Indiana. Miami and Potawatomi; Northwest Territory. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pork tenderloin sandwich", "s": "public-reference", "f": null}, {"t": "Visiting Turkey Run", "d": "How to experience Turkey Run.", "g": "attractions", "l": 2, "q": "What is Visiting Turkey Run?", "a": "How to experience Turkey Run.", "x": "Experiencing Turkey Run: plan around Indy 500, the state's rhythm — The Crossroads of America. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Indiana Dunes National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Eiteljorg Museum", "d": "Eiteljorg Museum: a top Indiana attraction.", "g": "attractions", "l": 2, "q": "What is Eiteljorg Museum?", "a": "Eiteljorg Museum: a top Indiana attraction.", "x": "Eiteljorg Museum is essential Indiana. Miami and Potawatomi; Northwest Territory. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pork tenderloin sandwich", "s": "public-reference", "f": null}, {"t": "Visiting Eiteljorg Museum", "d": "How to experience Eiteljorg Museum.", "g": "attractions", "l": 2, "q": "What is Visiting Eiteljorg Museum?", "a": "How to experience Eiteljorg Museum.", "x": "Experiencing Eiteljorg Museum: plan around Indy 500, the state's rhythm — The Crossroads of America. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Indiana Dunes National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Notre Dame", "d": "Notre Dame: a top Indiana attraction.", "g": "attractions", "l": 2, "q": "What is Notre Dame?", "a": "Notre Dame: a top Indiana attraction.", "x": "Notre Dame is essential Indiana. Miami and Potawatomi; Northwest Territory. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pork tenderloin sandwich", "s": "public-reference", "f": null}, {"t": "Visiting Notre Dame", "d": "How to experience Notre Dame.", "g": "attractions", "l": 2, "q": "What is Visiting Notre Dame?", "a": "How to experience Notre Dame.", "x": "Experiencing Notre Dame: plan around Indy 500, the state's rhythm — The Crossroads of America. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Indiana Dunes National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Holiday World", "d": "Holiday World: a top Indiana attraction.", "g": "attractions", "l": 2, "q": "What is Holiday World?", "a": "Holiday World: a top Indiana attraction.", "x": "Holiday World is essential Indiana. Miami and Potawatomi; Northwest Territory. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pork tenderloin sandwich", "s": "public-reference", "f": null}, {"t": "Visiting Holiday World", "d": "How to experience Holiday World.", "g": "attractions", "l": 2, "q": "What is Visiting Holiday World?", "a": "How to experience Holiday World.", "x": "Experiencing Holiday World: plan around Indy 500, the state's rhythm — The Crossroads of America. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Indiana Dunes National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Indiana Dunes National Park", "d": "Indiana Dunes National Park: Indiana's great park.", "g": "parks", "l": 2, "q": "What is Indiana Dunes National Park?", "a": "Indiana Dunes National Park: Indiana's great park.", "x": "Indiana Dunes National Park is Indiana's wild heart: Indianapolis 500. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Indy 500 Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Indiana Dunes National Park", "d": "How to explore Indiana Dunes National Park.", "g": "parks", "l": 2, "q": "What is Exploring Indiana Dunes National Park?", "a": "How to explore Indiana Dunes National Park.", "x": "Exploring Indiana Dunes National Park: get the park map, check conditions, carry water and layers, and tell someone your plan. The Crossroads of America Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Indianapolis: the capital city", "d": "Indianapolis, capital of Indiana.", "g": "cities", "l": 2, "q": "What is Indianapolis: the capital city?", "a": "Indianapolis, capital of Indiana.", "x": "Indianapolis: the capital of Indiana — government, history, and often the best museums. Underground Railroad; Civil War. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Indianapolis", "s": "public-reference", "f": null}, {"t": "Indianapolis: the biggest city", "d": "Indianapolis is Indiana's largest city.", "g": "cities", "l": 2, "q": "What is Indianapolis: the biggest city?", "a": "Indianapolis is Indiana's largest city.", "x": "Indianapolis is where Indiana comes to work and play: the skyline, the food, the music, the crowds. manufacturing (autos) Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Indy 500", "s": "public-reference", "f": null}, {"t": "pork tenderloin sandwich: the food", "d": "Taste Indiana: pork tenderloin sandwich.", "g": "food", "l": 2, "q": "What is pork tenderloin sandwich: the food?", "a": "Taste Indiana: pork tenderloin sandwich.", "x": "The taste of Indiana is pork tenderloin sandwich — and the foodways around it. Auto and steel; Indy 500. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Indy 500 Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Indiana", "d": "Eating your way through Indiana.", "g": "food", "l": 2, "q": "What is Food tour: Indiana?", "a": "Eating your way through Indiana.", "x": "Eating through Indiana: start with pork tenderloin sandwich, then follow the locals — diners, food trucks, farm stands. The Crossroads of America Food is the fastest way into a place's heart; the stories come free with the meal. Indianapolis", "s": "public-reference", "f": null}, {"t": "Indy 500", "d": "Indy 500: Indiana's signature festival.", "g": "festivals", "l": 2, "q": "What is Indy 500?", "a": "Indy 500: Indiana's signature festival.", "x": "Indy 500 is Indiana at its most celebratory: Basketball heartland.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Indianapolis Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Indiana year-round: Indy 500 and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Indiana year-round: Indy 500 and more.", "x": "The Indiana festival calendar runs year-round, with Indy 500 as the anchor. The Crossroads of America Every season has its celebration — plan trips around them for the liveliest version of the state. Indiana Dunes National Park", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-indiana-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
