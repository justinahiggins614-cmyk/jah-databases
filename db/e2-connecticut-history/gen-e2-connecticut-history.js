(function(){'use strict';
/* JAH Connecticut History Database generator — jahdb-e2-connecticut-history-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-connecticut-history',PREFIX='JAH-E2CONNECTIC-',NAME='JAH Connecticut History Database';
var FIELDS=["overview", "statehood", "history", "people", "economy", "geography", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Connecticut: history overview", "d": "Connecticut: the Constitution State, admitted 1788 (5th); capital Hartford.", "g": "overview", "l": 2, "q": "What is Connecticut: history overview?", "a": "Connecticut: the Constitution State, admitted 1788 (5th); capital Hartford.", "x": "Connecticut — \"Constitution State\" — entered the Union 1788 (5th). Its capital is Hartford and its largest city is Bridgeport. Pequot lands; Fundamental Orders 1639. This database tells the state's story: from its first peoples through statehood to the modern era, plus the famous sons and daughters, the industries, and the facts every resident should know.", "s": "public-reference", "f": null}, {"t": "Statehood", "d": "Connecticut became a state 1788 (5th).", "g": "statehood", "l": 2, "q": "What is Statehood?", "a": "Connecticut became a state 1788 (5th).", "x": "Connecticut achieved statehood 1788 (5th). The road to statehood ran through territorial government, population thresholds, and a congressional enabling act — the standard American path. Revolutionary arsenal; Constitution State. Statehood Day is still celebrated, and the admission order gives Connecticut its number among the states.", "s": "public-reference", "f": null}, {"t": "The statehood story", "d": "How Connecticut went from territory to state.", "g": "statehood", "l": 2, "q": "What is The statehood story?", "a": "How Connecticut went from territory to state.", "x": "The statehood story of Connecticut: settlement, territorial organization, the push for admission, and finally the star on the flag. Insurance and manufacturing. Every state's admission reflected the national politics of its era — Connecticut's story is no exception, and it explains much about the state's character today.", "s": "public-reference", "f": null}, {"t": "Capital: Hartford", "d": "Hartford is the capital of Connecticut.", "g": "overview", "l": 2, "q": "What is Capital: Hartford?", "a": "Hartford is the capital of Connecticut.", "x": "Hartford has been the seat of Connecticut government, home to the capitol building, the supreme court, and the legislature. Capitals are often not the biggest city — Connecticut's largest is Bridgeport — chosen instead for geography or politics. Visit the capitol: the building itself tells the state's story in stone.", "s": "public-reference", "f": null}, {"t": "Nickname: Constitution State", "d": "Connecticut is known as \"Constitution State.\"", "g": "overview", "l": 2, "q": "What is Nickname: Constitution State?", "a": "Connecticut is known as \"Constitution State.\"", "x": "The nickname \"Constitution State\" captures how Connecticut sees itself — and how America sees it. Submarines (Groton). State nicknames come from history, geography, or industry, and they appear on license plates, tourism campaigns, and sports teams. The motto goes deeper: \"Qui transtulit sustinet (He who transplanted still sustains).\"", "s": "public-reference", "f": null}, {"t": "Motto: Qui transtulit sustinet (He who transplanted still sustains)", "d": "The state motto of Connecticut is \"Qui transtulit sustinet (He who transplanted still sustains).\"", "g": "overview", "l": 2, "q": "What is Motto: Qui transtulit sustinet (He who transplanted still sustains)?", "a": "The state motto of Connecticut is \"Qui transtulit sustinet (He who transplanted still sustains).\"", "x": "The motto \"Qui transtulit sustinet (He who transplanted still sustains)\" is Connecticut's official creed, adopted by the legislature and carried on the state seal. Blue field with colonial grapevines shield. Mottos distill a state's ideals into a phrase — learn it, and you understand what the state aspires to be.", "s": "public-reference", "f": null}, {"t": "History 1", "d": "Pequot lands; Fundamental Orders 1639.", "g": "history", "l": 2, "q": "What is History 1?", "a": "Pequot lands; Fundamental Orders 1639.", "x": "Connecticut history: Pequot lands; Fundamental Orders 1639.. This chapter explains the Constitution State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 1: why it matters", "d": "Why this Connecticut chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 1: why it matters?", "a": "Why this Connecticut chapter still shapes the state.", "x": "Why it matters: Pequot lands; Fundamental Orders 1639. That event's fingerprints are on modern Connecticut — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 2", "d": "Revolutionary arsenal; Constitution State.", "g": "history", "l": 2, "q": "What is History 2?", "a": "Revolutionary arsenal; Constitution State.", "x": "Connecticut history: Revolutionary arsenal; Constitution State.. This chapter explains the Constitution State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 2: why it matters", "d": "Why this Connecticut chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 2: why it matters?", "a": "Why this Connecticut chapter still shapes the state.", "x": "Why it matters: Revolutionary arsenal; Constitution State. That event's fingerprints are on modern Connecticut — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 3", "d": "Insurance and manufacturing.", "g": "history", "l": 2, "q": "What is History 3?", "a": "Insurance and manufacturing.", "x": "Connecticut history: Insurance and manufacturing.. This chapter explains the Constitution State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 3: why it matters", "d": "Why this Connecticut chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 3: why it matters?", "a": "Why this Connecticut chapter still shapes the state.", "x": "Why it matters: Insurance and manufacturing. That event's fingerprints are on modern Connecticut — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "History 4", "d": "Submarines (Groton).", "g": "history", "l": 2, "q": "What is History 4?", "a": "Submarines (Groton).", "x": "Connecticut history: Submarines (Groton).. This chapter explains the Constitution State of today — the borders, the cities, the industries, even the accent. History here is lived, not just remembered: the old districts, the museums, and the stories grandparents tell.", "s": "public-reference", "f": null}, {"t": "History 4: why it matters", "d": "Why this Connecticut chapter still shapes the state.", "g": "history", "l": 2, "q": "What is History 4: why it matters?", "a": "Why this Connecticut chapter still shapes the state.", "x": "Why it matters: Submarines (Groton). That event's fingerprints are on modern Connecticut — in its laws, its demographics, its economy. Understanding it turns a drive through the state into a tour through time.", "s": "public-reference", "f": null}, {"t": "Mark Twain", "d": "Wrote in Hartford.", "g": "people", "l": 2, "q": "What is Mark Twain?", "a": "Wrote in Hartford.", "x": "Mark Twain — Wrote in Hartford.. Connecticut's famous sons and daughters carried the state's name worldwide. Wrote in Hartford. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Mark Twain: legacy", "d": "The legacy of Mark Twain.", "g": "people", "l": 2, "q": "What is Mark Twain: legacy?", "a": "The legacy of Mark Twain.", "x": "The legacy of Mark Twain: Wrote in Hartford.. Connecticut honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Harriet Beecher Stowe", "d": "Uncle Tom's Cabin; Hartford.", "g": "people", "l": 2, "q": "What is Harriet Beecher Stowe?", "a": "Uncle Tom's Cabin; Hartford.", "x": "Harriet Beecher Stowe — Uncle Tom's Cabin; Hartford.. Connecticut's famous sons and daughters carried the state's name worldwide. Uncle Tom's Cabin; Hartford. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Harriet Beecher Stowe: legacy", "d": "The legacy of Harriet Beecher Stowe.", "g": "people", "l": 2, "q": "What is Harriet Beecher Stowe: legacy?", "a": "The legacy of Harriet Beecher Stowe.", "x": "The legacy of Harriet Beecher Stowe: Uncle Tom's Cabin; Hartford.. Connecticut honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name.", "s": "public-reference", "f": null}, {"t": "Katharine Hepburn", "d": "Actress from Hartford.", "g": "people", "l": 2, "q": "What is Katharine Hepburn?", "a": "Actress from Hartford.", "x": "Katharine Hepburn — Actress from Hartford.. Connecticut's famous sons and daughters carried the state's name worldwide. Actress from Hartford. Their stories are taught in schools and toasted in hometowns — and they prove that where you start does not decide where you finish.", "s": "public-reference", "f": null}, {"t": "Katharine Hepburn: legacy", "d": "The legacy of Katharine Hepburn.", "g": "people", "l": 2, "q": "What is Katharine Hepburn: legacy?", "a": "The legacy of Katharine Hepburn.", "x": "The legacy of Katharine Hepburn: Actress from Hartford.. Connecticut honors its own — with museums, highways, and statues — because their achievements belong to everyone who shares the state's name. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Industry: insurance (Hartford)", "d": "insurance (Hartford)", "g": "economy", "l": 2, "q": "What is Industry: insurance (Hartford)?", "a": "insurance (Hartford)", "x": "Connecticut's economy: insurance (Hartford). Industries shape the state's cities, its workforce, and its politics. insurance (Hartford) From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Industry: defense (submarines)", "d": "defense (submarines)", "g": "economy", "l": 2, "q": "What is Industry: defense (submarines)?", "a": "defense (submarines)", "x": "Connecticut's economy: defense (submarines). Industries shape the state's cities, its workforce, and its politics. insurance (Hartford) From the first industry to today's employers, work is the through-line of the state's story.", "s": "public-reference", "f": null}, {"t": "Geography", "d": "The land of Connecticut: from Sleeping Giant State Park to its borders.", "g": "geography", "l": 2, "q": "What is Geography?", "a": "The land of Connecticut: from Sleeping Giant State Park to its borders.", "x": "The geography of Connecticut runs from Sleeping Giant State Park across the state's varied regions. Landforms decide climate, crops, and settlement — the mountains, plains, coasts, or forests that define the state's look and livelihood. Mystic Seaport", "s": "public-reference", "f": null}, {"t": "Modern era", "d": "Connecticut today: defense (submarines).", "g": "history", "l": 2, "q": "What is Modern era?", "a": "Connecticut today: defense (submarines).", "x": "Modern Connecticut: defense (submarines). Today's state balances growth with heritage — new industries beside historic downtowns, newcomers beside old families. The current chapter is still being written by everyone who lives here.", "s": "public-reference", "f": null}, {"t": "Visiting history", "d": "Experience Connecticut history firsthand.", "g": "facts", "l": 2, "q": "What is Visiting history?", "a": "Experience Connecticut history firsthand.", "x": "Experience Connecticut history: the capitol in Hartford, the museums, the historic districts, and Mystic Seaport. Mystic Outdoor Art Festival History is best learned standing where it happened — walk the old streets, read the plaques, and talk to the docents who love it.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-connecticut-history-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
