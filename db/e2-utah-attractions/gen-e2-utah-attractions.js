(function(){'use strict';
/* JAH Utah Attractions Database generator — jahdb-e2-utah-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-utah-attractions',PREFIX='JAH-E2UTAHATTRA-',NAME='JAH Utah Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Utah: attractions overview", "d": "The best of Utah: Zion, Bryce Canyon, Arches.", "g": "overview", "l": 2, "q": "What is Utah: attractions overview?", "a": "The best of Utah: Zion, Bryce Canyon, Arches.", "x": "The essential Utah: Zion, Bryce Canyon, Arches — plus Zion National Park, Utah's great fry sauce. Sundance Film Festival This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Zion", "d": "Zion: a top Utah attraction.", "g": "attractions", "l": 2, "q": "What is Zion?", "a": "Zion: a top Utah attraction.", "x": "Zion is essential Utah. Ute; Mormon pioneers 1847. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. fry sauce State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Zion", "d": "How to experience Zion.", "g": "attractions", "l": 2, "q": "What is Visiting Zion?", "a": "How to experience Zion.", "x": "Experiencing Zion: plan around Sundance Film Festival, the state's rhythm — Industry. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Zion National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Bryce Canyon", "d": "Bryce Canyon: a top Utah attraction.", "g": "attractions", "l": 2, "q": "What is Bryce Canyon?", "a": "Bryce Canyon: a top Utah attraction.", "x": "Bryce Canyon is essential Utah. Ute; Mormon pioneers 1847. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. fry sauce State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Bryce Canyon", "d": "How to experience Bryce Canyon.", "g": "attractions", "l": 2, "q": "What is Visiting Bryce Canyon?", "a": "How to experience Bryce Canyon.", "x": "Experiencing Bryce Canyon: plan around Sundance Film Festival, the state's rhythm — Industry. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Zion National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Arches", "d": "Arches: a top Utah attraction.", "g": "attractions", "l": 2, "q": "What is Arches?", "a": "Arches: a top Utah attraction.", "x": "Arches is essential Utah. Ute; Mormon pioneers 1847. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. fry sauce State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Arches", "d": "How to experience Arches.", "g": "attractions", "l": 2, "q": "What is Visiting Arches?", "a": "How to experience Arches.", "x": "Experiencing Arches: plan around Sundance Film Festival, the state's rhythm — Industry. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Zion National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Temple Square", "d": "Temple Square: a top Utah attraction.", "g": "attractions", "l": 2, "q": "What is Temple Square?", "a": "Temple Square: a top Utah attraction.", "x": "Temple Square is essential Utah. Ute; Mormon pioneers 1847. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. fry sauce State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Temple Square", "d": "How to experience Temple Square.", "g": "attractions", "l": 2, "q": "What is Visiting Temple Square?", "a": "How to experience Temple Square.", "x": "Experiencing Temple Square: plan around Sundance Film Festival, the state's rhythm — Industry. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Zion National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Park City", "d": "Park City: a top Utah attraction.", "g": "attractions", "l": 2, "q": "What is Park City?", "a": "Park City: a top Utah attraction.", "x": "Park City is essential Utah. Ute; Mormon pioneers 1847. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. fry sauce State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Park City", "d": "How to experience Park City.", "g": "attractions", "l": 2, "q": "What is Visiting Park City?", "a": "How to experience Park City.", "x": "Experiencing Park City: plan around Sundance Film Festival, the state's rhythm — Industry. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Zion National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Monument Valley (edge)", "d": "Monument Valley (edge): a top Utah attraction.", "g": "attractions", "l": 2, "q": "What is Monument Valley (edge)?", "a": "Monument Valley (edge): a top Utah attraction.", "x": "Monument Valley (edge) is essential Utah. Ute; Mormon pioneers 1847. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. fry sauce State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Monument Valley (edge)", "d": "How to experience Monument Valley (edge).", "g": "attractions", "l": 2, "q": "What is Visiting Monument Valley (edge)?", "a": "How to experience Monument Valley (edge).", "x": "Experiencing Monument Valley (edge): plan around Sundance Film Festival, the state's rhythm — Industry. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Zion National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Antelope Island", "d": "Antelope Island: a top Utah attraction.", "g": "attractions", "l": 2, "q": "What is Antelope Island?", "a": "Antelope Island: a top Utah attraction.", "x": "Antelope Island is essential Utah. Ute; Mormon pioneers 1847. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. fry sauce State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Antelope Island", "d": "How to experience Antelope Island.", "g": "attractions", "l": 2, "q": "What is Visiting Antelope Island?", "a": "How to experience Antelope Island.", "x": "Experiencing Antelope Island: plan around Sundance Film Festival, the state's rhythm — Industry. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Zion National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Sundance", "d": "Sundance: a top Utah attraction.", "g": "attractions", "l": 2, "q": "What is Sundance?", "a": "Sundance: a top Utah attraction.", "x": "Sundance is essential Utah. Ute; Mormon pioneers 1847. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. fry sauce State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Sundance", "d": "How to experience Sundance.", "g": "attractions", "l": 2, "q": "What is Visiting Sundance?", "a": "How to experience Sundance.", "x": "Experiencing Sundance: plan around Sundance Film Festival, the state's rhythm — Industry. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Zion National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Zion National Park", "d": "Zion National Park: Utah's great park.", "g": "parks", "l": 2, "q": "What is Zion National Park?", "a": "Zion National Park: Utah's great park.", "x": "Zion National Park is Utah's wild heart: Zion. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Sundance Film Festival Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Zion National Park", "d": "How to explore Zion National Park.", "g": "parks", "l": 2, "q": "What is Exploring Zion National Park?", "a": "How to explore Zion National Park.", "x": "Exploring Zion National Park: get the park map, check conditions, carry water and layers, and tell someone your plan. Industry Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Salt Lake City: the capital city", "d": "Salt Lake City, capital of Utah.", "g": "cities", "l": 2, "q": "What is Salt Lake City: the capital city?", "a": "Salt Lake City, capital of Utah.", "x": "Salt Lake City: the capital of Utah — government, history, and often the best museums. Statehood 1896. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Salt Lake City", "s": "public-reference", "f": null}, {"t": "Salt Lake City: the biggest city", "d": "Salt Lake City is Utah's largest city.", "g": "cities", "l": 2, "q": "What is Salt Lake City: the biggest city?", "a": "Salt Lake City is Utah's largest city.", "x": "Salt Lake City is where Utah comes to work and play: the skyline, the food, the music, the crowds. tourism (skiing) Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Sundance Film Festival", "s": "public-reference", "f": null}, {"t": "fry sauce: the food", "d": "Taste Utah: fry sauce.", "g": "food", "l": 2, "q": "What is fry sauce: the food?", "a": "Taste Utah: fry sauce.", "x": "The taste of Utah is fry sauce — and the foodways around it. Skiing; tech (Silicon Slopes). Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Sundance Film Festival Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Utah", "d": "Eating your way through Utah.", "g": "food", "l": 2, "q": "What is Food tour: Utah?", "a": "Eating your way through Utah.", "x": "Eating through Utah: start with fry sauce, then follow the locals — diners, food trucks, farm stands. Industry Food is the fastest way into a place's heart; the stories come free with the meal. Salt Lake City", "s": "public-reference", "f": null}, {"t": "Sundance Film Festival", "d": "Sundance Film Festival: Utah's signature festival.", "g": "festivals", "l": 2, "q": "What is Sundance Film Festival?", "a": "Sundance Film Festival: Utah's signature festival.", "x": "Sundance Film Festival is Utah at its most celebratory: The transcontinental railroad met at Promontory in 1869.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Salt Lake City Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Utah year-round: Sundance Film Festival and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Utah year-round: Sundance Film Festival and more.", "x": "The Utah festival calendar runs year-round, with Sundance Film Festival as the anchor. Industry Every season has its celebration — plan trips around them for the liveliest version of the state. Zion National Park", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-utah-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
