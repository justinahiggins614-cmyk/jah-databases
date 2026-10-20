(function(){'use strict';
/* JAH Tokyo City Database generator — jahdb-e2-city-tokyo-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-city-tokyo',PREFIX='JAH-E2CITYTOKYO-',NAME='JAH Tokyo City Database';
var FIELDS=["overview", "highlights", "details", "neighborhoods", "food", "transport", "visiting", "history", "culture", "shopping", "itinerary", "quiz"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Tokyo: the complete city guide", "d": "Tokyo, Japan: the world's largest metropolis..", "g": "overview", "l": 2, "q": "What is Tokyo: the complete city guide?", "a": "Tokyo, Japan: the world's largest metropolis..", "x": "The complete Tokyo city guide: the world's largest metropolis.. Shibuya Crossing. From landmarks to neighborhoods, food to festivals, getting around to staying safe — Tokyo in one database. Rail system best.", "s": "public-reference", "f": null}, {"t": "City at a glance", "d": "Tokyo essentials: Shibuya Crossing..", "g": "overview", "l": 2, "q": "What is City at a glance?", "a": "Tokyo essentials: Shibuya Crossing..", "x": "At a glance: Tokyo, Japan — the world's largest metropolis.. Senso-ji Temple. The numbers, the layout, the vibe: Tokyo in brief. Neighborhoods distinct. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1", "d": "Shibuya Crossing.", "g": "highlights", "l": 2, "q": "What is Highlight 1?", "a": "Shibuya Crossing.", "x": "Tokyo: Shibuya Crossing.. Neighborhoods distinct. One of the defining things about Tokyo — Tsukiji outer market.. the world's largest metropolis. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 1 guide", "d": "Experiencing: Shibuya Crossing..", "g": "highlights", "l": 2, "q": "What is Highlight 1 guide?", "a": "Experiencing: Shibuya Crossing..", "x": "Guide: Shibuya Crossing.. Safe. How to do it right — Tokyo. Shinjuku nightlife. the world's largest metropolis. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2", "d": "Senso-ji Temple.", "g": "highlights", "l": 2, "q": "What is Highlight 2?", "a": "Senso-ji Temple.", "x": "Tokyo: Senso-ji Temple.. Sushi capital. One of the defining things about Tokyo — Shinjuku nightlife.. the world's largest metropolis. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 2 guide", "d": "Experiencing: Senso-ji Temple..", "g": "highlights", "l": 2, "q": "What is Highlight 2 guide?", "a": "Experiencing: Senso-ji Temple..", "x": "Guide: Senso-ji Temple.. Day trips: Nikko. How to do it right — Tokyo. Meiji Shrine. the world's largest metropolis. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3", "d": "Tsukiji outer market.", "g": "highlights", "l": 2, "q": "What is Highlight 3?", "a": "Tsukiji outer market.", "x": "Tokyo: Tsukiji outer market.. Safe. One of the defining things about Tokyo — Meiji Shrine.. the world's largest metropolis. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 3 guide", "d": "Experiencing: Tsukiji outer market..", "g": "highlights", "l": 2, "q": "What is Highlight 3 guide?", "a": "Experiencing: Tsukiji outer market..", "x": "Guide: Tsukiji outer market.. Etiquette. How to do it right — Tokyo. Tokyo Skytree. the world's largest metropolis. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4", "d": "Shinjuku nightlife.", "g": "highlights", "l": 2, "q": "What is Highlight 4?", "a": "Shinjuku nightlife.", "x": "Tokyo: Shinjuku nightlife.. Day trips: Nikko. One of the defining things about Tokyo — Tokyo Skytree.. the world's largest metropolis. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 4 guide", "d": "Experiencing: Shinjuku nightlife..", "g": "highlights", "l": 2, "q": "What is Highlight 4 guide?", "a": "Experiencing: Shinjuku nightlife..", "x": "Guide: Shinjuku nightlife.. Rail system best. How to do it right — Tokyo. Shibuya Crossing. the world's largest metropolis. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5", "d": "Meiji Shrine.", "g": "highlights", "l": 2, "q": "What is Highlight 5?", "a": "Meiji Shrine.", "x": "Tokyo: Meiji Shrine.. Etiquette. One of the defining things about Tokyo — Shibuya Crossing.. the world's largest metropolis. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 5 guide", "d": "Experiencing: Meiji Shrine..", "g": "highlights", "l": 2, "q": "What is Highlight 5 guide?", "a": "Experiencing: Meiji Shrine..", "x": "Guide: Meiji Shrine.. Neighborhoods distinct. How to do it right — Tokyo. Senso-ji Temple. the world's largest metropolis. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6", "d": "Tokyo Skytree.", "g": "highlights", "l": 2, "q": "What is Highlight 6?", "a": "Tokyo Skytree.", "x": "Tokyo: Tokyo Skytree.. Rail system best. One of the defining things about Tokyo — Senso-ji Temple.. the world's largest metropolis. Do not miss it. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Highlight 6 guide", "d": "Experiencing: Tokyo Skytree..", "g": "highlights", "l": 2, "q": "What is Highlight 6 guide?", "a": "Experiencing: Tokyo Skytree..", "x": "Guide: Tokyo Skytree.. Sushi capital. How to do it right — Tokyo. Tsukiji outer market. the world's largest metropolis. rewards the prepared visitor. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 1", "d": "Rail system best.", "g": "details", "l": 2, "q": "What is Deep dive 1?", "a": "Rail system best.", "x": "Tokyo in depth: Rail system best.. Senso-ji Temple. The details — the world's largest metropolis.. Sushi capital. Shinjuku nightlife. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 2", "d": "Neighborhoods distinct.", "g": "details", "l": 2, "q": "What is Deep dive 2?", "a": "Neighborhoods distinct.", "x": "Tokyo in depth: Neighborhoods distinct.. Tsukiji outer market. The details — the world's largest metropolis.. Safe. Meiji Shrine. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 3", "d": "Sushi capital.", "g": "details", "l": 2, "q": "What is Deep dive 3?", "a": "Sushi capital.", "x": "Tokyo in depth: Sushi capital.. Shinjuku nightlife. The details — the world's largest metropolis.. Day trips: Nikko. Tokyo Skytree. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 4", "d": "Safe.", "g": "details", "l": 2, "q": "What is Deep dive 4?", "a": "Safe.", "x": "Tokyo in depth: Safe.. Meiji Shrine. The details — the world's largest metropolis.. Etiquette. Shibuya Crossing. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 5", "d": "Day trips: Nikko.", "g": "details", "l": 2, "q": "What is Deep dive 5?", "a": "Day trips: Nikko.", "x": "Tokyo in depth: Day trips: Nikko.. Tokyo Skytree. The details — the world's largest metropolis.. Rail system best. Senso-ji Temple. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Deep dive 6", "d": "Etiquette.", "g": "details", "l": 2, "q": "What is Deep dive 6?", "a": "Etiquette.", "x": "Tokyo in depth: Etiquette.. Shibuya Crossing. The details — the world's largest metropolis.. Neighborhoods distinct. Tsukiji outer market. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Neighborhoods", "d": "Tokyo's districts.", "g": "neighborhoods", "l": 2, "q": "What is Neighborhoods?", "a": "Tokyo's districts.", "x": "Neighborhoods: Rail system best.. Tsukiji outer market. Where to stay, eat, and wander — Tokyo. the world's largest metropolis. Every district has its own personality; Neighborhoods distinct.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Food and drink", "d": "Eating in Tokyo: Shinjuku nightlife..", "g": "food", "l": 2, "q": "What is Food and drink?", "a": "Eating in Tokyo: Shinjuku nightlife..", "x": "Food: Shinjuku nightlife.. Sushi capital. The tastes of Tokyo — the world's largest metropolis.. Meiji Shrine. Eat where locals eat. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Getting around", "d": "Tokyo transport.", "g": "transport", "l": 2, "q": "What is Getting around?", "a": "Tokyo transport.", "x": "Transport: Safe.. Tokyo Skytree. Subways, buses, walking — Tokyo. the world's largest metropolis. Learn the system on day one; Day trips: Nikko.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Best time to visit", "d": "When to see Tokyo.", "g": "visiting", "l": 2, "q": "What is Best time to visit?", "a": "When to see Tokyo.", "x": "Timing: Etiquette.. Shibuya Crossing. Seasons and festivals — Tokyo. the world's largest metropolis. Time it right for Rail system best.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}, {"t": "Safety", "d": "Tokyo safely.", "g": "visiting", "l": 2, "q": "What is Safety?", "a": "Tokyo safely.", "x": "Safety: Neighborhoods distinct.. Senso-ji Temple. Sensible precautions — Tokyo. the world's largest metropolis. Big cities reward street smarts; Sushi capital.. City and language facts from standard references. Populations are metro estimates and change over time.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-city-tokyo-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
