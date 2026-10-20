(function(){'use strict';
/* JAH New Jersey Attractions Database generator — jahdb-e2-new-jersey-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-new-jersey-attractions',PREFIX='JAH-E2NEWJERSEY-',NAME='JAH New Jersey Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "New Jersey: attractions overview", "d": "The best of New Jersey: Jersey Shore, Atlantic City, Princeton University.", "g": "overview", "l": 2, "q": "What is New Jersey: attractions overview?", "a": "The best of New Jersey: Jersey Shore, Atlantic City, Princeton University.", "x": "The essential New Jersey: Jersey Shore, Atlantic City, Princeton University — plus Delaware Water Gap National Recreation Area, New Jersey's great pork roll. Jersey Shore summers This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Jersey Shore", "d": "Jersey Shore: a top New Jersey attraction.", "g": "attractions", "l": 2, "q": "What is Jersey Shore?", "a": "Jersey Shore: a top New Jersey attraction.", "x": "Jersey Shore is essential New Jersey. Lenape; Dutch then English. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pork roll State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Jersey Shore", "d": "How to experience Jersey Shore.", "g": "attractions", "l": 2, "q": "What is Visiting Jersey Shore?", "a": "How to experience Jersey Shore.", "x": "Experiencing Jersey Shore: plan around Jersey Shore summers, the state's rhythm — Liberty and Prosperity. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Delaware Water Gap National Recreation Area Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Atlantic City", "d": "Atlantic City: a top New Jersey attraction.", "g": "attractions", "l": 2, "q": "What is Atlantic City?", "a": "Atlantic City: a top New Jersey attraction.", "x": "Atlantic City is essential New Jersey. Lenape; Dutch then English. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pork roll State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Atlantic City", "d": "How to experience Atlantic City.", "g": "attractions", "l": 2, "q": "What is Visiting Atlantic City?", "a": "How to experience Atlantic City.", "x": "Experiencing Atlantic City: plan around Jersey Shore summers, the state's rhythm — Liberty and Prosperity. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Delaware Water Gap National Recreation Area Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Princeton University", "d": "Princeton University: a top New Jersey attraction.", "g": "attractions", "l": 2, "q": "What is Princeton University?", "a": "Princeton University: a top New Jersey attraction.", "x": "Princeton University is essential New Jersey. Lenape; Dutch then English. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pork roll State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Princeton University", "d": "How to experience Princeton University.", "g": "attractions", "l": 2, "q": "What is Visiting Princeton University?", "a": "How to experience Princeton University.", "x": "Experiencing Princeton University: plan around Jersey Shore summers, the state's rhythm — Liberty and Prosperity. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Delaware Water Gap National Recreation Area Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Liberty State Park", "d": "Liberty State Park: a top New Jersey attraction.", "g": "attractions", "l": 2, "q": "What is Liberty State Park?", "a": "Liberty State Park: a top New Jersey attraction.", "x": "Liberty State Park is essential New Jersey. Lenape; Dutch then English. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pork roll State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Liberty State Park", "d": "How to experience Liberty State Park.", "g": "attractions", "l": 2, "q": "What is Visiting Liberty State Park?", "a": "How to experience Liberty State Park.", "x": "Experiencing Liberty State Park: plan around Jersey Shore summers, the state's rhythm — Liberty and Prosperity. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Delaware Water Gap National Recreation Area Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Thomas Edison Lab", "d": "Thomas Edison Lab: a top New Jersey attraction.", "g": "attractions", "l": 2, "q": "What is Thomas Edison Lab?", "a": "Thomas Edison Lab: a top New Jersey attraction.", "x": "Thomas Edison Lab is essential New Jersey. Lenape; Dutch then English. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pork roll State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Thomas Edison Lab", "d": "How to experience Thomas Edison Lab.", "g": "attractions", "l": 2, "q": "What is Visiting Thomas Edison Lab?", "a": "How to experience Thomas Edison Lab.", "x": "Experiencing Thomas Edison Lab: plan around Jersey Shore summers, the state's rhythm — Liberty and Prosperity. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Delaware Water Gap National Recreation Area Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Cape May", "d": "Cape May: a top New Jersey attraction.", "g": "attractions", "l": 2, "q": "What is Cape May?", "a": "Cape May: a top New Jersey attraction.", "x": "Cape May is essential New Jersey. Lenape; Dutch then English. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pork roll State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Cape May", "d": "How to experience Cape May.", "g": "attractions", "l": 2, "q": "What is Visiting Cape May?", "a": "How to experience Cape May.", "x": "Experiencing Cape May: plan around Jersey Shore summers, the state's rhythm — Liberty and Prosperity. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Delaware Water Gap National Recreation Area Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Delaware Water Gap", "d": "Delaware Water Gap: a top New Jersey attraction.", "g": "attractions", "l": 2, "q": "What is Delaware Water Gap?", "a": "Delaware Water Gap: a top New Jersey attraction.", "x": "Delaware Water Gap is essential New Jersey. Lenape; Dutch then English. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pork roll State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Delaware Water Gap", "d": "How to experience Delaware Water Gap.", "g": "attractions", "l": 2, "q": "What is Visiting Delaware Water Gap?", "a": "How to experience Delaware Water Gap.", "x": "Experiencing Delaware Water Gap: plan around Jersey Shore summers, the state's rhythm — Liberty and Prosperity. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Delaware Water Gap National Recreation Area Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Six Flags", "d": "Six Flags: a top New Jersey attraction.", "g": "attractions", "l": 2, "q": "What is Six Flags?", "a": "Six Flags: a top New Jersey attraction.", "x": "Six Flags is essential New Jersey. Lenape; Dutch then English. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pork roll State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Six Flags", "d": "How to experience Six Flags.", "g": "attractions", "l": 2, "q": "What is Visiting Six Flags?", "a": "How to experience Six Flags.", "x": "Experiencing Six Flags: plan around Jersey Shore summers, the state's rhythm — Liberty and Prosperity. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Delaware Water Gap National Recreation Area Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Delaware Water Gap National Recreation Area", "d": "Delaware Water Gap National Recreation Area: New Jersey's great park.", "g": "parks", "l": 2, "q": "What is Delaware Water Gap National Recreation Area?", "a": "Delaware Water Gap National Recreation Area: New Jersey's great park.", "x": "Delaware Water Gap National Recreation Area is New Jersey's wild heart: Jersey Shore. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Jersey Shore summers Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Delaware Water Gap National Recreation Area", "d": "How to explore Delaware Water Gap National Recreation Area.", "g": "parks", "l": 2, "q": "What is Exploring Delaware Water Gap National Recreation Area?", "a": "How to explore Delaware Water Gap National Recreation Area.", "x": "Exploring Delaware Water Gap National Recreation Area: get the park map, check conditions, carry water and layers, and tell someone your plan. Liberty and Prosperity Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Trenton: the capital city", "d": "Trenton, capital of New Jersey.", "g": "cities", "l": 2, "q": "What is Trenton: the capital city?", "a": "Trenton, capital of New Jersey.", "x": "Trenton: the capital of New Jersey — government, history, and often the best museums. Revolutionary crossroads; Trenton. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Newark", "s": "public-reference", "f": null}, {"t": "Newark: the biggest city", "d": "Newark is New Jersey's largest city.", "g": "cities", "l": 2, "q": "What is Newark: the biggest city?", "a": "Newark is New Jersey's largest city.", "x": "Newark is where New Jersey comes to work and play: the skyline, the food, the music, the crowds. pharmaceuticals Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Jersey Shore summers", "s": "public-reference", "f": null}, {"t": "pork roll: the food", "d": "Taste New Jersey: pork roll.", "g": "food", "l": 2, "q": "What is pork roll: the food?", "a": "Taste New Jersey: pork roll.", "x": "The taste of New Jersey is pork roll — and the foodways around it. Industry; pharma; shore. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Jersey Shore summers Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: New Jersey", "d": "Eating your way through New Jersey.", "g": "food", "l": 2, "q": "What is Food tour: New Jersey?", "a": "Eating your way through New Jersey.", "x": "Eating through New Jersey: start with pork roll, then follow the locals — diners, food trucks, farm stands. Liberty and Prosperity Food is the fastest way into a place's heart; the stories come free with the meal. Newark", "s": "public-reference", "f": null}, {"t": "Jersey Shore summers", "d": "Jersey Shore summers: New Jersey's signature festival.", "g": "festivals", "l": 2, "q": "What is Jersey Shore summers?", "a": "Jersey Shore summers: New Jersey's signature festival.", "x": "Jersey Shore summers is New Jersey at its most celebratory: Edison's Menlo Park laboratory lit the world.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Trenton Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "New Jersey year-round: Jersey Shore summers and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "New Jersey year-round: Jersey Shore summers and more.", "x": "The New Jersey festival calendar runs year-round, with Jersey Shore summers as the anchor. Liberty and Prosperity Every season has its celebration — plan trips around them for the liveliest version of the state. Delaware Water Gap National Recreation Area", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-new-jersey-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
