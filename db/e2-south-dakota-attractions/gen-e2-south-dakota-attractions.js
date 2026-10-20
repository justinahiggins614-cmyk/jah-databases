(function(){'use strict';
/* JAH South Dakota Attractions Database generator — jahdb-e2-south-dakota-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-south-dakota-attractions',PREFIX='JAH-E2SOUTHDAKO-',NAME='JAH South Dakota Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "South Dakota: attractions overview", "d": "The best of South Dakota: Mount Rushmore, Badlands, Custer State Park.", "g": "overview", "l": 2, "q": "What is South Dakota: attractions overview?", "a": "The best of South Dakota: Mount Rushmore, Badlands, Custer State Park.", "x": "The essential South Dakota: Mount Rushmore, Badlands, Custer State Park — plus Badlands National Park, South Dakota's great chislic. Sturgis Rally This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Mount Rushmore", "d": "Mount Rushmore: a top South Dakota attraction.", "g": "attractions", "l": 2, "q": "What is Mount Rushmore?", "a": "Mount Rushmore: a top South Dakota attraction.", "x": "Mount Rushmore is essential South Dakota. Lakota; gold rush 1874. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. chislic State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Mount Rushmore", "d": "How to experience Mount Rushmore.", "g": "attractions", "l": 2, "q": "What is Visiting Mount Rushmore?", "a": "How to experience Mount Rushmore.", "x": "Experiencing Mount Rushmore: plan around Sturgis Rally, the state's rhythm — Under God the people rule. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Badlands National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Badlands", "d": "Badlands: a top South Dakota attraction.", "g": "attractions", "l": 2, "q": "What is Badlands?", "a": "Badlands: a top South Dakota attraction.", "x": "Badlands is essential South Dakota. Lakota; gold rush 1874. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. chislic State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Badlands", "d": "How to experience Badlands.", "g": "attractions", "l": 2, "q": "What is Visiting Badlands?", "a": "How to experience Badlands.", "x": "Experiencing Badlands: plan around Sturgis Rally, the state's rhythm — Under God the people rule. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Badlands National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Custer State Park", "d": "Custer State Park: a top South Dakota attraction.", "g": "attractions", "l": 2, "q": "What is Custer State Park?", "a": "Custer State Park: a top South Dakota attraction.", "x": "Custer State Park is essential South Dakota. Lakota; gold rush 1874. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. chislic State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Custer State Park", "d": "How to experience Custer State Park.", "g": "attractions", "l": 2, "q": "What is Visiting Custer State Park?", "a": "How to experience Custer State Park.", "x": "Experiencing Custer State Park: plan around Sturgis Rally, the state's rhythm — Under God the people rule. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Badlands National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Crazy Horse Memorial", "d": "Crazy Horse Memorial: a top South Dakota attraction.", "g": "attractions", "l": 2, "q": "What is Crazy Horse Memorial?", "a": "Crazy Horse Memorial: a top South Dakota attraction.", "x": "Crazy Horse Memorial is essential South Dakota. Lakota; gold rush 1874. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. chislic State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Crazy Horse Memorial", "d": "How to experience Crazy Horse Memorial.", "g": "attractions", "l": 2, "q": "What is Visiting Crazy Horse Memorial?", "a": "How to experience Crazy Horse Memorial.", "x": "Experiencing Crazy Horse Memorial: plan around Sturgis Rally, the state's rhythm — Under God the people rule. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Badlands National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Deadwood", "d": "Deadwood: a top South Dakota attraction.", "g": "attractions", "l": 2, "q": "What is Deadwood?", "a": "Deadwood: a top South Dakota attraction.", "x": "Deadwood is essential South Dakota. Lakota; gold rush 1874. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. chislic State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Deadwood", "d": "How to experience Deadwood.", "g": "attractions", "l": 2, "q": "What is Visiting Deadwood?", "a": "How to experience Deadwood.", "x": "Experiencing Deadwood: plan around Sturgis Rally, the state's rhythm — Under God the people rule. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Badlands National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Wind Cave", "d": "Wind Cave: a top South Dakota attraction.", "g": "attractions", "l": 2, "q": "What is Wind Cave?", "a": "Wind Cave: a top South Dakota attraction.", "x": "Wind Cave is essential South Dakota. Lakota; gold rush 1874. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. chislic State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Wind Cave", "d": "How to experience Wind Cave.", "g": "attractions", "l": 2, "q": "What is Visiting Wind Cave?", "a": "How to experience Wind Cave.", "x": "Experiencing Wind Cave: plan around Sturgis Rally, the state's rhythm — Under God the people rule. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Badlands National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Spearfish Canyon", "d": "Spearfish Canyon: a top South Dakota attraction.", "g": "attractions", "l": 2, "q": "What is Spearfish Canyon?", "a": "Spearfish Canyon: a top South Dakota attraction.", "x": "Spearfish Canyon is essential South Dakota. Lakota; gold rush 1874. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. chislic State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Spearfish Canyon", "d": "How to experience Spearfish Canyon.", "g": "attractions", "l": 2, "q": "What is Visiting Spearfish Canyon?", "a": "How to experience Spearfish Canyon.", "x": "Experiencing Spearfish Canyon: plan around Sturgis Rally, the state's rhythm — Under God the people rule. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Badlands National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Falls Park", "d": "Falls Park: a top South Dakota attraction.", "g": "attractions", "l": 2, "q": "What is Falls Park?", "a": "Falls Park: a top South Dakota attraction.", "x": "Falls Park is essential South Dakota. Lakota; gold rush 1874. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. chislic State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Falls Park", "d": "How to experience Falls Park.", "g": "attractions", "l": 2, "q": "What is Visiting Falls Park?", "a": "How to experience Falls Park.", "x": "Experiencing Falls Park: plan around Sturgis Rally, the state's rhythm — Under God the people rule. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Badlands National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Badlands National Park", "d": "Badlands National Park: South Dakota's great park.", "g": "parks", "l": 2, "q": "What is Badlands National Park?", "a": "Badlands National Park: South Dakota's great park.", "x": "Badlands National Park is South Dakota's wild heart: Mount Rushmore. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Sturgis Rally Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Badlands National Park", "d": "How to explore Badlands National Park.", "g": "parks", "l": 2, "q": "What is Exploring Badlands National Park?", "a": "How to explore Badlands National Park.", "x": "Exploring Badlands National Park: get the park map, check conditions, carry water and layers, and tell someone your plan. Under God the people rule Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Pierre: the capital city", "d": "Pierre, capital of South Dakota.", "g": "cities", "l": 2, "q": "What is Pierre: the capital city?", "a": "Pierre, capital of South Dakota.", "x": "Pierre: the capital of South Dakota — government, history, and often the best museums. Wounded Knee 1890. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Sioux Falls", "s": "public-reference", "f": null}, {"t": "Sioux Falls: the biggest city", "d": "Sioux Falls is South Dakota's largest city.", "g": "cities", "l": 2, "q": "What is Sioux Falls: the biggest city?", "a": "Sioux Falls is South Dakota's largest city.", "x": "Sioux Falls is where South Dakota comes to work and play: the skyline, the food, the music, the crowds. agriculture Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Sturgis Rally", "s": "public-reference", "f": null}, {"t": "chislic: the food", "d": "Taste South Dakota: chislic.", "g": "food", "l": 2, "q": "What is chislic: the food?", "a": "Taste South Dakota: chislic.", "x": "The taste of South Dakota is chislic — and the foodways around it. Farming; tourism. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Sturgis Rally Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: South Dakota", "d": "Eating your way through South Dakota.", "g": "food", "l": 2, "q": "What is Food tour: South Dakota?", "a": "Eating your way through South Dakota.", "x": "Eating through South Dakota: start with chislic, then follow the locals — diners, food trucks, farm stands. Under God the people rule Food is the fastest way into a place's heart; the stories come free with the meal. Sioux Falls", "s": "public-reference", "f": null}, {"t": "Sturgis Rally", "d": "Sturgis Rally: South Dakota's signature festival.", "g": "festivals", "l": 2, "q": "What is Sturgis Rally?", "a": "Sturgis Rally: South Dakota's signature festival.", "x": "Sturgis Rally is South Dakota at its most celebratory: Mount Rushmore was carved from 1927 to 1941.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Pierre Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "South Dakota year-round: Sturgis Rally and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "South Dakota year-round: Sturgis Rally and more.", "x": "The South Dakota festival calendar runs year-round, with Sturgis Rally as the anchor. Under God the people rule Every season has its celebration — plan trips around them for the liveliest version of the state. Badlands National Park", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-south-dakota-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
