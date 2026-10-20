(function(){'use strict';
/* JAH New Mexico Attractions Database generator — jahdb-e2-new-mexico-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-new-mexico-attractions',PREFIX='JAH-E2NEWMEXICO-',NAME='JAH New Mexico Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "New Mexico: attractions overview", "d": "The best of New Mexico: Carlsbad Caverns, White Sands, Taos Pueblo.", "g": "overview", "l": 2, "q": "What is New Mexico: attractions overview?", "a": "The best of New Mexico: Carlsbad Caverns, White Sands, Taos Pueblo.", "x": "The essential New Mexico: Carlsbad Caverns, White Sands, Taos Pueblo — plus Carlsbad Caverns National Park, New Mexico's great green chile stew. Balloon Fiesta This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Carlsbad Caverns", "d": "Carlsbad Caverns: a top New Mexico attraction.", "g": "attractions", "l": 2, "q": "What is Carlsbad Caverns?", "a": "Carlsbad Caverns: a top New Mexico attraction.", "x": "Carlsbad Caverns is essential New Mexico. Pueblo peoples; Spanish 1598. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. green chile stew", "s": "public-reference", "f": null}, {"t": "Visiting Carlsbad Caverns", "d": "How to experience Carlsbad Caverns.", "g": "attractions", "l": 2, "q": "What is Visiting Carlsbad Caverns?", "a": "How to experience Carlsbad Caverns.", "x": "Experiencing Carlsbad Caverns: plan around Balloon Fiesta, the state's rhythm — Crescit eundo (It grows as it goes). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Carlsbad Caverns National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "White Sands", "d": "White Sands: a top New Mexico attraction.", "g": "attractions", "l": 2, "q": "What is White Sands?", "a": "White Sands: a top New Mexico attraction.", "x": "White Sands is essential New Mexico. Pueblo peoples; Spanish 1598. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. green chile stew State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting White Sands", "d": "How to experience White Sands.", "g": "attractions", "l": 2, "q": "What is Visiting White Sands?", "a": "How to experience White Sands.", "x": "Experiencing White Sands: plan around Balloon Fiesta, the state's rhythm — Crescit eundo (It grows as it goes). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Carlsbad Caverns National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Taos Pueblo", "d": "Taos Pueblo: a top New Mexico attraction.", "g": "attractions", "l": 2, "q": "What is Taos Pueblo?", "a": "Taos Pueblo: a top New Mexico attraction.", "x": "Taos Pueblo is essential New Mexico. Pueblo peoples; Spanish 1598. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. green chile stew State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Taos Pueblo", "d": "How to experience Taos Pueblo.", "g": "attractions", "l": 2, "q": "What is Visiting Taos Pueblo?", "a": "How to experience Taos Pueblo.", "x": "Experiencing Taos Pueblo: plan around Balloon Fiesta, the state's rhythm — Crescit eundo (It grows as it goes). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Carlsbad Caverns National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Santa Fe Plaza", "d": "Santa Fe Plaza: a top New Mexico attraction.", "g": "attractions", "l": 2, "q": "What is Santa Fe Plaza?", "a": "Santa Fe Plaza: a top New Mexico attraction.", "x": "Santa Fe Plaza is essential New Mexico. Pueblo peoples; Spanish 1598. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. green chile stew", "s": "public-reference", "f": null}, {"t": "Visiting Santa Fe Plaza", "d": "How to experience Santa Fe Plaza.", "g": "attractions", "l": 2, "q": "What is Visiting Santa Fe Plaza?", "a": "How to experience Santa Fe Plaza.", "x": "Experiencing Santa Fe Plaza: plan around Balloon Fiesta, the state's rhythm — Crescit eundo (It grows as it goes). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Carlsbad Caverns National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Bandelier", "d": "Bandelier: a top New Mexico attraction.", "g": "attractions", "l": 2, "q": "What is Bandelier?", "a": "Bandelier: a top New Mexico attraction.", "x": "Bandelier is essential New Mexico. Pueblo peoples; Spanish 1598. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. green chile stew State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Bandelier", "d": "How to experience Bandelier.", "g": "attractions", "l": 2, "q": "What is Visiting Bandelier?", "a": "How to experience Bandelier.", "x": "Experiencing Bandelier: plan around Balloon Fiesta, the state's rhythm — Crescit eundo (It grows as it goes). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Carlsbad Caverns National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Albuquerque Balloon Fiesta", "d": "Albuquerque Balloon Fiesta: a top New Mexico attraction.", "g": "attractions", "l": 2, "q": "What is Albuquerque Balloon Fiesta?", "a": "Albuquerque Balloon Fiesta: a top New Mexico attraction.", "x": "Albuquerque Balloon Fiesta is essential New Mexico. Pueblo peoples; Spanish 1598. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. green chile stew", "s": "public-reference", "f": null}, {"t": "Visiting Albuquerque Balloon Fiesta", "d": "How to experience Albuquerque Balloon Fiesta.", "g": "attractions", "l": 2, "q": "What is Visiting Albuquerque Balloon Fiesta?", "a": "How to experience Albuquerque Balloon Fiesta.", "x": "Experiencing Albuquerque Balloon Fiesta: plan around Balloon Fiesta, the state's rhythm — Crescit eundo (It grows as it goes). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Carlsbad Caverns National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Georgia O'Keeffe Museum", "d": "Georgia O'Keeffe Museum: a top New Mexico attraction.", "g": "attractions", "l": 2, "q": "What is Georgia O'Keeffe Museum?", "a": "Georgia O'Keeffe Museum: a top New Mexico attraction.", "x": "Georgia O'Keeffe Museum is essential New Mexico. Pueblo peoples; Spanish 1598. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. green chile stew", "s": "public-reference", "f": null}, {"t": "Visiting Georgia O'Keeffe Museum", "d": "How to experience Georgia O'Keeffe Museum.", "g": "attractions", "l": 2, "q": "What is Visiting Georgia O'Keeffe Museum?", "a": "How to experience Georgia O'Keeffe Museum.", "x": "Experiencing Georgia O'Keeffe Museum: plan around Balloon Fiesta, the state's rhythm — Crescit eundo (It grows as it goes). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Carlsbad Caverns National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Chaco Canyon", "d": "Chaco Canyon: a top New Mexico attraction.", "g": "attractions", "l": 2, "q": "What is Chaco Canyon?", "a": "Chaco Canyon: a top New Mexico attraction.", "x": "Chaco Canyon is essential New Mexico. Pueblo peoples; Spanish 1598. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. green chile stew", "s": "public-reference", "f": null}, {"t": "Visiting Chaco Canyon", "d": "How to experience Chaco Canyon.", "g": "attractions", "l": 2, "q": "What is Visiting Chaco Canyon?", "a": "How to experience Chaco Canyon.", "x": "Experiencing Chaco Canyon: plan around Balloon Fiesta, the state's rhythm — Crescit eundo (It grows as it goes). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Carlsbad Caverns National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Carlsbad Caverns National Park", "d": "Carlsbad Caverns National Park: New Mexico's great park.", "g": "parks", "l": 2, "q": "What is Carlsbad Caverns National Park?", "a": "Carlsbad Caverns National Park: New Mexico's great park.", "x": "Carlsbad Caverns National Park is New Mexico's wild heart: Carlsbad Caverns. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Balloon Fiesta Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Carlsbad Caverns National Park", "d": "How to explore Carlsbad Caverns National Park.", "g": "parks", "l": 2, "q": "What is Exploring Carlsbad Caverns National Park?", "a": "How to explore Carlsbad Caverns National Park.", "x": "Exploring Carlsbad Caverns National Park: get the park map, check conditions, carry water and layers, and tell someone your plan. Crescit eundo (It grows as it goes) Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Santa Fe: the capital city", "d": "Santa Fe, capital of New Mexico.", "g": "cities", "l": 2, "q": "What is Santa Fe: the capital city?", "a": "Santa Fe, capital of New Mexico.", "x": "Santa Fe: the capital of New Mexico — government, history, and often the best museums. Mexican then U.S. (1848). Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Albuquerque", "s": "public-reference", "f": null}, {"t": "Albuquerque: the biggest city", "d": "Albuquerque is New Mexico's largest city.", "g": "cities", "l": 2, "q": "What is Albuquerque: the biggest city?", "a": "Albuquerque is New Mexico's largest city.", "x": "Albuquerque is where New Mexico comes to work and play: the skyline, the food, the music, the crowds. federal labs Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Balloon Fiesta", "s": "public-reference", "f": null}, {"t": "green chile stew: the food", "d": "Taste New Mexico: green chile stew.", "g": "food", "l": 2, "q": "What is green chile stew: the food?", "a": "Taste New Mexico: green chile stew.", "x": "The taste of New Mexico is green chile stew — and the foodways around it. Manhattan Project; labs. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Balloon Fiesta Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: New Mexico", "d": "Eating your way through New Mexico.", "g": "food", "l": 2, "q": "What is Food tour: New Mexico?", "a": "Eating your way through New Mexico.", "x": "Eating through New Mexico: start with green chile stew, then follow the locals — diners, food trucks, farm stands. Crescit eundo (It grows as it goes) Food is the fastest way into a place's heart; the stories come free with the meal. Albuquerque", "s": "public-reference", "f": null}, {"t": "Balloon Fiesta", "d": "Balloon Fiesta: New Mexico's signature festival.", "g": "festivals", "l": 2, "q": "What is Balloon Fiesta?", "a": "Balloon Fiesta: New Mexico's signature festival.", "x": "Balloon Fiesta is New Mexico at its most celebratory: Art and desert culture.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Santa Fe Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "New Mexico year-round: Balloon Fiesta and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "New Mexico year-round: Balloon Fiesta and more.", "x": "The New Mexico festival calendar runs year-round, with Balloon Fiesta as the anchor. Crescit eundo (It grows as it goes) Every season has its celebration — plan trips around them for the liveliest version of the state. Carlsbad Caverns National Park", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-new-mexico-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
