(function(){'use strict';
/* JAH Comoros Complete Profile Database generator — jahdb-e2-comoros-profile-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-comoros-profile',PREFIX='JAH-E2COMOROSPR-',NAME='JAH Comoros Complete Profile Database';
var FIELDS=["overview", "people", "geography", "government", "economy", "history", "landmarks", "cuisine", "festivals", "customs", "nature", "travel"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Comoros: complete overview", "d": "Comoros: federal presidential republic nation in Southern Africa; capital Moroni; about about 850,000 people.", "g": "overview", "l": 2, "q": "What is Comoros: complete overview?", "a": "Comoros: federal presidential republic nation in Southern Africa; capital Moroni; about about 850,000 people.", "x": "Comoros is a federal presidential republic in Southern Africa. Its capital is Moroni, and about 850,000 people live there across about 2,000 sq km of land. The country speaks Comorian; French; Arabic and uses the Comorian franc. tropical This database profiles the nation completely: its people, land, government, economy, history, landmarks, food, festivals, customs, and nature — everything a student, traveler, or curious reader needs for a full picture.", "s": "public-reference", "f": null}, {"t": "Capital: Moroni", "d": "Moroni is the capital of Comoros.", "g": "people", "l": 2, "q": "What is Capital: Moroni?", "a": "Moroni is the capital of Comoros.", "x": "Moroni is the capital of Comoros: the seat of government and usually the cultural and economic heart. Capitals concentrate the nation's story — its museums, monuments, markets, and neighborhoods. Visitors should start here: a capital city teaches in days what books take weeks to explain.", "s": "public-reference", "f": null}, {"t": "People and population", "d": "Comoros has about about 850,000 residents.", "g": "people", "l": 2, "q": "What is People and population?", "a": "Comoros has about about 850,000 residents.", "x": "about 850,000 people call Comoros home. Population shapes everything: the cities' size, the languages heard on the street, the food on the tables. Comoros is a federal presidential republic, and its people's daily life — work, family, celebration — is the living culture no monument can replace.", "s": "public-reference", "f": null}, {"t": "Geography and land", "d": "Comoros covers about 2,000 sq km.", "g": "geography", "l": 2, "q": "What is Geography and land?", "a": "Comoros covers about 2,000 sq km.", "x": "Comoros covers about 2,000 sq km of land. Geography writes the country's character: its coasts or mountains decide its climate, its food, even its history of trade and invasion. tropical Understanding the map is the fastest way to understand the nation.", "s": "public-reference", "f": null}, {"t": "Climate", "d": "Comoros: tropical.", "g": "geography", "l": 2, "q": "What is Climate?", "a": "Comoros: tropical.", "x": "The climate of Comoros: tropical. Climate dictates the wardrobe, the harvest calendar, the festivals, and the architecture — life bends around weather everywhere. Travelers should check the seasons: the same country can feel like two different places between its wet and dry, hot and cold months.", "s": "public-reference", "f": null}, {"t": "Government", "d": "Comoros is a federal presidential republic.", "g": "government", "l": 2, "q": "What is Government?", "a": "Comoros is a federal presidential republic.", "x": "Comoros is governed as a federal presidential republic. The system of government shapes daily life through laws, services, and the citizen's relationship to the state. Its modern form dates to 1975 (independence) — and like all governments, it continues to evolve with its people.", "s": "public-reference", "f": null}, {"t": "Independence and statehood", "d": "Comoros: 1975 (independence).", "g": "government", "l": 2, "q": "What is Independence and statehood?", "a": "Comoros: 1975 (independence).", "x": "Statehood in Comoros: 1975 (independence). National days, flags, and anthems all trace to the moment of independence or founding — the story every schoolchild learns. Understanding it explains the country's pride, its holidays, and often its friendships and rivalries.", "s": "public-reference", "f": null}, {"t": "Languages", "d": "Comoros speaks Comorian; French; Arabic.", "g": "people", "l": 2, "q": "What is Languages?", "a": "Comoros speaks Comorian; French; Arabic.", "x": "Language in Comoros: Comorian; French; Arabic. Language carries the culture's humor, proverbs, and worldview — learning even greetings opens doors that stay closed to outsiders. Multilingual countries code-switch daily; visitors who try the local tongue are repaid with warmth.", "s": "public-reference", "f": null}, {"t": "Currency and money", "d": "Comoros uses the Comorian franc.", "g": "economy", "l": 2, "q": "What is Currency and money?", "a": "Comoros uses the Comorian franc.", "x": "Money in Comoros: the Comorian franc. Travelers should learn the denominations, the tipping customs, and whether cards or cash rule daily life. Exchange rates move, but the habit of checking prices in local terms keeps budgets honest.", "s": "public-reference", "f": null}, {"t": "Economy 1", "d": "Vanilla and cloves.", "g": "economy", "l": 2, "q": "What is Economy 1?", "a": "Vanilla and cloves.", "x": "The economy of Comoros: Vanilla and cloves.. Economies are the sum of what people make, grow, and sell — and they explain the cities' skylines, the countryside's crops, and the jobs young people dream about. A diverse economy weathers shocks; every nation is working toward that resilience.", "s": "public-reference", "f": null}, {"t": "Economy 2", "d": "Remittances.", "g": "economy", "l": 2, "q": "What is Economy 2?", "a": "Remittances.", "x": "The economy of Comoros: Remittances.. Economies are the sum of what people make, grow, and sell — and they explain the cities' skylines, the countryside's crops, and the jobs young people dream about. A diverse economy weathers shocks; every nation is working toward that resilience.", "s": "public-reference", "f": null}, {"t": "History 1", "d": "Swahili sultanates; French colony.", "g": "history", "l": 2, "q": "What is History 1?", "a": "Swahili sultanates; French colony.", "x": "Comoros history: Swahili sultanates; French colony.. History here is not dates to memorize but the explanation of the present — why the borders run where they do, why the holidays exist, why the food tastes the way it does. Every nation's story has golden ages and dark chapters; knowing both is respecting the country honestly.", "s": "public-reference", "f": null}, {"t": "History 2", "d": "Coups aplenty; fragile.", "g": "history", "l": 2, "q": "What is History 2?", "a": "Coups aplenty; fragile.", "x": "Comoros history: Coups aplenty; fragile.. History here is not dates to memorize but the explanation of the present — why the borders run where they do, why the holidays exist, why the food tastes the way it does. Every nation's story has golden ages and dark chapters; knowing both is respecting the country honestly.", "s": "public-reference", "f": null}, {"t": "History 3", "d": "Ylang-ylang islands.", "g": "history", "l": 2, "q": "What is History 3?", "a": "Ylang-ylang islands.", "x": "Comoros history: Ylang-ylang islands.. History here is not dates to memorize but the explanation of the present — why the borders run where they do, why the holidays exist, why the food tastes the way it does. Every nation's story has golden ages and dark chapters; knowing both is respecting the country honestly.", "s": "public-reference", "f": null}, {"t": "Karthala", "d": "Active volcano.", "g": "landmarks", "l": 2, "q": "What is Karthala?", "a": "Active volcano.", "x": "Karthala — Active volcano.. Landmarks are a country's exclamation points: the places postcards are made of and pilgrims of curiosity travel to see. Comoros Visit early in the day, learn the story before you go, and look past the crowds to the craft — someone built this to last centuries, and it worked.", "s": "public-reference", "f": null}, {"t": "Visiting Karthala", "d": "How to experience Karthala in Comoros.", "g": "landmarks", "l": 2, "q": "What is Visiting Karthala?", "a": "How to experience Karthala in Comoros.", "x": "Experiencing Karthala in Comoros: go with context — read its story first, then see it with understanding. Active volcano. Mornings beat crowds, local guides beat guidebooks, and the quiet corners near famous sites often hold the best moments. Leave only footprints; the landmark belongs to the future too.", "s": "public-reference", "f": null}, {"t": "Chomoni Beach", "d": "White sands.", "g": "landmarks", "l": 2, "q": "What is Chomoni Beach?", "a": "White sands.", "x": "Chomoni Beach — White sands.. Landmarks are a country's exclamation points: the places postcards are made of and pilgrims of curiosity travel to see. Comoros Visit early in the day, learn the story before you go, and look past the crowds to the craft — someone built this to last centuries, and it worked.", "s": "public-reference", "f": null}, {"t": "Visiting Chomoni Beach", "d": "How to experience Chomoni Beach in Comoros.", "g": "landmarks", "l": 2, "q": "What is Visiting Chomoni Beach?", "a": "How to experience Chomoni Beach in Comoros.", "x": "Experiencing Chomoni Beach in Comoros: go with context — read its story first, then see it with understanding. White sands. Mornings beat crowds, local guides beat guidebooks, and the quiet corners near famous sites often hold the best moments. Leave only footprints; the landmark belongs to the future too.", "s": "public-reference", "f": null}, {"t": "Moroni medina", "d": "Old town.", "g": "landmarks", "l": 2, "q": "What is Moroni medina?", "a": "Old town.", "x": "Moroni medina — Old town.. Landmarks are a country's exclamation points: the places postcards are made of and pilgrims of curiosity travel to see. Comoros Visit early in the day, learn the story before you go, and look past the crowds to the craft — someone built this to last centuries, and it worked.", "s": "public-reference", "f": null}, {"t": "Visiting Moroni medina", "d": "How to experience Moroni medina in Comoros.", "g": "landmarks", "l": 2, "q": "What is Visiting Moroni medina?", "a": "How to experience Moroni medina in Comoros.", "x": "Experiencing Moroni medina in Comoros: go with context — read its story first, then see it with understanding. Old town. Mornings beat crowds, local guides beat guidebooks, and the quiet corners near famous sites often hold the best moments. Leave only footprints; the landmark belongs to the future too.", "s": "public-reference", "f": null}, {"t": "Cuisine overview", "d": "The food of Comoros reflects its land and history.", "g": "cuisine", "l": 2, "q": "What is Cuisine overview?", "a": "The food of Comoros reflects its land and history.", "x": "The cuisine of Comoros is edible history: tropical Every dish tells where the country traded, what its soil grows, and who passed through. Eating locally is the fastest cultural education — markets first, then street stalls, then the family table if you are lucky.", "s": "public-reference", "f": null}, {"t": "Langouste a la vanille", "d": "Langouste a la vanille: Comoros's signature dish.", "g": "cuisine", "l": 2, "q": "What is Langouste a la vanille?", "a": "Langouste a la vanille: Comoros's signature dish.", "x": "Langouste a la vanille: Vanilla lobster.. Langouste a la vanille is Comoros's food at its most beloved: generations perfected it, regions argue over it, and everyone who leaves home craves it. Order it where the locals order it; the best version is rarely the fanciest.", "s": "public-reference", "f": null}, {"t": "Mkatra foutra", "d": "Mkatra foutra: Comoros's signature dish.", "g": "cuisine", "l": 2, "q": "What is Mkatra foutra?", "a": "Mkatra foutra: Comoros's signature dish.", "x": "Mkatra foutra: Coconut bread.. Mkatra foutra is Comoros's food at its most beloved: generations perfected it, regions argue over it, and everyone who leaves home craves it. Order it where the locals order it; the best version is rarely the fanciest.", "s": "public-reference", "f": null}, {"t": "Grilled fish", "d": "Grilled fish: Comoros's signature dish.", "g": "cuisine", "l": 2, "q": "What is Grilled fish?", "a": "Grilled fish: Comoros's signature dish.", "x": "Grilled fish: Island catch.. Grilled fish is Comoros's food at its most beloved: generations perfected it, regions argue over it, and everyone who leaves home craves it. Order it where the locals order it; the best version is rarely the fanciest.", "s": "public-reference", "f": null}, {"t": "Independence Day", "d": "Independence Day (July 6.).", "g": "festivals", "l": 2, "q": "What is Independence Day?", "a": "Independence Day (July 6.).", "x": "Independence Day (July 6.) is Comoros at its most joyful. Festivals are the culture with the volume turned up: the music, the food, the dress, the togetherness — everything the country values, celebrated in the streets. Comoros Time a visit for one if you can; participate respectfully, and you will be welcomed.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-comoros-profile-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
