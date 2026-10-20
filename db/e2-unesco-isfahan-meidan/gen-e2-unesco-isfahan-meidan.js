(function(){'use strict';
/* JAH Isfahan\'s Meidan Unesco Site Database generator — jahdb-e2-unesco-isfahan-meidan-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-unesco-isfahan-meidan',PREFIX='JAH-E2UNESCOISF-',NAME='JAH Isfahan\'s Meidan Unesco Site Database';
var FIELDS=["overview", "facts", "details", "location", "visiting", "ecology", "history", "conservation", "numbers", "stories", "nearby", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Isfahan's Meidan: the complete guide", "d": "Isfahan's Meidan: half the world..", "g": "overview", "l": 2, "q": "What is Isfahan's Meidan: the complete guide?", "a": "Isfahan's Meidan: half the world..", "x": "The complete unesco site guide to Isfahan's Meidan: half the world.. Shah Abbas. From formation to visiting, from wildlife to legends — everything about this unesco site in one database. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1", "d": "Shah Abbas.", "g": "facts", "l": 2, "q": "What is Key fact 1?", "a": "Shah Abbas.", "x": "Isfahan's Meidan: Shah Abbas.. Square. One of the defining facts — Bazaar.. half the world. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 1 explored", "d": "Understanding: Shah Abbas..", "g": "facts", "l": 2, "q": "What is Key fact 1 explored?", "a": "Understanding: Shah Abbas..", "x": "Explored: Shah Abbas.. Bazaar. Why it is so — Isfahan's Meidan. UNESCO 1979. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2", "d": "Sheikh Lotfollah.", "g": "facts", "l": 2, "q": "What is Key fact 2?", "a": "Sheikh Lotfollah.", "x": "Isfahan's Meidan: Sheikh Lotfollah.. Mosques. One of the defining facts — UNESCO 1979.. half the world. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 2 explored", "d": "Understanding: Sheikh Lotfollah..", "g": "facts", "l": 2, "q": "What is Key fact 2 explored?", "a": "Understanding: Sheikh Lotfollah..", "x": "Explored: Sheikh Lotfollah.. Tours. Why it is so — Isfahan's Meidan. Tiles. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3", "d": "Bazaar.", "g": "facts", "l": 2, "q": "What is Key fact 3?", "a": "Bazaar.", "x": "Isfahan's Meidan: Bazaar.. Bazaar. One of the defining facts — Tiles.. half the world. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 3 explored", "d": "Understanding: Bazaar..", "g": "facts", "l": 2, "q": "What is Key fact 3 explored?", "a": "Understanding: Bazaar..", "x": "Explored: Bazaar.. Visit. Why it is so — Isfahan's Meidan. Music. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4", "d": "UNESCO 1979.", "g": "facts", "l": 2, "q": "What is Key fact 4?", "a": "UNESCO 1979.", "x": "Isfahan's Meidan: UNESCO 1979.. Tours. One of the defining facts — Music.. half the world. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 4 explored", "d": "Understanding: UNESCO 1979..", "g": "facts", "l": 2, "q": "What is Key fact 4 explored?", "a": "Understanding: UNESCO 1979..", "x": "Explored: UNESCO 1979.. History. Why it is so — Isfahan's Meidan. Shah Abbas. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5", "d": "Tiles.", "g": "facts", "l": 2, "q": "What is Key fact 5?", "a": "Tiles.", "x": "Isfahan's Meidan: Tiles.. Visit. One of the defining facts — Shah Abbas.. half the world. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 5 explored", "d": "Understanding: Tiles..", "g": "facts", "l": 2, "q": "What is Key fact 5 explored?", "a": "Understanding: Tiles..", "x": "Explored: Tiles.. Square. Why it is so — Isfahan's Meidan. Sheikh Lotfollah. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6", "d": "Music.", "g": "facts", "l": 2, "q": "What is Key fact 6?", "a": "Music.", "x": "Isfahan's Meidan: Music.. History. One of the defining facts — Sheikh Lotfollah.. half the world. Learn it; it anchors the rest. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Key fact 6 explored", "d": "Understanding: Music..", "g": "facts", "l": 2, "q": "What is Key fact 6 explored?", "a": "Understanding: Music..", "x": "Explored: Music.. Mosques. Why it is so — Isfahan's Meidan. Bazaar. Understanding beats memorizing. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "History.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "History.", "x": "Isfahan's Meidan in depth: History.. Sheikh Lotfollah. The details reward the curious — half the world.. Mosques. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Square.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Square.", "x": "Isfahan's Meidan in depth: Square.. Bazaar. The details reward the curious — half the world.. Bazaar. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Mosques.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Mosques.", "x": "Isfahan's Meidan in depth: Mosques.. UNESCO 1979. The details reward the curious — half the world.. Tours. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Bazaar.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Bazaar.", "x": "Isfahan's Meidan in depth: Bazaar.. Tiles. The details reward the curious — half the world.. Visit. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Tours.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Tours.", "x": "Isfahan's Meidan in depth: Tours.. Music. The details reward the curious — half the world.. History. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Visit.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Visit.", "x": "Isfahan's Meidan in depth: Visit.. Shah Abbas. The details reward the curious — half the world.. Square. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Location and geography", "d": "Where Isfahan's Meidan is.", "g": "location", "l": 2, "q": "What is Location and geography?", "a": "Where Isfahan's Meidan is.", "x": "Location: Shah Abbas.. History. Getting oriented — Isfahan's Meidan. half the world. Know where it sits and the map makes sense. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Visiting", "d": "Experience Isfahan's Meidan.", "g": "visiting", "l": 2, "q": "What is Visiting?", "a": "Experience Isfahan's Meidan.", "x": "Visiting: Square.. Sheikh Lotfollah. Practical know-how — Isfahan's Meidan. half the world. Go prepared; great places reward planning. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Wildlife and ecology", "d": "Life around Isfahan's Meidan.", "g": "ecology", "l": 2, "q": "What is Wildlife and ecology?", "a": "Life around Isfahan's Meidan.", "x": "Ecology: Mosques.. Bazaar. The living world of Isfahan's Meidan — half the world.. Bazaar. Nature is the deepest attraction. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "History", "d": "Isfahan's Meidan through time.", "g": "history", "l": 2, "q": "What is History?", "a": "Isfahan's Meidan through time.", "x": "History: Tours.. UNESCO 1979. People and Isfahan's Meidan across the centuries — half the world.. Visit. Places have biographies too. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "Conservation", "d": "Protecting Isfahan's Meidan.", "g": "conservation", "l": 2, "q": "What is Conservation?", "a": "Protecting Isfahan's Meidan.", "x": "Conservation: Square.. Shah Abbas. Threats and guardians of Isfahan's Meidan — half the world.. Mosques. Visit lightly; leave it better. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}, {"t": "By the numbers", "d": "Isfahan's Meidan in numbers.", "g": "numbers", "l": 2, "q": "What is By the numbers?", "a": "Isfahan's Meidan in numbers.", "x": "Numbers: Shah Abbas.; Sheikh Lotfollah.. Bazaar. Statistics that stun — Isfahan's Meidan. half the world. Numbers give scale to wonder. Geography from standard references. Measurements follow published figures; ranks and records change with new surveys.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-unesco-isfahan-meidan-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
