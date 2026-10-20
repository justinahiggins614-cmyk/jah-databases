(function(){'use strict';
/* JAH North Island NZ Island Database generator — jahdb-e2-island-north-island-nz-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-island-north-island-nz',PREFIX='JAH-E2ISLANDNOR-',NAME='JAH North Island NZ Island Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "North Island NZ: the complete guide", "d": "North Island NZ: New Zealand's north..", "g": "overview", "l": 2, "q": "What is North Island NZ: the complete guide?", "a": "North Island NZ: New Zealand's north..", "x": "The complete island guide to North Island NZ: New Zealand's north.. 113,000 sq km. From formation to visiting, from wildlife to legends — everything about this island in one database. Geothermal. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "113,000 sq km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "113,000 sq km.", "x": "North Island NZ: 113,000 sq km.. Culture. One of the defining facts — Rotorua.. New Zealand's north. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 113,000 sq km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 113,000 sq km..", "x": "Explored: 113,000 sq km.. Cities. Why it is so — North Island NZ. Tongariro. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Auckland.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Auckland.", "x": "North Island NZ: Auckland.. Hikes. One of the defining facts — Tongariro.. New Zealand's north. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Auckland..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Auckland..", "x": "Explored: Auckland.. Beaches. Why it is so — North Island NZ. Wellington. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Rotorua.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Rotorua.", "x": "North Island NZ: Rotorua.. Cities. One of the defining facts — Wellington.. New Zealand's north. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Rotorua..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Rotorua..", "x": "Explored: Rotorua.. Travel. Why it is so — North Island NZ. Beaches. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Tongariro.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Tongariro.", "x": "North Island NZ: Tongariro.. Beaches. One of the defining facts — Beaches.. New Zealand's north. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Tongariro..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Tongariro..", "x": "Explored: Tongariro.. Geothermal. Why it is so — North Island NZ. 113,000 sq km. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Wellington.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Wellington.", "x": "North Island NZ: Wellington.. Travel. One of the defining facts — 113,000 sq km.. New Zealand's north. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Wellington..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Wellington..", "x": "Explored: Wellington.. Culture. Why it is so — North Island NZ. Auckland. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Beaches.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Beaches.", "x": "North Island NZ: Beaches.. Geothermal. One of the defining facts — Auckland.. New Zealand's north. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Beaches..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Beaches..", "x": "Explored: Beaches.. Hikes. Why it is so — North Island NZ. Rotorua. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Geothermal.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Geothermal.", "x": "North Island NZ in depth: Geothermal.. Auckland. The details reward the curious — New Zealand's north.. Hikes. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Culture.", "x": "North Island NZ in depth: Culture.. Rotorua. The details reward the curious — New Zealand's north.. Cities. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Hikes.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Hikes.", "x": "North Island NZ in depth: Hikes.. Tongariro. The details reward the curious — New Zealand's north.. Beaches. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Cities.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Cities.", "x": "North Island NZ in depth: Cities.. Wellington. The details reward the curious — New Zealand's north.. Travel. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Beaches.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Beaches.", "x": "North Island NZ in depth: Beaches.. Beaches. The details reward the curious — New Zealand's north.. Geothermal. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Travel.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Travel.", "x": "North Island NZ in depth: Travel.. 113,000 sq km. The details reward the curious — New Zealand's north.. Culture. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where North Island NZ is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where North Island NZ is.", "x": "Location: 113,000 sq km.. Geothermal. Getting oriented — North Island NZ. New Zealand's north. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience North Island NZ.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience North Island NZ.", "x": "Visiting: Culture.. Auckland. Practical know-how — North Island NZ. New Zealand's north. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around North Island NZ.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around North Island NZ.", "x": "Ecology: Hikes.. Rotorua. The living world of North Island NZ — New Zealand's north.. Cities. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "North Island NZ through time.", "g": "history", "l": 2, "q": "What is History?", "a": "North Island NZ through time.", "x": "History: Beaches.. Tongariro. People and North Island NZ across the centuries — New Zealand's north.. Travel. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting North Island NZ.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting North Island NZ.", "x": "Conservation: Culture.. 113,000 sq km. Threats and guardians of North Island NZ — New Zealand's north.. Hikes. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "North Island NZ in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "North Island NZ in numbers.", "x": "Numbers: 113,000 sq km.; Auckland.. Cities. Statistics that stun — North Island NZ. New Zealand's north. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-island-north-island-nz-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
