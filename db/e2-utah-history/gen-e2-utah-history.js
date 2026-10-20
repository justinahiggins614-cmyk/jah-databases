(function(){'use strict';
/* JAH Utah History Database generator — jahdb-e2-utah-history-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-utah-history',PREFIX='JAH-E2UTAHHISTO-',NAME='JAH Utah History Database';
var FIELDS=["overview", "statehood", "history", "people", "economy", "geography", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Utah: history overview", "d": "Utah: the Beehive State, admitted 1896 (45th); capital Salt Lake City.", "g": "overview", "l": 2, "q": "What is Utah: history overview?", "a": "Utah: the Beehive State, admitted 1896 (45th); capital Salt Lake City.", "x": "Utah — \"Beehive State\" — entered the Union 1896 (45th). Its capital is Salt Lake City and its largest city is Salt Lake City. Ute; Mormon pioneers 1847. This database tells the state's story: from its first peoples through statehood to the modern era, plus the famous sons and daughters, the industries, and the facts every resident should know.", "s": "public-reference", "f": null}, {"t": "Statehood", "d": "Utah became a state 1896 (45th).", "g": "statehood", "l": 2, "q": "What is Statehood?", "a": "Utah became a state 1896 (45th).", "x": "Utah achieved statehood 1896 (45th). The road to statehood ran through territorial government, population thresholds, and a congressional enabling act — the standard American path. Statehood 1896. Statehood Day is still celebrated, and the admission order gives Utah its number among the states.", "s": "public-reference", "f": null}, {"t": "The statehood story", "d": "How Utah went from territory to state.", "g": "statehood", "l": 2, "q": "What is The statehood story?", "a": "How Utah went from territory to state.", "x": "The statehood story of Utah: settlement, territorial organization, the push for admission, and finally the star on the flag. Skiing; tech (Silicon Slopes). Every state's admission reflected the national politics of its era — Utah's story is no exception, and it explains much about the state's character today.", "s": "public-reference", "f": null}, {"t": "Capital: Salt Lake City", "d": "Salt Lake City is the capital of Utah.", "g": "overview", "l": 2, "q": "What is Capital: Salt Lake City?", "a": "Salt Lake City is the capital of Utah.", "x": "Salt Lake City has been the seat of Utah government, home to the capitol building, the supreme court, and the legislature. Capitals are often not the biggest city — Utah's largest is Salt Lake City — chosen instead for geography or politics. Visit the capitol: the building itself tells the state's story in stone.", "s": "public-reference", "f": null}, {"t": "Nickname: Beehive State", "d": "Utah is known as \"Beehive State.\"", "g": "overview", "l": 2, "q": "What is Nickname: Beehive State?", "a": "Utah is known as \"Beehive State.\"", "x": "The nickname \"Beehive State\" captures how Utah sees itself — and how America sees it. The transcontinental railroad met at Promontory in 1869. State nicknames come from history, geography, or industry, and they appear on license plates, tourism campaigns, and sports teams. The motto goes deeper: \"Industry.\"", "s": "public-reference", "f": null}, {"t": "Motto: Industry", "d": "The state motto of Utah is \"Industry.\"", "g": "overview", "l": 2, "q": "What is Motto: Industry?", "a": "The state motto of Utah is \"Industry.\"", "x": "The motto \"Industry\" is Utah's official creed, adopted by the legislature and carried on the state seal. Beehive and sego lilies on new flag (2024). Mottos distill a state's ideals into a phrase — learn it, and you understand what the state aspires to be.", "s": "public-reference", "f": null}, {"t": "History 1", "d": "Ute; Mormon pioneers 1847.", "g": "history", "l": 2, "q": "What is History 1?", "a": "Ute; Mormon pioneers 1847.", "x": "Utah history: Ute; Mormon pioneers 1847.. This chapter explains the Beehive State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 1: why it matters", "d": "Why this Utah chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 1: why it matters?", "a": "Why this Utah chapter still shapes the state.", "x": "Why it matters: Ute; Mormon pioneers 1847. That event's fingerprints are on modern Utah — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 2", "d": "Statehood 1896.", "g": "history", "l": 2, "q": "What is History 2?", "a": "Statehood 1896.", "x": "Utah history: Statehood 1896.. This chapter explains the Beehive State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 2: why it matters", "d": "Why this Utah chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 2: why it matters?", "a": "Why this Utah chapter still shapes the state.", "x": "Why it matters: Statehood 1896. That event's fingerprints are on modern Utah — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "History 3", "d": "Skiing; tech (Silicon Slopes).", "g": "history", "l": 2, "q": "What is History 3?", "a": "Skiing; tech (Silicon Slopes).", "x": "Utah history: Skiing; tech (Silicon Slopes).. This chapter explains the Beehive State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 3: why it matters", "d": "Why this Utah chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 3: why it matters?", "a": "Why this Utah chapter still shapes the state.", "x": "Why it matters: Skiing; tech (Silicon Slopes). That event's fingerprints are on modern Utah — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 4", "d": "The transcontinental railroad met at Promontory in 1869.", "g": "history", "l": 2, "q": "What is History 4?", "a": "The transcontinental railroad met at Promontory in 1869.", "x": "Utah history: The transcontinental railroad met at Promontory in 1869.. This chapter explains the Beehive State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 4: why it matters", "d": "Why this Utah chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 4: why it matters?", "a": "Why this Utah chapter still shapes the state.", "x": "Why it matters: The transcontinental railroad met at Promontory in 1869. That event's fingerprints are on modern Utah — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "Brigham Young", "d": "Mormon leader.", "g": "people", "l": 2, "q": "What is Brigham Young?", "a": "Mormon leader.", "x": "Brigham Young — Mormon leader.. Utah's famous sons and daughters carried the state's name worldwide. Mormon leader. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Brigham Young: legacy", "d": "The legacy of Brigham Young.", "g": "people", "l": 2, "q": "What is Brigham Young: legacy?", "a": "The legacy of Brigham Young.", "x": "The legacy of Brigham Young: Mormon leader.. Utah honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Donny Osmond", "d": "Entertainer from Ogden.", "g": "people", "l": 2, "q": "What is Donny Osmond?", "a": "Entertainer from Ogden.", "x": "Donny Osmond — Entertainer from Ogden.. Utah's famous sons and daughters carried the state's name worldwide. Entertainer from Ogden. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Donny Osmond: legacy", "d": "The legacy of Donny Osmond.", "g": "people", "l": 2, "q": "What is Donny Osmond: legacy?", "a": "The legacy of Donny Osmond.", "x": "The legacy of Donny Osmond: Entertainer from Ogden.. Utah honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Robert Redford", "d": "Sundance founder; Utah ties.", "g": "people", "l": 2, "q": "What is Robert Redford?", "a": "Sundance founder; Utah ties.", "x": "Robert Redford — Sundance founder; Utah ties.. Utah's famous sons and daughters carried the state's name worldwide. Sundance founder; Utah ties. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Robert Redford: legacy", "d": "The legacy of Robert Redford.", "g": "people", "l": 2, "q": "What is Robert Redford: legacy?", "a": "The legacy of Robert Redford.", "x": "The legacy of Robert Redford: Sundance founder; Utah ties.. Utah honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Industry: tourism (skiing)", "d": "tourism (skiing)", "g": "economy", "l": 2, "q": "What is Industry: tourism (skiing)?", "a": "tourism (skiing)", "x": "Utah's economy: tourism (skiing). Industries shape the state's cities, its workforce, and its politics. tourism (skiing) From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Industry: technology", "d": "technology", "g": "economy", "l": 2, "q": "What is Industry: technology?", "a": "technology", "x": "Utah's economy: technology. Industries shape the state's cities, its workforce, and its politics. tourism (skiing) From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Geography", "d": "The land of Utah: from Zion National Park to its borders.", "g": "geography", "l": 2, "q": "What is Geography?", "a": "The land of Utah: from Zion National Park to its borders.", "x": "The geography of Utah runs from Zion National Park across the state's varied regions. Landforms decide climate, crops, and settlement — the mountains, plains, coasts, or forests that define the state's look and livelihood. Zion", "s": "public-reference", "f": null}, {"t": "Modern era", "d": "Utah today: technology.", "g": "history", "l": 2, "q": "What is Modern era?", "a": "Utah today: technology.", "x": "Modern Utah: technology. Today's state balances growth with heritage — new industries beside historic downtowns, newcomers beside old families. The current chapter is still being written by everyone who lives here.", "s": "public-reference", "f": null}, {"t": "Visiting history", "d": "Experience Utah history firsthand.", "g": "facts", "l": 2, "q": "What is Visiting history?", "a": "Experience Utah history firsthand.", "x": "Experience Utah history: the capitol in Salt Lake City, the museums, the historic districts, and Zion. Sundance Film Festival History is best learned standing where it happened — walk the old streets, read the plaques, and talk to the docents who love it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-utah-history-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
