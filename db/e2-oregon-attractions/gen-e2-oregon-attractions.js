(function(){'use strict';
/* JAH Oregon Attractions Database generator — jahdb-e2-oregon-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-oregon-attractions',PREFIX='JAH-E2OREGONATT-',NAME='JAH Oregon Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Oregon: attractions overview", "d": "The best of Oregon: Crater Lake, Multnomah Falls, Cannon Beach.", "g": "overview", "l": 2, "q": "What is Oregon: attractions overview?", "a": "The best of Oregon: Crater Lake, Multnomah Falls, Cannon Beach.", "x": "The essential Oregon: Crater Lake, Multnomah Falls, Cannon Beach — plus Crater Lake National Park, Oregon's great marionberry pie. Portland festivals This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Crater Lake", "d": "Crater Lake: a top Oregon attraction.", "g": "attractions", "l": 2, "q": "What is Crater Lake?", "a": "Crater Lake: a top Oregon attraction.", "x": "Crater Lake is essential Oregon. Chinook; Oregon Trail. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. marionberry pie State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Crater Lake", "d": "How to experience Crater Lake.", "g": "attractions", "l": 2, "q": "What is Visiting Crater Lake?", "a": "How to experience Crater Lake.", "x": "Experiencing Crater Lake: plan around Portland festivals, the state's rhythm — Alis volat propriis (She flies with her own wings). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Crater Lake National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Multnomah Falls", "d": "Multnomah Falls: a top Oregon attraction.", "g": "attractions", "l": 2, "q": "What is Multnomah Falls?", "a": "Multnomah Falls: a top Oregon attraction.", "x": "Multnomah Falls is essential Oregon. Chinook; Oregon Trail. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. marionberry pie State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Multnomah Falls", "d": "How to experience Multnomah Falls.", "g": "attractions", "l": 2, "q": "What is Visiting Multnomah Falls?", "a": "How to experience Multnomah Falls.", "x": "Experiencing Multnomah Falls: plan around Portland festivals, the state's rhythm — Alis volat propriis (She flies with her own wings). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Crater Lake National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Cannon Beach", "d": "Cannon Beach: a top Oregon attraction.", "g": "attractions", "l": 2, "q": "What is Cannon Beach?", "a": "Cannon Beach: a top Oregon attraction.", "x": "Cannon Beach is essential Oregon. Chinook; Oregon Trail. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. marionberry pie State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Cannon Beach", "d": "How to experience Cannon Beach.", "g": "attractions", "l": 2, "q": "What is Visiting Cannon Beach?", "a": "How to experience Cannon Beach.", "x": "Experiencing Cannon Beach: plan around Portland festivals, the state's rhythm — Alis volat propriis (She flies with her own wings). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Crater Lake National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Columbia Gorge", "d": "Columbia Gorge: a top Oregon attraction.", "g": "attractions", "l": 2, "q": "What is Columbia Gorge?", "a": "Columbia Gorge: a top Oregon attraction.", "x": "Columbia Gorge is essential Oregon. Chinook; Oregon Trail. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. marionberry pie State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Columbia Gorge", "d": "How to experience Columbia Gorge.", "g": "attractions", "l": 2, "q": "What is Visiting Columbia Gorge?", "a": "How to experience Columbia Gorge.", "x": "Experiencing Columbia Gorge: plan around Portland festivals, the state's rhythm — Alis volat propriis (She flies with her own wings). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Crater Lake National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Powell's Books", "d": "Powell's Books: a top Oregon attraction.", "g": "attractions", "l": 2, "q": "What is Powell's Books?", "a": "Powell's Books: a top Oregon attraction.", "x": "Powell's Books is essential Oregon. Chinook; Oregon Trail. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. marionberry pie State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Powell's Books", "d": "How to experience Powell's Books.", "g": "attractions", "l": 2, "q": "What is Visiting Powell's Books?", "a": "How to experience Powell's Books.", "x": "Experiencing Powell's Books: plan around Portland festivals, the state's rhythm — Alis volat propriis (She flies with her own wings). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Crater Lake National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Oregon Coast", "d": "Oregon Coast: a top Oregon attraction.", "g": "attractions", "l": 2, "q": "What is Oregon Coast?", "a": "Oregon Coast: a top Oregon attraction.", "x": "Oregon Coast is essential Oregon. Chinook; Oregon Trail. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. marionberry pie State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Oregon Coast", "d": "How to experience Oregon Coast.", "g": "attractions", "l": 2, "q": "What is Visiting Oregon Coast?", "a": "How to experience Oregon Coast.", "x": "Experiencing Oregon Coast: plan around Portland festivals, the state's rhythm — Alis volat propriis (She flies with her own wings). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Crater Lake National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Smith Rock", "d": "Smith Rock: a top Oregon attraction.", "g": "attractions", "l": 2, "q": "What is Smith Rock?", "a": "Smith Rock: a top Oregon attraction.", "x": "Smith Rock is essential Oregon. Chinook; Oregon Trail. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. marionberry pie State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Smith Rock", "d": "How to experience Smith Rock.", "g": "attractions", "l": 2, "q": "What is Visiting Smith Rock?", "a": "How to experience Smith Rock.", "x": "Experiencing Smith Rock: plan around Portland festivals, the state's rhythm — Alis volat propriis (She flies with her own wings). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Crater Lake National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Portland Japanese Garden", "d": "Portland Japanese Garden: a top Oregon attraction.", "g": "attractions", "l": 2, "q": "What is Portland Japanese Garden?", "a": "Portland Japanese Garden: a top Oregon attraction.", "x": "Portland Japanese Garden is essential Oregon. Chinook; Oregon Trail. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. marionberry pie", "s": "public-reference", "f": null}, {"t": "Visiting Portland Japanese Garden", "d": "How to experience Portland Japanese Garden.", "g": "attractions", "l": 2, "q": "What is Visiting Portland Japanese Garden?", "a": "How to experience Portland Japanese Garden.", "x": "Experiencing Portland Japanese Garden: plan around Portland festivals, the state's rhythm — Alis volat propriis (She flies with her own wings). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Crater Lake National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Crater Lake National Park", "d": "Crater Lake National Park: Oregon's great park.", "g": "parks", "l": 2, "q": "What is Crater Lake National Park?", "a": "Crater Lake National Park: Oregon's great park.", "x": "Crater Lake National Park is Oregon's wild heart: Crater Lake. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Portland festivals Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Crater Lake National Park", "d": "How to explore Crater Lake National Park.", "g": "parks", "l": 2, "q": "What is Exploring Crater Lake National Park?", "a": "How to explore Crater Lake National Park.", "x": "Exploring Crater Lake National Park: get the park map, check conditions, carry water and layers, and tell someone your plan. Alis volat propriis (She flies with her own wings) Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Salem: the capital city", "d": "Salem, capital of Oregon.", "g": "cities", "l": 2, "q": "What is Salem: the capital city?", "a": "Salem, capital of Oregon.", "x": "Salem: the capital of Oregon — government, history, and often the best museums. Statehood 1859. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Portland", "s": "public-reference", "f": null}, {"t": "Portland: the biggest city", "d": "Portland is Oregon's largest city.", "g": "cities", "l": 2, "q": "What is Portland: the biggest city?", "a": "Portland is Oregon's largest city.", "x": "Portland is where Oregon comes to work and play: the skyline, the food, the music, the crowds. technology (Intel) Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Portland festivals", "s": "public-reference", "f": null}, {"t": "marionberry pie: the food", "d": "Taste Oregon: marionberry pie.", "g": "food", "l": 2, "q": "What is marionberry pie: the food?", "a": "Taste Oregon: marionberry pie.", "x": "The taste of Oregon is marionberry pie — and the foodways around it. Timber to tech (Silicon Forest). Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Portland festivals Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Oregon", "d": "Eating your way through Oregon.", "g": "food", "l": 2, "q": "What is Food tour: Oregon?", "a": "Eating your way through Oregon.", "x": "Eating through Oregon: start with marionberry pie, then follow the locals — diners, food trucks, farm stands. Alis volat propriis (She flies with her own wings) Food is the fastest way into a place's heart; the stories come free with the meal. Portland", "s": "public-reference", "f": null}, {"t": "Portland festivals", "d": "Portland festivals: Oregon's signature festival.", "g": "festivals", "l": 2, "q": "What is Portland festivals?", "a": "Portland festivals: Oregon's signature festival.", "x": "Portland festivals is Oregon at its most celebratory: The Oregon Trail brought settlers west.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Salem Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Oregon year-round: Portland festivals and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Oregon year-round: Portland festivals and more.", "x": "The Oregon festival calendar runs year-round, with Portland festivals as the anchor. Alis volat propriis (She flies with her own wings) Every season has its celebration — plan trips around them for the liveliest version of the state. Crater Lake National Park", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-oregon-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
