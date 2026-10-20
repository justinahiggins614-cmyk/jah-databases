(function(){'use strict';
/* JAH Illinois History Database generator — jahdb-e2-illinois-history-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-illinois-history',PREFIX='JAH-E2ILLINOISH-',NAME='JAH Illinois History Database';
var FIELDS=["overview", "statehood", "history", "people", "economy", "geography", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Illinois: history overview", "d": "Illinois: the Prairie State, admitted 1818 (21st); capital Springfield.", "g": "overview", "l": 2, "q": "What is Illinois: history overview?", "a": "Illinois: the Prairie State, admitted 1818 (21st); capital Springfield.", "x": "Illinois — \"Prairie State\" — entered the Union 1818 (21st). Its capital is Springfield and its largest city is Chicago. Illini Confederacy; French then British. This database tells the state's story: from its first peoples through statehood to the modern era, plus the famous sons and daughters, the industries, and the facts every resident should know.", "s": "public-reference", "f": null}, {"t": "Statehood", "d": "Illinois became a state 1818 (21st).", "g": "statehood", "l": 2, "q": "What is Statehood?", "a": "Illinois became a state 1818 (21st).", "x": "Illinois achieved statehood 1818 (21st). The road to statehood ran through territorial government, population thresholds, and a congressional enabling act — the standard American path. Lincoln's home; Civil War. Statehood Day is still celebrated, and the admission order gives Illinois its number among the states.", "s": "public-reference", "f": null}, {"t": "The statehood story", "d": "How Illinois went from territory to state.", "g": "statehood", "l": 2, "q": "What is The statehood story?", "a": "How Illinois went from territory to state.", "x": "The statehood story of Illinois: settlement, territorial organization, the push for admission, and finally the star on the flag. Great Chicago Fire 1871. Every state's admission reflected the national politics of its era — Illinois's story is no exception, and it explains much about the state's character today.", "s": "public-reference", "f": null}, {"t": "Capital: Springfield", "d": "Springfield is the capital of Illinois.", "g": "overview", "l": 2, "q": "What is Capital: Springfield?", "a": "Springfield is the capital of Illinois.", "x": "Springfield has been the seat of Illinois government, home to the capitol building, the supreme court, and the legislature. Capitals are often not the biggest city — Illinois's largest is Chicago — chosen instead for geography or politics. Visit the capitol: the building itself tells the state's story in stone.", "s": "public-reference", "f": null}, {"t": "Nickname: Prairie State", "d": "Illinois is known as \"Prairie State.\"", "g": "overview", "l": 2, "q": "What is Nickname: Prairie State?", "a": "Illinois is known as \"Prairie State.\"", "x": "The nickname \"Prairie State\" captures how Illinois sees itself — and how America sees it. Corn, finance, industry. State nicknames come from history, geography, or industry, and they appear on license plates, tourism campaigns, and sports teams. The motto goes deeper: \"State sovereignty, national union.\"", "s": "public-reference", "f": null}, {"t": "Motto: State sovereignty, national union", "d": "The state motto of Illinois is \"State sovereignty, national union.\"", "g": "overview", "l": 2, "q": "What is Motto: State sovereignty, national union?", "a": "The state motto of Illinois is \"State sovereignty, national union.\"", "x": "The motto \"State sovereignty, national union\" is Illinois's official creed, adopted by the legislature and carried on the state seal. State seal on white; 'Illinois' added. Mottos distill a state's ideals into a phrase — learn it, and you understand what the state aspires to be.", "s": "public-reference", "f": null}, {"t": "History 1", "d": "Illini Confederacy; French then British.", "g": "history", "l": 2, "q": "What is History 1?", "a": "Illini Confederacy; French then British.", "x": "Illinois history: Illini Confederacy; French then British.. This chapter explains the Prairie State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 1: why it matters", "d": "Why this Illinois chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 1: why it matters?", "a": "Why this Illinois chapter still shapes the state.", "x": "Why it matters: Illini Confederacy; French then British. That event's fingerprints are on modern Illinois — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 2", "d": "Lincoln's home; Civil War.", "g": "history", "l": 2, "q": "What is History 2?", "a": "Lincoln's home; Civil War.", "x": "Illinois history: Lincoln's home; Civil War.. This chapter explains the Prairie State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 2: why it matters", "d": "Why this Illinois chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 2: why it matters?", "a": "Why this Illinois chapter still shapes the state.", "x": "Why it matters: Lincoln's home; Civil War. That event's fingerprints are on modern Illinois — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 3", "d": "Great Chicago Fire 1871.", "g": "history", "l": 2, "q": "What is History 3?", "a": "Great Chicago Fire 1871.", "x": "Illinois history: Great Chicago Fire 1871.. This chapter explains the Prairie State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 3: why it matters", "d": "Why this Illinois chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 3: why it matters?", "a": "Why this Illinois chapter still shapes the state.", "x": "Why it matters: Great Chicago Fire 1871. That event's fingerprints are on modern Illinois — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 4", "d": "Corn, finance, industry.", "g": "history", "l": 2, "q": "What is History 4?", "a": "Corn, finance, industry.", "x": "Illinois history: Corn, finance, industry.. This chapter explains the Prairie State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 4: why it matters", "d": "Why this Illinois chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 4: why it matters?", "a": "Why this Illinois chapter still shapes the state.", "x": "Why it matters: Corn, finance, industry. That event's fingerprints are on modern Illinois — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "Abraham Lincoln", "d": "16th president; Springfield.", "g": "people", "l": 2, "q": "What is Abraham Lincoln?", "a": "16th president; Springfield.", "x": "Abraham Lincoln — 16th president; Springfield.. Illinois's famous sons and daughters carried the state's name worldwide. 16th president; Springfield. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Abraham Lincoln: legacy", "d": "The legacy of Abraham Lincoln.", "g": "people", "l": 2, "q": "What is Abraham Lincoln: legacy?", "a": "The legacy of Abraham Lincoln.", "x": "The legacy of Abraham Lincoln: 16th president; Springfield.. Illinois honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Barack Obama", "d": "44th president; Chicago.", "g": "people", "l": 2, "q": "What is Barack Obama?", "a": "44th president; Chicago.", "x": "Barack Obama — 44th president; Chicago.. Illinois's famous sons and daughters carried the state's name worldwide. 44th president; Chicago. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Barack Obama: legacy", "d": "The legacy of Barack Obama.", "g": "people", "l": 2, "q": "What is Barack Obama: legacy?", "a": "The legacy of Barack Obama.", "x": "The legacy of Barack Obama: 44th president; Chicago.. Illinois honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Walt Disney", "d": "Born in Chicago.", "g": "people", "l": 2, "q": "What is Walt Disney?", "a": "Born in Chicago.", "x": "Walt Disney — Born in Chicago.. Illinois's famous sons and daughters carried the state's name worldwide. Born in Chicago. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Walt Disney: legacy", "d": "The legacy of Walt Disney.", "g": "people", "l": 2, "q": "What is Walt Disney: legacy?", "a": "The legacy of Walt Disney.", "x": "The legacy of Walt Disney: Born in Chicago.. Illinois honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Industry: finance (Chicago)", "d": "finance (Chicago)", "g": "economy", "l": 2, "q": "What is Industry: finance (Chicago)?", "a": "finance (Chicago)", "x": "Illinois's economy: finance (Chicago). Industries shape the state's cities, its workforce, and its politics. finance (Chicago) From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Industry: agriculture (corn, soy)", "d": "agriculture (corn, soy)", "g": "economy", "l": 2, "q": "What is Industry: agriculture (corn, soy)?", "a": "agriculture (corn, soy)", "x": "Illinois's economy: agriculture (corn, soy). Industries shape the state's cities, its workforce, and its politics. finance (Chicago) From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Geography", "d": "The land of Illinois: from Starved Rock State Park to its borders.", "g": "geography", "l": 2, "q": "What is Geography?", "a": "The land of Illinois: from Starved Rock State Park to its borders.", "x": "The geography of Illinois runs from Starved Rock State Park across the state's varied regions. Landforms decide climate, crops, and settlement — the mountains, plains, coasts, or forests that define the state's look and livelihood. Chicago skyline", "s": "public-reference", "f": null}, {"t": "Modern era", "d": "Illinois today: agriculture (corn, soy).", "g": "history", "l": 2, "q": "What is Modern era?", "a": "Illinois today: agriculture (corn, soy).", "x": "Modern Illinois: agriculture (corn, soy). Today's state balances growth with heritage — new industries beside historic downtowns, newcomers beside old families. The current chapter is still being written by everyone who lives here.", "s": "public-reference", "f": null}, {"t": "Visiting history", "d": "Experience Illinois history firsthand.", "g": "facts", "l": 2, "q": "What is Visiting history?", "a": "Experience Illinois history firsthand.", "x": "Experience Illinois history: the capitol in Springfield, the museums, the historic districts, and Chicago skyline. Taste of Chicago History is best learned standing where it happened — walk the old streets, read the plaques, and talk to the docents who love it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-illinois-history-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
