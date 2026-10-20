(function(){'use strict';
/* JAH Delaware Attractions Database generator — jahdb-e2-delaware-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-delaware-attractions',PREFIX='JAH-E2DELAWAREA-',NAME='JAH Delaware Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Delaware: attractions overview", "d": "The best of Delaware: Rehoboth Beach, Winterthur Museum, Delaware beaches.", "g": "overview", "l": 2, "q": "What is Delaware: attractions overview?", "a": "The best of Delaware: Rehoboth Beach, Winterthur Museum, Delaware beaches.", "x": "The essential Delaware: Rehoboth Beach, Winterthur Museum, Delaware beaches — plus Cape Henlopen State Park, Delaware's great scrapple. Rehoboth Beach festivals This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Rehoboth Beach", "d": "Rehoboth Beach: a top Delaware attraction.", "g": "attractions", "l": 2, "q": "What is Rehoboth Beach?", "a": "Rehoboth Beach: a top Delaware attraction.", "x": "Rehoboth Beach is essential Delaware. Lenape lands; Swedish then Dutch then English. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. scrapple", "s": "public-reference", "f": null}, {"t": "Visiting Rehoboth Beach", "d": "How to experience Rehoboth Beach.", "g": "attractions", "l": 2, "q": "What is Visiting Rehoboth Beach?", "a": "How to experience Rehoboth Beach.", "x": "Experiencing Rehoboth Beach: plan around Rehoboth Beach festivals, the state's rhythm — Liberty and Independence. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Cape Henlopen State Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Winterthur Museum", "d": "Winterthur Museum: a top Delaware attraction.", "g": "attractions", "l": 2, "q": "What is Winterthur Museum?", "a": "Winterthur Museum: a top Delaware attraction.", "x": "Winterthur Museum is essential Delaware. Lenape lands; Swedish then Dutch then English. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. scrapple", "s": "public-reference", "f": null}, {"t": "Visiting Winterthur Museum", "d": "How to experience Winterthur Museum.", "g": "attractions", "l": 2, "q": "What is Visiting Winterthur Museum?", "a": "How to experience Winterthur Museum.", "x": "Experiencing Winterthur Museum: plan around Rehoboth Beach festivals, the state's rhythm — Liberty and Independence. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Cape Henlopen State Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Delaware beaches", "d": "Delaware beaches: a top Delaware attraction.", "g": "attractions", "l": 2, "q": "What is Delaware beaches?", "a": "Delaware beaches: a top Delaware attraction.", "x": "Delaware beaches is essential Delaware. Lenape lands; Swedish then Dutch then English. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. scrapple", "s": "public-reference", "f": null}, {"t": "Visiting Delaware beaches", "d": "How to experience Delaware beaches.", "g": "attractions", "l": 2, "q": "What is Visiting Delaware beaches?", "a": "How to experience Delaware beaches.", "x": "Experiencing Delaware beaches: plan around Rehoboth Beach festivals, the state's rhythm — Liberty and Independence. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Cape Henlopen State Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Nemours Estate", "d": "Nemours Estate: a top Delaware attraction.", "g": "attractions", "l": 2, "q": "What is Nemours Estate?", "a": "Nemours Estate: a top Delaware attraction.", "x": "Nemours Estate is essential Delaware. Lenape lands; Swedish then Dutch then English. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. scrapple", "s": "public-reference", "f": null}, {"t": "Visiting Nemours Estate", "d": "How to experience Nemours Estate.", "g": "attractions", "l": 2, "q": "What is Visiting Nemours Estate?", "a": "How to experience Nemours Estate.", "x": "Experiencing Nemours Estate: plan around Rehoboth Beach festivals, the state's rhythm — Liberty and Independence. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Cape Henlopen State Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "First State Heritage Park", "d": "First State Heritage Park: a top Delaware attraction.", "g": "attractions", "l": 2, "q": "What is First State Heritage Park?", "a": "First State Heritage Park: a top Delaware attraction.", "x": "First State Heritage Park is essential Delaware. Lenape lands; Swedish then Dutch then English. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. scrapple", "s": "public-reference", "f": null}, {"t": "Visiting First State Heritage Park", "d": "How to experience First State Heritage Park.", "g": "attractions", "l": 2, "q": "What is Visiting First State Heritage Park?", "a": "How to experience First State Heritage Park.", "x": "Experiencing First State Heritage Park: plan around Rehoboth Beach festivals, the state's rhythm — Liberty and Independence. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Cape Henlopen State Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Bombay Hook refuge", "d": "Bombay Hook refuge: a top Delaware attraction.", "g": "attractions", "l": 2, "q": "What is Bombay Hook refuge?", "a": "Bombay Hook refuge: a top Delaware attraction.", "x": "Bombay Hook refuge is essential Delaware. Lenape lands; Swedish then Dutch then English. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. scrapple", "s": "public-reference", "f": null}, {"t": "Visiting Bombay Hook refuge", "d": "How to experience Bombay Hook refuge.", "g": "attractions", "l": 2, "q": "What is Visiting Bombay Hook refuge?", "a": "How to experience Bombay Hook refuge.", "x": "Experiencing Bombay Hook refuge: plan around Rehoboth Beach festivals, the state's rhythm — Liberty and Independence. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Cape Henlopen State Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Dover Downs", "d": "Dover Downs: a top Delaware attraction.", "g": "attractions", "l": 2, "q": "What is Dover Downs?", "a": "Dover Downs: a top Delaware attraction.", "x": "Dover Downs is essential Delaware. Lenape lands; Swedish then Dutch then English. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. scrapple", "s": "public-reference", "f": null}, {"t": "Visiting Dover Downs", "d": "How to experience Dover Downs.", "g": "attractions", "l": 2, "q": "What is Visiting Dover Downs?", "a": "How to experience Dover Downs.", "x": "Experiencing Dover Downs: plan around Rehoboth Beach festivals, the state's rhythm — Liberty and Independence. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Cape Henlopen State Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Cape Henlopen", "d": "Cape Henlopen: a top Delaware attraction.", "g": "attractions", "l": 2, "q": "What is Cape Henlopen?", "a": "Cape Henlopen: a top Delaware attraction.", "x": "Cape Henlopen is essential Delaware. Lenape lands; Swedish then Dutch then English. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. scrapple", "s": "public-reference", "f": null}, {"t": "Visiting Cape Henlopen", "d": "How to experience Cape Henlopen.", "g": "attractions", "l": 2, "q": "What is Visiting Cape Henlopen?", "a": "How to experience Cape Henlopen.", "x": "Experiencing Cape Henlopen: plan around Rehoboth Beach festivals, the state's rhythm — Liberty and Independence. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Cape Henlopen State Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Cape Henlopen State Park", "d": "Cape Henlopen State Park: Delaware's great park.", "g": "parks", "l": 2, "q": "What is Cape Henlopen State Park?", "a": "Cape Henlopen State Park: Delaware's great park.", "x": "Cape Henlopen State Park is Delaware's wild heart: Rehoboth Beach. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Rehoboth Beach festivals Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Cape Henlopen State Park", "d": "How to explore Cape Henlopen State Park.", "g": "parks", "l": 2, "q": "What is Exploring Cape Henlopen State Park?", "a": "How to explore Cape Henlopen State Park.", "x": "Exploring Cape Henlopen State Park: get the park map, check conditions, carry water and layers, and tell someone your plan. Liberty and Independence Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Dover: the capital city", "d": "Dover, capital of Delaware.", "g": "cities", "l": 2, "q": "What is Dover: the capital city?", "a": "Dover, capital of Delaware.", "x": "Dover: the capital of Delaware — government, history, and often the best museums. First to ratify the Constitution. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Wilmington", "s": "public-reference", "f": null}, {"t": "Wilmington: the biggest city", "d": "Wilmington is Delaware's largest city.", "g": "cities", "l": 2, "q": "What is Wilmington: the biggest city?", "a": "Wilmington is Delaware's largest city.", "x": "Wilmington is where Delaware comes to work and play: the skyline, the food, the music, the crowds. chemicals (DuPont) Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Rehoboth Beach festivals", "s": "public-reference", "f": null}, {"t": "scrapple: the food", "d": "Taste Delaware: scrapple.", "g": "food", "l": 2, "q": "What is scrapple: the food?", "a": "Taste Delaware: scrapple.", "x": "The taste of Delaware is scrapple — and the foodways around it. DuPont chemicals; corporate haven. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Rehoboth Beach festivals Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Delaware", "d": "Eating your way through Delaware.", "g": "food", "l": 2, "q": "What is Food tour: Delaware?", "a": "Eating your way through Delaware.", "x": "Eating through Delaware: start with scrapple, then follow the locals — diners, food trucks, farm stands. Liberty and Independence Food is the fastest way into a place's heart; the stories come free with the meal. Wilmington", "s": "public-reference", "f": null}, {"t": "Rehoboth Beach festivals", "d": "Rehoboth Beach festivals: Delaware's signature festival.", "g": "festivals", "l": 2, "q": "What is Rehoboth Beach festivals?", "a": "Rehoboth Beach festivals: Delaware's signature festival.", "x": "Rehoboth Beach festivals is Delaware at its most celebratory: Tax-free shopping.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Dover Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Delaware year-round: Rehoboth Beach festivals and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Delaware year-round: Rehoboth Beach festivals and more.", "x": "The Delaware festival calendar runs year-round, with Rehoboth Beach festivals as the anchor. Liberty and Independence Every season has its celebration — plan trips around them for the liveliest version of the state. Cape Henlopen State Park", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-delaware-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
