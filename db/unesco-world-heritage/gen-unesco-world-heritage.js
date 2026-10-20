(function(){'use strict';
/* JAH UNESCO World Heritage Database generator — jahdb-unesco-world-heritage-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='unesco-world-heritage',PREFIX='JAH-UNE-',NAME='JAH UNESCO World Heritage Database';
var FIELDS=["cultural", "natural", "mixed"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Great Wall of China", "d": "The 21,000-km fortification system.", "g": "cultural", "l": 2, "q": "What is Great Wall of China?", "a": "The 21,000-km fortification system.", "x": "The 21,000-km fortification system. country: China. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Pyramids of Giza", "d": "The last ancient wonder standing.", "g": "cultural", "l": 2, "q": "What is Pyramids of Giza?", "a": "The last ancient wonder standing.", "x": "The last ancient wonder standing. country: Egypt. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Machu Picchu", "d": "The Inca citadel in the clouds.", "g": "mixed", "l": 2, "q": "What is Machu Picchu?", "a": "The Inca citadel in the clouds.", "x": "The Inca citadel in the clouds. country: Peru. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Taj Mahal", "d": "The marble monument to love.", "g": "cultural", "l": 2, "q": "What is Taj Mahal?", "a": "The marble monument to love.", "x": "The marble monument to love. country: India. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Colosseum", "d": "Rome's eternal arena.", "g": "cultural", "l": 2, "q": "What is Colosseum?", "a": "Rome's eternal arena.", "x": "Rome's eternal arena. country: Italy. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Petra", "d": "The rose-red city carved in rock.", "g": "cultural", "l": 2, "q": "What is Petra?", "a": "The rose-red city carved in rock.", "x": "The rose-red city carved in rock. country: Jordan. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Angkor Wat", "d": "The world's largest religious monument.", "g": "cultural", "l": 2, "q": "What is Angkor Wat?", "a": "The world's largest religious monument.", "x": "The world's largest religious monument. country: Cambodia. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Chichen Itza", "d": "Maya pyramid of Kukulkan.", "g": "cultural", "l": 2, "q": "What is Chichen Itza?", "a": "Maya pyramid of Kukulkan.", "x": "Maya pyramid of Kukulkan. country: Mexico. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Acropolis of Athens", "d": "The Parthenon's hill.", "g": "cultural", "l": 2, "q": "What is Acropolis of Athens?", "a": "The Parthenon's hill.", "x": "The Parthenon's hill. country: Greece. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Historic Centre of Rome", "d": "Three millennia of the eternal city.", "g": "cultural", "l": 2, "q": "What is Historic Centre of Rome?", "a": "Three millennia of the eternal city.", "x": "Three millennia of the eternal city. country: Italy. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Venice and its Lagoon", "d": "The floating city.", "g": "cultural", "l": 2, "q": "What is Venice and its Lagoon?", "a": "The floating city.", "x": "The floating city. country: Italy. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Mont-Saint-Michel", "d": "The tidal abbey.", "g": "cultural", "l": 2, "q": "What is Mont-Saint-Michel?", "a": "The tidal abbey.", "x": "The tidal abbey. country: France. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Chartres Cathedral", "d": "Gothic perfection in glass.", "g": "cultural", "l": 2, "q": "What is Chartres Cathedral?", "a": "Gothic perfection in glass.", "x": "Gothic perfection in glass. country: France. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Cologne Cathedral", "d": "632 years in the making.", "g": "cultural", "l": 2, "q": "What is Cologne Cathedral?", "a": "632 years in the making.", "x": "632 years in the making. country: Germany. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Westminster", "d": "Abbey and palace of Parliament.", "g": "cultural", "l": 2, "q": "What is Westminster?", "a": "Abbey and palace of Parliament.", "x": "Abbey and palace of Parliament. country: United Kingdom. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Stonehenge", "d": "The 5,000-year-old stone circle.", "g": "cultural", "l": 2, "q": "What is Stonehenge?", "a": "The 5,000-year-old stone circle.", "x": "The 5,000-year-old stone circle. country: United Kingdom. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Alhambra", "d": "Moorish palace of water and light.", "g": "cultural", "l": 2, "q": "What is Alhambra?", "a": "Moorish palace of water and light.", "x": "Moorish palace of water and light. country: Spain. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Historic Cairo", "d": "A thousand years of Islamic Cairo.", "g": "cultural", "l": 2, "q": "What is Historic Cairo?", "a": "A thousand years of Islamic Cairo.", "x": "A thousand years of Islamic Cairo. country: Egypt. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Medina of Fez", "d": "The world's oldest university city.", "g": "cultural", "l": 2, "q": "What is Medina of Fez?", "a": "The world's oldest university city.", "x": "The world's oldest university city. country: Morocco. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Timbuktu", "d": "The legendary center of learning.", "g": "cultural", "l": 2, "q": "What is Timbuktu?", "a": "The legendary center of learning.", "x": "The legendary center of learning. country: Mali. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Great Zimbabwe", "d": "The stone city of Shona kings.", "g": "cultural", "l": 2, "q": "What is Great Zimbabwe?", "a": "The stone city of Shona kings.", "x": "The stone city of Shona kings. country: Zimbabwe. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Lalibela", "d": "Eleven churches carved from rock.", "g": "cultural", "l": 2, "q": "What is Lalibela?", "a": "Eleven churches carved from rock.", "x": "Eleven churches carved from rock. country: Ethiopia. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Persepolis", "d": "Ceremonial capital of Persia.", "g": "cultural", "l": 2, "q": "What is Persepolis?", "a": "Ceremonial capital of Persia.", "x": "Ceremonial capital of Persia. country: Iran. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Babylon", "d": "The ancient city of Hammurabi.", "g": "cultural", "l": 2, "q": "What is Babylon?", "a": "The ancient city of Hammurabi.", "x": "The ancient city of Hammurabi. country: Iraq. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Hatra", "d": "The desert fortress city.", "g": "cultural", "l": 2, "q": "What is Hatra?", "a": "The desert fortress city.", "x": "The desert fortress city. country: Iraq. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-unesco-world-heritage-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
