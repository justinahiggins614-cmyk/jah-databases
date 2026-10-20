(function(){'use strict';
/* JAH Baffin Island Island Database generator — jahdb-e2-island-baffin-island-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-island-baffin-island',PREFIX='JAH-E2ISLANDBAF-',NAME='JAH Baffin Island Island Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Baffin Island: the complete guide", "d": "Baffin Island: Canada's Arctic giant..", "g": "overview", "l": 2, "q": "What is Baffin Island: the complete guide?", "a": "Baffin Island: Canada's Arctic giant..", "x": "The complete island guide to Baffin Island: Canada's Arctic giant.. 507,000 sq km. From formation to visiting, from wildlife to legends — everything about this island in one database. Arctic. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "507,000 sq km.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "507,000 sq km.", "x": "Baffin Island: 507,000 sq km.. People. One of the defining facts — Fjords.. Canada's Arctic giant. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 507,000 sq km..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 507,000 sq km..", "x": "Explored: 507,000 sq km.. Tours. Why it is so — Baffin Island. Polar bears. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Inuit.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Inuit.", "x": "Baffin Island: Inuit.. Wildlife. One of the defining facts — Polar bears.. Canada's Arctic giant. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Inuit..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Inuit..", "x": "Explored: Inuit.. History. Why it is so — Baffin Island. Iqaluit. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Fjords.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Fjords.", "x": "Baffin Island: Fjords.. Tours. One of the defining facts — Iqaluit.. Canada's Arctic giant. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Fjords..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Fjords..", "x": "Explored: Fjords.. Travel. Why it is so — Baffin Island. Aurora. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Polar bears.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Polar bears.", "x": "Baffin Island: Polar bears.. History. One of the defining facts — Aurora.. Canada's Arctic giant. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Polar bears..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Polar bears..", "x": "Explored: Polar bears.. Arctic. Why it is so — Baffin Island. 507,000 sq km. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Iqaluit.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Iqaluit.", "x": "Baffin Island: Iqaluit.. Travel. One of the defining facts — 507,000 sq km.. Canada's Arctic giant. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Iqaluit..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Iqaluit..", "x": "Explored: Iqaluit.. People. Why it is so — Baffin Island. Inuit. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Aurora.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Aurora.", "x": "Baffin Island: Aurora.. Arctic. One of the defining facts — Inuit.. Canada's Arctic giant. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Aurora..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Aurora..", "x": "Explored: Aurora.. Wildlife. Why it is so — Baffin Island. Fjords. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Arctic.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Arctic.", "x": "Baffin Island in depth: Arctic.. Inuit. The details reward the curious — Canada's Arctic giant.. Wildlife. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "People.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "People.", "x": "Baffin Island in depth: People.. Fjords. The details reward the curious — Canada's Arctic giant.. Tours. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Wildlife.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Wildlife.", "x": "Baffin Island in depth: Wildlife.. Polar bears. The details reward the curious — Canada's Arctic giant.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tours.", "x": "Baffin Island in depth: Tours.. Iqaluit. The details reward the curious — Canada's Arctic giant.. Travel. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "History.", "x": "Baffin Island in depth: History.. Aurora. The details reward the curious — Canada's Arctic giant.. Arctic. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Travel.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Travel.", "x": "Baffin Island in depth: Travel.. 507,000 sq km. The details reward the curious — Canada's Arctic giant.. People. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Baffin Island is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Baffin Island is.", "x": "Location: 507,000 sq km.. Arctic. Getting oriented — Baffin Island. Canada's Arctic giant. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Baffin Island.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Baffin Island.", "x": "Visiting: People.. Inuit. Practical know-how — Baffin Island. Canada's Arctic giant. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Baffin Island.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Baffin Island.", "x": "Ecology: Wildlife.. Fjords. The living world of Baffin Island — Canada's Arctic giant.. Tours. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Baffin Island through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Baffin Island through time.", "x": "History: History.. Polar bears. People and Baffin Island across the centuries — Canada's Arctic giant.. Travel. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Baffin Island.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Baffin Island.", "x": "Conservation: People.. 507,000 sq km. Threats and guardians of Baffin Island — Canada's Arctic giant.. Wildlife. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Baffin Island in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Baffin Island in numbers.", "x": "Numbers: 507,000 sq km.; Inuit.. Tours. Statistics that stun — Baffin Island. Canada's Arctic giant. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-island-baffin-island-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
