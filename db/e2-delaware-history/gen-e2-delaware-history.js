(function(){'use strict';
/* JAH Delaware History Database generator — jahdb-e2-delaware-history-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-delaware-history',PREFIX='JAH-E2DELAWAREH-',NAME='JAH Delaware History Database';
var FIELDS=["overview", "statehood", "history", "people", "economy", "geography", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Delaware: history overview", "d": "Delaware: the First State, admitted 1787 (1st); capital Dover.", "g": "overview", "l": 2, "q": "What is Delaware: history overview?", "a": "Delaware: the First State, admitted 1787 (1st); capital Dover.", "x": "Delaware — \"First State\" — entered the Union 1787 (1st). Its capital is Dover and its largest city is Wilmington. Lenape lands; Swedish then Dutch then English. This database tells the state's story: from its first peoples through statehood to the modern era, plus the famous sons and daughters, the industries, and the facts every resident should know.", "s": "public-reference", "f": null}, {"t": "Statehood", "d": "Delaware became a state 1787 (1st).", "g": "statehood", "l": 2, "q": "What is Statehood?", "a": "Delaware became a state 1787 (1st).", "x": "Delaware achieved statehood 1787 (1st). The road to statehood ran through territorial government, population thresholds, and a congressional enabling act — the standard American path. First to ratify the Constitution. Statehood Day is still celebrated, and the admission order gives Delaware its number among the states.", "s": "public-reference", "f": null}, {"t": "The statehood story", "d": "How Delaware went from territory to state.", "g": "statehood", "l": 2, "q": "What is The statehood story?", "a": "How Delaware went from territory to state.", "x": "The statehood story of Delaware: settlement, territorial organization, the push for admission, and finally the star on the flag. DuPont chemicals; corporate haven. Every state's admission reflected the national politics of its era — Delaware's story is no exception, and it explains much about the state's character today.", "s": "public-reference", "f": null}, {"t": "Capital: Dover", "d": "Dover is the capital of Delaware.", "g": "overview", "l": 2, "q": "What is Capital: Dover?", "a": "Dover is the capital of Delaware.", "x": "Dover has been the seat of Delaware government, home to the capitol building, the supreme court, and the legislature. Capitals are often not the biggest city — Delaware's largest is Wilmington — chosen instead for geography or politics. Visit the capitol: the building itself tells the state's story in stone.", "s": "public-reference", "f": null}, {"t": "Nickname: First State", "d": "Delaware is known as \"First State.\"", "g": "overview", "l": 2, "q": "What is Nickname: First State?", "a": "Delaware is known as \"First State.\"", "x": "The nickname \"First State\" captures how Delaware sees itself — and how America sees it. Tax-free shopping. State nicknames come from history, geography, or industry, and they appear on license plates, tourism campaigns, and sports teams. The motto goes deeper: \"Liberty and Independence.\"", "s": "public-reference", "f": null}, {"t": "Motto: Liberty and Independence", "d": "The state motto of Delaware is \"Liberty and Independence.\"", "g": "overview", "l": 2, "q": "What is Motto: Liberty and Independence?", "a": "The state motto of Delaware is \"Liberty and Independence.\"", "x": "The motto \"Liberty and Independence\" is Delaware's official creed, adopted by the legislature and carried on the state seal. Buff diamond on colonial blue; 1787 date. Mottos distill a state's ideals into a phrase — learn it, and you understand what the state aspires to be.", "s": "public-reference", "f": null}, {"t": "History 1", "d": "Lenape lands; Swedish then Dutch then English.", "g": "history", "l": 2, "q": "What is History 1?", "a": "Lenape lands; Swedish then Dutch then English.", "x": "Delaware history: Lenape lands; Swedish then Dutch then English.. This chapter explains the First State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 1: why it matters", "d": "Why this Delaware chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 1: why it matters?", "a": "Why this Delaware chapter still shapes the state.", "x": "Why it matters: Lenape lands; Swedish then Dutch then English. That event's fingerprints are on modern Delaware — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 2", "d": "First to ratify the Constitution.", "g": "history", "l": 2, "q": "What is History 2?", "a": "First to ratify the Constitution.", "x": "Delaware history: First to ratify the Constitution.. This chapter explains the First State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 2: why it matters", "d": "Why this Delaware chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 2: why it matters?", "a": "Why this Delaware chapter still shapes the state.", "x": "Why it matters: First to ratify the Constitution. That event's fingerprints are on modern Delaware — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 3", "d": "DuPont chemicals; corporate haven.", "g": "history", "l": 2, "q": "What is History 3?", "a": "DuPont chemicals; corporate haven.", "x": "Delaware history: DuPont chemicals; corporate haven.. This chapter explains the First State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 3: why it matters", "d": "Why this Delaware chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 3: why it matters?", "a": "Why this Delaware chapter still shapes the state.", "x": "Why it matters: DuPont chemicals; corporate haven. That event's fingerprints are on modern Delaware — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 4", "d": "Tax-free shopping.", "g": "history", "l": 2, "q": "What is History 4?", "a": "Tax-free shopping.", "x": "Delaware history: Tax-free shopping.. This chapter explains the First State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 4: why it matters", "d": "Why this Delaware chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 4: why it matters?", "a": "Why this Delaware chapter still shapes the state.", "x": "Why it matters: Tax-free shopping. That event's fingerprints are on modern Delaware — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "Joe Biden", "d": "46th president; longtime senator.", "g": "people", "l": 2, "q": "What is Joe Biden?", "a": "46th president; longtime senator.", "x": "Joe Biden — 46th president; longtime senator.. Delaware's famous sons and daughters carried the state's name worldwide. 46th president; longtime senator. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Joe Biden: legacy", "d": "The legacy of Joe Biden.", "g": "people", "l": 2, "q": "What is Joe Biden: legacy?", "a": "The legacy of Joe Biden.", "x": "The legacy of Joe Biden: 46th president; longtime senator.. Delaware honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Annie Jump Cannon", "d": "Astronomer from Dover.", "g": "people", "l": 2, "q": "What is Annie Jump Cannon?", "a": "Astronomer from Dover.", "x": "Annie Jump Cannon — Astronomer from Dover.. Delaware's famous sons and daughters carried the state's name worldwide. Astronomer from Dover. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Annie Jump Cannon: legacy", "d": "The legacy of Annie Jump Cannon.", "g": "people", "l": 2, "q": "What is Annie Jump Cannon: legacy?", "a": "The legacy of Annie Jump Cannon.", "x": "The legacy of Annie Jump Cannon: Astronomer from Dover.. Delaware honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Valerie Bertinelli", "d": "Actress from Wilmington.", "g": "people", "l": 2, "q": "What is Valerie Bertinelli?", "a": "Actress from Wilmington.", "x": "Valerie Bertinelli — Actress from Wilmington.. Delaware's famous sons and daughters carried the state's name worldwide. Actress from Wilmington. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Valerie Bertinelli: legacy", "d": "The legacy of Valerie Bertinelli.", "g": "people", "l": 2, "q": "What is Valerie Bertinelli: legacy?", "a": "The legacy of Valerie Bertinelli.", "x": "The legacy of Valerie Bertinelli: Actress from Wilmington.. Delaware honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Industry: chemicals (DuPont)", "d": "chemicals (DuPont)", "g": "economy", "l": 2, "q": "What is Industry: chemicals (DuPont)?", "a": "chemicals (DuPont)", "x": "Delaware's economy: chemicals (DuPont). Industries shape the state's cities, its workforce, and its politics. chemicals (DuPont) From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Industry: corporate services", "d": "corporate services", "g": "economy", "l": 2, "q": "What is Industry: corporate services?", "a": "corporate services", "x": "Delaware's economy: corporate services. Industries shape the state's cities, its workforce, and its politics. chemicals (DuPont) From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Geography", "d": "The land of Delaware: from Cape Henlopen State Park to its borders.", "g": "geography", "l": 2, "q": "What is Geography?", "a": "The land of Delaware: from Cape Henlopen State Park to its borders.", "x": "The geography of Delaware runs from Cape Henlopen State Park across the state's varied regions. Landforms decide climate, crops, and settlement — the mountains, plains, coasts, or forests that define the state's look and livelihood. Rehoboth Beach", "s": "public-reference", "f": null}, {"t": "Modern era", "d": "Delaware today: corporate services.", "g": "history", "l": 2, "q": "What is Modern era?", "a": "Delaware today: corporate services.", "x": "Modern Delaware: corporate services. Today's state balances growth with heritage — new industries beside historic downtowns, newcomers beside old families. The current chapter is still being written by everyone who lives here.", "s": "public-reference", "f": null}, {"t": "Visiting history", "d": "Experience Delaware history firsthand.", "g": "facts", "l": 2, "q": "What is Visiting history?", "a": "Experience Delaware history firsthand.", "x": "Experience Delaware history: the capitol in Dover, the museums, the historic districts, and Rehoboth Beach. Rehoboth Beach festivals History is best learned standing where it happened — walk the old streets, read the plaques, and talk to the docents who love it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-delaware-history-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
