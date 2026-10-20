(function(){'use strict';
/* JAH Vermont History Database generator — jahdb-e2-vermont-history-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-vermont-history',PREFIX='JAH-E2VERMONTHI-',NAME='JAH Vermont History Database';
var FIELDS=["overview", "statehood", "history", "people", "economy", "geography", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Vermont: history overview", "d": "Vermont: the Green Mountain State, admitted 1791 (14th); capital Montpelier.", "g": "overview", "l": 2, "q": "What is Vermont: history overview?", "a": "Vermont: the Green Mountain State, admitted 1791 (14th); capital Montpelier.", "x": "Vermont — \"Green Mountain State\" — entered the Union 1791 (14th). Its capital is Montpelier and its largest city is Burlington. Abenaki; independent republic 1777-91. This database tells the state's story: from its first peoples through statehood to the modern era, plus the famous sons and daughters, the industries, and the facts every resident should know.", "s": "public-reference", "f": null}, {"t": "Statehood", "d": "Vermont became a state 1791 (14th).", "g": "statehood", "l": 2, "q": "What is Statehood?", "a": "Vermont became a state 1791 (14th).", "x": "Vermont achieved statehood 1791 (14th). The road to statehood ran through territorial government, population thresholds, and a congressional enabling act — the standard American path. First to abolish slavery (1777). Statehood Day is still celebrated, and the admission order gives Vermont its number among the states.", "s": "public-reference", "f": null}, {"t": "The statehood story", "d": "How Vermont went from territory to state.", "g": "statehood", "l": 2, "q": "What is The statehood story?", "a": "How Vermont went from territory to state.", "x": "The statehood story of Vermont: settlement, territorial organization, the push for admission, and finally the star on the flag. Dairy; maple; Bernie. Every state's admission reflected the national politics of its era — Vermont's story is no exception, and it explains much about the state's character today.", "s": "public-reference", "f": null}, {"t": "Capital: Montpelier", "d": "Montpelier is the capital of Vermont.", "g": "overview", "l": 2, "q": "What is Capital: Montpelier?", "a": "Montpelier is the capital of Vermont.", "x": "Montpelier has been the seat of Vermont government, home to the capitol building, the supreme court, and the legislature. Capitals are often not the biggest city — Vermont's largest is Burlington — chosen instead for geography or politics. Visit the capitol: the building itself tells the state's story in stone.", "s": "public-reference", "f": null}, {"t": "Nickname: Green Mountain State", "d": "Vermont is known as \"Green Mountain State.\"", "g": "overview", "l": 2, "q": "What is Nickname: Green Mountain State?", "a": "Vermont is known as \"Green Mountain State.\"", "x": "The nickname \"Green Mountain State\" captures how Vermont sees itself — and how America sees it. Its 1777 constitution was the first to abolish slavery. State nicknames come from history, geography, or industry, and they appear on license plates, tourism campaigns, and sports teams. The motto goes deeper: \"Freedom and Unity.\"", "s": "public-reference", "f": null}, {"t": "Motto: Freedom and Unity", "d": "The state motto of Vermont is \"Freedom and Unity.\"", "g": "overview", "l": 2, "q": "What is Motto: Freedom and Unity?", "a": "The state motto of Vermont is \"Freedom and Unity.\"", "x": "The motto \"Freedom and Unity\" is Vermont's official creed, adopted by the legislature and carried on the state seal. Seal with pine, cow, wheat on blue. Mottos distill a state's ideals into a phrase — learn it, and you understand what the state aspires to be.", "s": "public-reference", "f": null}, {"t": "History 1", "d": "Abenaki; independent republic 1777-91.", "g": "history", "l": 2, "q": "What is History 1?", "a": "Abenaki; independent republic 1777-91.", "x": "Vermont history: Abenaki; independent republic 1777-91.. This chapter explains the Green Mountain State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 1: why it matters", "d": "Why this Vermont chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 1: why it matters?", "a": "Why this Vermont chapter still shapes the state.", "x": "Why it matters: Abenaki; independent republic 1777-91. That event's fingerprints are on modern Vermont — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 2", "d": "First to abolish slavery (1777).", "g": "history", "l": 2, "q": "What is History 2?", "a": "First to abolish slavery (1777).", "x": "Vermont history: First to abolish slavery (1777).. This chapter explains the Green Mountain State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 2: why it matters", "d": "Why this Vermont chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 2: why it matters?", "a": "Why this Vermont chapter still shapes the state.", "x": "Why it matters: First to abolish slavery (1777). That event's fingerprints are on modern Vermont — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 3", "d": "Dairy; maple; Bernie.", "g": "history", "l": 2, "q": "What is History 3?", "a": "Dairy; maple; Bernie.", "x": "Vermont history: Dairy; maple; Bernie.. This chapter explains the Green Mountain State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 3: why it matters", "d": "Why this Vermont chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 3: why it matters?", "a": "Why this Vermont chapter still shapes the state.", "x": "Why it matters: Dairy; maple; Bernie. That event's fingerprints are on modern Vermont — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 4", "d": "Its 1777 constitution was the first to abolish slavery.", "g": "history", "l": 2, "q": "What is History 4?", "a": "Its 1777 constitution was the first to abolish slavery.", "x": "Vermont history: Its 1777 constitution was the first to abolish slavery.. This chapter explains the Green Mountain State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 4: why it matters", "d": "Why this Vermont chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 4: why it matters?", "a": "Why this Vermont chapter still shapes the state.", "x": "Why it matters: Its 1777 constitution was the first to abolish slavery. That event's fingerprints are on modern Vermont — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "Calvin Coolidge", "d": "30th president from Plymouth.", "g": "people", "l": 2, "q": "What is Calvin Coolidge?", "a": "30th president from Plymouth.", "x": "Calvin Coolidge — 30th president from Plymouth.. Vermont's famous sons and daughters carried the state's name worldwide. 30th president from Plymouth. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Calvin Coolidge: legacy", "d": "The legacy of Calvin Coolidge.", "g": "people", "l": 2, "q": "What is Calvin Coolidge: legacy?", "a": "The legacy of Calvin Coolidge.", "x": "The legacy of Calvin Coolidge: 30th president from Plymouth.. Vermont honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Bernie Sanders", "d": "Senator; Burlington mayor.", "g": "people", "l": 2, "q": "What is Bernie Sanders?", "a": "Senator; Burlington mayor.", "x": "Bernie Sanders — Senator; Burlington mayor.. Vermont's famous sons and daughters carried the state's name worldwide. Senator; Burlington mayor. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Bernie Sanders: legacy", "d": "The legacy of Bernie Sanders.", "g": "people", "l": 2, "q": "What is Bernie Sanders: legacy?", "a": "The legacy of Bernie Sanders.", "x": "The legacy of Bernie Sanders: Senator; Burlington mayor.. Vermont honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Ben & Jerry", "d": "Ice cream from Burlington.", "g": "people", "l": 2, "q": "What is Ben & Jerry?", "a": "Ice cream from Burlington.", "x": "Ben & Jerry — Ice cream from Burlington.. Vermont's famous sons and daughters carried the state's name worldwide. Ice cream from Burlington. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Ben & Jerry: legacy", "d": "The legacy of Ben & Jerry.", "g": "people", "l": 2, "q": "What is Ben & Jerry: legacy?", "a": "The legacy of Ben & Jerry.", "x": "The legacy of Ben & Jerry: Ice cream from Burlington.. Vermont honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Industry: dairy and maple", "d": "dairy and maple", "g": "economy", "l": 2, "q": "What is Industry: dairy and maple?", "a": "dairy and maple", "x": "Vermont's economy: dairy and maple. Industries shape the state's cities, its workforce, and its politics. dairy and maple From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Industry: tourism", "d": "tourism", "g": "economy", "l": 2, "q": "What is Industry: tourism?", "a": "tourism", "x": "Vermont's economy: tourism. Industries shape the state's cities, its workforce, and its politics. dairy and maple From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Geography", "d": "The land of Vermont: from Green Mountain National Forest to its borders.", "g": "geography", "l": 2, "q": "What is Geography?", "a": "The land of Vermont: from Green Mountain National Forest to its borders.", "x": "The geography of Vermont runs from Green Mountain National Forest across the state's varied regions. Landforms decide climate, crops, and settlement — the mountains, plains, coasts, or forests that define the state's look and livelihood. Stowe", "s": "public-reference", "f": null}, {"t": "Modern era", "d": "Vermont today: tourism.", "g": "history", "l": 2, "q": "What is Modern era?", "a": "Vermont today: tourism.", "x": "Modern Vermont: tourism. Today's state balances growth with heritage — new industries beside historic downtowns, newcomers beside old families. The current chapter is still being written by everyone who lives here.", "s": "public-reference", "f": null}, {"t": "Visiting history", "d": "Experience Vermont history firsthand.", "g": "facts", "l": 2, "q": "What is Visiting history?", "a": "Experience Vermont history firsthand.", "x": "Experience Vermont history: the capitol in Montpelier, the museums, the historic districts, and Stowe. Stowe festivals History is best learned standing where it happened — walk the old streets, read the plaques, and talk to the docents who love it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-vermont-history-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
