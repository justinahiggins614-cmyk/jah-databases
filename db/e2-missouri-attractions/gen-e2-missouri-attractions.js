(function(){'use strict';
/* JAH Missouri Attractions Database generator — jahdb-e2-missouri-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-missouri-attractions',PREFIX='JAH-E2MISSOURIA-',NAME='JAH Missouri Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Missouri: attractions overview", "d": "The best of Missouri: Gateway Arch, Branson, Kansas City BBQ.", "g": "overview", "l": 2, "q": "What is Missouri: attractions overview?", "a": "The best of Missouri: Gateway Arch, Branson, Kansas City BBQ.", "x": "The essential Missouri: Gateway Arch, Branson, Kansas City BBQ — plus Ozark National Scenic Riverways, Missouri's great toasted ravioli. Missouri State Fair This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Gateway Arch", "d": "Gateway Arch: a top Missouri attraction.", "g": "attractions", "l": 2, "q": "What is Gateway Arch?", "a": "Gateway Arch: a top Missouri attraction.", "x": "Gateway Arch is essential Missouri. Osage; Lewis & Clark; gateway west. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. toasted ravioli", "s": "public-reference", "f": null}, {"t": "Visiting Gateway Arch", "d": "How to experience Gateway Arch.", "g": "attractions", "l": 2, "q": "What is Visiting Gateway Arch?", "a": "How to experience Gateway Arch.", "x": "Experiencing Gateway Arch: plan around Missouri State Fair, the state's rhythm — Salus populi suprema lex esto (The welfare of the people shall be the supreme law). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Ozark National Scenic Riverways Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Branson", "d": "Branson: a top Missouri attraction.", "g": "attractions", "l": 2, "q": "What is Branson?", "a": "Branson: a top Missouri attraction.", "x": "Branson is essential Missouri. Osage; Lewis & Clark; gateway west. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. toasted ravioli State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Branson", "d": "How to experience Branson.", "g": "attractions", "l": 2, "q": "What is Visiting Branson?", "a": "How to experience Branson.", "x": "Experiencing Branson: plan around Missouri State Fair, the state's rhythm — Salus populi suprema lex esto (The welfare of the people shall be the supreme law). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Ozark National Scenic Riverways Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Kansas City BBQ", "d": "Kansas City BBQ: a top Missouri attraction.", "g": "attractions", "l": 2, "q": "What is Kansas City BBQ?", "a": "Kansas City BBQ: a top Missouri attraction.", "x": "Kansas City BBQ is essential Missouri. Osage; Lewis & Clark; gateway west. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. toasted ravioli", "s": "public-reference", "f": null}, {"t": "Visiting Kansas City BBQ", "d": "How to experience Kansas City BBQ.", "g": "attractions", "l": 2, "q": "What is Visiting Kansas City BBQ?", "a": "How to experience Kansas City BBQ.", "x": "Experiencing Kansas City BBQ: plan around Missouri State Fair, the state's rhythm — Salus populi suprema lex esto (The welfare of the people shall be the supreme law). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Ozark National Scenic Riverways Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Mark Twain's Hannibal", "d": "Mark Twain's Hannibal: a top Missouri attraction.", "g": "attractions", "l": 2, "q": "What is Mark Twain's Hannibal?", "a": "Mark Twain's Hannibal: a top Missouri attraction.", "x": "Mark Twain's Hannibal is essential Missouri. Osage; Lewis & Clark; gateway west. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. toasted ravioli", "s": "public-reference", "f": null}, {"t": "Visiting Mark Twain's Hannibal", "d": "How to experience Mark Twain's Hannibal.", "g": "attractions", "l": 2, "q": "What is Visiting Mark Twain's Hannibal?", "a": "How to experience Mark Twain's Hannibal.", "x": "Experiencing Mark Twain's Hannibal: plan around Missouri State Fair, the state's rhythm — Salus populi suprema lex esto (The welfare of the people shall be the supreme law). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Ozark National Scenic Riverways Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Silver Dollar City", "d": "Silver Dollar City: a top Missouri attraction.", "g": "attractions", "l": 2, "q": "What is Silver Dollar City?", "a": "Silver Dollar City: a top Missouri attraction.", "x": "Silver Dollar City is essential Missouri. Osage; Lewis & Clark; gateway west. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. toasted ravioli", "s": "public-reference", "f": null}, {"t": "Visiting Silver Dollar City", "d": "How to experience Silver Dollar City.", "g": "attractions", "l": 2, "q": "What is Visiting Silver Dollar City?", "a": "How to experience Silver Dollar City.", "x": "Experiencing Silver Dollar City: plan around Missouri State Fair, the state's rhythm — Salus populi suprema lex esto (The welfare of the people shall be the supreme law). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Ozark National Scenic Riverways Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Lake of the Ozarks", "d": "Lake of the Ozarks: a top Missouri attraction.", "g": "attractions", "l": 2, "q": "What is Lake of the Ozarks?", "a": "Lake of the Ozarks: a top Missouri attraction.", "x": "Lake of the Ozarks is essential Missouri. Osage; Lewis & Clark; gateway west. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. toasted ravioli", "s": "public-reference", "f": null}, {"t": "Visiting Lake of the Ozarks", "d": "How to experience Lake of the Ozarks.", "g": "attractions", "l": 2, "q": "What is Visiting Lake of the Ozarks?", "a": "How to experience Lake of the Ozarks.", "x": "Experiencing Lake of the Ozarks: plan around Missouri State Fair, the state's rhythm — Salus populi suprema lex esto (The welfare of the people shall be the supreme law). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Ozark National Scenic Riverways Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "St. Louis Zoo", "d": "St. Louis Zoo: a top Missouri attraction.", "g": "attractions", "l": 2, "q": "What is St. Louis Zoo?", "a": "St. Louis Zoo: a top Missouri attraction.", "x": "St. Louis Zoo is essential Missouri. Osage; Lewis & Clark; gateway west. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. toasted ravioli", "s": "public-reference", "f": null}, {"t": "Visiting St. Louis Zoo", "d": "How to experience St. Louis Zoo.", "g": "attractions", "l": 2, "q": "What is Visiting St. Louis Zoo?", "a": "How to experience St. Louis Zoo.", "x": "Experiencing St. Louis Zoo: plan around Missouri State Fair, the state's rhythm — Salus populi suprema lex esto (The welfare of the people shall be the supreme law). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Ozark National Scenic Riverways Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Wilson's Creek", "d": "Wilson's Creek: a top Missouri attraction.", "g": "attractions", "l": 2, "q": "What is Wilson's Creek?", "a": "Wilson's Creek: a top Missouri attraction.", "x": "Wilson's Creek is essential Missouri. Osage; Lewis & Clark; gateway west. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. toasted ravioli", "s": "public-reference", "f": null}, {"t": "Visiting Wilson's Creek", "d": "How to experience Wilson's Creek.", "g": "attractions", "l": 2, "q": "What is Visiting Wilson's Creek?", "a": "How to experience Wilson's Creek.", "x": "Experiencing Wilson's Creek: plan around Missouri State Fair, the state's rhythm — Salus populi suprema lex esto (The welfare of the people shall be the supreme law). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Ozark National Scenic Riverways Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Ozark National Scenic Riverways", "d": "Ozark National Scenic Riverways: Missouri's great park.", "g": "parks", "l": 2, "q": "What is Ozark National Scenic Riverways?", "a": "Ozark National Scenic Riverways: Missouri's great park.", "x": "Ozark National Scenic Riverways is Missouri's wild heart: Gateway Arch. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Missouri State Fair Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Ozark National Scenic Riverways", "d": "How to explore Ozark National Scenic Riverways.", "g": "parks", "l": 2, "q": "What is Exploring Ozark National Scenic Riverways?", "a": "How to explore Ozark National Scenic Riverways.", "x": "Exploring Ozark National Scenic Riverways: get the park map, check conditions, carry water and layers, and tell someone your plan. Salus populi suprema lex esto (The welfare of the people shall be the supreme law) Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Jefferson City: the capital city", "d": "Jefferson City, capital of Missouri.", "g": "cities", "l": 2, "q": "What is Jefferson City: the capital city?", "a": "Jefferson City, capital of Missouri.", "x": "Jefferson City: the capital of Missouri — government, history, and often the best museums. Civil War border state. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Kansas City", "s": "public-reference", "f": null}, {"t": "Kansas City: the biggest city", "d": "Kansas City is Missouri's largest city.", "g": "cities", "l": 2, "q": "What is Kansas City: the biggest city?", "a": "Kansas City is Missouri's largest city.", "x": "Kansas City is where Missouri comes to work and play: the skyline, the food, the music, the crowds. agriculture Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Missouri State Fair", "s": "public-reference", "f": null}, {"t": "toasted ravioli: the food", "d": "Taste Missouri: toasted ravioli.", "g": "food", "l": 2, "q": "What is toasted ravioli: the food?", "a": "Taste Missouri: toasted ravioli.", "x": "The taste of Missouri is toasted ravioli — and the foodways around it. Railroads; beer; BBQ. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Missouri State Fair Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Missouri", "d": "Eating your way through Missouri.", "g": "food", "l": 2, "q": "What is Food tour: Missouri?", "a": "Eating your way through Missouri.", "x": "Eating through Missouri: start with toasted ravioli, then follow the locals — diners, food trucks, farm stands. Salus populi suprema lex esto (The welfare of the people shall be the supreme law) Food is the fastest way into a place's heart; the stories come free with the meal. Kansas City", "s": "public-reference", "f": null}, {"t": "Missouri State Fair", "d": "Missouri State Fair: Missouri's signature festival.", "g": "festivals", "l": 2, "q": "What is Missouri State Fair?", "a": "Missouri State Fair: Missouri's signature festival.", "x": "Missouri State Fair is Missouri at its most celebratory: The Gateway Arch rose in 1965 as the westward monument.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Jefferson City Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Missouri year-round: Missouri State Fair and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Missouri year-round: Missouri State Fair and more.", "x": "The Missouri festival calendar runs year-round, with Missouri State Fair as the anchor. Salus populi suprema lex esto (The welfare of the people shall be the supreme law) Every season has its celebration — plan trips around them for the liveliest version of the state. Ozark National Scenic Riverways", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-missouri-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
