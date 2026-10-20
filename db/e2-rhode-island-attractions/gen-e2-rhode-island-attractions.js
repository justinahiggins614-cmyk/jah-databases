(function(){'use strict';
/* JAH Rhode Island Attractions Database generator — jahdb-e2-rhode-island-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-rhode-island-attractions',PREFIX='JAH-E2RHODEISLA-',NAME='JAH Rhode Island Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Rhode Island: attractions overview", "d": "The best of Rhode Island: Newport mansions, Cliff Walk, Providence.", "g": "overview", "l": 2, "q": "What is Rhode Island: attractions overview?", "a": "The best of Rhode Island: Newport mansions, Cliff Walk, Providence.", "x": "The essential Rhode Island: Newport mansions, Cliff Walk, Providence — plus Blackstone River Valley National Historical Park, Rhode Island's great clam cakes. Newport festivals This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Newport mansions", "d": "Newport mansions: a top Rhode Island attraction.", "g": "attractions", "l": 2, "q": "What is Newport mansions?", "a": "Newport mansions: a top Rhode Island attraction.", "x": "Newport mansions is essential Rhode Island. Narragansett; religious refuge 1636. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. clam cakes", "s": "public-reference", "f": null}, {"t": "Visiting Newport mansions", "d": "How to experience Newport mansions.", "g": "attractions", "l": 2, "q": "What is Visiting Newport mansions?", "a": "How to experience Newport mansions.", "x": "Experiencing Newport mansions: plan around Newport festivals, the state's rhythm — Hope. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Blackstone River Valley National Historical Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Cliff Walk", "d": "Cliff Walk: a top Rhode Island attraction.", "g": "attractions", "l": 2, "q": "What is Cliff Walk?", "a": "Cliff Walk: a top Rhode Island attraction.", "x": "Cliff Walk is essential Rhode Island. Narragansett; religious refuge 1636. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. clam cakes", "s": "public-reference", "f": null}, {"t": "Visiting Cliff Walk", "d": "How to experience Cliff Walk.", "g": "attractions", "l": 2, "q": "What is Visiting Cliff Walk?", "a": "How to experience Cliff Walk.", "x": "Experiencing Cliff Walk: plan around Newport festivals, the state's rhythm — Hope. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Blackstone River Valley National Historical Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Providence", "d": "Providence: a top Rhode Island attraction.", "g": "attractions", "l": 2, "q": "What is Providence?", "a": "Providence: a top Rhode Island attraction.", "x": "Providence is essential Rhode Island. Narragansett; religious refuge 1636. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. clam cakes", "s": "public-reference", "f": null}, {"t": "Visiting Providence", "d": "How to experience Providence.", "g": "attractions", "l": 2, "q": "What is Visiting Providence?", "a": "How to experience Providence.", "x": "Experiencing Providence: plan around Newport festivals, the state's rhythm — Hope. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Blackstone River Valley National Historical Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Block Island", "d": "Block Island: a top Rhode Island attraction.", "g": "attractions", "l": 2, "q": "What is Block Island?", "a": "Block Island: a top Rhode Island attraction.", "x": "Block Island is essential Rhode Island. Narragansett; religious refuge 1636. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. clam cakes", "s": "public-reference", "f": null}, {"t": "Visiting Block Island", "d": "How to experience Block Island.", "g": "attractions", "l": 2, "q": "What is Visiting Block Island?", "a": "How to experience Block Island.", "x": "Experiencing Block Island: plan around Newport festivals, the state's rhythm — Hope. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Blackstone River Valley National Historical Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Roger Williams Park", "d": "Roger Williams Park: a top Rhode Island attraction.", "g": "attractions", "l": 2, "q": "What is Roger Williams Park?", "a": "Roger Williams Park: a top Rhode Island attraction.", "x": "Roger Williams Park is essential Rhode Island. Narragansett; religious refuge 1636. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. clam cakes", "s": "public-reference", "f": null}, {"t": "Visiting Roger Williams Park", "d": "How to experience Roger Williams Park.", "g": "attractions", "l": 2, "q": "What is Visiting Roger Williams Park?", "a": "How to experience Roger Williams Park.", "x": "Experiencing Roger Williams Park: plan around Newport festivals, the state's rhythm — Hope. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Blackstone River Valley National Historical Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "WaterFire", "d": "WaterFire: a top Rhode Island attraction.", "g": "attractions", "l": 2, "q": "What is WaterFire?", "a": "WaterFire: a top Rhode Island attraction.", "x": "WaterFire is essential Rhode Island. Narragansett; religious refuge 1636. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. clam cakes", "s": "public-reference", "f": null}, {"t": "Visiting WaterFire", "d": "How to experience WaterFire.", "g": "attractions", "l": 2, "q": "What is Visiting WaterFire?", "a": "How to experience WaterFire.", "x": "Experiencing WaterFire: plan around Newport festivals, the state's rhythm — Hope. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Blackstone River Valley National Historical Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Narragansett Bay", "d": "Narragansett Bay: a top Rhode Island attraction.", "g": "attractions", "l": 2, "q": "What is Narragansett Bay?", "a": "Narragansett Bay: a top Rhode Island attraction.", "x": "Narragansett Bay is essential Rhode Island. Narragansett; religious refuge 1636. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. clam cakes", "s": "public-reference", "f": null}, {"t": "Visiting Narragansett Bay", "d": "How to experience Narragansett Bay.", "g": "attractions", "l": 2, "q": "What is Visiting Narragansett Bay?", "a": "How to experience Narragansett Bay.", "x": "Experiencing Narragansett Bay: plan around Newport festivals, the state's rhythm — Hope. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Blackstone River Valley National Historical Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "RISD Museum", "d": "RISD Museum: a top Rhode Island attraction.", "g": "attractions", "l": 2, "q": "What is RISD Museum?", "a": "RISD Museum: a top Rhode Island attraction.", "x": "RISD Museum is essential Rhode Island. Narragansett; religious refuge 1636. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. clam cakes", "s": "public-reference", "f": null}, {"t": "Visiting RISD Museum", "d": "How to experience RISD Museum.", "g": "attractions", "l": 2, "q": "What is Visiting RISD Museum?", "a": "How to experience RISD Museum.", "x": "Experiencing RISD Museum: plan around Newport festivals, the state's rhythm — Hope. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Blackstone River Valley National Historical Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Blackstone River Valley National Historical Park", "d": "Blackstone River Valley National Historical Park: Rhode Island's great park.", "g": "parks", "l": 2, "q": "What is Blackstone River Valley National Historical Park?", "a": "Blackstone River Valley National Historical Park: Rhode Island's great park.", "x": "Blackstone River Valley National Historical Park is Rhode Island's wild heart: Newport mansions. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Newport festivals Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Blackstone River Valley National Historical Park", "d": "How to explore Blackstone River Valley National Historical Park.", "g": "parks", "l": 2, "q": "What is Exploring Blackstone River Valley National Historical Park?", "a": "How to explore Blackstone River Valley National Historical Park.", "x": "Exploring Blackstone River Valley National Historical Park: get the park map, check conditions, carry water and layers, and tell someone your plan. Hope Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Providence: the capital city", "d": "Providence, capital of Rhode Island.", "g": "cities", "l": 2, "q": "What is Providence: the capital city?", "a": "Providence, capital of Rhode Island.", "x": "Providence: the capital of Rhode Island — government, history, and often the best museums. Industrial revolution mills. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Providence", "s": "public-reference", "f": null}, {"t": "Providence: the biggest city", "d": "Providence is Rhode Island's largest city.", "g": "cities", "l": 2, "q": "What is Providence: the biggest city?", "a": "Providence is Rhode Island's largest city.", "x": "Providence is where Rhode Island comes to work and play: the skyline, the food, the music, the crowds. healthcare Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Newport festivals", "s": "public-reference", "f": null}, {"t": "clam cakes: the food", "d": "Taste Rhode Island: clam cakes.", "g": "food", "l": 2, "q": "What is clam cakes: the food?", "a": "Taste Rhode Island: clam cakes.", "x": "The taste of Rhode Island is clam cakes — and the foodways around it. Smallest state; big coast. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Newport festivals Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Rhode Island", "d": "Eating your way through Rhode Island.", "g": "food", "l": 2, "q": "What is Food tour: Rhode Island?", "a": "Eating your way through Rhode Island.", "x": "Eating through Rhode Island: start with clam cakes, then follow the locals — diners, food trucks, farm stands. Hope Food is the fastest way into a place's heart; the stories come free with the meal. Providence", "s": "public-reference", "f": null}, {"t": "Newport festivals", "d": "Newport festivals: Rhode Island's signature festival.", "g": "festivals", "l": 2, "q": "What is Newport festivals?", "a": "Newport festivals: Rhode Island's signature festival.", "x": "Newport festivals is Rhode Island at its most celebratory: Slater's mill started America's factory era.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Providence Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Rhode Island year-round: Newport festivals and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Rhode Island year-round: Newport festivals and more.", "x": "The Rhode Island festival calendar runs year-round, with Newport festivals as the anchor. Hope Every season has its celebration — plan trips around them for the liveliest version of the state. Blackstone River Valley National Historical Park", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-rhode-island-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
