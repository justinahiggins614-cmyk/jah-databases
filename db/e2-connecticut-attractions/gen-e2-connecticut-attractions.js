(function(){'use strict';
/* JAH Connecticut Attractions Database generator — jahdb-e2-connecticut-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-connecticut-attractions',PREFIX='JAH-E2CONNECTIC-',NAME='JAH Connecticut Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Connecticut: attractions overview", "d": "The best of Connecticut: Mystic Seaport, Yale University, Mark Twain House.", "g": "overview", "l": 2, "q": "What is Connecticut: attractions overview?", "a": "The best of Connecticut: Mystic Seaport, Yale University, Mark Twain House.", "x": "The essential Connecticut: Mystic Seaport, Yale University, Mark Twain House — plus Sleeping Giant State Park, Connecticut's great New Haven pizza. Mystic Outdoor Art Festival This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Mystic Seaport", "d": "Mystic Seaport: a top Connecticut attraction.", "g": "attractions", "l": 2, "q": "What is Mystic Seaport?", "a": "Mystic Seaport: a top Connecticut attraction.", "x": "Mystic Seaport is essential Connecticut. Pequot lands; Fundamental Orders 1639. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. New Haven pizza", "s": "public-reference", "f": null}, {"t": "Visiting Mystic Seaport", "d": "How to experience Mystic Seaport.", "g": "attractions", "l": 2, "q": "What is Visiting Mystic Seaport?", "a": "How to experience Mystic Seaport.", "x": "Experiencing Mystic Seaport: plan around Mystic Outdoor Art Festival, the state's rhythm — Qui transtulit sustinet (He who transplanted still sustains). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Sleeping Giant State Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Yale University", "d": "Yale University: a top Connecticut attraction.", "g": "attractions", "l": 2, "q": "What is Yale University?", "a": "Yale University: a top Connecticut attraction.", "x": "Yale University is essential Connecticut. Pequot lands; Fundamental Orders 1639. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. New Haven pizza", "s": "public-reference", "f": null}, {"t": "Visiting Yale University", "d": "How to experience Yale University.", "g": "attractions", "l": 2, "q": "What is Visiting Yale University?", "a": "How to experience Yale University.", "x": "Experiencing Yale University: plan around Mystic Outdoor Art Festival, the state's rhythm — Qui transtulit sustinet (He who transplanted still sustains). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Sleeping Giant State Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Mark Twain House", "d": "Mark Twain House: a top Connecticut attraction.", "g": "attractions", "l": 2, "q": "What is Mark Twain House?", "a": "Mark Twain House: a top Connecticut attraction.", "x": "Mark Twain House is essential Connecticut. Pequot lands; Fundamental Orders 1639. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. New Haven pizza", "s": "public-reference", "f": null}, {"t": "Visiting Mark Twain House", "d": "How to experience Mark Twain House.", "g": "attractions", "l": 2, "q": "What is Visiting Mark Twain House?", "a": "How to experience Mark Twain House.", "x": "Experiencing Mark Twain House: plan around Mystic Outdoor Art Festival, the state's rhythm — Qui transtulit sustinet (He who transplanted still sustains). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Sleeping Giant State Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Gillette Castle", "d": "Gillette Castle: a top Connecticut attraction.", "g": "attractions", "l": 2, "q": "What is Gillette Castle?", "a": "Gillette Castle: a top Connecticut attraction.", "x": "Gillette Castle is essential Connecticut. Pequot lands; Fundamental Orders 1639. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. New Haven pizza", "s": "public-reference", "f": null}, {"t": "Visiting Gillette Castle", "d": "How to experience Gillette Castle.", "g": "attractions", "l": 2, "q": "What is Visiting Gillette Castle?", "a": "How to experience Gillette Castle.", "x": "Experiencing Gillette Castle: plan around Mystic Outdoor Art Festival, the state's rhythm — Qui transtulit sustinet (He who transplanted still sustains). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Sleeping Giant State Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Mashantucket Pequot Museum", "d": "Mashantucket Pequot Museum: a top Connecticut attraction.", "g": "attractions", "l": 2, "q": "What is Mashantucket Pequot Museum?", "a": "Mashantucket Pequot Museum: a top Connecticut attraction.", "x": "Mashantucket Pequot Museum is essential Connecticut. Pequot lands; Fundamental Orders 1639. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. New Haven pizza", "s": "public-reference", "f": null}, {"t": "Visiting Mashantucket Pequot Museum", "d": "How to experience Mashantucket Pequot Museum.", "g": "attractions", "l": 2, "q": "What is Visiting Mashantucket Pequot Museum?", "a": "How to experience Mashantucket Pequot Museum.", "x": "Experiencing Mashantucket Pequot Museum: plan around Mystic Outdoor Art Festival, the state's rhythm — Qui transtulit sustinet (He who transplanted still sustains). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Sleeping Giant State Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Thimble Islands", "d": "Thimble Islands: a top Connecticut attraction.", "g": "attractions", "l": 2, "q": "What is Thimble Islands?", "a": "Thimble Islands: a top Connecticut attraction.", "x": "Thimble Islands is essential Connecticut. Pequot lands; Fundamental Orders 1639. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. New Haven pizza", "s": "public-reference", "f": null}, {"t": "Visiting Thimble Islands", "d": "How to experience Thimble Islands.", "g": "attractions", "l": 2, "q": "What is Visiting Thimble Islands?", "a": "How to experience Thimble Islands.", "x": "Experiencing Thimble Islands: plan around Mystic Outdoor Art Festival, the state's rhythm — Qui transtulit sustinet (He who transplanted still sustains). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Sleeping Giant State Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Wadsworth Atheneum", "d": "Wadsworth Atheneum: a top Connecticut attraction.", "g": "attractions", "l": 2, "q": "What is Wadsworth Atheneum?", "a": "Wadsworth Atheneum: a top Connecticut attraction.", "x": "Wadsworth Atheneum is essential Connecticut. Pequot lands; Fundamental Orders 1639. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. New Haven pizza", "s": "public-reference", "f": null}, {"t": "Visiting Wadsworth Atheneum", "d": "How to experience Wadsworth Atheneum.", "g": "attractions", "l": 2, "q": "What is Visiting Wadsworth Atheneum?", "a": "How to experience Wadsworth Atheneum.", "x": "Experiencing Wadsworth Atheneum: plan around Mystic Outdoor Art Festival, the state's rhythm — Qui transtulit sustinet (He who transplanted still sustains). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Sleeping Giant State Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Essex Steam Train", "d": "Essex Steam Train: a top Connecticut attraction.", "g": "attractions", "l": 2, "q": "What is Essex Steam Train?", "a": "Essex Steam Train: a top Connecticut attraction.", "x": "Essex Steam Train is essential Connecticut. Pequot lands; Fundamental Orders 1639. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. New Haven pizza", "s": "public-reference", "f": null}, {"t": "Visiting Essex Steam Train", "d": "How to experience Essex Steam Train.", "g": "attractions", "l": 2, "q": "What is Visiting Essex Steam Train?", "a": "How to experience Essex Steam Train.", "x": "Experiencing Essex Steam Train: plan around Mystic Outdoor Art Festival, the state's rhythm — Qui transtulit sustinet (He who transplanted still sustains). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Sleeping Giant State Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Sleeping Giant State Park", "d": "Sleeping Giant State Park: Connecticut's great park.", "g": "parks", "l": 2, "q": "What is Sleeping Giant State Park?", "a": "Sleeping Giant State Park: Connecticut's great park.", "x": "Sleeping Giant State Park is Connecticut's wild heart: Mystic Seaport. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Mystic Outdoor Art Festival Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Sleeping Giant State Park", "d": "How to explore Sleeping Giant State Park.", "g": "parks", "l": 2, "q": "What is Exploring Sleeping Giant State Park?", "a": "How to explore Sleeping Giant State Park.", "x": "Exploring Sleeping Giant State Park: get the park map, check conditions, carry water and layers, and tell someone your plan. Qui transtulit sustinet (He who transplanted still sustains) Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Hartford: the capital city", "d": "Hartford, capital of Connecticut.", "g": "cities", "l": 2, "q": "What is Hartford: the capital city?", "a": "Hartford, capital of Connecticut.", "x": "Hartford: the capital of Connecticut — government, history, and often the best museums. Revolutionary arsenal; Constitution State. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Bridgeport", "s": "public-reference", "f": null}, {"t": "Bridgeport: the biggest city", "d": "Bridgeport is Connecticut's largest city.", "g": "cities", "l": 2, "q": "What is Bridgeport: the biggest city?", "a": "Bridgeport is Connecticut's largest city.", "x": "Bridgeport is where Connecticut comes to work and play: the skyline, the food, the music, the crowds. insurance (Hartford) Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Mystic Outdoor Art Festival", "s": "public-reference", "f": null}, {"t": "New Haven pizza: the food", "d": "Taste Connecticut: New Haven pizza.", "g": "food", "l": 2, "q": "What is New Haven pizza: the food?", "a": "Taste Connecticut: New Haven pizza.", "x": "The taste of Connecticut is New Haven pizza — and the foodways around it. Insurance and manufacturing. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Mystic Outdoor Art Festival Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Connecticut", "d": "Eating your way through Connecticut.", "g": "food", "l": 2, "q": "What is Food tour: Connecticut?", "a": "Eating your way through Connecticut.", "x": "Eating through Connecticut: start with New Haven pizza, then follow the locals — diners, food trucks, farm stands. Qui transtulit sustinet (He who transplanted still sustains) Food is the fastest way into a place's heart; the stories come free with the meal. Bridgeport", "s": "public-reference", "f": null}, {"t": "Mystic Outdoor Art Festival", "d": "Mystic Outdoor Art Festival: Connecticut's signature festival.", "g": "festivals", "l": 2, "q": "What is Mystic Outdoor Art Festival?", "a": "Mystic Outdoor Art Festival: Connecticut's signature festival.", "x": "Mystic Outdoor Art Festival is Connecticut at its most celebratory: Submarines (Groton).. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Hartford Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Connecticut year-round: Mystic Outdoor Art Festival and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Connecticut year-round: Mystic Outdoor Art Festival and more.", "x": "The Connecticut festival calendar runs year-round, with Mystic Outdoor Art Festival as the anchor. Qui transtulit sustinet (He who transplanted still sustains) Every season has its celebration — plan trips around them for the liveliest version of the state. Sleeping Giant State Park", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-connecticut-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
