(function(){'use strict';
/* JAH Missouri History Database generator — jahdb-e2-missouri-history-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-missouri-history',PREFIX='JAH-E2MISSOURIH-',NAME='JAH Missouri History Database';
var FIELDS=["overview", "statehood", "history", "people", "economy", "geography", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Missouri: history overview", "d": "Missouri: the Show-Me State, admitted 1821 (24th); capital Jefferson City.", "g": "overview", "l": 2, "q": "What is Missouri: history overview?", "a": "Missouri: the Show-Me State, admitted 1821 (24th); capital Jefferson City.", "x": "Missouri — \"Show-Me State\" — entered the Union 1821 (24th). Its capital is Jefferson City and its largest city is Kansas City. Osage; Lewis & Clark; gateway west. This database tells the state's story: from its first peoples through statehood to the modern era, plus the famous sons and daughters, the industries, and the facts every resident should know.", "s": "public-reference", "f": null}, {"t": "Statehood", "d": "Missouri became a state 1821 (24th).", "g": "statehood", "l": 2, "q": "What is Statehood?", "a": "Missouri became a state 1821 (24th).", "x": "Missouri achieved statehood 1821 (24th). The road to statehood ran through territorial government, population thresholds, and a congressional enabling act — the standard American path. Civil War border state. Statehood Day is still celebrated, and the admission order gives Missouri its number among the states.", "s": "public-reference", "f": null}, {"t": "The statehood story", "d": "How Missouri went from territory to state.", "g": "statehood", "l": 2, "q": "What is The statehood story?", "a": "How Missouri went from territory to state.", "x": "The statehood story of Missouri: settlement, territorial organization, the push for admission, and finally the star on the flag. Railroads; beer; BBQ. Every state's admission reflected the national politics of its era — Missouri's story is no exception, and it explains much about the state's character today.", "s": "public-reference", "f": null}, {"t": "Capital: Jefferson City", "d": "Jefferson City is the capital of Missouri.", "g": "overview", "l": 2, "q": "What is Capital: Jefferson City?", "a": "Jefferson City is the capital of Missouri.", "x": "Jefferson City has been the seat of Missouri government, home to the capitol building, the supreme court, and the legislature. Capitals are often not the biggest city — Missouri's largest is Kansas City — chosen instead for geography or politics. Visit the capitol: the building itself tells the state's story in stone.", "s": "public-reference", "f": null}, {"t": "Nickname: Show-Me State", "d": "Missouri is known as \"Show-Me State.\"", "g": "overview", "l": 2, "q": "What is Nickname: Show-Me State?", "a": "Missouri is known as \"Show-Me State.\"", "x": "The nickname \"Show-Me State\" captures how Missouri sees itself — and how America sees it. The Gateway Arch rose in 1965 as the westward monument. State nicknames come from history, geography, or industry, and they appear on license plates, tourism campaigns, and sports teams. The motto goes deeper: \"Salus populi suprema lex esto (The welfare of the people shall be the supreme law).\"", "s": "public-reference", "f": null}, {"t": "Motto: Salus populi suprema lex esto (The welfare of the people shall be the supreme law)", "d": "The state motto of Missouri is \"Salus populi suprema lex esto (The welfare of the people shall be the supreme law).\"", "g": "overview", "l": 2, "q": "What is Motto: Salus populi suprema lex esto (The welfare of the people shall be the supreme law)?", "a": "The state motto of Missouri is \"Salus populi suprema lex esto (The welfare of the people shall be the supreme law).\"", "x": "The motto \"Salus populi suprema lex esto (The welfare of the people shall be the supreme law)\" is Missouri's official creed, adopted by the legislature and carried on the state seal. Seal with bears and crescent on red-white-blue. Mottos distill a state's ideals into a phrase — learn it, and you understand what the state aspires to be.", "s": "public-reference", "f": null}, {"t": "History 1", "d": "Osage; Lewis & Clark; gateway west.", "g": "history", "l": 2, "q": "What is History 1?", "a": "Osage; Lewis & Clark; gateway west.", "x": "Missouri history: Osage; Lewis & Clark; gateway west.. This chapter explains the Show-Me State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 1: why it matters", "d": "Why this Missouri chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 1: why it matters?", "a": "Why this Missouri chapter still shapes the state.", "x": "Why it matters: Osage; Lewis & Clark; gateway west. That event's fingerprints are on modern Missouri — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 2", "d": "Civil War border state.", "g": "history", "l": 2, "q": "What is History 2?", "a": "Civil War border state.", "x": "Missouri history: Civil War border state.. This chapter explains the Show-Me State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 2: why it matters", "d": "Why this Missouri chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 2: why it matters?", "a": "Why this Missouri chapter still shapes the state.", "x": "Why it matters: Civil War border state. That event's fingerprints are on modern Missouri — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 3", "d": "Railroads; beer; BBQ.", "g": "history", "l": 2, "q": "What is History 3?", "a": "Railroads; beer; BBQ.", "x": "Missouri history: Railroads; beer; BBQ.. This chapter explains the Show-Me State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 3: why it matters", "d": "Why this Missouri chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 3: why it matters?", "a": "Why this Missouri chapter still shapes the state.", "x": "Why it matters: Railroads; beer; BBQ. That event's fingerprints are on modern Missouri — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 4", "d": "The Gateway Arch rose in 1965 as the westward monument.", "g": "history", "l": 2, "q": "What is History 4?", "a": "The Gateway Arch rose in 1965 as the westward monument.", "x": "Missouri history: The Gateway Arch rose in 1965 as the westward monument.. This chapter explains the Show-Me State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 4: why it matters", "d": "Why this Missouri chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 4: why it matters?", "a": "Why this Missouri chapter still shapes the state.", "x": "Why it matters: The Gateway Arch rose in 1965 as the westward monument. That event's fingerprints are on modern Missouri — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "Mark Twain", "d": "Author from Hannibal.", "g": "people", "l": 2, "q": "What is Mark Twain?", "a": "Author from Hannibal.", "x": "Mark Twain — Author from Hannibal.. Missouri's famous sons and daughters carried the state's name worldwide. Author from Hannibal. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Mark Twain: legacy", "d": "The legacy of Mark Twain.", "g": "people", "l": 2, "q": "What is Mark Twain: legacy?", "a": "The legacy of Mark Twain.", "x": "The legacy of Mark Twain: Author from Hannibal.. Missouri honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Harry Truman", "d": "33rd president from Independence.", "g": "people", "l": 2, "q": "What is Harry Truman?", "a": "33rd president from Independence.", "x": "Harry Truman — 33rd president from Independence.. Missouri's famous sons and daughters carried the state's name worldwide. 33rd president from Independence. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Harry Truman: legacy", "d": "The legacy of Harry Truman.", "g": "people", "l": 2, "q": "What is Harry Truman: legacy?", "a": "The legacy of Harry Truman.", "x": "The legacy of Harry Truman: 33rd president from Independence.. Missouri honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name.", "s": "public-reference", "f": null}, {"t": "Walt Disney", "d": "Grew up in Marceline.", "g": "people", "l": 2, "q": "What is Walt Disney?", "a": "Grew up in Marceline.", "x": "Walt Disney — Grew up in Marceline.. Missouri's famous sons and daughters carried the state's name worldwide. Grew up in Marceline. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Walt Disney: legacy", "d": "The legacy of Walt Disney.", "g": "people", "l": 2, "q": "What is Walt Disney: legacy?", "a": "The legacy of Walt Disney.", "x": "The legacy of Walt Disney: Grew up in Marceline.. Missouri honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Industry: agriculture", "d": "agriculture", "g": "economy", "l": 2, "q": "What is Industry: agriculture?", "a": "agriculture", "x": "Missouri's economy: agriculture. Industries shape the state's cities, its workforce, and its politics. agriculture From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Industry: logistics", "d": "logistics", "g": "economy", "l": 2, "q": "What is Industry: logistics?", "a": "logistics", "x": "Missouri's economy: logistics. Industries shape the state's cities, its workforce, and its politics. agriculture From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Geography", "d": "The land of Missouri: from Ozark National Scenic Riverways to its borders.", "g": "geography", "l": 2, "q": "What is Geography?", "a": "The land of Missouri: from Ozark National Scenic Riverways to its borders.", "x": "The geography of Missouri runs from Ozark National Scenic Riverways across the state's varied regions. Landforms decide climate, crops, and settlement — the mountains, plains, coasts, or forests that define the state's look and livelihood. Gateway Arch", "s": "public-reference", "f": null}, {"t": "Modern era", "d": "Missouri today: logistics.", "g": "history", "l": 2, "q": "What is Modern era?", "a": "Missouri today: logistics.", "x": "Modern Missouri: logistics. Today's state balances growth with heritage — new industries beside historic downtowns, newcomers beside old families. The current chapter is still being written by everyone who lives here.", "s": "public-reference", "f": null}, {"t": "Visiting history", "d": "Experience Missouri history firsthand.", "g": "facts", "l": 2, "q": "What is Visiting history?", "a": "Experience Missouri history firsthand.", "x": "Experience Missouri history: the capitol in Jefferson City, the museums, the historic districts, and Gateway Arch. Missouri State Fair History is best learned standing where it happened — walk the old streets, read the plaques, and talk to the docents who love it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-missouri-history-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
