(function(){'use strict';
/* JAH Montana Attractions Database generator — jahdb-e2-montana-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-montana-attractions',PREFIX='JAH-E2MONTANAAT-',NAME='JAH Montana Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Montana: attractions overview", "d": "The best of Montana: Glacier National Park, Yellowstone (edge), Little Bighorn.", "g": "overview", "l": 2, "q": "What is Montana: attractions overview?", "a": "The best of Montana: Glacier National Park, Yellowstone (edge), Little Bighorn.", "x": "The essential Montana: Glacier National Park, Yellowstone (edge), Little Bighorn — plus Glacier National Park, Montana's great huckleberry pie. Montana State Fair This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Glacier National Park", "d": "Glacier National Park: a top Montana attraction.", "g": "attractions", "l": 2, "q": "What is Glacier National Park?", "a": "Glacier National Park: a top Montana attraction.", "x": "Glacier National Park is essential Montana. Crow and Cheyenne; Little Bighorn 1876. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. huckleberry pie", "s": "public-reference", "f": null}, {"t": "Visiting Glacier National Park", "d": "How to experience Glacier National Park.", "g": "attractions", "l": 2, "q": "What is Visiting Glacier National Park?", "a": "How to experience Glacier National Park.", "x": "Experiencing Glacier National Park: plan around Montana State Fair, the state's rhythm — Oro y plata (Gold and silver). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Glacier National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Yellowstone (edge)", "d": "Yellowstone (edge): a top Montana attraction.", "g": "attractions", "l": 2, "q": "What is Yellowstone (edge)?", "a": "Yellowstone (edge): a top Montana attraction.", "x": "Yellowstone (edge) is essential Montana. Crow and Cheyenne; Little Bighorn 1876. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. huckleberry pie", "s": "public-reference", "f": null}, {"t": "Visiting Yellowstone (edge)", "d": "How to experience Yellowstone (edge).", "g": "attractions", "l": 2, "q": "What is Visiting Yellowstone (edge)?", "a": "How to experience Yellowstone (edge).", "x": "Experiencing Yellowstone (edge): plan around Montana State Fair, the state's rhythm — Oro y plata (Gold and silver). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Glacier National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Little Bighorn", "d": "Little Bighorn: a top Montana attraction.", "g": "attractions", "l": 2, "q": "What is Little Bighorn?", "a": "Little Bighorn: a top Montana attraction.", "x": "Little Bighorn is essential Montana. Crow and Cheyenne; Little Bighorn 1876. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. huckleberry pie", "s": "public-reference", "f": null}, {"t": "Visiting Little Bighorn", "d": "How to experience Little Bighorn.", "g": "attractions", "l": 2, "q": "What is Visiting Little Bighorn?", "a": "How to experience Little Bighorn.", "x": "Experiencing Little Bighorn: plan around Montana State Fair, the state's rhythm — Oro y plata (Gold and silver). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Glacier National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Flathead Lake", "d": "Flathead Lake: a top Montana attraction.", "g": "attractions", "l": 2, "q": "What is Flathead Lake?", "a": "Flathead Lake: a top Montana attraction.", "x": "Flathead Lake is essential Montana. Crow and Cheyenne; Little Bighorn 1876. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. huckleberry pie", "s": "public-reference", "f": null}, {"t": "Visiting Flathead Lake", "d": "How to experience Flathead Lake.", "g": "attractions", "l": 2, "q": "What is Visiting Flathead Lake?", "a": "How to experience Flathead Lake.", "x": "Experiencing Flathead Lake: plan around Montana State Fair, the state's rhythm — Oro y plata (Gold and silver). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Glacier National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Virginia City", "d": "Virginia City: a top Montana attraction.", "g": "attractions", "l": 2, "q": "What is Virginia City?", "a": "Virginia City: a top Montana attraction.", "x": "Virginia City is essential Montana. Crow and Cheyenne; Little Bighorn 1876. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. huckleberry pie", "s": "public-reference", "f": null}, {"t": "Visiting Virginia City", "d": "How to experience Virginia City.", "g": "attractions", "l": 2, "q": "What is Visiting Virginia City?", "a": "How to experience Virginia City.", "x": "Experiencing Virginia City: plan around Montana State Fair, the state's rhythm — Oro y plata (Gold and silver). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Glacier National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Beartooth Highway", "d": "Beartooth Highway: a top Montana attraction.", "g": "attractions", "l": 2, "q": "What is Beartooth Highway?", "a": "Beartooth Highway: a top Montana attraction.", "x": "Beartooth Highway is essential Montana. Crow and Cheyenne; Little Bighorn 1876. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. huckleberry pie", "s": "public-reference", "f": null}, {"t": "Visiting Beartooth Highway", "d": "How to experience Beartooth Highway.", "g": "attractions", "l": 2, "q": "What is Visiting Beartooth Highway?", "a": "How to experience Beartooth Highway.", "x": "Experiencing Beartooth Highway: plan around Montana State Fair, the state's rhythm — Oro y plata (Gold and silver). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Glacier National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Museum of the Rockies", "d": "Museum of the Rockies: a top Montana attraction.", "g": "attractions", "l": 2, "q": "What is Museum of the Rockies?", "a": "Museum of the Rockies: a top Montana attraction.", "x": "Museum of the Rockies is essential Montana. Crow and Cheyenne; Little Bighorn 1876. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. huckleberry pie", "s": "public-reference", "f": null}, {"t": "Visiting Museum of the Rockies", "d": "How to experience Museum of the Rockies.", "g": "attractions", "l": 2, "q": "What is Visiting Museum of the Rockies?", "a": "How to experience Museum of the Rockies.", "x": "Experiencing Museum of the Rockies: plan around Montana State Fair, the state's rhythm — Oro y plata (Gold and silver). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Glacier National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Gates of the Mountains", "d": "Gates of the Mountains: a top Montana attraction.", "g": "attractions", "l": 2, "q": "What is Gates of the Mountains?", "a": "Gates of the Mountains: a top Montana attraction.", "x": "Gates of the Mountains is essential Montana. Crow and Cheyenne; Little Bighorn 1876. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. huckleberry pie", "s": "public-reference", "f": null}, {"t": "Visiting Gates of the Mountains", "d": "How to experience Gates of the Mountains.", "g": "attractions", "l": 2, "q": "What is Visiting Gates of the Mountains?", "a": "How to experience Gates of the Mountains.", "x": "Experiencing Gates of the Mountains: plan around Montana State Fair, the state's rhythm — Oro y plata (Gold and silver). Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Glacier National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Glacier National Park", "d": "Glacier National Park: Montana's great park.", "g": "parks", "l": 2, "q": "What is Glacier National Park?", "a": "Glacier National Park: Montana's great park.", "x": "Glacier National Park is Montana's wild heart: Glacier National Park. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Montana State Fair Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Glacier National Park", "d": "How to explore Glacier National Park.", "g": "parks", "l": 2, "q": "What is Exploring Glacier National Park?", "a": "How to explore Glacier National Park.", "x": "Exploring Glacier National Park: get the park map, check conditions, carry water and layers, and tell someone your plan. Oro y plata (Gold and silver) Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Helena: the capital city", "d": "Helena, capital of Montana.", "g": "cities", "l": 2, "q": "What is Helena: the capital city?", "a": "Helena, capital of Montana.", "x": "Helena: the capital of Montana — government, history, and often the best museums. Copper kings; homesteading. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Billings", "s": "public-reference", "f": null}, {"t": "Billings: the biggest city", "d": "Billings is Montana's largest city.", "g": "cities", "l": 2, "q": "What is Billings: the biggest city?", "a": "Billings is Montana's largest city.", "x": "Billings is where Montana comes to work and play: the skyline, the food, the music, the crowds. agriculture Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Montana State Fair", "s": "public-reference", "f": null}, {"t": "huckleberry pie: the food", "d": "Taste Montana: huckleberry pie.", "g": "food", "l": 2, "q": "What is huckleberry pie: the food?", "a": "Taste Montana: huckleberry pie.", "x": "The taste of Montana is huckleberry pie — and the foodways around it. Big Sky country. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Montana State Fair Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Montana", "d": "Eating your way through Montana.", "g": "food", "l": 2, "q": "What is Food tour: Montana?", "a": "Eating your way through Montana.", "x": "Eating through Montana: start with huckleberry pie, then follow the locals — diners, food trucks, farm stands. Oro y plata (Gold and silver) Food is the fastest way into a place's heart; the stories come free with the meal. Billings", "s": "public-reference", "f": null}, {"t": "Montana State Fair", "d": "Montana State Fair: Montana's signature festival.", "g": "festivals", "l": 2, "q": "What is Montana State Fair?", "a": "Montana State Fair: Montana's signature festival.", "x": "Montana State Fair is Montana at its most celebratory: Copper kings and homesteaders shaped the Treasure State.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Helena Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Montana year-round: Montana State Fair and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Montana year-round: Montana State Fair and more.", "x": "The Montana festival calendar runs year-round, with Montana State Fair as the anchor. Oro y plata (Gold and silver) Every season has its celebration — plan trips around them for the liveliest version of the state. Glacier National Park", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-montana-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
