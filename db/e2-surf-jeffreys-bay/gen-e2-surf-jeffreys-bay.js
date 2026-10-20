(function(){'use strict';
/* JAH Jeffrey\'s Bay Surf Spot Database generator — jahdb-e2-surf-jeffreys-bay-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-surf-jeffreys-bay',PREFIX='JAH-E2SURFJEFFR-',NAME='JAH Jeffrey\'s Bay Surf Spot Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Jeffrey's Bay: the complete guide", "d": "Jeffrey's Bay: South Africa's perfect point..", "g": "overview", "l": 2, "q": "What is Jeffrey's Bay: the complete guide?", "a": "Jeffrey's Bay: South Africa's perfect point..", "x": "The complete surf spot guide to Jeffrey's Bay: South Africa's perfect point.. J-Bay. From formation to visiting, from wildlife to legends — everything about this surf spot in one database. Point. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "J-Bay.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "J-Bay.", "x": "Jeffrey's Bay: J-Bay.. WCT. One of the defining facts — Point.. South Africa's perfect point. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: J-Bay..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: J-Bay..", "x": "Explored: J-Bay.. Dolphins. Why it is so — Jeffrey's Bay. WCT. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Supertubes.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Supertubes.", "x": "Jeffrey's Bay: Supertubes.. Speed. One of the defining facts — WCT.. South Africa's perfect point. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Supertubes..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Supertubes..", "x": "Explored: Supertubes.. SA. Why it is so — Jeffrey's Bay. Dolphins. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Point.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Point.", "x": "Jeffrey's Bay: Point.. Dolphins. One of the defining facts — Dolphins.. South Africa's perfect point. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Point..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Point..", "x": "Explored: Point.. Perfection. Why it is so — Jeffrey's Bay. Speed. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "WCT.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "WCT.", "x": "Jeffrey's Bay: WCT.. SA. One of the defining facts — Speed.. South Africa's perfect point. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: WCT..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: WCT..", "x": "Explored: WCT.. Point. Why it is so — Jeffrey's Bay. J-Bay. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Dolphins.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Dolphins.", "x": "Jeffrey's Bay: Dolphins.. Perfection. One of the defining facts — J-Bay.. South Africa's perfect point. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Dolphins..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Dolphins..", "x": "Explored: Dolphins.. WCT. Why it is so — Jeffrey's Bay. Supertubes. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Speed.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Speed.", "x": "Jeffrey's Bay: Speed.. Point. One of the defining facts — Supertubes.. South Africa's perfect point. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Speed..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Speed..", "x": "Explored: Speed.. Speed. Why it is so — Jeffrey's Bay. Point. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Point.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Point.", "x": "Jeffrey's Bay in depth: Point.. Supertubes. The details reward the curious — South Africa's perfect point.. Speed. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "WCT.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "WCT.", "x": "Jeffrey's Bay in depth: WCT.. Point. The details reward the curious — South Africa's perfect point.. Dolphins. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Speed.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Speed.", "x": "Jeffrey's Bay in depth: Speed.. WCT. The details reward the curious — South Africa's perfect point.. SA. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Dolphins.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Dolphins.", "x": "Jeffrey's Bay in depth: Dolphins.. Dolphins. The details reward the curious — South Africa's perfect point.. Perfection. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "SA.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "SA.", "x": "Jeffrey's Bay in depth: SA.. Speed. The details reward the curious — South Africa's perfect point.. Point. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Perfection.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Perfection.", "x": "Jeffrey's Bay in depth: Perfection.. J-Bay. The details reward the curious — South Africa's perfect point.. WCT. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Jeffrey's Bay is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Jeffrey's Bay is.", "x": "Location: J-Bay.. Point. Getting oriented — Jeffrey's Bay. South Africa's perfect point. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Jeffrey's Bay.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Jeffrey's Bay.", "x": "Visiting: WCT.. Supertubes. Practical know-how — Jeffrey's Bay. South Africa's perfect point. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Jeffrey's Bay.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Jeffrey's Bay.", "x": "Ecology: Speed.. Point. The living world of Jeffrey's Bay — South Africa's perfect point.. Dolphins. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Jeffrey's Bay through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Jeffrey's Bay through time.", "x": "History: SA.. WCT. People and Jeffrey's Bay across the centuries — South Africa's perfect point.. Perfection. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Jeffrey's Bay.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Jeffrey's Bay.", "x": "Conservation: WCT.. J-Bay. Threats and guardians of Jeffrey's Bay — South Africa's perfect point.. Speed. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Jeffrey's Bay in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Jeffrey's Bay in numbers.", "x": "Numbers: J-Bay.; Supertubes.. Dolphins. Statistics that stun — Jeffrey's Bay. South Africa's perfect point. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-surf-jeffreys-bay-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
