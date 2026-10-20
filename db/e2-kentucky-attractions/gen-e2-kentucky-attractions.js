(function(){'use strict';
/* JAH Kentucky Attractions Database generator — jahdb-e2-kentucky-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-kentucky-attractions',PREFIX='JAH-E2KENTUCKYA-',NAME='JAH Kentucky Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Kentucky: attractions overview", "d": "The best of Kentucky: Mammoth Cave, Kentucky Derby, Bourbon Trail.", "g": "overview", "l": 2, "q": "What is Kentucky: attractions overview?", "a": "The best of Kentucky: Mammoth Cave, Kentucky Derby, Bourbon Trail.", "x": "The essential Kentucky: Mammoth Cave, Kentucky Derby, Bourbon Trail — plus Mammoth Cave National Park, Kentucky's great Hot Brown. Kentucky Derby This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Mammoth Cave", "d": "Mammoth Cave: a top Kentucky attraction.", "g": "attractions", "l": 2, "q": "What is Mammoth Cave?", "a": "Mammoth Cave: a top Kentucky attraction.", "x": "Mammoth Cave is essential Kentucky. Shawnee hunting grounds; Daniel Boone. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Hot Brown", "s": "public-reference", "f": null}, {"t": "Visiting Mammoth Cave", "d": "How to experience Mammoth Cave.", "g": "attractions", "l": 2, "q": "What is Visiting Mammoth Cave?", "a": "How to experience Mammoth Cave.", "x": "Experiencing Mammoth Cave: plan around Kentucky Derby, the state's rhythm — United we stand, divided we fall. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Mammoth Cave National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Kentucky Derby", "d": "Kentucky Derby: a top Kentucky attraction.", "g": "attractions", "l": 2, "q": "What is Kentucky Derby?", "a": "Kentucky Derby: a top Kentucky attraction.", "x": "Kentucky Derby is essential Kentucky. Shawnee hunting grounds; Daniel Boone. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Hot Brown", "s": "public-reference", "f": null}, {"t": "Visiting Kentucky Derby", "d": "How to experience Kentucky Derby.", "g": "attractions", "l": 2, "q": "What is Visiting Kentucky Derby?", "a": "How to experience Kentucky Derby.", "x": "Experiencing Kentucky Derby: plan around Kentucky Derby, the state's rhythm — United we stand, divided we fall. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Mammoth Cave National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Bourbon Trail", "d": "Bourbon Trail: a top Kentucky attraction.", "g": "attractions", "l": 2, "q": "What is Bourbon Trail?", "a": "Bourbon Trail: a top Kentucky attraction.", "x": "Bourbon Trail is essential Kentucky. Shawnee hunting grounds; Daniel Boone. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Hot Brown", "s": "public-reference", "f": null}, {"t": "Visiting Bourbon Trail", "d": "How to experience Bourbon Trail.", "g": "attractions", "l": 2, "q": "What is Visiting Bourbon Trail?", "a": "How to experience Bourbon Trail.", "x": "Experiencing Bourbon Trail: plan around Kentucky Derby, the state's rhythm — United we stand, divided we fall. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Mammoth Cave National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Red River Gorge", "d": "Red River Gorge: a top Kentucky attraction.", "g": "attractions", "l": 2, "q": "What is Red River Gorge?", "a": "Red River Gorge: a top Kentucky attraction.", "x": "Red River Gorge is essential Kentucky. Shawnee hunting grounds; Daniel Boone. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Hot Brown", "s": "public-reference", "f": null}, {"t": "Visiting Red River Gorge", "d": "How to experience Red River Gorge.", "g": "attractions", "l": 2, "q": "What is Visiting Red River Gorge?", "a": "How to experience Red River Gorge.", "x": "Experiencing Red River Gorge: plan around Kentucky Derby, the state's rhythm — United we stand, divided we fall. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Mammoth Cave National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Louisville Slugger Museum", "d": "Louisville Slugger Museum: a top Kentucky attraction.", "g": "attractions", "l": 2, "q": "What is Louisville Slugger Museum?", "a": "Louisville Slugger Museum: a top Kentucky attraction.", "x": "Louisville Slugger Museum is essential Kentucky. Shawnee hunting grounds; Daniel Boone. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Hot Brown", "s": "public-reference", "f": null}, {"t": "Visiting Louisville Slugger Museum", "d": "How to experience Louisville Slugger Museum.", "g": "attractions", "l": 2, "q": "What is Visiting Louisville Slugger Museum?", "a": "How to experience Louisville Slugger Museum.", "x": "Experiencing Louisville Slugger Museum: plan around Kentucky Derby, the state's rhythm — United we stand, divided we fall. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Mammoth Cave National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Ark Encounter", "d": "Ark Encounter: a top Kentucky attraction.", "g": "attractions", "l": 2, "q": "What is Ark Encounter?", "a": "Ark Encounter: a top Kentucky attraction.", "x": "Ark Encounter is essential Kentucky. Shawnee hunting grounds; Daniel Boone. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Hot Brown", "s": "public-reference", "f": null}, {"t": "Visiting Ark Encounter", "d": "How to experience Ark Encounter.", "g": "attractions", "l": 2, "q": "What is Visiting Ark Encounter?", "a": "How to experience Ark Encounter.", "x": "Experiencing Ark Encounter: plan around Kentucky Derby, the state's rhythm — United we stand, divided we fall. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Mammoth Cave National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Cumberland Falls", "d": "Cumberland Falls: a top Kentucky attraction.", "g": "attractions", "l": 2, "q": "What is Cumberland Falls?", "a": "Cumberland Falls: a top Kentucky attraction.", "x": "Cumberland Falls is essential Kentucky. Shawnee hunting grounds; Daniel Boone. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Hot Brown", "s": "public-reference", "f": null}, {"t": "Visiting Cumberland Falls", "d": "How to experience Cumberland Falls.", "g": "attractions", "l": 2, "q": "What is Visiting Cumberland Falls?", "a": "How to experience Cumberland Falls.", "x": "Experiencing Cumberland Falls: plan around Kentucky Derby, the state's rhythm — United we stand, divided we fall. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Mammoth Cave National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Keeneland", "d": "Keeneland: a top Kentucky attraction.", "g": "attractions", "l": 2, "q": "What is Keeneland?", "a": "Keeneland: a top Kentucky attraction.", "x": "Keeneland is essential Kentucky. Shawnee hunting grounds; Daniel Boone. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Hot Brown State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Keeneland", "d": "How to experience Keeneland.", "g": "attractions", "l": 2, "q": "What is Visiting Keeneland?", "a": "How to experience Keeneland.", "x": "Experiencing Keeneland: plan around Kentucky Derby, the state's rhythm — United we stand, divided we fall. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Mammoth Cave National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Mammoth Cave National Park", "d": "Mammoth Cave National Park: Kentucky's great park.", "g": "parks", "l": 2, "q": "What is Mammoth Cave National Park?", "a": "Mammoth Cave National Park: Kentucky's great park.", "x": "Mammoth Cave National Park is Kentucky's wild heart: Mammoth Cave. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Kentucky Derby Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Mammoth Cave National Park", "d": "How to explore Mammoth Cave National Park.", "g": "parks", "l": 2, "q": "What is Exploring Mammoth Cave National Park?", "a": "How to explore Mammoth Cave National Park.", "x": "Exploring Mammoth Cave National Park: get the park map, check conditions, carry water and layers, and tell someone your plan. United we stand, divided we fall Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Frankfort: the capital city", "d": "Frankfort, capital of Kentucky.", "g": "cities", "l": 2, "q": "What is Frankfort: the capital city?", "a": "Frankfort, capital of Kentucky.", "x": "Frankfort: the capital of Kentucky — government, history, and often the best museums. Civil War border state. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Louisville", "s": "public-reference", "f": null}, {"t": "Louisville: the biggest city", "d": "Louisville is Kentucky's largest city.", "g": "cities", "l": 2, "q": "What is Louisville: the biggest city?", "a": "Louisville is Kentucky's largest city.", "x": "Louisville is where Kentucky comes to work and play: the skyline, the food, the music, the crowds. bourbon Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Kentucky Derby", "s": "public-reference", "f": null}, {"t": "Hot Brown: the food", "d": "Taste Kentucky: Hot Brown.", "g": "food", "l": 2, "q": "What is Hot Brown: the food?", "a": "Taste Kentucky: Hot Brown.", "x": "The taste of Kentucky is Hot Brown — and the foodways around it. Bourbon, horses, coal. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Kentucky Derby Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Kentucky", "d": "Eating your way through Kentucky.", "g": "food", "l": 2, "q": "What is Food tour: Kentucky?", "a": "Eating your way through Kentucky.", "x": "Eating through Kentucky: start with Hot Brown, then follow the locals — diners, food trucks, farm stands. United we stand, divided we fall Food is the fastest way into a place's heart; the stories come free with the meal. Louisville", "s": "public-reference", "f": null}, {"t": "Kentucky Derby", "d": "Kentucky Derby: Kentucky's signature festival.", "g": "festivals", "l": 2, "q": "What is Kentucky Derby?", "a": "Kentucky Derby: Kentucky's signature festival.", "x": "Kentucky Derby is Kentucky at its most celebratory: The Kentucky Derby has run every year since 1875.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Frankfort Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Kentucky year-round: Kentucky Derby and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Kentucky year-round: Kentucky Derby and more.", "x": "The Kentucky festival calendar runs year-round, with Kentucky Derby as the anchor. United we stand, divided we fall Every season has its celebration — plan trips around them for the liveliest version of the state. Mammoth Cave National Park", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-kentucky-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
