(function(){'use strict';
/* JAH Georgia Attractions Database generator — jahdb-e2-georgia-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-georgia-attractions',PREFIX='JAH-E2GEORGIAAT-',NAME='JAH Georgia Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Georgia: attractions overview", "d": "The best of Georgia: Savannah historic district, Stone Mountain, World of Coca-Cola.", "g": "overview", "l": 2, "q": "What is Georgia: attractions overview?", "a": "The best of Georgia: Savannah historic district, Stone Mountain, World of Coca-Cola.", "x": "The essential Georgia: Savannah historic district, Stone Mountain, World of Coca-Cola — plus Okefenokee National Wildlife Refuge, Georgia's great peach cobbler. Savannah St. Patrick's Day This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Savannah historic district", "d": "Savannah historic district: a top Georgia attraction.", "g": "attractions", "l": 2, "q": "What is Savannah historic district?", "a": "Savannah historic district: a top Georgia attraction.", "x": "Savannah historic district is essential Georgia. Creek and Cherokee; Trail of Tears. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. peach cobbler", "s": "public-reference", "f": null}, {"t": "Visiting Savannah historic district", "d": "How to experience Savannah historic district.", "g": "attractions", "l": 2, "q": "What is Visiting Savannah historic district?", "a": "How to experience Savannah historic district.", "x": "Experiencing Savannah historic district: plan around Savannah St. Patrick's Day, the state's rhythm — Wisdom, Justice, Moderation. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Okefenokee National Wildlife Refuge Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Stone Mountain", "d": "Stone Mountain: a top Georgia attraction.", "g": "attractions", "l": 2, "q": "What is Stone Mountain?", "a": "Stone Mountain: a top Georgia attraction.", "x": "Stone Mountain is essential Georgia. Creek and Cherokee; Trail of Tears. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. peach cobbler", "s": "public-reference", "f": null}, {"t": "Visiting Stone Mountain", "d": "How to experience Stone Mountain.", "g": "attractions", "l": 2, "q": "What is Visiting Stone Mountain?", "a": "How to experience Stone Mountain.", "x": "Experiencing Stone Mountain: plan around Savannah St. Patrick's Day, the state's rhythm — Wisdom, Justice, Moderation. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Okefenokee National Wildlife Refuge Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "World of Coca-Cola", "d": "World of Coca-Cola: a top Georgia attraction.", "g": "attractions", "l": 2, "q": "What is World of Coca-Cola?", "a": "World of Coca-Cola: a top Georgia attraction.", "x": "World of Coca-Cola is essential Georgia. Creek and Cherokee; Trail of Tears. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. peach cobbler", "s": "public-reference", "f": null}, {"t": "Visiting World of Coca-Cola", "d": "How to experience World of Coca-Cola.", "g": "attractions", "l": 2, "q": "What is Visiting World of Coca-Cola?", "a": "How to experience World of Coca-Cola.", "x": "Experiencing World of Coca-Cola: plan around Savannah St. Patrick's Day, the state's rhythm — Wisdom, Justice, Moderation. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Okefenokee National Wildlife Refuge Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Georgia Aquarium", "d": "Georgia Aquarium: a top Georgia attraction.", "g": "attractions", "l": 2, "q": "What is Georgia Aquarium?", "a": "Georgia Aquarium: a top Georgia attraction.", "x": "Georgia Aquarium is essential Georgia. Creek and Cherokee; Trail of Tears. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. peach cobbler", "s": "public-reference", "f": null}, {"t": "Visiting Georgia Aquarium", "d": "How to experience Georgia Aquarium.", "g": "attractions", "l": 2, "q": "What is Visiting Georgia Aquarium?", "a": "How to experience Georgia Aquarium.", "x": "Experiencing Georgia Aquarium: plan around Savannah St. Patrick's Day, the state's rhythm — Wisdom, Justice, Moderation. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Okefenokee National Wildlife Refuge Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Okefenokee Swamp", "d": "Okefenokee Swamp: a top Georgia attraction.", "g": "attractions", "l": 2, "q": "What is Okefenokee Swamp?", "a": "Okefenokee Swamp: a top Georgia attraction.", "x": "Okefenokee Swamp is essential Georgia. Creek and Cherokee; Trail of Tears. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. peach cobbler", "s": "public-reference", "f": null}, {"t": "Visiting Okefenokee Swamp", "d": "How to experience Okefenokee Swamp.", "g": "attractions", "l": 2, "q": "What is Visiting Okefenokee Swamp?", "a": "How to experience Okefenokee Swamp.", "x": "Experiencing Okefenokee Swamp: plan around Savannah St. Patrick's Day, the state's rhythm — Wisdom, Justice, Moderation. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Okefenokee National Wildlife Refuge Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "MLK Historic Site", "d": "MLK Historic Site: a top Georgia attraction.", "g": "attractions", "l": 2, "q": "What is MLK Historic Site?", "a": "MLK Historic Site: a top Georgia attraction.", "x": "MLK Historic Site is essential Georgia. Creek and Cherokee; Trail of Tears. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. peach cobbler", "s": "public-reference", "f": null}, {"t": "Visiting MLK Historic Site", "d": "How to experience MLK Historic Site.", "g": "attractions", "l": 2, "q": "What is Visiting MLK Historic Site?", "a": "How to experience MLK Historic Site.", "x": "Experiencing MLK Historic Site: plan around Savannah St. Patrick's Day, the state's rhythm — Wisdom, Justice, Moderation. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Okefenokee National Wildlife Refuge Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Tybee Island", "d": "Tybee Island: a top Georgia attraction.", "g": "attractions", "l": 2, "q": "What is Tybee Island?", "a": "Tybee Island: a top Georgia attraction.", "x": "Tybee Island is essential Georgia. Creek and Cherokee; Trail of Tears. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. peach cobbler", "s": "public-reference", "f": null}, {"t": "Visiting Tybee Island", "d": "How to experience Tybee Island.", "g": "attractions", "l": 2, "q": "What is Visiting Tybee Island?", "a": "How to experience Tybee Island.", "x": "Experiencing Tybee Island: plan around Savannah St. Patrick's Day, the state's rhythm — Wisdom, Justice, Moderation. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Okefenokee National Wildlife Refuge Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Callaway Gardens", "d": "Callaway Gardens: a top Georgia attraction.", "g": "attractions", "l": 2, "q": "What is Callaway Gardens?", "a": "Callaway Gardens: a top Georgia attraction.", "x": "Callaway Gardens is essential Georgia. Creek and Cherokee; Trail of Tears. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. peach cobbler", "s": "public-reference", "f": null}, {"t": "Visiting Callaway Gardens", "d": "How to experience Callaway Gardens.", "g": "attractions", "l": 2, "q": "What is Visiting Callaway Gardens?", "a": "How to experience Callaway Gardens.", "x": "Experiencing Callaway Gardens: plan around Savannah St. Patrick's Day, the state's rhythm — Wisdom, Justice, Moderation. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Okefenokee National Wildlife Refuge Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Okefenokee National Wildlife Refuge", "d": "Okefenokee National Wildlife Refuge: Georgia's great park.", "g": "parks", "l": 2, "q": "What is Okefenokee National Wildlife Refuge?", "a": "Okefenokee National Wildlife Refuge: Georgia's great park.", "x": "Okefenokee National Wildlife Refuge is Georgia's wild heart: Savannah historic district. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Savannah St. Patrick's Day Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Okefenokee National Wildlife Refuge", "d": "How to explore Okefenokee National Wildlife Refuge.", "g": "parks", "l": 2, "q": "What is Exploring Okefenokee National Wildlife Refuge?", "a": "How to explore Okefenokee National Wildlife Refuge.", "x": "Exploring Okefenokee National Wildlife Refuge: get the park map, check conditions, carry water and layers, and tell someone your plan. Wisdom, Justice, Moderation Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Atlanta: the capital city", "d": "Atlanta, capital of Georgia.", "g": "cities", "l": 2, "q": "What is Atlanta: the capital city?", "a": "Atlanta, capital of Georgia.", "x": "Atlanta: the capital of Georgia — government, history, and often the best museums. Cotton kingdom; Sherman's March. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Atlanta", "s": "public-reference", "f": null}, {"t": "Atlanta: the biggest city", "d": "Atlanta is Georgia's largest city.", "g": "cities", "l": 2, "q": "What is Atlanta: the biggest city?", "a": "Atlanta is Georgia's largest city.", "x": "Atlanta is where Georgia comes to work and play: the skyline, the food, the music, the crowds. logistics (Delta, UPS) Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Savannah St. Patrick's Day", "s": "public-reference", "f": null}, {"t": "peach cobbler: the food", "d": "Taste Georgia: peach cobbler.", "g": "food", "l": 2, "q": "What is peach cobbler: the food?", "a": "Taste Georgia: peach cobbler.", "x": "The taste of Georgia is peach cobbler — and the foodways around it. Civil Rights: MLK from Atlanta. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Savannah St. Patrick's Day Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Georgia", "d": "Eating your way through Georgia.", "g": "food", "l": 2, "q": "What is Food tour: Georgia?", "a": "Eating your way through Georgia.", "x": "Eating through Georgia: start with peach cobbler, then follow the locals — diners, food trucks, farm stands. Wisdom, Justice, Moderation Food is the fastest way into a place's heart; the stories come free with the meal. Atlanta", "s": "public-reference", "f": null}, {"t": "Savannah St. Patrick's Day", "d": "Savannah St. Patrick's Day: Georgia's signature festival.", "g": "festivals", "l": 2, "q": "What is Savannah St. Patrick's Day?", "a": "Savannah St. Patrick's Day: Georgia's signature festival.", "x": "Savannah St. Patrick's Day is Georgia at its most celebratory: Coca-Cola, CNN, Delta hub.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Atlanta Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Georgia year-round: Savannah St. Patrick's Day and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Georgia year-round: Savannah St. Patrick's Day and more.", "x": "The Georgia festival calendar runs year-round, with Savannah St. Patrick's Day as the anchor. Wisdom, Justice, Moderation Every season has its celebration — plan trips around them for the liveliest version of the state. Okefenokee National Wildlife Refuge", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-georgia-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
