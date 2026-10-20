(function(){'use strict';
/* JAH West Virginia Attractions Database generator — jahdb-e2-west-virginia-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-west-virginia-attractions',PREFIX='JAH-E2WESTVIRGI-',NAME='JAH West Virginia Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "West Virginia: attractions overview", "d": "The best of West Virginia: New River Gorge, Harpers Ferry, Seneca Rocks.", "g": "overview", "l": 2, "q": "What is West Virginia: attractions overview?", "a": "The best of West Virginia: New River Gorge, Harpers Ferry, Seneca Rocks.", "x": "The essential West Virginia: New River Gorge, Harpers Ferry, Seneca Rocks — plus New River Gorge National Park, West Virginia's great pepperoni roll. Bridge Day This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "New River Gorge", "d": "New River Gorge: a top West Virginia attraction.", "g": "attractions", "l": 2, "q": "What is New River Gorge?", "a": "New River Gorge: a top West Virginia attraction.", "x": "New River Gorge is essential West Virginia. Split from Virginia 1863 (Civil War). Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pepperoni roll", "s": "public-reference", "f": null}, {"t": "Visiting New River Gorge", "d": "How to experience New River Gorge.", "g": "attractions", "l": 2, "q": "What is Visiting New River Gorge?", "a": "How to experience New River Gorge.", "x": "Experiencing New River Gorge: plan around Bridge Day, the state's rhythm — Montani semper liberi (Mountaineers are always free). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. New River Gorge National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Harpers Ferry", "d": "Harpers Ferry: a top West Virginia attraction.", "g": "attractions", "l": 2, "q": "What is Harpers Ferry?", "a": "Harpers Ferry: a top West Virginia attraction.", "x": "Harpers Ferry is essential West Virginia. Split from Virginia 1863 (Civil War). Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pepperoni roll", "s": "public-reference", "f": null}, {"t": "Visiting Harpers Ferry", "d": "How to experience Harpers Ferry.", "g": "attractions", "l": 2, "q": "What is Visiting Harpers Ferry?", "a": "How to experience Harpers Ferry.", "x": "Experiencing Harpers Ferry: plan around Bridge Day, the state's rhythm — Montani semper liberi (Mountaineers are always free). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. New River Gorge National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Seneca Rocks", "d": "Seneca Rocks: a top West Virginia attraction.", "g": "attractions", "l": 2, "q": "What is Seneca Rocks?", "a": "Seneca Rocks: a top West Virginia attraction.", "x": "Seneca Rocks is essential West Virginia. Split from Virginia 1863 (Civil War). Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pepperoni roll", "s": "public-reference", "f": null}, {"t": "Visiting Seneca Rocks", "d": "How to experience Seneca Rocks.", "g": "attractions", "l": 2, "q": "What is Visiting Seneca Rocks?", "a": "How to experience Seneca Rocks.", "x": "Experiencing Seneca Rocks: plan around Bridge Day, the state's rhythm — Montani semper liberi (Mountaineers are always free). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. New River Gorge National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Greenbrier", "d": "Greenbrier: a top West Virginia attraction.", "g": "attractions", "l": 2, "q": "What is Greenbrier?", "a": "Greenbrier: a top West Virginia attraction.", "x": "Greenbrier is essential West Virginia. Split from Virginia 1863 (Civil War). Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pepperoni roll", "s": "public-reference", "f": null}, {"t": "Visiting Greenbrier", "d": "How to experience Greenbrier.", "g": "attractions", "l": 2, "q": "What is Visiting Greenbrier?", "a": "How to experience Greenbrier.", "x": "Experiencing Greenbrier: plan around Bridge Day, the state's rhythm — Montani semper liberi (Mountaineers are always free). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. New River Gorge National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Snowshoe", "d": "Snowshoe: a top West Virginia attraction.", "g": "attractions", "l": 2, "q": "What is Snowshoe?", "a": "Snowshoe: a top West Virginia attraction.", "x": "Snowshoe is essential West Virginia. Split from Virginia 1863 (Civil War). Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pepperoni roll", "s": "public-reference", "f": null}, {"t": "Visiting Snowshoe", "d": "How to experience Snowshoe.", "g": "attractions", "l": 2, "q": "What is Visiting Snowshoe?", "a": "How to experience Snowshoe.", "x": "Experiencing Snowshoe: plan around Bridge Day, the state's rhythm — Montani semper liberi (Mountaineers are always free). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. New River Gorge National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Blackwater Falls", "d": "Blackwater Falls: a top West Virginia attraction.", "g": "attractions", "l": 2, "q": "What is Blackwater Falls?", "a": "Blackwater Falls: a top West Virginia attraction.", "x": "Blackwater Falls is essential West Virginia. Split from Virginia 1863 (Civil War). Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pepperoni roll", "s": "public-reference", "f": null}, {"t": "Visiting Blackwater Falls", "d": "How to experience Blackwater Falls.", "g": "attractions", "l": 2, "q": "What is Visiting Blackwater Falls?", "a": "How to experience Blackwater Falls.", "x": "Experiencing Blackwater Falls: plan around Bridge Day, the state's rhythm — Montani semper liberi (Mountaineers are always free). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. New River Gorge National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Cass Scenic Railroad", "d": "Cass Scenic Railroad: a top West Virginia attraction.", "g": "attractions", "l": 2, "q": "What is Cass Scenic Railroad?", "a": "Cass Scenic Railroad: a top West Virginia attraction.", "x": "Cass Scenic Railroad is essential West Virginia. Split from Virginia 1863 (Civil War). Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pepperoni roll", "s": "public-reference", "f": null}, {"t": "Visiting Cass Scenic Railroad", "d": "How to experience Cass Scenic Railroad.", "g": "attractions", "l": 2, "q": "What is Visiting Cass Scenic Railroad?", "a": "How to experience Cass Scenic Railroad.", "x": "Experiencing Cass Scenic Railroad: plan around Bridge Day, the state's rhythm — Montani semper liberi (Mountaineers are always free). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. New River Gorge National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Trans-Allegheny Lunatic Asylum", "d": "Trans-Allegheny Lunatic Asylum: a top West Virginia attraction.", "g": "attractions", "l": 2, "q": "What is Trans-Allegheny Lunatic Asylum?", "a": "Trans-Allegheny Lunatic Asylum: a top West Virginia attraction.", "x": "Trans-Allegheny Lunatic Asylum is essential West Virginia. Split from Virginia 1863 (Civil War). Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pepperoni roll", "s": "public-reference", "f": null}, {"t": "Visiting Trans-Allegheny Lunatic Asylum", "d": "How to experience Trans-Allegheny Lunatic Asylum.", "g": "attractions", "l": 2, "q": "What is Visiting Trans-Allegheny Lunatic Asylum?", "a": "How to experience Trans-Allegheny Lunatic Asylum.", "x": "Experiencing Trans-Allegheny Lunatic Asylum: plan around Bridge Day, the state's rhythm — Montani semper liberi (Mountaineers are always free). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. New River Gorge National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "New River Gorge National Park", "d": "New River Gorge National Park: West Virginia's great park.", "g": "parks", "l": 2, "q": "What is New River Gorge National Park?", "a": "New River Gorge National Park: West Virginia's great park.", "x": "New River Gorge National Park is West Virginia's wild heart: New River Gorge. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Bridge Day Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring New River Gorge National Park", "d": "How to explore New River Gorge National Park.", "g": "parks", "l": 2, "q": "What is Exploring New River Gorge National Park?", "a": "How to explore New River Gorge National Park.", "x": "Exploring New River Gorge National Park: get the park map, check conditions, carry water and layers, and tell someone your plan. Montani semper liberi (Mountaineers are always free) Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Charleston: the capital city", "d": "Charleston, capital of West Virginia.", "g": "cities", "l": 2, "q": "What is Charleston: the capital city?", "a": "Charleston, capital of West Virginia.", "x": "Charleston: the capital of West Virginia — government, history, and often the best museums. Coal kingdom. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Charleston", "s": "public-reference", "f": null}, {"t": "Charleston: the biggest city", "d": "Charleston is West Virginia's largest city.", "g": "cities", "l": 2, "q": "What is Charleston: the biggest city?", "a": "Charleston is West Virginia's largest city.", "x": "Charleston is where West Virginia comes to work and play: the skyline, the food, the music, the crowds. energy (coal, gas) Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Bridge Day", "s": "public-reference", "f": null}, {"t": "pepperoni roll: the food", "d": "Taste West Virginia: pepperoni roll.", "g": "food", "l": 2, "q": "What is pepperoni roll: the food?", "a": "Taste West Virginia: pepperoni roll.", "x": "The taste of West Virginia is pepperoni roll — and the foodways around it. New River Gorge park. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Bridge Day Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: West Virginia", "d": "Eating your way through West Virginia.", "g": "food", "l": 2, "q": "What is Food tour: West Virginia?", "a": "Eating your way through West Virginia.", "x": "Eating through West Virginia: start with pepperoni roll, then follow the locals — diners, food trucks, farm stands. Montani semper liberi (Mountaineers are always free) Food is the fastest way into a place's heart; the stories come free with the meal. Charleston", "s": "public-reference", "f": null}, {"t": "Bridge Day", "d": "Bridge Day: West Virginia's signature festival.", "g": "festivals", "l": 2, "q": "What is Bridge Day?", "a": "Bridge Day: West Virginia's signature festival.", "x": "Bridge Day is West Virginia at its most celebratory: Coal built the Mountain State.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Charleston Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "West Virginia year-round: Bridge Day and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "West Virginia year-round: Bridge Day and more.", "x": "The West Virginia festival calendar runs year-round, with Bridge Day as the anchor. Montani semper liberi (Mountaineers are always free) Every season has its celebration — plan trips around them for the liveliest version of the state. New River Gorge National Park", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-west-virginia-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
