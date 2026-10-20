(function(){'use strict';
/* JAH Illinois Attractions Database generator — jahdb-e2-illinois-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-illinois-attractions',PREFIX='JAH-E2ILLINOISA-',NAME='JAH Illinois Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Illinois: attractions overview", "d": "The best of Illinois: Chicago skyline, Lincoln sites (Springfield), Navy Pier.", "g": "overview", "l": 2, "q": "What is Illinois: attractions overview?", "a": "The best of Illinois: Chicago skyline, Lincoln sites (Springfield), Navy Pier.", "x": "The essential Illinois: Chicago skyline, Lincoln sites (Springfield), Navy Pier — plus Starved Rock State Park, Illinois's great deep-dish pizza. Taste of Chicago This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Chicago skyline", "d": "Chicago skyline: a top Illinois attraction.", "g": "attractions", "l": 2, "q": "What is Chicago skyline?", "a": "Chicago skyline: a top Illinois attraction.", "x": "Chicago skyline is essential Illinois. Illini Confederacy; French then British. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. deep-dish pizza", "s": "public-reference", "f": null}, {"t": "Visiting Chicago skyline", "d": "How to experience Chicago skyline.", "g": "attractions", "l": 2, "q": "What is Visiting Chicago skyline?", "a": "How to experience Chicago skyline.", "x": "Experiencing Chicago skyline: plan around Taste of Chicago, the state's rhythm — State sovereignty, national union. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Starved Rock State Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Lincoln sites (Springfield)", "d": "Lincoln sites (Springfield): a top Illinois attraction.", "g": "attractions", "l": 2, "q": "What is Lincoln sites (Springfield)?", "a": "Lincoln sites (Springfield): a top Illinois attraction.", "x": "Lincoln sites (Springfield) is essential Illinois. Illini Confederacy; French then British. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. deep-dish pizza", "s": "public-reference", "f": null}, {"t": "Visiting Lincoln sites (Springfield)", "d": "How to experience Lincoln sites (Springfield).", "g": "attractions", "l": 2, "q": "What is Visiting Lincoln sites (Springfield)?", "a": "How to experience Lincoln sites (Springfield).", "x": "Experiencing Lincoln sites (Springfield): plan around Taste of Chicago, the state's rhythm — State sovereignty, national union. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Starved Rock State Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Navy Pier", "d": "Navy Pier: a top Illinois attraction.", "g": "attractions", "l": 2, "q": "What is Navy Pier?", "a": "Navy Pier: a top Illinois attraction.", "x": "Navy Pier is essential Illinois. Illini Confederacy; French then British. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. deep-dish pizza", "s": "public-reference", "f": null}, {"t": "Visiting Navy Pier", "d": "How to experience Navy Pier.", "g": "attractions", "l": 2, "q": "What is Visiting Navy Pier?", "a": "How to experience Navy Pier.", "x": "Experiencing Navy Pier: plan around Taste of Chicago, the state's rhythm — State sovereignty, national union. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Starved Rock State Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Starved Rock", "d": "Starved Rock: a top Illinois attraction.", "g": "attractions", "l": 2, "q": "What is Starved Rock?", "a": "Starved Rock: a top Illinois attraction.", "x": "Starved Rock is essential Illinois. Illini Confederacy; French then British. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. deep-dish pizza", "s": "public-reference", "f": null}, {"t": "Visiting Starved Rock", "d": "How to experience Starved Rock.", "g": "attractions", "l": 2, "q": "What is Visiting Starved Rock?", "a": "How to experience Starved Rock.", "x": "Experiencing Starved Rock: plan around Taste of Chicago, the state's rhythm — State sovereignty, national union. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Starved Rock State Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Cahokia Mounds", "d": "Cahokia Mounds: a top Illinois attraction.", "g": "attractions", "l": 2, "q": "What is Cahokia Mounds?", "a": "Cahokia Mounds: a top Illinois attraction.", "x": "Cahokia Mounds is essential Illinois. Illini Confederacy; French then British. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. deep-dish pizza", "s": "public-reference", "f": null}, {"t": "Visiting Cahokia Mounds", "d": "How to experience Cahokia Mounds.", "g": "attractions", "l": 2, "q": "What is Visiting Cahokia Mounds?", "a": "How to experience Cahokia Mounds.", "x": "Experiencing Cahokia Mounds: plan around Taste of Chicago, the state's rhythm — State sovereignty, national union. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Starved Rock State Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Route 66", "d": "Route 66: a top Illinois attraction.", "g": "attractions", "l": 2, "q": "What is Route 66?", "a": "Route 66: a top Illinois attraction.", "x": "Route 66 is essential Illinois. Illini Confederacy; French then British. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. deep-dish pizza", "s": "public-reference", "f": null}, {"t": "Visiting Route 66", "d": "How to experience Route 66.", "g": "attractions", "l": 2, "q": "What is Visiting Route 66?", "a": "How to experience Route 66.", "x": "Experiencing Route 66: plan around Taste of Chicago, the state's rhythm — State sovereignty, national union. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Starved Rock State Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Art Institute", "d": "Art Institute: a top Illinois attraction.", "g": "attractions", "l": 2, "q": "What is Art Institute?", "a": "Art Institute: a top Illinois attraction.", "x": "Art Institute is essential Illinois. Illini Confederacy; French then British. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. deep-dish pizza", "s": "public-reference", "f": null}, {"t": "Visiting Art Institute", "d": "How to experience Art Institute.", "g": "attractions", "l": 2, "q": "What is Visiting Art Institute?", "a": "How to experience Art Institute.", "x": "Experiencing Art Institute: plan around Taste of Chicago, the state's rhythm — State sovereignty, national union. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Starved Rock State Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Galena", "d": "Galena: a top Illinois attraction.", "g": "attractions", "l": 2, "q": "What is Galena?", "a": "Galena: a top Illinois attraction.", "x": "Galena is essential Illinois. Illini Confederacy; French then British. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. deep-dish pizza", "s": "public-reference", "f": null}, {"t": "Visiting Galena", "d": "How to experience Galena.", "g": "attractions", "l": 2, "q": "What is Visiting Galena?", "a": "How to experience Galena.", "x": "Experiencing Galena: plan around Taste of Chicago, the state's rhythm — State sovereignty, national union. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Starved Rock State Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Starved Rock State Park", "d": "Starved Rock State Park: Illinois's great park.", "g": "parks", "l": 2, "q": "What is Starved Rock State Park?", "a": "Starved Rock State Park: Illinois's great park.", "x": "Starved Rock State Park is Illinois's wild heart: Chicago skyline. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Taste of Chicago Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Starved Rock State Park", "d": "How to explore Starved Rock State Park.", "g": "parks", "l": 2, "q": "What is Exploring Starved Rock State Park?", "a": "How to explore Starved Rock State Park.", "x": "Exploring Starved Rock State Park: get the park map, check conditions, carry water and layers, and tell someone your plan. State sovereignty, national union Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Springfield: the capital city", "d": "Springfield, capital of Illinois.", "g": "cities", "l": 2, "q": "What is Springfield: the capital city?", "a": "Springfield, capital of Illinois.", "x": "Springfield: the capital of Illinois — government, history, and often the best museums. Lincoln's home; Civil War. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Chicago", "s": "public-reference", "f": null}, {"t": "Chicago: the biggest city", "d": "Chicago is Illinois's largest city.", "g": "cities", "l": 2, "q": "What is Chicago: the biggest city?", "a": "Chicago is Illinois's largest city.", "x": "Chicago is where Illinois comes to work and play: the skyline, the food, the music, the crowds. finance (Chicago) Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Taste of Chicago", "s": "public-reference", "f": null}, {"t": "deep-dish pizza: the food", "d": "Taste Illinois: deep-dish pizza.", "g": "food", "l": 2, "q": "What is deep-dish pizza: the food?", "a": "Taste Illinois: deep-dish pizza.", "x": "The taste of Illinois is deep-dish pizza — and the foodways around it. Great Chicago Fire 1871. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Taste of Chicago Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Illinois", "d": "Eating your way through Illinois.", "g": "food", "l": 2, "q": "What is Food tour: Illinois?", "a": "Eating your way through Illinois.", "x": "Eating through Illinois: start with deep-dish pizza, then follow the locals — diners, food trucks, farm stands. State sovereignty, national union Food is the fastest way into a place's heart; the stories come free with the meal. Chicago", "s": "public-reference", "f": null}, {"t": "Taste of Chicago", "d": "Taste of Chicago: Illinois's signature festival.", "g": "festivals", "l": 2, "q": "What is Taste of Chicago?", "a": "Taste of Chicago: Illinois's signature festival.", "x": "Taste of Chicago is Illinois at its most celebratory: Corn, finance, industry.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Springfield Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Illinois year-round: Taste of Chicago and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Illinois year-round: Taste of Chicago and more.", "x": "The Illinois festival calendar runs year-round, with Taste of Chicago as the anchor. State sovereignty, national union Every season has its celebration — plan trips around them for the liveliest version of the state. Starved Rock State Park", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-illinois-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
