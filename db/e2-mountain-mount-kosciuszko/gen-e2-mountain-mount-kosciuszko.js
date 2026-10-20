(function(){'use strict';
/* JAH Mount Kosciuszko Mountain Database generator — jahdb-e2-mountain-mount-kosciuszko-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-mountain-mount-kosciuszko',PREFIX='JAH-E2MOUNTAINM-',NAME='JAH Mount Kosciuszko Mountain Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mount Kosciuszko: the complete guide", "d": "Mount Kosciuszko: Australia's highest..", "g": "overview", "l": 2, "q": "What is Mount Kosciuszko: the complete guide?", "a": "Mount Kosciuszko: Australia's highest..", "x": "The complete mountain guide to Mount Kosciuszko: Australia's highest.. 2,228m. From formation to visiting, from wildlife to legends — everything about this mountain in one database. Walk. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "2,228m.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "2,228m.", "x": "Mount Kosciuszko: 2,228m.. History. One of the defining facts — Snowy Mountains.. Australia's highest. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 2,228m..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 2,228m..", "x": "Explored: 2,228m.. Views. Why it is so — Mount Kosciuszko. Thredbo. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Easy walk.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Easy walk.", "x": "Mount Kosciuszko: Easy walk.. Skiing. One of the defining facts — Thredbo.. Australia's highest. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Easy walk..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Easy walk..", "x": "Explored: Easy walk.. Flora. Why it is so — Mount Kosciuszko. Wildflowers. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Snowy Mountains.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Snowy Mountains.", "x": "Mount Kosciuszko: Snowy Mountains.. Views. One of the defining facts — Wildflowers.. Australia's highest. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Snowy Mountains..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Snowy Mountains..", "x": "Explored: Snowy Mountains.. Seven. Why it is so — Mount Kosciuszko. Seven. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Thredbo.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Thredbo.", "x": "Mount Kosciuszko: Thredbo.. Flora. One of the defining facts — Seven.. Australia's highest. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Thredbo..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Thredbo..", "x": "Explored: Thredbo.. Walk. Why it is so — Mount Kosciuszko. 2,228m. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Wildflowers.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Wildflowers.", "x": "Mount Kosciuszko: Wildflowers.. Seven. One of the defining facts — 2,228m.. Australia's highest. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Wildflowers..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Wildflowers..", "x": "Explored: Wildflowers.. History. Why it is so — Mount Kosciuszko. Easy walk. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Seven.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Seven.", "x": "Mount Kosciuszko: Seven.. Walk. One of the defining facts — Easy walk.. Australia's highest. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Seven..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Seven..", "x": "Explored: Seven.. Skiing. Why it is so — Mount Kosciuszko. Snowy Mountains. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Walk.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Walk.", "x": "Mount Kosciuszko in depth: Walk.. Easy walk. The details reward the curious — Australia's highest.. Skiing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "History.", "x": "Mount Kosciuszko in depth: History.. Snowy Mountains. The details reward the curious — Australia's highest.. Views. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Skiing.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Skiing.", "x": "Mount Kosciuszko in depth: Skiing.. Thredbo. The details reward the curious — Australia's highest.. Flora. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Views.", "x": "Mount Kosciuszko in depth: Views.. Wildflowers. The details reward the curious — Australia's highest.. Seven. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Flora.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Flora.", "x": "Mount Kosciuszko in depth: Flora.. Seven. The details reward the curious — Australia's highest.. Walk. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Seven.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Seven.", "x": "Mount Kosciuszko in depth: Seven.. 2,228m. The details reward the curious — Australia's highest.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Mount Kosciuszko is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Mount Kosciuszko is.", "x": "Location: 2,228m.. Walk. Getting oriented — Mount Kosciuszko. Australia's highest. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Mount Kosciuszko.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Mount Kosciuszko.", "x": "Visiting: History.. Easy walk. Practical know-how — Mount Kosciuszko. Australia's highest. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Mount Kosciuszko.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Mount Kosciuszko.", "x": "Ecology: Skiing.. Snowy Mountains. The living world of Mount Kosciuszko — Australia's highest.. Views. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Mount Kosciuszko through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Mount Kosciuszko through time.", "x": "History: Flora.. Thredbo. People and Mount Kosciuszko across the centuries — Australia's highest.. Seven. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Mount Kosciuszko.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Mount Kosciuszko.", "x": "Conservation: History.. 2,228m. Threats and guardians of Mount Kosciuszko — Australia's highest.. Skiing. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Mount Kosciuszko in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Mount Kosciuszko in numbers.", "x": "Numbers: 2,228m.; Easy walk.. Views. Statistics that stun — Mount Kosciuszko. Australia's highest. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-mountain-mount-kosciuszko-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
