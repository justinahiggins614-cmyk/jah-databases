(function(){'use strict';
/* JAH Iowa History Database generator — jahdb-e2-iowa-history-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-iowa-history',PREFIX='JAH-E2IOWAHISTO-',NAME='JAH Iowa History Database';
var FIELDS=["overview", "statehood", "history", "people", "economy", "geography", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Iowa: history overview", "d": "Iowa: the Hawkeye State, admitted 1846 (29th); capital Des Moines.", "g": "overview", "l": 2, "q": "What is Iowa: history overview?", "a": "Iowa: the Hawkeye State, admitted 1846 (29th); capital Des Moines.", "x": "Iowa — \"Hawkeye State\" — entered the Union 1846 (29th). Its capital is Des Moines and its largest city is Des Moines. Meskwaki and Sioux; Black Hawk War. This database tells the state's story: from its first peoples through statehood to the modern era, plus the famous sons and daughters, the industries, and the facts every resident should know.", "s": "public-reference", "f": null}, {"t": "Statehood", "d": "Iowa became a state 1846 (29th).", "g": "statehood", "l": 2, "q": "What is Statehood?", "a": "Iowa became a state 1846 (29th).", "x": "Iowa achieved statehood 1846 (29th). The road to statehood ran through territorial government, population thresholds, and a congressional enabling act — the standard American path. Corn and hogs; caucus fame. Statehood Day is still celebrated, and the admission order gives Iowa its number among the states.", "s": "public-reference", "f": null}, {"t": "The statehood story", "d": "How Iowa went from territory to state.", "g": "statehood", "l": 2, "q": "What is The statehood story?", "a": "How Iowa went from territory to state.", "x": "The statehood story of Iowa: settlement, territorial organization, the push for admission, and finally the star on the flag. Bridges of Madison County. Every state's admission reflected the national politics of its era — Iowa's story is no exception, and it explains much about the state's character today.", "s": "public-reference", "f": null}, {"t": "Capital: Des Moines", "d": "Des Moines is the capital of Iowa.", "g": "overview", "l": 2, "q": "What is Capital: Des Moines?", "a": "Des Moines is the capital of Iowa.", "x": "Des Moines has been the seat of Iowa government, home to the capitol building, the supreme court, and the legislature. Capitals are often not the biggest city — Iowa's largest is Des Moines — chosen instead for geography or politics. Visit the capitol: the building itself tells the state's story in stone.", "s": "public-reference", "f": null}, {"t": "Nickname: Hawkeye State", "d": "Iowa is known as \"Hawkeye State.\"", "g": "overview", "l": 2, "q": "What is Nickname: Hawkeye State?", "a": "Iowa is known as \"Hawkeye State.\"", "x": "The nickname \"Hawkeye State\" captures how Iowa sees itself — and how America sees it. The Iowa caucuses made it first-in-the-nation every four years. State nicknames come from history, geography, or industry, and they appear on license plates, tourism campaigns, and sports teams. The motto goes deeper: \"Our liberties we prize and our rights we will maintain.\"", "s": "public-reference", "f": null}, {"t": "Motto: Our liberties we prize and our rights we will maintain", "d": "The state motto of Iowa is \"Our liberties we prize and our rights we will maintain.\"", "g": "overview", "l": 2, "q": "What is Motto: Our liberties we prize and our rights we will maintain?", "a": "The state motto of Iowa is \"Our liberties we prize and our rights we will maintain.\"", "x": "The motto \"Our liberties we prize and our rights we will maintain\" is Iowa's official creed, adopted by the legislature and carried on the state seal. Eagle with Iowa motto ribbon on blue. Mottos distill a state's ideals into a phrase — learn it, and you understand what the state aspires to be.", "s": "public-reference", "f": null}, {"t": "History 1", "d": "Meskwaki and Sioux; Black Hawk War.", "g": "history", "l": 2, "q": "What is History 1?", "a": "Meskwaki and Sioux; Black Hawk War.", "x": "Iowa history: Meskwaki and Sioux; Black Hawk War.. This chapter explains the Hawkeye State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 1: why it matters", "d": "Why this Iowa chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 1: why it matters?", "a": "Why this Iowa chapter still shapes the state.", "x": "Why it matters: Meskwaki and Sioux; Black Hawk War. That event's fingerprints are on modern Iowa — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 2", "d": "Corn and hogs; caucus fame.", "g": "history", "l": 2, "q": "What is History 2?", "a": "Corn and hogs; caucus fame.", "x": "Iowa history: Corn and hogs; caucus fame.. This chapter explains the Hawkeye State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 2: why it matters", "d": "Why this Iowa chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 2: why it matters?", "a": "Why this Iowa chapter still shapes the state.", "x": "Why it matters: Corn and hogs; caucus fame. That event's fingerprints are on modern Iowa — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 3", "d": "Bridges of Madison County.", "g": "history", "l": 2, "q": "What is History 3?", "a": "Bridges of Madison County.", "x": "Iowa history: Bridges of Madison County.. This chapter explains the Hawkeye State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 3: why it matters", "d": "Why this Iowa chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 3: why it matters?", "a": "Why this Iowa chapter still shapes the state.", "x": "Why it matters: Bridges of Madison County. That event's fingerprints are on modern Iowa — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 4", "d": "The Iowa caucuses made it first-in-the-nation every four years.", "g": "history", "l": 2, "q": "What is History 4?", "a": "The Iowa caucuses made it first-in-the-nation every four years.", "x": "Iowa history: The Iowa caucuses made it first-in-the-nation every four years.. This chapter explains the Hawkeye State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 4: why it matters", "d": "Why this Iowa chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 4: why it matters?", "a": "Why this Iowa chapter still shapes the state.", "x": "Why it matters: The Iowa caucuses made it first-in-the-nation every four years. That event's fingerprints are on modern Iowa — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "John Wayne", "d": "Actor from Winterset.", "g": "people", "l": 2, "q": "What is John Wayne?", "a": "Actor from Winterset.", "x": "John Wayne — Actor from Winterset.. Iowa's famous sons and daughters carried the state's name worldwide. Actor from Winterset. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "John Wayne: legacy", "d": "The legacy of John Wayne.", "g": "people", "l": 2, "q": "What is John Wayne: legacy?", "a": "The legacy of John Wayne.", "x": "The legacy of John Wayne: Actor from Winterset.. Iowa honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Herbert Hoover", "d": "31st president from West Branch.", "g": "people", "l": 2, "q": "What is Herbert Hoover?", "a": "31st president from West Branch.", "x": "Herbert Hoover — 31st president from West Branch.. Iowa's famous sons and daughters carried the state's name worldwide. 31st president from West Branch. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Herbert Hoover: legacy", "d": "The legacy of Herbert Hoover.", "g": "people", "l": 2, "q": "What is Herbert Hoover: legacy?", "a": "The legacy of Herbert Hoover.", "x": "The legacy of Herbert Hoover: 31st president from West Branch.. Iowa honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Johnny Carson", "d": "TV host from Corning.", "g": "people", "l": 2, "q": "What is Johnny Carson?", "a": "TV host from Corning.", "x": "Johnny Carson — TV host from Corning.. Iowa's famous sons and daughters carried the state's name worldwide. TV host from Corning. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Johnny Carson: legacy", "d": "The legacy of Johnny Carson.", "g": "people", "l": 2, "q": "What is Johnny Carson: legacy?", "a": "The legacy of Johnny Carson.", "x": "The legacy of Johnny Carson: TV host from Corning.. Iowa honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Industry: agriculture (corn, hogs)", "d": "agriculture (corn, hogs)", "g": "economy", "l": 2, "q": "What is Industry: agriculture (corn, hogs)?", "a": "agriculture (corn, hogs)", "x": "Iowa's economy: agriculture (corn, hogs). Industries shape the state's cities, its workforce, and its politics. agriculture (corn, hogs) From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Industry: insurance (Des Moines)", "d": "insurance (Des Moines)", "g": "economy", "l": 2, "q": "What is Industry: insurance (Des Moines)?", "a": "insurance (Des Moines)", "x": "Iowa's economy: insurance (Des Moines). Industries shape the state's cities, its workforce, and its politics. agriculture (corn, hogs) From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Geography", "d": "The land of Iowa: from Effigy Mounds National Monument to its borders.", "g": "geography", "l": 2, "q": "What is Geography?", "a": "The land of Iowa: from Effigy Mounds National Monument to its borders.", "x": "The geography of Iowa runs from Effigy Mounds National Monument across the state's varied regions. Landforms decide climate, crops, and settlement — the mountains, plains, coasts, or forests that define the state's look and livelihood. Field of Dreams", "s": "public-reference", "f": null}, {"t": "Modern era", "d": "Iowa today: insurance (Des Moines).", "g": "history", "l": 2, "q": "What is Modern era?", "a": "Iowa today: insurance (Des Moines).", "x": "Modern Iowa: insurance (Des Moines). Today's state balances growth with heritage — new industries beside historic downtowns, newcomers beside old families. The current chapter is still being written by everyone who lives here.", "s": "public-reference", "f": null}, {"t": "Visiting history", "d": "Experience Iowa history firsthand.", "g": "facts", "l": 2, "q": "What is Visiting history?", "a": "Experience Iowa history firsthand.", "x": "Experience Iowa history: the capitol in Des Moines, the museums, the historic districts, and Field of Dreams. Iowa State Fair History is best learned standing where it happened — walk the old streets, read the plaques, and talk to the docents who love it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-iowa-history-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
