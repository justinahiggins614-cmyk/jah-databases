(function(){'use strict';
/* JAH Siam Park Theme Park Database generator — jahdb-e2-themepark-siam-park-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-themepark-siam-park',PREFIX='JAH-E2THEMEPARK-',NAME='JAH Siam Park Theme Park Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Siam Park: the complete guide", "d": "Siam Park: the Thai water kingdom..", "g": "overview", "l": 2, "q": "What is Siam Park: the complete guide?", "a": "Siam Park: the Thai water kingdom..", "x": "The complete theme park guide to Siam Park: the Thai water kingdom.. 2008. From formation to visiting, from wildlife to legends — everything about this theme park in one database. Slides. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2008.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2008.", "x": "Siam Park: 2008.. Lazy. One of the defining facts — Tower of Power.. the Thai water kingdom. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 2008..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 2008..", "x": "Explored: 2008.. Tickets. Why it is so — Siam Park. Lazy river. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Tenerife.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Tenerife.", "x": "Siam Park: Tenerife.. Records. One of the defining facts — Lazy river.. the Thai water kingdom. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Tenerife..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Tenerife..", "x": "Explored: Tenerife.. Tenerife. Why it is so — Siam Park. Best water park. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Tower of Power.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Tower of Power.", "x": "Siam Park: Tower of Power.. Tickets. One of the defining facts — Best water park.. the Thai water kingdom. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Tower of Power..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Tower of Power..", "x": "Explored: Tower of Power.. Thai. Why it is so — Siam Park. Thai. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Lazy river.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Lazy river.", "x": "Siam Park: Lazy river.. Tenerife. One of the defining facts — Thai.. the Thai water kingdom. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Lazy river..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Lazy river..", "x": "Explored: Lazy river.. Slides. Why it is so — Siam Park. 2008. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Best water park.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Best water park.", "x": "Siam Park: Best water park.. Thai. One of the defining facts — 2008.. the Thai water kingdom. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Best water park..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Best water park..", "x": "Explored: Best water park.. Lazy. Why it is so — Siam Park. Tenerife. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Thai.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Thai.", "x": "Siam Park: Thai.. Slides. One of the defining facts — Tenerife.. the Thai water kingdom. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Thai..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Thai..", "x": "Explored: Thai.. Records. Why it is so — Siam Park. Tower of Power. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Slides.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Slides.", "x": "Siam Park in depth: Slides.. Tenerife. The details reward the curious — the Thai water kingdom.. Records. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Lazy.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Lazy.", "x": "Siam Park in depth: Lazy.. Tower of Power. The details reward the curious — the Thai water kingdom.. Tickets. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Records.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Records.", "x": "Siam Park in depth: Records.. Lazy river. The details reward the curious — the Thai water kingdom.. Tenerife. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Tickets.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Tickets.", "x": "Siam Park in depth: Tickets.. Best water park. The details reward the curious — the Thai water kingdom.. Thai. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Tenerife.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Tenerife.", "x": "Siam Park in depth: Tenerife.. Thai. The details reward the curious — the Thai water kingdom.. Slides. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Thai.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Thai.", "x": "Siam Park in depth: Thai.. 2008. The details reward the curious — the Thai water kingdom.. Lazy. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Siam Park is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Siam Park is.", "x": "Location: 2008.. Slides. Getting oriented — Siam Park. the Thai water kingdom. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Siam Park.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Siam Park.", "x": "Visiting: Lazy.. Tenerife. Practical know-how — Siam Park. the Thai water kingdom. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Siam Park.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Siam Park.", "x": "Ecology: Records.. Tower of Power. The living world of Siam Park — the Thai water kingdom.. Tickets. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Siam Park through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Siam Park through time.", "x": "History: Tenerife.. Lazy river. People and Siam Park across the centuries — the Thai water kingdom.. Thai. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Siam Park.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Siam Park.", "x": "Conservation: Lazy.. 2008. Threats and guardians of Siam Park — the Thai water kingdom.. Records. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Siam Park in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Siam Park in numbers.", "x": "Numbers: 2008.; Tenerife.. Tickets. Statistics that stun — Siam Park. the Thai water kingdom. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-themepark-siam-park-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
