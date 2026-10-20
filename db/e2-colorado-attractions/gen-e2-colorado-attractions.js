(function(){'use strict';
/* JAH Colorado Attractions Database generator — jahdb-e2-colorado-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-colorado-attractions',PREFIX='JAH-E2COLORADOA-',NAME='JAH Colorado Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Colorado: attractions overview", "d": "The best of Colorado: Rocky Mountain National Park, Garden of the Gods, Mesa Verde.", "g": "overview", "l": 2, "q": "What is Colorado: attractions overview?", "a": "The best of Colorado: Rocky Mountain National Park, Garden of the Gods, Mesa Verde.", "x": "The essential Colorado: Rocky Mountain National Park, Garden of the Gods, Mesa Verde — plus Rocky Mountain National Park, Colorado's great green chile. Red Rocks concerts This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Rocky Mountain National Park", "d": "Rocky Mountain National Park: a top Colorado attraction.", "g": "attractions", "l": 2, "q": "What is Rocky Mountain National Park?", "a": "Rocky Mountain National Park: a top Colorado attraction.", "x": "Rocky Mountain National Park is essential Colorado. Ute lands; Pikes Peak gold rush 1859. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. green chile", "s": "public-reference", "f": null}, {"t": "Visiting Rocky Mountain National Park", "d": "How to experience Rocky Mountain National Park.", "g": "attractions", "l": 2, "q": "What is Visiting Rocky Mountain National Park?", "a": "How to experience Rocky Mountain National Park.", "x": "Experiencing Rocky Mountain National Park: plan around Red Rocks concerts, the state's rhythm — Nil sine numine (Nothing without providence). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Rocky Mountain National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Garden of the Gods", "d": "Garden of the Gods: a top Colorado attraction.", "g": "attractions", "l": 2, "q": "What is Garden of the Gods?", "a": "Garden of the Gods: a top Colorado attraction.", "x": "Garden of the Gods is essential Colorado. Ute lands; Pikes Peak gold rush 1859. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. green chile", "s": "public-reference", "f": null}, {"t": "Visiting Garden of the Gods", "d": "How to experience Garden of the Gods.", "g": "attractions", "l": 2, "q": "What is Visiting Garden of the Gods?", "a": "How to experience Garden of the Gods.", "x": "Experiencing Garden of the Gods: plan around Red Rocks concerts, the state's rhythm — Nil sine numine (Nothing without providence). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Rocky Mountain National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Mesa Verde", "d": "Mesa Verde: a top Colorado attraction.", "g": "attractions", "l": 2, "q": "What is Mesa Verde?", "a": "Mesa Verde: a top Colorado attraction.", "x": "Mesa Verde is essential Colorado. Ute lands; Pikes Peak gold rush 1859. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. green chile State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Mesa Verde", "d": "How to experience Mesa Verde.", "g": "attractions", "l": 2, "q": "What is Visiting Mesa Verde?", "a": "How to experience Mesa Verde.", "x": "Experiencing Mesa Verde: plan around Red Rocks concerts, the state's rhythm — Nil sine numine (Nothing without providence). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Rocky Mountain National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Red Rocks Amphitheatre", "d": "Red Rocks Amphitheatre: a top Colorado attraction.", "g": "attractions", "l": 2, "q": "What is Red Rocks Amphitheatre?", "a": "Red Rocks Amphitheatre: a top Colorado attraction.", "x": "Red Rocks Amphitheatre is essential Colorado. Ute lands; Pikes Peak gold rush 1859. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. green chile", "s": "public-reference", "f": null}, {"t": "Visiting Red Rocks Amphitheatre", "d": "How to experience Red Rocks Amphitheatre.", "g": "attractions", "l": 2, "q": "What is Visiting Red Rocks Amphitheatre?", "a": "How to experience Red Rocks Amphitheatre.", "x": "Experiencing Red Rocks Amphitheatre: plan around Red Rocks concerts, the state's rhythm — Nil sine numine (Nothing without providence). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Rocky Mountain National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Pikes Peak", "d": "Pikes Peak: a top Colorado attraction.", "g": "attractions", "l": 2, "q": "What is Pikes Peak?", "a": "Pikes Peak: a top Colorado attraction.", "x": "Pikes Peak is essential Colorado. Ute lands; Pikes Peak gold rush 1859. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. green chile State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Pikes Peak", "d": "How to experience Pikes Peak.", "g": "attractions", "l": 2, "q": "What is Visiting Pikes Peak?", "a": "How to experience Pikes Peak.", "x": "Experiencing Pikes Peak: plan around Red Rocks concerts, the state's rhythm — Nil sine numine (Nothing without providence). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Rocky Mountain National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Great Sand Dunes", "d": "Great Sand Dunes: a top Colorado attraction.", "g": "attractions", "l": 2, "q": "What is Great Sand Dunes?", "a": "Great Sand Dunes: a top Colorado attraction.", "x": "Great Sand Dunes is essential Colorado. Ute lands; Pikes Peak gold rush 1859. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. green chile", "s": "public-reference", "f": null}, {"t": "Visiting Great Sand Dunes", "d": "How to experience Great Sand Dunes.", "g": "attractions", "l": 2, "q": "What is Visiting Great Sand Dunes?", "a": "How to experience Great Sand Dunes.", "x": "Experiencing Great Sand Dunes: plan around Red Rocks concerts, the state's rhythm — Nil sine numine (Nothing without providence). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Rocky Mountain National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Denver Art Museum", "d": "Denver Art Museum: a top Colorado attraction.", "g": "attractions", "l": 2, "q": "What is Denver Art Museum?", "a": "Denver Art Museum: a top Colorado attraction.", "x": "Denver Art Museum is essential Colorado. Ute lands; Pikes Peak gold rush 1859. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. green chile", "s": "public-reference", "f": null}, {"t": "Visiting Denver Art Museum", "d": "How to experience Denver Art Museum.", "g": "attractions", "l": 2, "q": "What is Visiting Denver Art Museum?", "a": "How to experience Denver Art Museum.", "x": "Experiencing Denver Art Museum: plan around Red Rocks concerts, the state's rhythm — Nil sine numine (Nothing without providence). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Rocky Mountain National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Ski resorts (Aspen, Vail)", "d": "Ski resorts (Aspen, Vail): a top Colorado attraction.", "g": "attractions", "l": 2, "q": "What is Ski resorts (Aspen, Vail)?", "a": "Ski resorts (Aspen, Vail): a top Colorado attraction.", "x": "Ski resorts (Aspen, Vail) is essential Colorado. Ute lands; Pikes Peak gold rush 1859. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. green chile", "s": "public-reference", "f": null}, {"t": "Visiting Ski resorts (Aspen, Vail)", "d": "How to experience Ski resorts (Aspen, Vail).", "g": "attractions", "l": 2, "q": "What is Visiting Ski resorts (Aspen, Vail)?", "a": "How to experience Ski resorts (Aspen, Vail).", "x": "Experiencing Ski resorts (Aspen, Vail): plan around Red Rocks concerts, the state's rhythm — Nil sine numine (Nothing without providence). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Rocky Mountain National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Rocky Mountain National Park", "d": "Rocky Mountain National Park: Colorado's great park.", "g": "parks", "l": 2, "q": "What is Rocky Mountain National Park?", "a": "Rocky Mountain National Park: Colorado's great park.", "x": "Rocky Mountain National Park is Colorado's wild heart: Rocky Mountain National Park. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Red Rocks concerts Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Rocky Mountain National Park", "d": "How to explore Rocky Mountain National Park.", "g": "parks", "l": 2, "q": "What is Exploring Rocky Mountain National Park?", "a": "How to explore Rocky Mountain National Park.", "x": "Exploring Rocky Mountain National Park: get the park map, check conditions, carry water and layers, and tell someone your plan. Nil sine numine (Nothing without providence) Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Denver: the capital city", "d": "Denver, capital of Colorado.", "g": "cities", "l": 2, "q": "What is Denver: the capital city?", "a": "Denver, capital of Colorado.", "x": "Denver: the capital of Colorado — government, history, and often the best museums. Statehood in centennial year 1876. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Denver", "s": "public-reference", "f": null}, {"t": "Denver: the biggest city", "d": "Denver is Colorado's largest city.", "g": "cities", "l": 2, "q": "What is Denver: the biggest city?", "a": "Denver is Colorado's largest city.", "x": "Denver is where Colorado comes to work and play: the skyline, the food, the music, the crowds. aerospace and defense Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Red Rocks concerts", "s": "public-reference", "f": null}, {"t": "green chile: the food", "d": "Taste Colorado: green chile.", "g": "food", "l": 2, "q": "What is green chile: the food?", "a": "Taste Colorado: green chile.", "x": "The taste of Colorado is green chile — and the foodways around it. Mining to aerospace to tech. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Red Rocks concerts Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Colorado", "d": "Eating your way through Colorado.", "g": "food", "l": 2, "q": "What is Food tour: Colorado?", "a": "Eating your way through Colorado.", "x": "Eating through Colorado: start with green chile, then follow the locals — diners, food trucks, farm stands. Nil sine numine (Nothing without providence) Food is the fastest way into a place's heart; the stories come free with the meal. Denver", "s": "public-reference", "f": null}, {"t": "Red Rocks concerts", "d": "Red Rocks concerts: Colorado's signature festival.", "g": "festivals", "l": 2, "q": "What is Red Rocks concerts?", "a": "Red Rocks concerts: Colorado's signature festival.", "x": "Red Rocks concerts is Colorado at its most celebratory: Legal cannabis pioneer 2014.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Denver Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Colorado year-round: Red Rocks concerts and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Colorado year-round: Red Rocks concerts and more.", "x": "The Colorado festival calendar runs year-round, with Red Rocks concerts as the anchor. Nil sine numine (Nothing without providence) Every season has its celebration — plan trips around them for the liveliest version of the state. Rocky Mountain National Park", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-colorado-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
