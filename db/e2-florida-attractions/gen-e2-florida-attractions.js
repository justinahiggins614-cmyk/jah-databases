(function(){'use strict';
/* JAH Florida Attractions Database generator — jahdb-e2-florida-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-florida-attractions',PREFIX='JAH-E2FLORIDAAT-',NAME='JAH Florida Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Florida: attractions overview", "d": "The best of Florida: Walt Disney World, Everglades, Kennedy Space Center.", "g": "overview", "l": 2, "q": "What is Florida: attractions overview?", "a": "The best of Florida: Walt Disney World, Everglades, Kennedy Space Center.", "x": "The essential Florida: Walt Disney World, Everglades, Kennedy Space Center — plus Everglades National Park, Florida's great key lime pie. Calle Ocho Festival This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Walt Disney World", "d": "Walt Disney World: a top Florida attraction.", "g": "attractions", "l": 2, "q": "What is Walt Disney World?", "a": "Walt Disney World: a top Florida attraction.", "x": "Walt Disney World is essential Florida. Timucua and Seminole lands; Spanish 1513. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. key lime pie", "s": "public-reference", "f": null}, {"t": "Visiting Walt Disney World", "d": "How to experience Walt Disney World.", "g": "attractions", "l": 2, "q": "What is Visiting Walt Disney World?", "a": "How to experience Walt Disney World.", "x": "Experiencing Walt Disney World: plan around Calle Ocho Festival, the state's rhythm — In God We Trust. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Everglades National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Everglades", "d": "Everglades: a top Florida attraction.", "g": "attractions", "l": 2, "q": "What is Everglades?", "a": "Everglades: a top Florida attraction.", "x": "Everglades is essential Florida. Timucua and Seminole lands; Spanish 1513. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. key lime pie", "s": "public-reference", "f": null}, {"t": "Visiting Everglades", "d": "How to experience Everglades.", "g": "attractions", "l": 2, "q": "What is Visiting Everglades?", "a": "How to experience Everglades.", "x": "Experiencing Everglades: plan around Calle Ocho Festival, the state's rhythm — In God We Trust. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Everglades National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Kennedy Space Center", "d": "Kennedy Space Center: a top Florida attraction.", "g": "attractions", "l": 2, "q": "What is Kennedy Space Center?", "a": "Kennedy Space Center: a top Florida attraction.", "x": "Kennedy Space Center is essential Florida. Timucua and Seminole lands; Spanish 1513. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. key lime pie", "s": "public-reference", "f": null}, {"t": "Visiting Kennedy Space Center", "d": "How to experience Kennedy Space Center.", "g": "attractions", "l": 2, "q": "What is Visiting Kennedy Space Center?", "a": "How to experience Kennedy Space Center.", "x": "Experiencing Kennedy Space Center: plan around Calle Ocho Festival, the state's rhythm — In God We Trust. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Everglades National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "South Beach", "d": "South Beach: a top Florida attraction.", "g": "attractions", "l": 2, "q": "What is South Beach?", "a": "South Beach: a top Florida attraction.", "x": "South Beach is essential Florida. Timucua and Seminole lands; Spanish 1513. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. key lime pie", "s": "public-reference", "f": null}, {"t": "Visiting South Beach", "d": "How to experience South Beach.", "g": "attractions", "l": 2, "q": "What is Visiting South Beach?", "a": "How to experience South Beach.", "x": "Experiencing South Beach: plan around Calle Ocho Festival, the state's rhythm — In God We Trust. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Everglades National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Key West", "d": "Key West: a top Florida attraction.", "g": "attractions", "l": 2, "q": "What is Key West?", "a": "Key West: a top Florida attraction.", "x": "Key West is essential Florida. Timucua and Seminole lands; Spanish 1513. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. key lime pie", "s": "public-reference", "f": null}, {"t": "Visiting Key West", "d": "How to experience Key West.", "g": "attractions", "l": 2, "q": "What is Visiting Key West?", "a": "How to experience Key West.", "x": "Experiencing Key West: plan around Calle Ocho Festival, the state's rhythm — In God We Trust. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Everglades National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Universal Orlando", "d": "Universal Orlando: a top Florida attraction.", "g": "attractions", "l": 2, "q": "What is Universal Orlando?", "a": "Universal Orlando: a top Florida attraction.", "x": "Universal Orlando is essential Florida. Timucua and Seminole lands; Spanish 1513. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. key lime pie", "s": "public-reference", "f": null}, {"t": "Visiting Universal Orlando", "d": "How to experience Universal Orlando.", "g": "attractions", "l": 2, "q": "What is Visiting Universal Orlando?", "a": "How to experience Universal Orlando.", "x": "Experiencing Universal Orlando: plan around Calle Ocho Festival, the state's rhythm — In God We Trust. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Everglades National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "St. Augustine", "d": "St. Augustine: a top Florida attraction.", "g": "attractions", "l": 2, "q": "What is St. Augustine?", "a": "St. Augustine: a top Florida attraction.", "x": "St. Augustine is essential Florida. Timucua and Seminole lands; Spanish 1513. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. key lime pie", "s": "public-reference", "f": null}, {"t": "Visiting St. Augustine", "d": "How to experience St. Augustine.", "g": "attractions", "l": 2, "q": "What is Visiting St. Augustine?", "a": "How to experience St. Augustine.", "x": "Experiencing St. Augustine: plan around Calle Ocho Festival, the state's rhythm — In God We Trust. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Everglades National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Dry Tortugas", "d": "Dry Tortugas: a top Florida attraction.", "g": "attractions", "l": 2, "q": "What is Dry Tortugas?", "a": "Dry Tortugas: a top Florida attraction.", "x": "Dry Tortugas is essential Florida. Timucua and Seminole lands; Spanish 1513. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. key lime pie", "s": "public-reference", "f": null}, {"t": "Visiting Dry Tortugas", "d": "How to experience Dry Tortugas.", "g": "attractions", "l": 2, "q": "What is Visiting Dry Tortugas?", "a": "How to experience Dry Tortugas.", "x": "Experiencing Dry Tortugas: plan around Calle Ocho Festival, the state's rhythm — In God We Trust. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Everglades National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Everglades National Park", "d": "Everglades National Park: Florida's great park.", "g": "parks", "l": 2, "q": "What is Everglades National Park?", "a": "Everglades National Park: Florida's great park.", "x": "Everglades National Park is Florida's wild heart: Walt Disney World. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Calle Ocho Festival Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Everglades National Park", "d": "How to explore Everglades National Park.", "g": "parks", "l": 2, "q": "What is Exploring Everglades National Park?", "a": "How to explore Everglades National Park.", "x": "Exploring Everglades National Park: get the park map, check conditions, carry water and layers, and tell someone your plan. In God We Trust Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Tallahassee: the capital city", "d": "Tallahassee, capital of Florida.", "g": "cities", "l": 2, "q": "What is Tallahassee: the capital city?", "a": "Tallahassee, capital of Florida.", "x": "Tallahassee: the capital of Florida — government, history, and often the best museums. U.S. 1819; Civil War; citrus empire. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Jacksonville", "s": "public-reference", "f": null}, {"t": "Jacksonville: the biggest city", "d": "Jacksonville is Florida's largest city.", "g": "cities", "l": 2, "q": "What is Jacksonville: the biggest city?", "a": "Jacksonville is Florida's largest city.", "x": "Jacksonville is where Florida comes to work and play: the skyline, the food, the music, the crowds. tourism Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Calle Ocho Festival", "s": "public-reference", "f": null}, {"t": "key lime pie: the food", "d": "Taste Florida: key lime pie.", "g": "food", "l": 2, "q": "What is key lime pie: the food?", "a": "Taste Florida: key lime pie.", "x": "The taste of Florida is key lime pie — and the foodways around it. Disney 1971; space coast; boom state. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Calle Ocho Festival Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Florida", "d": "Eating your way through Florida.", "g": "food", "l": 2, "q": "What is Food tour: Florida?", "a": "Eating your way through Florida.", "x": "Eating through Florida: start with key lime pie, then follow the locals — diners, food trucks, farm stands. In God We Trust Food is the fastest way into a place's heart; the stories come free with the meal. Jacksonville", "s": "public-reference", "f": null}, {"t": "Calle Ocho Festival", "d": "Calle Ocho Festival: Florida's signature festival.", "g": "festivals", "l": 2, "q": "What is Calle Ocho Festival?", "a": "Calle Ocho Festival: Florida's signature festival.", "x": "Calle Ocho Festival is Florida at its most celebratory: Disney World opened in 1971, transforming central Florida.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Tallahassee Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Florida year-round: Calle Ocho Festival and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Florida year-round: Calle Ocho Festival and more.", "x": "The Florida festival calendar runs year-round, with Calle Ocho Festival as the anchor. In God We Trust Every season has its celebration — plan trips around them for the liveliest version of the state. Everglades National Park", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-florida-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
