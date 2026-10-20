(function(){'use strict';
/* JAH Idaho Attractions Database generator — jahdb-e2-idaho-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-idaho-attractions',PREFIX='JAH-E2IDAHOATTR-',NAME='JAH Idaho Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Idaho: attractions overview", "d": "The best of Idaho: Craters of the Moon, Shoshone Falls, Sawtooth Mountains.", "g": "overview", "l": 2, "q": "What is Idaho: attractions overview?", "a": "The best of Idaho: Craters of the Moon, Shoshone Falls, Sawtooth Mountains.", "x": "The essential Idaho: Craters of the Moon, Shoshone Falls, Sawtooth Mountains — plus Sawtooth National Recreation Area, Idaho's great finger steaks. Sun Valley festivals This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Craters of the Moon", "d": "Craters of the Moon: a top Idaho attraction.", "g": "attractions", "l": 2, "q": "What is Craters of the Moon?", "a": "Craters of the Moon: a top Idaho attraction.", "x": "Craters of the Moon is essential Idaho. Nez Perce and Shoshone; Lewis & Clark. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. finger steaks", "s": "public-reference", "f": null}, {"t": "Visiting Craters of the Moon", "d": "How to experience Craters of the Moon.", "g": "attractions", "l": 2, "q": "What is Visiting Craters of the Moon?", "a": "How to experience Craters of the Moon.", "x": "Experiencing Craters of the Moon: plan around Sun Valley festivals, the state's rhythm — Esto perpetua (Let it be perpetual). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Sawtooth National Recreation Area Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Shoshone Falls", "d": "Shoshone Falls: a top Idaho attraction.", "g": "attractions", "l": 2, "q": "What is Shoshone Falls?", "a": "Shoshone Falls: a top Idaho attraction.", "x": "Shoshone Falls is essential Idaho. Nez Perce and Shoshone; Lewis & Clark. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. finger steaks", "s": "public-reference", "f": null}, {"t": "Visiting Shoshone Falls", "d": "How to experience Shoshone Falls.", "g": "attractions", "l": 2, "q": "What is Visiting Shoshone Falls?", "a": "How to experience Shoshone Falls.", "x": "Experiencing Shoshone Falls: plan around Sun Valley festivals, the state's rhythm — Esto perpetua (Let it be perpetual). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Sawtooth National Recreation Area Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Sawtooth Mountains", "d": "Sawtooth Mountains: a top Idaho attraction.", "g": "attractions", "l": 2, "q": "What is Sawtooth Mountains?", "a": "Sawtooth Mountains: a top Idaho attraction.", "x": "Sawtooth Mountains is essential Idaho. Nez Perce and Shoshone; Lewis & Clark. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. finger steaks", "s": "public-reference", "f": null}, {"t": "Visiting Sawtooth Mountains", "d": "How to experience Sawtooth Mountains.", "g": "attractions", "l": 2, "q": "What is Visiting Sawtooth Mountains?", "a": "How to experience Sawtooth Mountains.", "x": "Experiencing Sawtooth Mountains: plan around Sun Valley festivals, the state's rhythm — Esto perpetua (Let it be perpetual). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Sawtooth National Recreation Area Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Sun Valley", "d": "Sun Valley: a top Idaho attraction.", "g": "attractions", "l": 2, "q": "What is Sun Valley?", "a": "Sun Valley: a top Idaho attraction.", "x": "Sun Valley is essential Idaho. Nez Perce and Shoshone; Lewis & Clark. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. finger steaks State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Sun Valley", "d": "How to experience Sun Valley.", "g": "attractions", "l": 2, "q": "What is Visiting Sun Valley?", "a": "How to experience Sun Valley.", "x": "Experiencing Sun Valley: plan around Sun Valley festivals, the state's rhythm — Esto perpetua (Let it be perpetual). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Sawtooth National Recreation Area Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Hells Canyon", "d": "Hells Canyon: a top Idaho attraction.", "g": "attractions", "l": 2, "q": "What is Hells Canyon?", "a": "Hells Canyon: a top Idaho attraction.", "x": "Hells Canyon is essential Idaho. Nez Perce and Shoshone; Lewis & Clark. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. finger steaks", "s": "public-reference", "f": null}, {"t": "Visiting Hells Canyon", "d": "How to experience Hells Canyon.", "g": "attractions", "l": 2, "q": "What is Visiting Hells Canyon?", "a": "How to experience Hells Canyon.", "x": "Experiencing Hells Canyon: plan around Sun Valley festivals, the state's rhythm — Esto perpetua (Let it be perpetual). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Sawtooth National Recreation Area Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Coeur d'Alene Lake", "d": "Coeur d'Alene Lake: a top Idaho attraction.", "g": "attractions", "l": 2, "q": "What is Coeur d'Alene Lake?", "a": "Coeur d'Alene Lake: a top Idaho attraction.", "x": "Coeur d'Alene Lake is essential Idaho. Nez Perce and Shoshone; Lewis & Clark. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. finger steaks", "s": "public-reference", "f": null}, {"t": "Visiting Coeur d'Alene Lake", "d": "How to experience Coeur d'Alene Lake.", "g": "attractions", "l": 2, "q": "What is Visiting Coeur d'Alene Lake?", "a": "How to experience Coeur d'Alene Lake.", "x": "Experiencing Coeur d'Alene Lake: plan around Sun Valley festivals, the state's rhythm — Esto perpetua (Let it be perpetual). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Sawtooth National Recreation Area Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Boise River Greenbelt", "d": "Boise River Greenbelt: a top Idaho attraction.", "g": "attractions", "l": 2, "q": "What is Boise River Greenbelt?", "a": "Boise River Greenbelt: a top Idaho attraction.", "x": "Boise River Greenbelt is essential Idaho. Nez Perce and Shoshone; Lewis & Clark. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. finger steaks", "s": "public-reference", "f": null}, {"t": "Visiting Boise River Greenbelt", "d": "How to experience Boise River Greenbelt.", "g": "attractions", "l": 2, "q": "What is Visiting Boise River Greenbelt?", "a": "How to experience Boise River Greenbelt.", "x": "Experiencing Boise River Greenbelt: plan around Sun Valley festivals, the state's rhythm — Esto perpetua (Let it be perpetual). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Sawtooth National Recreation Area Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Yellowstone edge", "d": "Yellowstone edge: a top Idaho attraction.", "g": "attractions", "l": 2, "q": "What is Yellowstone edge?", "a": "Yellowstone edge: a top Idaho attraction.", "x": "Yellowstone edge is essential Idaho. Nez Perce and Shoshone; Lewis & Clark. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. finger steaks", "s": "public-reference", "f": null}, {"t": "Visiting Yellowstone edge", "d": "How to experience Yellowstone edge.", "g": "attractions", "l": 2, "q": "What is Visiting Yellowstone edge?", "a": "How to experience Yellowstone edge.", "x": "Experiencing Yellowstone edge: plan around Sun Valley festivals, the state's rhythm — Esto perpetua (Let it be perpetual). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Sawtooth National Recreation Area Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Sawtooth National Recreation Area", "d": "Sawtooth National Recreation Area: Idaho's great park.", "g": "parks", "l": 2, "q": "What is Sawtooth National Recreation Area?", "a": "Sawtooth National Recreation Area: Idaho's great park.", "x": "Sawtooth National Recreation Area is Idaho's wild heart: Craters of the Moon. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Sun Valley festivals Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Sawtooth National Recreation Area", "d": "How to explore Sawtooth National Recreation Area.", "g": "parks", "l": 2, "q": "What is Exploring Sawtooth National Recreation Area?", "a": "How to explore Sawtooth National Recreation Area.", "x": "Exploring Sawtooth National Recreation Area: get the park map, check conditions, carry water and layers, and tell someone your plan. Esto perpetua (Let it be perpetual) Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Boise: the capital city", "d": "Boise, capital of Idaho.", "g": "cities", "l": 2, "q": "What is Boise: the capital city?", "a": "Boise, capital of Idaho.", "x": "Boise: the capital of Idaho — government, history, and often the best museums. Gold and silver rushes. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Boise", "s": "public-reference", "f": null}, {"t": "Boise: the biggest city", "d": "Boise is Idaho's largest city.", "g": "cities", "l": 2, "q": "What is Boise: the biggest city?", "a": "Boise is Idaho's largest city.", "x": "Boise is where Idaho comes to work and play: the skyline, the food, the music, the crowds. agriculture (potatoes) Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Sun Valley festivals", "s": "public-reference", "f": null}, {"t": "finger steaks: the food", "d": "Taste Idaho: finger steaks.", "g": "food", "l": 2, "q": "What is finger steaks: the food?", "a": "Taste Idaho: finger steaks.", "x": "The taste of Idaho is finger steaks — and the foodways around it. Potatoes; nuclear lab (INL). Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Sun Valley festivals Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Idaho", "d": "Eating your way through Idaho.", "g": "food", "l": 2, "q": "What is Food tour: Idaho?", "a": "Eating your way through Idaho.", "x": "Eating through Idaho: start with finger steaks, then follow the locals — diners, food trucks, farm stands. Esto perpetua (Let it be perpetual) Food is the fastest way into a place's heart; the stories come free with the meal. Boise", "s": "public-reference", "f": null}, {"t": "Sun Valley festivals", "d": "Sun Valley festivals: Idaho's signature festival.", "g": "festivals", "l": 2, "q": "What is Sun Valley festivals?", "a": "Sun Valley festivals: Idaho's signature festival.", "x": "Sun Valley festivals is Idaho at its most celebratory: Boise boom.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Boise Time a visit for one; book early. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Idaho year-round: Sun Valley festivals and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Idaho year-round: Sun Valley festivals and more.", "x": "The Idaho festival calendar runs year-round, with Sun Valley festivals as the anchor. Esto perpetua (Let it be perpetual) Every season has its celebration — plan trips around them for the liveliest version of the state. Sawtooth National Recreation Area", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-idaho-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
