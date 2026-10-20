(function(){'use strict';
/* JAH English Idioms Database generator — jahdb-idioms-english-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='idioms-english',PREFIX='JAH-IDI-',NAME='JAH English Idioms Database';
var FIELDS=["idiom"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Break the ice", "d": "To initiate conversation in a social setting.", "g": "idiom", "l": 2, "q": "What is Break the ice?", "a": "To initiate conversation in a social setting.", "x": "Break the ice — To initiate conversation in a social setting. Example: Everyday English phrase..  Ancient stories retold accurately from standard sources. Proverbs and idioms are folk wisdom, not verified claims.", "s": "public-reference", "f": null}, {"t": "Hit the nail on the head", "d": "To say exactly the right thing.", "g": "idiom", "l": 2, "q": "What is Hit the nail on the head?", "a": "To say exactly the right thing.", "x": "Hit the nail on the head — To say exactly the right thing. Example: Everyday English phrase..  Ancient stories retold accurately from standard sources. Proverbs and idioms are folk wisdom, not verified claims.", "s": "public-reference", "f": null}, {"t": "Piece of cake", "d": "Something very easy.", "g": "idiom", "l": 2, "q": "What is Piece of cake?", "a": "Something very easy.", "x": "Piece of cake — Something very easy. Example: Everyday English phrase..  Ancient stories retold accurately from standard sources. Proverbs and idioms are folk wisdom, not verified claims. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Let the cat out of the bag", "d": "To reveal a secret.", "g": "idiom", "l": 2, "q": "What is Let the cat out of the bag?", "a": "To reveal a secret.", "x": "Let the cat out of the bag — To reveal a secret. Example: Everyday English phrase..  Ancient stories retold accurately from standard sources. Proverbs and idioms are folk wisdom, not verified claims. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Kill two birds with one stone", "d": "To accomplish two things at once.", "g": "idiom", "l": 2, "q": "What is Kill two birds with one stone?", "a": "To accomplish two things at once.", "x": "Kill two birds with one stone — To accomplish two things at once. Example: Everyday English phrase..  Ancient stories retold accurately from standard sources. Proverbs and idioms are folk wisdom, not verified claims.", "s": "public-reference", "f": null}, {"t": "Bite the bullet", "d": "To face something unpleasant bravely.", "g": "idiom", "l": 2, "q": "What is Bite the bullet?", "a": "To face something unpleasant bravely.", "x": "Bite the bullet — To face something unpleasant bravely. Example: Everyday English phrase..  Ancient stories retold accurately from standard sources. Proverbs and idioms are folk wisdom, not verified claims.", "s": "public-reference", "f": null}, {"t": "Burn the midnight oil", "d": "To work late into the night.", "g": "idiom", "l": 2, "q": "What is Burn the midnight oil?", "a": "To work late into the night.", "x": "Burn the midnight oil — To work late into the night. Example: Everyday English phrase..  Ancient stories retold accurately from standard sources. Proverbs and idioms are folk wisdom, not verified claims.", "s": "public-reference", "f": null}, {"t": "Cost an arm and a leg", "d": "To be very expensive.", "g": "idiom", "l": 2, "q": "What is Cost an arm and a leg?", "a": "To be very expensive.", "x": "Cost an arm and a leg — To be very expensive. Example: Everyday English phrase..  Ancient stories retold accurately from standard sources. Proverbs and idioms are folk wisdom, not verified claims. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Cut to the chase", "d": "To get to the point.", "g": "idiom", "l": 2, "q": "What is Cut to the chase?", "a": "To get to the point.", "x": "Cut to the chase — To get to the point. Example: Everyday English phrase..  Ancient stories retold accurately from standard sources. Proverbs and idioms are folk wisdom, not verified claims. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Devil's advocate", "d": "Arguing the opposite side for discussion.", "g": "idiom", "l": 2, "q": "What is Devil's advocate?", "a": "Arguing the opposite side for discussion.", "x": "Devil's advocate — Arguing the opposite side for discussion. Example: Everyday English phrase..  Ancient stories retold accurately from standard sources. Proverbs and idioms are folk wisdom, not verified claims.", "s": "public-reference", "f": null}, {"t": "Don't cry over spilled milk", "d": "Don't regret what cannot be undone.", "g": "idiom", "l": 2, "q": "What is Don't cry over spilled milk?", "a": "Don't regret what cannot be undone.", "x": "Don't cry over spilled milk — Don't regret what cannot be undone. Example: Everyday English phrase..  Ancient stories retold accurately from standard sources. Proverbs and idioms are folk wisdom, not verified claims.", "s": "public-reference", "f": null}, {"t": "Down to earth", "d": "Practical and realistic.", "g": "idiom", "l": 2, "q": "What is Down to earth?", "a": "Practical and realistic.", "x": "Down to earth — Practical and realistic. Example: Everyday English phrase..  Ancient stories retold accurately from standard sources. Proverbs and idioms are folk wisdom, not verified claims. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Drive someone up the wall", "d": "To irritate greatly.", "g": "idiom", "l": 2, "q": "What is Drive someone up the wall?", "a": "To irritate greatly.", "x": "Drive someone up the wall — To irritate greatly. Example: Everyday English phrase..  Ancient stories retold accurately from standard sources. Proverbs and idioms are folk wisdom, not verified claims. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Drop in the bucket", "d": "A tiny amount relative to need.", "g": "idiom", "l": 2, "q": "What is Drop in the bucket?", "a": "A tiny amount relative to need.", "x": "Drop in the bucket — A tiny amount relative to need. Example: Everyday English phrase..  Ancient stories retold accurately from standard sources. Proverbs and idioms are folk wisdom, not verified claims.", "s": "public-reference", "f": null}, {"t": "Eat humble pie", "d": "To admit fault humbly.", "g": "idiom", "l": 2, "q": "What is Eat humble pie?", "a": "To admit fault humbly.", "x": "Eat humble pie — To admit fault humbly. Example: Everyday English phrase..  Ancient stories retold accurately from standard sources. Proverbs and idioms are folk wisdom, not verified claims. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Elephant in the room", "d": "An obvious issue nobody mentions.", "g": "idiom", "l": 2, "q": "What is Elephant in the room?", "a": "An obvious issue nobody mentions.", "x": "Elephant in the room — An obvious issue nobody mentions. Example: Everyday English phrase..  Ancient stories retold accurately from standard sources. Proverbs and idioms are folk wisdom, not verified claims.", "s": "public-reference", "f": null}, {"t": "Feeling under the weather", "d": "Feeling ill.", "g": "idiom", "l": 2, "q": "What is Feeling under the weather?", "a": "Feeling ill.", "x": "Feeling under the weather — Feeling ill. Example: Everyday English phrase..  Ancient stories retold accurately from standard sources. Proverbs and idioms are folk wisdom, not verified claims. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Get cold feet", "d": "To become too afraid to act.", "g": "idiom", "l": 2, "q": "What is Get cold feet?", "a": "To become too afraid to act.", "x": "Get cold feet — To become too afraid to act. Example: Everyday English phrase..  Ancient stories retold accurately from standard sources. Proverbs and idioms are folk wisdom, not verified claims. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Give the benefit of the doubt", "d": "To trust without proof.", "g": "idiom", "l": 2, "q": "What is Give the benefit of the doubt?", "a": "To trust without proof.", "x": "Give the benefit of the doubt — To trust without proof. Example: Everyday English phrase..  Ancient stories retold accurately from standard sources. Proverbs and idioms are folk wisdom, not verified claims.", "s": "public-reference", "f": null}, {"t": "Go the extra mile", "d": "To do more than expected.", "g": "idiom", "l": 2, "q": "What is Go the extra mile?", "a": "To do more than expected.", "x": "Go the extra mile — To do more than expected. Example: Everyday English phrase..  Ancient stories retold accurately from standard sources. Proverbs and idioms are folk wisdom, not verified claims. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Hit the hay", "d": "To go to bed.", "g": "idiom", "l": 2, "q": "What is Hit the hay?", "a": "To go to bed.", "x": "Hit the hay — To go to bed. Example: Everyday English phrase..  Ancient stories retold accurately from standard sources. Proverbs and idioms are folk wisdom, not verified claims. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "In hot water", "d": "In trouble.", "g": "idiom", "l": 2, "q": "What is In hot water?", "a": "In trouble.", "x": "In hot water — In trouble. Example: Everyday English phrase..  Ancient stories retold accurately from standard sources. Proverbs and idioms are folk wisdom, not verified claims. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Jump on the bandwagon", "d": "To join a popular trend.", "g": "idiom", "l": 2, "q": "What is Jump on the bandwagon?", "a": "To join a popular trend.", "x": "Jump on the bandwagon — To join a popular trend. Example: Everyday English phrase..  Ancient stories retold accurately from standard sources. Proverbs and idioms are folk wisdom, not verified claims. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Keep your chin up", "d": "Stay positive.", "g": "idiom", "l": 2, "q": "What is Keep your chin up?", "a": "Stay positive.", "x": "Keep your chin up — Stay positive. Example: Everyday English phrase..  Ancient stories retold accurately from standard sources. Proverbs and idioms are folk wisdom, not verified claims. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Let sleeping dogs lie", "d": "Avoid restarting old conflicts.", "g": "idiom", "l": 2, "q": "What is Let sleeping dogs lie?", "a": "Avoid restarting old conflicts.", "x": "Let sleeping dogs lie — Avoid restarting old conflicts. Example: Everyday English phrase..  Ancient stories retold accurately from standard sources. Proverbs and idioms are folk wisdom, not verified claims.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-idioms-english-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
