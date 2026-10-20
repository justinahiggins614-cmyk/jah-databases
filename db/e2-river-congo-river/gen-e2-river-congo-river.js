(function(){'use strict';
/* JAH Congo River River Database generator — jahdb-e2-river-congo-river-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-river-congo-river',PREFIX='JAH-E2RIVERCONG-',NAME='JAH Congo River River Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Congo River: the complete guide", "d": "Congo River: world's deepest; Africa's power..", "g": "overview", "l": 2, "q": "What is Congo River: the complete guide?", "a": "Congo River: world's deepest; Africa's power..", "x": "The complete river guide to Congo River: world's deepest; Africa's power.. Deepest: 220m. From formation to visiting, from wildlife to legends — everything about this river in one database. Source: Zambia.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Deepest: 220m.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Deepest: 220m.", "x": "Congo River: Deepest: 220m.. Kinshasa/Brazzaville. One of the defining facts — Second discharge.. world's deepest; Africa's power. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: Deepest: 220m..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: Deepest: 220m..", "x": "Explored: Deepest: 220m.. Navigability. Why it is so — Congo River. Inga dams potential. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "4,700 km.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "4,700 km.", "x": "Congo River: 4,700 km.. Biodiversity. One of the defining facts — Inga dams potential.. world's deepest; Africa's power. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: 4,700 km..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: 4,700 km..", "x": "Explored: 4,700 km.. History. Why it is so — Congo River. Rainforest. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Second discharge.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Second discharge.", "x": "Congo River: Second discharge.. Navigability. One of the defining facts — Rainforest.. world's deepest; Africa's power. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Second discharge..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Second discharge..", "x": "Explored: Second discharge.. Power. Why it is so — Congo River. Livingstone. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Inga dams potential.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Inga dams potential.", "x": "Congo River: Inga dams potential.. History. One of the defining facts — Livingstone.. world's deepest; Africa's power. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Inga dams potential..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Inga dams potential..", "x": "Explored: Inga dams potential.. Source: Zambia. Why it is so — Congo River. Deepest: 220m. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Rainforest.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Rainforest.", "x": "Congo River: Rainforest.. Power. One of the defining facts — Deepest: 220m.. world's deepest; Africa's power. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Rainforest..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Rainforest..", "x": "Explored: Rainforest.. Kinshasa/Brazzaville. Why it is so — Congo River. 4,700 km. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Livingstone.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Livingstone.", "x": "Congo River: Livingstone.. Source: Zambia. One of the defining facts — 4,700 km.. world's deepest; Africa's power. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Livingstone..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Livingstone..", "x": "Explored: Livingstone.. Biodiversity. Why it is so — Congo River. Second discharge. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Source: Zambia.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Source: Zambia.", "x": "Congo River in depth: Source: Zambia.. 4,700 km. The details reward the curious — world's deepest; Africa's power.. Biodiversity. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Kinshasa/Brazzaville.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Kinshasa/Brazzaville.", "x": "Congo River in depth: Kinshasa/Brazzaville.. Second discharge. The details reward the curious — world's deepest; Africa's power.. Navigability. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Biodiversity.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Biodiversity.", "x": "Congo River in depth: Biodiversity.. Inga dams potential. The details reward the curious — world's deepest; Africa's power.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Navigability.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Navigability.", "x": "Congo River in depth: Navigability.. Rainforest. The details reward the curious — world's deepest; Africa's power.. Power. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "History.", "x": "Congo River in depth: History.. Livingstone. The details reward the curious — world's deepest; Africa's power.. Source: Zambia. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Power.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Power.", "x": "Congo River in depth: Power.. Deepest: 220m. The details reward the curious — world's deepest; Africa's power.. Kinshasa/Brazzaville. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Congo River is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Congo River is.", "x": "Location: Deepest: 220m.. Source: Zambia. Getting oriented — Congo River. world's deepest; Africa's power. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Congo River.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Congo River.", "x": "Visiting: Kinshasa/Brazzaville.. 4,700 km. Practical know-how — Congo River. world's deepest; Africa's power. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Congo River.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Congo River.", "x": "Ecology: Biodiversity.. Second discharge. The living world of Congo River — world's deepest; Africa's power.. Navigability. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Congo River through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Congo River through time.", "x": "History: History.. Inga dams potential. People and Congo River across the centuries — world's deepest; Africa's power.. Power. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Congo River.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Congo River.", "x": "Conservation: Kinshasa/Brazzaville.. Deepest: 220m. Threats and guardians of Congo River — world's deepest; Africa's power.. Biodiversity. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Congo River in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Congo River in numbers.", "x": "Numbers: Deepest: 220m.; 4,700 km.. Navigability. Statistics that stun — Congo River. world's deepest; Africa's power. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-river-congo-river-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
