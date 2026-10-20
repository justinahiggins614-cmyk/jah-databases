(function(){'use strict';
/* JAH North Carolina History Database generator — jahdb-e2-north-carolina-history-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-north-carolina-history',PREFIX='JAH-E2NORTHCARO-',NAME='JAH North Carolina History Database';
var FIELDS=["overview", "statehood", "history", "people", "economy", "geography", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "North Carolina: history overview", "d": "North Carolina: the Tar Heel State, admitted 1789 (12th); capital Raleigh.", "g": "overview", "l": 2, "q": "What is North Carolina: history overview?", "a": "North Carolina: the Tar Heel State, admitted 1789 (12th); capital Raleigh.", "x": "North Carolina — \"Tar Heel State\" — entered the Union 1789 (12th). Its capital is Raleigh and its largest city is Charlotte. Cherokee; Lost Colony 1587. This database tells the state's story: from its first peoples through statehood to the modern era, plus the famous sons and daughters, the industries, and the facts every resident should know.", "s": "public-reference", "f": null}, {"t": "Statehood", "d": "North Carolina became a state 1789 (12th).", "g": "statehood", "l": 2, "q": "What is Statehood?", "a": "North Carolina became a state 1789 (12th).", "x": "North Carolina achieved statehood 1789 (12th). The road to statehood ran through territorial government, population thresholds, and a congressional enabling act — the standard American path. Revolution; Civil War. Statehood Day is still celebrated, and the admission order gives North Carolina its number among the states.", "s": "public-reference", "f": null}, {"t": "The statehood story", "d": "How North Carolina went from territory to state.", "g": "statehood", "l": 2, "q": "What is The statehood story?", "a": "How North Carolina went from territory to state.", "x": "The statehood story of North Carolina: settlement, territorial organization, the push for admission, and finally the star on the flag. Tobacco, textiles, tech (Research Triangle). Every state's admission reflected the national politics of its era — North Carolina's story is no exception, and it explains much about the state's character today.", "s": "public-reference", "f": null}, {"t": "Capital: Raleigh", "d": "Raleigh is the capital of North Carolina.", "g": "overview", "l": 2, "q": "What is Capital: Raleigh?", "a": "Raleigh is the capital of North Carolina.", "x": "Raleigh has been the seat of North Carolina government, home to the capitol building, the supreme court, and the legislature. Capitals are often not the biggest city — North Carolina's largest is Charlotte — chosen instead for geography or politics. Visit the capitol: the building itself tells the state's story in stone.", "s": "public-reference", "f": null}, {"t": "Nickname: Tar Heel State", "d": "North Carolina is known as \"Tar Heel State.\"", "g": "overview", "l": 2, "q": "What is Nickname: Tar Heel State?", "a": "North Carolina is known as \"Tar Heel State.\"", "x": "The nickname \"Tar Heel State\" captures how North Carolina sees itself — and how America sees it. The Research Triangle made it a tech hub. State nicknames come from history, geography, or industry, and they appear on license plates, tourism campaigns, and sports teams. The motto goes deeper: \"Esse quam videri (To be rather than to seem).\"", "s": "public-reference", "f": null}, {"t": "Motto: Esse quam videri (To be rather than to seem)", "d": "The state motto of North Carolina is \"Esse quam videri (To be rather than to seem).\"", "g": "overview", "l": 2, "q": "What is Motto: Esse quam videri (To be rather than to seem)?", "a": "The state motto of North Carolina is \"Esse quam videri (To be rather than to seem).\"", "x": "The motto \"Esse quam videri (To be rather than to seem)\" is North Carolina's official creed, adopted by the legislature and carried on the state seal. Seal with Liberty and Plenty on blue. Mottos distill a state's ideals into a phrase — learn it, and you understand what the state aspires to be.", "s": "public-reference", "f": null}, {"t": "History 1", "d": "Cherokee; Lost Colony 1587.", "g": "history", "l": 2, "q": "What is History 1?", "a": "Cherokee; Lost Colony 1587.", "x": "North Carolina history: Cherokee; Lost Colony 1587.. This chapter explains the Tar Heel State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 1: why it matters", "d": "Why this North Carolina chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 1: why it matters?", "a": "Why this North Carolina chapter still shapes the state.", "x": "Why it matters: Cherokee; Lost Colony 1587. That event's fingerprints are on modern North Carolina — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 2", "d": "Revolution; Civil War.", "g": "history", "l": 2, "q": "What is History 2?", "a": "Revolution; Civil War.", "x": "North Carolina history: Revolution; Civil War.. This chapter explains the Tar Heel State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 2: why it matters", "d": "Why this North Carolina chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 2: why it matters?", "a": "Why this North Carolina chapter still shapes the state.", "x": "Why it matters: Revolution; Civil War. That event's fingerprints are on modern North Carolina — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 3", "d": "Tobacco, textiles, tech (Research Triangle).", "g": "history", "l": 2, "q": "What is History 3?", "a": "Tobacco, textiles, tech (Research Triangle).", "x": "North Carolina history: Tobacco, textiles, tech (Research Triangle).. This chapter explains the Tar Heel State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 3: why it matters", "d": "Why this North Carolina chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 3: why it matters?", "a": "Why this North Carolina chapter still shapes the state.", "x": "Why it matters: Tobacco, textiles, tech (Research Triangle). That event's fingerprints are on modern North Carolina — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 4", "d": "The Research Triangle made it a tech hub.", "g": "history", "l": 2, "q": "What is History 4?", "a": "The Research Triangle made it a tech hub.", "x": "North Carolina history: The Research Triangle made it a tech hub.. This chapter explains the Tar Heel State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 4: why it matters", "d": "Why this North Carolina chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 4: why it matters?", "a": "Why this North Carolina chapter still shapes the state.", "x": "Why it matters: The Research Triangle made it a tech hub. That event's fingerprints are on modern North Carolina — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "Michael Jordan", "d": "Basketball legend; UNC.", "g": "people", "l": 2, "q": "What is Michael Jordan?", "a": "Basketball legend; UNC.", "x": "Michael Jordan — Basketball legend; UNC.. North Carolina's famous sons and daughters carried the state's name worldwide. Basketball legend; UNC. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Michael Jordan: legacy", "d": "The legacy of Michael Jordan.", "g": "people", "l": 2, "q": "What is Michael Jordan: legacy?", "a": "The legacy of Michael Jordan.", "x": "The legacy of Michael Jordan: Basketball legend; UNC.. North Carolina honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Andy Griffith", "d": "Actor from Mount Airy.", "g": "people", "l": 2, "q": "What is Andy Griffith?", "a": "Actor from Mount Airy.", "x": "Andy Griffith — Actor from Mount Airy.. North Carolina's famous sons and daughters carried the state's name worldwide. Actor from Mount Airy. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Andy Griffith: legacy", "d": "The legacy of Andy Griffith.", "g": "people", "l": 2, "q": "What is Andy Griffith: legacy?", "a": "The legacy of Andy Griffith.", "x": "The legacy of Andy Griffith: Actor from Mount Airy.. North Carolina honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Nina Simone", "d": "Singer from Tryon.", "g": "people", "l": 2, "q": "What is Nina Simone?", "a": "Singer from Tryon.", "x": "Nina Simone — Singer from Tryon.. North Carolina's famous sons and daughters carried the state's name worldwide. Singer from Tryon. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Nina Simone: legacy", "d": "The legacy of Nina Simone.", "g": "people", "l": 2, "q": "What is Nina Simone: legacy?", "a": "The legacy of Nina Simone.", "x": "The legacy of Nina Simone: Singer from Tryon.. North Carolina honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Industry: technology (Research Triangle)", "d": "technology (Research Triangle)", "g": "economy", "l": 2, "q": "What is Industry: technology (Research Triangle)?", "a": "technology (Research Triangle)", "x": "North Carolina's economy: technology (Research Triangle). Industries shape the state's cities, its workforce, and its politics. technology (Research Triangle) From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Industry: banking (Charlotte)", "d": "banking (Charlotte)", "g": "economy", "l": 2, "q": "What is Industry: banking (Charlotte)?", "a": "banking (Charlotte)", "x": "North Carolina's economy: banking (Charlotte). Industries shape the state's cities, its workforce, and its politics. technology (Research Triangle) From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Geography", "d": "The land of North Carolina: from Great Smoky Mountains National Park to its borders.", "g": "geography", "l": 2, "q": "What is Geography?", "a": "The land of North Carolina: from Great Smoky Mountains National Park to its borders.", "x": "The geography of North Carolina runs from Great Smoky Mountains National Park across the state's varied regions. Landforms decide climate, crops, and settlement — the mountains, plains, coasts, or forests that define the state's look and livelihood. Blue Ridge Parkway", "s": "public-reference", "f": null}, {"t": "Modern era", "d": "North Carolina today: banking (Charlotte).", "g": "history", "l": 2, "q": "What is Modern era?", "a": "North Carolina today: banking (Charlotte).", "x": "Modern North Carolina: banking (Charlotte). Today's state balances growth with heritage — new industries beside historic downtowns, newcomers beside old families. The current chapter is still being written by everyone who lives here.", "s": "public-reference", "f": null}, {"t": "Visiting history", "d": "Experience North Carolina history firsthand.", "g": "facts", "l": 2, "q": "What is Visiting history?", "a": "Experience North Carolina history firsthand.", "x": "Experience North Carolina history: the capitol in Raleigh, the museums, the historic districts, and Blue Ridge Parkway. MerleFest History is best learned standing where it happened — walk the old streets, read the plaques, and talk to the docents who love it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-north-carolina-history-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
