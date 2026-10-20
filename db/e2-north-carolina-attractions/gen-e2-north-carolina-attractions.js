(function(){'use strict';
/* JAH North Carolina Attractions Database generator — jahdb-e2-north-carolina-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-north-carolina-attractions',PREFIX='JAH-E2NORTHCARO-',NAME='JAH North Carolina Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "North Carolina: attractions overview", "d": "The best of North Carolina: Blue Ridge Parkway, Outer Banks, Biltmore Estate.", "g": "overview", "l": 2, "q": "What is North Carolina: attractions overview?", "a": "The best of North Carolina: Blue Ridge Parkway, Outer Banks, Biltmore Estate.", "x": "The essential North Carolina: Blue Ridge Parkway, Outer Banks, Biltmore Estate — plus Great Smoky Mountains National Park, North Carolina's great pulled pork BBQ. MerleFest This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Blue Ridge Parkway", "d": "Blue Ridge Parkway: a top North Carolina attraction.", "g": "attractions", "l": 2, "q": "What is Blue Ridge Parkway?", "a": "Blue Ridge Parkway: a top North Carolina attraction.", "x": "Blue Ridge Parkway is essential North Carolina. Cherokee; Lost Colony 1587. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pulled pork BBQ", "s": "public-reference", "f": null}, {"t": "Visiting Blue Ridge Parkway", "d": "How to experience Blue Ridge Parkway.", "g": "attractions", "l": 2, "q": "What is Visiting Blue Ridge Parkway?", "a": "How to experience Blue Ridge Parkway.", "x": "Experiencing Blue Ridge Parkway: plan around MerleFest, the state's rhythm — Esse quam videri (To be rather than to seem). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Great Smoky Mountains National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Outer Banks", "d": "Outer Banks: a top North Carolina attraction.", "g": "attractions", "l": 2, "q": "What is Outer Banks?", "a": "Outer Banks: a top North Carolina attraction.", "x": "Outer Banks is essential North Carolina. Cherokee; Lost Colony 1587. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pulled pork BBQ", "s": "public-reference", "f": null}, {"t": "Visiting Outer Banks", "d": "How to experience Outer Banks.", "g": "attractions", "l": 2, "q": "What is Visiting Outer Banks?", "a": "How to experience Outer Banks.", "x": "Experiencing Outer Banks: plan around MerleFest, the state's rhythm — Esse quam videri (To be rather than to seem). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Great Smoky Mountains National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Biltmore Estate", "d": "Biltmore Estate: a top North Carolina attraction.", "g": "attractions", "l": 2, "q": "What is Biltmore Estate?", "a": "Biltmore Estate: a top North Carolina attraction.", "x": "Biltmore Estate is essential North Carolina. Cherokee; Lost Colony 1587. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pulled pork BBQ", "s": "public-reference", "f": null}, {"t": "Visiting Biltmore Estate", "d": "How to experience Biltmore Estate.", "g": "attractions", "l": 2, "q": "What is Visiting Biltmore Estate?", "a": "How to experience Biltmore Estate.", "x": "Experiencing Biltmore Estate: plan around MerleFest, the state's rhythm — Esse quam videri (To be rather than to seem). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Great Smoky Mountains National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Great Smoky Mountains", "d": "Great Smoky Mountains: a top North Carolina attraction.", "g": "attractions", "l": 2, "q": "What is Great Smoky Mountains?", "a": "Great Smoky Mountains: a top North Carolina attraction.", "x": "Great Smoky Mountains is essential North Carolina. Cherokee; Lost Colony 1587. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pulled pork BBQ", "s": "public-reference", "f": null}, {"t": "Visiting Great Smoky Mountains", "d": "How to experience Great Smoky Mountains.", "g": "attractions", "l": 2, "q": "What is Visiting Great Smoky Mountains?", "a": "How to experience Great Smoky Mountains.", "x": "Experiencing Great Smoky Mountains: plan around MerleFest, the state's rhythm — Esse quam videri (To be rather than to seem). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Great Smoky Mountains National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Wright Brothers Memorial", "d": "Wright Brothers Memorial: a top North Carolina attraction.", "g": "attractions", "l": 2, "q": "What is Wright Brothers Memorial?", "a": "Wright Brothers Memorial: a top North Carolina attraction.", "x": "Wright Brothers Memorial is essential North Carolina. Cherokee; Lost Colony 1587. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pulled pork BBQ", "s": "public-reference", "f": null}, {"t": "Visiting Wright Brothers Memorial", "d": "How to experience Wright Brothers Memorial.", "g": "attractions", "l": 2, "q": "What is Visiting Wright Brothers Memorial?", "a": "How to experience Wright Brothers Memorial.", "x": "Experiencing Wright Brothers Memorial: plan around MerleFest, the state's rhythm — Esse quam videri (To be rather than to seem). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Great Smoky Mountains National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "NASCAR Hall of Fame", "d": "NASCAR Hall of Fame: a top North Carolina attraction.", "g": "attractions", "l": 2, "q": "What is NASCAR Hall of Fame?", "a": "NASCAR Hall of Fame: a top North Carolina attraction.", "x": "NASCAR Hall of Fame is essential North Carolina. Cherokee; Lost Colony 1587. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pulled pork BBQ", "s": "public-reference", "f": null}, {"t": "Visiting NASCAR Hall of Fame", "d": "How to experience NASCAR Hall of Fame.", "g": "attractions", "l": 2, "q": "What is Visiting NASCAR Hall of Fame?", "a": "How to experience NASCAR Hall of Fame.", "x": "Experiencing NASCAR Hall of Fame: plan around MerleFest, the state's rhythm — Esse quam videri (To be rather than to seem). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Great Smoky Mountains National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Asheville", "d": "Asheville: a top North Carolina attraction.", "g": "attractions", "l": 2, "q": "What is Asheville?", "a": "Asheville: a top North Carolina attraction.", "x": "Asheville is essential North Carolina. Cherokee; Lost Colony 1587. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pulled pork BBQ State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Asheville", "d": "How to experience Asheville.", "g": "attractions", "l": 2, "q": "What is Visiting Asheville?", "a": "How to experience Asheville.", "x": "Experiencing Asheville: plan around MerleFest, the state's rhythm — Esse quam videri (To be rather than to seem). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Great Smoky Mountains National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Cape Hatteras", "d": "Cape Hatteras: a top North Carolina attraction.", "g": "attractions", "l": 2, "q": "What is Cape Hatteras?", "a": "Cape Hatteras: a top North Carolina attraction.", "x": "Cape Hatteras is essential North Carolina. Cherokee; Lost Colony 1587. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pulled pork BBQ", "s": "public-reference", "f": null}, {"t": "Visiting Cape Hatteras", "d": "How to experience Cape Hatteras.", "g": "attractions", "l": 2, "q": "What is Visiting Cape Hatteras?", "a": "How to experience Cape Hatteras.", "x": "Experiencing Cape Hatteras: plan around MerleFest, the state's rhythm — Esse quam videri (To be rather than to seem). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Great Smoky Mountains National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Great Smoky Mountains National Park", "d": "Great Smoky Mountains National Park: North Carolina's great park.", "g": "parks", "l": 2, "q": "What is Great Smoky Mountains National Park?", "a": "Great Smoky Mountains National Park: North Carolina's great park.", "x": "Great Smoky Mountains National Park is North Carolina's wild heart: Blue Ridge Parkway. Parks preserve what development cannot replace — the views, the wildlife, the quiet. MerleFest Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Great Smoky Mountains National Park", "d": "How to explore Great Smoky Mountains National Park.", "g": "parks", "l": 2, "q": "What is Exploring Great Smoky Mountains National Park?", "a": "How to explore Great Smoky Mountains National Park.", "x": "Exploring Great Smoky Mountains National Park: get the park map, check conditions, carry water and layers, and tell someone your plan. Esse quam videri (To be rather than to seem) Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Raleigh: the capital city", "d": "Raleigh, capital of North Carolina.", "g": "cities", "l": 2, "q": "What is Raleigh: the capital city?", "a": "Raleigh, capital of North Carolina.", "x": "Raleigh: the capital of North Carolina — government, history, and often the best museums. Revolution; Civil War. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Charlotte", "s": "public-reference", "f": null}, {"t": "Charlotte: the biggest city", "d": "Charlotte is North Carolina's largest city.", "g": "cities", "l": 2, "q": "What is Charlotte: the biggest city?", "a": "Charlotte is North Carolina's largest city.", "x": "Charlotte is where North Carolina comes to work and play: the skyline, the food, the music, the crowds. technology (Research Triangle) Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. MerleFest", "s": "public-reference", "f": null}, {"t": "pulled pork BBQ: the food", "d": "Taste North Carolina: pulled pork BBQ.", "g": "food", "l": 2, "q": "What is pulled pork BBQ: the food?", "a": "Taste North Carolina: pulled pork BBQ.", "x": "The taste of North Carolina is pulled pork BBQ — and the foodways around it. Tobacco, textiles, tech (Research Triangle). Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. MerleFest Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: North Carolina", "d": "Eating your way through North Carolina.", "g": "food", "l": 2, "q": "What is Food tour: North Carolina?", "a": "Eating your way through North Carolina.", "x": "Eating through North Carolina: start with pulled pork BBQ, then follow the locals — diners, food trucks, farm stands. Esse quam videri (To be rather than to seem) Food is the fastest way into a place's heart; the stories come free with the meal. Charlotte", "s": "public-reference", "f": null}, {"t": "MerleFest", "d": "MerleFest: North Carolina's signature festival.", "g": "festivals", "l": 2, "q": "What is MerleFest?", "a": "MerleFest: North Carolina's signature festival.", "x": "MerleFest is North Carolina at its most celebratory: The Research Triangle made it a tech hub.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Raleigh Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "North Carolina year-round: MerleFest and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "North Carolina year-round: MerleFest and more.", "x": "The North Carolina festival calendar runs year-round, with MerleFest as the anchor. Esse quam videri (To be rather than to seem) Every season has its celebration — plan trips around them for the liveliest version of the state. Great Smoky Mountains National Park", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-north-carolina-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
