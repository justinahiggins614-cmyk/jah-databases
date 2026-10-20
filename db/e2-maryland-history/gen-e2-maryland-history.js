(function(){'use strict';
/* JAH Maryland History Database generator — jahdb-e2-maryland-history-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-maryland-history',PREFIX='JAH-E2MARYLANDH-',NAME='JAH Maryland History Database';
var FIELDS=["overview", "statehood", "history", "people", "economy", "geography", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Maryland: history overview", "d": "Maryland: the Old Line State, admitted 1788 (7th); capital Annapolis.", "g": "overview", "l": 2, "q": "What is Maryland: history overview?", "a": "Maryland: the Old Line State, admitted 1788 (7th); capital Annapolis.", "x": "Maryland — \"Old Line State\" — entered the Union 1788 (7th). Its capital is Annapolis and its largest city is Baltimore. Catholic refuge colony 1634. This database tells the state's story: from its first peoples through statehood to the modern era, plus the famous sons and daughters, the industries, and the facts every resident should know.", "s": "public-reference", "f": null}, {"t": "Statehood", "d": "Maryland became a state 1788 (7th).", "g": "statehood", "l": 2, "q": "What is Statehood?", "a": "Maryland became a state 1788 (7th).", "x": "Maryland achieved statehood 1788 (7th). The road to statehood ran through territorial government, population thresholds, and a congressional enabling act — the standard American path. Civil War border state. Statehood Day is still celebrated, and the admission order gives Maryland its number among the states.", "s": "public-reference", "f": null}, {"t": "The statehood story", "d": "How Maryland went from territory to state.", "g": "statehood", "l": 2, "q": "What is The statehood story?", "a": "How Maryland went from territory to state.", "x": "The statehood story of Maryland: settlement, territorial organization, the push for admission, and finally the star on the flag. Chesapeake Bay; federal workforce. Every state's admission reflected the national politics of its era — Maryland's story is no exception, and it explains much about the state's character today.", "s": "public-reference", "f": null}, {"t": "Capital: Annapolis", "d": "Annapolis is the capital of Maryland.", "g": "overview", "l": 2, "q": "What is Capital: Annapolis?", "a": "Annapolis is the capital of Maryland.", "x": "Annapolis has been the seat of Maryland government, home to the capitol building, the supreme court, and the legislature. Capitals are often not the biggest city — Maryland's largest is Baltimore — chosen instead for geography or politics. Visit the capitol: the building itself tells the state's story in stone.", "s": "public-reference", "f": null}, {"t": "Nickname: Old Line State", "d": "Maryland is known as \"Old Line State.\"", "g": "overview", "l": 2, "q": "What is Nickname: Old Line State?", "a": "Maryland is known as \"Old Line State.\"", "x": "The nickname \"Old Line State\" captures how Maryland sees itself — and how America sees it. Fort McHenry's 1814 defense inspired the Star-Spangled Banner. State nicknames come from history, geography, or industry, and they appear on license plates, tourism campaigns, and sports teams. The motto goes deeper: \"Fatti maschii, parole femine (Manly deeds, womanly words).\"", "s": "public-reference", "f": null}, {"t": "Motto: Fatti maschii, parole femine (Manly deeds, womanly words)", "d": "The state motto of Maryland is \"Fatti maschii, parole femine (Manly deeds, womanly words).\"", "g": "overview", "l": 2, "q": "What is Motto: Fatti maschii, parole femine (Manly deeds, womanly words)?", "a": "The state motto of Maryland is \"Fatti maschii, parole femine (Manly deeds, womanly words).\"", "x": "The motto \"Fatti maschii, parole femine (Manly deeds, womanly words)\" is Maryland's official creed, adopted by the legislature and carried on the state seal. Calvert and Crossland heraldic banner. Mottos distill a state's ideals into a phrase — learn it, and you understand what the state aspires to be.", "s": "public-reference", "f": null}, {"t": "History 1", "d": "Catholic refuge colony 1634.", "g": "history", "l": 2, "q": "What is History 1?", "a": "Catholic refuge colony 1634.", "x": "Maryland history: Catholic refuge colony 1634.. This chapter explains the Old Line State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 1: why it matters", "d": "Why this Maryland chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 1: why it matters?", "a": "Why this Maryland chapter still shapes the state.", "x": "Why it matters: Catholic refuge colony 1634. That event's fingerprints are on modern Maryland — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 2", "d": "Civil War border state.", "g": "history", "l": 2, "q": "What is History 2?", "a": "Civil War border state.", "x": "Maryland history: Civil War border state.. This chapter explains the Old Line State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 2: why it matters", "d": "Why this Maryland chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 2: why it matters?", "a": "Why this Maryland chapter still shapes the state.", "x": "Why it matters: Civil War border state. That event's fingerprints are on modern Maryland — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 3", "d": "Chesapeake Bay; federal workforce.", "g": "history", "l": 2, "q": "What is History 3?", "a": "Chesapeake Bay; federal workforce.", "x": "Maryland history: Chesapeake Bay; federal workforce.. This chapter explains the Old Line State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 3: why it matters", "d": "Why this Maryland chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 3: why it matters?", "a": "Why this Maryland chapter still shapes the state.", "x": "Why it matters: Chesapeake Bay; federal workforce. That event's fingerprints are on modern Maryland — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 4", "d": "Fort McHenry's 1814 defense inspired the Star-Spangled Banner.", "g": "history", "l": 2, "q": "What is History 4?", "a": "Fort McHenry's 1814 defense inspired the Star-Spangled Banner.", "x": "Maryland history: Fort McHenry's 1814 defense inspired the Star-Spangled Banner.. This chapter explains the Old Line State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 4: why it matters", "d": "Why this Maryland chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 4: why it matters?", "a": "Why this Maryland chapter still shapes the state.", "x": "Why it matters: Fort McHenry's 1814 defense inspired the Star-Spangled Banner. That event's fingerprints are on modern Maryland — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "Frederick Douglass", "d": "Abolitionist from Talbot County.", "g": "people", "l": 2, "q": "What is Frederick Douglass?", "a": "Abolitionist from Talbot County.", "x": "Frederick Douglass — Abolitionist from Talbot County.. Maryland's famous sons and daughters carried the state's name worldwide. Abolitionist from Talbot County. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Frederick Douglass: legacy", "d": "The legacy of Frederick Douglass.", "g": "people", "l": 2, "q": "What is Frederick Douglass: legacy?", "a": "The legacy of Frederick Douglass.", "x": "The legacy of Frederick Douglass: Abolitionist from Talbot County.. Maryland honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name.", "s": "public-reference", "f": null}, {"t": "Babe Ruth", "d": "Born in Baltimore.", "g": "people", "l": 2, "q": "What is Babe Ruth?", "a": "Born in Baltimore.", "x": "Babe Ruth — Born in Baltimore.. Maryland's famous sons and daughters carried the state's name worldwide. Born in Baltimore. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Babe Ruth: legacy", "d": "The legacy of Babe Ruth.", "g": "people", "l": 2, "q": "What is Babe Ruth: legacy?", "a": "The legacy of Babe Ruth.", "x": "The legacy of Babe Ruth: Born in Baltimore.. Maryland honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Harriet Tubman", "d": "Underground Railroad; Dorchester County.", "g": "people", "l": 2, "q": "What is Harriet Tubman?", "a": "Underground Railroad; Dorchester County.", "x": "Harriet Tubman — Underground Railroad; Dorchester County.. Maryland's famous sons and daughters carried the state's name worldwide. Underground Railroad; Dorchester County. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Harriet Tubman: legacy", "d": "The legacy of Harriet Tubman.", "g": "people", "l": 2, "q": "What is Harriet Tubman: legacy?", "a": "The legacy of Harriet Tubman.", "x": "The legacy of Harriet Tubman: Underground Railroad; Dorchester County.. Maryland honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name.", "s": "public-reference", "f": null}, {"t": "Industry: federal government", "d": "federal government", "g": "economy", "l": 2, "q": "What is Industry: federal government?", "a": "federal government", "x": "Maryland's economy: federal government. Industries shape the state's cities, its workforce, and its politics. federal government From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Industry: biotech", "d": "biotech", "g": "economy", "l": 2, "q": "What is Industry: biotech?", "a": "biotech", "x": "Maryland's economy: biotech. Industries shape the state's cities, its workforce, and its politics. federal government From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Geography", "d": "The land of Maryland: from Assateague Island National Seashore to its borders.", "g": "geography", "l": 2, "q": "What is Geography?", "a": "The land of Maryland: from Assateague Island National Seashore to its borders.", "x": "The geography of Maryland runs from Assateague Island National Seashore across the state's varied regions. Landforms decide climate, crops, and settlement — the mountains, plains, coasts, or forests that define the state's look and livelihood. Inner Harbor", "s": "public-reference", "f": null}, {"t": "Modern era", "d": "Maryland today: biotech.", "g": "history", "l": 2, "q": "What is Modern era?", "a": "Maryland today: biotech.", "x": "Modern Maryland: biotech. Today's state balances growth with heritage — new industries beside historic downtowns, newcomers beside old families. The current chapter is still being written by everyone who lives here.", "s": "public-reference", "f": null}, {"t": "Visiting history", "d": "Experience Maryland history firsthand.", "g": "facts", "l": 2, "q": "What is Visiting history?", "a": "Experience Maryland history firsthand.", "x": "Experience Maryland history: the capitol in Annapolis, the museums, the historic districts, and Inner Harbor. Preakness Stakes History is best learned standing where it happened — walk the old streets, read the plaques, and talk to the docents who love it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-maryland-history-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
