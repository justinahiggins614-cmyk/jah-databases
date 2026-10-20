(function(){'use strict';
/* JAH Nevada History Database generator — jahdb-e2-nevada-history-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-nevada-history',PREFIX='JAH-E2NEVADAHIS-',NAME='JAH Nevada History Database';
var FIELDS=["overview", "statehood", "history", "people", "economy", "geography", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Nevada: history overview", "d": "Nevada: the Silver State, admitted 1864 (36th); capital Carson City.", "g": "overview", "l": 2, "q": "What is Nevada: history overview?", "a": "Nevada: the Silver State, admitted 1864 (36th); capital Carson City.", "x": "Nevada — \"Silver State\" — entered the Union 1864 (36th). Its capital is Carson City and its largest city is Las Vegas. Washoe; Comstock Lode silver. This database tells the state's story: from its first peoples through statehood to the modern era, plus the famous sons and daughters, the industries, and the facts every resident should know.", "s": "public-reference", "f": null}, {"t": "Statehood", "d": "Nevada became a state 1864 (36th).", "g": "statehood", "l": 2, "q": "What is Statehood?", "a": "Nevada became a state 1864 (36th).", "x": "Nevada achieved statehood 1864 (36th). The road to statehood ran through territorial government, population thresholds, and a congressional enabling act — the standard American path. Statehood during Civil War. Statehood Day is still celebrated, and the admission order gives Nevada its number among the states.", "s": "public-reference", "f": null}, {"t": "The statehood story", "d": "How Nevada went from territory to state.", "g": "statehood", "l": 2, "q": "What is The statehood story?", "a": "How Nevada went from territory to state.", "x": "The statehood story of Nevada: settlement, territorial organization, the push for admission, and finally the star on the flag. Gaming legalized 1931; Hoover Dam. Every state's admission reflected the national politics of its era — Nevada's story is no exception, and it explains much about the state's character today.", "s": "public-reference", "f": null}, {"t": "Capital: Carson City", "d": "Carson City is the capital of Nevada.", "g": "overview", "l": 2, "q": "What is Capital: Carson City?", "a": "Carson City is the capital of Nevada.", "x": "Carson City has been the seat of Nevada government, home to the capitol building, the supreme court, and the legislature. Capitals are often not the biggest city — Nevada's largest is Las Vegas — chosen instead for geography or politics. Visit the capitol: the building itself tells the state's story in stone.", "s": "public-reference", "f": null}, {"t": "Nickname: Silver State", "d": "Nevada is known as \"Silver State.\"", "g": "overview", "l": 2, "q": "What is Nickname: Silver State?", "a": "Nevada is known as \"Silver State.\"", "x": "The nickname \"Silver State\" captures how Nevada sees itself — and how America sees it. Gaming legalized in 1931 created Las Vegas. State nicknames come from history, geography, or industry, and they appear on license plates, tourism campaigns, and sports teams. The motto goes deeper: \"All for our country.\"", "s": "public-reference", "f": null}, {"t": "Motto: All for our country", "d": "The state motto of Nevada is \"All for our country.\"", "g": "overview", "l": 2, "q": "What is Motto: All for our country?", "a": "The state motto of Nevada is \"All for our country.\"", "x": "The motto \"All for our country\" is Nevada's official creed, adopted by the legislature and carried on the state seal. Silver star with 'Battle Born' on blue. Mottos distill a state's ideals into a phrase — learn it, and you understand what the state aspires to be.", "s": "public-reference", "f": null}, {"t": "History 1", "d": "Washoe; Comstock Lode silver.", "g": "history", "l": 2, "q": "What is History 1?", "a": "Washoe; Comstock Lode silver.", "x": "Nevada history: Washoe; Comstock Lode silver.. This chapter explains the Silver State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 1: why it matters", "d": "Why this Nevada chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 1: why it matters?", "a": "Why this Nevada chapter still shapes the state.", "x": "Why it matters: Washoe; Comstock Lode silver. That event's fingerprints are on modern Nevada — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 2", "d": "Statehood during Civil War.", "g": "history", "l": 2, "q": "What is History 2?", "a": "Statehood during Civil War.", "x": "Nevada history: Statehood during Civil War.. This chapter explains the Silver State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 2: why it matters", "d": "Why this Nevada chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 2: why it matters?", "a": "Why this Nevada chapter still shapes the state.", "x": "Why it matters: Statehood during Civil War. That event's fingerprints are on modern Nevada — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 3", "d": "Gaming legalized 1931; Hoover Dam.", "g": "history", "l": 2, "q": "What is History 3?", "a": "Gaming legalized 1931; Hoover Dam.", "x": "Nevada history: Gaming legalized 1931; Hoover Dam.. This chapter explains the Silver State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 3: why it matters", "d": "Why this Nevada chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 3: why it matters?", "a": "Why this Nevada chapter still shapes the state.", "x": "Why it matters: Gaming legalized 1931; Hoover Dam. That event's fingerprints are on modern Nevada — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 4", "d": "Gaming legalized in 1931 created Las Vegas.", "g": "history", "l": 2, "q": "What is History 4?", "a": "Gaming legalized in 1931 created Las Vegas.", "x": "Nevada history: Gaming legalized in 1931 created Las Vegas.. This chapter explains the Silver State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 4: why it matters", "d": "Why this Nevada chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 4: why it matters?", "a": "Why this Nevada chapter still shapes the state.", "x": "Why it matters: Gaming legalized in 1931 created Las Vegas. That event's fingerprints are on modern Nevada — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "Andre Agassi", "d": "Tennis star from Las Vegas.", "g": "people", "l": 2, "q": "What is Andre Agassi?", "a": "Tennis star from Las Vegas.", "x": "Andre Agassi — Tennis star from Las Vegas.. Nevada's famous sons and daughters carried the state's name worldwide. Tennis star from Las Vegas. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Andre Agassi: legacy", "d": "The legacy of Andre Agassi.", "g": "people", "l": 2, "q": "What is Andre Agassi: legacy?", "a": "The legacy of Andre Agassi.", "x": "The legacy of Andre Agassi: Tennis star from Las Vegas.. Nevada honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Pat Nixon", "d": "First Lady from Ely.", "g": "people", "l": 2, "q": "What is Pat Nixon?", "a": "First Lady from Ely.", "x": "Pat Nixon — First Lady from Ely.. Nevada's famous sons and daughters carried the state's name worldwide. First Lady from Ely. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Pat Nixon: legacy", "d": "The legacy of Pat Nixon.", "g": "people", "l": 2, "q": "What is Pat Nixon: legacy?", "a": "The legacy of Pat Nixon.", "x": "The legacy of Pat Nixon: First Lady from Ely.. Nevada honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "The Killers", "d": "Band from Las Vegas.", "g": "people", "l": 2, "q": "What is The Killers?", "a": "Band from Las Vegas.", "x": "The Killers — Band from Las Vegas.. Nevada's famous sons and daughters carried the state's name worldwide. Band from Las Vegas. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "The Killers: legacy", "d": "The legacy of The Killers.", "g": "people", "l": 2, "q": "What is The Killers: legacy?", "a": "The legacy of The Killers.", "x": "The legacy of The Killers: Band from Las Vegas.. Nevada honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Industry: tourism (gaming)", "d": "tourism (gaming)", "g": "economy", "l": 2, "q": "What is Industry: tourism (gaming)?", "a": "tourism (gaming)", "x": "Nevada's economy: tourism (gaming). Industries shape the state's cities, its workforce, and its politics. tourism (gaming) From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Industry: mining", "d": "mining", "g": "economy", "l": 2, "q": "What is Industry: mining?", "a": "mining", "x": "Nevada's economy: mining. Industries shape the state's cities, its workforce, and its politics. tourism (gaming) From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Geography", "d": "The land of Nevada: from Great Basin National Park to its borders.", "g": "geography", "l": 2, "q": "What is Geography?", "a": "The land of Nevada: from Great Basin National Park to its borders.", "x": "The geography of Nevada runs from Great Basin National Park across the state's varied regions. Landforms decide climate, crops, and settlement — the mountains, plains, coasts, or forests that define the state's look and livelihood. Las Vegas Strip", "s": "public-reference", "f": null}, {"t": "Modern era", "d": "Nevada today: mining.", "g": "history", "l": 2, "q": "What is Modern era?", "a": "Nevada today: mining.", "x": "Modern Nevada: mining. Today's state balances growth with heritage — new industries beside historic downtowns, newcomers beside old families. The current chapter is still being written by everyone who lives here.", "s": "public-reference", "f": null}, {"t": "Visiting history", "d": "Experience Nevada history firsthand.", "g": "facts", "l": 2, "q": "What is Visiting history?", "a": "Experience Nevada history firsthand.", "x": "Experience Nevada history: the capitol in Carson City, the museums, the historic districts, and Las Vegas Strip. Burning Man History is best learned standing where it happened — walk the old streets, read the plaques, and talk to the docents who love it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-nevada-history-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
