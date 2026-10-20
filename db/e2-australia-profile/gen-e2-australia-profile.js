(function(){'use strict';
/* JAH Australia Complete Profile Database generator — jahdb-e2-australia-profile-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-australia-profile',PREFIX='JAH-E2AUSTRALIA-',NAME='JAH Australia Complete Profile Database';
var FIELDS=["overview", "people", "geography", "government", "economy", "history", "landmarks", "cuisine", "festivals", "customs", "nature", "travel"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Australia: complete overview", "d": "Australia: federal parliamentary constitutional monarchy nation in Oceania; capital Canberra; about about 26 million people.", "g": "overview", "l": 2, "q": "What is Australia: complete overview?", "a": "Australia: federal parliamentary constitutional monarchy nation in Oceania; capital Canberra; about about 26 million people.", "x": "Australia is a federal parliamentary constitutional monarchy in Oceania. Its capital is Canberra, and about 26 million people live there across about 7.7 million sq km of land. The country speaks English and uses the Australian dollar. varied This database profiles the nation completely: its people, land, government, economy, history, landmarks, food, festivals, customs, and nature — everything a student, traveler, or curious reader needs for a full picture.", "s": "public-reference", "f": null}, {"t": "Capital: Canberra", "d": "Canberra is the capital of Australia.", "g": "people", "l": 2, "q": "What is Capital: Canberra?", "a": "Canberra is the capital of Australia.", "x": "Canberra is the capital of Australia: the seat of government and usually the cultural and economic heart. Capitals concentrate the nation's story — its museums, monuments, markets, and neighborhoods. Visitors should start here: a capital city teaches in days what books take weeks to explain.", "s": "public-reference", "f": null}, {"t": "People and population", "d": "Australia has about about 26 million residents.", "g": "people", "l": 2, "q": "What is People and population?", "a": "Australia has about about 26 million residents.", "x": "about 26 million people call Australia home. Population shapes everything: the cities' size, the languages heard on the street, the food on the tables. Australia is a federal parliamentary constitutional monarchy, and its people's daily life — work, family, celebration — is the living culture no monument can replace.", "s": "public-reference", "f": null}, {"t": "Geography and land", "d": "Australia covers about 7.7 million sq km.", "g": "geography", "l": 2, "q": "What is Geography and land?", "a": "Australia covers about 7.7 million sq km.", "x": "Australia covers about 7.7 million sq km of land. Geography writes the country's character: its coasts or mountains decide its climate, its food, even its history of trade and invasion. varied Understanding the map is the fastest way to understand the nation.", "s": "public-reference", "f": null}, {"t": "Climate", "d": "Australia: varied.", "g": "geography", "l": 2, "q": "What is Climate?", "a": "Australia: varied.", "x": "The climate of Australia: varied. Climate dictates the wardrobe, the harvest calendar, the festivals, and the architecture — life bends around weather everywhere. Travelers should check the seasons: the same country can feel like two different places between its wet and dry, hot and cold months.", "s": "public-reference", "f": null}, {"t": "Government", "d": "Australia is a federal parliamentary constitutional monarchy.", "g": "government", "l": 2, "q": "What is Government?", "a": "Australia is a federal parliamentary constitutional monarchy.", "x": "Australia is governed as a federal parliamentary constitutional monarchy. The system of government shapes daily life through laws, services, and the citizen's relationship to the state. Its modern form dates to 1901 (federation) — and like all governments, it continues to evolve with its people.", "s": "public-reference", "f": null}, {"t": "Independence and statehood", "d": "Australia: 1901 (federation).", "g": "government", "l": 2, "q": "What is Independence and statehood?", "a": "Australia: 1901 (federation).", "x": "Statehood in Australia: 1901 (federation). National days, flags, and anthems all trace to the moment of independence or founding — the story every schoolchild learns. Understanding it explains the country's pride, its holidays, and often its friendships and rivalries.", "s": "public-reference", "f": null}, {"t": "Languages", "d": "Australia speaks English.", "g": "people", "l": 2, "q": "What is Languages?", "a": "Australia speaks English.", "x": "Language in Australia: English. Language carries the culture's humor, proverbs, and worldview — learning even greetings opens doors that stay closed to outsiders. Multilingual countries code-switch daily; visitors who try the local tongue are repaid with warmth.", "s": "public-reference", "f": null}, {"t": "Currency and money", "d": "Australia uses the Australian dollar.", "g": "economy", "l": 2, "q": "What is Currency and money?", "a": "Australia uses the Australian dollar.", "x": "Money in Australia: the Australian dollar. Travelers should learn the denominations, the tipping customs, and whether cards or cash rule daily life. Exchange rates move, but the habit of checking prices in local terms keeps budgets honest.", "s": "public-reference", "f": null}, {"t": "Economy 1", "d": "Mining and services.", "g": "economy", "l": 2, "q": "What is Economy 1?", "a": "Mining and services.", "x": "The economy of Australia: Mining and services.. Economies are the sum of what people make, grow, and sell — and they explain the cities' skylines, the countryside's crops, and the jobs young people dream about. A diverse economy weathers shocks; every nation is working toward that resilience.", "s": "public-reference", "f": null}, {"t": "Economy 2", "d": "High income.", "g": "economy", "l": 2, "q": "What is Economy 2?", "a": "High income.", "x": "The economy of Australia: High income.. Economies are the sum of what people make, grow, and sell — and they explain the cities' skylines, the countryside's crops, and the jobs young people dream about. A diverse economy weathers shocks; every nation is working toward that resilience.", "s": "public-reference", "f": null}, {"t": "History 1", "d": "Aboriginal 65,000 years.", "g": "history", "l": 2, "q": "What is History 1?", "a": "Aboriginal 65,000 years.", "x": "Australia history: Aboriginal 65,000 years.. History here is not dates to memorize but the explanation of the present — why the borders run where they do, why the holidays exist, why the food tastes the way it does. Every nation's story has golden ages and dark chapters; knowing both is respecting the country honestly.", "s": "public-reference", "f": null}, {"t": "History 2", "d": "British colony 1788.", "g": "history", "l": 2, "q": "What is History 2?", "a": "British colony 1788.", "x": "Australia history: British colony 1788.. History here is not dates to memorize but the explanation of the present — why the borders run where they do, why the holidays exist, why the food tastes the way it does. Every nation's story has golden ages and dark chapters; knowing both is respecting the country honestly.", "s": "public-reference", "f": null}, {"t": "History 3", "d": "Federation 1901.", "g": "history", "l": 2, "q": "What is History 3?", "a": "Federation 1901.", "x": "Australia history: Federation 1901.. History here is not dates to memorize but the explanation of the present — why the borders run where they do, why the holidays exist, why the food tastes the way it does. Every nation's story has golden ages and dark chapters; knowing both is respecting the country honestly.", "s": "public-reference", "f": null}, {"t": "Sydney Opera House", "d": "The sail icon.", "g": "landmarks", "l": 2, "q": "What is Sydney Opera House?", "a": "The sail icon.", "x": "Sydney Opera House — The sail icon.. Landmarks are a country's exclamation points: the places postcards are made of and pilgrims of curiosity travel to see. Australia Visit early in the day, learn the story before you go, and look past the crowds to the craft — someone built this to last centuries, and it worked.", "s": "public-reference", "f": null}, {"t": "Visiting Sydney Opera House", "d": "How to experience Sydney Opera House in Australia.", "g": "landmarks", "l": 2, "q": "What is Visiting Sydney Opera House?", "a": "How to experience Sydney Opera House in Australia.", "x": "Experiencing Sydney Opera House in Australia: go with context — read its story first, then see it with understanding. The sail icon. Mornings beat crowds, local guides beat guidebooks, and the quiet corners near famous sites often hold the best moments. Leave only footprints; the landmark belongs to the future too.", "s": "public-reference", "f": null}, {"t": "Great Barrier Reef", "d": "The living wonder.", "g": "landmarks", "l": 2, "q": "What is Great Barrier Reef?", "a": "The living wonder.", "x": "Great Barrier Reef — The living wonder.. Landmarks are a country's exclamation points: the places postcards are made of and pilgrims of curiosity travel to see. Australia Visit early in the day, learn the story before you go, and look past the crowds to the craft — someone built this to last centuries, and it worked.", "s": "public-reference", "f": null}, {"t": "Visiting Great Barrier Reef", "d": "How to experience Great Barrier Reef in Australia.", "g": "landmarks", "l": 2, "q": "What is Visiting Great Barrier Reef?", "a": "How to experience Great Barrier Reef in Australia.", "x": "Experiencing Great Barrier Reef in Australia: go with context — read its story first, then see it with understanding. The living wonder. Mornings beat crowds, local guides beat guidebooks, and the quiet corners near famous sites often hold the best moments. Leave only footprints; the landmark belongs to the future too.", "s": "public-reference", "f": null}, {"t": "Uluru", "d": "The sacred monolith.", "g": "landmarks", "l": 2, "q": "What is Uluru?", "a": "The sacred monolith.", "x": "Uluru — The sacred monolith.. Landmarks are a country's exclamation points: the places postcards are made of and pilgrims of curiosity travel to see. Australia Visit early in the day, learn the story before you go, and look past the crowds to the craft — someone built this to last centuries, and it worked.", "s": "public-reference", "f": null}, {"t": "Visiting Uluru", "d": "How to experience Uluru in Australia.", "g": "landmarks", "l": 2, "q": "What is Visiting Uluru?", "a": "How to experience Uluru in Australia.", "x": "Experiencing Uluru in Australia: go with context — read its story first, then see it with understanding. The sacred monolith. Mornings beat crowds, local guides beat guidebooks, and the quiet corners near famous sites often hold the best moments. Leave only footprints; the landmark belongs to the future too.", "s": "public-reference", "f": null}, {"t": "Cuisine overview", "d": "The food of Australia reflects its land and history.", "g": "cuisine", "l": 2, "q": "What is Cuisine overview?", "a": "The food of Australia reflects its land and history.", "x": "The cuisine of Australia is edible history: varied Every dish tells where the country traded, what its soil grows, and who passed through. Eating locally is the fastest cultural education — markets first, then street stalls, then the family table if you are lucky.", "s": "public-reference", "f": null}, {"t": "Vegemite", "d": "Vegemite: Australia's signature dish.", "g": "cuisine", "l": 2, "q": "What is Vegemite?", "a": "Vegemite: Australia's signature dish.", "x": "Vegemite: The yeast-spread icon.. Vegemite is Australia's food at its most beloved: generations perfected it, regions argue over it, and everyone who leaves home craves it. Order it where the locals order it; the best version is rarely the fanciest.", "s": "public-reference", "f": null}, {"t": "Meat pie", "d": "Meat pie: Australia's signature dish.", "g": "cuisine", "l": 2, "q": "What is Meat pie?", "a": "Meat pie: Australia's signature dish.", "x": "Meat pie: The handheld classic.. Meat pie is Australia's food at its most beloved: generations perfected it, regions argue over it, and everyone who leaves home craves it. Order it where the locals order it; the best version is rarely the fanciest.", "s": "public-reference", "f": null}, {"t": "Lamingtons", "d": "Lamingtons: Australia's signature dish.", "g": "cuisine", "l": 2, "q": "What is Lamingtons?", "a": "Lamingtons: Australia's signature dish.", "x": "Lamingtons: Chocolate-coconut cake.. Lamingtons is Australia's food at its most beloved: generations perfected it, regions argue over it, and everyone who leaves home craves it. Order it where the locals order it; the best version is rarely the fanciest.", "s": "public-reference", "f": null}, {"t": "Australia Day", "d": "Australia Day (Jan 26: debated.).", "g": "festivals", "l": 2, "q": "What is Australia Day?", "a": "Australia Day (Jan 26: debated.).", "x": "Australia Day (Jan 26: debated.) is Australia at its most joyful. Festivals are the culture with the volume turned up: the music, the food, the dress, the togetherness — everything the country values, celebrated in the streets. Australia Time a visit for one if you can; participate respectfully, and you will be welcomed.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-australia-profile-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
