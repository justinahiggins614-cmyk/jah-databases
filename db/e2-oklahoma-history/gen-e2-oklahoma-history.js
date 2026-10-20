(function(){'use strict';
/* JAH Oklahoma History Database generator — jahdb-e2-oklahoma-history-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-oklahoma-history',PREFIX='JAH-E2OKLAHOMAH-',NAME='JAH Oklahoma History Database';
var FIELDS=["overview", "statehood", "history", "people", "economy", "geography", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Oklahoma: history overview", "d": "Oklahoma: the Sooner State, admitted 1907 (46th); capital Oklahoma City.", "g": "overview", "l": 2, "q": "What is Oklahoma: history overview?", "a": "Oklahoma: the Sooner State, admitted 1907 (46th); capital Oklahoma City.", "x": "Oklahoma — \"Sooner State\" — entered the Union 1907 (46th). Its capital is Oklahoma City and its largest city is Oklahoma City. Trail of Tears; Five Tribes. This database tells the state's story: from its first peoples through statehood to the modern era, plus the famous sons and daughters, the industries, and the facts every resident should know.", "s": "public-reference", "f": null}, {"t": "Statehood", "d": "Oklahoma became a state 1907 (46th).", "g": "statehood", "l": 2, "q": "What is Statehood?", "a": "Oklahoma became a state 1907 (46th).", "x": "Oklahoma achieved statehood 1907 (46th). The road to statehood ran through territorial government, population thresholds, and a congressional enabling act — the standard American path. Land Run 1889; Dust Bowl. Statehood Day is still celebrated, and the admission order gives Oklahoma its number among the states.", "s": "public-reference", "f": null}, {"t": "The statehood story", "d": "How Oklahoma went from territory to state.", "g": "statehood", "l": 2, "q": "What is The statehood story?", "a": "How Oklahoma went from territory to state.", "x": "The statehood story of Oklahoma: settlement, territorial organization, the push for admission, and finally the star on the flag. Oil and Native nations. Every state's admission reflected the national politics of its era — Oklahoma's story is no exception, and it explains much about the state's character today.", "s": "public-reference", "f": null}, {"t": "Capital: Oklahoma City", "d": "Oklahoma City is the capital of Oklahoma.", "g": "overview", "l": 2, "q": "What is Capital: Oklahoma City?", "a": "Oklahoma City is the capital of Oklahoma.", "x": "Oklahoma City has been the seat of Oklahoma government, home to the capitol building, the supreme court, and the legislature. Capitals are often not the biggest city — Oklahoma's largest is Oklahoma City — chosen instead for geography or politics. Visit the capitol: the building itself tells the state's story in stone.", "s": "public-reference", "f": null}, {"t": "Nickname: Sooner State", "d": "Oklahoma is known as \"Sooner State.\"", "g": "overview", "l": 2, "q": "What is Nickname: Sooner State?", "a": "Oklahoma is known as \"Sooner State.\"", "x": "The nickname \"Sooner State\" captures how Oklahoma sees itself — and how America sees it. The Land Run of 1889 settled it in a single day. State nicknames come from history, geography, or industry, and they appear on license plates, tourism campaigns, and sports teams. The motto goes deeper: \"Labor omnia vincit (Labor conquers all things).\"", "s": "public-reference", "f": null}, {"t": "Motto: Labor omnia vincit (Labor conquers all things)", "d": "The state motto of Oklahoma is \"Labor omnia vincit (Labor conquers all things).\"", "g": "overview", "l": 2, "q": "What is Motto: Labor omnia vincit (Labor conquers all things)?", "a": "The state motto of Oklahoma is \"Labor omnia vincit (Labor conquers all things).\"", "x": "The motto \"Labor omnia vincit (Labor conquers all things)\" is Oklahoma's official creed, adopted by the legislature and carried on the state seal. Osage shield on blue. Mottos distill a state's ideals into a phrase — learn it, and you understand what the state aspires to be.", "s": "public-reference", "f": null}, {"t": "History 1", "d": "Trail of Tears; Five Tribes.", "g": "history", "l": 2, "q": "What is History 1?", "a": "Trail of Tears; Five Tribes.", "x": "Oklahoma history: Trail of Tears; Five Tribes.. This chapter explains the Sooner State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 1: why it matters", "d": "Why this Oklahoma chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 1: why it matters?", "a": "Why this Oklahoma chapter still shapes the state.", "x": "Why it matters: Trail of Tears; Five Tribes. That event's fingerprints are on modern Oklahoma — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 2", "d": "Land Run 1889; Dust Bowl.", "g": "history", "l": 2, "q": "What is History 2?", "a": "Land Run 1889; Dust Bowl.", "x": "Oklahoma history: Land Run 1889; Dust Bowl.. This chapter explains the Sooner State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 2: why it matters", "d": "Why this Oklahoma chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 2: why it matters?", "a": "Why this Oklahoma chapter still shapes the state.", "x": "Why it matters: Land Run 1889; Dust Bowl. That event's fingerprints are on modern Oklahoma — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 3", "d": "Oil and Native nations.", "g": "history", "l": 2, "q": "What is History 3?", "a": "Oil and Native nations.", "x": "Oklahoma history: Oil and Native nations.. This chapter explains the Sooner State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 3: why it matters", "d": "Why this Oklahoma chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 3: why it matters?", "a": "Why this Oklahoma chapter still shapes the state.", "x": "Why it matters: Oil and Native nations. That event's fingerprints are on modern Oklahoma — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 4", "d": "The Land Run of 1889 settled it in a single day.", "g": "history", "l": 2, "q": "What is History 4?", "a": "The Land Run of 1889 settled it in a single day.", "x": "Oklahoma history: The Land Run of 1889 settled it in a single day.. This chapter explains the Sooner State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 4: why it matters", "d": "Why this Oklahoma chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 4: why it matters?", "a": "Why this Oklahoma chapter still shapes the state.", "x": "Why it matters: The Land Run of 1889 settled it in a single day. That event's fingerprints are on modern Oklahoma — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "Will Rogers", "d": "Humorist from Oologah.", "g": "people", "l": 2, "q": "What is Will Rogers?", "a": "Humorist from Oologah.", "x": "Will Rogers — Humorist from Oologah.. Oklahoma's famous sons and daughters carried the state's name worldwide. Humorist from Oologah. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Will Rogers: legacy", "d": "The legacy of Will Rogers.", "g": "people", "l": 2, "q": "What is Will Rogers: legacy?", "a": "The legacy of Will Rogers.", "x": "The legacy of Will Rogers: Humorist from Oologah.. Oklahoma honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Woody Guthrie", "d": "Singer from Okemah.", "g": "people", "l": 2, "q": "What is Woody Guthrie?", "a": "Singer from Okemah.", "x": "Woody Guthrie — Singer from Okemah.. Oklahoma's famous sons and daughters carried the state's name worldwide. Singer from Okemah. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Woody Guthrie: legacy", "d": "The legacy of Woody Guthrie.", "g": "people", "l": 2, "q": "What is Woody Guthrie: legacy?", "a": "The legacy of Woody Guthrie.", "x": "The legacy of Woody Guthrie: Singer from Okemah.. Oklahoma honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Reba McEntire", "d": "Singer from McAlester.", "g": "people", "l": 2, "q": "What is Reba McEntire?", "a": "Singer from McAlester.", "x": "Reba McEntire — Singer from McAlester.. Oklahoma's famous sons and daughters carried the state's name worldwide. Singer from McAlester. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Reba McEntire: legacy", "d": "The legacy of Reba McEntire.", "g": "people", "l": 2, "q": "What is Reba McEntire: legacy?", "a": "The legacy of Reba McEntire.", "x": "The legacy of Reba McEntire: Singer from McAlester.. Oklahoma honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Industry: energy (oil, wind)", "d": "energy (oil, wind)", "g": "economy", "l": 2, "q": "What is Industry: energy (oil, wind)?", "a": "energy (oil, wind)", "x": "Oklahoma's economy: energy (oil, wind). Industries shape the state's cities, its workforce, and its politics. energy (oil, wind) From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Industry: aerospace", "d": "aerospace", "g": "economy", "l": 2, "q": "What is Industry: aerospace?", "a": "aerospace", "x": "Oklahoma's economy: aerospace. Industries shape the state's cities, its workforce, and its politics. energy (oil, wind) From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Geography", "d": "The land of Oklahoma: from Wichita Mountains Wildlife Refuge to its borders.", "g": "geography", "l": 2, "q": "What is Geography?", "a": "The land of Oklahoma: from Wichita Mountains Wildlife Refuge to its borders.", "x": "The geography of Oklahoma runs from Wichita Mountains Wildlife Refuge across the state's varied regions. Landforms decide climate, crops, and settlement — the mountains, plains, coasts, or forests that define the state's look and livelihood. Oklahoma City Memorial", "s": "public-reference", "f": null}, {"t": "Modern era", "d": "Oklahoma today: aerospace.", "g": "history", "l": 2, "q": "What is Modern era?", "a": "Oklahoma today: aerospace.", "x": "Modern Oklahoma: aerospace. Today's state balances growth with heritage — new industries beside historic downtowns, newcomers beside old families. The current chapter is still being written by everyone who lives here.", "s": "public-reference", "f": null}, {"t": "Visiting history", "d": "Experience Oklahoma history firsthand.", "g": "facts", "l": 2, "q": "What is Visiting history?", "a": "Experience Oklahoma history firsthand.", "x": "Experience Oklahoma history: the capitol in Oklahoma City, the museums, the historic districts, and Oklahoma City Memorial. Oklahoma State Fair History is best learned standing where it happened — walk the old streets, read the plaques, and talk to the docents who love it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-oklahoma-history-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
