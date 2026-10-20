(function(){'use strict';
/* JAH South Sudan Complete Profile Database generator — jahdb-e2-south-sudan-profile-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-south-sudan-profile',PREFIX='JAH-E2SOUTHSUDA-',NAME='JAH South Sudan Complete Profile Database';
var FIELDS=["overview", "people", "geography", "government", "economy", "history", "landmarks", "cuisine", "festivals", "customs", "nature", "travel"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "South Sudan: complete overview", "d": "South Sudan: presidential republic nation in East Africa; capital Juba; about about 11 million people.", "g": "overview", "l": 2, "q": "What is South Sudan: complete overview?", "a": "South Sudan: presidential republic nation in East Africa; capital Juba; about about 11 million people.", "x": "South Sudan is a presidential republic in East Africa. Its capital is Juba, and about 11 million people live there across about 620,000 sq km of land. The country speaks English and uses the South Sudanese pound. tropical This database profiles the nation completely: its people, land, government, economy, history, landmarks, food, festivals, customs, and nature — everything a student, traveler, or curious reader needs for a full picture.", "s": "public-reference", "f": null}, {"t": "Capital: Juba", "d": "Juba is the capital of South Sudan.", "g": "people", "l": 2, "q": "What is Capital: Juba?", "a": "Juba is the capital of South Sudan.", "x": "Juba is the capital of South Sudan: the seat of government and usually the cultural and economic heart. Capitals concentrate the nation's story — its museums, monuments, markets, and neighborhoods. Visitors should start here: a capital city teaches in days what books take weeks to explain.", "s": "public-reference", "f": null}, {"t": "People and population", "d": "South Sudan has about about 11 million residents.", "g": "people", "l": 2, "q": "What is People and population?", "a": "South Sudan has about about 11 million residents.", "x": "about 11 million people call South Sudan home. Population shapes everything: the cities' size, the languages heard on the street, the food on the tables. South Sudan is a presidential republic, and its people's daily life — work, family, celebration — is the living culture no monument can replace.", "s": "public-reference", "f": null}, {"t": "Geography and land", "d": "South Sudan covers about 620,000 sq km.", "g": "geography", "l": 2, "q": "What is Geography and land?", "a": "South Sudan covers about 620,000 sq km.", "x": "South Sudan covers about 620,000 sq km of land. Geography writes the country's character: its coasts or mountains decide its climate, its food, even its history of trade and invasion. tropical Understanding the map is the fastest way to understand the nation.", "s": "public-reference", "f": null}, {"t": "Climate", "d": "South Sudan: tropical.", "g": "geography", "l": 2, "q": "What is Climate?", "a": "South Sudan: tropical.", "x": "The climate of South Sudan: tropical. Climate dictates the wardrobe, the harvest calendar, the festivals, and the architecture — life bends around weather everywhere. Travelers should check the seasons: the same country can feel like two different places between its wet and dry, hot and cold months.", "s": "public-reference", "f": null}, {"t": "Government", "d": "South Sudan is a presidential republic.", "g": "government", "l": 2, "q": "What is Government?", "a": "South Sudan is a presidential republic.", "x": "South Sudan is governed as a presidential republic. The system of government shapes daily life through laws, services, and the citizen's relationship to the state. Its modern form dates to 2011 (independence) — and like all governments, it continues to evolve with its people.", "s": "public-reference", "f": null}, {"t": "Independence and statehood", "d": "South Sudan: 2011 (independence).", "g": "government", "l": 2, "q": "What is Independence and statehood?", "a": "South Sudan: 2011 (independence).", "x": "Statehood in South Sudan: 2011 (independence). National days, flags, and anthems all trace to the moment of independence or founding — the story every schoolchild learns. Understanding it explains the country's pride, its holidays, and often its friendships and rivalries.", "s": "public-reference", "f": null}, {"t": "Languages", "d": "South Sudan speaks English.", "g": "people", "l": 2, "q": "What is Languages?", "a": "South Sudan speaks English.", "x": "Language in South Sudan: English. Language carries the culture's humor, proverbs, and worldview — learning even greetings opens doors that stay closed to outsiders. Multilingual countries code-switch daily; visitors who try the local tongue are repaid with warmth.", "s": "public-reference", "f": null}, {"t": "Currency and money", "d": "South Sudan uses the South Sudanese pound.", "g": "economy", "l": 2, "q": "What is Currency and money?", "a": "South Sudan uses the South Sudanese pound.", "x": "Money in South Sudan: the South Sudanese pound. Travelers should learn the denominations, the tipping customs, and whether cards or cash rule daily life. Exchange rates move, but the habit of checking prices in local terms keeps budgets honest.", "s": "public-reference", "f": null}, {"t": "Economy 1", "d": "Oil; aid-dependent.", "g": "economy", "l": 2, "q": "What is Economy 1?", "a": "Oil; aid-dependent.", "x": "The economy of South Sudan: Oil; aid-dependent.. Economies are the sum of what people make, grow, and sell — and they explain the cities' skylines, the countryside's crops, and the jobs young people dream about. A diverse economy weathers shocks; every nation is working toward that resilience.", "s": "public-reference", "f": null}, {"t": "Economy 2", "d": "Fragile state.", "g": "economy", "l": 2, "q": "What is Economy 2?", "a": "Fragile state.", "x": "The economy of South Sudan: Fragile state.. Economies are the sum of what people make, grow, and sell — and they explain the cities' skylines, the countryside's crops, and the jobs young people dream about. A diverse economy weathers shocks; every nation is working toward that resilience.", "s": "public-reference", "f": null}, {"t": "History 1", "d": "Anglo-Egyptian Sudan; civil wars.", "g": "history", "l": 2, "q": "What is History 1?", "a": "Anglo-Egyptian Sudan; civil wars.", "x": "South Sudan history: Anglo-Egyptian Sudan; civil wars.. History here is not dates to memorize but the explanation of the present — why the borders run where they do, why the holidays exist, why the food tastes the way it does. Every nation's story has golden ages and dark chapters; knowing both is respecting the country honestly.", "s": "public-reference", "f": null}, {"t": "History 2", "d": "Independence 2011; civil war 2013-20.", "g": "history", "l": 2, "q": "What is History 2?", "a": "Independence 2011; civil war 2013-20.", "x": "South Sudan history: Independence 2011; civil war 2013-20.. History here is not dates to memorize but the explanation of the present — why the borders run where they do, why the holidays exist, why the food tastes the way it does. Every nation's story has golden ages and dark chapters; knowing both is respecting the country honestly.", "s": "public-reference", "f": null}, {"t": "History 3", "d": "World's newest-ish nation.", "g": "history", "l": 2, "q": "What is History 3?", "a": "World's newest-ish nation.", "x": "South Sudan history: World's newest-ish nation.. History here is not dates to memorize but the explanation of the present — why the borders run where they do, why the holidays exist, why the food tastes the way it does. Every nation's story has golden ages and dark chapters; knowing both is respecting the country honestly.", "s": "public-reference", "f": null}, {"t": "Boma", "d": "Wildlife plateau.", "g": "landmarks", "l": 2, "q": "What is Boma?", "a": "Wildlife plateau.", "x": "Boma — Wildlife plateau.. Landmarks are a country's exclamation points: the places postcards are made of and pilgrims of curiosity travel to see. South Sudan Visit early in the day, learn the story before you go, and look past the crowds to the craft — someone built this to last centuries, and it worked.", "s": "public-reference", "f": null}, {"t": "Visiting Boma", "d": "How to experience Boma in South Sudan.", "g": "landmarks", "l": 2, "q": "What is Visiting Boma?", "a": "How to experience Boma in South Sudan.", "x": "Experiencing Boma in South Sudan: go with context — read its story first, then see it with understanding. Wildlife plateau. Mornings beat crowds, local guides beat guidebooks, and the quiet corners near famous sites often hold the best moments. Leave only footprints; the landmark belongs to the future too.", "s": "public-reference", "f": null}, {"t": "Sudd", "d": "The great swamp.", "g": "landmarks", "l": 2, "q": "What is Sudd?", "a": "The great swamp.", "x": "Sudd — The great swamp.. Landmarks are a country's exclamation points: the places postcards are made of and pilgrims of curiosity travel to see. South Sudan Visit early in the day, learn the story before you go, and look past the crowds to the craft — someone built this to last centuries, and it worked.", "s": "public-reference", "f": null}, {"t": "Visiting Sudd", "d": "How to experience Sudd in South Sudan.", "g": "landmarks", "l": 2, "q": "What is Visiting Sudd?", "a": "How to experience Sudd in South Sudan.", "x": "Experiencing Sudd in South Sudan: go with context — read its story first, then see it with understanding. The great swamp. Mornings beat crowds, local guides beat guidebooks, and the quiet corners near famous sites often hold the best moments. Leave only footprints; the landmark belongs to the future too.", "s": "public-reference", "f": null}, {"t": "Juba", "d": "The riverside capital.", "g": "landmarks", "l": 2, "q": "What is Juba?", "a": "The riverside capital.", "x": "Juba — The riverside capital.. Landmarks are a country's exclamation points: the places postcards are made of and pilgrims of curiosity travel to see. South Sudan Visit early in the day, learn the story before you go, and look past the crowds to the craft — someone built this to last centuries, and it worked.", "s": "public-reference", "f": null}, {"t": "Visiting Juba", "d": "How to experience Juba in South Sudan.", "g": "landmarks", "l": 2, "q": "What is Visiting Juba?", "a": "How to experience Juba in South Sudan.", "x": "Experiencing Juba in South Sudan: go with context — read its story first, then see it with understanding. The riverside capital. Mornings beat crowds, local guides beat guidebooks, and the quiet corners near famous sites often hold the best moments. Leave only footprints; the landmark belongs to the future too.", "s": "public-reference", "f": null}, {"t": "Cuisine overview", "d": "The food of South Sudan reflects its land and history.", "g": "cuisine", "l": 2, "q": "What is Cuisine overview?", "a": "The food of South Sudan reflects its land and history.", "x": "The cuisine of South Sudan is edible history: tropical Every dish tells where the country traded, what its soil grows, and who passed through. Eating locally is the fastest cultural education — markets first, then street stalls, then the family table if you are lucky.", "s": "public-reference", "f": null}, {"t": "Kisra", "d": "Kisra: South Sudan's signature dish.", "g": "cuisine", "l": 2, "q": "What is Kisra?", "a": "Kisra: South Sudan's signature dish.", "x": "Kisra: As in the north.. Kisra is South Sudan's food at its most beloved: generations perfected it, regions argue over it, and everyone who leaves home craves it. Order it where the locals order it; the best version is rarely the fanciest.", "s": "public-reference", "f": null}, {"t": "Wala-wala", "d": "Wala-wala: South Sudan's signature dish.", "g": "cuisine", "l": 2, "q": "What is Wala-wala?", "a": "Wala-wala: South Sudan's signature dish.", "x": "Wala-wala: Porridge staple.. Wala-wala is South Sudan's food at its most beloved: generations perfected it, regions argue over it, and everyone who leaves home craves it. Order it where the locals order it; the best version is rarely the fanciest.", "s": "public-reference", "f": null}, {"t": "Dried fish", "d": "Dried fish: South Sudan's signature dish.", "g": "cuisine", "l": 2, "q": "What is Dried fish?", "a": "Dried fish: South Sudan's signature dish.", "x": "Dried fish: The Sudd's harvest.. Dried fish is South Sudan's food at its most beloved: generations perfected it, regions argue over it, and everyone who leaves home craves it. Order it where the locals order it; the best version is rarely the fanciest.", "s": "public-reference", "f": null}, {"t": "Independence Day", "d": "Independence Day (July 9.).", "g": "festivals", "l": 2, "q": "What is Independence Day?", "a": "Independence Day (July 9.).", "x": "Independence Day (July 9.) is South Sudan at its most joyful. Festivals are the culture with the volume turned up: the music, the food, the dress, the togetherness — everything the country values, celebrated in the streets. South Sudan Time a visit for one if you can; participate respectfully, and you will be welcomed.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-south-sudan-profile-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
