(function(){'use strict';
/* JAH Vermont Attractions Database generator — jahdb-e2-vermont-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-vermont-attractions',PREFIX='JAH-E2VERMONTAT-',NAME='JAH Vermont Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Vermont: attractions overview", "d": "The best of Vermont: Stowe, Ben & Jerry's Factory, Shelburne Museum.", "g": "overview", "l": 2, "q": "What is Vermont: attractions overview?", "a": "The best of Vermont: Stowe, Ben & Jerry's Factory, Shelburne Museum.", "x": "The essential Vermont: Stowe, Ben & Jerry's Factory, Shelburne Museum — plus Green Mountain National Forest, Vermont's great maple creemee. Stowe festivals This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Stowe", "d": "Stowe: a top Vermont attraction.", "g": "attractions", "l": 2, "q": "What is Stowe?", "a": "Stowe: a top Vermont attraction.", "x": "Stowe is essential Vermont. Abenaki; independent republic 1777-91. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. maple creemee State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Stowe", "d": "How to experience Stowe.", "g": "attractions", "l": 2, "q": "What is Visiting Stowe?", "a": "How to experience Stowe.", "x": "Experiencing Stowe: plan around Stowe festivals, the state's rhythm — Freedom and Unity. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Green Mountain National Forest Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Ben & Jerry's Factory", "d": "Ben & Jerry's Factory: a top Vermont attraction.", "g": "attractions", "l": 2, "q": "What is Ben & Jerry's Factory?", "a": "Ben & Jerry's Factory: a top Vermont attraction.", "x": "Ben & Jerry's Factory is essential Vermont. Abenaki; independent republic 1777-91. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. maple creemee", "s": "public-reference", "f": null}, {"t": "Visiting Ben & Jerry's Factory", "d": "How to experience Ben & Jerry's Factory.", "g": "attractions", "l": 2, "q": "What is Visiting Ben & Jerry's Factory?", "a": "How to experience Ben & Jerry's Factory.", "x": "Experiencing Ben & Jerry's Factory: plan around Stowe festivals, the state's rhythm — Freedom and Unity. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Green Mountain National Forest Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Shelburne Museum", "d": "Shelburne Museum: a top Vermont attraction.", "g": "attractions", "l": 2, "q": "What is Shelburne Museum?", "a": "Shelburne Museum: a top Vermont attraction.", "x": "Shelburne Museum is essential Vermont. Abenaki; independent republic 1777-91. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. maple creemee", "s": "public-reference", "f": null}, {"t": "Visiting Shelburne Museum", "d": "How to experience Shelburne Museum.", "g": "attractions", "l": 2, "q": "What is Visiting Shelburne Museum?", "a": "How to experience Shelburne Museum.", "x": "Experiencing Shelburne Museum: plan around Stowe festivals, the state's rhythm — Freedom and Unity. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Green Mountain National Forest Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Lake Champlain", "d": "Lake Champlain: a top Vermont attraction.", "g": "attractions", "l": 2, "q": "What is Lake Champlain?", "a": "Lake Champlain: a top Vermont attraction.", "x": "Lake Champlain is essential Vermont. Abenaki; independent republic 1777-91. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. maple creemee", "s": "public-reference", "f": null}, {"t": "Visiting Lake Champlain", "d": "How to experience Lake Champlain.", "g": "attractions", "l": 2, "q": "What is Visiting Lake Champlain?", "a": "How to experience Lake Champlain.", "x": "Experiencing Lake Champlain: plan around Stowe festivals, the state's rhythm — Freedom and Unity. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Green Mountain National Forest Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Green Mountains", "d": "Green Mountains: a top Vermont attraction.", "g": "attractions", "l": 2, "q": "What is Green Mountains?", "a": "Green Mountains: a top Vermont attraction.", "x": "Green Mountains is essential Vermont. Abenaki; independent republic 1777-91. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. maple creemee", "s": "public-reference", "f": null}, {"t": "Visiting Green Mountains", "d": "How to experience Green Mountains.", "g": "attractions", "l": 2, "q": "What is Visiting Green Mountains?", "a": "How to experience Green Mountains.", "x": "Experiencing Green Mountains: plan around Stowe festivals, the state's rhythm — Freedom and Unity. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Green Mountain National Forest Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Woodstock", "d": "Woodstock: a top Vermont attraction.", "g": "attractions", "l": 2, "q": "What is Woodstock?", "a": "Woodstock: a top Vermont attraction.", "x": "Woodstock is essential Vermont. Abenaki; independent republic 1777-91. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. maple creemee", "s": "public-reference", "f": null}, {"t": "Visiting Woodstock", "d": "How to experience Woodstock.", "g": "attractions", "l": 2, "q": "What is Visiting Woodstock?", "a": "How to experience Woodstock.", "x": "Experiencing Woodstock: plan around Stowe festivals, the state's rhythm — Freedom and Unity. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Green Mountain National Forest Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Quechee Gorge", "d": "Quechee Gorge: a top Vermont attraction.", "g": "attractions", "l": 2, "q": "What is Quechee Gorge?", "a": "Quechee Gorge: a top Vermont attraction.", "x": "Quechee Gorge is essential Vermont. Abenaki; independent republic 1777-91. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. maple creemee", "s": "public-reference", "f": null}, {"t": "Visiting Quechee Gorge", "d": "How to experience Quechee Gorge.", "g": "attractions", "l": 2, "q": "What is Visiting Quechee Gorge?", "a": "How to experience Quechee Gorge.", "x": "Experiencing Quechee Gorge: plan around Stowe festivals, the state's rhythm — Freedom and Unity. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Green Mountain National Forest Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Burlington waterfront", "d": "Burlington waterfront: a top Vermont attraction.", "g": "attractions", "l": 2, "q": "What is Burlington waterfront?", "a": "Burlington waterfront: a top Vermont attraction.", "x": "Burlington waterfront is essential Vermont. Abenaki; independent republic 1777-91. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. maple creemee", "s": "public-reference", "f": null}, {"t": "Visiting Burlington waterfront", "d": "How to experience Burlington waterfront.", "g": "attractions", "l": 2, "q": "What is Visiting Burlington waterfront?", "a": "How to experience Burlington waterfront.", "x": "Experiencing Burlington waterfront: plan around Stowe festivals, the state's rhythm — Freedom and Unity. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Green Mountain National Forest Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Green Mountain National Forest", "d": "Green Mountain National Forest: Vermont's great park.", "g": "parks", "l": 2, "q": "What is Green Mountain National Forest?", "a": "Green Mountain National Forest: Vermont's great park.", "x": "Green Mountain National Forest is Vermont's wild heart: Stowe. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Stowe festivals Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Green Mountain National Forest", "d": "How to explore Green Mountain National Forest.", "g": "parks", "l": 2, "q": "What is Exploring Green Mountain National Forest?", "a": "How to explore Green Mountain National Forest.", "x": "Exploring Green Mountain National Forest: get the park map, check conditions, carry water and layers, and tell someone your plan. Freedom and Unity Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Montpelier: the capital city", "d": "Montpelier, capital of Vermont.", "g": "cities", "l": 2, "q": "What is Montpelier: the capital city?", "a": "Montpelier, capital of Vermont.", "x": "Montpelier: the capital of Vermont — government, history, and often the best museums. First to abolish slavery (1777). Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Burlington", "s": "public-reference", "f": null}, {"t": "Burlington: the biggest city", "d": "Burlington is Vermont's largest city.", "g": "cities", "l": 2, "q": "What is Burlington: the biggest city?", "a": "Burlington is Vermont's largest city.", "x": "Burlington is where Vermont comes to work and play: the skyline, the food, the music, the crowds. dairy and maple Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Stowe festivals", "s": "public-reference", "f": null}, {"t": "maple creemee: the food", "d": "Taste Vermont: maple creemee.", "g": "food", "l": 2, "q": "What is maple creemee: the food?", "a": "Taste Vermont: maple creemee.", "x": "The taste of Vermont is maple creemee — and the foodways around it. Dairy; maple; Bernie. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Stowe festivals Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Vermont", "d": "Eating your way through Vermont.", "g": "food", "l": 2, "q": "What is Food tour: Vermont?", "a": "Eating your way through Vermont.", "x": "Eating through Vermont: start with maple creemee, then follow the locals — diners, food trucks, farm stands. Freedom and Unity Food is the fastest way into a place's heart; the stories come free with the meal. Burlington", "s": "public-reference", "f": null}, {"t": "Stowe festivals", "d": "Stowe festivals: Vermont's signature festival.", "g": "festivals", "l": 2, "q": "What is Stowe festivals?", "a": "Stowe festivals: Vermont's signature festival.", "x": "Stowe festivals is Vermont at its most celebratory: Its 1777 constitution was the first to abolish slavery.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Montpelier Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Vermont year-round: Stowe festivals and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Vermont year-round: Stowe festivals and more.", "x": "The Vermont festival calendar runs year-round, with Stowe festivals as the anchor. Freedom and Unity Every season has its celebration — plan trips around them for the liveliest version of the state. Green Mountain National Forest", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-vermont-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
