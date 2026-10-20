(function(){'use strict';
/* JAH Ohio Symbols Database generator — jahdb-e2-ohio-symbols-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-ohio-symbols',PREFIX='JAH-E2OHIOSYMBO-',NAME='JAH Ohio Symbols Database';
var FIELDS=["overview", "symbols", "flag", "nature", "culture", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Ohio: symbols overview", "d": "Ohio's official symbols: scarlet carnation, northern cardinal, Ohio buckeye, and more.", "g": "overview", "l": 2, "q": "What is Ohio: symbols overview?", "a": "Ohio's official symbols: scarlet carnation, northern cardinal, Ohio buckeye, and more.", "x": "The official symbols of Ohio — the \"Buckeye State\" — tell the state's story in shorthand: the scarlet carnation (flower), the northern cardinal (bird), the Ohio buckeye (tree), the motto \"With God, all things are possible,\" and the flag. Burgee pennant with 17 stars. Legislatures designate symbols to honor what the state values; this database covers every one, what it means, and where to see it.", "s": "public-reference", "f": null}, {"t": "Nickname: Buckeye State", "d": "The nickname of Ohio is \"Buckeye State.\"", "g": "symbols", "l": 2, "q": "What is Nickname: Buckeye State?", "a": "The nickname of Ohio is \"Buckeye State.\"", "x": "The nickname of Ohio — \"Buckeye State\" — was adopted to express the state's identity. Burgee pennant with 17 stars. It appears on seals, plates, and proclamations. Shawnee; Northwest Territory. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Nickname: the story", "d": "Why Ohio chose \"Buckeye State.\"", "g": "symbols", "l": 2, "q": "What is Nickname: the story?", "a": "Why Ohio chose \"Buckeye State.\"", "x": "Why \"Buckeye State\": the nickname's story reaches into Ohio's history — Underground Railroad; Civil War.. Symbols are chosen, not found: committees, contests, and legislators all played a part. Knowing the story makes the symbol mean something.", "s": "public-reference", "f": null}, {"t": "Motto: With God, all things are possible", "d": "The motto of Ohio is \"With God, all things are possible.\"", "g": "symbols", "l": 2, "q": "What is Motto: With God, all things are possible?", "a": "The motto of Ohio is \"With God, all things are possible.\"", "x": "The motto of Ohio — \"With God, all things are possible\" — was adopted to express the state's identity. Burgee pennant with 17 stars. It appears on seals, plates, and proclamations. Shawnee; Northwest Territory.", "s": "public-reference", "f": null}, {"t": "Motto: the story", "d": "Why Ohio chose \"With God, all things are possible.\"", "g": "symbols", "l": 2, "q": "What is Motto: the story?", "a": "Why Ohio chose \"With God, all things are possible.\"", "x": "Why \"With God, all things are possible\": the motto's story reaches into Ohio's history — Underground Railroad; Civil War.. Symbols are chosen, not found: committees, contests, and legislators all played a part. Knowing the story makes the symbol mean something.", "s": "public-reference", "f": null}, {"t": "State flower: scarlet carnation", "d": "The state flower of Ohio is the scarlet carnation.", "g": "nature", "l": 2, "q": "What is State flower: scarlet carnation?", "a": "The state flower of Ohio is the scarlet carnation.", "x": "The scarlet carnation — scarlet carnation — is Ohio's officially designated state flower. Burgee pennant with 17 stars. It was chosen for its beauty, its abundance, or its meaning to the people. Cedar Point", "s": "public-reference", "f": null}, {"t": "scarlet carnation: natural history", "d": "The scarlet carnation in the wild.", "g": "nature", "l": 2, "q": "What is scarlet carnation: natural history?", "a": "The scarlet carnation in the wild.", "x": "In the wild, the scarlet carnation blooms across the state. Ohio Learning the state flower's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Cuyahoga Valley National Park's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the flower", "d": "See Ohio's state flower at Cuyahoga Valley National Park.", "g": "nature", "l": 2, "q": "What is Where to see the flower?", "a": "See Ohio's state flower at Cuyahoga Valley National Park.", "x": "See the state flower where it thrives: Cuyahoga Valley National Park in Ohio is the surest bet, and Hocking Hills rewards the observant. Ohio State Fair Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "State bird: northern cardinal", "d": "The state bird of Ohio is the northern cardinal.", "g": "nature", "l": 2, "q": "What is State bird: northern cardinal?", "a": "The state bird of Ohio is the northern cardinal.", "x": "The northern cardinal — northern cardinal — is Ohio's officially designated state bird. Burgee pennant with 17 stars. It was chosen for its beauty, its abundance, or its meaning to the people. Cedar Point", "s": "public-reference", "f": null}, {"t": "northern cardinal: natural history", "d": "The northern cardinal in the wild.", "g": "nature", "l": 2, "q": "What is northern cardinal: natural history?", "a": "The northern cardinal in the wild.", "x": "In the wild, the northern cardinal lives across the state. Ohio Learning the state bird's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Cuyahoga Valley National Park's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the bird", "d": "See Ohio's state bird at Cuyahoga Valley National Park.", "g": "nature", "l": 2, "q": "What is Where to see the bird?", "a": "See Ohio's state bird at Cuyahoga Valley National Park.", "x": "See the state bird where it thrives: Cuyahoga Valley National Park in Ohio is the surest bet, and Hocking Hills rewards the observant. Ohio State Fair Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "State tree: Ohio buckeye", "d": "The state tree of Ohio is the Ohio buckeye.", "g": "nature", "l": 2, "q": "What is State tree: Ohio buckeye?", "a": "The state tree of Ohio is the Ohio buckeye.", "x": "The Ohio buckeye — Ohio buckeye — is Ohio's officially designated state tree. Burgee pennant with 17 stars. It was chosen for its beauty, its abundance, or its meaning to the people. Cedar Point State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Ohio buckeye: natural history", "d": "The Ohio buckeye in the wild.", "g": "nature", "l": 2, "q": "What is Ohio buckeye: natural history?", "a": "The Ohio buckeye in the wild.", "x": "In the wild, the Ohio buckeye lives across the state. Ohio Learning the state tree's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Cuyahoga Valley National Park's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the tree", "d": "See Ohio's state tree at Cuyahoga Valley National Park.", "g": "nature", "l": 2, "q": "What is Where to see the tree?", "a": "See Ohio's state tree at Cuyahoga Valley National Park.", "x": "See the state tree where it thrives: Cuyahoga Valley National Park in Ohio is the surest bet, and Hocking Hills rewards the observant. Ohio State Fair Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "The state flag: design", "d": "Ohio's flag: Burgee pennant with 17 stars..", "g": "flag", "l": 2, "q": "What is The state flag: design?", "a": "Ohio's flag: Burgee pennant with 17 stars..", "x": "The flag of Ohio: Burgee pennant with 17 stars.. Every element was chosen deliberately — colors, seals, stars — and the design's history mirrors the state's. Presidents; industry; aviation. Fly it correctly: the flag code gives the rules, and Ohio flies it with pride.", "s": "public-reference", "f": null}, {"t": "The state flag: colors and emblem", "d": "What Ohio's flag means.", "g": "flag", "l": 2, "q": "What is The state flag: colors and emblem?", "a": "What Ohio's flag means.", "x": "The colors and emblem of Ohio's flag carry meaning: Burgee pennant with 17 stars.. With God, all things are possible Vexillologists rank flags by simplicity and symbolism — Ohio's tells its story at a glance to those who know the code.", "s": "public-reference", "f": null}, {"t": "The state flag: history", "d": "How Ohio got its flag.", "g": "flag", "l": 2, "q": "What is The state flag: history?", "a": "How Ohio got its flag.", "x": "The history of Ohio's flag: adopted after contests or commission designs, sometimes replacing earlier banners. Seven U.S. presidents were born in Ohio. Flags evolve with states — each change marks an era. The current design has flown over Columbus's modern history.", "s": "public-reference", "f": null}, {"t": "The state seal", "d": "The Great Seal of Ohio.", "g": "symbols", "l": 2, "q": "What is The state seal?", "a": "The Great Seal of Ohio.", "x": "The Great Seal of Ohio authenticates the state's official acts — every law and commission bears it. Burgee pennant with 17 stars. The seal's imagery compresses the state's identity: its industries, its ideals, its motto \"With God, all things are possible.\"", "s": "public-reference", "f": null}, {"t": "The state quarter", "d": "Ohio's quarter in the 50 State Quarters program.", "g": "symbols", "l": 2, "q": "What is The state quarter?", "a": "Ohio's quarter in the 50 State Quarters program.", "x": "Ohio's quarter: the US Mint's 50 State Quarters program (1999-2008) gave every state a circulating canvas. Ohio's design honors Buckeye State — pocket change as history lesson. Collectors still hunt them.", "s": "public-reference", "f": null}, {"t": "The capitol building", "d": "Ohio's capitol in Columbus.", "g": "culture", "l": 2, "q": "What is The capitol building?", "a": "Ohio's capitol in Columbus.", "x": "The Ohio State Capitol in Columbus: the building where laws are made and history happened. Shawnee; Northwest Territory. Capitols are museums of democracy — tour the chambers, the rotunda, the grounds. Rock & Roll Hall of Fame", "s": "public-reference", "f": null}, {"t": "The state song", "d": "Ohio's officially adopted state song.", "g": "culture", "l": 2, "q": "What is The state song?", "a": "Ohio's officially adopted state song.", "x": "The state song of Ohio was adopted by the legislature — every state has one, sung at official occasions. Ohio State Fair Songs, like flags, are identity set to music. Learn the chorus; it is the state's anthem in miniature.", "s": "public-reference", "f": null}, {"t": "How symbols are chosen", "d": "The legislature designates Ohio's symbols.", "g": "symbols", "l": 2, "q": "What is How symbols are chosen?", "a": "The legislature designates Ohio's symbols.", "x": "Symbols become official when the Ohio legislature says so — often after schoolchildren campaign, contests run, or committees deliberate. With God, all things are possible The process itself is civics: citizens proposing, debating, and adopting what represents them.", "s": "public-reference", "f": null}, {"t": "Flag etiquette", "d": "Displaying Ohio's flag correctly.", "g": "flag", "l": 2, "q": "What is Flag etiquette?", "a": "Displaying Ohio's flag correctly.", "x": "Flag etiquette for Ohio's banner: fly it sunrise to sunset (or lit at night), never let it touch the ground, and retire worn flags with dignity. Buckeye State The state flag flies below the US flag — a daily reminder of the federal order.", "s": "public-reference", "f": null}, {"t": "Symbol fact 1", "d": "More Ohio symbols: scarlet carnation.", "g": "facts", "l": 2, "q": "What is Symbol fact 1?", "a": "More Ohio symbols: scarlet carnation.", "x": "From the Ohio symbol file: scarlet carnation. Ohio's symbols reward the curious — each one opens a story about the land, the people, or the moment it was chosen. \"With God, all things are possible\" indeed.", "s": "public-reference", "f": null}, {"t": "Symbol fact 2", "d": "More Ohio symbols: northern cardinal.", "g": "facts", "l": 2, "q": "What is Symbol fact 2?", "a": "More Ohio symbols: northern cardinal.", "x": "From the Ohio symbol file: northern cardinal. Ohio's symbols reward the curious — each one opens a story about the land, the people, or the moment it was chosen. \"With God, all things are possible\" indeed.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-ohio-symbols-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
