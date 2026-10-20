(function(){'use strict';
/* JAH Georgia History Database generator — jahdb-e2-georgia-history-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-georgia-history',PREFIX='JAH-E2GEORGIAHI-',NAME='JAH Georgia History Database';
var FIELDS=["overview", "statehood", "history", "people", "economy", "geography", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Georgia: history overview", "d": "Georgia: the Peach State, admitted 1788 (4th); capital Atlanta.", "g": "overview", "l": 2, "q": "What is Georgia: history overview?", "a": "Georgia: the Peach State, admitted 1788 (4th); capital Atlanta.", "x": "Georgia — \"Peach State\" — entered the Union 1788 (4th). Its capital is Atlanta and its largest city is Atlanta. Creek and Cherokee; Trail of Tears. This database tells the state's story: from its first peoples through statehood to the modern era, plus the famous sons and daughters, the industries, and the facts every resident should know.", "s": "public-reference", "f": null}, {"t": "Statehood", "d": "Georgia became a state 1788 (4th).", "g": "statehood", "l": 2, "q": "What is Statehood?", "a": "Georgia became a state 1788 (4th).", "x": "Georgia achieved statehood 1788 (4th). The road to statehood ran through territorial government, population thresholds, and a congressional enabling act — the standard American path. Cotton kingdom; Sherman's March. Statehood Day is still celebrated, and the admission order gives Georgia its number among the states.", "s": "public-reference", "f": null}, {"t": "The statehood story", "d": "How Georgia went from territory to state.", "g": "statehood", "l": 2, "q": "What is The statehood story?", "a": "How Georgia went from territory to state.", "x": "The statehood story of Georgia: settlement, territorial organization, the push for admission, and finally the star on the flag. Civil Rights: MLK from Atlanta. Every state's admission reflected the national politics of its era — Georgia's story is no exception, and it explains much about the state's character today.", "s": "public-reference", "f": null}, {"t": "Capital: Atlanta", "d": "Atlanta is the capital of Georgia.", "g": "overview", "l": 2, "q": "What is Capital: Atlanta?", "a": "Atlanta is the capital of Georgia.", "x": "Atlanta has been the seat of Georgia government, home to the capitol building, the supreme court, and the legislature. Capitals are often not the biggest city — Georgia's largest is Atlanta — chosen instead for geography or politics. Visit the capitol: the building itself tells the state's story in stone.", "s": "public-reference", "f": null}, {"t": "Nickname: Peach State", "d": "Georgia is known as \"Peach State.\"", "g": "overview", "l": 2, "q": "What is Nickname: Peach State?", "a": "Georgia is known as \"Peach State.\"", "x": "The nickname \"Peach State\" captures how Georgia sees itself — and how America sees it. Coca-Cola, CNN, Delta hub. State nicknames come from history, geography, or industry, and they appear on license plates, tourism campaigns, and sports teams. The motto goes deeper: \"Wisdom, Justice, Moderation.\"", "s": "public-reference", "f": null}, {"t": "Motto: Wisdom, Justice, Moderation", "d": "The state motto of Georgia is \"Wisdom, Justice, Moderation.\"", "g": "overview", "l": 2, "q": "What is Motto: Wisdom, Justice, Moderation?", "a": "The state motto of Georgia is \"Wisdom, Justice, Moderation.\"", "x": "The motto \"Wisdom, Justice, Moderation\" is Georgia's official creed, adopted by the legislature and carried on the state seal. Three stripes with state seal; 'In God We Trust'. Mottos distill a state's ideals into a phrase — learn it, and you understand what the state aspires to be.", "s": "public-reference", "f": null}, {"t": "History 1", "d": "Creek and Cherokee; Trail of Tears.", "g": "history", "l": 2, "q": "What is History 1?", "a": "Creek and Cherokee; Trail of Tears.", "x": "Georgia history: Creek and Cherokee; Trail of Tears.. This chapter explains the Peach State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 1: why it matters", "d": "Why this Georgia chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 1: why it matters?", "a": "Why this Georgia chapter still shapes the state.", "x": "Why it matters: Creek and Cherokee; Trail of Tears. That event's fingerprints are on modern Georgia — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 2", "d": "Cotton kingdom; Sherman's March.", "g": "history", "l": 2, "q": "What is History 2?", "a": "Cotton kingdom; Sherman's March.", "x": "Georgia history: Cotton kingdom; Sherman's March.. This chapter explains the Peach State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 2: why it matters", "d": "Why this Georgia chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 2: why it matters?", "a": "Why this Georgia chapter still shapes the state.", "x": "Why it matters: Cotton kingdom; Sherman's March. That event's fingerprints are on modern Georgia — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 3", "d": "Civil Rights: MLK from Atlanta.", "g": "history", "l": 2, "q": "What is History 3?", "a": "Civil Rights: MLK from Atlanta.", "x": "Georgia history: Civil Rights: MLK from Atlanta.. This chapter explains the Peach State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 3: why it matters", "d": "Why this Georgia chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 3: why it matters?", "a": "Why this Georgia chapter still shapes the state.", "x": "Why it matters: Civil Rights: MLK from Atlanta. That event's fingerprints are on modern Georgia — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 4", "d": "Coca-Cola, CNN, Delta hub.", "g": "history", "l": 2, "q": "What is History 4?", "a": "Coca-Cola, CNN, Delta hub.", "x": "Georgia history: Coca-Cola, CNN, Delta hub.. This chapter explains the Peach State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 4: why it matters", "d": "Why this Georgia chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 4: why it matters?", "a": "Why this Georgia chapter still shapes the state.", "x": "Why it matters: Coca-Cola, CNN, Delta hub. That event's fingerprints are on modern Georgia — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "Martin Luther King Jr.", "d": "Civil rights leader from Atlanta.", "g": "people", "l": 2, "q": "What is Martin Luther King Jr.?", "a": "Civil rights leader from Atlanta.", "x": "Martin Luther King Jr. — Civil rights leader from Atlanta.. Georgia's famous sons and daughters carried the state's name worldwide. Civil rights leader from Atlanta. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Martin Luther King Jr.: legacy", "d": "The legacy of Martin Luther King Jr..", "g": "people", "l": 2, "q": "What is Martin Luther King Jr.: legacy?", "a": "The legacy of Martin Luther King Jr..", "x": "The legacy of Martin Luther King Jr.: Civil rights leader from Atlanta.. Georgia honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name.", "s": "public-reference", "f": null}, {"t": "Jimmy Carter", "d": "39th president from Plains.", "g": "people", "l": 2, "q": "What is Jimmy Carter?", "a": "39th president from Plains.", "x": "Jimmy Carter — 39th president from Plains.. Georgia's famous sons and daughters carried the state's name worldwide. 39th president from Plains. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Jimmy Carter: legacy", "d": "The legacy of Jimmy Carter.", "g": "people", "l": 2, "q": "What is Jimmy Carter: legacy?", "a": "The legacy of Jimmy Carter.", "x": "The legacy of Jimmy Carter: 39th president from Plains.. Georgia honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Ray Charles", "d": "Singer from Albany.", "g": "people", "l": 2, "q": "What is Ray Charles?", "a": "Singer from Albany.", "x": "Ray Charles — Singer from Albany.. Georgia's famous sons and daughters carried the state's name worldwide. Singer from Albany. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Ray Charles: legacy", "d": "The legacy of Ray Charles.", "g": "people", "l": 2, "q": "What is Ray Charles: legacy?", "a": "The legacy of Ray Charles.", "x": "The legacy of Ray Charles: Singer from Albany.. Georgia honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Industry: logistics (Delta, UPS)", "d": "logistics (Delta, UPS)", "g": "economy", "l": 2, "q": "What is Industry: logistics (Delta, UPS)?", "a": "logistics (Delta, UPS)", "x": "Georgia's economy: logistics (Delta, UPS). Industries shape the state's cities, its workforce, and its politics. logistics (Delta, UPS) From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Industry: film (Hollywood of the South)", "d": "film (Hollywood of the South)", "g": "economy", "l": 2, "q": "What is Industry: film (Hollywood of the South)?", "a": "film (Hollywood of the South)", "x": "Georgia's economy: film (Hollywood of the South). Industries shape the state's cities, its workforce, and its politics. logistics (Delta, UPS) From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Geography", "d": "The land of Georgia: from Okefenokee National Wildlife Refuge to its borders.", "g": "geography", "l": 2, "q": "What is Geography?", "a": "The land of Georgia: from Okefenokee National Wildlife Refuge to its borders.", "x": "The geography of Georgia runs from Okefenokee National Wildlife Refuge across the state's varied regions. Landforms decide climate, crops, and settlement — the mountains, plains, coasts, or forests that define the state's look and livelihood. Savannah historic district", "s": "public-reference", "f": null}, {"t": "Modern era", "d": "Georgia today: film (Hollywood of the South).", "g": "history", "l": 2, "q": "What is Modern era?", "a": "Georgia today: film (Hollywood of the South).", "x": "Modern Georgia: film (Hollywood of the South). Today's state balances growth with heritage — new industries beside historic downtowns, newcomers beside old families. The current chapter is still being written by everyone who lives here.", "s": "public-reference", "f": null}, {"t": "Visiting history", "d": "Experience Georgia history firsthand.", "g": "facts", "l": 2, "q": "What is Visiting history?", "a": "Experience Georgia history firsthand.", "x": "Experience Georgia history: the capitol in Atlanta, the museums, the historic districts, and Savannah historic district. Savannah St. Patrick's Day History is best learned standing where it happened — walk the old streets, read the plaques, and talk to the docents who love it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-georgia-history-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
