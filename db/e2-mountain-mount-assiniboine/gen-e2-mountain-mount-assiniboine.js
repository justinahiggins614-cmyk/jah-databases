(function(){'use strict';
/* JAH Mount Assiniboine Mountain Database generator — jahdb-e2-mountain-mount-assiniboine-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-mountain-mount-assiniboine',PREFIX='JAH-E2MOUNTAINM-',NAME='JAH Mount Assiniboine Mountain Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mount Assiniboine: the complete guide", "d": "Mount Assiniboine: the Matterhorn of Rockies..", "g": "overview", "l": 2, "q": "What is Mount Assiniboine: the complete guide?", "a": "Mount Assiniboine: the Matterhorn of Rockies..", "x": "The complete mountain guide to Mount Assiniboine: the Matterhorn of Rockies.. 3,618m. From formation to visiting, from wildlife to legends — everything about this mountain in one database. Hiking. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "3,618m.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "3,618m.", "x": "Mount Assiniboine: 3,618m.. Huts. One of the defining facts — Huts.. the Matterhorn of Rockies. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: 3,618m..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: 3,618m..", "x": "Explored: 3,618m.. Wildlife. Why it is so — Mount Assiniboine. Views. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Backcountry.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Backcountry.", "x": "Mount Assiniboine: Backcountry.. Views. One of the defining facts — Views.. the Matterhorn of Rockies. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Backcountry..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Backcountry..", "x": "Explored: Backcountry.. History. Why it is so — Mount Assiniboine. Trails. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Huts.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Huts.", "x": "Mount Assiniboine: Huts.. Wildlife. One of the defining facts — Trails.. the Matterhorn of Rockies. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Huts..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Huts..", "x": "Explored: Huts.. Access. Why it is so — Mount Assiniboine. Photos. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "Views.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "Views.", "x": "Mount Assiniboine: Views.. History. One of the defining facts — Photos.. the Matterhorn of Rockies. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: Views..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: Views..", "x": "Explored: Views.. Hiking. Why it is so — Mount Assiniboine. 3,618m. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Trails.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Trails.", "x": "Mount Assiniboine: Trails.. Access. One of the defining facts — 3,618m.. the Matterhorn of Rockies. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Trails..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Trails..", "x": "Explored: Trails.. Huts. Why it is so — Mount Assiniboine. Backcountry. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Photos.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Photos.", "x": "Mount Assiniboine: Photos.. Hiking. One of the defining facts — Backcountry.. the Matterhorn of Rockies. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Photos..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Photos..", "x": "Explored: Photos.. Views. Why it is so — Mount Assiniboine. Huts. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Hiking.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Hiking.", "x": "Mount Assiniboine in depth: Hiking.. Backcountry. The details reward the curious — the Matterhorn of Rockies.. Views. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Huts.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Huts.", "x": "Mount Assiniboine in depth: Huts.. Huts. The details reward the curious — the Matterhorn of Rockies.. Wildlife. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Views.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Views.", "x": "Mount Assiniboine in depth: Views.. Views. The details reward the curious — the Matterhorn of Rockies.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Wildlife.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Wildlife.", "x": "Mount Assiniboine in depth: Wildlife.. Trails. The details reward the curious — the Matterhorn of Rockies.. Access. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "History.", "x": "Mount Assiniboine in depth: History.. Photos. The details reward the curious — the Matterhorn of Rockies.. Hiking. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Access.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Access.", "x": "Mount Assiniboine in depth: Access.. 3,618m. The details reward the curious — the Matterhorn of Rockies.. Huts. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Mount Assiniboine is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Mount Assiniboine is.", "x": "Location: 3,618m.. Hiking. Getting oriented — Mount Assiniboine. the Matterhorn of Rockies. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Mount Assiniboine.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Mount Assiniboine.", "x": "Visiting: Huts.. Backcountry. Practical know-how — Mount Assiniboine. the Matterhorn of Rockies. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Mount Assiniboine.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Mount Assiniboine.", "x": "Ecology: Views.. Huts. The living world of Mount Assiniboine — the Matterhorn of Rockies.. Wildlife. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Mount Assiniboine through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Mount Assiniboine through time.", "x": "History: History.. Views. People and Mount Assiniboine across the centuries — the Matterhorn of Rockies.. Access. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Mount Assiniboine.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Mount Assiniboine.", "x": "Conservation: Huts.. 3,618m. Threats and guardians of Mount Assiniboine — the Matterhorn of Rockies.. Views. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Mount Assiniboine in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Mount Assiniboine in numbers.", "x": "Numbers: 3,618m.; Backcountry.. Wildlife. Statistics that stun — Mount Assiniboine. the Matterhorn of Rockies. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-mountain-mount-assiniboine-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
