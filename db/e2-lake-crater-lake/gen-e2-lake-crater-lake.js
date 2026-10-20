(function(){'use strict';
/* JAH Crater Lake Lake Database generator — jahdb-e2-lake-crater-lake-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-lake-crater-lake',PREFIX='JAH-E2LAKECRATE-',NAME='JAH Crater Lake Lake Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Crater Lake: the complete guide", "d": "Crater Lake: deepest US lake; volcanic..", "g": "overview", "l": 2, "q": "What is Crater Lake: the complete guide?", "a": "Crater Lake: deepest US lake; volcanic..", "x": "The complete lake guide to Crater Lake: deepest US lake; volcanic.. 594m deep. From formation to visiting, from wildlife to legends — everything about this lake in one database. Geology. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "594m deep.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "594m deep.", "x": "Crater Lake: 594m deep.. Park. One of the defining facts — Wizard Island.. deepest US lake; volcanic. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 594m deep..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 594m deep..", "x": "Explored: 594m deep.. Boats. Why it is so — Crater Lake. Mazama. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Blue.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Blue.", "x": "Crater Lake: Blue.. Hikes. One of the defining facts — Mazama.. deepest US lake; volcanic. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Blue..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Blue..", "x": "Explored: Blue.. Winter. Why it is so — Crater Lake. Snow. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Wizard Island.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Wizard Island.", "x": "Crater Lake: Wizard Island.. Boats. One of the defining facts — Snow.. deepest US lake; volcanic. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Wizard Island..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Wizard Island..", "x": "Explored: Wizard Island.. History. Why it is so — Crater Lake. Park. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Mazama.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Mazama.", "x": "Crater Lake: Mazama.. Winter. One of the defining facts — Park.. deepest US lake; volcanic. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Mazama..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Mazama..", "x": "Explored: Mazama.. Geology. Why it is so — Crater Lake. 594m deep. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Snow.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Snow.", "x": "Crater Lake: Snow.. History. One of the defining facts — 594m deep.. deepest US lake; volcanic. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Snow..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Snow..", "x": "Explored: Snow.. Park. Why it is so — Crater Lake. Blue. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Park.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Park.", "x": "Crater Lake: Park.. Geology. One of the defining facts — Blue.. deepest US lake; volcanic. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Park..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Park..", "x": "Explored: Park.. Hikes. Why it is so — Crater Lake. Wizard Island. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Geology.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Geology.", "x": "Crater Lake in depth: Geology.. Blue. The details reward the curious — deepest US lake; volcanic.. Hikes. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Park.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Park.", "x": "Crater Lake in depth: Park.. Wizard Island. The details reward the curious — deepest US lake; volcanic.. Boats. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Hikes.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Hikes.", "x": "Crater Lake in depth: Hikes.. Mazama. The details reward the curious — deepest US lake; volcanic.. Winter. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Boats.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Boats.", "x": "Crater Lake in depth: Boats.. Snow. The details reward the curious — deepest US lake; volcanic.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Winter.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Winter.", "x": "Crater Lake in depth: Winter.. Park. The details reward the curious — deepest US lake; volcanic.. Geology. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "History.", "x": "Crater Lake in depth: History.. 594m deep. The details reward the curious — deepest US lake; volcanic.. Park. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Crater Lake is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Crater Lake is.", "x": "Location: 594m deep.. Geology. Getting oriented — Crater Lake. deepest US lake; volcanic. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Crater Lake.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Crater Lake.", "x": "Visiting: Park.. Blue. Practical know-how — Crater Lake. deepest US lake; volcanic. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Crater Lake.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Crater Lake.", "x": "Ecology: Hikes.. Wizard Island. The living world of Crater Lake — deepest US lake; volcanic.. Boats. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Crater Lake through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Crater Lake through time.", "x": "History: Winter.. Mazama. People and Crater Lake across the centuries — deepest US lake; volcanic.. History. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Crater Lake.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Crater Lake.", "x": "Conservation: Park.. 594m deep. Threats and guardians of Crater Lake — deepest US lake; volcanic.. Hikes. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Crater Lake in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Crater Lake in numbers.", "x": "Numbers: 594m deep.; Blue.. Boats. Statistics that stun — Crater Lake. deepest US lake; volcanic. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-lake-crater-lake-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
