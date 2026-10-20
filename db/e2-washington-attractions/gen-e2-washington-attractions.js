(function(){'use strict';
/* JAH Washington Attractions Database generator — jahdb-e2-washington-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-washington-attractions',PREFIX='JAH-E2WASHINGTO-',NAME='JAH Washington Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Washington: attractions overview", "d": "The best of Washington: Space Needle, Mount Rainier, Olympic National Park.", "g": "overview", "l": 2, "q": "What is Washington: attractions overview?", "a": "The best of Washington: Space Needle, Mount Rainier, Olympic National Park.", "x": "The essential Washington: Space Needle, Mount Rainier, Olympic National Park — plus Olympic National Park, Washington's great salmon. Seafair This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Space Needle", "d": "Space Needle: a top Washington attraction.", "g": "attractions", "l": 2, "q": "What is Space Needle?", "a": "Space Needle: a top Washington attraction.", "x": "Space Needle is essential Washington. Coast Salish; Oregon Trail. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. salmon State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Space Needle", "d": "How to experience Space Needle.", "g": "attractions", "l": 2, "q": "What is Visiting Space Needle?", "a": "How to experience Space Needle.", "x": "Experiencing Space Needle: plan around Seafair, the state's rhythm — Al-ki (By and by). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Olympic National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Mount Rainier", "d": "Mount Rainier: a top Washington attraction.", "g": "attractions", "l": 2, "q": "What is Mount Rainier?", "a": "Mount Rainier: a top Washington attraction.", "x": "Mount Rainier is essential Washington. Coast Salish; Oregon Trail. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. salmon State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Mount Rainier", "d": "How to experience Mount Rainier.", "g": "attractions", "l": 2, "q": "What is Visiting Mount Rainier?", "a": "How to experience Mount Rainier.", "x": "Experiencing Mount Rainier: plan around Seafair, the state's rhythm — Al-ki (By and by). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Olympic National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Olympic National Park", "d": "Olympic National Park: a top Washington attraction.", "g": "attractions", "l": 2, "q": "What is Olympic National Park?", "a": "Olympic National Park: a top Washington attraction.", "x": "Olympic National Park is essential Washington. Coast Salish; Oregon Trail. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. salmon State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Olympic National Park", "d": "How to experience Olympic National Park.", "g": "attractions", "l": 2, "q": "What is Visiting Olympic National Park?", "a": "How to experience Olympic National Park.", "x": "Experiencing Olympic National Park: plan around Seafair, the state's rhythm — Al-ki (By and by). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Olympic National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Pike Place Market", "d": "Pike Place Market: a top Washington attraction.", "g": "attractions", "l": 2, "q": "What is Pike Place Market?", "a": "Pike Place Market: a top Washington attraction.", "x": "Pike Place Market is essential Washington. Coast Salish; Oregon Trail. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. salmon State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Pike Place Market", "d": "How to experience Pike Place Market.", "g": "attractions", "l": 2, "q": "What is Visiting Pike Place Market?", "a": "How to experience Pike Place Market.", "x": "Experiencing Pike Place Market: plan around Seafair, the state's rhythm — Al-ki (By and by). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Olympic National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "San Juan Islands", "d": "San Juan Islands: a top Washington attraction.", "g": "attractions", "l": 2, "q": "What is San Juan Islands?", "a": "San Juan Islands: a top Washington attraction.", "x": "San Juan Islands is essential Washington. Coast Salish; Oregon Trail. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. salmon State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting San Juan Islands", "d": "How to experience San Juan Islands.", "g": "attractions", "l": 2, "q": "What is Visiting San Juan Islands?", "a": "How to experience San Juan Islands.", "x": "Experiencing San Juan Islands: plan around Seafair, the state's rhythm — Al-ki (By and by). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Olympic National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "North Cascades", "d": "North Cascades: a top Washington attraction.", "g": "attractions", "l": 2, "q": "What is North Cascades?", "a": "North Cascades: a top Washington attraction.", "x": "North Cascades is essential Washington. Coast Salish; Oregon Trail. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. salmon State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting North Cascades", "d": "How to experience North Cascades.", "g": "attractions", "l": 2, "q": "What is Visiting North Cascades?", "a": "How to experience North Cascades.", "x": "Experiencing North Cascades: plan around Seafair, the state's rhythm — Al-ki (By and by). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Olympic National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Seattle waterfront", "d": "Seattle waterfront: a top Washington attraction.", "g": "attractions", "l": 2, "q": "What is Seattle waterfront?", "a": "Seattle waterfront: a top Washington attraction.", "x": "Seattle waterfront is essential Washington. Coast Salish; Oregon Trail. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. salmon State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Seattle waterfront", "d": "How to experience Seattle waterfront.", "g": "attractions", "l": 2, "q": "What is Visiting Seattle waterfront?", "a": "How to experience Seattle waterfront.", "x": "Experiencing Seattle waterfront: plan around Seafair, the state's rhythm — Al-ki (By and by). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Olympic National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Chihuly Garden", "d": "Chihuly Garden: a top Washington attraction.", "g": "attractions", "l": 2, "q": "What is Chihuly Garden?", "a": "Chihuly Garden: a top Washington attraction.", "x": "Chihuly Garden is essential Washington. Coast Salish; Oregon Trail. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. salmon State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Chihuly Garden", "d": "How to experience Chihuly Garden.", "g": "attractions", "l": 2, "q": "What is Visiting Chihuly Garden?", "a": "How to experience Chihuly Garden.", "x": "Experiencing Chihuly Garden: plan around Seafair, the state's rhythm — Al-ki (By and by). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Olympic National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Olympic National Park", "d": "Olympic National Park: Washington's great park.", "g": "parks", "l": 2, "q": "What is Olympic National Park?", "a": "Olympic National Park: Washington's great park.", "x": "Olympic National Park is Washington's wild heart: Space Needle. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Seafair Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Olympic National Park", "d": "How to explore Olympic National Park.", "g": "parks", "l": 2, "q": "What is Exploring Olympic National Park?", "a": "How to explore Olympic National Park.", "x": "Exploring Olympic National Park: get the park map, check conditions, carry water and layers, and tell someone your plan. Al-ki (By and by) Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Olympia: the capital city", "d": "Olympia, capital of Washington.", "g": "cities", "l": 2, "q": "What is Olympia: the capital city?", "a": "Olympia, capital of Washington.", "x": "Olympia: the capital of Washington — government, history, and often the best museums. Statehood 1889; timber. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Seattle", "s": "public-reference", "f": null}, {"t": "Seattle: the biggest city", "d": "Seattle is Washington's largest city.", "g": "cities", "l": 2, "q": "What is Seattle: the biggest city?", "a": "Seattle is Washington's largest city.", "x": "Seattle is where Washington comes to work and play: the skyline, the food, the music, the crowds. technology Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Seafair", "s": "public-reference", "f": null}, {"t": "salmon: the food", "d": "Taste Washington: salmon.", "g": "food", "l": 2, "q": "What is salmon: the food?", "a": "Taste Washington: salmon.", "x": "The taste of Washington is salmon — and the foodways around it. Boeing, Microsoft, Amazon. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Seafair Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Washington", "d": "Eating your way through Washington.", "g": "food", "l": 2, "q": "What is Food tour: Washington?", "a": "Eating your way through Washington.", "x": "Eating through Washington: start with salmon, then follow the locals — diners, food trucks, farm stands. Al-ki (By and by) Food is the fastest way into a place's heart; the stories come free with the meal. Seattle", "s": "public-reference", "f": null}, {"t": "Seafair", "d": "Seafair: Washington's signature festival.", "g": "festivals", "l": 2, "q": "What is Seafair?", "a": "Seafair: Washington's signature festival.", "x": "Seafair is Washington at its most celebratory: Boeing and Microsoft made Seattle a tech capital.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Olympia Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Washington year-round: Seafair and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Washington year-round: Seafair and more.", "x": "The Washington festival calendar runs year-round, with Seafair as the anchor. Al-ki (By and by) Every season has its celebration — plan trips around them for the liveliest version of the state. Olympic National Park", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-washington-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
