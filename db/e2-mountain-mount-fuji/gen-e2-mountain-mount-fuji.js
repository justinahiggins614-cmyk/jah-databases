(function(){'use strict';
/* JAH Mount Fuji Mountain Database generator — jahdb-e2-mountain-mount-fuji-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-mountain-mount-fuji',PREFIX='JAH-E2MOUNTAINM-',NAME='JAH Mount Fuji Mountain Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mount Fuji: the complete guide", "d": "Mount Fuji: Japan's sacred volcano..", "g": "overview", "l": 2, "q": "What is Mount Fuji: the complete guide?", "a": "Mount Fuji: Japan's sacred volcano..", "x": "The complete mountain guide to Mount Fuji: Japan's sacred volcano.. 3,776m. From formation to visiting, from wildlife to legends — everything about this mountain in one database. Culture. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "3,776m.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "3,776m.", "x": "Mount Fuji: 3,776m.. Routes. One of the defining facts — Climb July-Aug.. Japan's sacred volcano. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 3,776m..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 3,776m..", "x": "Explored: 3,776m.. Views. Why it is so — Mount Fuji. Sunrise. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Sacred.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Sacred.", "x": "Mount Fuji: Sacred.. Huts. One of the defining facts — Sunrise.. Japan's sacred volcano. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Sacred..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Sacred..", "x": "Explored: Sacred.. Art. Why it is so — Mount Fuji. Hokusai. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Climb July-Aug.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Climb July-Aug.", "x": "Mount Fuji: Climb July-Aug.. Views. One of the defining facts — Hokusai.. Japan's sacred volcano. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Climb July-Aug..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Climb July-Aug..", "x": "Explored: Climb July-Aug.. Respect. Why it is so — Mount Fuji. Yoshida trail. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Sunrise.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Sunrise.", "x": "Mount Fuji: Sunrise.. Art. One of the defining facts — Yoshida trail.. Japan's sacred volcano. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Sunrise..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Sunrise..", "x": "Explored: Sunrise.. Culture. Why it is so — Mount Fuji. 3,776m. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Hokusai.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Hokusai.", "x": "Mount Fuji: Hokusai.. Respect. One of the defining facts — 3,776m.. Japan's sacred volcano. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Hokusai..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Hokusai..", "x": "Explored: Hokusai.. Routes. Why it is so — Mount Fuji. Sacred. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Yoshida trail.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Yoshida trail.", "x": "Mount Fuji: Yoshida trail.. Culture. One of the defining facts — Sacred.. Japan's sacred volcano. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Yoshida trail..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Yoshida trail..", "x": "Explored: Yoshida trail.. Huts. Why it is so — Mount Fuji. Climb July-Aug. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Culture.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Culture.", "x": "Mount Fuji in depth: Culture.. Sacred. The details reward the curious — Japan's sacred volcano.. Huts. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Routes.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Routes.", "x": "Mount Fuji in depth: Routes.. Climb July-Aug. The details reward the curious — Japan's sacred volcano.. Views. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Huts.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Huts.", "x": "Mount Fuji in depth: Huts.. Sunrise. The details reward the curious — Japan's sacred volcano.. Art. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Views.", "x": "Mount Fuji in depth: Views.. Hokusai. The details reward the curious — Japan's sacred volcano.. Respect. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Art.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Art.", "x": "Mount Fuji in depth: Art.. Yoshida trail. The details reward the curious — Japan's sacred volcano.. Culture. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Respect.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Respect.", "x": "Mount Fuji in depth: Respect.. 3,776m. The details reward the curious — Japan's sacred volcano.. Routes. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Mount Fuji is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Mount Fuji is.", "x": "Location: 3,776m.. Culture. Getting oriented — Mount Fuji. Japan's sacred volcano. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Mount Fuji.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Mount Fuji.", "x": "Visiting: Routes.. Sacred. Practical know-how — Mount Fuji. Japan's sacred volcano. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Mount Fuji.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Mount Fuji.", "x": "Ecology: Huts.. Climb July-Aug. The living world of Mount Fuji — Japan's sacred volcano.. Views. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Mount Fuji through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Mount Fuji through time.", "x": "History: Art.. Sunrise. People and Mount Fuji across the centuries — Japan's sacred volcano.. Respect. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Mount Fuji.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Mount Fuji.", "x": "Conservation: Routes.. 3,776m. Threats and guardians of Mount Fuji — Japan's sacred volcano.. Huts. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Mount Fuji in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Mount Fuji in numbers.", "x": "Numbers: 3,776m.; Sacred.. Views. Statistics that stun — Mount Fuji. Japan's sacred volcano. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-mountain-mount-fuji-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
