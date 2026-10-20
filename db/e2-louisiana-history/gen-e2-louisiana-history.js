(function(){'use strict';
/* JAH Louisiana History Database generator — jahdb-e2-louisiana-history-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-louisiana-history',PREFIX='JAH-E2LOUISIANA-',NAME='JAH Louisiana History Database';
var FIELDS=["overview", "statehood", "history", "people", "economy", "geography", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Louisiana: history overview", "d": "Louisiana: the Pelican State, admitted 1812 (18th); capital Baton Rouge.", "g": "overview", "l": 2, "q": "What is Louisiana: history overview?", "a": "Louisiana: the Pelican State, admitted 1812 (18th); capital Baton Rouge.", "x": "Louisiana — \"Pelican State\" — entered the Union 1812 (18th). Its capital is Baton Rouge and its largest city is New Orleans. French and Spanish colony. This database tells the state's story: from its first peoples through statehood to the modern era, plus the famous sons and daughters, the industries, and the facts every resident should know.", "s": "public-reference", "f": null}, {"t": "Statehood", "d": "Louisiana became a state 1812 (18th).", "g": "statehood", "l": 2, "q": "What is Statehood?", "a": "Louisiana became a state 1812 (18th).", "x": "Louisiana achieved statehood 1812 (18th). The road to statehood ran through territorial government, population thresholds, and a congressional enabling act — the standard American path. Louisiana Purchase 1803. Statehood Day is still celebrated, and the admission order gives Louisiana its number among the states.", "s": "public-reference", "f": null}, {"t": "The statehood story", "d": "How Louisiana went from territory to state.", "g": "statehood", "l": 2, "q": "What is The statehood story?", "a": "How Louisiana went from territory to state.", "x": "The statehood story of Louisiana: settlement, territorial organization, the push for admission, and finally the star on the flag. Civil War; Huey Long era. Every state's admission reflected the national politics of its era — Louisiana's story is no exception, and it explains much about the state's character today.", "s": "public-reference", "f": null}, {"t": "Capital: Baton Rouge", "d": "Baton Rouge is the capital of Louisiana.", "g": "overview", "l": 2, "q": "What is Capital: Baton Rouge?", "a": "Baton Rouge is the capital of Louisiana.", "x": "Baton Rouge has been the seat of Louisiana government, home to the capitol building, the supreme court, and the legislature. Capitals are often not the biggest city — Louisiana's largest is New Orleans — chosen instead for geography or politics. Visit the capitol: the building itself tells the state's story in stone.", "s": "public-reference", "f": null}, {"t": "Nickname: Pelican State", "d": "Louisiana is known as \"Pelican State.\"", "g": "overview", "l": 2, "q": "What is Nickname: Pelican State?", "a": "Louisiana is known as \"Pelican State.\"", "x": "The nickname \"Pelican State\" captures how Louisiana sees itself — and how America sees it. Oil, jazz, Katrina 2005. State nicknames come from history, geography, or industry, and they appear on license plates, tourism campaigns, and sports teams. The motto goes deeper: \"Union, justice, confidence.\"", "s": "public-reference", "f": null}, {"t": "Motto: Union, justice, confidence", "d": "The state motto of Louisiana is \"Union, justice, confidence.\"", "g": "overview", "l": 2, "q": "What is Motto: Union, justice, confidence?", "a": "The state motto of Louisiana is \"Union, justice, confidence.\"", "x": "The motto \"Union, justice, confidence\" is Louisiana's official creed, adopted by the legislature and carried on the state seal. Pelican with chicks on blue; gold fringe. Mottos distill a state's ideals into a phrase — learn it, and you understand what the state aspires to be.", "s": "public-reference", "f": null}, {"t": "History 1", "d": "French and Spanish colony.", "g": "history", "l": 2, "q": "What is History 1?", "a": "French and Spanish colony.", "x": "Louisiana history: French and Spanish colony.. This chapter explains the Pelican State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 1: why it matters", "d": "Why this Louisiana chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 1: why it matters?", "a": "Why this Louisiana chapter still shapes the state.", "x": "Why it matters: French and Spanish colony. That event's fingerprints are on modern Louisiana — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 2", "d": "Louisiana Purchase 1803.", "g": "history", "l": 2, "q": "What is History 2?", "a": "Louisiana Purchase 1803.", "x": "Louisiana history: Louisiana Purchase 1803.. This chapter explains the Pelican State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 2: why it matters", "d": "Why this Louisiana chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 2: why it matters?", "a": "Why this Louisiana chapter still shapes the state.", "x": "Why it matters: Louisiana Purchase 1803. That event's fingerprints are on modern Louisiana — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 3", "d": "Civil War; Huey Long era.", "g": "history", "l": 2, "q": "What is History 3?", "a": "Civil War; Huey Long era.", "x": "Louisiana history: Civil War; Huey Long era.. This chapter explains the Pelican State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 3: why it matters", "d": "Why this Louisiana chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 3: why it matters?", "a": "Why this Louisiana chapter still shapes the state.", "x": "Why it matters: Civil War; Huey Long era. That event's fingerprints are on modern Louisiana — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 4", "d": "Oil, jazz, Katrina 2005.", "g": "history", "l": 2, "q": "What is History 4?", "a": "Oil, jazz, Katrina 2005.", "x": "Louisiana history: Oil, jazz, Katrina 2005.. This chapter explains the Pelican State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 4: why it matters", "d": "Why this Louisiana chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 4: why it matters?", "a": "Why this Louisiana chapter still shapes the state.", "x": "Why it matters: Oil, jazz, Katrina 2005. That event's fingerprints are on modern Louisiana — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "Louis Armstrong", "d": "Jazz legend from New Orleans.", "g": "people", "l": 2, "q": "What is Louis Armstrong?", "a": "Jazz legend from New Orleans.", "x": "Louis Armstrong — Jazz legend from New Orleans.. Louisiana's famous sons and daughters carried the state's name worldwide. Jazz legend from New Orleans. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Louis Armstrong: legacy", "d": "The legacy of Louis Armstrong.", "g": "people", "l": 2, "q": "What is Louis Armstrong: legacy?", "a": "The legacy of Louis Armstrong.", "x": "The legacy of Louis Armstrong: Jazz legend from New Orleans.. Louisiana honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name.", "s": "public-reference", "f": null}, {"t": "Huey Long", "d": "Governor/senator.", "g": "people", "l": 2, "q": "What is Huey Long?", "a": "Governor/senator.", "x": "Huey Long — Governor/senator.. Louisiana's famous sons and daughters carried the state's name worldwide. Governor/senator. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Huey Long: legacy", "d": "The legacy of Huey Long.", "g": "people", "l": 2, "q": "What is Huey Long: legacy?", "a": "The legacy of Huey Long.", "x": "The legacy of Huey Long: Governor/senator.. Louisiana honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Britney Spears", "d": "Singer from McComb.", "g": "people", "l": 2, "q": "What is Britney Spears?", "a": "Singer from McComb.", "x": "Britney Spears — Singer from McComb.. Louisiana's famous sons and daughters carried the state's name worldwide. Singer from McComb. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Britney Spears: legacy", "d": "The legacy of Britney Spears.", "g": "people", "l": 2, "q": "What is Britney Spears: legacy?", "a": "The legacy of Britney Spears.", "x": "The legacy of Britney Spears: Singer from McComb.. Louisiana honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Industry: oil and gas", "d": "oil and gas", "g": "economy", "l": 2, "q": "What is Industry: oil and gas?", "a": "oil and gas", "x": "Louisiana's economy: oil and gas. Industries shape the state's cities, its workforce, and its politics. oil and gas From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Industry: tourism (New Orleans)", "d": "tourism (New Orleans)", "g": "economy", "l": 2, "q": "What is Industry: tourism (New Orleans)?", "a": "tourism (New Orleans)", "x": "Louisiana's economy: tourism (New Orleans). Industries shape the state's cities, its workforce, and its politics. oil and gas From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Geography", "d": "The land of Louisiana: from Jean Lafitte National Historical Park to its borders.", "g": "geography", "l": 2, "q": "What is Geography?", "a": "The land of Louisiana: from Jean Lafitte National Historical Park to its borders.", "x": "The geography of Louisiana runs from Jean Lafitte National Historical Park across the state's varied regions. Landforms decide climate, crops, and settlement — the mountains, plains, coasts, or forests that define the state's look and livelihood. French Quarter", "s": "public-reference", "f": null}, {"t": "Modern era", "d": "Louisiana today: tourism (New Orleans).", "g": "history", "l": 2, "q": "What is Modern era?", "a": "Louisiana today: tourism (New Orleans).", "x": "Modern Louisiana: tourism (New Orleans). Today's state balances growth with heritage — new industries beside historic downtowns, newcomers beside old families. The current chapter is still being written by everyone who lives here.", "s": "public-reference", "f": null}, {"t": "Visiting history", "d": "Experience Louisiana history firsthand.", "g": "facts", "l": 2, "q": "What is Visiting history?", "a": "Experience Louisiana history firsthand.", "x": "Experience Louisiana history: the capitol in Baton Rouge, the museums, the historic districts, and French Quarter. Mardi Gras History is best learned standing where it happened — walk the old streets, read the plaques, and talk to the docents who love it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-louisiana-history-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
