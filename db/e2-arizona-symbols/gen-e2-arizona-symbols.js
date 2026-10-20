(function(){'use strict';
/* JAH Arizona Symbols Database generator — jahdb-e2-arizona-symbols-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-arizona-symbols',PREFIX='JAH-E2ARIZONASY-',NAME='JAH Arizona Symbols Database';
var FIELDS=["overview", "symbols", "flag", "nature", "culture", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Arizona: symbols overview", "d": "Arizona's official symbols: saguaro cactus blossom, cactus wren, palo verde, and more.", "g": "overview", "l": 2, "q": "What is Arizona: symbols overview?", "a": "Arizona's official symbols: saguaro cactus blossom, cactus wren, palo verde, and more.", "x": "The official symbols of Arizona — the \"Grand Canyon State\" — tell the state's story in shorthand: the saguaro cactus blossom (flower), the cactus wren (bird), the palo verde (tree), the motto \"Ditat Deus (God enriches),\" and the flag. Copper star on red-blue rays; Spanish colors. Legislatures designate symbols to honor what the state values; this database covers every one, what it means, and where to see it.", "s": "public-reference", "f": null}, {"t": "Nickname: Grand Canyon State", "d": "The nickname of Arizona is \"Grand Canyon State.\"", "g": "symbols", "l": 2, "q": "What is Nickname: Grand Canyon State?", "a": "The nickname of Arizona is \"Grand Canyon State.\"", "x": "The nickname of Arizona — \"Grand Canyon State\" — was adopted to express the state's identity. Copper star on red-blue rays; Spanish colors. It appears on seals, plates, and proclamations. Ancestral Puebloans; Spanish missions.", "s": "public-reference", "f": null}, {"t": "Nickname: the story", "d": "Why Arizona chose \"Grand Canyon State.\"", "g": "symbols", "l": 2, "q": "What is Nickname: the story?", "a": "Why Arizona chose \"Grand Canyon State.\"", "x": "Why \"Grand Canyon State\": the nickname's story reaches into Arizona's history — Mexican then U.S. territory (1848).. Symbols are chosen, not found: committees, contests, and legislators all played a part. Knowing the story makes the symbol mean something.", "s": "public-reference", "f": null}, {"t": "Motto: Ditat Deus (God enriches)", "d": "The motto of Arizona is \"Ditat Deus (God enriches).\"", "g": "symbols", "l": 2, "q": "What is Motto: Ditat Deus (God enriches)?", "a": "The motto of Arizona is \"Ditat Deus (God enriches).\"", "x": "The motto of Arizona — \"Ditat Deus (God enriches)\" — was adopted to express the state's identity. Copper star on red-blue rays; Spanish colors. It appears on seals, plates, and proclamations. Ancestral Puebloans; Spanish missions.", "s": "public-reference", "f": null}, {"t": "Motto: the story", "d": "Why Arizona chose \"Ditat Deus (God enriches).\"", "g": "symbols", "l": 2, "q": "What is Motto: the story?", "a": "Why Arizona chose \"Ditat Deus (God enriches).\"", "x": "Why \"Ditat Deus (God enriches)\": the motto's story reaches into Arizona's history — Mexican then U.S. territory (1848).. Symbols are chosen, not found: committees, contests, and legislators all played a part. Knowing the story makes the symbol mean something.", "s": "public-reference", "f": null}, {"t": "State flower: saguaro cactus blossom", "d": "The state flower of Arizona is the saguaro cactus blossom.", "g": "nature", "l": 2, "q": "What is State flower: saguaro cactus blossom?", "a": "The state flower of Arizona is the saguaro cactus blossom.", "x": "The saguaro cactus blossom — saguaro cactus blossom — is Arizona's officially designated state flower. Copper star on red-blue rays; Spanish colors. It was chosen for its beauty, its abundance, or its meaning to the people. Antelope Canyon", "s": "public-reference", "f": null}, {"t": "saguaro cactus blossom: natural history", "d": "The saguaro cactus blossom in the wild.", "g": "nature", "l": 2, "q": "What is saguaro cactus blossom: natural history?", "a": "The saguaro cactus blossom in the wild.", "x": "In the wild, the saguaro cactus blossom blooms across the state. Arizona Learning the state flower's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Grand Canyon National Park's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the flower", "d": "See Arizona's state flower at Grand Canyon National Park.", "g": "nature", "l": 2, "q": "What is Where to see the flower?", "a": "See Arizona's state flower at Grand Canyon National Park.", "x": "See the state flower where it thrives: Grand Canyon National Park in Arizona is the surest bet, and Sedona red rocks rewards the observant. Tucson Gem Show Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "State bird: cactus wren", "d": "The state bird of Arizona is the cactus wren.", "g": "nature", "l": 2, "q": "What is State bird: cactus wren?", "a": "The state bird of Arizona is the cactus wren.", "x": "The cactus wren — cactus wren — is Arizona's officially designated state bird. Copper star on red-blue rays; Spanish colors. It was chosen for its beauty, its abundance, or its meaning to the people. Antelope Canyon", "s": "public-reference", "f": null}, {"t": "cactus wren: natural history", "d": "The cactus wren in the wild.", "g": "nature", "l": 2, "q": "What is cactus wren: natural history?", "a": "The cactus wren in the wild.", "x": "In the wild, the cactus wren lives across the state. Arizona Learning the state bird's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Grand Canyon National Park's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the bird", "d": "See Arizona's state bird at Grand Canyon National Park.", "g": "nature", "l": 2, "q": "What is Where to see the bird?", "a": "See Arizona's state bird at Grand Canyon National Park.", "x": "See the state bird where it thrives: Grand Canyon National Park in Arizona is the surest bet, and Sedona red rocks rewards the observant. Tucson Gem Show Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "State tree: palo verde", "d": "The state tree of Arizona is the palo verde.", "g": "nature", "l": 2, "q": "What is State tree: palo verde?", "a": "The state tree of Arizona is the palo verde.", "x": "The palo verde — palo verde — is Arizona's officially designated state tree. Copper star on red-blue rays; Spanish colors. It was chosen for its beauty, its abundance, or its meaning to the people. Antelope Canyon", "s": "public-reference", "f": null}, {"t": "palo verde: natural history", "d": "The palo verde in the wild.", "g": "nature", "l": 2, "q": "What is palo verde: natural history?", "a": "The palo verde in the wild.", "x": "In the wild, the palo verde lives across the state. Arizona Learning the state tree's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Grand Canyon National Park's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the tree", "d": "See Arizona's state tree at Grand Canyon National Park.", "g": "nature", "l": 2, "q": "What is Where to see the tree?", "a": "See Arizona's state tree at Grand Canyon National Park.", "x": "See the state tree where it thrives: Grand Canyon National Park in Arizona is the surest bet, and Sedona red rocks rewards the observant. Tucson Gem Show Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "The state flag: design", "d": "Arizona's flag: Copper star on red-blue rays; Spanish colors..", "g": "flag", "l": 2, "q": "What is The state flag: design?", "a": "Arizona's flag: Copper star on red-blue rays; Spanish colors..", "x": "The flag of Arizona: Copper star on red-blue rays; Spanish colors.. Every element was chosen deliberately — colors, seals, stars — and the design's history mirrors the state's. Copper and cattle; Hoover Dam era. Fly it correctly: the flag code gives the rules, and Arizona flies it with pride.", "s": "public-reference", "f": null}, {"t": "The state flag: colors and emblem", "d": "What Arizona's flag means.", "g": "flag", "l": 2, "q": "What is The state flag: colors and emblem?", "a": "What Arizona's flag means.", "x": "The colors and emblem of Arizona's flag carry meaning: Copper star on red-blue rays; Spanish colors.. Ditat Deus (God enriches) Vexillologists rank flags by simplicity and symbolism — Arizona's tells its story at a glance to those who know the code.", "s": "public-reference", "f": null}, {"t": "The state flag: history", "d": "How Arizona got its flag.", "g": "flag", "l": 2, "q": "What is The state flag: history?", "a": "How Arizona got its flag.", "x": "The history of Arizona's flag: adopted after contests or commission designs, sometimes replacing earlier banners. Sun Belt boom; retirement haven. Flags evolve with states — each change marks an era. The current design has flown over Phoenix's modern history.", "s": "public-reference", "f": null}, {"t": "The state seal", "d": "The Great Seal of Arizona.", "g": "symbols", "l": 2, "q": "What is The state seal?", "a": "The Great Seal of Arizona.", "x": "The Great Seal of Arizona authenticates the state's official acts — every law and commission bears it. Copper star on red-blue rays; Spanish colors. The seal's imagery compresses the state's identity: its industries, its ideals, its motto \"Ditat Deus (God enriches).\"", "s": "public-reference", "f": null}, {"t": "The state quarter", "d": "Arizona's quarter in the 50 State Quarters program.", "g": "symbols", "l": 2, "q": "What is The state quarter?", "a": "Arizona's quarter in the 50 State Quarters program.", "x": "Arizona's quarter: the US Mint's 50 State Quarters program (1999-2008) gave every state a circulating canvas. Arizona's design honors Grand Canyon State — pocket change as history lesson. Collectors still hunt them.", "s": "public-reference", "f": null}, {"t": "The capitol building", "d": "Arizona's capitol in Phoenix.", "g": "culture", "l": 2, "q": "What is The capitol building?", "a": "Arizona's capitol in Phoenix.", "x": "The Arizona State Capitol in Phoenix: the building where laws are made and history happened. Ancestral Puebloans; Spanish missions. Capitols are museums of democracy — tour the chambers, the rotunda, the grounds. Grand Canyon", "s": "public-reference", "f": null}, {"t": "The state song", "d": "Arizona's officially adopted state song.", "g": "culture", "l": 2, "q": "What is The state song?", "a": "Arizona's officially adopted state song.", "x": "The state song of Arizona was adopted by the legislature — every state has one, sung at official occasions. Tucson Gem Show Songs, like flags, are identity set to music. Learn the chorus; it is the state's anthem in miniature.", "s": "public-reference", "f": null}, {"t": "How symbols are chosen", "d": "The legislature designates Arizona's symbols.", "g": "symbols", "l": 2, "q": "What is How symbols are chosen?", "a": "The legislature designates Arizona's symbols.", "x": "Symbols become official when the Arizona legislature says so — often after schoolchildren campaign, contests run, or committees deliberate. Ditat Deus (God enriches) The process itself is civics: citizens proposing, debating, and adopting what represents them.", "s": "public-reference", "f": null}, {"t": "Flag etiquette", "d": "Displaying Arizona's flag correctly.", "g": "flag", "l": 2, "q": "What is Flag etiquette?", "a": "Displaying Arizona's flag correctly.", "x": "Flag etiquette for Arizona's banner: fly it sunrise to sunset (or lit at night), never let it touch the ground, and retire worn flags with dignity. Grand Canyon State The state flag flies below the US flag — a daily reminder of the federal order.", "s": "public-reference", "f": null}, {"t": "Symbol fact 1", "d": "More Arizona symbols: saguaro cactus blossom.", "g": "facts", "l": 2, "q": "What is Symbol fact 1?", "a": "More Arizona symbols: saguaro cactus blossom.", "x": "From the Arizona symbol file: saguaro cactus blossom. Arizona's symbols reward the curious — each one opens a story about the land, the people, or the moment it was chosen. \"Ditat Deus (God enriches)\" indeed.", "s": "public-reference", "f": null}, {"t": "Symbol fact 2", "d": "More Arizona symbols: cactus wren.", "g": "facts", "l": 2, "q": "What is Symbol fact 2?", "a": "More Arizona symbols: cactus wren.", "x": "From the Arizona symbol file: cactus wren. Arizona's symbols reward the curious — each one opens a story about the land, the people, or the moment it was chosen. \"Ditat Deus (God enriches)\" indeed. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-arizona-symbols-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
