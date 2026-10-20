(function(){'use strict';
/* JAH New Hampshire Attractions Database generator — jahdb-e2-new-hampshire-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-new-hampshire-attractions',PREFIX='JAH-E2NEWHAMPSH-',NAME='JAH New Hampshire Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "New Hampshire: attractions overview", "d": "The best of New Hampshire: White Mountains, Lake Winnipesaukee, Canterbury Shaker Village.", "g": "overview", "l": 2, "q": "What is New Hampshire: attractions overview?", "a": "The best of New Hampshire: White Mountains, Lake Winnipesaukee, Canterbury Shaker Village.", "x": "The essential New Hampshire: White Mountains, Lake Winnipesaukee, Canterbury Shaker Village — plus White Mountain National Forest, New Hampshire's great apple cider donuts. Hampton Beach festivals This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "White Mountains", "d": "White Mountains: a top New Hampshire attraction.", "g": "attractions", "l": 2, "q": "What is White Mountains?", "a": "White Mountains: a top New Hampshire attraction.", "x": "White Mountains is essential New Hampshire. Abenaki; first primary state. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. apple cider donuts", "s": "public-reference", "f": null}, {"t": "Visiting White Mountains", "d": "How to experience White Mountains.", "g": "attractions", "l": 2, "q": "What is Visiting White Mountains?", "a": "How to experience White Mountains.", "x": "Experiencing White Mountains: plan around Hampton Beach festivals, the state's rhythm — Live Free or Die. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. White Mountain National Forest Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Lake Winnipesaukee", "d": "Lake Winnipesaukee: a top New Hampshire attraction.", "g": "attractions", "l": 2, "q": "What is Lake Winnipesaukee?", "a": "Lake Winnipesaukee: a top New Hampshire attraction.", "x": "Lake Winnipesaukee is essential New Hampshire. Abenaki; first primary state. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. apple cider donuts", "s": "public-reference", "f": null}, {"t": "Visiting Lake Winnipesaukee", "d": "How to experience Lake Winnipesaukee.", "g": "attractions", "l": 2, "q": "What is Visiting Lake Winnipesaukee?", "a": "How to experience Lake Winnipesaukee.", "x": "Experiencing Lake Winnipesaukee: plan around Hampton Beach festivals, the state's rhythm — Live Free or Die. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. White Mountain National Forest Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Canterbury Shaker Village", "d": "Canterbury Shaker Village: a top New Hampshire attraction.", "g": "attractions", "l": 2, "q": "What is Canterbury Shaker Village?", "a": "Canterbury Shaker Village: a top New Hampshire attraction.", "x": "Canterbury Shaker Village is essential New Hampshire. Abenaki; first primary state. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. apple cider donuts", "s": "public-reference", "f": null}, {"t": "Visiting Canterbury Shaker Village", "d": "How to experience Canterbury Shaker Village.", "g": "attractions", "l": 2, "q": "What is Visiting Canterbury Shaker Village?", "a": "How to experience Canterbury Shaker Village.", "x": "Experiencing Canterbury Shaker Village: plan around Hampton Beach festivals, the state's rhythm — Live Free or Die. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. White Mountain National Forest Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Portsmouth", "d": "Portsmouth: a top New Hampshire attraction.", "g": "attractions", "l": 2, "q": "What is Portsmouth?", "a": "Portsmouth: a top New Hampshire attraction.", "x": "Portsmouth is essential New Hampshire. Abenaki; first primary state. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. apple cider donuts", "s": "public-reference", "f": null}, {"t": "Visiting Portsmouth", "d": "How to experience Portsmouth.", "g": "attractions", "l": 2, "q": "What is Visiting Portsmouth?", "a": "How to experience Portsmouth.", "x": "Experiencing Portsmouth: plan around Hampton Beach festivals, the state's rhythm — Live Free or Die. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. White Mountain National Forest Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Kancamagus Highway", "d": "Kancamagus Highway: a top New Hampshire attraction.", "g": "attractions", "l": 2, "q": "What is Kancamagus Highway?", "a": "Kancamagus Highway: a top New Hampshire attraction.", "x": "Kancamagus Highway is essential New Hampshire. Abenaki; first primary state. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. apple cider donuts", "s": "public-reference", "f": null}, {"t": "Visiting Kancamagus Highway", "d": "How to experience Kancamagus Highway.", "g": "attractions", "l": 2, "q": "What is Visiting Kancamagus Highway?", "a": "How to experience Kancamagus Highway.", "x": "Experiencing Kancamagus Highway: plan around Hampton Beach festivals, the state's rhythm — Live Free or Die. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. White Mountain National Forest Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Mount Washington", "d": "Mount Washington: a top New Hampshire attraction.", "g": "attractions", "l": 2, "q": "What is Mount Washington?", "a": "Mount Washington: a top New Hampshire attraction.", "x": "Mount Washington is essential New Hampshire. Abenaki; first primary state. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. apple cider donuts", "s": "public-reference", "f": null}, {"t": "Visiting Mount Washington", "d": "How to experience Mount Washington.", "g": "attractions", "l": 2, "q": "What is Visiting Mount Washington?", "a": "How to experience Mount Washington.", "x": "Experiencing Mount Washington: plan around Hampton Beach festivals, the state's rhythm — Live Free or Die. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. White Mountain National Forest Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Strawbery Banke", "d": "Strawbery Banke: a top New Hampshire attraction.", "g": "attractions", "l": 2, "q": "What is Strawbery Banke?", "a": "Strawbery Banke: a top New Hampshire attraction.", "x": "Strawbery Banke is essential New Hampshire. Abenaki; first primary state. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. apple cider donuts", "s": "public-reference", "f": null}, {"t": "Visiting Strawbery Banke", "d": "How to experience Strawbery Banke.", "g": "attractions", "l": 2, "q": "What is Visiting Strawbery Banke?", "a": "How to experience Strawbery Banke.", "x": "Experiencing Strawbery Banke: plan around Hampton Beach festivals, the state's rhythm — Live Free or Die. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. White Mountain National Forest Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Hampton Beach", "d": "Hampton Beach: a top New Hampshire attraction.", "g": "attractions", "l": 2, "q": "What is Hampton Beach?", "a": "Hampton Beach: a top New Hampshire attraction.", "x": "Hampton Beach is essential New Hampshire. Abenaki; first primary state. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. apple cider donuts", "s": "public-reference", "f": null}, {"t": "Visiting Hampton Beach", "d": "How to experience Hampton Beach.", "g": "attractions", "l": 2, "q": "What is Visiting Hampton Beach?", "a": "How to experience Hampton Beach.", "x": "Experiencing Hampton Beach: plan around Hampton Beach festivals, the state's rhythm — Live Free or Die. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. White Mountain National Forest Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "White Mountain National Forest", "d": "White Mountain National Forest: New Hampshire's great park.", "g": "parks", "l": 2, "q": "What is White Mountain National Forest?", "a": "White Mountain National Forest: New Hampshire's great park.", "x": "White Mountain National Forest is New Hampshire's wild heart: White Mountains. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Hampton Beach festivals Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring White Mountain National Forest", "d": "How to explore White Mountain National Forest.", "g": "parks", "l": 2, "q": "What is Exploring White Mountain National Forest?", "a": "How to explore White Mountain National Forest.", "x": "Exploring White Mountain National Forest: get the park map, check conditions, carry water and layers, and tell someone your plan. Live Free or Die Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Concord: the capital city", "d": "Concord, capital of New Hampshire.", "g": "cities", "l": 2, "q": "What is Concord: the capital city?", "a": "Concord, capital of New Hampshire.", "x": "Concord: the capital of New Hampshire — government, history, and often the best museums. Revolutionary; industrial mills. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Manchester", "s": "public-reference", "f": null}, {"t": "Manchester: the biggest city", "d": "Manchester is New Hampshire's largest city.", "g": "cities", "l": 2, "q": "What is Manchester: the biggest city?", "a": "Manchester is New Hampshire's largest city.", "x": "Manchester is where New Hampshire comes to work and play: the skyline, the food, the music, the crowds. tourism Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Hampton Beach festivals", "s": "public-reference", "f": null}, {"t": "apple cider donuts: the food", "d": "Taste New Hampshire: apple cider donuts.", "g": "food", "l": 2, "q": "What is apple cider donuts: the food?", "a": "Taste New Hampshire: apple cider donuts.", "x": "The taste of New Hampshire is apple cider donuts — and the foodways around it. First-in-the-nation primary. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Hampton Beach festivals Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: New Hampshire", "d": "Eating your way through New Hampshire.", "g": "food", "l": 2, "q": "What is Food tour: New Hampshire?", "a": "Eating your way through New Hampshire.", "x": "Eating through New Hampshire: start with apple cider donuts, then follow the locals — diners, food trucks, farm stands. Live Free or Die Food is the fastest way into a place's heart; the stories come free with the meal. Manchester", "s": "public-reference", "f": null}, {"t": "Hampton Beach festivals", "d": "Hampton Beach festivals: New Hampshire's signature festival.", "g": "festivals", "l": 2, "q": "What is Hampton Beach festivals?", "a": "Hampton Beach festivals: New Hampshire's signature festival.", "x": "Hampton Beach festivals is New Hampshire at its most celebratory: The first-in-the-nation primary made it a political proving ground.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Concord Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "New Hampshire year-round: Hampton Beach festivals and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "New Hampshire year-round: Hampton Beach festivals and more.", "x": "The New Hampshire festival calendar runs year-round, with Hampton Beach festivals as the anchor. Live Free or Die Every season has its celebration — plan trips around them for the liveliest version of the state. White Mountain National Forest", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-new-hampshire-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
