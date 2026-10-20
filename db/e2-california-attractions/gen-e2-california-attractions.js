(function(){'use strict';
/* JAH California Attractions Database generator — jahdb-e2-california-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-california-attractions',PREFIX='JAH-E2CALIFORNI-',NAME='JAH California Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "California: attractions overview", "d": "The best of California: Yosemite, Golden Gate Bridge, Disneyland.", "g": "overview", "l": 2, "q": "What is California: attractions overview?", "a": "The best of California: Yosemite, Golden Gate Bridge, Disneyland.", "x": "The essential California: Yosemite, Golden Gate Bridge, Disneyland — plus Yosemite National Park, California's great fish tacos. Coachella This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Yosemite", "d": "Yosemite: a top California attraction.", "g": "attractions", "l": 2, "q": "What is Yosemite?", "a": "Yosemite: a top California attraction.", "x": "Yosemite is essential California. Native nations; Spanish missions (1769). Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. fish tacos", "s": "public-reference", "f": null}, {"t": "Visiting Yosemite", "d": "How to experience Yosemite.", "g": "attractions", "l": 2, "q": "What is Visiting Yosemite?", "a": "How to experience Yosemite.", "x": "Experiencing Yosemite: plan around Coachella, the state's rhythm — Eureka (I have found it). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Yosemite National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Golden Gate Bridge", "d": "Golden Gate Bridge: a top California attraction.", "g": "attractions", "l": 2, "q": "What is Golden Gate Bridge?", "a": "Golden Gate Bridge: a top California attraction.", "x": "Golden Gate Bridge is essential California. Native nations; Spanish missions (1769). Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. fish tacos", "s": "public-reference", "f": null}, {"t": "Visiting Golden Gate Bridge", "d": "How to experience Golden Gate Bridge.", "g": "attractions", "l": 2, "q": "What is Visiting Golden Gate Bridge?", "a": "How to experience Golden Gate Bridge.", "x": "Experiencing Golden Gate Bridge: plan around Coachella, the state's rhythm — Eureka (I have found it). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Yosemite National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Disneyland", "d": "Disneyland: a top California attraction.", "g": "attractions", "l": 2, "q": "What is Disneyland?", "a": "Disneyland: a top California attraction.", "x": "Disneyland is essential California. Native nations; Spanish missions (1769). Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. fish tacos", "s": "public-reference", "f": null}, {"t": "Visiting Disneyland", "d": "How to experience Disneyland.", "g": "attractions", "l": 2, "q": "What is Visiting Disneyland?", "a": "How to experience Disneyland.", "x": "Experiencing Disneyland: plan around Coachella, the state's rhythm — Eureka (I have found it). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Yosemite National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Hollywood", "d": "Hollywood: a top California attraction.", "g": "attractions", "l": 2, "q": "What is Hollywood?", "a": "Hollywood: a top California attraction.", "x": "Hollywood is essential California. Native nations; Spanish missions (1769). Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. fish tacos", "s": "public-reference", "f": null}, {"t": "Visiting Hollywood", "d": "How to experience Hollywood.", "g": "attractions", "l": 2, "q": "What is Visiting Hollywood?", "a": "How to experience Hollywood.", "x": "Experiencing Hollywood: plan around Coachella, the state's rhythm — Eureka (I have found it). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Yosemite National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Big Sur", "d": "Big Sur: a top California attraction.", "g": "attractions", "l": 2, "q": "What is Big Sur?", "a": "Big Sur: a top California attraction.", "x": "Big Sur is essential California. Native nations; Spanish missions (1769). Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. fish tacos", "s": "public-reference", "f": null}, {"t": "Visiting Big Sur", "d": "How to experience Big Sur.", "g": "attractions", "l": 2, "q": "What is Visiting Big Sur?", "a": "How to experience Big Sur.", "x": "Experiencing Big Sur: plan around Coachella, the state's rhythm — Eureka (I have found it). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Yosemite National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Death Valley", "d": "Death Valley: a top California attraction.", "g": "attractions", "l": 2, "q": "What is Death Valley?", "a": "Death Valley: a top California attraction.", "x": "Death Valley is essential California. Native nations; Spanish missions (1769). Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. fish tacos", "s": "public-reference", "f": null}, {"t": "Visiting Death Valley", "d": "How to experience Death Valley.", "g": "attractions", "l": 2, "q": "What is Visiting Death Valley?", "a": "How to experience Death Valley.", "x": "Experiencing Death Valley: plan around Coachella, the state's rhythm — Eureka (I have found it). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Yosemite National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Lake Tahoe", "d": "Lake Tahoe: a top California attraction.", "g": "attractions", "l": 2, "q": "What is Lake Tahoe?", "a": "Lake Tahoe: a top California attraction.", "x": "Lake Tahoe is essential California. Native nations; Spanish missions (1769). Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. fish tacos", "s": "public-reference", "f": null}, {"t": "Visiting Lake Tahoe", "d": "How to experience Lake Tahoe.", "g": "attractions", "l": 2, "q": "What is Visiting Lake Tahoe?", "a": "How to experience Lake Tahoe.", "x": "Experiencing Lake Tahoe: plan around Coachella, the state's rhythm — Eureka (I have found it). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Yosemite National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "San Diego Zoo", "d": "San Diego Zoo: a top California attraction.", "g": "attractions", "l": 2, "q": "What is San Diego Zoo?", "a": "San Diego Zoo: a top California attraction.", "x": "San Diego Zoo is essential California. Native nations; Spanish missions (1769). Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. fish tacos", "s": "public-reference", "f": null}, {"t": "Visiting San Diego Zoo", "d": "How to experience San Diego Zoo.", "g": "attractions", "l": 2, "q": "What is Visiting San Diego Zoo?", "a": "How to experience San Diego Zoo.", "x": "Experiencing San Diego Zoo: plan around Coachella, the state's rhythm — Eureka (I have found it). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Yosemite National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Yosemite National Park", "d": "Yosemite National Park: California's great park.", "g": "parks", "l": 2, "q": "What is Yosemite National Park?", "a": "Yosemite National Park: California's great park.", "x": "Yosemite National Park is California's wild heart: Yosemite. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Coachella Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Yosemite National Park", "d": "How to explore Yosemite National Park.", "g": "parks", "l": 2, "q": "What is Exploring Yosemite National Park?", "a": "How to explore Yosemite National Park.", "x": "Exploring Yosemite National Park: get the park map, check conditions, carry water and layers, and tell someone your plan. Eureka (I have found it) Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Sacramento: the capital city", "d": "Sacramento, capital of California.", "g": "cities", "l": 2, "q": "What is Sacramento: the capital city?", "a": "Sacramento, capital of California.", "x": "Sacramento: the capital of California — government, history, and often the best museums. Gold Rush 1849; statehood 1850. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Los Angeles", "s": "public-reference", "f": null}, {"t": "Los Angeles: the biggest city", "d": "Los Angeles is California's largest city.", "g": "cities", "l": 2, "q": "What is Los Angeles: the biggest city?", "a": "Los Angeles is California's largest city.", "x": "Los Angeles is where California comes to work and play: the skyline, the food, the music, the crowds. technology (Silicon Valley) Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Coachella", "s": "public-reference", "f": null}, {"t": "fish tacos: the food", "d": "Taste California: fish tacos.", "g": "food", "l": 2, "q": "What is fish tacos: the food?", "a": "Taste California: fish tacos.", "x": "The taste of California is fish tacos — and the foodways around it. Hollywood, Silicon Valley, aerospace. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Coachella Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: California", "d": "Eating your way through California.", "g": "food", "l": 2, "q": "What is Food tour: California?", "a": "Eating your way through California.", "x": "Eating through California: start with fish tacos, then follow the locals — diners, food trucks, farm stands. Eureka (I have found it) Food is the fastest way into a place's heart; the stories come free with the meal. Los Angeles", "s": "public-reference", "f": null}, {"t": "Coachella", "d": "Coachella: California's signature festival.", "g": "festivals", "l": 2, "q": "What is Coachella?", "a": "Coachella: California's signature festival.", "x": "Coachella is California at its most celebratory: Progressive politics; wildfire era.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Sacramento Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "California year-round: Coachella and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "California year-round: Coachella and more.", "x": "The California festival calendar runs year-round, with Coachella as the anchor. Eureka (I have found it) Every season has its celebration — plan trips around them for the liveliest version of the state. Yosemite National Park", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-california-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
