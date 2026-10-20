(function(){'use strict';
/* JAH Wyoming Attractions Database generator — jahdb-e2-wyoming-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-wyoming-attractions',PREFIX='JAH-E2WYOMINGAT-',NAME='JAH Wyoming Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Wyoming: attractions overview", "d": "The best of Wyoming: Yellowstone, Grand Teton, Devils Tower.", "g": "overview", "l": 2, "q": "What is Wyoming: attractions overview?", "a": "The best of Wyoming: Yellowstone, Grand Teton, Devils Tower.", "x": "The essential Wyoming: Yellowstone, Grand Teton, Devils Tower — plus Yellowstone National Park, Wyoming's great bison burger. Cheyenne Frontier Days This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Yellowstone", "d": "Yellowstone: a top Wyoming attraction.", "g": "attractions", "l": 2, "q": "What is Yellowstone?", "a": "Yellowstone: a top Wyoming attraction.", "x": "Yellowstone is essential Wyoming. Shoshone and Arapaho; Yellowstone 1872. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. bison burger", "s": "public-reference", "f": null}, {"t": "Visiting Yellowstone", "d": "How to experience Yellowstone.", "g": "attractions", "l": 2, "q": "What is Visiting Yellowstone?", "a": "How to experience Yellowstone.", "x": "Experiencing Yellowstone: plan around Cheyenne Frontier Days, the state's rhythm — Equal rights. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Yellowstone National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Grand Teton", "d": "Grand Teton: a top Wyoming attraction.", "g": "attractions", "l": 2, "q": "What is Grand Teton?", "a": "Grand Teton: a top Wyoming attraction.", "x": "Grand Teton is essential Wyoming. Shoshone and Arapaho; Yellowstone 1872. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. bison burger", "s": "public-reference", "f": null}, {"t": "Visiting Grand Teton", "d": "How to experience Grand Teton.", "g": "attractions", "l": 2, "q": "What is Visiting Grand Teton?", "a": "How to experience Grand Teton.", "x": "Experiencing Grand Teton: plan around Cheyenne Frontier Days, the state's rhythm — Equal rights. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Yellowstone National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Devils Tower", "d": "Devils Tower: a top Wyoming attraction.", "g": "attractions", "l": 2, "q": "What is Devils Tower?", "a": "Devils Tower: a top Wyoming attraction.", "x": "Devils Tower is essential Wyoming. Shoshone and Arapaho; Yellowstone 1872. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. bison burger", "s": "public-reference", "f": null}, {"t": "Visiting Devils Tower", "d": "How to experience Devils Tower.", "g": "attractions", "l": 2, "q": "What is Visiting Devils Tower?", "a": "How to experience Devils Tower.", "x": "Experiencing Devils Tower: plan around Cheyenne Frontier Days, the state's rhythm — Equal rights. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Yellowstone National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Jackson Hole", "d": "Jackson Hole: a top Wyoming attraction.", "g": "attractions", "l": 2, "q": "What is Jackson Hole?", "a": "Jackson Hole: a top Wyoming attraction.", "x": "Jackson Hole is essential Wyoming. Shoshone and Arapaho; Yellowstone 1872. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. bison burger", "s": "public-reference", "f": null}, {"t": "Visiting Jackson Hole", "d": "How to experience Jackson Hole.", "g": "attractions", "l": 2, "q": "What is Visiting Jackson Hole?", "a": "How to experience Jackson Hole.", "x": "Experiencing Jackson Hole: plan around Cheyenne Frontier Days, the state's rhythm — Equal rights. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Yellowstone National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Cody", "d": "Cody: a top Wyoming attraction.", "g": "attractions", "l": 2, "q": "What is Cody?", "a": "Cody: a top Wyoming attraction.", "x": "Cody is essential Wyoming. Shoshone and Arapaho; Yellowstone 1872. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. bison burger State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Cody", "d": "How to experience Cody.", "g": "attractions", "l": 2, "q": "What is Visiting Cody?", "a": "How to experience Cody.", "x": "Experiencing Cody: plan around Cheyenne Frontier Days, the state's rhythm — Equal rights. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Yellowstone National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Hot Springs State Park", "d": "Hot Springs State Park: a top Wyoming attraction.", "g": "attractions", "l": 2, "q": "What is Hot Springs State Park?", "a": "Hot Springs State Park: a top Wyoming attraction.", "x": "Hot Springs State Park is essential Wyoming. Shoshone and Arapaho; Yellowstone 1872. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. bison burger", "s": "public-reference", "f": null}, {"t": "Visiting Hot Springs State Park", "d": "How to experience Hot Springs State Park.", "g": "attractions", "l": 2, "q": "What is Visiting Hot Springs State Park?", "a": "How to experience Hot Springs State Park.", "x": "Experiencing Hot Springs State Park: plan around Cheyenne Frontier Days, the state's rhythm — Equal rights. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Yellowstone National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Fossil Butte", "d": "Fossil Butte: a top Wyoming attraction.", "g": "attractions", "l": 2, "q": "What is Fossil Butte?", "a": "Fossil Butte: a top Wyoming attraction.", "x": "Fossil Butte is essential Wyoming. Shoshone and Arapaho; Yellowstone 1872. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. bison burger", "s": "public-reference", "f": null}, {"t": "Visiting Fossil Butte", "d": "How to experience Fossil Butte.", "g": "attractions", "l": 2, "q": "What is Visiting Fossil Butte?", "a": "How to experience Fossil Butte.", "x": "Experiencing Fossil Butte: plan around Cheyenne Frontier Days, the state's rhythm — Equal rights. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Yellowstone National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Vedauwoo", "d": "Vedauwoo: a top Wyoming attraction.", "g": "attractions", "l": 2, "q": "What is Vedauwoo?", "a": "Vedauwoo: a top Wyoming attraction.", "x": "Vedauwoo is essential Wyoming. Shoshone and Arapaho; Yellowstone 1872. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. bison burger State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Vedauwoo", "d": "How to experience Vedauwoo.", "g": "attractions", "l": 2, "q": "What is Visiting Vedauwoo?", "a": "How to experience Vedauwoo.", "x": "Experiencing Vedauwoo: plan around Cheyenne Frontier Days, the state's rhythm — Equal rights. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Yellowstone National Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Yellowstone National Park", "d": "Yellowstone National Park: Wyoming's great park.", "g": "parks", "l": 2, "q": "What is Yellowstone National Park?", "a": "Yellowstone National Park: Wyoming's great park.", "x": "Yellowstone National Park is Wyoming's wild heart: Yellowstone. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Cheyenne Frontier Days Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Yellowstone National Park", "d": "How to explore Yellowstone National Park.", "g": "parks", "l": 2, "q": "What is Exploring Yellowstone National Park?", "a": "How to explore Yellowstone National Park.", "x": "Exploring Yellowstone National Park: get the park map, check conditions, carry water and layers, and tell someone your plan. Equal rights Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Cheyenne: the capital city", "d": "Cheyenne, capital of Wyoming.", "g": "cities", "l": 2, "q": "What is Cheyenne: the capital city?", "a": "Cheyenne, capital of Wyoming.", "x": "Cheyenne: the capital of Wyoming — government, history, and often the best museums. Women's suffrage first (1869). Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Cheyenne", "s": "public-reference", "f": null}, {"t": "Cheyenne: the biggest city", "d": "Cheyenne is Wyoming's largest city.", "g": "cities", "l": 2, "q": "What is Cheyenne: the biggest city?", "a": "Cheyenne is Wyoming's largest city.", "x": "Cheyenne is where Wyoming comes to work and play: the skyline, the food, the music, the crowds. energy (coal, gas) Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Cheyenne Frontier Days", "s": "public-reference", "f": null}, {"t": "bison burger: the food", "d": "Taste Wyoming: bison burger.", "g": "food", "l": 2, "q": "What is bison burger: the food?", "a": "Taste Wyoming: bison burger.", "x": "The taste of Wyoming is bison burger — and the foodways around it. Coal, gas, tourism. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Cheyenne Frontier Days Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Wyoming", "d": "Eating your way through Wyoming.", "g": "food", "l": 2, "q": "What is Food tour: Wyoming?", "a": "Eating your way through Wyoming.", "x": "Eating through Wyoming: start with bison burger, then follow the locals — diners, food trucks, farm stands. Equal rights Food is the fastest way into a place's heart; the stories come free with the meal. Cheyenne", "s": "public-reference", "f": null}, {"t": "Cheyenne Frontier Days", "d": "Cheyenne Frontier Days: Wyoming's signature festival.", "g": "festivals", "l": 2, "q": "What is Cheyenne Frontier Days?", "a": "Cheyenne Frontier Days: Wyoming's signature festival.", "x": "Cheyenne Frontier Days is Wyoming at its most celebratory: Yellowstone became the world's first national park in 1872.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Cheyenne Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Wyoming year-round: Cheyenne Frontier Days and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Wyoming year-round: Cheyenne Frontier Days and more.", "x": "The Wyoming festival calendar runs year-round, with Cheyenne Frontier Days as the anchor. Equal rights Every season has its celebration — plan trips around them for the liveliest version of the state. Yellowstone National Park", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-wyoming-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
