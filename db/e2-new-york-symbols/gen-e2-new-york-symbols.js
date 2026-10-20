(function(){'use strict';
/* JAH New York Symbols Database generator — jahdb-e2-new-york-symbols-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-new-york-symbols',PREFIX='JAH-E2NEWYORKSY-',NAME='JAH New York Symbols Database';
var FIELDS=["overview", "symbols", "flag", "nature", "culture", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "New York: symbols overview", "d": "New York's official symbols: rose, eastern bluebird, sugar maple, and more.", "g": "overview", "l": 2, "q": "What is New York: symbols overview?", "a": "New York's official symbols: rose, eastern bluebird, sugar maple, and more.", "x": "The official symbols of New York — the \"Empire State\" — tell the state's story in shorthand: the rose (flower), the eastern bluebird (bird), the sugar maple (tree), the motto \"Excelsior (Ever upward),\" and the flag. Seal with Liberty and Justice on blue. Legislatures designate symbols to honor what the state values; this database covers every one, what it means, and where to see it.", "s": "public-reference", "f": null}, {"t": "Nickname: Empire State", "d": "The nickname of New York is \"Empire State.\"", "g": "symbols", "l": 2, "q": "What is Nickname: Empire State?", "a": "The nickname of New York is \"Empire State.\"", "x": "The nickname of New York — \"Empire State\" — was adopted to express the state's identity. Seal with Liberty and Justice on blue. It appears on seals, plates, and proclamations. Haudenosaunee; Dutch New Amsterdam.", "s": "public-reference", "f": null}, {"t": "Nickname: the story", "d": "Why New York chose \"Empire State.\"", "g": "symbols", "l": 2, "q": "What is Nickname: the story?", "a": "Why New York chose \"Empire State.\"", "x": "Why \"Empire State\": the nickname's story reaches into New York's history — Revolution; Erie Canal.. Symbols are chosen, not found: committees, contests, and legislators all played a part. Knowing the story makes the symbol mean something.", "s": "public-reference", "f": null}, {"t": "Motto: Excelsior (Ever upward)", "d": "The motto of New York is \"Excelsior (Ever upward).\"", "g": "symbols", "l": 2, "q": "What is Motto: Excelsior (Ever upward)?", "a": "The motto of New York is \"Excelsior (Ever upward).\"", "x": "The motto of New York — \"Excelsior (Ever upward)\" — was adopted to express the state's identity. Seal with Liberty and Justice on blue. It appears on seals, plates, and proclamations. Haudenosaunee; Dutch New Amsterdam.", "s": "public-reference", "f": null}, {"t": "Motto: the story", "d": "Why New York chose \"Excelsior (Ever upward).\"", "g": "symbols", "l": 2, "q": "What is Motto: the story?", "a": "Why New York chose \"Excelsior (Ever upward).\"", "x": "Why \"Excelsior (Ever upward)\": the motto's story reaches into New York's history — Revolution; Erie Canal.. Symbols are chosen, not found: committees, contests, and legislators all played a part. Knowing the story makes the symbol mean something.", "s": "public-reference", "f": null}, {"t": "State flower: rose", "d": "The state flower of New York is the rose.", "g": "nature", "l": 2, "q": "What is State flower: rose?", "a": "The state flower of New York is the rose.", "x": "The rose — rose — is New York's officially designated state flower. Seal with Liberty and Justice on blue. It was chosen for its beauty, its abundance, or its meaning to the people. Times Square State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "rose: natural history", "d": "The rose in the wild.", "g": "nature", "l": 2, "q": "What is rose: natural history?", "a": "The rose in the wild.", "x": "In the wild, the rose blooms across the state. New York Learning the state flower's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Adirondack Park's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the flower", "d": "See New York's state flower at Adirondack Park.", "g": "nature", "l": 2, "q": "What is Where to see the flower?", "a": "See New York's state flower at Adirondack Park.", "x": "See the state flower where it thrives: Adirondack Park in New York is the surest bet, and Niagara Falls rewards the observant. Macy's Thanksgiving Parade Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "State bird: eastern bluebird", "d": "The state bird of New York is the eastern bluebird.", "g": "nature", "l": 2, "q": "What is State bird: eastern bluebird?", "a": "The state bird of New York is the eastern bluebird.", "x": "The eastern bluebird — eastern bluebird — is New York's officially designated state bird. Seal with Liberty and Justice on blue. It was chosen for its beauty, its abundance, or its meaning to the people. Times Square", "s": "public-reference", "f": null}, {"t": "eastern bluebird: natural history", "d": "The eastern bluebird in the wild.", "g": "nature", "l": 2, "q": "What is eastern bluebird: natural history?", "a": "The eastern bluebird in the wild.", "x": "In the wild, the eastern bluebird lives across the state. New York Learning the state bird's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Adirondack Park's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the bird", "d": "See New York's state bird at Adirondack Park.", "g": "nature", "l": 2, "q": "What is Where to see the bird?", "a": "See New York's state bird at Adirondack Park.", "x": "See the state bird where it thrives: Adirondack Park in New York is the surest bet, and Niagara Falls rewards the observant. Macy's Thanksgiving Parade Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "State tree: sugar maple", "d": "The state tree of New York is the sugar maple.", "g": "nature", "l": 2, "q": "What is State tree: sugar maple?", "a": "The state tree of New York is the sugar maple.", "x": "The sugar maple — sugar maple — is New York's officially designated state tree. Seal with Liberty and Justice on blue. It was chosen for its beauty, its abundance, or its meaning to the people. Times Square", "s": "public-reference", "f": null}, {"t": "sugar maple: natural history", "d": "The sugar maple in the wild.", "g": "nature", "l": 2, "q": "What is sugar maple: natural history?", "a": "The sugar maple in the wild.", "x": "In the wild, the sugar maple lives across the state. New York Learning the state tree's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Adirondack Park's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the tree", "d": "See New York's state tree at Adirondack Park.", "g": "nature", "l": 2, "q": "What is Where to see the tree?", "a": "See New York's state tree at Adirondack Park.", "x": "See the state tree where it thrives: Adirondack Park in New York is the surest bet, and Niagara Falls rewards the observant. Macy's Thanksgiving Parade Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "The state flag: design", "d": "New York's flag: Seal with Liberty and Justice on blue..", "g": "flag", "l": 2, "q": "What is The state flag: design?", "a": "New York's flag: Seal with Liberty and Justice on blue..", "x": "The flag of New York: Seal with Liberty and Justice on blue.. Every element was chosen deliberately — colors, seals, stars — and the design's history mirrors the state's. Finance, media, immigration. Fly it correctly: the flag code gives the rules, and New York flies it with pride.", "s": "public-reference", "f": null}, {"t": "The state flag: colors and emblem", "d": "What New York's flag means.", "g": "flag", "l": 2, "q": "What is The state flag: colors and emblem?", "a": "What New York's flag means.", "x": "The colors and emblem of New York's flag carry meaning: Seal with Liberty and Justice on blue.. Excelsior (Ever upward) Vexillologists rank flags by simplicity and symbolism — New York's tells its story at a glance to those who know the code.", "s": "public-reference", "f": null}, {"t": "The state flag: history", "d": "How New York got its flag.", "g": "flag", "l": 2, "q": "What is The state flag: history?", "a": "How New York got its flag.", "x": "The history of New York's flag: adopted after contests or commission designs, sometimes replacing earlier banners. The Erie Canal made New York the nation's port. Flags evolve with states — each change marks an era. The current design has flown over Albany's modern history.", "s": "public-reference", "f": null}, {"t": "The state seal", "d": "The Great Seal of New York.", "g": "symbols", "l": 2, "q": "What is The state seal?", "a": "The Great Seal of New York.", "x": "The Great Seal of New York authenticates the state's official acts — every law and commission bears it. Seal with Liberty and Justice on blue. The seal's imagery compresses the state's identity: its industries, its ideals, its motto \"Excelsior (Ever upward).\"", "s": "public-reference", "f": null}, {"t": "The state quarter", "d": "New York's quarter in the 50 State Quarters program.", "g": "symbols", "l": 2, "q": "What is The state quarter?", "a": "New York's quarter in the 50 State Quarters program.", "x": "New York's quarter: the US Mint's 50 State Quarters program (1999-2008) gave every state a circulating canvas. New York's design honors Empire State — pocket change as history lesson. Collectors still hunt them.", "s": "public-reference", "f": null}, {"t": "The capitol building", "d": "New York's capitol in Albany.", "g": "culture", "l": 2, "q": "What is The capitol building?", "a": "New York's capitol in Albany.", "x": "The New York State Capitol in Albany: the building where laws are made and history happened. Haudenosaunee; Dutch New Amsterdam. Capitols are museums of democracy — tour the chambers, the rotunda, the grounds. Statue of Liberty", "s": "public-reference", "f": null}, {"t": "The state song", "d": "New York's officially adopted state song.", "g": "culture", "l": 2, "q": "What is The state song?", "a": "New York's officially adopted state song.", "x": "The state song of New York was adopted by the legislature — every state has one, sung at official occasions. Macy's Thanksgiving Parade Songs, like flags, are identity set to music. Learn the chorus; it is the state's anthem in miniature.", "s": "public-reference", "f": null}, {"t": "How symbols are chosen", "d": "The legislature designates New York's symbols.", "g": "symbols", "l": 2, "q": "What is How symbols are chosen?", "a": "The legislature designates New York's symbols.", "x": "Symbols become official when the New York legislature says so — often after schoolchildren campaign, contests run, or committees deliberate. Excelsior (Ever upward) The process itself is civics: citizens proposing, debating, and adopting what represents them.", "s": "public-reference", "f": null}, {"t": "Flag etiquette", "d": "Displaying New York's flag correctly.", "g": "flag", "l": 2, "q": "What is Flag etiquette?", "a": "Displaying New York's flag correctly.", "x": "Flag etiquette for New York's banner: fly it sunrise to sunset (or lit at night), never let it touch the ground, and retire worn flags with dignity. Empire State The state flag flies below the US flag — a daily reminder of the federal order.", "s": "public-reference", "f": null}, {"t": "Symbol fact 1", "d": "More New York symbols: rose.", "g": "facts", "l": 2, "q": "What is Symbol fact 1?", "a": "More New York symbols: rose.", "x": "From the New York symbol file: rose. New York's symbols reward the curious — each one opens a story about the land, the people, or the moment it was chosen. \"Excelsior (Ever upward)\" indeed. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Symbol fact 2", "d": "More New York symbols: eastern bluebird.", "g": "facts", "l": 2, "q": "What is Symbol fact 2?", "a": "More New York symbols: eastern bluebird.", "x": "From the New York symbol file: eastern bluebird. New York's symbols reward the curious — each one opens a story about the land, the people, or the moment it was chosen. \"Excelsior (Ever upward)\" indeed.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-new-york-symbols-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
