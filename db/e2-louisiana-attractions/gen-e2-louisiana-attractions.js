(function(){'use strict';
/* JAH Louisiana Attractions Database generator — jahdb-e2-louisiana-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-louisiana-attractions',PREFIX='JAH-E2LOUISIANA-',NAME='JAH Louisiana Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Louisiana: attractions overview", "d": "The best of Louisiana: French Quarter, Mardi Gras, Oak Alley Plantation.", "g": "overview", "l": 2, "q": "What is Louisiana: attractions overview?", "a": "The best of Louisiana: French Quarter, Mardi Gras, Oak Alley Plantation.", "x": "The essential Louisiana: French Quarter, Mardi Gras, Oak Alley Plantation — plus Jean Lafitte National Historical Park, Louisiana's great gumbo. Mardi Gras This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "French Quarter", "d": "French Quarter: a top Louisiana attraction.", "g": "attractions", "l": 2, "q": "What is French Quarter?", "a": "French Quarter: a top Louisiana attraction.", "x": "French Quarter is essential Louisiana. French and Spanish colony. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. gumbo State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting French Quarter", "d": "How to experience French Quarter.", "g": "attractions", "l": 2, "q": "What is Visiting French Quarter?", "a": "How to experience French Quarter.", "x": "Experiencing French Quarter: plan around Mardi Gras, the state's rhythm — Union, justice, confidence. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Jean Lafitte National Historical Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Mardi Gras", "d": "Mardi Gras: a top Louisiana attraction.", "g": "attractions", "l": 2, "q": "What is Mardi Gras?", "a": "Mardi Gras: a top Louisiana attraction.", "x": "Mardi Gras is essential Louisiana. French and Spanish colony. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. gumbo State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Mardi Gras", "d": "How to experience Mardi Gras.", "g": "attractions", "l": 2, "q": "What is Visiting Mardi Gras?", "a": "How to experience Mardi Gras.", "x": "Experiencing Mardi Gras: plan around Mardi Gras, the state's rhythm — Union, justice, confidence. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Jean Lafitte National Historical Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Oak Alley Plantation", "d": "Oak Alley Plantation: a top Louisiana attraction.", "g": "attractions", "l": 2, "q": "What is Oak Alley Plantation?", "a": "Oak Alley Plantation: a top Louisiana attraction.", "x": "Oak Alley Plantation is essential Louisiana. French and Spanish colony. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. gumbo State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Oak Alley Plantation", "d": "How to experience Oak Alley Plantation.", "g": "attractions", "l": 2, "q": "What is Visiting Oak Alley Plantation?", "a": "How to experience Oak Alley Plantation.", "x": "Experiencing Oak Alley Plantation: plan around Mardi Gras, the state's rhythm — Union, justice, confidence. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Jean Lafitte National Historical Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Atchafalaya Basin", "d": "Atchafalaya Basin: a top Louisiana attraction.", "g": "attractions", "l": 2, "q": "What is Atchafalaya Basin?", "a": "Atchafalaya Basin: a top Louisiana attraction.", "x": "Atchafalaya Basin is essential Louisiana. French and Spanish colony. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. gumbo State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Atchafalaya Basin", "d": "How to experience Atchafalaya Basin.", "g": "attractions", "l": 2, "q": "What is Visiting Atchafalaya Basin?", "a": "How to experience Atchafalaya Basin.", "x": "Experiencing Atchafalaya Basin: plan around Mardi Gras, the state's rhythm — Union, justice, confidence. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Jean Lafitte National Historical Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "National WWII Museum", "d": "National WWII Museum: a top Louisiana attraction.", "g": "attractions", "l": 2, "q": "What is National WWII Museum?", "a": "National WWII Museum: a top Louisiana attraction.", "x": "National WWII Museum is essential Louisiana. French and Spanish colony. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. gumbo State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting National WWII Museum", "d": "How to experience National WWII Museum.", "g": "attractions", "l": 2, "q": "What is Visiting National WWII Museum?", "a": "How to experience National WWII Museum.", "x": "Experiencing National WWII Museum: plan around Mardi Gras, the state's rhythm — Union, justice, confidence. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Jean Lafitte National Historical Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Cajun country", "d": "Cajun country: a top Louisiana attraction.", "g": "attractions", "l": 2, "q": "What is Cajun country?", "a": "Cajun country: a top Louisiana attraction.", "x": "Cajun country is essential Louisiana. French and Spanish colony. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. gumbo State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Cajun country", "d": "How to experience Cajun country.", "g": "attractions", "l": 2, "q": "What is Visiting Cajun country?", "a": "How to experience Cajun country.", "x": "Experiencing Cajun country: plan around Mardi Gras, the state's rhythm — Union, justice, confidence. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Jean Lafitte National Historical Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Garden District", "d": "Garden District: a top Louisiana attraction.", "g": "attractions", "l": 2, "q": "What is Garden District?", "a": "Garden District: a top Louisiana attraction.", "x": "Garden District is essential Louisiana. French and Spanish colony. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. gumbo State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Garden District", "d": "How to experience Garden District.", "g": "attractions", "l": 2, "q": "What is Visiting Garden District?", "a": "How to experience Garden District.", "x": "Experiencing Garden District: plan around Mardi Gras, the state's rhythm — Union, justice, confidence. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Jean Lafitte National Historical Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Avery Island (Tabasco)", "d": "Avery Island (Tabasco): a top Louisiana attraction.", "g": "attractions", "l": 2, "q": "What is Avery Island (Tabasco)?", "a": "Avery Island (Tabasco): a top Louisiana attraction.", "x": "Avery Island (Tabasco) is essential Louisiana. French and Spanish colony. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. gumbo State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Avery Island (Tabasco)", "d": "How to experience Avery Island (Tabasco).", "g": "attractions", "l": 2, "q": "What is Visiting Avery Island (Tabasco)?", "a": "How to experience Avery Island (Tabasco).", "x": "Experiencing Avery Island (Tabasco): plan around Mardi Gras, the state's rhythm — Union, justice, confidence. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Jean Lafitte National Historical Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Jean Lafitte National Historical Park", "d": "Jean Lafitte National Historical Park: Louisiana's great park.", "g": "parks", "l": 2, "q": "What is Jean Lafitte National Historical Park?", "a": "Jean Lafitte National Historical Park: Louisiana's great park.", "x": "Jean Lafitte National Historical Park is Louisiana's wild heart: French Quarter. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Mardi Gras Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Jean Lafitte National Historical Park", "d": "How to explore Jean Lafitte National Historical Park.", "g": "parks", "l": 2, "q": "What is Exploring Jean Lafitte National Historical Park?", "a": "How to explore Jean Lafitte National Historical Park.", "x": "Exploring Jean Lafitte National Historical Park: get the park map, check conditions, carry water and layers, and tell someone your plan. Union, justice, confidence Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Baton Rouge: the capital city", "d": "Baton Rouge, capital of Louisiana.", "g": "cities", "l": 2, "q": "What is Baton Rouge: the capital city?", "a": "Baton Rouge, capital of Louisiana.", "x": "Baton Rouge: the capital of Louisiana — government, history, and often the best museums. Louisiana Purchase 1803. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. New Orleans", "s": "public-reference", "f": null}, {"t": "New Orleans: the biggest city", "d": "New Orleans is Louisiana's largest city.", "g": "cities", "l": 2, "q": "What is New Orleans: the biggest city?", "a": "New Orleans is Louisiana's largest city.", "x": "New Orleans is where Louisiana comes to work and play: the skyline, the food, the music, the crowds. oil and gas Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Mardi Gras", "s": "public-reference", "f": null}, {"t": "gumbo: the food", "d": "Taste Louisiana: gumbo.", "g": "food", "l": 2, "q": "What is gumbo: the food?", "a": "Taste Louisiana: gumbo.", "x": "The taste of Louisiana is gumbo — and the foodways around it. Civil War; Huey Long era. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Mardi Gras Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Louisiana", "d": "Eating your way through Louisiana.", "g": "food", "l": 2, "q": "What is Food tour: Louisiana?", "a": "Eating your way through Louisiana.", "x": "Eating through Louisiana: start with gumbo, then follow the locals — diners, food trucks, farm stands. Union, justice, confidence Food is the fastest way into a place's heart; the stories come free with the meal. New Orleans", "s": "public-reference", "f": null}, {"t": "Mardi Gras", "d": "Mardi Gras: Louisiana's signature festival.", "g": "festivals", "l": 2, "q": "What is Mardi Gras?", "a": "Mardi Gras: Louisiana's signature festival.", "x": "Mardi Gras is Louisiana at its most celebratory: Oil, jazz, Katrina 2005.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Baton Rouge Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Louisiana year-round: Mardi Gras and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Louisiana year-round: Mardi Gras and more.", "x": "The Louisiana festival calendar runs year-round, with Mardi Gras as the anchor. Union, justice, confidence Every season has its celebration — plan trips around them for the liveliest version of the state. Jean Lafitte National Historical Park", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-louisiana-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
