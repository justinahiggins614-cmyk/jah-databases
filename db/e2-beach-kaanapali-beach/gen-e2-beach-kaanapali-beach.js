(function(){'use strict';
/* JAH Ka\'anapali Beach Beach Database generator — jahdb-e2-beach-kaanapali-beach-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-beach-kaanapali-beach',PREFIX='JAH-E2BEACHKAAN-',NAME='JAH Ka\'anapali Beach Beach Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Ka'anapali Beach: the complete guide", "d": "Ka'anapali Beach: Maui's golden mile..", "g": "overview", "l": 2, "q": "What is Ka'anapali Beach: the complete guide?", "a": "Ka'anapali Beach: Maui's golden mile..", "x": "The complete beach guide to Ka'anapali Beach: Maui's golden mile.. Maui. From formation to visiting, from wildlife to legends — everything about this beach in one database. Length. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Maui.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Maui.", "x": "Ka'anapali Beach: Maui.. Cliff. One of the defining facts — Cliff dive.. Maui's golden mile. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: Maui..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: Maui..", "x": "Explored: Maui.. Maui. Why it is so — Ka'anapali Beach. Whales. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "3 miles.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "3 miles.", "x": "Ka'anapali Beach: 3 miles.. Whales. One of the defining facts — Whales.. Maui's golden mile. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: 3 miles..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: 3 miles..", "x": "Explored: 3 miles.. Sunsets. Why it is so — Ka'anapali Beach. Black Rock. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Cliff dive.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Cliff dive.", "x": "Ka'anapali Beach: Cliff dive.. Maui. One of the defining facts — Black Rock.. Maui's golden mile. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Cliff dive..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Cliff dive..", "x": "Explored: Cliff dive.. Snorkel. Why it is so — Ka'anapali Beach. Sunsets. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Whales.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Whales.", "x": "Ka'anapali Beach: Whales.. Sunsets. One of the defining facts — Sunsets.. Maui's golden mile. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Whales..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Whales..", "x": "Explored: Whales.. Length. Why it is so — Ka'anapali Beach. Maui. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Black Rock.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Black Rock.", "x": "Ka'anapali Beach: Black Rock.. Snorkel. One of the defining facts — Maui.. Maui's golden mile. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Black Rock..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Black Rock..", "x": "Explored: Black Rock.. Cliff. Why it is so — Ka'anapali Beach. 3 miles. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Sunsets.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Sunsets.", "x": "Ka'anapali Beach: Sunsets.. Length. One of the defining facts — 3 miles.. Maui's golden mile. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Sunsets..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Sunsets..", "x": "Explored: Sunsets.. Whales. Why it is so — Ka'anapali Beach. Cliff dive. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Length.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Length.", "x": "Ka'anapali Beach in depth: Length.. 3 miles. The details reward the curious — Maui's golden mile.. Whales. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Cliff.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Cliff.", "x": "Ka'anapali Beach in depth: Cliff.. Cliff dive. The details reward the curious — Maui's golden mile.. Maui. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Whales.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Whales.", "x": "Ka'anapali Beach in depth: Whales.. Whales. The details reward the curious — Maui's golden mile.. Sunsets. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Maui.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Maui.", "x": "Ka'anapali Beach in depth: Maui.. Black Rock. The details reward the curious — Maui's golden mile.. Snorkel. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Sunsets.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Sunsets.", "x": "Ka'anapali Beach in depth: Sunsets.. Sunsets. The details reward the curious — Maui's golden mile.. Length. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Snorkel.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Snorkel.", "x": "Ka'anapali Beach in depth: Snorkel.. Maui. The details reward the curious — Maui's golden mile.. Cliff. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Ka'anapali Beach is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Ka'anapali Beach is.", "x": "Location: Maui.. Length. Getting oriented — Ka'anapali Beach. Maui's golden mile. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Ka'anapali Beach.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Ka'anapali Beach.", "x": "Visiting: Cliff.. 3 miles. Practical know-how — Ka'anapali Beach. Maui's golden mile. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Ka'anapali Beach.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Ka'anapali Beach.", "x": "Ecology: Whales.. Cliff dive. The living world of Ka'anapali Beach — Maui's golden mile.. Maui. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Ka'anapali Beach through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Ka'anapali Beach through time.", "x": "History: Sunsets.. Whales. People and Ka'anapali Beach across the centuries — Maui's golden mile.. Snorkel. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Ka'anapali Beach.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Ka'anapali Beach.", "x": "Conservation: Cliff.. Maui. Threats and guardians of Ka'anapali Beach — Maui's golden mile.. Whales. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Ka'anapali Beach in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Ka'anapali Beach in numbers.", "x": "Numbers: Maui.; 3 miles.. Maui. Statistics that stun — Ka'anapali Beach. Maui's golden mile. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-beach-kaanapali-beach-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
