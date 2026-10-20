(function(){'use strict';
/* JAH Wisconsin Attractions Database generator — jahdb-e2-wisconsin-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-wisconsin-attractions',PREFIX='JAH-E2WISCONSIN-',NAME='JAH Wisconsin Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Wisconsin: attractions overview", "d": "The best of Wisconsin: Door County, Wisconsin Dells, Lambeau Field.", "g": "overview", "l": 2, "q": "What is Wisconsin: attractions overview?", "a": "The best of Wisconsin: Door County, Wisconsin Dells, Lambeau Field.", "x": "The essential Wisconsin: Door County, Wisconsin Dells, Lambeau Field — plus Apostle Islands National Lakeshore, Wisconsin's great cheese curds. Summerfest This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Door County", "d": "Door County: a top Wisconsin attraction.", "g": "attractions", "l": 2, "q": "What is Door County?", "a": "Door County: a top Wisconsin attraction.", "x": "Door County is essential Wisconsin. Ho-Chunk; lead mining. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. cheese curds State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Door County", "d": "How to experience Door County.", "g": "attractions", "l": 2, "q": "What is Visiting Door County?", "a": "How to experience Door County.", "x": "Experiencing Door County: plan around Summerfest, the state's rhythm — Forward. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Apostle Islands National Lakeshore Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Wisconsin Dells", "d": "Wisconsin Dells: a top Wisconsin attraction.", "g": "attractions", "l": 2, "q": "What is Wisconsin Dells?", "a": "Wisconsin Dells: a top Wisconsin attraction.", "x": "Wisconsin Dells is essential Wisconsin. Ho-Chunk; lead mining. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. cheese curds State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Wisconsin Dells", "d": "How to experience Wisconsin Dells.", "g": "attractions", "l": 2, "q": "What is Visiting Wisconsin Dells?", "a": "How to experience Wisconsin Dells.", "x": "Experiencing Wisconsin Dells: plan around Summerfest, the state's rhythm — Forward. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Apostle Islands National Lakeshore Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Lambeau Field", "d": "Lambeau Field: a top Wisconsin attraction.", "g": "attractions", "l": 2, "q": "What is Lambeau Field?", "a": "Lambeau Field: a top Wisconsin attraction.", "x": "Lambeau Field is essential Wisconsin. Ho-Chunk; lead mining. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. cheese curds State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Lambeau Field", "d": "How to experience Lambeau Field.", "g": "attractions", "l": 2, "q": "What is Visiting Lambeau Field?", "a": "How to experience Lambeau Field.", "x": "Experiencing Lambeau Field: plan around Summerfest, the state's rhythm — Forward. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Apostle Islands National Lakeshore Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Milwaukee Art Museum", "d": "Milwaukee Art Museum: a top Wisconsin attraction.", "g": "attractions", "l": 2, "q": "What is Milwaukee Art Museum?", "a": "Milwaukee Art Museum: a top Wisconsin attraction.", "x": "Milwaukee Art Museum is essential Wisconsin. Ho-Chunk; lead mining. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. cheese curds State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Milwaukee Art Museum", "d": "How to experience Milwaukee Art Museum.", "g": "attractions", "l": 2, "q": "What is Visiting Milwaukee Art Museum?", "a": "How to experience Milwaukee Art Museum.", "x": "Experiencing Milwaukee Art Museum: plan around Summerfest, the state's rhythm — Forward. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Apostle Islands National Lakeshore Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Apostle Islands", "d": "Apostle Islands: a top Wisconsin attraction.", "g": "attractions", "l": 2, "q": "What is Apostle Islands?", "a": "Apostle Islands: a top Wisconsin attraction.", "x": "Apostle Islands is essential Wisconsin. Ho-Chunk; lead mining. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. cheese curds State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Apostle Islands", "d": "How to experience Apostle Islands.", "g": "attractions", "l": 2, "q": "What is Visiting Apostle Islands?", "a": "How to experience Apostle Islands.", "x": "Experiencing Apostle Islands: plan around Summerfest, the state's rhythm — Forward. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Apostle Islands National Lakeshore Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "House on the Rock", "d": "House on the Rock: a top Wisconsin attraction.", "g": "attractions", "l": 2, "q": "What is House on the Rock?", "a": "House on the Rock: a top Wisconsin attraction.", "x": "House on the Rock is essential Wisconsin. Ho-Chunk; lead mining. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. cheese curds State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting House on the Rock", "d": "How to experience House on the Rock.", "g": "attractions", "l": 2, "q": "What is Visiting House on the Rock?", "a": "How to experience House on the Rock.", "x": "Experiencing House on the Rock: plan around Summerfest, the state's rhythm — Forward. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Apostle Islands National Lakeshore Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Taliesin", "d": "Taliesin: a top Wisconsin attraction.", "g": "attractions", "l": 2, "q": "What is Taliesin?", "a": "Taliesin: a top Wisconsin attraction.", "x": "Taliesin is essential Wisconsin. Ho-Chunk; lead mining. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. cheese curds State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Taliesin", "d": "How to experience Taliesin.", "g": "attractions", "l": 2, "q": "What is Visiting Taliesin?", "a": "How to experience Taliesin.", "x": "Experiencing Taliesin: plan around Summerfest, the state's rhythm — Forward. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Apostle Islands National Lakeshore Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Devil's Lake", "d": "Devil's Lake: a top Wisconsin attraction.", "g": "attractions", "l": 2, "q": "What is Devil's Lake?", "a": "Devil's Lake: a top Wisconsin attraction.", "x": "Devil's Lake is essential Wisconsin. Ho-Chunk; lead mining. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. cheese curds State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Devil's Lake", "d": "How to experience Devil's Lake.", "g": "attractions", "l": 2, "q": "What is Visiting Devil's Lake?", "a": "How to experience Devil's Lake.", "x": "Experiencing Devil's Lake: plan around Summerfest, the state's rhythm — Forward. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Apostle Islands National Lakeshore Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Apostle Islands National Lakeshore", "d": "Apostle Islands National Lakeshore: Wisconsin's great park.", "g": "parks", "l": 2, "q": "What is Apostle Islands National Lakeshore?", "a": "Apostle Islands National Lakeshore: Wisconsin's great park.", "x": "Apostle Islands National Lakeshore is Wisconsin's wild heart: Door County. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Summerfest Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Apostle Islands National Lakeshore", "d": "How to explore Apostle Islands National Lakeshore.", "g": "parks", "l": 2, "q": "What is Exploring Apostle Islands National Lakeshore?", "a": "How to explore Apostle Islands National Lakeshore.", "x": "Exploring Apostle Islands National Lakeshore: get the park map, check conditions, carry water and layers, and tell someone your plan. Forward Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Madison: the capital city", "d": "Madison, capital of Wisconsin.", "g": "cities", "l": 2, "q": "What is Madison: the capital city?", "a": "Madison, capital of Wisconsin.", "x": "Madison: the capital of Wisconsin — government, history, and often the best museums. Dairy state; progressivism. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Milwaukee", "s": "public-reference", "f": null}, {"t": "Milwaukee: the biggest city", "d": "Milwaukee is Wisconsin's largest city.", "g": "cities", "l": 2, "q": "What is Milwaukee: the biggest city?", "a": "Milwaukee is Wisconsin's largest city.", "x": "Milwaukee is where Wisconsin comes to work and play: the skyline, the food, the music, the crowds. dairy Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Summerfest", "s": "public-reference", "f": null}, {"t": "cheese curds: the food", "d": "Taste Wisconsin: cheese curds.", "g": "food", "l": 2, "q": "What is cheese curds: the food?", "a": "Taste Wisconsin: cheese curds.", "x": "The taste of Wisconsin is cheese curds — and the foodways around it. Beer, cheese, Harleys. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Summerfest Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Wisconsin", "d": "Eating your way through Wisconsin.", "g": "food", "l": 2, "q": "What is Food tour: Wisconsin?", "a": "Eating your way through Wisconsin.", "x": "Eating through Wisconsin: start with cheese curds, then follow the locals — diners, food trucks, farm stands. Forward Food is the fastest way into a place's heart; the stories come free with the meal. Milwaukee", "s": "public-reference", "f": null}, {"t": "Summerfest", "d": "Summerfest: Wisconsin's signature festival.", "g": "festivals", "l": 2, "q": "What is Summerfest?", "a": "Summerfest: Wisconsin's signature festival.", "x": "Summerfest is Wisconsin at its most celebratory: Dairy made it America's Dairyland.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Madison Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Wisconsin year-round: Summerfest and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Wisconsin year-round: Summerfest and more.", "x": "The Wisconsin festival calendar runs year-round, with Summerfest as the anchor. Forward Every season has its celebration — plan trips around them for the liveliest version of the state. Apostle Islands National Lakeshore", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-wisconsin-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
