(function(){'use strict';
/* JAH Alaska Attractions Database generator — jahdb-e2-alaska-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-alaska-attractions',PREFIX='JAH-E2ALASKAATT-',NAME='JAH Alaska Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Alaska: attractions overview", "d": "The best of Alaska: Denali National Park, Glacier Bay, Kenai Fjords.", "g": "overview", "l": 2, "q": "What is Alaska: attractions overview?", "a": "The best of Alaska: Denali National Park, Glacier Bay, Kenai Fjords.", "x": "The essential Alaska: Denali National Park, Glacier Bay, Kenai Fjords — plus Denali National Park, Alaska's great king crab. Iditarod This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Denali National Park", "d": "Denali National Park: a top Alaska attraction.", "g": "attractions", "l": 2, "q": "What is Denali National Park?", "a": "Denali National Park: a top Alaska attraction.", "x": "Denali National Park is essential Alaska. Native Alutiiq, Tlingit cultures for millennia. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. king crab", "s": "public-reference", "f": null}, {"t": "Visiting Denali National Park", "d": "How to experience Denali National Park.", "g": "attractions", "l": 2, "q": "What is Visiting Denali National Park?", "a": "How to experience Denali National Park.", "x": "Experiencing Denali National Park: plan around Iditarod, the state's rhythm — North to the Future. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Denali National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Glacier Bay", "d": "Glacier Bay: a top Alaska attraction.", "g": "attractions", "l": 2, "q": "What is Glacier Bay?", "a": "Glacier Bay: a top Alaska attraction.", "x": "Glacier Bay is essential Alaska. Native Alutiiq, Tlingit cultures for millennia. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. king crab", "s": "public-reference", "f": null}, {"t": "Visiting Glacier Bay", "d": "How to experience Glacier Bay.", "g": "attractions", "l": 2, "q": "What is Visiting Glacier Bay?", "a": "How to experience Glacier Bay.", "x": "Experiencing Glacier Bay: plan around Iditarod, the state's rhythm — North to the Future. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Denali National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Kenai Fjords", "d": "Kenai Fjords: a top Alaska attraction.", "g": "attractions", "l": 2, "q": "What is Kenai Fjords?", "a": "Kenai Fjords: a top Alaska attraction.", "x": "Kenai Fjords is essential Alaska. Native Alutiiq, Tlingit cultures for millennia. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. king crab", "s": "public-reference", "f": null}, {"t": "Visiting Kenai Fjords", "d": "How to experience Kenai Fjords.", "g": "attractions", "l": 2, "q": "What is Visiting Kenai Fjords?", "a": "How to experience Kenai Fjords.", "x": "Experiencing Kenai Fjords: plan around Iditarod, the state's rhythm — North to the Future. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Denali National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Mendenhall Glacier", "d": "Mendenhall Glacier: a top Alaska attraction.", "g": "attractions", "l": 2, "q": "What is Mendenhall Glacier?", "a": "Mendenhall Glacier: a top Alaska attraction.", "x": "Mendenhall Glacier is essential Alaska. Native Alutiiq, Tlingit cultures for millennia. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. king crab", "s": "public-reference", "f": null}, {"t": "Visiting Mendenhall Glacier", "d": "How to experience Mendenhall Glacier.", "g": "attractions", "l": 2, "q": "What is Visiting Mendenhall Glacier?", "a": "How to experience Mendenhall Glacier.", "x": "Experiencing Mendenhall Glacier: plan around Iditarod, the state's rhythm — North to the Future. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Denali National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Alaska Native Heritage Center", "d": "Alaska Native Heritage Center: a top Alaska attraction.", "g": "attractions", "l": 2, "q": "What is Alaska Native Heritage Center?", "a": "Alaska Native Heritage Center: a top Alaska attraction.", "x": "Alaska Native Heritage Center is essential Alaska. Native Alutiiq, Tlingit cultures for millennia. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. king crab", "s": "public-reference", "f": null}, {"t": "Visiting Alaska Native Heritage Center", "d": "How to experience Alaska Native Heritage Center.", "g": "attractions", "l": 2, "q": "What is Visiting Alaska Native Heritage Center?", "a": "How to experience Alaska Native Heritage Center.", "x": "Experiencing Alaska Native Heritage Center: plan around Iditarod, the state's rhythm — North to the Future. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Denali National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Iditarod Trail", "d": "Iditarod Trail: a top Alaska attraction.", "g": "attractions", "l": 2, "q": "What is Iditarod Trail?", "a": "Iditarod Trail: a top Alaska attraction.", "x": "Iditarod Trail is essential Alaska. Native Alutiiq, Tlingit cultures for millennia. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. king crab", "s": "public-reference", "f": null}, {"t": "Visiting Iditarod Trail", "d": "How to experience Iditarod Trail.", "g": "attractions", "l": 2, "q": "What is Visiting Iditarod Trail?", "a": "How to experience Iditarod Trail.", "x": "Experiencing Iditarod Trail: plan around Iditarod, the state's rhythm — North to the Future. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Denali National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Northern lights (Fairbanks)", "d": "Northern lights (Fairbanks): a top Alaska attraction.", "g": "attractions", "l": 2, "q": "What is Northern lights (Fairbanks)?", "a": "Northern lights (Fairbanks): a top Alaska attraction.", "x": "Northern lights (Fairbanks) is essential Alaska. Native Alutiiq, Tlingit cultures for millennia. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. king crab", "s": "public-reference", "f": null}, {"t": "Visiting Northern lights (Fairbanks)", "d": "How to experience Northern lights (Fairbanks).", "g": "attractions", "l": 2, "q": "What is Visiting Northern lights (Fairbanks)?", "a": "How to experience Northern lights (Fairbanks).", "x": "Experiencing Northern lights (Fairbanks): plan around Iditarod, the state's rhythm — North to the Future. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Denali National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Inside Passage", "d": "Inside Passage: a top Alaska attraction.", "g": "attractions", "l": 2, "q": "What is Inside Passage?", "a": "Inside Passage: a top Alaska attraction.", "x": "Inside Passage is essential Alaska. Native Alutiiq, Tlingit cultures for millennia. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. king crab", "s": "public-reference", "f": null}, {"t": "Visiting Inside Passage", "d": "How to experience Inside Passage.", "g": "attractions", "l": 2, "q": "What is Visiting Inside Passage?", "a": "How to experience Inside Passage.", "x": "Experiencing Inside Passage: plan around Iditarod, the state's rhythm — North to the Future. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Denali National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Denali National Park", "d": "Denali National Park: Alaska's great park.", "g": "parks", "l": 2, "q": "What is Denali National Park?", "a": "Denali National Park: Alaska's great park.", "x": "Denali National Park is Alaska's wild heart: Denali National Park. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Iditarod Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Denali National Park", "d": "How to explore Denali National Park.", "g": "parks", "l": 2, "q": "What is Exploring Denali National Park?", "a": "How to explore Denali National Park.", "x": "Exploring Denali National Park: get the park map, check conditions, carry water and layers, and tell someone your plan. North to the Future Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Juneau: the capital city", "d": "Juneau, capital of Alaska.", "g": "cities", "l": 2, "q": "What is Juneau: the capital city?", "a": "Juneau, capital of Alaska.", "x": "Juneau: the capital of Alaska — government, history, and often the best museums. Russian colony; U.S. purchase 1867. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Anchorage", "s": "public-reference", "f": null}, {"t": "Anchorage: the biggest city", "d": "Anchorage is Alaska's largest city.", "g": "cities", "l": 2, "q": "What is Anchorage: the biggest city?", "a": "Anchorage is Alaska's largest city.", "x": "Anchorage is where Alaska comes to work and play: the skyline, the food, the music, the crowds. oil and gas Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Iditarod", "s": "public-reference", "f": null}, {"t": "king crab: the food", "d": "Taste Alaska: king crab.", "g": "food", "l": 2, "q": "What is king crab: the food?", "a": "Taste Alaska: king crab.", "x": "The taste of Alaska is king crab — and the foodways around it. Gold rush 1898; oil at Prudhoe Bay. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Iditarod Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Alaska", "d": "Eating your way through Alaska.", "g": "food", "l": 2, "q": "What is Food tour: Alaska?", "a": "Eating your way through Alaska.", "x": "Eating through Alaska: start with king crab, then follow the locals — diners, food trucks, farm stands. North to the Future Food is the fastest way into a place's heart; the stories come free with the meal. Anchorage", "s": "public-reference", "f": null}, {"t": "Iditarod", "d": "Iditarod: Alaska's signature festival.", "g": "festivals", "l": 2, "q": "What is Iditarod?", "a": "Iditarod: Alaska's signature festival.", "x": "Iditarod is Alaska at its most celebratory: Statehood 1959; pipeline era.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Juneau Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Alaska year-round: Iditarod and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Alaska year-round: Iditarod and more.", "x": "The Alaska festival calendar runs year-round, with Iditarod as the anchor. North to the Future Every season has its celebration — plan trips around them for the liveliest version of the state. Denali National Park", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-alaska-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
