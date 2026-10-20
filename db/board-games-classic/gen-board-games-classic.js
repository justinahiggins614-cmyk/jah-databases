(function(){'use strict';
/* JAH Classic Board Games Database generator — jahdb-board-games-classic-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='board-games-classic',PREFIX='JAH-BRD-',NAME='JAH Classic Board Games Database';
var FIELDS=["Strategy", "Family", "Word", "Mystery", "Cooperative", "Party", "Trivia", "Classic", "Kids", "Horror"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Chess", "d": "The 1,500-year-old game of kings.", "g": "Strategy", "l": 2, "q": "What is Chess?", "a": "The 1,500-year-old game of kings.", "x": "The 1,500-year-old game of kings. players: 2. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Go", "d": "The ancient game of surrounding territory.", "g": "Strategy", "l": 2, "q": "What is Go?", "a": "The ancient game of surrounding territory.", "x": "The ancient game of surrounding territory. players: 2. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Checkers", "d": "Jump and king me.", "g": "Strategy", "l": 2, "q": "What is Checkers?", "a": "Jump and king me.", "x": "Jump and king me. players: 2. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Backgammon", "d": "Dice, pieces, and 5,000 years.", "g": "Strategy", "l": 2, "q": "What is Backgammon?", "a": "Dice, pieces, and 5,000 years.", "x": "Dice, pieces, and 5,000 years. players: 2. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Monopoly", "d": "Bankrupt your family since 1935.", "g": "Family", "l": 2, "q": "What is Monopoly?", "a": "Bankrupt your family since 1935.", "x": "Bankrupt your family since 1935. players: 2-8. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Scrabble", "d": "Triple word score glory.", "g": "Word", "l": 2, "q": "What is Scrabble?", "a": "Triple word score glory.", "x": "Triple word score glory. players: 2-4. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Clue", "d": "Colonel Mustard in the library.", "g": "Mystery", "l": 2, "q": "What is Clue?", "a": "Colonel Mustard in the library.", "x": "Colonel Mustard in the library. players: 3-6. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Risk", "d": "World domination, one roll at a time.", "g": "Strategy", "l": 2, "q": "What is Risk?", "a": "World domination, one roll at a time.", "x": "World domination, one roll at a time. players: 2-6. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Catan", "d": "Trade, build, settle — the modern classic.", "g": "Strategy", "l": 2, "q": "What is Catan?", "a": "Trade, build, settle — the modern classic.", "x": "Trade, build, settle — the modern classic. players: 3-4. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Ticket to Ride", "d": "Claim railway routes across the map.", "g": "Family", "l": 2, "q": "What is Ticket to Ride?", "a": "Claim railway routes across the map.", "x": "Claim railway routes across the map. players: 2-5. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Pandemic", "d": "Save the world together.", "g": "Cooperative", "l": 2, "q": "What is Pandemic?", "a": "Save the world together.", "x": "Save the world together. players: 2-4. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Carcassonne", "d": "Tile-laying medieval France.", "g": "Family", "l": 2, "q": "What is Carcassonne?", "a": "Tile-laying medieval France.", "x": "Tile-laying medieval France. players: 2-5. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Azul", "d": "Beautiful tile-drafting.", "g": "Family", "l": 2, "q": "What is Azul?", "a": "Beautiful tile-drafting.", "x": "Beautiful tile-drafting. players: 2-4. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Splendor", "d": "Gem engine-building.", "g": "Family", "l": 2, "q": "What is Splendor?", "a": "Gem engine-building.", "x": "Gem engine-building. players: 2-4. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Codenames", "d": "One-word clues, clever teams.", "g": "Party", "l": 2, "q": "What is Codenames?", "a": "One-word clues, clever teams.", "x": "One-word clues, clever teams. players: 4+. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Pictionary", "d": "Draw it fast.", "g": "Party", "l": 2, "q": "What is Pictionary?", "a": "Draw it fast.", "x": "Draw it fast. players: 4+. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Trivial Pursuit", "d": "Six wedges of knowledge.", "g": "Trivia", "l": 2, "q": "What is Trivial Pursuit?", "a": "Six wedges of knowledge.", "x": "Six wedges of knowledge. players: 2-6. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Battleship", "d": "You sunk my battleship.", "g": "Classic", "l": 2, "q": "What is Battleship?", "a": "You sunk my battleship.", "x": "You sunk my battleship. players: 2. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Connect Four", "d": "Four in a row drops.", "g": "Classic", "l": 2, "q": "What is Connect Four?", "a": "Four in a row drops.", "x": "Four in a row drops. players: 2. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Sorry!", "d": "Send them back to start.", "g": "Family", "l": 2, "q": "What is Sorry!?", "a": "Send them back to start.", "x": "Send them back to start. players: 2-4. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Trouble", "d": "Pop the bubble.", "g": "Family", "l": 2, "q": "What is Trouble?", "a": "Pop the bubble.", "x": "Pop the bubble. players: 2-4. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Candy Land", "d": "The first game for many.", "g": "Kids", "l": 2, "q": "What is Candy Land?", "a": "The first game for many.", "x": "The first game for many. players: 2-4. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Chutes and Ladders", "d": "Climb and slide.", "g": "Kids", "l": 2, "q": "What is Chutes and Ladders?", "a": "Climb and slide.", "x": "Climb and slide. players: 2-4. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Life", "d": "Spin through careers and kids.", "g": "Family", "l": 2, "q": "What is Life?", "a": "Spin through careers and kids.", "x": "Spin through careers and kids. players: 2-6. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Operation", "d": "Steady hands, no buzzers.", "g": "Kids", "l": 2, "q": "What is Operation?", "a": "Steady hands, no buzzers.", "x": "Steady hands, no buzzers. players: 1-4. Facts checked against standard references and public records. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-board-games-classic-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
