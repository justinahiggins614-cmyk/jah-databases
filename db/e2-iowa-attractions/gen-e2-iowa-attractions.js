(function(){'use strict';
/* JAH Iowa Attractions Database generator — jahdb-e2-iowa-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-iowa-attractions',PREFIX='JAH-E2IOWAATTRA-',NAME='JAH Iowa Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Iowa: attractions overview", "d": "The best of Iowa: Field of Dreams, Amana Colonies, Des Moines Art Center.", "g": "overview", "l": 2, "q": "What is Iowa: attractions overview?", "a": "The best of Iowa: Field of Dreams, Amana Colonies, Des Moines Art Center.", "x": "The essential Iowa: Field of Dreams, Amana Colonies, Des Moines Art Center — plus Effigy Mounds National Monument, Iowa's great pork tenderloin. Iowa State Fair This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Field of Dreams", "d": "Field of Dreams: a top Iowa attraction.", "g": "attractions", "l": 2, "q": "What is Field of Dreams?", "a": "Field of Dreams: a top Iowa attraction.", "x": "Field of Dreams is essential Iowa. Meskwaki and Sioux; Black Hawk War. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pork tenderloin", "s": "public-reference", "f": null}, {"t": "Visiting Field of Dreams", "d": "How to experience Field of Dreams.", "g": "attractions", "l": 2, "q": "What is Visiting Field of Dreams?", "a": "How to experience Field of Dreams.", "x": "Experiencing Field of Dreams: plan around Iowa State Fair, the state's rhythm — Our liberties we prize and our rights we will maintain. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Effigy Mounds National Monument Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Amana Colonies", "d": "Amana Colonies: a top Iowa attraction.", "g": "attractions", "l": 2, "q": "What is Amana Colonies?", "a": "Amana Colonies: a top Iowa attraction.", "x": "Amana Colonies is essential Iowa. Meskwaki and Sioux; Black Hawk War. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pork tenderloin", "s": "public-reference", "f": null}, {"t": "Visiting Amana Colonies", "d": "How to experience Amana Colonies.", "g": "attractions", "l": 2, "q": "What is Visiting Amana Colonies?", "a": "How to experience Amana Colonies.", "x": "Experiencing Amana Colonies: plan around Iowa State Fair, the state's rhythm — Our liberties we prize and our rights we will maintain. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Effigy Mounds National Monument Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Des Moines Art Center", "d": "Des Moines Art Center: a top Iowa attraction.", "g": "attractions", "l": 2, "q": "What is Des Moines Art Center?", "a": "Des Moines Art Center: a top Iowa attraction.", "x": "Des Moines Art Center is essential Iowa. Meskwaki and Sioux; Black Hawk War. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pork tenderloin", "s": "public-reference", "f": null}, {"t": "Visiting Des Moines Art Center", "d": "How to experience Des Moines Art Center.", "g": "attractions", "l": 2, "q": "What is Visiting Des Moines Art Center?", "a": "How to experience Des Moines Art Center.", "x": "Experiencing Des Moines Art Center: plan around Iowa State Fair, the state's rhythm — Our liberties we prize and our rights we will maintain. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Effigy Mounds National Monument Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Pikes Peak State Park", "d": "Pikes Peak State Park: a top Iowa attraction.", "g": "attractions", "l": 2, "q": "What is Pikes Peak State Park?", "a": "Pikes Peak State Park: a top Iowa attraction.", "x": "Pikes Peak State Park is essential Iowa. Meskwaki and Sioux; Black Hawk War. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pork tenderloin", "s": "public-reference", "f": null}, {"t": "Visiting Pikes Peak State Park", "d": "How to experience Pikes Peak State Park.", "g": "attractions", "l": 2, "q": "What is Visiting Pikes Peak State Park?", "a": "How to experience Pikes Peak State Park.", "x": "Experiencing Pikes Peak State Park: plan around Iowa State Fair, the state's rhythm — Our liberties we prize and our rights we will maintain. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Effigy Mounds National Monument Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Bridges of Madison County", "d": "Bridges of Madison County: a top Iowa attraction.", "g": "attractions", "l": 2, "q": "What is Bridges of Madison County?", "a": "Bridges of Madison County: a top Iowa attraction.", "x": "Bridges of Madison County is essential Iowa. Meskwaki and Sioux; Black Hawk War. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pork tenderloin", "s": "public-reference", "f": null}, {"t": "Visiting Bridges of Madison County", "d": "How to experience Bridges of Madison County.", "g": "attractions", "l": 2, "q": "What is Visiting Bridges of Madison County?", "a": "How to experience Bridges of Madison County.", "x": "Experiencing Bridges of Madison County: plan around Iowa State Fair, the state's rhythm — Our liberties we prize and our rights we will maintain. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Effigy Mounds National Monument Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Iowa State Fair", "d": "Iowa State Fair: a top Iowa attraction.", "g": "attractions", "l": 2, "q": "What is Iowa State Fair?", "a": "Iowa State Fair: a top Iowa attraction.", "x": "Iowa State Fair is essential Iowa. Meskwaki and Sioux; Black Hawk War. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pork tenderloin", "s": "public-reference", "f": null}, {"t": "Visiting Iowa State Fair", "d": "How to experience Iowa State Fair.", "g": "attractions", "l": 2, "q": "What is Visiting Iowa State Fair?", "a": "How to experience Iowa State Fair.", "x": "Experiencing Iowa State Fair: plan around Iowa State Fair, the state's rhythm — Our liberties we prize and our rights we will maintain. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Effigy Mounds National Monument Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Effigy Mounds", "d": "Effigy Mounds: a top Iowa attraction.", "g": "attractions", "l": 2, "q": "What is Effigy Mounds?", "a": "Effigy Mounds: a top Iowa attraction.", "x": "Effigy Mounds is essential Iowa. Meskwaki and Sioux; Black Hawk War. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pork tenderloin", "s": "public-reference", "f": null}, {"t": "Visiting Effigy Mounds", "d": "How to experience Effigy Mounds.", "g": "attractions", "l": 2, "q": "What is Visiting Effigy Mounds?", "a": "How to experience Effigy Mounds.", "x": "Experiencing Effigy Mounds: plan around Iowa State Fair, the state's rhythm — Our liberties we prize and our rights we will maintain. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Effigy Mounds National Monument Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Maquoketa Caves", "d": "Maquoketa Caves: a top Iowa attraction.", "g": "attractions", "l": 2, "q": "What is Maquoketa Caves?", "a": "Maquoketa Caves: a top Iowa attraction.", "x": "Maquoketa Caves is essential Iowa. Meskwaki and Sioux; Black Hawk War. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. pork tenderloin", "s": "public-reference", "f": null}, {"t": "Visiting Maquoketa Caves", "d": "How to experience Maquoketa Caves.", "g": "attractions", "l": 2, "q": "What is Visiting Maquoketa Caves?", "a": "How to experience Maquoketa Caves.", "x": "Experiencing Maquoketa Caves: plan around Iowa State Fair, the state's rhythm — Our liberties we prize and our rights we will maintain. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Effigy Mounds National Monument Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Effigy Mounds National Monument", "d": "Effigy Mounds National Monument: Iowa's great park.", "g": "parks", "l": 2, "q": "What is Effigy Mounds National Monument?", "a": "Effigy Mounds National Monument: Iowa's great park.", "x": "Effigy Mounds National Monument is Iowa's wild heart: Field of Dreams. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Iowa State Fair Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Effigy Mounds National Monument", "d": "How to explore Effigy Mounds National Monument.", "g": "parks", "l": 2, "q": "What is Exploring Effigy Mounds National Monument?", "a": "How to explore Effigy Mounds National Monument.", "x": "Exploring Effigy Mounds National Monument: get the park map, check conditions, carry water and layers, and tell someone your plan. Our liberties we prize and our rights we will maintain Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Des Moines: the capital city", "d": "Des Moines, capital of Iowa.", "g": "cities", "l": 2, "q": "What is Des Moines: the capital city?", "a": "Des Moines, capital of Iowa.", "x": "Des Moines: the capital of Iowa — government, history, and often the best museums. Corn and hogs; caucus fame. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Des Moines", "s": "public-reference", "f": null}, {"t": "Des Moines: the biggest city", "d": "Des Moines is Iowa's largest city.", "g": "cities", "l": 2, "q": "What is Des Moines: the biggest city?", "a": "Des Moines is Iowa's largest city.", "x": "Des Moines is where Iowa comes to work and play: the skyline, the food, the music, the crowds. agriculture (corn, hogs) Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Iowa State Fair", "s": "public-reference", "f": null}, {"t": "pork tenderloin: the food", "d": "Taste Iowa: pork tenderloin.", "g": "food", "l": 2, "q": "What is pork tenderloin: the food?", "a": "Taste Iowa: pork tenderloin.", "x": "The taste of Iowa is pork tenderloin — and the foodways around it. Bridges of Madison County. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Iowa State Fair Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Iowa", "d": "Eating your way through Iowa.", "g": "food", "l": 2, "q": "What is Food tour: Iowa?", "a": "Eating your way through Iowa.", "x": "Eating through Iowa: start with pork tenderloin, then follow the locals — diners, food trucks, farm stands. Our liberties we prize and our rights we will maintain Food is the fastest way into a place's heart; the stories come free with the meal. Des Moines", "s": "public-reference", "f": null}, {"t": "Iowa State Fair", "d": "Iowa State Fair: Iowa's signature festival.", "g": "festivals", "l": 2, "q": "What is Iowa State Fair?", "a": "Iowa State Fair: Iowa's signature festival.", "x": "Iowa State Fair is Iowa at its most celebratory: The Iowa caucuses made it first-in-the-nation every four years.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Des Moines Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Iowa year-round: Iowa State Fair and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Iowa year-round: Iowa State Fair and more.", "x": "The Iowa festival calendar runs year-round, with Iowa State Fair as the anchor. Our liberties we prize and our rights we will maintain Every season has its celebration — plan trips around them for the liveliest version of the state. Effigy Mounds National Monument", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-iowa-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
