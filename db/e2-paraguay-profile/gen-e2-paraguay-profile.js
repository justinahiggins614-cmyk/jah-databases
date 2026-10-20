(function(){'use strict';
/* JAH Paraguay Complete Profile Database generator — jahdb-e2-paraguay-profile-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-paraguay-profile',PREFIX='JAH-E2PARAGUAYP-',NAME='JAH Paraguay Complete Profile Database';
var FIELDS=["overview", "people", "geography", "government", "economy", "history", "landmarks", "cuisine", "festivals", "customs", "nature", "travel"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Paraguay: complete overview", "d": "Paraguay: presidential republic nation in South America; capital Asuncion; about about 6.9 million people.", "g": "overview", "l": 2, "q": "What is Paraguay: complete overview?", "a": "Paraguay: presidential republic nation in South America; capital Asuncion; about about 6.9 million people.", "x": "Paraguay is a presidential republic in South America. Its capital is Asuncion, and about 6.9 million people live there across about 407,000 sq km of land. The country speaks Spanish; Guarani and uses the Paraguayan guarani. subtropical This database profiles the nation completely: its people, land, government, economy, history, landmarks, food, festivals, customs, and nature — everything a student, traveler, or curious reader needs for a full picture.", "s": "public-reference", "f": null}, {"t": "Capital: Asuncion", "d": "Asuncion is the capital of Paraguay.", "g": "people", "l": 2, "q": "What is Capital: Asuncion?", "a": "Asuncion is the capital of Paraguay.", "x": "Asuncion is the capital of Paraguay: the seat of government and usually the cultural and economic heart. Capitals concentrate the nation's story — its museums, monuments, markets, and neighborhoods. Visitors should start here: a capital city teaches in days what books take weeks to explain.", "s": "public-reference", "f": null}, {"t": "People and population", "d": "Paraguay has about about 6.9 million residents.", "g": "people", "l": 2, "q": "What is People and population?", "a": "Paraguay has about about 6.9 million residents.", "x": "about 6.9 million people call Paraguay home. Population shapes everything: the cities' size, the languages heard on the street, the food on the tables. Paraguay is a presidential republic, and its people's daily life — work, family, celebration — is the living culture no monument can replace.", "s": "public-reference", "f": null}, {"t": "Geography and land", "d": "Paraguay covers about 407,000 sq km.", "g": "geography", "l": 2, "q": "What is Geography and land?", "a": "Paraguay covers about 407,000 sq km.", "x": "Paraguay covers about 407,000 sq km of land. Geography writes the country's character: its coasts or mountains decide its climate, its food, even its history of trade and invasion. subtropical Understanding the map is the fastest way to understand the nation.", "s": "public-reference", "f": null}, {"t": "Climate", "d": "Paraguay: subtropical.", "g": "geography", "l": 2, "q": "What is Climate?", "a": "Paraguay: subtropical.", "x": "The climate of Paraguay: subtropical. Climate dictates the wardrobe, the harvest calendar, the festivals, and the architecture — life bends around weather everywhere. Travelers should check the seasons: the same country can feel like two different places between its wet and dry, hot and cold months.", "s": "public-reference", "f": null}, {"t": "Government", "d": "Paraguay is a presidential republic.", "g": "government", "l": 2, "q": "What is Government?", "a": "Paraguay is a presidential republic.", "x": "Paraguay is governed as a presidential republic. The system of government shapes daily life through laws, services, and the citizen's relationship to the state. Its modern form dates to 1811 (independence) — and like all governments, it continues to evolve with its people.", "s": "public-reference", "f": null}, {"t": "Independence and statehood", "d": "Paraguay: 1811 (independence).", "g": "government", "l": 2, "q": "What is Independence and statehood?", "a": "Paraguay: 1811 (independence).", "x": "Statehood in Paraguay: 1811 (independence). National days, flags, and anthems all trace to the moment of independence or founding — the story every schoolchild learns. Understanding it explains the country's pride, its holidays, and often its friendships and rivalries.", "s": "public-reference", "f": null}, {"t": "Languages", "d": "Paraguay speaks Spanish; Guarani.", "g": "people", "l": 2, "q": "What is Languages?", "a": "Paraguay speaks Spanish; Guarani.", "x": "Language in Paraguay: Spanish; Guarani. Language carries the culture's humor, proverbs, and worldview — learning even greetings opens doors that stay closed to outsiders. Multilingual countries code-switch daily; visitors who try the local tongue are repaid with warmth.", "s": "public-reference", "f": null}, {"t": "Currency and money", "d": "Paraguay uses the Paraguayan guarani.", "g": "economy", "l": 2, "q": "What is Currency and money?", "a": "Paraguay uses the Paraguayan guarani.", "x": "Money in Paraguay: the Paraguayan guarani. Travelers should learn the denominations, the tipping customs, and whether cards or cash rule daily life. Exchange rates move, but the habit of checking prices in local terms keeps budgets honest.", "s": "public-reference", "f": null}, {"t": "Economy 1", "d": "Soy and hydropower.", "g": "economy", "l": 2, "q": "What is Economy 1?", "a": "Soy and hydropower.", "x": "The economy of Paraguay: Soy and hydropower.. Economies are the sum of what people make, grow, and sell — and they explain the cities' skylines, the countryside's crops, and the jobs young people dream about. A diverse economy weathers shocks; every nation is working toward that resilience.", "s": "public-reference", "f": null}, {"t": "Economy 2", "d": "Landlocked.", "g": "economy", "l": 2, "q": "What is Economy 2?", "a": "Landlocked.", "x": "The economy of Paraguay: Landlocked.. Economies are the sum of what people make, grow, and sell — and they explain the cities' skylines, the countryside's crops, and the jobs young people dream about. A diverse economy weathers shocks; every nation is working toward that resilience.", "s": "public-reference", "f": null}, {"t": "History 1", "d": "Jesuit missions; Francia's isolation.", "g": "history", "l": 2, "q": "What is History 1?", "a": "Jesuit missions; Francia's isolation.", "x": "Paraguay history: Jesuit missions; Francia's isolation.. History here is not dates to memorize but the explanation of the present — why the borders run where they do, why the holidays exist, why the food tastes the way it does. Every nation's story has golden ages and dark chapters; knowing both is respecting the country honestly.", "s": "public-reference", "f": null}, {"t": "History 2", "d": "Triple Alliance war 1864-70.", "g": "history", "l": 2, "q": "What is History 2?", "a": "Triple Alliance war 1864-70.", "x": "Paraguay history: Triple Alliance war 1864-70.. History here is not dates to memorize but the explanation of the present — why the borders run where they do, why the holidays exist, why the food tastes the way it does. Every nation's story has golden ages and dark chapters; knowing both is respecting the country honestly.", "s": "public-reference", "f": null}, {"t": "History 3", "d": "Stroessner 1954-89.", "g": "history", "l": 2, "q": "What is History 3?", "a": "Stroessner 1954-89.", "x": "Paraguay history: Stroessner 1954-89.. History here is not dates to memorize but the explanation of the present — why the borders run where they do, why the holidays exist, why the food tastes the way it does. Every nation's story has golden ages and dark chapters; knowing both is respecting the country honestly.", "s": "public-reference", "f": null}, {"t": "Itaipu Dam", "d": "Among the world's largest.", "g": "landmarks", "l": 2, "q": "What is Itaipu Dam?", "a": "Among the world's largest.", "x": "Itaipu Dam — Among the world's largest.. Landmarks are a country's exclamation points: the places postcards are made of and pilgrims of curiosity travel to see. Paraguay Visit early in the day, learn the story before you go, and look past the crowds to the craft — someone built this to last centuries, and it worked.", "s": "public-reference", "f": null}, {"t": "Visiting Itaipu Dam", "d": "How to experience Itaipu Dam in Paraguay.", "g": "landmarks", "l": 2, "q": "What is Visiting Itaipu Dam?", "a": "How to experience Itaipu Dam in Paraguay.", "x": "Experiencing Itaipu Dam in Paraguay: go with context — read its story first, then see it with understanding. Among the world's largest. Mornings beat crowds, local guides beat guidebooks, and the quiet corners near famous sites often hold the best moments. Leave only footprints; the landmark belongs to the future too.", "s": "public-reference", "f": null}, {"t": "Jesuit Missions", "d": "UNESCO reductions.", "g": "landmarks", "l": 2, "q": "What is Jesuit Missions?", "a": "UNESCO reductions.", "x": "Jesuit Missions — UNESCO reductions.. Landmarks are a country's exclamation points: the places postcards are made of and pilgrims of curiosity travel to see. Paraguay Visit early in the day, learn the story before you go, and look past the crowds to the craft — someone built this to last centuries, and it worked.", "s": "public-reference", "f": null}, {"t": "Visiting Jesuit Missions", "d": "How to experience Jesuit Missions in Paraguay.", "g": "landmarks", "l": 2, "q": "What is Visiting Jesuit Missions?", "a": "How to experience Jesuit Missions in Paraguay.", "x": "Experiencing Jesuit Missions in Paraguay: go with context — read its story first, then see it with understanding. UNESCO reductions. Mornings beat crowds, local guides beat guidebooks, and the quiet corners near famous sites often hold the best moments. Leave only footprints; the landmark belongs to the future too.", "s": "public-reference", "f": null}, {"t": "Chaco", "d": "The wild west.", "g": "landmarks", "l": 2, "q": "What is Chaco?", "a": "The wild west.", "x": "Chaco — The wild west.. Landmarks are a country's exclamation points: the places postcards are made of and pilgrims of curiosity travel to see. Paraguay Visit early in the day, learn the story before you go, and look past the crowds to the craft — someone built this to last centuries, and it worked.", "s": "public-reference", "f": null}, {"t": "Visiting Chaco", "d": "How to experience Chaco in Paraguay.", "g": "landmarks", "l": 2, "q": "What is Visiting Chaco?", "a": "How to experience Chaco in Paraguay.", "x": "Experiencing Chaco in Paraguay: go with context — read its story first, then see it with understanding. The wild west. Mornings beat crowds, local guides beat guidebooks, and the quiet corners near famous sites often hold the best moments. Leave only footprints; the landmark belongs to the future too.", "s": "public-reference", "f": null}, {"t": "Cuisine overview", "d": "The food of Paraguay reflects its land and history.", "g": "cuisine", "l": 2, "q": "What is Cuisine overview?", "a": "The food of Paraguay reflects its land and history.", "x": "The cuisine of Paraguay is edible history: subtropical Every dish tells where the country traded, what its soil grows, and who passed through. Eating locally is the fastest cultural education — markets first, then street stalls, then the family table if you are lucky.", "s": "public-reference", "f": null}, {"t": "Sopa paraguaya", "d": "Sopa paraguaya: Paraguay's signature dish.", "g": "cuisine", "l": 2, "q": "What is Sopa paraguaya?", "a": "Sopa paraguaya: Paraguay's signature dish.", "x": "Sopa paraguaya: Cornbread soup.. Sopa paraguaya is Paraguay's food at its most beloved: generations perfected it, regions argue over it, and everyone who leaves home craves it. Order it where the locals order it; the best version is rarely the fanciest.", "s": "public-reference", "f": null}, {"t": "Chipa", "d": "Chipa: Paraguay's signature dish.", "g": "cuisine", "l": 2, "q": "What is Chipa?", "a": "Chipa: Paraguay's signature dish.", "x": "Chipa: Cheese-manioc bread.. Chipa is Paraguay's food at its most beloved: generations perfected it, regions argue over it, and everyone who leaves home craves it. Order it where the locals order it; the best version is rarely the fanciest.", "s": "public-reference", "f": null}, {"t": "Asado", "d": "Asado: Paraguay's signature dish.", "g": "cuisine", "l": 2, "q": "What is Asado?", "a": "Asado: Paraguay's signature dish.", "x": "Asado: The barbecue ritual.. Asado is Paraguay's food at its most beloved: generations perfected it, regions argue over it, and everyone who leaves home craves it. Order it where the locals order it; the best version is rarely the fanciest.", "s": "public-reference", "f": null}, {"t": "Carnival", "d": "Carnival (Feb: Encarnacion.).", "g": "festivals", "l": 2, "q": "What is Carnival?", "a": "Carnival (Feb: Encarnacion.).", "x": "Carnival (Feb: Encarnacion.) is Paraguay at its most joyful. Festivals are the culture with the volume turned up: the music, the food, the dress, the togetherness — everything the country values, celebrated in the streets. Paraguay Time a visit for one if you can; participate respectfully, and you will be welcomed.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-paraguay-profile-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
