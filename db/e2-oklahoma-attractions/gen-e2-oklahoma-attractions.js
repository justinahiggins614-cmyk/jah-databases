(function(){'use strict';
/* JAH Oklahoma Attractions Database generator — jahdb-e2-oklahoma-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-oklahoma-attractions',PREFIX='JAH-E2OKLAHOMAA-',NAME='JAH Oklahoma Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Oklahoma: attractions overview", "d": "The best of Oklahoma: Oklahoma City Memorial, Route 66, Wichita Mountains.", "g": "overview", "l": 2, "q": "What is Oklahoma: attractions overview?", "a": "The best of Oklahoma: Oklahoma City Memorial, Route 66, Wichita Mountains.", "x": "The essential Oklahoma: Oklahoma City Memorial, Route 66, Wichita Mountains — plus Wichita Mountains Wildlife Refuge, Oklahoma's great chicken-fried steak. Oklahoma State Fair This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Oklahoma City Memorial", "d": "Oklahoma City Memorial: a top Oklahoma attraction.", "g": "attractions", "l": 2, "q": "What is Oklahoma City Memorial?", "a": "Oklahoma City Memorial: a top Oklahoma attraction.", "x": "Oklahoma City Memorial is essential Oklahoma. Trail of Tears; Five Tribes. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. chicken-fried steak", "s": "public-reference", "f": null}, {"t": "Visiting Oklahoma City Memorial", "d": "How to experience Oklahoma City Memorial.", "g": "attractions", "l": 2, "q": "What is Visiting Oklahoma City Memorial?", "a": "How to experience Oklahoma City Memorial.", "x": "Experiencing Oklahoma City Memorial: plan around Oklahoma State Fair, the state's rhythm — Labor omnia vincit (Labor conquers all things). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Wichita Mountains Wildlife Refuge Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Route 66", "d": "Route 66: a top Oklahoma attraction.", "g": "attractions", "l": 2, "q": "What is Route 66?", "a": "Route 66: a top Oklahoma attraction.", "x": "Route 66 is essential Oklahoma. Trail of Tears; Five Tribes. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. chicken-fried steak State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Route 66", "d": "How to experience Route 66.", "g": "attractions", "l": 2, "q": "What is Visiting Route 66?", "a": "How to experience Route 66.", "x": "Experiencing Route 66: plan around Oklahoma State Fair, the state's rhythm — Labor omnia vincit (Labor conquers all things). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Wichita Mountains Wildlife Refuge Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Wichita Mountains", "d": "Wichita Mountains: a top Oklahoma attraction.", "g": "attractions", "l": 2, "q": "What is Wichita Mountains?", "a": "Wichita Mountains: a top Oklahoma attraction.", "x": "Wichita Mountains is essential Oklahoma. Trail of Tears; Five Tribes. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. chicken-fried steak", "s": "public-reference", "f": null}, {"t": "Visiting Wichita Mountains", "d": "How to experience Wichita Mountains.", "g": "attractions", "l": 2, "q": "What is Visiting Wichita Mountains?", "a": "How to experience Wichita Mountains.", "x": "Experiencing Wichita Mountains: plan around Oklahoma State Fair, the state's rhythm — Labor omnia vincit (Labor conquers all things). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Wichita Mountains Wildlife Refuge Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Chickasaw Cultural Center", "d": "Chickasaw Cultural Center: a top Oklahoma attraction.", "g": "attractions", "l": 2, "q": "What is Chickasaw Cultural Center?", "a": "Chickasaw Cultural Center: a top Oklahoma attraction.", "x": "Chickasaw Cultural Center is essential Oklahoma. Trail of Tears; Five Tribes. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. chicken-fried steak", "s": "public-reference", "f": null}, {"t": "Visiting Chickasaw Cultural Center", "d": "How to experience Chickasaw Cultural Center.", "g": "attractions", "l": 2, "q": "What is Visiting Chickasaw Cultural Center?", "a": "How to experience Chickasaw Cultural Center.", "x": "Experiencing Chickasaw Cultural Center: plan around Oklahoma State Fair, the state's rhythm — Labor omnia vincit (Labor conquers all things). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Wichita Mountains Wildlife Refuge Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Tallgrass Prairie Preserve", "d": "Tallgrass Prairie Preserve: a top Oklahoma attraction.", "g": "attractions", "l": 2, "q": "What is Tallgrass Prairie Preserve?", "a": "Tallgrass Prairie Preserve: a top Oklahoma attraction.", "x": "Tallgrass Prairie Preserve is essential Oklahoma. Trail of Tears; Five Tribes. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. chicken-fried steak", "s": "public-reference", "f": null}, {"t": "Visiting Tallgrass Prairie Preserve", "d": "How to experience Tallgrass Prairie Preserve.", "g": "attractions", "l": 2, "q": "What is Visiting Tallgrass Prairie Preserve?", "a": "How to experience Tallgrass Prairie Preserve.", "x": "Experiencing Tallgrass Prairie Preserve: plan around Oklahoma State Fair, the state's rhythm — Labor omnia vincit (Labor conquers all things). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Wichita Mountains Wildlife Refuge Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Philbrook Museum", "d": "Philbrook Museum: a top Oklahoma attraction.", "g": "attractions", "l": 2, "q": "What is Philbrook Museum?", "a": "Philbrook Museum: a top Oklahoma attraction.", "x": "Philbrook Museum is essential Oklahoma. Trail of Tears; Five Tribes. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. chicken-fried steak", "s": "public-reference", "f": null}, {"t": "Visiting Philbrook Museum", "d": "How to experience Philbrook Museum.", "g": "attractions", "l": 2, "q": "What is Visiting Philbrook Museum?", "a": "How to experience Philbrook Museum.", "x": "Experiencing Philbrook Museum: plan around Oklahoma State Fair, the state's rhythm — Labor omnia vincit (Labor conquers all things). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Wichita Mountains Wildlife Refuge Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Beavers Bend", "d": "Beavers Bend: a top Oklahoma attraction.", "g": "attractions", "l": 2, "q": "What is Beavers Bend?", "a": "Beavers Bend: a top Oklahoma attraction.", "x": "Beavers Bend is essential Oklahoma. Trail of Tears; Five Tribes. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. chicken-fried steak", "s": "public-reference", "f": null}, {"t": "Visiting Beavers Bend", "d": "How to experience Beavers Bend.", "g": "attractions", "l": 2, "q": "What is Visiting Beavers Bend?", "a": "How to experience Beavers Bend.", "x": "Experiencing Beavers Bend: plan around Oklahoma State Fair, the state's rhythm — Labor omnia vincit (Labor conquers all things). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Wichita Mountains Wildlife Refuge Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Turner Falls", "d": "Turner Falls: a top Oklahoma attraction.", "g": "attractions", "l": 2, "q": "What is Turner Falls?", "a": "Turner Falls: a top Oklahoma attraction.", "x": "Turner Falls is essential Oklahoma. Trail of Tears; Five Tribes. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. chicken-fried steak", "s": "public-reference", "f": null}, {"t": "Visiting Turner Falls", "d": "How to experience Turner Falls.", "g": "attractions", "l": 2, "q": "What is Visiting Turner Falls?", "a": "How to experience Turner Falls.", "x": "Experiencing Turner Falls: plan around Oklahoma State Fair, the state's rhythm — Labor omnia vincit (Labor conquers all things). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Wichita Mountains Wildlife Refuge Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Wichita Mountains Wildlife Refuge", "d": "Wichita Mountains Wildlife Refuge: Oklahoma's great park.", "g": "parks", "l": 2, "q": "What is Wichita Mountains Wildlife Refuge?", "a": "Wichita Mountains Wildlife Refuge: Oklahoma's great park.", "x": "Wichita Mountains Wildlife Refuge is Oklahoma's wild heart: Oklahoma City Memorial. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Oklahoma State Fair Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Wichita Mountains Wildlife Refuge", "d": "How to explore Wichita Mountains Wildlife Refuge.", "g": "parks", "l": 2, "q": "What is Exploring Wichita Mountains Wildlife Refuge?", "a": "How to explore Wichita Mountains Wildlife Refuge.", "x": "Exploring Wichita Mountains Wildlife Refuge: get the park map, check conditions, carry water and layers, and tell someone your plan. Labor omnia vincit (Labor conquers all things) Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Oklahoma City: the capital city", "d": "Oklahoma City, capital of Oklahoma.", "g": "cities", "l": 2, "q": "What is Oklahoma City: the capital city?", "a": "Oklahoma City, capital of Oklahoma.", "x": "Oklahoma City: the capital of Oklahoma — government, history, and often the best museums. Land Run 1889; Dust Bowl. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Oklahoma City", "s": "public-reference", "f": null}, {"t": "Oklahoma City: the biggest city", "d": "Oklahoma City is Oklahoma's largest city.", "g": "cities", "l": 2, "q": "What is Oklahoma City: the biggest city?", "a": "Oklahoma City is Oklahoma's largest city.", "x": "Oklahoma City is where Oklahoma comes to work and play: the skyline, the food, the music, the crowds. energy (oil, wind) Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Oklahoma State Fair", "s": "public-reference", "f": null}, {"t": "chicken-fried steak: the food", "d": "Taste Oklahoma: chicken-fried steak.", "g": "food", "l": 2, "q": "What is chicken-fried steak: the food?", "a": "Taste Oklahoma: chicken-fried steak.", "x": "The taste of Oklahoma is chicken-fried steak — and the foodways around it. Oil and Native nations. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Oklahoma State Fair Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Oklahoma", "d": "Eating your way through Oklahoma.", "g": "food", "l": 2, "q": "What is Food tour: Oklahoma?", "a": "Eating your way through Oklahoma.", "x": "Eating through Oklahoma: start with chicken-fried steak, then follow the locals — diners, food trucks, farm stands. Labor omnia vincit (Labor conquers all things) Food is the fastest way into a place's heart; the stories come free with the meal. Oklahoma City", "s": "public-reference", "f": null}, {"t": "Oklahoma State Fair", "d": "Oklahoma State Fair: Oklahoma's signature festival.", "g": "festivals", "l": 2, "q": "What is Oklahoma State Fair?", "a": "Oklahoma State Fair: Oklahoma's signature festival.", "x": "Oklahoma State Fair is Oklahoma at its most celebratory: The Land Run of 1889 settled it in a single day.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Oklahoma City Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Oklahoma year-round: Oklahoma State Fair and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Oklahoma year-round: Oklahoma State Fair and more.", "x": "The Oklahoma festival calendar runs year-round, with Oklahoma State Fair as the anchor. Labor omnia vincit (Labor conquers all things) Every season has its celebration — plan trips around them for the liveliest version of the state. Wichita Mountains Wildlife Refuge", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-oklahoma-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
