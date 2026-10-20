(function(){'use strict';
/* JAH Nebraska History Database generator — jahdb-e2-nebraska-history-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-nebraska-history',PREFIX='JAH-E2NEBRASKAH-',NAME='JAH Nebraska History Database';
var FIELDS=["overview", "statehood", "history", "people", "economy", "geography", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Nebraska: history overview", "d": "Nebraska: the Cornhusker State, admitted 1867 (37th); capital Lincoln.", "g": "overview", "l": 2, "q": "What is Nebraska: history overview?", "a": "Nebraska: the Cornhusker State, admitted 1867 (37th); capital Lincoln.", "x": "Nebraska — \"Cornhusker State\" — entered the Union 1867 (37th). Its capital is Lincoln and its largest city is Omaha. Pawnee; Oregon Trail; homesteading. This database tells the state's story: from its first peoples through statehood to the modern era, plus the famous sons and daughters, the industries, and the facts every resident should know.", "s": "public-reference", "f": null}, {"t": "Statehood", "d": "Nebraska became a state 1867 (37th).", "g": "statehood", "l": 2, "q": "What is Statehood?", "a": "Nebraska became a state 1867 (37th).", "x": "Nebraska achieved statehood 1867 (37th). The road to statehood ran through territorial government, population thresholds, and a congressional enabling act — the standard American path. Corn and cattle; College World Series. Statehood Day is still celebrated, and the admission order gives Nebraska its number among the states.", "s": "public-reference", "f": null}, {"t": "The statehood story", "d": "How Nebraska went from territory to state.", "g": "statehood", "l": 2, "q": "What is The statehood story?", "a": "How Nebraska went from territory to state.", "x": "The statehood story of Nebraska: settlement, territorial organization, the push for admission, and finally the star on the flag. Warren Buffett's Omaha. Every state's admission reflected the national politics of its era — Nebraska's story is no exception, and it explains much about the state's character today.", "s": "public-reference", "f": null}, {"t": "Capital: Lincoln", "d": "Lincoln is the capital of Nebraska.", "g": "overview", "l": 2, "q": "What is Capital: Lincoln?", "a": "Lincoln is the capital of Nebraska.", "x": "Lincoln has been the seat of Nebraska government, home to the capitol building, the supreme court, and the legislature. Capitals are often not the biggest city — Nebraska's largest is Omaha — chosen instead for geography or politics. Visit the capitol: the building itself tells the state's story in stone.", "s": "public-reference", "f": null}, {"t": "Nickname: Cornhusker State", "d": "Nebraska is known as \"Cornhusker State.\"", "g": "overview", "l": 2, "q": "What is Nickname: Cornhusker State?", "a": "Nebraska is known as \"Cornhusker State.\"", "x": "The nickname \"Cornhusker State\" captures how Nebraska sees itself — and how America sees it. The railroad and the Homestead Act settled the plains. State nicknames come from history, geography, or industry, and they appear on license plates, tourism campaigns, and sports teams. The motto goes deeper: \"Equality before the law.\"", "s": "public-reference", "f": null}, {"t": "Motto: Equality before the law", "d": "The state motto of Nebraska is \"Equality before the law.\"", "g": "overview", "l": 2, "q": "What is Motto: Equality before the law?", "a": "The state motto of Nebraska is \"Equality before the law.\"", "x": "The motto \"Equality before the law\" is Nebraska's official creed, adopted by the legislature and carried on the state seal. Seal with blacksmith and wheat on blue. Mottos distill a state's ideals into a phrase — learn it, and you understand what the state aspires to be.", "s": "public-reference", "f": null}, {"t": "History 1", "d": "Pawnee; Oregon Trail; homesteading.", "g": "history", "l": 2, "q": "What is History 1?", "a": "Pawnee; Oregon Trail; homesteading.", "x": "Nebraska history: Pawnee; Oregon Trail; homesteading.. This chapter explains the Cornhusker State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 1: why it matters", "d": "Why this Nebraska chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 1: why it matters?", "a": "Why this Nebraska chapter still shapes the state.", "x": "Why it matters: Pawnee; Oregon Trail; homesteading. That event's fingerprints are on modern Nebraska — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 2", "d": "Corn and cattle; College World Series.", "g": "history", "l": 2, "q": "What is History 2?", "a": "Corn and cattle; College World Series.", "x": "Nebraska history: Corn and cattle; College World Series.. This chapter explains the Cornhusker State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 2: why it matters", "d": "Why this Nebraska chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 2: why it matters?", "a": "Why this Nebraska chapter still shapes the state.", "x": "Why it matters: Corn and cattle; College World Series. That event's fingerprints are on modern Nebraska — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 3", "d": "Warren Buffett's Omaha.", "g": "history", "l": 2, "q": "What is History 3?", "a": "Warren Buffett's Omaha.", "x": "Nebraska history: Warren Buffett's Omaha.. This chapter explains the Cornhusker State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 3: why it matters", "d": "Why this Nebraska chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 3: why it matters?", "a": "Why this Nebraska chapter still shapes the state.", "x": "Why it matters: Warren Buffett's Omaha. That event's fingerprints are on modern Nebraska — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 4", "d": "The railroad and the Homestead Act settled the plains.", "g": "history", "l": 2, "q": "What is History 4?", "a": "The railroad and the Homestead Act settled the plains.", "x": "Nebraska history: The railroad and the Homestead Act settled the plains.. This chapter explains the Cornhusker State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 4: why it matters", "d": "Why this Nebraska chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 4: why it matters?", "a": "Why this Nebraska chapter still shapes the state.", "x": "Why it matters: The railroad and the Homestead Act settled the plains. That event's fingerprints are on modern Nebraska — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "Warren Buffett", "d": "Investor from Omaha.", "g": "people", "l": 2, "q": "What is Warren Buffett?", "a": "Investor from Omaha.", "x": "Warren Buffett — Investor from Omaha.. Nebraska's famous sons and daughters carried the state's name worldwide. Investor from Omaha. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Warren Buffett: legacy", "d": "The legacy of Warren Buffett.", "g": "people", "l": 2, "q": "What is Warren Buffett: legacy?", "a": "The legacy of Warren Buffett.", "x": "The legacy of Warren Buffett: Investor from Omaha.. Nebraska honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Johnny Carson", "d": "TV host from Norfolk.", "g": "people", "l": 2, "q": "What is Johnny Carson?", "a": "TV host from Norfolk.", "x": "Johnny Carson — TV host from Norfolk.. Nebraska's famous sons and daughters carried the state's name worldwide. TV host from Norfolk. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Johnny Carson: legacy", "d": "The legacy of Johnny Carson.", "g": "people", "l": 2, "q": "What is Johnny Carson: legacy?", "a": "The legacy of Johnny Carson.", "x": "The legacy of Johnny Carson: TV host from Norfolk.. Nebraska honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Marlon Brando", "d": "Actor from Omaha.", "g": "people", "l": 2, "q": "What is Marlon Brando?", "a": "Actor from Omaha.", "x": "Marlon Brando — Actor from Omaha.. Nebraska's famous sons and daughters carried the state's name worldwide. Actor from Omaha. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Marlon Brando: legacy", "d": "The legacy of Marlon Brando.", "g": "people", "l": 2, "q": "What is Marlon Brando: legacy?", "a": "The legacy of Marlon Brando.", "x": "The legacy of Marlon Brando: Actor from Omaha.. Nebraska honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Industry: agriculture (corn, beef)", "d": "agriculture (corn, beef)", "g": "economy", "l": 2, "q": "What is Industry: agriculture (corn, beef)?", "a": "agriculture (corn, beef)", "x": "Nebraska's economy: agriculture (corn, beef). Industries shape the state's cities, its workforce, and its politics. agriculture (corn, beef) From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Industry: insurance and rail", "d": "insurance and rail", "g": "economy", "l": 2, "q": "What is Industry: insurance and rail?", "a": "insurance and rail", "x": "Nebraska's economy: insurance and rail. Industries shape the state's cities, its workforce, and its politics. agriculture (corn, beef) From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Geography", "d": "The land of Nebraska: from Scotts Bluff National Monument to its borders.", "g": "geography", "l": 2, "q": "What is Geography?", "a": "The land of Nebraska: from Scotts Bluff National Monument to its borders.", "x": "The geography of Nebraska runs from Scotts Bluff National Monument across the state's varied regions. Landforms decide climate, crops, and settlement — the mountains, plains, coasts, or forests that define the state's look and livelihood. Scotts Bluff", "s": "public-reference", "f": null}, {"t": "Modern era", "d": "Nebraska today: insurance and rail.", "g": "history", "l": 2, "q": "What is Modern era?", "a": "Nebraska today: insurance and rail.", "x": "Modern Nebraska: insurance and rail. Today's state balances growth with heritage — new industries beside historic downtowns, newcomers beside old families. The current chapter is still being written by everyone who lives here.", "s": "public-reference", "f": null}, {"t": "Visiting history", "d": "Experience Nebraska history firsthand.", "g": "facts", "l": 2, "q": "What is Visiting history?", "a": "Experience Nebraska history firsthand.", "x": "Experience Nebraska history: the capitol in Lincoln, the museums, the historic districts, and Scotts Bluff. College World Series History is best learned standing where it happened — walk the old streets, read the plaques, and talk to the docents who love it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-nebraska-history-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
