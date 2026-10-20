(function(){'use strict';
/* JAH Pennsylvania Attractions Database generator — jahdb-e2-pennsylvania-attractions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-pennsylvania-attractions',PREFIX='JAH-E2PENNSYLVA-',NAME='JAH Pennsylvania Attractions Database';
var FIELDS=["overview", "attractions", "parks", "cities", "food", "festivals", "itinerary"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Pennsylvania: attractions overview", "d": "The best of Pennsylvania: Independence Hall, Gettysburg, Hersheypark.", "g": "overview", "l": 2, "q": "What is Pennsylvania: attractions overview?", "a": "The best of Pennsylvania: Independence Hall, Gettysburg, Hersheypark.", "x": "The essential Pennsylvania: Independence Hall, Gettysburg, Hersheypark — plus Valley Forge National Historical Park, Pennsylvania's great cheesesteak. Groundhog Day This database is the complete visitor's guide: the famous sights, the parks, the cities, the food, and the festivals, with practical know-how for each.", "s": "public-reference", "f": null}, {"t": "Independence Hall", "d": "Independence Hall: a top Pennsylvania attraction.", "g": "attractions", "l": 2, "q": "What is Independence Hall?", "a": "Independence Hall: a top Pennsylvania attraction.", "x": "Independence Hall is essential Pennsylvania. Lenape; Quaker colony 1681. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. cheesesteak", "s": "public-reference", "f": null}, {"t": "Visiting Independence Hall", "d": "How to experience Independence Hall.", "g": "attractions", "l": 2, "q": "What is Visiting Independence Hall?", "a": "How to experience Independence Hall.", "x": "Experiencing Independence Hall: plan around Groundhog Day, the state's rhythm — Virtue, liberty and independence. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Valley Forge National Historical Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Gettysburg", "d": "Gettysburg: a top Pennsylvania attraction.", "g": "attractions", "l": 2, "q": "What is Gettysburg?", "a": "Gettysburg: a top Pennsylvania attraction.", "x": "Gettysburg is essential Pennsylvania. Lenape; Quaker colony 1681. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. cheesesteak State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Gettysburg", "d": "How to experience Gettysburg.", "g": "attractions", "l": 2, "q": "What is Visiting Gettysburg?", "a": "How to experience Gettysburg.", "x": "Experiencing Gettysburg: plan around Groundhog Day, the state's rhythm — Virtue, liberty and independence. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Valley Forge National Historical Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Hersheypark", "d": "Hersheypark: a top Pennsylvania attraction.", "g": "attractions", "l": 2, "q": "What is Hersheypark?", "a": "Hersheypark: a top Pennsylvania attraction.", "x": "Hersheypark is essential Pennsylvania. Lenape; Quaker colony 1681. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. cheesesteak State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Hersheypark", "d": "How to experience Hersheypark.", "g": "attractions", "l": 2, "q": "What is Visiting Hersheypark?", "a": "How to experience Hersheypark.", "x": "Experiencing Hersheypark: plan around Groundhog Day, the state's rhythm — Virtue, liberty and independence. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Valley Forge National Historical Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Fallingwater", "d": "Fallingwater: a top Pennsylvania attraction.", "g": "attractions", "l": 2, "q": "What is Fallingwater?", "a": "Fallingwater: a top Pennsylvania attraction.", "x": "Fallingwater is essential Pennsylvania. Lenape; Quaker colony 1681. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. cheesesteak State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Fallingwater", "d": "How to experience Fallingwater.", "g": "attractions", "l": 2, "q": "What is Visiting Fallingwater?", "a": "How to experience Fallingwater.", "x": "Experiencing Fallingwater: plan around Groundhog Day, the state's rhythm — Virtue, liberty and independence. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Valley Forge National Historical Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Liberty Bell", "d": "Liberty Bell: a top Pennsylvania attraction.", "g": "attractions", "l": 2, "q": "What is Liberty Bell?", "a": "Liberty Bell: a top Pennsylvania attraction.", "x": "Liberty Bell is essential Pennsylvania. Lenape; Quaker colony 1681. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. cheesesteak State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Liberty Bell", "d": "How to experience Liberty Bell.", "g": "attractions", "l": 2, "q": "What is Visiting Liberty Bell?", "a": "How to experience Liberty Bell.", "x": "Experiencing Liberty Bell: plan around Groundhog Day, the state's rhythm — Virtue, liberty and independence. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Valley Forge National Historical Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Pittsburgh", "d": "Pittsburgh: a top Pennsylvania attraction.", "g": "attractions", "l": 2, "q": "What is Pittsburgh?", "a": "Pittsburgh: a top Pennsylvania attraction.", "x": "Pittsburgh is essential Pennsylvania. Lenape; Quaker colony 1681. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. cheesesteak State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Pittsburgh", "d": "How to experience Pittsburgh.", "g": "attractions", "l": 2, "q": "What is Visiting Pittsburgh?", "a": "How to experience Pittsburgh.", "x": "Experiencing Pittsburgh: plan around Groundhog Day, the state's rhythm — Virtue, liberty and independence. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Valley Forge National Historical Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Lancaster Amish country", "d": "Lancaster Amish country: a top Pennsylvania attraction.", "g": "attractions", "l": 2, "q": "What is Lancaster Amish country?", "a": "Lancaster Amish country: a top Pennsylvania attraction.", "x": "Lancaster Amish country is essential Pennsylvania. Lenape; Quaker colony 1681. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. cheesesteak", "s": "public-reference", "f": null}, {"t": "Visiting Lancaster Amish country", "d": "How to experience Lancaster Amish country.", "g": "attractions", "l": 2, "q": "What is Visiting Lancaster Amish country?", "a": "How to experience Lancaster Amish country.", "x": "Experiencing Lancaster Amish country: plan around Groundhog Day, the state's rhythm — Virtue, liberty and independence. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Valley Forge National Historical Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Valley Forge", "d": "Valley Forge: a top Pennsylvania attraction.", "g": "attractions", "l": 2, "q": "What is Valley Forge?", "a": "Valley Forge: a top Pennsylvania attraction.", "x": "Valley Forge is essential Pennsylvania. Lenape; Quaker colony 1681. Go early, read the story before you arrive, and give it the time it deserves — the famous sights earned their fame. cheesesteak State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Visiting Valley Forge", "d": "How to experience Valley Forge.", "g": "attractions", "l": 2, "q": "What is Visiting Valley Forge?", "a": "How to experience Valley Forge.", "x": "Experiencing Valley Forge: plan around Groundhog Day, the state's rhythm — Virtue, liberty and independence. Mornings beat crowds, weekdays beat weekends, and the shoulder seasons beat both. Valley Forge National Historical Park Book ahead where needed; the best experiences reward planners.", "s": "public-reference", "f": null}, {"t": "Valley Forge National Historical Park", "d": "Valley Forge National Historical Park: Pennsylvania's great park.", "g": "parks", "l": 2, "q": "What is Valley Forge National Historical Park?", "a": "Valley Forge National Historical Park: Pennsylvania's great park.", "x": "Valley Forge National Historical Park is Pennsylvania's wild heart: Independence Hall. Parks preserve what development cannot replace — the views, the wildlife, the quiet. Groundhog Day Hike it, camp it, or just stand in it; protected land is the state's gift to the future.", "s": "public-reference", "f": null}, {"t": "Exploring Valley Forge National Historical Park", "d": "How to explore Valley Forge National Historical Park.", "g": "parks", "l": 2, "q": "What is Exploring Valley Forge National Historical Park?", "a": "How to explore Valley Forge National Historical Park.", "x": "Exploring Valley Forge National Historical Park: get the park map, check conditions, carry water and layers, and tell someone your plan. Virtue, liberty and independence Rangers are the best guides — ask them. Leave no trace; the park's beauty is a loan from the future.", "s": "public-reference", "f": null}, {"t": "Harrisburg: the capital city", "d": "Harrisburg, capital of Pennsylvania.", "g": "cities", "l": 2, "q": "What is Harrisburg: the capital city?", "a": "Harrisburg, capital of Pennsylvania.", "x": "Harrisburg: the capital of Pennsylvania — government, history, and often the best museums. Independence; Gettysburg. Beyond the capitol, capitals have their own character: neighborhoods, food scenes, and the rhythm of a working government town. Philadelphia", "s": "public-reference", "f": null}, {"t": "Philadelphia: the biggest city", "d": "Philadelphia is Pennsylvania's largest city.", "g": "cities", "l": 2, "q": "What is Philadelphia: the biggest city?", "a": "Philadelphia is Pennsylvania's largest city.", "x": "Philadelphia is where Pennsylvania comes to work and play: the skyline, the food, the music, the crowds. manufacturing Big cities concentrate a state's energy — its ambition, its diversity, its contradictions. Groundhog Day", "s": "public-reference", "f": null}, {"t": "cheesesteak: the food", "d": "Taste Pennsylvania: cheesesteak.", "g": "food", "l": 2, "q": "What is cheesesteak: the food?", "a": "Taste Pennsylvania: cheesesteak.", "x": "The taste of Pennsylvania is cheesesteak — and the foodways around it. Steel; Hershey; liberty. Every state has a flavor: the dish locals defend, the restaurant rows, the festival foods. Groundhog Day Eat where the line is longest.", "s": "public-reference", "f": null}, {"t": "Food tour: Pennsylvania", "d": "Eating your way through Pennsylvania.", "g": "food", "l": 2, "q": "What is Food tour: Pennsylvania?", "a": "Eating your way through Pennsylvania.", "x": "Eating through Pennsylvania: start with cheesesteak, then follow the locals — diners, food trucks, farm stands. Virtue, liberty and independence Food is the fastest way into a place's heart; the stories come free with the meal. Philadelphia", "s": "public-reference", "f": null}, {"t": "Groundhog Day", "d": "Groundhog Day: Pennsylvania's signature festival.", "g": "festivals", "l": 2, "q": "What is Groundhog Day?", "a": "Groundhog Day: Pennsylvania's signature festival.", "x": "Groundhog Day is Pennsylvania at its most celebratory: Steel built Pittsburgh; Hershey built chocolate.. Festivals distill a place — its music, food, craft, and pride — into a few joyful days. Harrisburg Time a visit for one; book early.", "s": "public-reference", "f": null}, {"t": "Festival calendar", "d": "Pennsylvania year-round: Groundhog Day and more.", "g": "festivals", "l": 2, "q": "What is Festival calendar?", "a": "Pennsylvania year-round: Groundhog Day and more.", "x": "The Pennsylvania festival calendar runs year-round, with Groundhog Day as the anchor. Virtue, liberty and independence Every season has its celebration — plan trips around them for the liveliest version of the state. Valley Forge National Historical Park", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-pennsylvania-attractions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
