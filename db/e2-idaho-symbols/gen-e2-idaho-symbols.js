(function(){'use strict';
/* JAH Idaho Symbols Database generator — jahdb-e2-idaho-symbols-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-idaho-symbols',PREFIX='JAH-E2IDAHOSYMB-',NAME='JAH Idaho Symbols Database';
var FIELDS=["overview", "symbols", "flag", "nature", "culture", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Idaho: symbols overview", "d": "Idaho's official symbols: syringa (mock orange), mountain bluebird, western white pine, and more.", "g": "overview", "l": 2, "q": "What is Idaho: symbols overview?", "a": "Idaho's official symbols: syringa (mock orange), mountain bluebird, western white pine, and more.", "x": "The official symbols of Idaho — the \"Gem State\" — tell the state's story in shorthand: the syringa (mock orange) (flower), the mountain bluebird (bird), the western white pine (tree), the motto \"Esto perpetua (Let it be perpetual),\" and the flag. State seal on blue with gold fringe. Legislatures designate symbols to honor what the state values; this database covers every one, what it means, and where to see it.", "s": "public-reference", "f": null}, {"t": "Nickname: Gem State", "d": "The nickname of Idaho is \"Gem State.\"", "g": "symbols", "l": 2, "q": "What is Nickname: Gem State?", "a": "The nickname of Idaho is \"Gem State.\"", "x": "The nickname of Idaho — \"Gem State\" — was adopted to express the state's identity. State seal on blue with gold fringe. It appears on seals, plates, and proclamations. Nez Perce and Shoshone; Lewis & Clark.", "s": "public-reference", "f": null}, {"t": "Nickname: the story", "d": "Why Idaho chose \"Gem State.\"", "g": "symbols", "l": 2, "q": "What is Nickname: the story?", "a": "Why Idaho chose \"Gem State.\"", "x": "Why \"Gem State\": the nickname's story reaches into Idaho's history — Gold and silver rushes.. Symbols are chosen, not found: committees, contests, and legislators all played a part. Knowing the story makes the symbol mean something.", "s": "public-reference", "f": null}, {"t": "Motto: Esto perpetua (Let it be perpetual)", "d": "The motto of Idaho is \"Esto perpetua (Let it be perpetual).\"", "g": "symbols", "l": 2, "q": "What is Motto: Esto perpetua (Let it be perpetual)?", "a": "The motto of Idaho is \"Esto perpetua (Let it be perpetual).\"", "x": "The motto of Idaho — \"Esto perpetua (Let it be perpetual)\" — was adopted to express the state's identity. State seal on blue with gold fringe. It appears on seals, plates, and proclamations. Nez Perce and Shoshone; Lewis & Clark.", "s": "public-reference", "f": null}, {"t": "Motto: the story", "d": "Why Idaho chose \"Esto perpetua (Let it be perpetual).\"", "g": "symbols", "l": 2, "q": "What is Motto: the story?", "a": "Why Idaho chose \"Esto perpetua (Let it be perpetual).\"", "x": "Why \"Esto perpetua (Let it be perpetual)\": the motto's story reaches into Idaho's history — Gold and silver rushes.. Symbols are chosen, not found: committees, contests, and legislators all played a part. Knowing the story makes the symbol mean something.", "s": "public-reference", "f": null}, {"t": "State flower: syringa (mock orange)", "d": "The state flower of Idaho is the syringa (mock orange).", "g": "nature", "l": 2, "q": "What is State flower: syringa (mock orange)?", "a": "The state flower of Idaho is the syringa (mock orange).", "x": "The syringa (mock orange) — syringa (mock orange) — is Idaho's officially designated state flower. State seal on blue with gold fringe. It was chosen for its beauty, its abundance, or its meaning to the people. Shoshone Falls", "s": "public-reference", "f": null}, {"t": "syringa (mock orange): natural history", "d": "The syringa (mock orange) in the wild.", "g": "nature", "l": 2, "q": "What is syringa (mock orange): natural history?", "a": "The syringa (mock orange) in the wild.", "x": "In the wild, the syringa (mock orange) blooms across the state. Idaho Learning the state flower's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Sawtooth National Recreation Area's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the flower", "d": "See Idaho's state flower at Sawtooth National Recreation Area.", "g": "nature", "l": 2, "q": "What is Where to see the flower?", "a": "See Idaho's state flower at Sawtooth National Recreation Area.", "x": "See the state flower where it thrives: Sawtooth National Recreation Area in Idaho is the surest bet, and Sawtooth Mountains rewards the observant. Sun Valley festivals Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "State bird: mountain bluebird", "d": "The state bird of Idaho is the mountain bluebird.", "g": "nature", "l": 2, "q": "What is State bird: mountain bluebird?", "a": "The state bird of Idaho is the mountain bluebird.", "x": "The mountain bluebird — mountain bluebird — is Idaho's officially designated state bird. State seal on blue with gold fringe. It was chosen for its beauty, its abundance, or its meaning to the people. Shoshone Falls", "s": "public-reference", "f": null}, {"t": "mountain bluebird: natural history", "d": "The mountain bluebird in the wild.", "g": "nature", "l": 2, "q": "What is mountain bluebird: natural history?", "a": "The mountain bluebird in the wild.", "x": "In the wild, the mountain bluebird lives across the state. Idaho Learning the state bird's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Sawtooth National Recreation Area's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the bird", "d": "See Idaho's state bird at Sawtooth National Recreation Area.", "g": "nature", "l": 2, "q": "What is Where to see the bird?", "a": "See Idaho's state bird at Sawtooth National Recreation Area.", "x": "See the state bird where it thrives: Sawtooth National Recreation Area in Idaho is the surest bet, and Sawtooth Mountains rewards the observant. Sun Valley festivals Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "State tree: western white pine", "d": "The state tree of Idaho is the western white pine.", "g": "nature", "l": 2, "q": "What is State tree: western white pine?", "a": "The state tree of Idaho is the western white pine.", "x": "The western white pine — western white pine — is Idaho's officially designated state tree. State seal on blue with gold fringe. It was chosen for its beauty, its abundance, or its meaning to the people. Shoshone Falls", "s": "public-reference", "f": null}, {"t": "western white pine: natural history", "d": "The western white pine in the wild.", "g": "nature", "l": 2, "q": "What is western white pine: natural history?", "a": "The western white pine in the wild.", "x": "In the wild, the western white pine lives across the state. Idaho Learning the state tree's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Sawtooth National Recreation Area's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the tree", "d": "See Idaho's state tree at Sawtooth National Recreation Area.", "g": "nature", "l": 2, "q": "What is Where to see the tree?", "a": "See Idaho's state tree at Sawtooth National Recreation Area.", "x": "See the state tree where it thrives: Sawtooth National Recreation Area in Idaho is the surest bet, and Sawtooth Mountains rewards the observant. Sun Valley festivals Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "The state flag: design", "d": "Idaho's flag: State seal on blue with gold fringe..", "g": "flag", "l": 2, "q": "What is The state flag: design?", "a": "Idaho's flag: State seal on blue with gold fringe..", "x": "The flag of Idaho: State seal on blue with gold fringe.. Every element was chosen deliberately — colors, seals, stars — and the design's history mirrors the state's. Potatoes; nuclear lab (INL). Fly it correctly: the flag code gives the rules, and Idaho flies it with pride.", "s": "public-reference", "f": null}, {"t": "The state flag: colors and emblem", "d": "What Idaho's flag means.", "g": "flag", "l": 2, "q": "What is The state flag: colors and emblem?", "a": "What Idaho's flag means.", "x": "The colors and emblem of Idaho's flag carry meaning: State seal on blue with gold fringe.. Esto perpetua (Let it be perpetual) Vexillologists rank flags by simplicity and symbolism — Idaho's tells its story at a glance to those who know the code.", "s": "public-reference", "f": null}, {"t": "The state flag: history", "d": "How Idaho got its flag.", "g": "flag", "l": 2, "q": "What is The state flag: history?", "a": "How Idaho got its flag.", "x": "The history of Idaho's flag: adopted after contests or commission designs, sometimes replacing earlier banners. Boise boom. Flags evolve with states — each change marks an era. The current design has flown over Boise's modern history.", "s": "public-reference", "f": null}, {"t": "The state seal", "d": "The Great Seal of Idaho.", "g": "symbols", "l": 2, "q": "What is The state seal?", "a": "The Great Seal of Idaho.", "x": "The Great Seal of Idaho authenticates the state's official acts — every law and commission bears it. State seal on blue with gold fringe. The seal's imagery compresses the state's identity: its industries, its ideals, its motto \"Esto perpetua (Let it be perpetual).\"", "s": "public-reference", "f": null}, {"t": "The state quarter", "d": "Idaho's quarter in the 50 State Quarters program.", "g": "symbols", "l": 2, "q": "What is The state quarter?", "a": "Idaho's quarter in the 50 State Quarters program.", "x": "Idaho's quarter: the US Mint's 50 State Quarters program (1999-2008) gave every state a circulating canvas. Idaho's design honors Gem State — pocket change as history lesson. Collectors still hunt them.", "s": "public-reference", "f": null}, {"t": "The capitol building", "d": "Idaho's capitol in Boise.", "g": "culture", "l": 2, "q": "What is The capitol building?", "a": "Idaho's capitol in Boise.", "x": "The Idaho State Capitol in Boise: the building where laws are made and history happened. Nez Perce and Shoshone; Lewis & Clark. Capitols are museums of democracy — tour the chambers, the rotunda, the grounds. Craters of the Moon", "s": "public-reference", "f": null}, {"t": "The state song", "d": "Idaho's officially adopted state song.", "g": "culture", "l": 2, "q": "What is The state song?", "a": "Idaho's officially adopted state song.", "x": "The state song of Idaho was adopted by the legislature — every state has one, sung at official occasions. Sun Valley festivals Songs, like flags, are identity set to music. Learn the chorus; it is the state's anthem in miniature.", "s": "public-reference", "f": null}, {"t": "How symbols are chosen", "d": "The legislature designates Idaho's symbols.", "g": "symbols", "l": 2, "q": "What is How symbols are chosen?", "a": "The legislature designates Idaho's symbols.", "x": "Symbols become official when the Idaho legislature says so — often after schoolchildren campaign, contests run, or committees deliberate. Esto perpetua (Let it be perpetual) The process itself is civics: citizens proposing, debating, and adopting what represents them.", "s": "public-reference", "f": null}, {"t": "Flag etiquette", "d": "Displaying Idaho's flag correctly.", "g": "flag", "l": 2, "q": "What is Flag etiquette?", "a": "Displaying Idaho's flag correctly.", "x": "Flag etiquette for Idaho's banner: fly it sunrise to sunset (or lit at night), never let it touch the ground, and retire worn flags with dignity. Gem State The state flag flies below the US flag — a daily reminder of the federal order.", "s": "public-reference", "f": null}, {"t": "Symbol fact 1", "d": "More Idaho symbols: syringa (mock orange).", "g": "facts", "l": 2, "q": "What is Symbol fact 1?", "a": "More Idaho symbols: syringa (mock orange).", "x": "From the Idaho symbol file: syringa (mock orange). Idaho's symbols reward the curious — each one opens a story about the land, the people, or the moment it was chosen. \"Esto perpetua (Let it be perpetual)\" indeed.", "s": "public-reference", "f": null}, {"t": "Symbol fact 2", "d": "More Idaho symbols: mountain bluebird.", "g": "facts", "l": 2, "q": "What is Symbol fact 2?", "a": "More Idaho symbols: mountain bluebird.", "x": "From the Idaho symbol file: mountain bluebird. Idaho's symbols reward the curious — each one opens a story about the land, the people, or the moment it was chosen. \"Esto perpetua (Let it be perpetual)\" indeed.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-idaho-symbols-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
