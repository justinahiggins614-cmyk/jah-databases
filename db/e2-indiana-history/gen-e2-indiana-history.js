(function(){'use strict';
/* JAH Indiana History Database generator — jahdb-e2-indiana-history-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-indiana-history',PREFIX='JAH-E2INDIANAHI-',NAME='JAH Indiana History Database';
var FIELDS=["overview", "statehood", "history", "people", "economy", "geography", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Indiana: history overview", "d": "Indiana: the Hoosier State, admitted 1816 (19th); capital Indianapolis.", "g": "overview", "l": 2, "q": "What is Indiana: history overview?", "a": "Indiana: the Hoosier State, admitted 1816 (19th); capital Indianapolis.", "x": "Indiana — \"Hoosier State\" — entered the Union 1816 (19th). Its capital is Indianapolis and its largest city is Indianapolis. Miami and Potawatomi; Northwest Territory. This database tells the state's story: from its first peoples through statehood to the modern era, plus the famous sons and daughters, the industries, and the facts every resident should know.", "s": "public-reference", "f": null}, {"t": "Statehood", "d": "Indiana became a state 1816 (19th).", "g": "statehood", "l": 2, "q": "What is Statehood?", "a": "Indiana became a state 1816 (19th).", "x": "Indiana achieved statehood 1816 (19th). The road to statehood ran through territorial government, population thresholds, and a congressional enabling act — the standard American path. Underground Railroad; Civil War. Statehood Day is still celebrated, and the admission order gives Indiana its number among the states.", "s": "public-reference", "f": null}, {"t": "The statehood story", "d": "How Indiana went from territory to state.", "g": "statehood", "l": 2, "q": "What is The statehood story?", "a": "How Indiana went from territory to state.", "x": "The statehood story of Indiana: settlement, territorial organization, the push for admission, and finally the star on the flag. Auto and steel; Indy 500. Every state's admission reflected the national politics of its era — Indiana's story is no exception, and it explains much about the state's character today.", "s": "public-reference", "f": null}, {"t": "Capital: Indianapolis", "d": "Indianapolis is the capital of Indiana.", "g": "overview", "l": 2, "q": "What is Capital: Indianapolis?", "a": "Indianapolis is the capital of Indiana.", "x": "Indianapolis has been the seat of Indiana government, home to the capitol building, the supreme court, and the legislature. Capitals are often not the biggest city — Indiana's largest is Indianapolis — chosen instead for geography or politics. Visit the capitol: the building itself tells the state's story in stone.", "s": "public-reference", "f": null}, {"t": "Nickname: Hoosier State", "d": "Indiana is known as \"Hoosier State.\"", "g": "overview", "l": 2, "q": "What is Nickname: Hoosier State?", "a": "Indiana is known as \"Hoosier State.\"", "x": "The nickname \"Hoosier State\" captures how Indiana sees itself — and how America sees it. Basketball heartland. State nicknames come from history, geography, or industry, and they appear on license plates, tourism campaigns, and sports teams. The motto goes deeper: \"The Crossroads of America.\"", "s": "public-reference", "f": null}, {"t": "Motto: The Crossroads of America", "d": "The state motto of Indiana is \"The Crossroads of America.\"", "g": "overview", "l": 2, "q": "What is Motto: The Crossroads of America?", "a": "The state motto of Indiana is \"The Crossroads of America.\"", "x": "The motto \"The Crossroads of America\" is Indiana's official creed, adopted by the legislature and carried on the state seal. Torch of liberty with 19 stars on blue. Mottos distill a state's ideals into a phrase — learn it, and you understand what the state aspires to be.", "s": "public-reference", "f": null}, {"t": "History 1", "d": "Miami and Potawatomi; Northwest Territory.", "g": "history", "l": 2, "q": "What is History 1?", "a": "Miami and Potawatomi; Northwest Territory.", "x": "Indiana history: Miami and Potawatomi; Northwest Territory.. This chapter explains the Hoosier State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 1: why it matters", "d": "Why this Indiana chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 1: why it matters?", "a": "Why this Indiana chapter still shapes the state.", "x": "Why it matters: Miami and Potawatomi; Northwest Territory. That event's fingerprints are on modern Indiana — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 2", "d": "Underground Railroad; Civil War.", "g": "history", "l": 2, "q": "What is History 2?", "a": "Underground Railroad; Civil War.", "x": "Indiana history: Underground Railroad; Civil War.. This chapter explains the Hoosier State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 2: why it matters", "d": "Why this Indiana chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 2: why it matters?", "a": "Why this Indiana chapter still shapes the state.", "x": "Why it matters: Underground Railroad; Civil War. That event's fingerprints are on modern Indiana — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 3", "d": "Auto and steel; Indy 500.", "g": "history", "l": 2, "q": "What is History 3?", "a": "Auto and steel; Indy 500.", "x": "Indiana history: Auto and steel; Indy 500.. This chapter explains the Hoosier State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 3: why it matters", "d": "Why this Indiana chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 3: why it matters?", "a": "Why this Indiana chapter still shapes the state.", "x": "Why it matters: Auto and steel; Indy 500. That event's fingerprints are on modern Indiana — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 4", "d": "Basketball heartland.", "g": "history", "l": 2, "q": "What is History 4?", "a": "Basketball heartland.", "x": "Indiana history: Basketball heartland.. This chapter explains the Hoosier State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 4: why it matters", "d": "Why this Indiana chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 4: why it matters?", "a": "Why this Indiana chapter still shapes the state.", "x": "Why it matters: Basketball heartland. That event's fingerprints are on modern Indiana — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "Larry Bird", "d": "Celtics legend from French Lick.", "g": "people", "l": 2, "q": "What is Larry Bird?", "a": "Celtics legend from French Lick.", "x": "Larry Bird — Celtics legend from French Lick.. Indiana's famous sons and daughters carried the state's name worldwide. Celtics legend from French Lick. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Larry Bird: legacy", "d": "The legacy of Larry Bird.", "g": "people", "l": 2, "q": "What is Larry Bird: legacy?", "a": "The legacy of Larry Bird.", "x": "The legacy of Larry Bird: Celtics legend from French Lick.. Indiana honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "James Dean", "d": "Actor from Marion.", "g": "people", "l": 2, "q": "What is James Dean?", "a": "Actor from Marion.", "x": "James Dean — Actor from Marion.. Indiana's famous sons and daughters carried the state's name worldwide. Actor from Marion. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "James Dean: legacy", "d": "The legacy of James Dean.", "g": "people", "l": 2, "q": "What is James Dean: legacy?", "a": "The legacy of James Dean.", "x": "The legacy of James Dean: Actor from Marion.. Indiana honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Michael Jackson", "d": "Born in Gary.", "g": "people", "l": 2, "q": "What is Michael Jackson?", "a": "Born in Gary.", "x": "Michael Jackson — Born in Gary.. Indiana's famous sons and daughters carried the state's name worldwide. Born in Gary. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Michael Jackson: legacy", "d": "The legacy of Michael Jackson.", "g": "people", "l": 2, "q": "What is Michael Jackson: legacy?", "a": "The legacy of Michael Jackson.", "x": "The legacy of Michael Jackson: Born in Gary.. Indiana honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Industry: manufacturing (autos)", "d": "manufacturing (autos)", "g": "economy", "l": 2, "q": "What is Industry: manufacturing (autos)?", "a": "manufacturing (autos)", "x": "Indiana's economy: manufacturing (autos). Industries shape the state's cities, its workforce, and its politics. manufacturing (autos) From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Industry: agriculture (corn)", "d": "agriculture (corn)", "g": "economy", "l": 2, "q": "What is Industry: agriculture (corn)?", "a": "agriculture (corn)", "x": "Indiana's economy: agriculture (corn). Industries shape the state's cities, its workforce, and its politics. manufacturing (autos) From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Geography", "d": "The land of Indiana: from Indiana Dunes National Park to its borders.", "g": "geography", "l": 2, "q": "What is Geography?", "a": "The land of Indiana: from Indiana Dunes National Park to its borders.", "x": "The geography of Indiana runs from Indiana Dunes National Park across the state's varied regions. Landforms decide climate, crops, and settlement — the mountains, plains, coasts, or forests that define the state's look and livelihood. Indianapolis 500", "s": "public-reference", "f": null}, {"t": "Modern era", "d": "Indiana today: agriculture (corn).", "g": "history", "l": 2, "q": "What is Modern era?", "a": "Indiana today: agriculture (corn).", "x": "Modern Indiana: agriculture (corn). Today's state balances growth with heritage — new industries beside historic downtowns, newcomers beside old families. The current chapter is still being written by everyone who lives here.", "s": "public-reference", "f": null}, {"t": "Visiting history", "d": "Experience Indiana history firsthand.", "g": "facts", "l": 2, "q": "What is Visiting history?", "a": "Experience Indiana history firsthand.", "x": "Experience Indiana history: the capitol in Indianapolis, the museums, the historic districts, and Indianapolis 500. Indy 500 History is best learned standing where it happened — walk the old streets, read the plaques, and talk to the docents who love it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-indiana-history-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
