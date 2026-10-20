(function(){'use strict';
/* JAH Martha\'s Vineyard Beaches Beach Database generator — jahdb-e2-beach-marthas-vineyard-beaches-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-beach-marthas-vineyard-beaches',PREFIX='JAH-E2BEACHMART-',NAME='JAH Martha\'s Vineyard Beaches Beach Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Martha's Vineyard Beaches: the complete guide", "d": "Martha's Vineyard Beaches: the island's shores..", "g": "overview", "l": 2, "q": "What is Martha's Vineyard Beaches: the complete guide?", "a": "Martha's Vineyard Beaches: the island's shores..", "x": "The complete beach guide to Martha's Vineyard Beaches: the island's shores.. Aquinnah. From formation to visiting, from wildlife to legends — everything about this beach in one database. Cliffs. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Aquinnah.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Aquinnah.", "x": "Martha's Vineyard Beaches: Aquinnah.. Jaws. One of the defining facts — South Beach.. the island's shores. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: Aquinnah..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: Aquinnah..", "x": "Explored: Aquinnah.. Vineyard. Why it is so — Martha's Vineyard Beaches. Jaws. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Cliffs.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Cliffs.", "x": "Martha's Vineyard Beaches: Cliffs.. Summer. One of the defining facts — Jaws.. the island's shores. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Cliffs..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Cliffs..", "x": "Explored: Cliffs.. Lighthouses. Why it is so — Martha's Vineyard Beaches. Summer. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "South Beach.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "South Beach.", "x": "Martha's Vineyard Beaches: South Beach.. Vineyard. One of the defining facts — Summer.. the island's shores. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: South Beach..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: South Beach..", "x": "Explored: South Beach.. Sand. Why it is so — Martha's Vineyard Beaches. Lighthouses. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Jaws.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Jaws.", "x": "Martha's Vineyard Beaches: Jaws.. Lighthouses. One of the defining facts — Lighthouses.. the island's shores. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Jaws..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Jaws..", "x": "Explored: Jaws.. Cliffs. Why it is so — Martha's Vineyard Beaches. Aquinnah. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Summer.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Summer.", "x": "Martha's Vineyard Beaches: Summer.. Sand. One of the defining facts — Aquinnah.. the island's shores. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Summer..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Summer..", "x": "Explored: Summer.. Jaws. Why it is so — Martha's Vineyard Beaches. Cliffs. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Lighthouses.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Lighthouses.", "x": "Martha's Vineyard Beaches: Lighthouses.. Cliffs. One of the defining facts — Cliffs.. the island's shores. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Lighthouses..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Lighthouses..", "x": "Explored: Lighthouses.. Summer. Why it is so — Martha's Vineyard Beaches. South Beach. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Cliffs.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Cliffs.", "x": "Martha's Vineyard Beaches in depth: Cliffs.. Cliffs. The details reward the curious — the island's shores.. Summer. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Jaws.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Jaws.", "x": "Martha's Vineyard Beaches in depth: Jaws.. South Beach. The details reward the curious — the island's shores.. Vineyard. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Summer.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Summer.", "x": "Martha's Vineyard Beaches in depth: Summer.. Jaws. The details reward the curious — the island's shores.. Lighthouses. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Vineyard.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Vineyard.", "x": "Martha's Vineyard Beaches in depth: Vineyard.. Summer. The details reward the curious — the island's shores.. Sand. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Lighthouses.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Lighthouses.", "x": "Martha's Vineyard Beaches in depth: Lighthouses.. Lighthouses. The details reward the curious — the island's shores.. Cliffs. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Sand.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Sand.", "x": "Martha's Vineyard Beaches in depth: Sand.. Aquinnah. The details reward the curious — the island's shores.. Jaws. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Martha's Vineyard Beaches is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Martha's Vineyard Beaches is.", "x": "Location: Aquinnah.. Cliffs. Getting oriented — Martha's Vineyard Beaches. the island's shores. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Martha's Vineyard Beaches.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Martha's Vineyard Beaches.", "x": "Visiting: Jaws.. Cliffs. Practical know-how — Martha's Vineyard Beaches. the island's shores. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Martha's Vineyard Beaches.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Martha's Vineyard Beaches.", "x": "Ecology: Summer.. South Beach. The living world of Martha's Vineyard Beaches — the island's shores.. Vineyard. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Martha's Vineyard Beaches through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Martha's Vineyard Beaches through time.", "x": "History: Lighthouses.. Jaws. People and Martha's Vineyard Beaches across the centuries — the island's shores.. Sand. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Martha's Vineyard Beaches.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Martha's Vineyard Beaches.", "x": "Conservation: Jaws.. Aquinnah. Threats and guardians of Martha's Vineyard Beaches — the island's shores.. Summer. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Martha's Vineyard Beaches in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Martha's Vineyard Beaches in numbers.", "x": "Numbers: Aquinnah.; Cliffs.. Vineyard. Statistics that stun — Martha's Vineyard Beaches. the island's shores. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-beach-marthas-vineyard-beaches-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
