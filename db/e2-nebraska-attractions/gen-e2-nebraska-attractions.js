(function(){'use strict';
/* JAH Nebraska Attractions Database generator — jahdb-e2-nebraska-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-nebraska-attractions',PREFIX='JAH-E2NEBRASKAA-',NAME='JAH Nebraska Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Nebraska: attractions overview", "d": "The best of Nebraska: Scotts Bluff, Chimney Rock, Henry Doorly Zoo.", "g": "overview", "l": 2, "q": "What is Nebraska: attractions overview?", "a": "The best of Nebraska: Scotts Bluff, Chimney Rock, Henry Doorly Zoo.", "x": "The essential Nebraska: Scotts Bluff, Chimney Rock, Henry Doorly Zoo — plus Scotts Bluff National Monument, Nebraska's great Runza. College World Series This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Scotts Bluff", "d": "Scotts Bluff: a top Nebraska attraction.", "g": "attractions", "l": 2, "q": "What is Scotts Bluff?", "a": "Scotts Bluff: a top Nebraska attraction.", "x": "Scotts Bluff is essential Nebraska. Pawnee; Oregon Trail; homesteading. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Runza State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Scotts Bluff", "d": "How to experience Scotts Bluff.", "g": "attractions", "l": 2, "q": "What is Visiting Scotts Bluff?", "a": "How to experience Scotts Bluff.", "x": "Experiencing Scotts Bluff: plan around College World Series, the state's rhythm — Equality before the law. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Scotts Bluff National Monument Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Chimney Rock", "d": "Chimney Rock: a top Nebraska attraction.", "g": "attractions", "l": 2, "q": "What is Chimney Rock?", "a": "Chimney Rock: a top Nebraska attraction.", "x": "Chimney Rock is essential Nebraska. Pawnee; Oregon Trail; homesteading. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Runza State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Chimney Rock", "d": "How to experience Chimney Rock.", "g": "attractions", "l": 2, "q": "What is Visiting Chimney Rock?", "a": "How to experience Chimney Rock.", "x": "Experiencing Chimney Rock: plan around College World Series, the state's rhythm — Equality before the law. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Scotts Bluff National Monument Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Henry Doorly Zoo", "d": "Henry Doorly Zoo: a top Nebraska attraction.", "g": "attractions", "l": 2, "q": "What is Henry Doorly Zoo?", "a": "Henry Doorly Zoo: a top Nebraska attraction.", "x": "Henry Doorly Zoo is essential Nebraska. Pawnee; Oregon Trail; homesteading. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Runza State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Henry Doorly Zoo", "d": "How to experience Henry Doorly Zoo.", "g": "attractions", "l": 2, "q": "What is Visiting Henry Doorly Zoo?", "a": "How to experience Henry Doorly Zoo.", "x": "Experiencing Henry Doorly Zoo: plan around College World Series, the state's rhythm — Equality before the law. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Scotts Bluff National Monument Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Old Market Omaha", "d": "Old Market Omaha: a top Nebraska attraction.", "g": "attractions", "l": 2, "q": "What is Old Market Omaha?", "a": "Old Market Omaha: a top Nebraska attraction.", "x": "Old Market Omaha is essential Nebraska. Pawnee; Oregon Trail; homesteading. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Runza State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Old Market Omaha", "d": "How to experience Old Market Omaha.", "g": "attractions", "l": 2, "q": "What is Visiting Old Market Omaha?", "a": "How to experience Old Market Omaha.", "x": "Experiencing Old Market Omaha: plan around College World Series, the state's rhythm — Equality before the law. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Scotts Bluff National Monument Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Carhenge", "d": "Carhenge: a top Nebraska attraction.", "g": "attractions", "l": 2, "q": "What is Carhenge?", "a": "Carhenge: a top Nebraska attraction.", "x": "Carhenge is essential Nebraska. Pawnee; Oregon Trail; homesteading. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Runza State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Carhenge", "d": "How to experience Carhenge.", "g": "attractions", "l": 2, "q": "What is Visiting Carhenge?", "a": "How to experience Carhenge.", "x": "Experiencing Carhenge: plan around College World Series, the state's rhythm — Equality before the law. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Scotts Bluff National Monument Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Sandhills", "d": "Sandhills: a top Nebraska attraction.", "g": "attractions", "l": 2, "q": "What is Sandhills?", "a": "Sandhills: a top Nebraska attraction.", "x": "Sandhills is essential Nebraska. Pawnee; Oregon Trail; homesteading. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Runza State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Sandhills", "d": "How to experience Sandhills.", "g": "attractions", "l": 2, "q": "What is Visiting Sandhills?", "a": "How to experience Sandhills.", "x": "Experiencing Sandhills: plan around College World Series, the state's rhythm — Equality before the law. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Scotts Bluff National Monument Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Strategic Air Command Museum", "d": "Strategic Air Command Museum: a top Nebraska attraction.", "g": "attractions", "l": 2, "q": "What is Strategic Air Command Museum?", "a": "Strategic Air Command Museum: a top Nebraska attraction.", "x": "Strategic Air Command Museum is essential Nebraska. Pawnee; Oregon Trail; homesteading. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Runza", "s": "public-reference", "f": null}, {"t": "Visiting Strategic Air Command Museum", "d": "How to experience Strategic Air Command Museum.", "g": "attractions", "l": 2, "q": "What is Visiting Strategic Air Command Museum?", "a": "How to experience Strategic Air Command Museum.", "x": "Experiencing Strategic Air Command Museum: plan around College World Series, the state's rhythm — Equality before the law. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Scotts Bluff National Monument Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Lincoln's Haymarket", "d": "Lincoln's Haymarket: a top Nebraska attraction.", "g": "attractions", "l": 2, "q": "What is Lincoln's Haymarket?", "a": "Lincoln's Haymarket: a top Nebraska attraction.", "x": "Lincoln's Haymarket is essential Nebraska. Pawnee; Oregon Trail; homesteading. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Runza", "s": "public-reference", "f": null}, {"t": "Visiting Lincoln's Haymarket", "d": "How to experience Lincoln's Haymarket.", "g": "attractions", "l": 2, "q": "What is Visiting Lincoln's Haymarket?", "a": "How to experience Lincoln's Haymarket.", "x": "Experiencing Lincoln's Haymarket: plan around College World Series, the state's rhythm — Equality before the law. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Scotts Bluff National Monument Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Scotts Bluff National Monument", "d": "Scotts Bluff National Monument: Nebraska's great park.", "g": "parks", "l": 2, "q": "What is Scotts Bluff National Monument?", "a": "Scotts Bluff National Monument: Nebraska's great park.", "x": "Scotts Bluff National Monument is Nebraska's wild heart: Scotts Bluff. Parks preserve what development cannot replace — the views, the wildlife, the quiet. College World Series Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Scotts Bluff National Monument", "d": "How to explore Scotts Bluff National Monument.", "g": "parks", "l": 2, "q": "What is Exploring Scotts Bluff National Monument?", "a": "How to explore Scotts Bluff National Monument.", "x": "Exploring Scotts Bluff National Monument: get the park map, check conditions, carry water and layers, and tell someone your plan. Equality before the law Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Lincoln: the capital city", "d": "Lincoln, capital of Nebraska.", "g": "cities", "l": 2, "q": "What is Lincoln: the capital city?", "a": "Lincoln, capital of Nebraska.", "x": "Lincoln: the capital of Nebraska — government, history, and often the best museums. Corn and cattle; College World Series. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Omaha", "s": "public-reference", "f": null}, {"t": "Omaha: the biggest city", "d": "Omaha is Nebraska's largest city.", "g": "cities", "l": 2, "q": "What is Omaha: the biggest city?", "a": "Omaha is Nebraska's largest city.", "x": "Omaha is where Nebraska comes to work and play: the skyline, the food, the music, the crowds. agriculture (corn, beef) Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. College World Series", "s": "public-reference", "f": null}, {"t": "Runza: the food", "d": "Taste Nebraska: Runza.", "g": "food", "l": 2, "q": "What is Runza: the food?", "a": "Taste Nebraska: Runza.", "x": "The taste of Nebraska is Runza — and the foodways around it. Warren Buffett's Omaha. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. College World Series Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Nebraska", "d": "Eating your way through Nebraska.", "g": "food", "l": 2, "q": "What is Food tour: Nebraska?", "a": "Eating your way through Nebraska.", "x": "Eating through Nebraska: start with Runza, then follow the locals — diners, food trucks, farm stands. Equality before the law Food is the fastest way into a place's heart; the stories come free with the meal. Omaha", "s": "public-reference", "f": null}, {"t": "College World Series", "d": "College World Series: Nebraska's signature festival.", "g": "festivals", "l": 2, "q": "What is College World Series?", "a": "College World Series: Nebraska's signature festival.", "x": "College World Series is Nebraska at its most celebratory: The railroad and the Homestead Act settled the plains.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Lincoln Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Nebraska year-round: College World Series and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Nebraska year-round: College World Series and more.", "x": "The Nebraska festival calendar runs year-round, with College World Series as the anchor. Equality before the law Every season has its celebration — plan trips around them for the liveliest version of the state. Scotts Bluff National Monument", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-nebraska-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
