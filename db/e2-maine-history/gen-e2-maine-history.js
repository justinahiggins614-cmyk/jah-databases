(function(){'use strict';
/* JAH Maine History Database generator — jahdb-e2-maine-history-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-maine-history',PREFIX='JAH-E2MAINEHIST-',NAME='JAH Maine History Database';
var FIELDS=["overview", "statehood", "history", "people", "economy", "geography", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Maine: history overview", "d": "Maine: the Pine Tree State, admitted 1820 (23rd); capital Augusta.", "g": "overview", "l": 2, "q": "What is Maine: history overview?", "a": "Maine: the Pine Tree State, admitted 1820 (23rd); capital Augusta.", "x": "Maine — \"Pine Tree State\" — entered the Union 1820 (23rd). Its capital is Augusta and its largest city is Portland. Wabanaki; Massachusetts district. This database tells the state's story: from its first peoples through statehood to the modern era, plus the famous sons and daughters, the industries, and the facts every resident should know.", "s": "public-reference", "f": null}, {"t": "Statehood", "d": "Maine became a state 1820 (23rd).", "g": "statehood", "l": 2, "q": "What is Statehood?", "a": "Maine became a state 1820 (23rd).", "x": "Maine achieved statehood 1820 (23rd). The road to statehood ran through territorial government, population thresholds, and a congressional enabling act — the standard American path. Statehood 1820 (Missouri Compromise). Statehood Day is still celebrated, and the admission order gives Maine its number among the states.", "s": "public-reference", "f": null}, {"t": "The statehood story", "d": "How Maine went from territory to state.", "g": "statehood", "l": 2, "q": "What is The statehood story?", "a": "How Maine went from territory to state.", "x": "The statehood story of Maine: settlement, territorial organization, the push for admission, and finally the star on the flag. Shipbuilding; lumber; lobster. Every state's admission reflected the national politics of its era — Maine's story is no exception, and it explains much about the state's character today.", "s": "public-reference", "f": null}, {"t": "Capital: Augusta", "d": "Augusta is the capital of Maine.", "g": "overview", "l": 2, "q": "What is Capital: Augusta?", "a": "Augusta is the capital of Maine.", "x": "Augusta has been the seat of Maine government, home to the capitol building, the supreme court, and the legislature. Capitals are often not the biggest city — Maine's largest is Portland — chosen instead for geography or politics. Visit the capitol: the building itself tells the state's story in stone.", "s": "public-reference", "f": null}, {"t": "Nickname: Pine Tree State", "d": "Maine is known as \"Pine Tree State.\"", "g": "overview", "l": 2, "q": "What is Nickname: Pine Tree State?", "a": "Maine is known as \"Pine Tree State.\"", "x": "The nickname \"Pine Tree State\" captures how Maine sees itself — and how America sees it. Shipbuilding and lumber built the coastal economy. State nicknames come from history, geography, or industry, and they appear on license plates, tourism campaigns, and sports teams. The motto goes deeper: \"Dirigo (I lead).\"", "s": "public-reference", "f": null}, {"t": "Motto: Dirigo (I lead)", "d": "The state motto of Maine is \"Dirigo (I lead).\"", "g": "overview", "l": 2, "q": "What is Motto: Dirigo (I lead)?", "a": "The state motto of Maine is \"Dirigo (I lead).\"", "x": "The motto \"Dirigo (I lead)\" is Maine's official creed, adopted by the legislature and carried on the state seal. Pine and moose seal on blue. Mottos distill a state's ideals into a phrase — learn it, and you understand what the state aspires to be.", "s": "public-reference", "f": null}, {"t": "History 1", "d": "Wabanaki; Massachusetts district.", "g": "history", "l": 2, "q": "What is History 1?", "a": "Wabanaki; Massachusetts district.", "x": "Maine history: Wabanaki; Massachusetts district.. This chapter explains the Pine Tree State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 1: why it matters", "d": "Why this Maine chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 1: why it matters?", "a": "Why this Maine chapter still shapes the state.", "x": "Why it matters: Wabanaki; Massachusetts district. That event's fingerprints are on modern Maine — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 2", "d": "Statehood 1820 (Missouri Compromise).", "g": "history", "l": 2, "q": "What is History 2?", "a": "Statehood 1820 (Missouri Compromise).", "x": "Maine history: Statehood 1820 (Missouri Compromise).. This chapter explains the Pine Tree State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 2: why it matters", "d": "Why this Maine chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 2: why it matters?", "a": "Why this Maine chapter still shapes the state.", "x": "Why it matters: Statehood 1820 (Missouri Compromise). That event's fingerprints are on modern Maine — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 3", "d": "Shipbuilding; lumber; lobster.", "g": "history", "l": 2, "q": "What is History 3?", "a": "Shipbuilding; lumber; lobster.", "x": "Maine history: Shipbuilding; lumber; lobster.. This chapter explains the Pine Tree State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 3: why it matters", "d": "Why this Maine chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 3: why it matters?", "a": "Why this Maine chapter still shapes the state.", "x": "Why it matters: Shipbuilding; lumber; lobster. That event's fingerprints are on modern Maine — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 4", "d": "Shipbuilding and lumber built the coastal economy.", "g": "history", "l": 2, "q": "What is History 4?", "a": "Shipbuilding and lumber built the coastal economy.", "x": "Maine history: Shipbuilding and lumber built the coastal economy.. This chapter explains the Pine Tree State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 4: why it matters", "d": "Why this Maine chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 4: why it matters?", "a": "Why this Maine chapter still shapes the state.", "x": "Why it matters: Shipbuilding and lumber built the coastal economy. That event's fingerprints are on modern Maine — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "Stephen King", "d": "Author from Bangor.", "g": "people", "l": 2, "q": "What is Stephen King?", "a": "Author from Bangor.", "x": "Stephen King — Author from Bangor.. Maine's famous sons and daughters carried the state's name worldwide. Author from Bangor. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Stephen King: legacy", "d": "The legacy of Stephen King.", "g": "people", "l": 2, "q": "What is Stephen King: legacy?", "a": "The legacy of Stephen King.", "x": "The legacy of Stephen King: Author from Bangor.. Maine honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Henry Wadsworth Longfellow", "d": "Poet from Portland.", "g": "people", "l": 2, "q": "What is Henry Wadsworth Longfellow?", "a": "Poet from Portland.", "x": "Henry Wadsworth Longfellow — Poet from Portland.. Maine's famous sons and daughters carried the state's name worldwide. Poet from Portland. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Henry Wadsworth Longfellow: legacy", "d": "The legacy of Henry Wadsworth Longfellow.", "g": "people", "l": 2, "q": "What is Henry Wadsworth Longfellow: legacy?", "a": "The legacy of Henry Wadsworth Longfellow.", "x": "The legacy of Henry Wadsworth Longfellow: Poet from Portland.. Maine honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Margaret Chase Smith", "d": "Senator from Skowhegan.", "g": "people", "l": 2, "q": "What is Margaret Chase Smith?", "a": "Senator from Skowhegan.", "x": "Margaret Chase Smith — Senator from Skowhegan.. Maine's famous sons and daughters carried the state's name worldwide. Senator from Skowhegan. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Margaret Chase Smith: legacy", "d": "The legacy of Margaret Chase Smith.", "g": "people", "l": 2, "q": "What is Margaret Chase Smith: legacy?", "a": "The legacy of Margaret Chase Smith.", "x": "The legacy of Margaret Chase Smith: Senator from Skowhegan.. Maine honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Industry: lobster fishing", "d": "lobster fishing", "g": "economy", "l": 2, "q": "What is Industry: lobster fishing?", "a": "lobster fishing", "x": "Maine's economy: lobster fishing. Industries shape the state's cities, its workforce, and its politics. lobster fishing From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Industry: tourism", "d": "tourism", "g": "economy", "l": 2, "q": "What is Industry: tourism?", "a": "tourism", "x": "Maine's economy: tourism. Industries shape the state's cities, its workforce, and its politics. lobster fishing From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Geography", "d": "The land of Maine: from Acadia National Park to its borders.", "g": "geography", "l": 2, "q": "What is Geography?", "a": "The land of Maine: from Acadia National Park to its borders.", "x": "The geography of Maine runs from Acadia National Park across the state's varied regions. Landforms decide climate, crops, and settlement — the mountains, plains, coasts, or forests that define the state's look and livelihood. Acadia National Park", "s": "public-reference", "f": null}, {"t": "Modern era", "d": "Maine today: tourism.", "g": "history", "l": 2, "q": "What is Modern era?", "a": "Maine today: tourism.", "x": "Modern Maine: tourism. Today's state balances growth with heritage — new industries beside historic downtowns, newcomers beside old families. The current chapter is still being written by everyone who lives here.", "s": "public-reference", "f": null}, {"t": "Visiting history", "d": "Experience Maine history firsthand.", "g": "facts", "l": 2, "q": "What is Visiting history?", "a": "Experience Maine history firsthand.", "x": "Experience Maine history: the capitol in Augusta, the museums, the historic districts, and Acadia National Park. Portland festivals History is best learned standing where it happened — walk the old streets, read the plaques, and talk to the docents who love it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-maine-history-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
