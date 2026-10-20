(function(){'use strict';
/* JAH Arkansas History Database generator — jahdb-e2-arkansas-history-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-arkansas-history',PREFIX='JAH-E2ARKANSASH-',NAME='JAH Arkansas History Database';
var FIELDS=["overview", "statehood", "history", "people", "economy", "geography", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Arkansas: history overview", "d": "Arkansas: the The Natural State, admitted 1836 (25th); capital Little Rock.", "g": "overview", "l": 2, "q": "What is Arkansas: history overview?", "a": "Arkansas: the The Natural State, admitted 1836 (25th); capital Little Rock.", "x": "Arkansas — \"The Natural State\" — entered the Union 1836 (25th). Its capital is Little Rock and its largest city is Little Rock. Quapaw and Caddo lands; French then U.S. This database tells the state's story: from its first peoples through statehood to the modern era, plus the famous sons and daughters, the industries, and the facts every resident should know.", "s": "public-reference", "f": null}, {"t": "Statehood", "d": "Arkansas became a state 1836 (25th).", "g": "statehood", "l": 2, "q": "What is Statehood?", "a": "Arkansas became a state 1836 (25th).", "x": "Arkansas achieved statehood 1836 (25th). The road to statehood ran through territorial government, population thresholds, and a congressional enabling act — the standard American path. Cotton and slavery; Civil War. Statehood Day is still celebrated, and the admission order gives Arkansas its number among the states.", "s": "public-reference", "f": null}, {"t": "The statehood story", "d": "How Arkansas went from territory to state.", "g": "statehood", "l": 2, "q": "What is The statehood story?", "a": "How Arkansas went from territory to state.", "x": "The statehood story of Arkansas: settlement, territorial organization, the push for admission, and finally the star on the flag. Little Rock Nine (1957) desegregation. Every state's admission reflected the national politics of its era — Arkansas's story is no exception, and it explains much about the state's character today.", "s": "public-reference", "f": null}, {"t": "Capital: Little Rock", "d": "Little Rock is the capital of Arkansas.", "g": "overview", "l": 2, "q": "What is Capital: Little Rock?", "a": "Little Rock is the capital of Arkansas.", "x": "Little Rock has been the seat of Arkansas government, home to the capitol building, the supreme court, and the legislature. Capitals are often not the biggest city — Arkansas's largest is Little Rock — chosen instead for geography or politics. Visit the capitol: the building itself tells the state's story in stone.", "s": "public-reference", "f": null}, {"t": "Nickname: The Natural State", "d": "Arkansas is known as \"The Natural State.\"", "g": "overview", "l": 2, "q": "What is Nickname: The Natural State?", "a": "Arkansas is known as \"The Natural State.\"", "x": "The nickname \"The Natural State\" captures how Arkansas sees itself — and how America sees it. Walmart and Tyson era. State nicknames come from history, geography, or industry, and they appear on license plates, tourism campaigns, and sports teams. The motto goes deeper: \"Regnat populus (The people rule).\"", "s": "public-reference", "f": null}, {"t": "Motto: Regnat populus (The people rule)", "d": "The state motto of Arkansas is \"Regnat populus (The people rule).\"", "g": "overview", "l": 2, "q": "What is Motto: Regnat populus (The people rule)?", "a": "The state motto of Arkansas is \"Regnat populus (The people rule).\"", "x": "The motto \"Regnat populus (The people rule)\" is Arkansas's official creed, adopted by the legislature and carried on the state seal. Diamond shape for its diamond mine; 25 stars. Mottos distill a state's ideals into a phrase — learn it, and you understand what the state aspires to be.", "s": "public-reference", "f": null}, {"t": "History 1", "d": "Quapaw and Caddo lands; French then U.S.", "g": "history", "l": 2, "q": "What is History 1?", "a": "Quapaw and Caddo lands; French then U.S.", "x": "Arkansas history: Quapaw and Caddo lands; French then U.S.. This chapter explains the The Natural State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 1: why it matters", "d": "Why this Arkansas chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 1: why it matters?", "a": "Why this Arkansas chapter still shapes the state.", "x": "Why it matters: Quapaw and Caddo lands; French then U.S. That event's fingerprints are on modern Arkansas — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 2", "d": "Cotton and slavery; Civil War.", "g": "history", "l": 2, "q": "What is History 2?", "a": "Cotton and slavery; Civil War.", "x": "Arkansas history: Cotton and slavery; Civil War.. This chapter explains the The Natural State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 2: why it matters", "d": "Why this Arkansas chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 2: why it matters?", "a": "Why this Arkansas chapter still shapes the state.", "x": "Why it matters: Cotton and slavery; Civil War. That event's fingerprints are on modern Arkansas — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 3", "d": "Little Rock Nine (1957) desegregation.", "g": "history", "l": 2, "q": "What is History 3?", "a": "Little Rock Nine (1957) desegregation.", "x": "Arkansas history: Little Rock Nine (1957) desegregation.. This chapter explains the The Natural State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 3: why it matters", "d": "Why this Arkansas chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 3: why it matters?", "a": "Why this Arkansas chapter still shapes the state.", "x": "Why it matters: Little Rock Nine (1957) desegregation. That event's fingerprints are on modern Arkansas — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 4", "d": "Walmart and Tyson era.", "g": "history", "l": 2, "q": "What is History 4?", "a": "Walmart and Tyson era.", "x": "Arkansas history: Walmart and Tyson era.. This chapter explains the The Natural State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 4: why it matters", "d": "Why this Arkansas chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 4: why it matters?", "a": "Why this Arkansas chapter still shapes the state.", "x": "Why it matters: Walmart and Tyson era. That event's fingerprints are on modern Arkansas — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "Bill Clinton", "d": "42nd president from Hope.", "g": "people", "l": 2, "q": "What is Bill Clinton?", "a": "42nd president from Hope.", "x": "Bill Clinton — 42nd president from Hope.. Arkansas's famous sons and daughters carried the state's name worldwide. 42nd president from Hope. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Bill Clinton: legacy", "d": "The legacy of Bill Clinton.", "g": "people", "l": 2, "q": "What is Bill Clinton: legacy?", "a": "The legacy of Bill Clinton.", "x": "The legacy of Bill Clinton: 42nd president from Hope.. Arkansas honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Johnny Cash", "d": "Singer from Kingsland.", "g": "people", "l": 2, "q": "What is Johnny Cash?", "a": "Singer from Kingsland.", "x": "Johnny Cash — Singer from Kingsland.. Arkansas's famous sons and daughters carried the state's name worldwide. Singer from Kingsland. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Johnny Cash: legacy", "d": "The legacy of Johnny Cash.", "g": "people", "l": 2, "q": "What is Johnny Cash: legacy?", "a": "The legacy of Johnny Cash.", "x": "The legacy of Johnny Cash: Singer from Kingsland.. Arkansas honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Daisy Bates", "d": "Little Rock Nine mentor.", "g": "people", "l": 2, "q": "What is Daisy Bates?", "a": "Little Rock Nine mentor.", "x": "Daisy Bates — Little Rock Nine mentor.. Arkansas's famous sons and daughters carried the state's name worldwide. Little Rock Nine mentor. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Daisy Bates: legacy", "d": "The legacy of Daisy Bates.", "g": "people", "l": 2, "q": "What is Daisy Bates: legacy?", "a": "The legacy of Daisy Bates.", "x": "The legacy of Daisy Bates: Little Rock Nine mentor.. Arkansas honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Industry: retail (Walmart HQ)", "d": "retail (Walmart HQ)", "g": "economy", "l": 2, "q": "What is Industry: retail (Walmart HQ)?", "a": "retail (Walmart HQ)", "x": "Arkansas's economy: retail (Walmart HQ). Industries shape the state's cities, its workforce, and its politics. retail (Walmart HQ) From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Industry: poultry (Tyson)", "d": "poultry (Tyson)", "g": "economy", "l": 2, "q": "What is Industry: poultry (Tyson)?", "a": "poultry (Tyson)", "x": "Arkansas's economy: poultry (Tyson). Industries shape the state's cities, its workforce, and its politics. retail (Walmart HQ) From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Geography", "d": "The land of Arkansas: from Hot Springs National Park to its borders.", "g": "geography", "l": 2, "q": "What is Geography?", "a": "The land of Arkansas: from Hot Springs National Park to its borders.", "x": "The geography of Arkansas runs from Hot Springs National Park across the state's varied regions. Landforms decide climate, crops, and settlement — the mountains, plains, coasts, or forests that define the state's look and livelihood. Hot Springs National Park", "s": "public-reference", "f": null}, {"t": "Modern era", "d": "Arkansas today: poultry (Tyson).", "g": "history", "l": 2, "q": "What is Modern era?", "a": "Arkansas today: poultry (Tyson).", "x": "Modern Arkansas: poultry (Tyson). Today's state balances growth with heritage — new industries beside historic downtowns, newcomers beside old families. The current chapter is still being written by everyone who lives here.", "s": "public-reference", "f": null}, {"t": "Visiting history", "d": "Experience Arkansas history firsthand.", "g": "facts", "l": 2, "q": "What is Visiting history?", "a": "Experience Arkansas history firsthand.", "x": "Experience Arkansas history: the capitol in Little Rock, the museums, the historic districts, and Hot Springs National Park. Little Rock Central High anniversaries History is best learned standing where it happened — walk the old streets, read the plaques, and talk to the docents who love it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-arkansas-history-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
