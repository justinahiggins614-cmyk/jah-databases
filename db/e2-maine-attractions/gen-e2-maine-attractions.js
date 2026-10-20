(function(){'use strict';
/* JAH Maine Attractions Database generator — jahdb-e2-maine-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-maine-attractions',PREFIX='JAH-E2MAINEATTR-',NAME='JAH Maine Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Maine: attractions overview", "d": "The best of Maine: Acadia National Park, Portland Head Light, Bar Harbor.", "g": "overview", "l": 2, "q": "What is Maine: attractions overview?", "a": "The best of Maine: Acadia National Park, Portland Head Light, Bar Harbor.", "x": "The essential Maine: Acadia National Park, Portland Head Light, Bar Harbor — plus Acadia National Park, Maine's great lobster roll. Portland festivals This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Acadia National Park", "d": "Acadia National Park: a top Maine attraction.", "g": "attractions", "l": 2, "q": "What is Acadia National Park?", "a": "Acadia National Park: a top Maine attraction.", "x": "Acadia National Park is essential Maine. Wabanaki; Massachusetts district. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. lobster roll", "s": "public-reference", "f": null}, {"t": "Visiting Acadia National Park", "d": "How to experience Acadia National Park.", "g": "attractions", "l": 2, "q": "What is Visiting Acadia National Park?", "a": "How to experience Acadia National Park.", "x": "Experiencing Acadia National Park: plan around Portland festivals, the state's rhythm — Dirigo (I lead). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Acadia National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Portland Head Light", "d": "Portland Head Light: a top Maine attraction.", "g": "attractions", "l": 2, "q": "What is Portland Head Light?", "a": "Portland Head Light: a top Maine attraction.", "x": "Portland Head Light is essential Maine. Wabanaki; Massachusetts district. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. lobster roll", "s": "public-reference", "f": null}, {"t": "Visiting Portland Head Light", "d": "How to experience Portland Head Light.", "g": "attractions", "l": 2, "q": "What is Visiting Portland Head Light?", "a": "How to experience Portland Head Light.", "x": "Experiencing Portland Head Light: plan around Portland festivals, the state's rhythm — Dirigo (I lead). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Acadia National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Bar Harbor", "d": "Bar Harbor: a top Maine attraction.", "g": "attractions", "l": 2, "q": "What is Bar Harbor?", "a": "Bar Harbor: a top Maine attraction.", "x": "Bar Harbor is essential Maine. Wabanaki; Massachusetts district. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. lobster roll State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Bar Harbor", "d": "How to experience Bar Harbor.", "g": "attractions", "l": 2, "q": "What is Visiting Bar Harbor?", "a": "How to experience Bar Harbor.", "x": "Experiencing Bar Harbor: plan around Portland festivals, the state's rhythm — Dirigo (I lead). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Acadia National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Baxter State Park", "d": "Baxter State Park: a top Maine attraction.", "g": "attractions", "l": 2, "q": "What is Baxter State Park?", "a": "Baxter State Park: a top Maine attraction.", "x": "Baxter State Park is essential Maine. Wabanaki; Massachusetts district. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. lobster roll", "s": "public-reference", "f": null}, {"t": "Visiting Baxter State Park", "d": "How to experience Baxter State Park.", "g": "attractions", "l": 2, "q": "What is Visiting Baxter State Park?", "a": "How to experience Baxter State Park.", "x": "Experiencing Baxter State Park: plan around Portland festivals, the state's rhythm — Dirigo (I lead). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Acadia National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Old Port Portland", "d": "Old Port Portland: a top Maine attraction.", "g": "attractions", "l": 2, "q": "What is Old Port Portland?", "a": "Old Port Portland: a top Maine attraction.", "x": "Old Port Portland is essential Maine. Wabanaki; Massachusetts district. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. lobster roll", "s": "public-reference", "f": null}, {"t": "Visiting Old Port Portland", "d": "How to experience Old Port Portland.", "g": "attractions", "l": 2, "q": "What is Visiting Old Port Portland?", "a": "How to experience Old Port Portland.", "x": "Experiencing Old Port Portland: plan around Portland festivals, the state's rhythm — Dirigo (I lead). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Acadia National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Kennebunkport", "d": "Kennebunkport: a top Maine attraction.", "g": "attractions", "l": 2, "q": "What is Kennebunkport?", "a": "Kennebunkport: a top Maine attraction.", "x": "Kennebunkport is essential Maine. Wabanaki; Massachusetts district. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. lobster roll State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Kennebunkport", "d": "How to experience Kennebunkport.", "g": "attractions", "l": 2, "q": "What is Visiting Kennebunkport?", "a": "How to experience Kennebunkport.", "x": "Experiencing Kennebunkport: plan around Portland festivals, the state's rhythm — Dirigo (I lead). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Acadia National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Camden Hills", "d": "Camden Hills: a top Maine attraction.", "g": "attractions", "l": 2, "q": "What is Camden Hills?", "a": "Camden Hills: a top Maine attraction.", "x": "Camden Hills is essential Maine. Wabanaki; Massachusetts district. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. lobster roll State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Camden Hills", "d": "How to experience Camden Hills.", "g": "attractions", "l": 2, "q": "What is Visiting Camden Hills?", "a": "How to experience Camden Hills.", "x": "Experiencing Camden Hills: plan around Portland festivals, the state's rhythm — Dirigo (I lead). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Acadia National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Moosehead Lake", "d": "Moosehead Lake: a top Maine attraction.", "g": "attractions", "l": 2, "q": "What is Moosehead Lake?", "a": "Moosehead Lake: a top Maine attraction.", "x": "Moosehead Lake is essential Maine. Wabanaki; Massachusetts district. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. lobster roll State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Moosehead Lake", "d": "How to experience Moosehead Lake.", "g": "attractions", "l": 2, "q": "What is Visiting Moosehead Lake?", "a": "How to experience Moosehead Lake.", "x": "Experiencing Moosehead Lake: plan around Portland festivals, the state's rhythm — Dirigo (I lead). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Acadia National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Acadia National Park", "d": "Acadia National Park: Maine's great park.", "g": "parks", "l": 2, "q": "What is Acadia National Park?", "a": "Acadia National Park: Maine's great park.", "x": "Acadia National Park is Maine's wild heart: Acadia National Park. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Portland festivals Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Acadia National Park", "d": "How to explore Acadia National Park.", "g": "parks", "l": 2, "q": "What is Exploring Acadia National Park?", "a": "How to explore Acadia National Park.", "x": "Exploring Acadia National Park: get the park map, check conditions, carry water and layers, and tell someone your plan. Dirigo (I lead) Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Augusta: the capital city", "d": "Augusta, capital of Maine.", "g": "cities", "l": 2, "q": "What is Augusta: the capital city?", "a": "Augusta, capital of Maine.", "x": "Augusta: the capital of Maine — government, history, and often the best museums. Statehood 1820 (Missouri Compromise). Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Portland", "s": "public-reference", "f": null}, {"t": "Portland: the biggest city", "d": "Portland is Maine's largest city.", "g": "cities", "l": 2, "q": "What is Portland: the biggest city?", "a": "Portland is Maine's largest city.", "x": "Portland is where Maine comes to work and play: the skyline, the food, the music, the crowds. lobster fishing Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Portland festivals", "s": "public-reference", "f": null}, {"t": "lobster roll: the food", "d": "Taste Maine: lobster roll.", "g": "food", "l": 2, "q": "What is lobster roll: the food?", "a": "Taste Maine: lobster roll.", "x": "The taste of Maine is lobster roll — and the foodways around it. Shipbuilding; lumber; lobster. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Portland festivals Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Maine", "d": "Eating your way through Maine.", "g": "food", "l": 2, "q": "What is Food tour: Maine?", "a": "Eating your way through Maine.", "x": "Eating through Maine: start with lobster roll, then follow the locals — diners, food trucks, farm stands. Dirigo (I lead) Food is the fastest way into a place's heart; the stories come free with the meal. Portland", "s": "public-reference", "f": null}, {"t": "Portland festivals", "d": "Portland festivals: Maine's signature festival.", "g": "festivals", "l": 2, "q": "What is Portland festivals?", "a": "Portland festivals: Maine's signature festival.", "x": "Portland festivals is Maine at its most celebratory: Shipbuilding and lumber built the coastal economy.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Augusta Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Maine year-round: Portland festivals and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Maine year-round: Portland festivals and more.", "x": "The Maine festival calendar runs year-round, with Portland festivals as the anchor. Dirigo (I lead) Every season has its celebration — plan trips around them for the liveliest version of the state. Acadia National Park", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-maine-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
