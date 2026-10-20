(function(){'use strict';
/* JAH Minnesota History Database generator — jahdb-e2-minnesota-history-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-minnesota-history',PREFIX='JAH-E2MINNESOTA-',NAME='JAH Minnesota History Database';
var FIELDS=["overview", "statehood", "history", "people", "economy", "geography", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Minnesota: history overview", "d": "Minnesota: the North Star State, admitted 1858 (32nd); capital St. Paul.", "g": "overview", "l": 2, "q": "What is Minnesota: history overview?", "a": "Minnesota: the North Star State, admitted 1858 (32nd); capital St. Paul.", "x": "Minnesota — \"North Star State\" — entered the Union 1858 (32nd). Its capital is St. Paul and its largest city is Minneapolis. Dakota and Ojibwe; French then U.S. This database tells the state's story: from its first peoples through statehood to the modern era, plus the famous sons and daughters, the industries, and the facts every resident should know.", "s": "public-reference", "f": null}, {"t": "Statehood", "d": "Minnesota became a state 1858 (32nd).", "g": "statehood", "l": 2, "q": "What is Statehood?", "a": "Minnesota became a state 1858 (32nd).", "x": "Minnesota achieved statehood 1858 (32nd). The road to statehood ran through territorial government, population thresholds, and a congressional enabling act — the standard American path. Flour milling; iron range. Statehood Day is still celebrated, and the admission order gives Minnesota its number among the states.", "s": "public-reference", "f": null}, {"t": "The statehood story", "d": "How Minnesota went from territory to state.", "g": "statehood", "l": 2, "q": "What is The statehood story?", "a": "How Minnesota went from territory to state.", "x": "The statehood story of Minnesota: settlement, territorial organization, the push for admission, and finally the star on the flag. Progressive politics; Mayo Clinic. Every state's admission reflected the national politics of its era — Minnesota's story is no exception, and it explains much about the state's character today.", "s": "public-reference", "f": null}, {"t": "Capital: St. Paul", "d": "St. Paul is the capital of Minnesota.", "g": "overview", "l": 2, "q": "What is Capital: St. Paul?", "a": "St. Paul is the capital of Minnesota.", "x": "St. Paul has been the seat of Minnesota government, home to the capitol building, the supreme court, and the legislature. Capitals are often not the biggest city — Minnesota's largest is Minneapolis — chosen instead for geography or politics. Visit the capitol: the building itself tells the state's story in stone.", "s": "public-reference", "f": null}, {"t": "Nickname: North Star State", "d": "Minnesota is known as \"North Star State.\"", "g": "overview", "l": 2, "q": "What is Nickname: North Star State?", "a": "Minnesota is known as \"North Star State.\"", "x": "The nickname \"North Star State\" captures how Minnesota sees itself — and how America sees it. The Mayo Clinic made Rochester a medical mecca. State nicknames come from history, geography, or industry, and they appear on license plates, tourism campaigns, and sports teams. The motto goes deeper: \"L'Etoile du Nord (The star of the north).\"", "s": "public-reference", "f": null}, {"t": "Motto: L'Etoile du Nord (The star of the north)", "d": "The state motto of Minnesota is \"L'Etoile du Nord (The star of the north).\"", "g": "overview", "l": 2, "q": "What is Motto: L'Etoile du Nord (The star of the north)?", "a": "The state motto of Minnesota is \"L'Etoile du Nord (The star of the north).\"", "x": "The motto \"L'Etoile du Nord (The star of the north)\" is Minnesota's official creed, adopted by the legislature and carried on the state seal. Seal with farmer, Native American, Mississippi on blue. Mottos distill a state's ideals into a phrase — learn it, and you understand what the state aspires to be.", "s": "public-reference", "f": null}, {"t": "History 1", "d": "Dakota and Ojibwe; French then U.S.", "g": "history", "l": 2, "q": "What is History 1?", "a": "Dakota and Ojibwe; French then U.S.", "x": "Minnesota history: Dakota and Ojibwe; French then U.S.. This chapter explains the North Star State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 1: why it matters", "d": "Why this Minnesota chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 1: why it matters?", "a": "Why this Minnesota chapter still shapes the state.", "x": "Why it matters: Dakota and Ojibwe; French then U.S. That event's fingerprints are on modern Minnesota — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 2", "d": "Flour milling; iron range.", "g": "history", "l": 2, "q": "What is History 2?", "a": "Flour milling; iron range.", "x": "Minnesota history: Flour milling; iron range.. This chapter explains the North Star State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 2: why it matters", "d": "Why this Minnesota chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 2: why it matters?", "a": "Why this Minnesota chapter still shapes the state.", "x": "Why it matters: Flour milling; iron range. That event's fingerprints are on modern Minnesota — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 3", "d": "Progressive politics; Mayo Clinic.", "g": "history", "l": 2, "q": "What is History 3?", "a": "Progressive politics; Mayo Clinic.", "x": "Minnesota history: Progressive politics; Mayo Clinic.. This chapter explains the North Star State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 3: why it matters", "d": "Why this Minnesota chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 3: why it matters?", "a": "Why this Minnesota chapter still shapes the state.", "x": "Why it matters: Progressive politics; Mayo Clinic. That event's fingerprints are on modern Minnesota — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 4", "d": "The Mayo Clinic made Rochester a medical mecca.", "g": "history", "l": 2, "q": "What is History 4?", "a": "The Mayo Clinic made Rochester a medical mecca.", "x": "Minnesota history: The Mayo Clinic made Rochester a medical mecca.. This chapter explains the North Star State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 4: why it matters", "d": "Why this Minnesota chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 4: why it matters?", "a": "Why this Minnesota chapter still shapes the state.", "x": "Why it matters: The Mayo Clinic made Rochester a medical mecca. That event's fingerprints are on modern Minnesota — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "Prince", "d": "Musician from Minneapolis.", "g": "people", "l": 2, "q": "What is Prince?", "a": "Musician from Minneapolis.", "x": "Prince — Musician from Minneapolis.. Minnesota's famous sons and daughters carried the state's name worldwide. Musician from Minneapolis. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Prince: legacy", "d": "The legacy of Prince.", "g": "people", "l": 2, "q": "What is Prince: legacy?", "a": "The legacy of Prince.", "x": "The legacy of Prince: Musician from Minneapolis.. Minnesota honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Bob Dylan", "d": "Born in Duluth.", "g": "people", "l": 2, "q": "What is Bob Dylan?", "a": "Born in Duluth.", "x": "Bob Dylan — Born in Duluth.. Minnesota's famous sons and daughters carried the state's name worldwide. Born in Duluth. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Bob Dylan: legacy", "d": "The legacy of Bob Dylan.", "g": "people", "l": 2, "q": "What is Bob Dylan: legacy?", "a": "The legacy of Bob Dylan.", "x": "The legacy of Bob Dylan: Born in Duluth.. Minnesota honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Hubert Humphrey", "d": "VP from Wallace.", "g": "people", "l": 2, "q": "What is Hubert Humphrey?", "a": "VP from Wallace.", "x": "Hubert Humphrey — VP from Wallace.. Minnesota's famous sons and daughters carried the state's name worldwide. VP from Wallace. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Hubert Humphrey: legacy", "d": "The legacy of Hubert Humphrey.", "g": "people", "l": 2, "q": "What is Hubert Humphrey: legacy?", "a": "The legacy of Hubert Humphrey.", "x": "The legacy of Hubert Humphrey: VP from Wallace.. Minnesota honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Industry: healthcare (Mayo, UnitedHealth)", "d": "healthcare (Mayo, UnitedHealth)", "g": "economy", "l": 2, "q": "What is Industry: healthcare (Mayo, UnitedHealth)?", "a": "healthcare (Mayo, UnitedHealth)", "x": "Minnesota's economy: healthcare (Mayo, UnitedHealth). Industries shape the state's cities, its workforce, and its politics. healthcare (Mayo, UnitedHealth) From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Industry: agriculture", "d": "agriculture", "g": "economy", "l": 2, "q": "What is Industry: agriculture?", "a": "agriculture", "x": "Minnesota's economy: agriculture. Industries shape the state's cities, its workforce, and its politics. healthcare (Mayo, UnitedHealth) From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Geography", "d": "The land of Minnesota: from Voyageurs National Park to its borders.", "g": "geography", "l": 2, "q": "What is Geography?", "a": "The land of Minnesota: from Voyageurs National Park to its borders.", "x": "The geography of Minnesota runs from Voyageurs National Park across the state's varied regions. Landforms decide climate, crops, and settlement — the mountains, plains, coasts, or forests that define the state's look and livelihood. Mall of America", "s": "public-reference", "f": null}, {"t": "Modern era", "d": "Minnesota today: agriculture.", "g": "history", "l": 2, "q": "What is Modern era?", "a": "Minnesota today: agriculture.", "x": "Modern Minnesota: agriculture. Today's state balances growth with heritage — new industries beside historic downtowns, newcomers beside old families. The current chapter is still being written by everyone who lives here.", "s": "public-reference", "f": null}, {"t": "Visiting history", "d": "Experience Minnesota history firsthand.", "g": "facts", "l": 2, "q": "What is Visiting history?", "a": "Experience Minnesota history firsthand.", "x": "Experience Minnesota history: the capitol in St. Paul, the museums, the historic districts, and Mall of America. Minnesota State Fair History is best learned standing where it happened — walk the old streets, read the plaques, and talk to the docents who love it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-minnesota-history-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
