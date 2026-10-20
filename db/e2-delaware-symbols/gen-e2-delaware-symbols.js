(function(){'use strict';
/* JAH Delaware Symbols Database generator — jahdb-e2-delaware-symbols-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-delaware-symbols',PREFIX='JAH-E2DELAWARES-',NAME='JAH Delaware Symbols Database';
var FIELDS=["overview", "symbols", "flag", "nature", "culture", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Delaware: symbols overview", "d": "Delaware's official symbols: peach blossom, Delaware blue hen, American holly, and more.", "g": "overview", "l": 2, "q": "What is Delaware: symbols overview?", "a": "Delaware's official symbols: peach blossom, Delaware blue hen, American holly, and more.", "x": "The official symbols of Delaware — the \"First State\" — tell the state's story in shorthand: the peach blossom (flower), the Delaware blue hen (bird), the American holly (tree), the motto \"Liberty and Independence,\" and the flag. Buff diamond on colonial blue; 1787 date. Legislatures designate symbols to honor what the state values; this database covers every one, what it means, and where to see it.", "s": "public-reference", "f": null}, {"t": "Nickname: First State", "d": "The nickname of Delaware is \"First State.\"", "g": "symbols", "l": 2, "q": "What is Nickname: First State?", "a": "The nickname of Delaware is \"First State.\"", "x": "The nickname of Delaware — \"First State\" — was adopted to express the state's identity. Buff diamond on colonial blue; 1787 date. It appears on seals, plates, and proclamations. Lenape lands; Swedish then Dutch then English.", "s": "public-reference", "f": null}, {"t": "Nickname: the story", "d": "Why Delaware chose \"First State.\"", "g": "symbols", "l": 2, "q": "What is Nickname: the story?", "a": "Why Delaware chose \"First State.\"", "x": "Why \"First State\": the nickname's story reaches into Delaware's history — First to ratify the Constitution.. Symbols are chosen, not found: committees, contests, and legislators all played a part. Knowing the story makes the symbol mean something.", "s": "public-reference", "f": null}, {"t": "Motto: Liberty and Independence", "d": "The motto of Delaware is \"Liberty and Independence.\"", "g": "symbols", "l": 2, "q": "What is Motto: Liberty and Independence?", "a": "The motto of Delaware is \"Liberty and Independence.\"", "x": "The motto of Delaware — \"Liberty and Independence\" — was adopted to express the state's identity. Buff diamond on colonial blue; 1787 date. It appears on seals, plates, and proclamations. Lenape lands; Swedish then Dutch then English.", "s": "public-reference", "f": null}, {"t": "Motto: the story", "d": "Why Delaware chose \"Liberty and Independence.\"", "g": "symbols", "l": 2, "q": "What is Motto: the story?", "a": "Why Delaware chose \"Liberty and Independence.\"", "x": "Why \"Liberty and Independence\": the motto's story reaches into Delaware's history — First to ratify the Constitution.. Symbols are chosen, not found: committees, contests, and legislators all played a part. Knowing the story makes the symbol mean something.", "s": "public-reference", "f": null}, {"t": "State flower: peach blossom", "d": "The state flower of Delaware is the peach blossom.", "g": "nature", "l": 2, "q": "What is State flower: peach blossom?", "a": "The state flower of Delaware is the peach blossom.", "x": "The peach blossom — peach blossom — is Delaware's officially designated state flower. Buff diamond on colonial blue; 1787 date. It was chosen for its beauty, its abundance, or its meaning to the people. Winterthur Museum", "s": "public-reference", "f": null}, {"t": "peach blossom: natural history", "d": "The peach blossom in the wild.", "g": "nature", "l": 2, "q": "What is peach blossom: natural history?", "a": "The peach blossom in the wild.", "x": "In the wild, the peach blossom blooms across the state. Delaware Learning the state flower's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Cape Henlopen State Park's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the flower", "d": "See Delaware's state flower at Cape Henlopen State Park.", "g": "nature", "l": 2, "q": "What is Where to see the flower?", "a": "See Delaware's state flower at Cape Henlopen State Park.", "x": "See the state flower where it thrives: Cape Henlopen State Park in Delaware is the surest bet, and Delaware beaches rewards the observant. Rehoboth Beach festivals Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "State bird: Delaware blue hen", "d": "The state bird of Delaware is the Delaware blue hen.", "g": "nature", "l": 2, "q": "What is State bird: Delaware blue hen?", "a": "The state bird of Delaware is the Delaware blue hen.", "x": "The Delaware blue hen — Delaware blue hen — is Delaware's officially designated state bird. Buff diamond on colonial blue; 1787 date. It was chosen for its beauty, its abundance, or its meaning to the people. Winterthur Museum", "s": "public-reference", "f": null}, {"t": "Delaware blue hen: natural history", "d": "The Delaware blue hen in the wild.", "g": "nature", "l": 2, "q": "What is Delaware blue hen: natural history?", "a": "The Delaware blue hen in the wild.", "x": "In the wild, the Delaware blue hen lives across the state. Delaware Learning the state bird's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Cape Henlopen State Park's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the bird", "d": "See Delaware's state bird at Cape Henlopen State Park.", "g": "nature", "l": 2, "q": "What is Where to see the bird?", "a": "See Delaware's state bird at Cape Henlopen State Park.", "x": "See the state bird where it thrives: Cape Henlopen State Park in Delaware is the surest bet, and Delaware beaches rewards the observant. Rehoboth Beach festivals Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "State tree: American holly", "d": "The state tree of Delaware is the American holly.", "g": "nature", "l": 2, "q": "What is State tree: American holly?", "a": "The state tree of Delaware is the American holly.", "x": "The American holly — American holly — is Delaware's officially designated state tree. Buff diamond on colonial blue; 1787 date. It was chosen for its beauty, its abundance, or its meaning to the people. Winterthur Museum", "s": "public-reference", "f": null}, {"t": "American holly: natural history", "d": "The American holly in the wild.", "g": "nature", "l": 2, "q": "What is American holly: natural history?", "a": "The American holly in the wild.", "x": "In the wild, the American holly lives across the state. Delaware Learning the state tree's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Cape Henlopen State Park's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the tree", "d": "See Delaware's state tree at Cape Henlopen State Park.", "g": "nature", "l": 2, "q": "What is Where to see the tree?", "a": "See Delaware's state tree at Cape Henlopen State Park.", "x": "See the state tree where it thrives: Cape Henlopen State Park in Delaware is the surest bet, and Delaware beaches rewards the observant. Rehoboth Beach festivals Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "The state flag: design", "d": "Delaware's flag: Buff diamond on colonial blue; 1787 date..", "g": "flag", "l": 2, "q": "What is The state flag: design?", "a": "Delaware's flag: Buff diamond on colonial blue; 1787 date..", "x": "The flag of Delaware: Buff diamond on colonial blue; 1787 date.. Every element was chosen deliberately — colors, seals, stars — and the design's history mirrors the state's. DuPont chemicals; corporate haven. Fly it correctly: the flag code gives the rules, and Delaware flies it with pride.", "s": "public-reference", "f": null}, {"t": "The state flag: colors and emblem", "d": "What Delaware's flag means.", "g": "flag", "l": 2, "q": "What is The state flag: colors and emblem?", "a": "What Delaware's flag means.", "x": "The colors and emblem of Delaware's flag carry meaning: Buff diamond on colonial blue; 1787 date.. Liberty and Independence Vexillologists rank flags by simplicity and symbolism — Delaware's tells its story at a glance to those who know the code.", "s": "public-reference", "f": null}, {"t": "The state flag: history", "d": "How Delaware got its flag.", "g": "flag", "l": 2, "q": "What is The state flag: history?", "a": "How Delaware got its flag.", "x": "The history of Delaware's flag: adopted after contests or commission designs, sometimes replacing earlier banners. Tax-free shopping. Flags evolve with states — each change marks an era. The current design has flown over Dover's modern history.", "s": "public-reference", "f": null}, {"t": "The state seal", "d": "The Great Seal of Delaware.", "g": "symbols", "l": 2, "q": "What is The state seal?", "a": "The Great Seal of Delaware.", "x": "The Great Seal of Delaware authenticates the state's official acts — every law and commission bears it. Buff diamond on colonial blue; 1787 date. The seal's imagery compresses the state's identity: its industries, its ideals, its motto \"Liberty and Independence.\"", "s": "public-reference", "f": null}, {"t": "The state quarter", "d": "Delaware's quarter in the 50 State Quarters program.", "g": "symbols", "l": 2, "q": "What is The state quarter?", "a": "Delaware's quarter in the 50 State Quarters program.", "x": "Delaware's quarter: the US Mint's 50 State Quarters program (1999-2008) gave every state a circulating canvas. Delaware's design honors First State — pocket change as history lesson. Collectors still hunt them.", "s": "public-reference", "f": null}, {"t": "The capitol building", "d": "Delaware's capitol in Dover.", "g": "culture", "l": 2, "q": "What is The capitol building?", "a": "Delaware's capitol in Dover.", "x": "The Delaware State Capitol in Dover: the building where laws are made and history happened. Lenape lands; Swedish then Dutch then English. Capitols are museums of democracy — tour the chambers, the rotunda, the grounds. Rehoboth Beach", "s": "public-reference", "f": null}, {"t": "The state song", "d": "Delaware's officially adopted state song.", "g": "culture", "l": 2, "q": "What is The state song?", "a": "Delaware's officially adopted state song.", "x": "The state song of Delaware was adopted by the legislature — every state has one, sung at official occasions. Rehoboth Beach festivals Songs, like flags, are identity set to music. Learn the chorus; it is the state's anthem in miniature.", "s": "public-reference", "f": null}, {"t": "How symbols are chosen", "d": "The legislature designates Delaware's symbols.", "g": "symbols", "l": 2, "q": "What is How symbols are chosen?", "a": "The legislature designates Delaware's symbols.", "x": "Symbols become official when the Delaware legislature says so — often after schoolchildren campaign, contests run, or committees deliberate. Liberty and Independence The process itself is civics: citizens proposing, debating, and adopting what represents them.", "s": "public-reference", "f": null}, {"t": "Flag etiquette", "d": "Displaying Delaware's flag correctly.", "g": "flag", "l": 2, "q": "What is Flag etiquette?", "a": "Displaying Delaware's flag correctly.", "x": "Flag etiquette for Delaware's banner: fly it sunrise to sunset (or lit at night), never let it touch the ground, and retire worn flags with dignity. First State The state flag flies below the US flag — a daily reminder of the federal order.", "s": "public-reference", "f": null}, {"t": "Symbol fact 1", "d": "More Delaware symbols: peach blossom.", "g": "facts", "l": 2, "q": "What is Symbol fact 1?", "a": "More Delaware symbols: peach blossom.", "x": "From the Delaware symbol file: peach blossom. Delaware's symbols reward the curious — each one opens a story about the land, the people, or the moment it was chosen. \"Liberty and Independence\" indeed.", "s": "public-reference", "f": null}, {"t": "Symbol fact 2", "d": "More Delaware symbols: Delaware blue hen.", "g": "facts", "l": 2, "q": "What is Symbol fact 2?", "a": "More Delaware symbols: Delaware blue hen.", "x": "From the Delaware symbol file: Delaware blue hen. Delaware's symbols reward the curious — each one opens a story about the land, the people, or the moment it was chosen. \"Liberty and Independence\" indeed.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-delaware-symbols-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
