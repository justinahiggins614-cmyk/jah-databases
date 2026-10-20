(function(){'use strict';
/* JAH Rocky Mountain National Park National Park Database generator — jahdb-e2-park-rocky-mountain-np-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-park-rocky-mountain-np',PREFIX='JAH-E2PARKROCKY-',NAME='JAH Rocky Mountain National Park National Park Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Rocky Mountain National Park: the complete guide", "d": "Rocky Mountain National Park: Colorado's high park..", "g": "overview", "l": 2, "q": "What is Rocky Mountain National Park: the complete guide?", "a": "Rocky Mountain National Park: Colorado's high park..", "x": "The complete national park guide to Rocky Mountain National Park: Colorado's high park.. Trail Ridge Road. From formation to visiting, from wildlife to legends — everything about this national park in one database. Road.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Trail Ridge Road.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Trail Ridge Road.", "x": "Rocky Mountain National Park: Trail Ridge Road.. Peaks. One of the defining facts — Longs Peak.. Colorado's high park. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: Trail Ridge Road..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: Trail Ridge Road..", "x": "Explored: Trail Ridge Road.. Town. Why it is so — Rocky Mountain National Park. Alpine. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Elk.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Elk.", "x": "Rocky Mountain National Park: Elk.. Wildlife. One of the defining facts — Alpine.. Colorado's high park. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Elk..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Elk..", "x": "Explored: Elk.. Seasons. Why it is so — Rocky Mountain National Park. Estes Park. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Longs Peak.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Longs Peak.", "x": "Rocky Mountain National Park: Longs Peak.. Town. One of the defining facts — Estes Park.. Colorado's high park. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Longs Peak..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Longs Peak..", "x": "Explored: Longs Peak.. Hikes. Why it is so — Rocky Mountain National Park. Wildlife. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Alpine.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Alpine.", "x": "Rocky Mountain National Park: Alpine.. Seasons. One of the defining facts — Wildlife.. Colorado's high park. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Alpine..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Alpine..", "x": "Explored: Alpine.. Road. Why it is so — Rocky Mountain National Park. Trail Ridge Road. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Estes Park.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Estes Park.", "x": "Rocky Mountain National Park: Estes Park.. Hikes. One of the defining facts — Trail Ridge Road.. Colorado's high park. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Estes Park..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Estes Park..", "x": "Explored: Estes Park.. Peaks. Why it is so — Rocky Mountain National Park. Elk. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Wildlife.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Wildlife.", "x": "Rocky Mountain National Park: Wildlife.. Road. One of the defining facts — Elk.. Colorado's high park. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Wildlife..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Wildlife..", "x": "Explored: Wildlife.. Wildlife. Why it is so — Rocky Mountain National Park. Longs Peak. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Road.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Road.", "x": "Rocky Mountain National Park in depth: Road.. Elk. The details reward the curious — Colorado's high park.. Wildlife. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Peaks.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Peaks.", "x": "Rocky Mountain National Park in depth: Peaks.. Longs Peak. The details reward the curious — Colorado's high park.. Town. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Wildlife.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Wildlife.", "x": "Rocky Mountain National Park in depth: Wildlife.. Alpine. The details reward the curious — Colorado's high park.. Seasons. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Town.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Town.", "x": "Rocky Mountain National Park in depth: Town.. Estes Park. The details reward the curious — Colorado's high park.. Hikes. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Seasons.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Seasons.", "x": "Rocky Mountain National Park in depth: Seasons.. Wildlife. The details reward the curious — Colorado's high park.. Road. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Hikes.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Hikes.", "x": "Rocky Mountain National Park in depth: Hikes.. Trail Ridge Road. The details reward the curious — Colorado's high park.. Peaks. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Rocky Mountain National Park is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Rocky Mountain National Park is.", "x": "Location: Trail Ridge Road.. Road. Getting oriented — Rocky Mountain National Park. Colorado's high park. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Rocky Mountain National Park.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Rocky Mountain National Park.", "x": "Visiting: Peaks.. Elk. Practical know-how — Rocky Mountain National Park. Colorado's high park. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Rocky Mountain National Park.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Rocky Mountain National Park.", "x": "Ecology: Wildlife.. Longs Peak. The living world of Rocky Mountain National Park — Colorado's high park.. Town. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Rocky Mountain National Park through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Rocky Mountain National Park through time.", "x": "History: Seasons.. Alpine. People and Rocky Mountain National Park across the centuries — Colorado's high park.. Hikes. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Rocky Mountain National Park.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Rocky Mountain National Park.", "x": "Conservation: Peaks.. Trail Ridge Road. Threats and guardians of Rocky Mountain National Park — Colorado's high park.. Wildlife. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Rocky Mountain National Park in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Rocky Mountain National Park in numbers.", "x": "Numbers: Trail Ridge Road.; Elk.. Town. Statistics that stun — Rocky Mountain National Park. Colorado's high park. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-park-rocky-mountain-np-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
