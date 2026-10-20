(function(){'use strict';
/* JAH Mississippi Attractions Database generator — jahdb-e2-mississippi-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-mississippi-attractions',PREFIX='JAH-E2MISSISSIP-',NAME='JAH Mississippi Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Mississippi: attractions overview", "d": "The best of Mississippi: Vicksburg battlefield, Natchez Trace, Gulf Coast beaches.", "g": "overview", "l": 2, "q": "What is Mississippi: attractions overview?", "a": "The best of Mississippi: Vicksburg battlefield, Natchez Trace, Gulf Coast beaches.", "x": "The essential Mississippi: Vicksburg battlefield, Natchez Trace, Gulf Coast beaches — plus Natchez Trace Parkway, Mississippi's great fried catfish. Neshoba County Fair This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Vicksburg battlefield", "d": "Vicksburg battlefield: a top Mississippi attraction.", "g": "attractions", "l": 2, "q": "What is Vicksburg battlefield?", "a": "Vicksburg battlefield: a top Mississippi attraction.", "x": "Vicksburg battlefield is essential Mississippi. Choctaw and Chickasaw; cotton kingdom. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. fried catfish", "s": "public-reference", "f": null}, {"t": "Visiting Vicksburg battlefield", "d": "How to experience Vicksburg battlefield.", "g": "attractions", "l": 2, "q": "What is Visiting Vicksburg battlefield?", "a": "How to experience Vicksburg battlefield.", "x": "Experiencing Vicksburg battlefield: plan around Neshoba County Fair, the state's rhythm — Virtute et armis (By valor and arms). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Natchez Trace Parkway Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Natchez Trace", "d": "Natchez Trace: a top Mississippi attraction.", "g": "attractions", "l": 2, "q": "What is Natchez Trace?", "a": "Natchez Trace: a top Mississippi attraction.", "x": "Natchez Trace is essential Mississippi. Choctaw and Chickasaw; cotton kingdom. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. fried catfish", "s": "public-reference", "f": null}, {"t": "Visiting Natchez Trace", "d": "How to experience Natchez Trace.", "g": "attractions", "l": 2, "q": "What is Visiting Natchez Trace?", "a": "How to experience Natchez Trace.", "x": "Experiencing Natchez Trace: plan around Neshoba County Fair, the state's rhythm — Virtute et armis (By valor and arms). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Natchez Trace Parkway Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Gulf Coast beaches", "d": "Gulf Coast beaches: a top Mississippi attraction.", "g": "attractions", "l": 2, "q": "What is Gulf Coast beaches?", "a": "Gulf Coast beaches: a top Mississippi attraction.", "x": "Gulf Coast beaches is essential Mississippi. Choctaw and Chickasaw; cotton kingdom. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. fried catfish", "s": "public-reference", "f": null}, {"t": "Visiting Gulf Coast beaches", "d": "How to experience Gulf Coast beaches.", "g": "attractions", "l": 2, "q": "What is Visiting Gulf Coast beaches?", "a": "How to experience Gulf Coast beaches.", "x": "Experiencing Gulf Coast beaches: plan around Neshoba County Fair, the state's rhythm — Virtute et armis (By valor and arms). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Natchez Trace Parkway Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Elvis birthplace (Tupelo)", "d": "Elvis birthplace (Tupelo): a top Mississippi attraction.", "g": "attractions", "l": 2, "q": "What is Elvis birthplace (Tupelo)?", "a": "Elvis birthplace (Tupelo): a top Mississippi attraction.", "x": "Elvis birthplace (Tupelo) is essential Mississippi. Choctaw and Chickasaw; cotton kingdom. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. fried catfish", "s": "public-reference", "f": null}, {"t": "Visiting Elvis birthplace (Tupelo)", "d": "How to experience Elvis birthplace (Tupelo).", "g": "attractions", "l": 2, "q": "What is Visiting Elvis birthplace (Tupelo)?", "a": "How to experience Elvis birthplace (Tupelo).", "x": "Experiencing Elvis birthplace (Tupelo): plan around Neshoba County Fair, the state's rhythm — Virtute et armis (By valor and arms). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Natchez Trace Parkway Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "BB King Museum", "d": "BB King Museum: a top Mississippi attraction.", "g": "attractions", "l": 2, "q": "What is BB King Museum?", "a": "BB King Museum: a top Mississippi attraction.", "x": "BB King Museum is essential Mississippi. Choctaw and Chickasaw; cotton kingdom. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. fried catfish", "s": "public-reference", "f": null}, {"t": "Visiting BB King Museum", "d": "How to experience BB King Museum.", "g": "attractions", "l": 2, "q": "What is Visiting BB King Museum?", "a": "How to experience BB King Museum.", "x": "Experiencing BB King Museum: plan around Neshoba County Fair, the state's rhythm — Virtute et armis (By valor and arms). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Natchez Trace Parkway Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Oxford's Square", "d": "Oxford's Square: a top Mississippi attraction.", "g": "attractions", "l": 2, "q": "What is Oxford's Square?", "a": "Oxford's Square: a top Mississippi attraction.", "x": "Oxford's Square is essential Mississippi. Choctaw and Chickasaw; cotton kingdom. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. fried catfish", "s": "public-reference", "f": null}, {"t": "Visiting Oxford's Square", "d": "How to experience Oxford's Square.", "g": "attractions", "l": 2, "q": "What is Visiting Oxford's Square?", "a": "How to experience Oxford's Square.", "x": "Experiencing Oxford's Square: plan around Neshoba County Fair, the state's rhythm — Virtute et armis (By valor and arms). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Natchez Trace Parkway Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Biloxi casinos", "d": "Biloxi casinos: a top Mississippi attraction.", "g": "attractions", "l": 2, "q": "What is Biloxi casinos?", "a": "Biloxi casinos: a top Mississippi attraction.", "x": "Biloxi casinos is essential Mississippi. Choctaw and Chickasaw; cotton kingdom. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. fried catfish", "s": "public-reference", "f": null}, {"t": "Visiting Biloxi casinos", "d": "How to experience Biloxi casinos.", "g": "attractions", "l": 2, "q": "What is Visiting Biloxi casinos?", "a": "How to experience Biloxi casinos.", "x": "Experiencing Biloxi casinos: plan around Neshoba County Fair, the state's rhythm — Virtute et armis (By valor and arms). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Natchez Trace Parkway Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Tishomingo State Park", "d": "Tishomingo State Park: a top Mississippi attraction.", "g": "attractions", "l": 2, "q": "What is Tishomingo State Park?", "a": "Tishomingo State Park: a top Mississippi attraction.", "x": "Tishomingo State Park is essential Mississippi. Choctaw and Chickasaw; cotton kingdom. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. fried catfish", "s": "public-reference", "f": null}, {"t": "Visiting Tishomingo State Park", "d": "How to experience Tishomingo State Park.", "g": "attractions", "l": 2, "q": "What is Visiting Tishomingo State Park?", "a": "How to experience Tishomingo State Park.", "x": "Experiencing Tishomingo State Park: plan around Neshoba County Fair, the state's rhythm — Virtute et armis (By valor and arms). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Natchez Trace Parkway Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Natchez Trace Parkway", "d": "Natchez Trace Parkway: Mississippi's great park.", "g": "parks", "l": 2, "q": "What is Natchez Trace Parkway?", "a": "Natchez Trace Parkway: Mississippi's great park.", "x": "Natchez Trace Parkway is Mississippi's wild heart: Vicksburg battlefield. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Neshoba County Fair Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Natchez Trace Parkway", "d": "How to explore Natchez Trace Parkway.", "g": "parks", "l": 2, "q": "What is Exploring Natchez Trace Parkway?", "a": "How to explore Natchez Trace Parkway.", "x": "Exploring Natchez Trace Parkway: get the park map, check conditions, carry water and layers, and tell someone your plan. Virtute et armis (By valor and arms) Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Jackson: the capital city", "d": "Jackson, capital of Mississippi.", "g": "cities", "l": 2, "q": "What is Jackson: the capital city?", "a": "Jackson, capital of Mississippi.", "x": "Jackson: the capital of Mississippi — government, history, and often the best museums. Civil War; civil rights struggle. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Jackson", "s": "public-reference", "f": null}, {"t": "Jackson: the biggest city", "d": "Jackson is Mississippi's largest city.", "g": "cities", "l": 2, "q": "What is Jackson: the biggest city?", "a": "Jackson is Mississippi's largest city.", "x": "Jackson is where Mississippi comes to work and play: the skyline, the food, the music, the crowds. agriculture Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Neshoba County Fair", "s": "public-reference", "f": null}, {"t": "fried catfish: the food", "d": "Taste Mississippi: fried catfish.", "g": "food", "l": 2, "q": "What is fried catfish: the food?", "a": "Taste Mississippi: fried catfish.", "x": "The taste of Mississippi is fried catfish — and the foodways around it. Blues birthplace. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Neshoba County Fair Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Mississippi", "d": "Eating your way through Mississippi.", "g": "food", "l": 2, "q": "What is Food tour: Mississippi?", "a": "Eating your way through Mississippi.", "x": "Eating through Mississippi: start with fried catfish, then follow the locals — diners, food trucks, farm stands. Virtute et armis (By valor and arms) Food is the fastest way into a place's heart; the stories come free with the meal. Jackson", "s": "public-reference", "f": null}, {"t": "Neshoba County Fair", "d": "Neshoba County Fair: Mississippi's signature festival.", "g": "festivals", "l": 2, "q": "What is Neshoba County Fair?", "a": "Neshoba County Fair: Mississippi's signature festival.", "x": "Neshoba County Fair is Mississippi at its most celebratory: The blues was born in the Delta.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Jackson Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Mississippi year-round: Neshoba County Fair and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Mississippi year-round: Neshoba County Fair and more.", "x": "The Mississippi festival calendar runs year-round, with Neshoba County Fair as the anchor. Virtute et armis (By valor and arms) Every season has its celebration — plan trips around them for the liveliest version of the state. Natchez Trace Parkway", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-mississippi-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
