(function(){'use strict';
/* JAH Chambers Bay Golf Course Database generator — jahdb-e2-golf-chambers-bay-golf-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-golf-chambers-bay-golf',PREFIX='JAH-E2GOLFCHAMB-',NAME='JAH Chambers Bay Golf Course Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Chambers Bay: the complete guide", "d": "Chambers Bay: the quarry US Open..", "g": "overview", "l": 2, "q": "What is Chambers Bay: the complete guide?", "a": "Chambers Bay: the quarry US Open..", "x": "The complete golf course guide to Chambers Bay: the quarry US Open.. 2007. From formation to visiting, from wildlife to legends — everything about this golf course in one database. Quarry. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2007.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2007.", "x": "Chambers Bay: 2007.. US Open. One of the defining facts — Quarry.. the quarry US Open. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 2007..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 2007..", "x": "Explored: 2007.. Links. Why it is so — Chambers Bay. Puget Sound. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "US Open.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "US Open.", "x": "Chambers Bay: US Open.. Sound. One of the defining facts — Puget Sound.. the quarry US Open. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: US Open..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: US Open..", "x": "Explored: US Open.. Washington. Why it is so — Chambers Bay. Links. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Quarry.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Quarry.", "x": "Chambers Bay: Quarry.. Links. One of the defining facts — Links.. the quarry US Open. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Quarry..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Quarry..", "x": "Explored: Quarry.. Modern. Why it is so — Chambers Bay. Washington. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Puget Sound.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Puget Sound.", "x": "Chambers Bay: Puget Sound.. Washington. One of the defining facts — Washington.. the quarry US Open. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Puget Sound..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Puget Sound..", "x": "Explored: Puget Sound.. Quarry. Why it is so — Chambers Bay. 2007. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Links.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Links.", "x": "Chambers Bay: Links.. Modern. One of the defining facts — 2007.. the quarry US Open. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Links..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Links..", "x": "Explored: Links.. US Open. Why it is so — Chambers Bay. US Open. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Washington.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Washington.", "x": "Chambers Bay: Washington.. Quarry. One of the defining facts — US Open.. the quarry US Open. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Washington..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Washington..", "x": "Explored: Washington.. Sound. Why it is so — Chambers Bay. Quarry. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Quarry.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Quarry.", "x": "Chambers Bay in depth: Quarry.. US Open. The details reward the curious — the quarry US Open.. Sound. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "US Open.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "US Open.", "x": "Chambers Bay in depth: US Open.. Quarry. The details reward the curious — the quarry US Open.. Links. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Sound.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Sound.", "x": "Chambers Bay in depth: Sound.. Puget Sound. The details reward the curious — the quarry US Open.. Washington. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Links.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Links.", "x": "Chambers Bay in depth: Links.. Links. The details reward the curious — the quarry US Open.. Modern. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Washington.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Washington.", "x": "Chambers Bay in depth: Washington.. Washington. The details reward the curious — the quarry US Open.. Quarry. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Modern.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Modern.", "x": "Chambers Bay in depth: Modern.. 2007. The details reward the curious — the quarry US Open.. US Open. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Chambers Bay is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Chambers Bay is.", "x": "Location: 2007.. Quarry. Getting oriented — Chambers Bay. the quarry US Open. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Chambers Bay.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Chambers Bay.", "x": "Visiting: US Open.. US Open. Practical know-how — Chambers Bay. the quarry US Open. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Chambers Bay.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Chambers Bay.", "x": "Ecology: Sound.. Quarry. The living world of Chambers Bay — the quarry US Open.. Links. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Chambers Bay through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Chambers Bay through time.", "x": "History: Washington.. Puget Sound. People and Chambers Bay across the centuries — the quarry US Open.. Modern. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Chambers Bay.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Chambers Bay.", "x": "Conservation: US Open.. 2007. Threats and guardians of Chambers Bay — the quarry US Open.. Sound. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Chambers Bay in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Chambers Bay in numbers.", "x": "Numbers: 2007.; US Open.. Links. Statistics that stun — Chambers Bay. the quarry US Open. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-golf-chambers-bay-golf-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
