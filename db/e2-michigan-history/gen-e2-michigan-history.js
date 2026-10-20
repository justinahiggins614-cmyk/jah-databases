(function(){'use strict';
/* JAH Michigan History Database generator — jahdb-e2-michigan-history-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-michigan-history',PREFIX='JAH-E2MICHIGANH-',NAME='JAH Michigan History Database';
var FIELDS=["overview", "statehood", "history", "people", "economy", "geography", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Michigan: history overview", "d": "Michigan: the Great Lakes State, admitted 1837 (26th); capital Lansing.", "g": "overview", "l": 2, "q": "What is Michigan: history overview?", "a": "Michigan: the Great Lakes State, admitted 1837 (26th); capital Lansing.", "x": "Michigan — \"Great Lakes State\" — entered the Union 1837 (26th). Its capital is Lansing and its largest city is Detroit. Ojibwe; French then British. This database tells the state's story: from its first peoples through statehood to the modern era, plus the famous sons and daughters, the industries, and the facts every resident should know.", "s": "public-reference", "f": null}, {"t": "Statehood", "d": "Michigan became a state 1837 (26th).", "g": "statehood", "l": 2, "q": "What is Statehood?", "a": "Michigan became a state 1837 (26th).", "x": "Michigan achieved statehood 1837 (26th). The road to statehood ran through territorial government, population thresholds, and a congressional enabling act — the standard American path. Auto industry; Detroit boom. Statehood Day is still celebrated, and the admission order gives Michigan its number among the states.", "s": "public-reference", "f": null}, {"t": "The statehood story", "d": "How Michigan went from territory to state.", "g": "statehood", "l": 2, "q": "What is The statehood story?", "a": "How Michigan went from territory to state.", "x": "The statehood story of Michigan: settlement, territorial organization, the push for admission, and finally the star on the flag. Deindustrialization; comeback. Every state's admission reflected the national politics of its era — Michigan's story is no exception, and it explains much about the state's character today.", "s": "public-reference", "f": null}, {"t": "Capital: Lansing", "d": "Lansing is the capital of Michigan.", "g": "overview", "l": 2, "q": "What is Capital: Lansing?", "a": "Lansing is the capital of Michigan.", "x": "Lansing has been the seat of Michigan government, home to the capitol building, the supreme court, and the legislature. Capitals are often not the biggest city — Michigan's largest is Detroit — chosen instead for geography or politics. Visit the capitol: the building itself tells the state's story in stone.", "s": "public-reference", "f": null}, {"t": "Nickname: Great Lakes State", "d": "Michigan is known as \"Great Lakes State.\"", "g": "overview", "l": 2, "q": "What is Nickname: Great Lakes State?", "a": "Michigan is known as \"Great Lakes State.\"", "x": "The nickname \"Great Lakes State\" captures how Michigan sees itself — and how America sees it. The auto industry made Detroit the Motor City. State nicknames come from history, geography, or industry, and they appear on license plates, tourism campaigns, and sports teams. The motto goes deeper: \"Si quaeris peninsulam amoenam circumspice (If you seek a pleasant peninsula, look about you).\"", "s": "public-reference", "f": null}, {"t": "Motto: Si quaeris peninsulam amoenam circumspice (If you seek a pleasant peninsula, look about you)", "d": "The state motto of Michigan is \"Si quaeris peninsulam amoenam circumspice (If you seek a pleasant peninsula, look about you).\"", "g": "overview", "l": 2, "q": "What is Motto: Si quaeris peninsulam amoenam circumspice (If you seek a pleasant peninsula, look about you)?", "a": "The state motto of Michigan is \"Si quaeris peninsulam amoenam circumspice (If you seek a pleasant peninsula, look about you).\"", "x": "The motto \"Si quaeris peninsulam amoenam circumspice (If you seek a pleasant peninsula, look about you)\" is Michigan's official creed, adopted by the legislature and carried on the state seal. Elk, moose, and eagle seal on blue. Mottos distill a state's ideals into a phrase — learn it, and you understand what the state aspires to be.", "s": "public-reference", "f": null}, {"t": "History 1", "d": "Ojibwe; French then British.", "g": "history", "l": 2, "q": "What is History 1?", "a": "Ojibwe; French then British.", "x": "Michigan history: Ojibwe; French then British.. This chapter explains the Great Lakes State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 1: why it matters", "d": "Why this Michigan chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 1: why it matters?", "a": "Why this Michigan chapter still shapes the state.", "x": "Why it matters: Ojibwe; French then British. That event's fingerprints are on modern Michigan — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 2", "d": "Auto industry; Detroit boom.", "g": "history", "l": 2, "q": "What is History 2?", "a": "Auto industry; Detroit boom.", "x": "Michigan history: Auto industry; Detroit boom.. This chapter explains the Great Lakes State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 2: why it matters", "d": "Why this Michigan chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 2: why it matters?", "a": "Why this Michigan chapter still shapes the state.", "x": "Why it matters: Auto industry; Detroit boom. That event's fingerprints are on modern Michigan — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 3", "d": "Deindustrialization; comeback.", "g": "history", "l": 2, "q": "What is History 3?", "a": "Deindustrialization; comeback.", "x": "Michigan history: Deindustrialization; comeback.. This chapter explains the Great Lakes State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 3: why it matters", "d": "Why this Michigan chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 3: why it matters?", "a": "Why this Michigan chapter still shapes the state.", "x": "Why it matters: Deindustrialization; comeback. That event's fingerprints are on modern Michigan — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 4", "d": "The auto industry made Detroit the Motor City.", "g": "history", "l": 2, "q": "What is History 4?", "a": "The auto industry made Detroit the Motor City.", "x": "Michigan history: The auto industry made Detroit the Motor City.. This chapter explains the Great Lakes State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 4: why it matters", "d": "Why this Michigan chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 4: why it matters?", "a": "Why this Michigan chapter still shapes the state.", "x": "Why it matters: The auto industry made Detroit the Motor City. That event's fingerprints are on modern Michigan — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "Henry Ford", "d": "Auto pioneer.", "g": "people", "l": 2, "q": "What is Henry Ford?", "a": "Auto pioneer.", "x": "Henry Ford — Auto pioneer.. Michigan's famous sons and daughters carried the state's name worldwide. Auto pioneer. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Henry Ford: legacy", "d": "The legacy of Henry Ford.", "g": "people", "l": 2, "q": "What is Henry Ford: legacy?", "a": "The legacy of Henry Ford.", "x": "The legacy of Henry Ford: Auto pioneer.. Michigan honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Aretha Franklin", "d": "Queen of Soul; Detroit.", "g": "people", "l": 2, "q": "What is Aretha Franklin?", "a": "Queen of Soul; Detroit.", "x": "Aretha Franklin — Queen of Soul; Detroit.. Michigan's famous sons and daughters carried the state's name worldwide. Queen of Soul; Detroit. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Aretha Franklin: legacy", "d": "The legacy of Aretha Franklin.", "g": "people", "l": 2, "q": "What is Aretha Franklin: legacy?", "a": "The legacy of Aretha Franklin.", "x": "The legacy of Aretha Franklin: Queen of Soul; Detroit.. Michigan honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Gerald Ford", "d": "38th president from Grand Rapids.", "g": "people", "l": 2, "q": "What is Gerald Ford?", "a": "38th president from Grand Rapids.", "x": "Gerald Ford — 38th president from Grand Rapids.. Michigan's famous sons and daughters carried the state's name worldwide. 38th president from Grand Rapids. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Gerald Ford: legacy", "d": "The legacy of Gerald Ford.", "g": "people", "l": 2, "q": "What is Gerald Ford: legacy?", "a": "The legacy of Gerald Ford.", "x": "The legacy of Gerald Ford: 38th president from Grand Rapids.. Michigan honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name.", "s": "public-reference", "f": null}, {"t": "Industry: automotive", "d": "automotive", "g": "economy", "l": 2, "q": "What is Industry: automotive?", "a": "automotive", "x": "Michigan's economy: automotive. Industries shape the state's cities, its workforce, and its politics. automotive From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Industry: tourism", "d": "tourism", "g": "economy", "l": 2, "q": "What is Industry: tourism?", "a": "tourism", "x": "Michigan's economy: tourism. Industries shape the state's cities, its workforce, and its politics. automotive From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Geography", "d": "The land of Michigan: from Sleeping Bear Dunes National Lakeshore to its borders.", "g": "geography", "l": 2, "q": "What is Geography?", "a": "The land of Michigan: from Sleeping Bear Dunes National Lakeshore to its borders.", "x": "The geography of Michigan runs from Sleeping Bear Dunes National Lakeshore across the state's varied regions. Landforms decide climate, crops, and settlement — the mountains, plains, coasts, or forests that define the state's look and livelihood. Mackinac Island", "s": "public-reference", "f": null}, {"t": "Modern era", "d": "Michigan today: tourism.", "g": "history", "l": 2, "q": "What is Modern era?", "a": "Michigan today: tourism.", "x": "Modern Michigan: tourism. Today's state balances growth with heritage — new industries beside historic downtowns, newcomers beside old families. The current chapter is still being written by everyone who lives here.", "s": "public-reference", "f": null}, {"t": "Visiting history", "d": "Experience Michigan history firsthand.", "g": "facts", "l": 2, "q": "What is Visiting history?", "a": "Experience Michigan history firsthand.", "x": "Experience Michigan history: the capitol in Lansing, the museums, the historic districts, and Mackinac Island. Detroit Jazz Festival History is best learned standing where it happened — walk the old streets, read the plaques, and talk to the docents who love it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-michigan-history-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
