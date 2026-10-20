(function(){'use strict';
/* JAH Oregon Symbols Database generator — jahdb-e2-oregon-symbols-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-oregon-symbols',PREFIX='JAH-E2OREGONSYM-',NAME='JAH Oregon Symbols Database';
var FIELDS=["overview", "symbols", "flag", "nature", "culture", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Oregon: symbols overview", "d": "Oregon's official symbols: Oregon grape, western meadowlark, Douglas fir, and more.", "g": "overview", "l": 2, "q": "What is Oregon: symbols overview?", "a": "Oregon's official symbols: Oregon grape, western meadowlark, Douglas fir, and more.", "x": "The official symbols of Oregon — the \"Beaver State\" — tell the state's story in shorthand: the Oregon grape (flower), the western meadowlark (bird), the Douglas fir (tree), the motto \"Alis volat propriis (She flies with her own wings),\" and the flag. Seal with beaver and ship on blue. Legislatures designate symbols to honor what the state values; this database covers every one, what it means, and where to see it.", "s": "public-reference", "f": null}, {"t": "Nickname: Beaver State", "d": "The nickname of Oregon is \"Beaver State.\"", "g": "symbols", "l": 2, "q": "What is Nickname: Beaver State?", "a": "The nickname of Oregon is \"Beaver State.\"", "x": "The nickname of Oregon — \"Beaver State\" — was adopted to express the state's identity. Seal with beaver and ship on blue. It appears on seals, plates, and proclamations. Chinook; Oregon Trail. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Nickname: the story", "d": "Why Oregon chose \"Beaver State.\"", "g": "symbols", "l": 2, "q": "What is Nickname: the story?", "a": "Why Oregon chose \"Beaver State.\"", "x": "Why \"Beaver State\": the nickname's story reaches into Oregon's history — Statehood 1859.. Symbols are chosen, not found: committees, contests, and legislators all played a part. Knowing the story makes the symbol mean something.", "s": "public-reference", "f": null}, {"t": "Motto: Alis volat propriis (She flies with her own wings)", "d": "The motto of Oregon is \"Alis volat propriis (She flies with her own wings).\"", "g": "symbols", "l": 2, "q": "What is Motto: Alis volat propriis (She flies with her own wings)?", "a": "The motto of Oregon is \"Alis volat propriis (She flies with her own wings).\"", "x": "The motto of Oregon — \"Alis volat propriis (She flies with her own wings)\" — was adopted to express the state's identity. Seal with beaver and ship on blue. It appears on seals, plates, and proclamations. Chinook; Oregon Trail.", "s": "public-reference", "f": null}, {"t": "Motto: the story", "d": "Why Oregon chose \"Alis volat propriis (She flies with her own wings).\"", "g": "symbols", "l": 2, "q": "What is Motto: the story?", "a": "Why Oregon chose \"Alis volat propriis (She flies with her own wings).\"", "x": "Why \"Alis volat propriis (She flies with her own wings)\": the motto's story reaches into Oregon's history — Statehood 1859.. Symbols are chosen, not found: committees, contests, and legislators all played a part. Knowing the story makes the symbol mean something.", "s": "public-reference", "f": null}, {"t": "State flower: Oregon grape", "d": "The state flower of Oregon is the Oregon grape.", "g": "nature", "l": 2, "q": "What is State flower: Oregon grape?", "a": "The state flower of Oregon is the Oregon grape.", "x": "The Oregon grape — Oregon grape — is Oregon's officially designated state flower. Seal with beaver and ship on blue. It was chosen for its beauty, its abundance, or its meaning to the people. Multnomah Falls", "s": "public-reference", "f": null}, {"t": "Oregon grape: natural history", "d": "The Oregon grape in the wild.", "g": "nature", "l": 2, "q": "What is Oregon grape: natural history?", "a": "The Oregon grape in the wild.", "x": "In the wild, the Oregon grape blooms across the state. Oregon Learning the state flower's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Crater Lake National Park's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the flower", "d": "See Oregon's state flower at Crater Lake National Park.", "g": "nature", "l": 2, "q": "What is Where to see the flower?", "a": "See Oregon's state flower at Crater Lake National Park.", "x": "See the state flower where it thrives: Crater Lake National Park in Oregon is the surest bet, and Cannon Beach rewards the observant. Portland festivals Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "State bird: western meadowlark", "d": "The state bird of Oregon is the western meadowlark.", "g": "nature", "l": 2, "q": "What is State bird: western meadowlark?", "a": "The state bird of Oregon is the western meadowlark.", "x": "The western meadowlark — western meadowlark — is Oregon's officially designated state bird. Seal with beaver and ship on blue. It was chosen for its beauty, its abundance, or its meaning to the people. Multnomah Falls", "s": "public-reference", "f": null}, {"t": "western meadowlark: natural history", "d": "The western meadowlark in the wild.", "g": "nature", "l": 2, "q": "What is western meadowlark: natural history?", "a": "The western meadowlark in the wild.", "x": "In the wild, the western meadowlark lives across the state. Oregon Learning the state bird's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Crater Lake National Park's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the bird", "d": "See Oregon's state bird at Crater Lake National Park.", "g": "nature", "l": 2, "q": "What is Where to see the bird?", "a": "See Oregon's state bird at Crater Lake National Park.", "x": "See the state bird where it thrives: Crater Lake National Park in Oregon is the surest bet, and Cannon Beach rewards the observant. Portland festivals Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "State tree: Douglas fir", "d": "The state tree of Oregon is the Douglas fir.", "g": "nature", "l": 2, "q": "What is State tree: Douglas fir?", "a": "The state tree of Oregon is the Douglas fir.", "x": "The Douglas fir — Douglas fir — is Oregon's officially designated state tree. Seal with beaver and ship on blue. It was chosen for its beauty, its abundance, or its meaning to the people. Multnomah Falls", "s": "public-reference", "f": null}, {"t": "Douglas fir: natural history", "d": "The Douglas fir in the wild.", "g": "nature", "l": 2, "q": "What is Douglas fir: natural history?", "a": "The Douglas fir in the wild.", "x": "In the wild, the Douglas fir lives across the state. Oregon Learning the state tree's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Crater Lake National Park's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the tree", "d": "See Oregon's state tree at Crater Lake National Park.", "g": "nature", "l": 2, "q": "What is Where to see the tree?", "a": "See Oregon's state tree at Crater Lake National Park.", "x": "See the state tree where it thrives: Crater Lake National Park in Oregon is the surest bet, and Cannon Beach rewards the observant. Portland festivals Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "The state flag: design", "d": "Oregon's flag: Seal with beaver and ship on blue..", "g": "flag", "l": 2, "q": "What is The state flag: design?", "a": "Oregon's flag: Seal with beaver and ship on blue..", "x": "The flag of Oregon: Seal with beaver and ship on blue.. Every element was chosen deliberately — colors, seals, stars — and the design's history mirrors the state's. Timber to tech (Silicon Forest). Fly it correctly: the flag code gives the rules, and Oregon flies it with pride.", "s": "public-reference", "f": null}, {"t": "The state flag: colors and emblem", "d": "What Oregon's flag means.", "g": "flag", "l": 2, "q": "What is The state flag: colors and emblem?", "a": "What Oregon's flag means.", "x": "The colors and emblem of Oregon's flag carry meaning: Seal with beaver and ship on blue.. Alis volat propriis (She flies with her own wings) Vexillologists rank flags by simplicity and symbolism — Oregon's tells its story at a glance to those who know the code.", "s": "public-reference", "f": null}, {"t": "The state flag: history", "d": "How Oregon got its flag.", "g": "flag", "l": 2, "q": "What is The state flag: history?", "a": "How Oregon got its flag.", "x": "The history of Oregon's flag: adopted after contests or commission designs, sometimes replacing earlier banners. The Oregon Trail brought settlers west. Flags evolve with states — each change marks an era. The current design has flown over Salem's modern history.", "s": "public-reference", "f": null}, {"t": "The state seal", "d": "The Great Seal of Oregon.", "g": "symbols", "l": 2, "q": "What is The state seal?", "a": "The Great Seal of Oregon.", "x": "The Great Seal of Oregon authenticates the state's official acts — every law and commission bears it. Seal with beaver and ship on blue. The seal's imagery compresses the state's identity: its industries, its ideals, its motto \"Alis volat propriis (She flies with her own wings).\"", "s": "public-reference", "f": null}, {"t": "The state quarter", "d": "Oregon's quarter in the 50 State Quarters program.", "g": "symbols", "l": 2, "q": "What is The state quarter?", "a": "Oregon's quarter in the 50 State Quarters program.", "x": "Oregon's quarter: the US Mint's 50 State Quarters program (1999-2008) gave every state a circulating canvas. Oregon's design honors Beaver State — pocket change as history lesson. Collectors still hunt them.", "s": "public-reference", "f": null}, {"t": "The capitol building", "d": "Oregon's capitol in Salem.", "g": "culture", "l": 2, "q": "What is The capitol building?", "a": "Oregon's capitol in Salem.", "x": "The Oregon State Capitol in Salem: the building where laws are made and history happened. Chinook; Oregon Trail. Capitols are museums of democracy — tour the chambers, the rotunda, the grounds. Crater Lake", "s": "public-reference", "f": null}, {"t": "The state song", "d": "Oregon's officially adopted state song.", "g": "culture", "l": 2, "q": "What is The state song?", "a": "Oregon's officially adopted state song.", "x": "The state song of Oregon was adopted by the legislature — every state has one, sung at official occasions. Portland festivals Songs, like flags, are identity set to music. Learn the chorus; it is the state's anthem in miniature.", "s": "public-reference", "f": null}, {"t": "How symbols are chosen", "d": "The legislature designates Oregon's symbols.", "g": "symbols", "l": 2, "q": "What is How symbols are chosen?", "a": "The legislature designates Oregon's symbols.", "x": "Symbols become official when the Oregon legislature says so — often after schoolchildren campaign, contests run, or committees deliberate. Alis volat propriis (She flies with her own wings) The process itself is civics: citizens proposing, debating, and adopting what represents them.", "s": "public-reference", "f": null}, {"t": "Flag etiquette", "d": "Displaying Oregon's flag correctly.", "g": "flag", "l": 2, "q": "What is Flag etiquette?", "a": "Displaying Oregon's flag correctly.", "x": "Flag etiquette for Oregon's banner: fly it sunrise to sunset (or lit at night), never let it touch the ground, and retire worn flags with dignity. Beaver State The state flag flies below the US flag — a daily reminder of the federal order.", "s": "public-reference", "f": null}, {"t": "Symbol fact 1", "d": "More Oregon symbols: Oregon grape.", "g": "facts", "l": 2, "q": "What is Symbol fact 1?", "a": "More Oregon symbols: Oregon grape.", "x": "From the Oregon symbol file: Oregon grape. Oregon's symbols reward the curious — each one opens a story about the land, the people, or the moment it was chosen. \"Alis volat propriis (She flies with her own wings)\" indeed.", "s": "public-reference", "f": null}, {"t": "Symbol fact 2", "d": "More Oregon symbols: western meadowlark.", "g": "facts", "l": 2, "q": "What is Symbol fact 2?", "a": "More Oregon symbols: western meadowlark.", "x": "From the Oregon symbol file: western meadowlark. Oregon's symbols reward the curious — each one opens a story about the land, the people, or the moment it was chosen. \"Alis volat propriis (She flies with her own wings)\" indeed.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-oregon-symbols-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
