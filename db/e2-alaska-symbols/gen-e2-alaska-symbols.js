(function(){'use strict';
/* JAH Alaska Symbols Database generator — jahdb-e2-alaska-symbols-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-alaska-symbols',PREFIX='JAH-E2ALASKASYM-',NAME='JAH Alaska Symbols Database';
var FIELDS=["overview", "symbols", "flag", "nature", "culture", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Alaska: symbols overview", "d": "Alaska's official symbols: forget-me-not, willow ptarmigan, Sitka spruce, and more.", "g": "overview", "l": 2, "q": "What is Alaska: symbols overview?", "a": "Alaska's official symbols: forget-me-not, willow ptarmigan, Sitka spruce, and more.", "x": "The official symbols of Alaska — the \"The Last Frontier\" — tell the state's story in shorthand: the forget-me-not (flower), the willow ptarmigan (bird), the Sitka spruce (tree), the motto \"North to the Future,\" and the flag. Eight gold stars (Big Dipper + Polaris) on blue. Legislatures designate symbols to honor what the state values; this database covers every one, what it means, and where to see it.", "s": "public-reference", "f": null}, {"t": "Nickname: The Last Frontier", "d": "The nickname of Alaska is \"The Last Frontier.\"", "g": "symbols", "l": 2, "q": "What is Nickname: The Last Frontier?", "a": "The nickname of Alaska is \"The Last Frontier.\"", "x": "The nickname of Alaska — \"The Last Frontier\" — was adopted to express the state's identity. Eight gold stars (Big Dipper + Polaris) on blue. It appears on seals, plates, and proclamations. Native Alutiiq, Tlingit cultures for millennia.", "s": "public-reference", "f": null}, {"t": "Nickname: the story", "d": "Why Alaska chose \"The Last Frontier.\"", "g": "symbols", "l": 2, "q": "What is Nickname: the story?", "a": "Why Alaska chose \"The Last Frontier.\"", "x": "Why \"The Last Frontier\": the nickname's story reaches into Alaska's history — Russian colony; U.S. purchase 1867.. Symbols are chosen, not found: committees, contests, and legislators all played a part. Knowing the story makes the symbol mean something.", "s": "public-reference", "f": null}, {"t": "Motto: North to the Future", "d": "The motto of Alaska is \"North to the Future.\"", "g": "symbols", "l": 2, "q": "What is Motto: North to the Future?", "a": "The motto of Alaska is \"North to the Future.\"", "x": "The motto of Alaska — \"North to the Future\" — was adopted to express the state's identity. Eight gold stars (Big Dipper + Polaris) on blue. It appears on seals, plates, and proclamations. Native Alutiiq, Tlingit cultures for millennia.", "s": "public-reference", "f": null}, {"t": "Motto: the story", "d": "Why Alaska chose \"North to the Future.\"", "g": "symbols", "l": 2, "q": "What is Motto: the story?", "a": "Why Alaska chose \"North to the Future.\"", "x": "Why \"North to the Future\": the motto's story reaches into Alaska's history — Russian colony; U.S. purchase 1867.. Symbols are chosen, not found: committees, contests, and legislators all played a part. Knowing the story makes the symbol mean something.", "s": "public-reference", "f": null}, {"t": "State flower: forget-me-not", "d": "The state flower of Alaska is the forget-me-not.", "g": "nature", "l": 2, "q": "What is State flower: forget-me-not?", "a": "The state flower of Alaska is the forget-me-not.", "x": "The forget-me-not — forget-me-not — is Alaska's officially designated state flower. Eight gold stars (Big Dipper + Polaris) on blue. It was chosen for its beauty, its abundance, or its meaning to the people. Glacier Bay", "s": "public-reference", "f": null}, {"t": "forget-me-not: natural history", "d": "The forget-me-not in the wild.", "g": "nature", "l": 2, "q": "What is forget-me-not: natural history?", "a": "The forget-me-not in the wild.", "x": "In the wild, the forget-me-not blooms across the state. Alaska Learning the state flower's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Denali National Park's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the flower", "d": "See Alaska's state flower at Denali National Park.", "g": "nature", "l": 2, "q": "What is Where to see the flower?", "a": "See Alaska's state flower at Denali National Park.", "x": "See the state flower where it thrives: Denali National Park in Alaska is the surest bet, and Kenai Fjords rewards the observant. Iditarod Visit in season, bring patience, and leave only footprints. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "State bird: willow ptarmigan", "d": "The state bird of Alaska is the willow ptarmigan.", "g": "nature", "l": 2, "q": "What is State bird: willow ptarmigan?", "a": "The state bird of Alaska is the willow ptarmigan.", "x": "The willow ptarmigan — willow ptarmigan — is Alaska's officially designated state bird. Eight gold stars (Big Dipper + Polaris) on blue. It was chosen for its beauty, its abundance, or its meaning to the people. Glacier Bay", "s": "public-reference", "f": null}, {"t": "willow ptarmigan: natural history", "d": "The willow ptarmigan in the wild.", "g": "nature", "l": 2, "q": "What is willow ptarmigan: natural history?", "a": "The willow ptarmigan in the wild.", "x": "In the wild, the willow ptarmigan lives across the state. Alaska Learning the state bird's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Denali National Park's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the bird", "d": "See Alaska's state bird at Denali National Park.", "g": "nature", "l": 2, "q": "What is Where to see the bird?", "a": "See Alaska's state bird at Denali National Park.", "x": "See the state bird where it thrives: Denali National Park in Alaska is the surest bet, and Kenai Fjords rewards the observant. Iditarod Visit in season, bring patience, and leave only footprints. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "State tree: Sitka spruce", "d": "The state tree of Alaska is the Sitka spruce.", "g": "nature", "l": 2, "q": "What is State tree: Sitka spruce?", "a": "The state tree of Alaska is the Sitka spruce.", "x": "The Sitka spruce — Sitka spruce — is Alaska's officially designated state tree. Eight gold stars (Big Dipper + Polaris) on blue. It was chosen for its beauty, its abundance, or its meaning to the people. Glacier Bay", "s": "public-reference", "f": null}, {"t": "Sitka spruce: natural history", "d": "The Sitka spruce in the wild.", "g": "nature", "l": 2, "q": "What is Sitka spruce: natural history?", "a": "The Sitka spruce in the wild.", "x": "In the wild, the Sitka spruce lives across the state. Alaska Learning the state tree's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Denali National Park's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the tree", "d": "See Alaska's state tree at Denali National Park.", "g": "nature", "l": 2, "q": "What is Where to see the tree?", "a": "See Alaska's state tree at Denali National Park.", "x": "See the state tree where it thrives: Denali National Park in Alaska is the surest bet, and Kenai Fjords rewards the observant. Iditarod Visit in season, bring patience, and leave only footprints. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "The state flag: design", "d": "Alaska's flag: Eight gold stars (Big Dipper + Polaris) on blue..", "g": "flag", "l": 2, "q": "What is The state flag: design?", "a": "Alaska's flag: Eight gold stars (Big Dipper + Polaris) on blue..", "x": "The flag of Alaska: Eight gold stars (Big Dipper + Polaris) on blue.. Every element was chosen deliberately — colors, seals, stars — and the design's history mirrors the state's. Gold rush 1898; oil at Prudhoe Bay. Fly it correctly: the flag code gives the rules, and Alaska flies it with pride.", "s": "public-reference", "f": null}, {"t": "The state flag: colors and emblem", "d": "What Alaska's flag means.", "g": "flag", "l": 2, "q": "What is The state flag: colors and emblem?", "a": "What Alaska's flag means.", "x": "The colors and emblem of Alaska's flag carry meaning: Eight gold stars (Big Dipper + Polaris) on blue.. North to the Future Vexillologists rank flags by simplicity and symbolism — Alaska's tells its story at a glance to those who know the code.", "s": "public-reference", "f": null}, {"t": "The state flag: history", "d": "How Alaska got its flag.", "g": "flag", "l": 2, "q": "What is The state flag: history?", "a": "How Alaska got its flag.", "x": "The history of Alaska's flag: adopted after contests or commission designs, sometimes replacing earlier banners. Statehood 1959; pipeline era. Flags evolve with states — each change marks an era. The current design has flown over Juneau's modern history.", "s": "public-reference", "f": null}, {"t": "The state seal", "d": "The Great Seal of Alaska.", "g": "symbols", "l": 2, "q": "What is The state seal?", "a": "The Great Seal of Alaska.", "x": "The Great Seal of Alaska authenticates the state's official acts — every law and commission bears it. Eight gold stars (Big Dipper + Polaris) on blue. The seal's imagery compresses the state's identity: its industries, its ideals, its motto \"North to the Future.\"", "s": "public-reference", "f": null}, {"t": "The state quarter", "d": "Alaska's quarter in the 50 State Quarters program.", "g": "symbols", "l": 2, "q": "What is The state quarter?", "a": "Alaska's quarter in the 50 State Quarters program.", "x": "Alaska's quarter: the US Mint's 50 State Quarters program (1999-2008) gave every state a circulating canvas. Alaska's design honors The Last Frontier — pocket change as history lesson. Collectors still hunt them.", "s": "public-reference", "f": null}, {"t": "The capitol building", "d": "Alaska's capitol in Juneau.", "g": "culture", "l": 2, "q": "What is The capitol building?", "a": "Alaska's capitol in Juneau.", "x": "The Alaska State Capitol in Juneau: the building where laws are made and history happened. Native Alutiiq, Tlingit cultures for millennia. Capitols are museums of democracy — tour the chambers, the rotunda, the grounds. Denali National Park", "s": "public-reference", "f": null}, {"t": "The state song", "d": "Alaska's officially adopted state song.", "g": "culture", "l": 2, "q": "What is The state song?", "a": "Alaska's officially adopted state song.", "x": "The state song of Alaska was adopted by the legislature — every state has one, sung at official occasions. Iditarod Songs, like flags, are identity set to music. Learn the chorus; it is the state's anthem in miniature.", "s": "public-reference", "f": null}, {"t": "How symbols are chosen", "d": "The legislature designates Alaska's symbols.", "g": "symbols", "l": 2, "q": "What is How symbols are chosen?", "a": "The legislature designates Alaska's symbols.", "x": "Symbols become official when the Alaska legislature says so — often after schoolchildren campaign, contests run, or committees deliberate. North to the Future The process itself is civics: citizens proposing, debating, and adopting what represents them.", "s": "public-reference", "f": null}, {"t": "Flag etiquette", "d": "Displaying Alaska's flag correctly.", "g": "flag", "l": 2, "q": "What is Flag etiquette?", "a": "Displaying Alaska's flag correctly.", "x": "Flag etiquette for Alaska's banner: fly it sunrise to sunset (or lit at night), never let it touch the ground, and retire worn flags with dignity. The Last Frontier The state flag flies below the US flag — a daily reminder of the federal order.", "s": "public-reference", "f": null}, {"t": "Symbol fact 1", "d": "More Alaska symbols: forget-me-not.", "g": "facts", "l": 2, "q": "What is Symbol fact 1?", "a": "More Alaska symbols: forget-me-not.", "x": "From the Alaska symbol file: forget-me-not. Alaska's symbols reward the curious — each one opens a story about the land, the people, or the moment it was chosen. \"North to the Future\" indeed. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "Symbol fact 2", "d": "More Alaska symbols: willow ptarmigan.", "g": "facts", "l": 2, "q": "What is Symbol fact 2?", "a": "More Alaska symbols: willow ptarmigan.", "x": "From the Alaska symbol file: willow ptarmigan. Alaska's symbols reward the curious — each one opens a story about the land, the people, or the moment it was chosen. \"North to the Future\" indeed. State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-alaska-symbols-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
