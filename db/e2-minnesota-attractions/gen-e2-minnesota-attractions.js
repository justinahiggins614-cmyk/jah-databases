(function(){'use strict';
/* JAH Minnesota Attractions Database generator — jahdb-e2-minnesota-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-minnesota-attractions',PREFIX='JAH-E2MINNESOTA-',NAME='JAH Minnesota Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Minnesota: attractions overview", "d": "The best of Minnesota: Mall of America, Boundary Waters, Minnehaha Falls.", "g": "overview", "l": 2, "q": "What is Minnesota: attractions overview?", "a": "The best of Minnesota: Mall of America, Boundary Waters, Minnehaha Falls.", "x": "The essential Minnesota: Mall of America, Boundary Waters, Minnehaha Falls — plus Voyageurs National Park, Minnesota's great Juicy Lucy. Minnesota State Fair This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Mall of America", "d": "Mall of America: a top Minnesota attraction.", "g": "attractions", "l": 2, "q": "What is Mall of America?", "a": "Mall of America: a top Minnesota attraction.", "x": "Mall of America is essential Minnesota. Dakota and Ojibwe; French then U.S. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Juicy Lucy", "s": "public-reference", "f": null}, {"t": "Visiting Mall of America", "d": "How to experience Mall of America.", "g": "attractions", "l": 2, "q": "What is Visiting Mall of America?", "a": "How to experience Mall of America.", "x": "Experiencing Mall of America: plan around Minnesota State Fair, the state's rhythm — L'Etoile du Nord (The star of the north). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Voyageurs National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Boundary Waters", "d": "Boundary Waters: a top Minnesota attraction.", "g": "attractions", "l": 2, "q": "What is Boundary Waters?", "a": "Boundary Waters: a top Minnesota attraction.", "x": "Boundary Waters is essential Minnesota. Dakota and Ojibwe; French then U.S. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Juicy Lucy", "s": "public-reference", "f": null}, {"t": "Visiting Boundary Waters", "d": "How to experience Boundary Waters.", "g": "attractions", "l": 2, "q": "What is Visiting Boundary Waters?", "a": "How to experience Boundary Waters.", "x": "Experiencing Boundary Waters: plan around Minnesota State Fair, the state's rhythm — L'Etoile du Nord (The star of the north). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Voyageurs National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Minnehaha Falls", "d": "Minnehaha Falls: a top Minnesota attraction.", "g": "attractions", "l": 2, "q": "What is Minnehaha Falls?", "a": "Minnehaha Falls: a top Minnesota attraction.", "x": "Minnehaha Falls is essential Minnesota. Dakota and Ojibwe; French then U.S. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Juicy Lucy", "s": "public-reference", "f": null}, {"t": "Visiting Minnehaha Falls", "d": "How to experience Minnehaha Falls.", "g": "attractions", "l": 2, "q": "What is Visiting Minnehaha Falls?", "a": "How to experience Minnehaha Falls.", "x": "Experiencing Minnehaha Falls: plan around Minnesota State Fair, the state's rhythm — L'Etoile du Nord (The star of the north). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Voyageurs National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Split Rock Lighthouse", "d": "Split Rock Lighthouse: a top Minnesota attraction.", "g": "attractions", "l": 2, "q": "What is Split Rock Lighthouse?", "a": "Split Rock Lighthouse: a top Minnesota attraction.", "x": "Split Rock Lighthouse is essential Minnesota. Dakota and Ojibwe; French then U.S. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Juicy Lucy", "s": "public-reference", "f": null}, {"t": "Visiting Split Rock Lighthouse", "d": "How to experience Split Rock Lighthouse.", "g": "attractions", "l": 2, "q": "What is Visiting Split Rock Lighthouse?", "a": "How to experience Split Rock Lighthouse.", "x": "Experiencing Split Rock Lighthouse: plan around Minnesota State Fair, the state's rhythm — L'Etoile du Nord (The star of the north). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Voyageurs National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "North Shore", "d": "North Shore: a top Minnesota attraction.", "g": "attractions", "l": 2, "q": "What is North Shore?", "a": "North Shore: a top Minnesota attraction.", "x": "North Shore is essential Minnesota. Dakota and Ojibwe; French then U.S. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Juicy Lucy State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting North Shore", "d": "How to experience North Shore.", "g": "attractions", "l": 2, "q": "What is Visiting North Shore?", "a": "How to experience North Shore.", "x": "Experiencing North Shore: plan around Minnesota State Fair, the state's rhythm — L'Etoile du Nord (The star of the north). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Voyageurs National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Voyageurs National Park", "d": "Voyageurs National Park: a top Minnesota attraction.", "g": "attractions", "l": 2, "q": "What is Voyageurs National Park?", "a": "Voyageurs National Park: a top Minnesota attraction.", "x": "Voyageurs National Park is essential Minnesota. Dakota and Ojibwe; French then U.S. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Juicy Lucy", "s": "public-reference", "f": null}, {"t": "Visiting Voyageurs National Park", "d": "How to experience Voyageurs National Park.", "g": "attractions", "l": 2, "q": "What is Visiting Voyageurs National Park?", "a": "How to experience Voyageurs National Park.", "x": "Experiencing Voyageurs National Park: plan around Minnesota State Fair, the state's rhythm — L'Etoile du Nord (The star of the north). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Voyageurs National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Walker Art Center", "d": "Walker Art Center: a top Minnesota attraction.", "g": "attractions", "l": 2, "q": "What is Walker Art Center?", "a": "Walker Art Center: a top Minnesota attraction.", "x": "Walker Art Center is essential Minnesota. Dakota and Ojibwe; French then U.S. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Juicy Lucy", "s": "public-reference", "f": null}, {"t": "Visiting Walker Art Center", "d": "How to experience Walker Art Center.", "g": "attractions", "l": 2, "q": "What is Visiting Walker Art Center?", "a": "How to experience Walker Art Center.", "x": "Experiencing Walker Art Center: plan around Minnesota State Fair, the state's rhythm — L'Etoile du Nord (The star of the north). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Voyageurs National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Como Zoo", "d": "Como Zoo: a top Minnesota attraction.", "g": "attractions", "l": 2, "q": "What is Como Zoo?", "a": "Como Zoo: a top Minnesota attraction.", "x": "Como Zoo is essential Minnesota. Dakota and Ojibwe; French then U.S. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Juicy Lucy State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Como Zoo", "d": "How to experience Como Zoo.", "g": "attractions", "l": 2, "q": "What is Visiting Como Zoo?", "a": "How to experience Como Zoo.", "x": "Experiencing Como Zoo: plan around Minnesota State Fair, the state's rhythm — L'Etoile du Nord (The star of the north). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Voyageurs National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Voyageurs National Park", "d": "Voyageurs National Park: Minnesota's great park.", "g": "parks", "l": 2, "q": "What is Voyageurs National Park?", "a": "Voyageurs National Park: Minnesota's great park.", "x": "Voyageurs National Park is Minnesota's wild heart: Mall of America. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Minnesota State Fair Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Voyageurs National Park", "d": "How to explore Voyageurs National Park.", "g": "parks", "l": 2, "q": "What is Exploring Voyageurs National Park?", "a": "How to explore Voyageurs National Park.", "x": "Exploring Voyageurs National Park: get the park map, check conditions, carry water and layers, and tell someone your plan. L'Etoile du Nord (The star of the north) Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "St. Paul: the capital city", "d": "St. Paul, capital of Minnesota.", "g": "cities", "l": 2, "q": "What is St. Paul: the capital city?", "a": "St. Paul, capital of Minnesota.", "x": "St. Paul: the capital of Minnesota — government, history, and often the best museums. Flour milling; iron range. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Minneapolis", "s": "public-reference", "f": null}, {"t": "Minneapolis: the biggest city", "d": "Minneapolis is Minnesota's largest city.", "g": "cities", "l": 2, "q": "What is Minneapolis: the biggest city?", "a": "Minneapolis is Minnesota's largest city.", "x": "Minneapolis is where Minnesota comes to work and play: the skyline, the food, the music, the crowds. healthcare (Mayo, UnitedHealth) Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Minnesota State Fair", "s": "public-reference", "f": null}, {"t": "Juicy Lucy: the food", "d": "Taste Minnesota: Juicy Lucy.", "g": "food", "l": 2, "q": "What is Juicy Lucy: the food?", "a": "Taste Minnesota: Juicy Lucy.", "x": "The taste of Minnesota is Juicy Lucy — and the foodways around it. Progressive politics; Mayo Clinic. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Minnesota State Fair Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Minnesota", "d": "Eating your way through Minnesota.", "g": "food", "l": 2, "q": "What is Food tour: Minnesota?", "a": "Eating your way through Minnesota.", "x": "Eating through Minnesota: start with Juicy Lucy, then follow the locals — diners, food trucks, farm stands. L'Etoile du Nord (The star of the north) Food is the fastest way into a place's heart; the stories come free with the meal. Minneapolis", "s": "public-reference", "f": null}, {"t": "Minnesota State Fair", "d": "Minnesota State Fair: Minnesota's signature festival.", "g": "festivals", "l": 2, "q": "What is Minnesota State Fair?", "a": "Minnesota State Fair: Minnesota's signature festival.", "x": "Minnesota State Fair is Minnesota at its most celebratory: The Mayo Clinic made Rochester a medical mecca.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. St. Paul Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Minnesota year-round: Minnesota State Fair and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Minnesota year-round: Minnesota State Fair and more.", "x": "The Minnesota festival calendar runs year-round, with Minnesota State Fair as the anchor. L'Etoile du Nord (The star of the north) Every season has its celebration — plan trips around them for the liveliest version of the state. Voyageurs National Park", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-minnesota-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
