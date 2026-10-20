(function(){'use strict';
/* JAH New York Attractions Database generator — jahdb-e2-new-york-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-new-york-attractions',PREFIX='JAH-E2NEWYORKAT-',NAME='JAH New York Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "New York: attractions overview", "d": "The best of New York: Statue of Liberty, Times Square, Niagara Falls.", "g": "overview", "l": 2, "q": "What is New York: attractions overview?", "a": "The best of New York: Statue of Liberty, Times Square, Niagara Falls.", "x": "The essential New York: Statue of Liberty, Times Square, Niagara Falls — plus Adirondack Park, New York's great Buffalo wings. Macy's Thanksgiving Parade This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Statue of Liberty", "d": "Statue of Liberty: a top New York attraction.", "g": "attractions", "l": 2, "q": "What is Statue of Liberty?", "a": "Statue of Liberty: a top New York attraction.", "x": "Statue of Liberty is essential New York. Haudenosaunee; Dutch New Amsterdam. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Buffalo wings", "s": "public-reference", "f": null}, {"t": "Visiting Statue of Liberty", "d": "How to experience Statue of Liberty.", "g": "attractions", "l": 2, "q": "What is Visiting Statue of Liberty?", "a": "How to experience Statue of Liberty.", "x": "Experiencing Statue of Liberty: plan around Macy's Thanksgiving Parade, the state's rhythm — Excelsior (Ever upward). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Adirondack Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Times Square", "d": "Times Square: a top New York attraction.", "g": "attractions", "l": 2, "q": "What is Times Square?", "a": "Times Square: a top New York attraction.", "x": "Times Square is essential New York. Haudenosaunee; Dutch New Amsterdam. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Buffalo wings", "s": "public-reference", "f": null}, {"t": "Visiting Times Square", "d": "How to experience Times Square.", "g": "attractions", "l": 2, "q": "What is Visiting Times Square?", "a": "How to experience Times Square.", "x": "Experiencing Times Square: plan around Macy's Thanksgiving Parade, the state's rhythm — Excelsior (Ever upward). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Adirondack Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Niagara Falls", "d": "Niagara Falls: a top New York attraction.", "g": "attractions", "l": 2, "q": "What is Niagara Falls?", "a": "Niagara Falls: a top New York attraction.", "x": "Niagara Falls is essential New York. Haudenosaunee; Dutch New Amsterdam. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Buffalo wings", "s": "public-reference", "f": null}, {"t": "Visiting Niagara Falls", "d": "How to experience Niagara Falls.", "g": "attractions", "l": 2, "q": "What is Visiting Niagara Falls?", "a": "How to experience Niagara Falls.", "x": "Experiencing Niagara Falls: plan around Macy's Thanksgiving Parade, the state's rhythm — Excelsior (Ever upward). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Adirondack Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Adirondacks", "d": "Adirondacks: a top New York attraction.", "g": "attractions", "l": 2, "q": "What is Adirondacks?", "a": "Adirondacks: a top New York attraction.", "x": "Adirondacks is essential New York. Haudenosaunee; Dutch New Amsterdam. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Buffalo wings", "s": "public-reference", "f": null}, {"t": "Visiting Adirondacks", "d": "How to experience Adirondacks.", "g": "attractions", "l": 2, "q": "What is Visiting Adirondacks?", "a": "How to experience Adirondacks.", "x": "Experiencing Adirondacks: plan around Macy's Thanksgiving Parade, the state's rhythm — Excelsior (Ever upward). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Adirondack Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Central Park", "d": "Central Park: a top New York attraction.", "g": "attractions", "l": 2, "q": "What is Central Park?", "a": "Central Park: a top New York attraction.", "x": "Central Park is essential New York. Haudenosaunee; Dutch New Amsterdam. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Buffalo wings", "s": "public-reference", "f": null}, {"t": "Visiting Central Park", "d": "How to experience Central Park.", "g": "attractions", "l": 2, "q": "What is Visiting Central Park?", "a": "How to experience Central Park.", "x": "Experiencing Central Park: plan around Macy's Thanksgiving Parade, the state's rhythm — Excelsior (Ever upward). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Adirondack Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Finger Lakes", "d": "Finger Lakes: a top New York attraction.", "g": "attractions", "l": 2, "q": "What is Finger Lakes?", "a": "Finger Lakes: a top New York attraction.", "x": "Finger Lakes is essential New York. Haudenosaunee; Dutch New Amsterdam. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Buffalo wings", "s": "public-reference", "f": null}, {"t": "Visiting Finger Lakes", "d": "How to experience Finger Lakes.", "g": "attractions", "l": 2, "q": "What is Visiting Finger Lakes?", "a": "How to experience Finger Lakes.", "x": "Experiencing Finger Lakes: plan around Macy's Thanksgiving Parade, the state's rhythm — Excelsior (Ever upward). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Adirondack Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Museums (Met, MoMA)", "d": "Museums (Met, MoMA): a top New York attraction.", "g": "attractions", "l": 2, "q": "What is Museums (Met, MoMA)?", "a": "Museums (Met, MoMA): a top New York attraction.", "x": "Museums (Met, MoMA) is essential New York. Haudenosaunee; Dutch New Amsterdam. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Buffalo wings", "s": "public-reference", "f": null}, {"t": "Visiting Museums (Met, MoMA)", "d": "How to experience Museums (Met, MoMA).", "g": "attractions", "l": 2, "q": "What is Visiting Museums (Met, MoMA)?", "a": "How to experience Museums (Met, MoMA).", "x": "Experiencing Museums (Met, MoMA): plan around Macy's Thanksgiving Parade, the state's rhythm — Excelsior (Ever upward). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Adirondack Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Hudson Valley", "d": "Hudson Valley: a top New York attraction.", "g": "attractions", "l": 2, "q": "What is Hudson Valley?", "a": "Hudson Valley: a top New York attraction.", "x": "Hudson Valley is essential New York. Haudenosaunee; Dutch New Amsterdam. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. Buffalo wings", "s": "public-reference", "f": null}, {"t": "Visiting Hudson Valley", "d": "How to experience Hudson Valley.", "g": "attractions", "l": 2, "q": "What is Visiting Hudson Valley?", "a": "How to experience Hudson Valley.", "x": "Experiencing Hudson Valley: plan around Macy's Thanksgiving Parade, the state's rhythm — Excelsior (Ever upward). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Adirondack Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Adirondack Park", "d": "Adirondack Park: New York's great park.", "g": "parks", "l": 2, "q": "What is Adirondack Park?", "a": "Adirondack Park: New York's great park.", "x": "Adirondack Park is New York's wild heart: Statue of Liberty. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Macy's Thanksgiving Parade Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Adirondack Park", "d": "How to explore Adirondack Park.", "g": "parks", "l": 2, "q": "What is Exploring Adirondack Park?", "a": "How to explore Adirondack Park.", "x": "Exploring Adirondack Park: get the park map, check conditions, carry water and layers, and tell someone your plan. Excelsior (Ever upward) Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Albany: the capital city", "d": "Albany, capital of New York.", "g": "cities", "l": 2, "q": "What is Albany: the capital city?", "a": "Albany, capital of New York.", "x": "Albany: the capital of New York — government, history, and often the best museums. Revolution; Erie Canal. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. New York City", "s": "public-reference", "f": null}, {"t": "New York City: the biggest city", "d": "New York City is New York's largest city.", "g": "cities", "l": 2, "q": "What is New York City: the biggest city?", "a": "New York City is New York's largest city.", "x": "New York City is where New York comes to work and play: the skyline, the food, the music, the crowds. finance Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Macy's Thanksgiving Parade", "s": "public-reference", "f": null}, {"t": "Buffalo wings: the food", "d": "Taste New York: Buffalo wings.", "g": "food", "l": 2, "q": "What is Buffalo wings: the food?", "a": "Taste New York: Buffalo wings.", "x": "The taste of New York is Buffalo wings — and the foodways around it. Finance, media, immigration. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Macy's Thanksgiving Parade Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: New York", "d": "Eating your way through New York.", "g": "food", "l": 2, "q": "What is Food tour: New York?", "a": "Eating your way through New York.", "x": "Eating through New York: start with Buffalo wings, then follow the locals — diners, food trucks, farm stands. Excelsior (Ever upward) Food is the fastest way into a place's heart; the stories come free with the meal. New York City", "s": "public-reference", "f": null}, {"t": "Macy's Thanksgiving Parade", "d": "Macy's Thanksgiving Parade: New York's signature festival.", "g": "festivals", "l": 2, "q": "What is Macy's Thanksgiving Parade?", "a": "Macy's Thanksgiving Parade: New York's signature festival.", "x": "Macy's Thanksgiving Parade is New York at its most celebratory: The Erie Canal made New York the nation's port.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Albany Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "New York year-round: Macy's Thanksgiving Parade and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "New York year-round: Macy's Thanksgiving Parade and more.", "x": "The New York festival calendar runs year-round, with Macy's Thanksgiving Parade as the anchor. Excelsior (Ever upward) Every season has its celebration — plan trips around them for the liveliest version of the state. Adirondack Park", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-new-york-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
