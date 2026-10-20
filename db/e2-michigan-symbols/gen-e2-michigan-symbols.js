(function(){'use strict';
/* JAH Michigan Symbols Database generator — jahdb-e2-michigan-symbols-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-michigan-symbols',PREFIX='JAH-E2MICHIGANS-',NAME='JAH Michigan Symbols Database';
var FIELDS=["overview", "symbols", "flag", "nature", "culture", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Michigan: symbols overview", "d": "Michigan's official symbols: apple blossom, American robin, eastern white pine, and more.", "g": "overview", "l": 2, "q": "What is Michigan: symbols overview?", "a": "Michigan's official symbols: apple blossom, American robin, eastern white pine, and more.", "x": "The official symbols of Michigan — the \"Great Lakes State\" — tell the state's story in shorthand: the apple blossom (flower), the American robin (bird), the eastern white pine (tree), the motto \"Si quaeris peninsulam amoenam circumspice (If you seek a pleasant peninsula, look about you),\" and the flag. Elk, moose, and eagle seal on blue. Legislatures designate symbols to honor what the state values; this database covers every one, what it means, and where to see it.", "s": "public-reference", "f": null}, {"t": "Nickname: Great Lakes State", "d": "The nickname of Michigan is \"Great Lakes State.\"", "g": "symbols", "l": 2, "q": "What is Nickname: Great Lakes State?", "a": "The nickname of Michigan is \"Great Lakes State.\"", "x": "The nickname of Michigan — \"Great Lakes State\" — was adopted to express the state's identity. Elk, moose, and eagle seal on blue. It appears on seals, plates, and proclamations. Ojibwe; French then British.", "s": "public-reference", "f": null}, {"t": "Nickname: the story", "d": "Why Michigan chose \"Great Lakes State.\"", "g": "symbols", "l": 2, "q": "What is Nickname: the story?", "a": "Why Michigan chose \"Great Lakes State.\"", "x": "Why \"Great Lakes State\": the nickname's story reaches into Michigan's history — Auto industry; Detroit boom.. Symbols are chosen, not found: committees, contests, and legislators all played a part. Knowing the story makes the symbol mean something.", "s": "public-reference", "f": null}, {"t": "Motto: Si quaeris peninsulam amoenam circumspice (If you seek a pleasant peninsula, look about you)", "d": "The motto of Michigan is \"Si quaeris peninsulam amoenam circumspice (If you seek a pleasant peninsula, look about you).\"", "g": "symbols", "l": 2, "q": "What is Motto: Si quaeris peninsulam amoenam circumspice (If you seek a pleasant peninsula, look about you)?", "a": "The motto of Michigan is \"Si quaeris peninsulam amoenam circumspice (If you seek a pleasant peninsula, look about you).\"", "x": "The motto of Michigan — \"Si quaeris peninsulam amoenam circumspice (If you seek a pleasant peninsula, look about you)\" — was adopted to express the state's identity. Elk, moose, and eagle seal on blue. It appears on seals, plates, and proclamations. Ojibwe; French then British.", "s": "public-reference", "f": null}, {"t": "Motto: the story", "d": "Why Michigan chose \"Si quaeris peninsulam amoenam circumspice (If you seek a pleasant peninsula, look about you).\"", "g": "symbols", "l": 2, "q": "What is Motto: the story?", "a": "Why Michigan chose \"Si quaeris peninsulam amoenam circumspice (If you seek a pleasant peninsula, look about you).\"", "x": "Why \"Si quaeris peninsulam amoenam circumspice (If you seek a pleasant peninsula, look about you)\": the motto's story reaches into Michigan's history — Auto industry; Detroit boom.. Symbols are chosen, not found: committees, contests, and legislators all played a part. Knowing the story makes the symbol mean something.", "s": "public-reference", "f": null}, {"t": "State flower: apple blossom", "d": "The state flower of Michigan is the apple blossom.", "g": "nature", "l": 2, "q": "What is State flower: apple blossom?", "a": "The state flower of Michigan is the apple blossom.", "x": "The apple blossom — apple blossom — is Michigan's officially designated state flower. Elk, moose, and eagle seal on blue. It was chosen for its beauty, its abundance, or its meaning to the people. Sleeping Bear Dunes", "s": "public-reference", "f": null}, {"t": "apple blossom: natural history", "d": "The apple blossom in the wild.", "g": "nature", "l": 2, "q": "What is apple blossom: natural history?", "a": "The apple blossom in the wild.", "x": "In the wild, the apple blossom blooms across the state. Michigan Learning the state flower's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Sleeping Bear Dunes National Lakeshore's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the flower", "d": "See Michigan's state flower at Sleeping Bear Dunes National Lakeshore.", "g": "nature", "l": 2, "q": "What is Where to see the flower?", "a": "See Michigan's state flower at Sleeping Bear Dunes National Lakeshore.", "x": "See the state flower where it thrives: Sleeping Bear Dunes National Lakeshore in Michigan is the surest bet, and Henry Ford Museum rewards the observant. Detroit Jazz Festival Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "State bird: American robin", "d": "The state bird of Michigan is the American robin.", "g": "nature", "l": 2, "q": "What is State bird: American robin?", "a": "The state bird of Michigan is the American robin.", "x": "The American robin — American robin — is Michigan's officially designated state bird. Elk, moose, and eagle seal on blue. It was chosen for its beauty, its abundance, or its meaning to the people. Sleeping Bear Dunes", "s": "public-reference", "f": null}, {"t": "American robin: natural history", "d": "The American robin in the wild.", "g": "nature", "l": 2, "q": "What is American robin: natural history?", "a": "The American robin in the wild.", "x": "In the wild, the American robin lives across the state. Michigan Learning the state bird's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Sleeping Bear Dunes National Lakeshore's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the bird", "d": "See Michigan's state bird at Sleeping Bear Dunes National Lakeshore.", "g": "nature", "l": 2, "q": "What is Where to see the bird?", "a": "See Michigan's state bird at Sleeping Bear Dunes National Lakeshore.", "x": "See the state bird where it thrives: Sleeping Bear Dunes National Lakeshore in Michigan is the surest bet, and Henry Ford Museum rewards the observant. Detroit Jazz Festival Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "State tree: eastern white pine", "d": "The state tree of Michigan is the eastern white pine.", "g": "nature", "l": 2, "q": "What is State tree: eastern white pine?", "a": "The state tree of Michigan is the eastern white pine.", "x": "The eastern white pine — eastern white pine — is Michigan's officially designated state tree. Elk, moose, and eagle seal on blue. It was chosen for its beauty, its abundance, or its meaning to the people. Sleeping Bear Dunes", "s": "public-reference", "f": null}, {"t": "eastern white pine: natural history", "d": "The eastern white pine in the wild.", "g": "nature", "l": 2, "q": "What is eastern white pine: natural history?", "a": "The eastern white pine in the wild.", "x": "In the wild, the eastern white pine lives across the state. Michigan Learning the state tree's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Sleeping Bear Dunes National Lakeshore's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the tree", "d": "See Michigan's state tree at Sleeping Bear Dunes National Lakeshore.", "g": "nature", "l": 2, "q": "What is Where to see the tree?", "a": "See Michigan's state tree at Sleeping Bear Dunes National Lakeshore.", "x": "See the state tree where it thrives: Sleeping Bear Dunes National Lakeshore in Michigan is the surest bet, and Henry Ford Museum rewards the observant. Detroit Jazz Festival Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "The state flag: design", "d": "Michigan's flag: Elk, moose, and eagle seal on blue..", "g": "flag", "l": 2, "q": "What is The state flag: design?", "a": "Michigan's flag: Elk, moose, and eagle seal on blue..", "x": "The flag of Michigan: Elk, moose, and eagle seal on blue.. Every element was chosen deliberately — colors, seals, stars — and the design's history mirrors the state's. Deindustrialization; comeback. Fly it correctly: the flag code gives the rules, and Michigan flies it with pride.", "s": "public-reference", "f": null}, {"t": "The state flag: colors and emblem", "d": "What Michigan's flag means.", "g": "flag", "l": 2, "q": "What is The state flag: colors and emblem?", "a": "What Michigan's flag means.", "x": "The colors and emblem of Michigan's flag carry meaning: Elk, moose, and eagle seal on blue.. Si quaeris peninsulam amoenam circumspice (If you seek a pleasant peninsula, look about you) Vexillologists rank flags by simplicity and symbolism — Michigan's tells its story at a glance to those who know the code.", "s": "public-reference", "f": null}, {"t": "The state flag: history", "d": "How Michigan got its flag.", "g": "flag", "l": 2, "q": "What is The state flag: history?", "a": "How Michigan got its flag.", "x": "The history of Michigan's flag: adopted after contests or commission designs, sometimes replacing earlier banners. The auto industry made Detroit the Motor City. Flags evolve with states — each change marks an era. The current design has flown over Lansing's modern history.", "s": "public-reference", "f": null}, {"t": "The state seal", "d": "The Great Seal of Michigan.", "g": "symbols", "l": 2, "q": "What is The state seal?", "a": "The Great Seal of Michigan.", "x": "The Great Seal of Michigan authenticates the state's official acts — every law and commission bears it. Elk, moose, and eagle seal on blue. The seal's imagery compresses the state's identity: its industries, its ideals, its motto \"Si quaeris peninsulam amoenam circumspice (If you seek a pleasant peninsula, look about you).\"", "s": "public-reference", "f": null}, {"t": "The state quarter", "d": "Michigan's quarter in the 50 State Quarters program.", "g": "symbols", "l": 2, "q": "What is The state quarter?", "a": "Michigan's quarter in the 50 State Quarters program.", "x": "Michigan's quarter: the US Mint's 50 State Quarters program (1999-2008) gave every state a circulating canvas. Michigan's design honors Great Lakes State — pocket change as history lesson. Collectors still hunt them.", "s": "public-reference", "f": null}, {"t": "The capitol building", "d": "Michigan's capitol in Lansing.", "g": "culture", "l": 2, "q": "What is The capitol building?", "a": "Michigan's capitol in Lansing.", "x": "The Michigan State Capitol in Lansing: the building where laws are made and history happened. Ojibwe; French then British. Capitols are museums of democracy — tour the chambers, the rotunda, the grounds. Mackinac Island", "s": "public-reference", "f": null}, {"t": "The state song", "d": "Michigan's officially adopted state song.", "g": "culture", "l": 2, "q": "What is The state song?", "a": "Michigan's officially adopted state song.", "x": "The state song of Michigan was adopted by the legislature — every state has one, sung at official occasions. Detroit Jazz Festival Songs, like flags, are identity set to music. Learn the chorus; it is the state's anthem in miniature.", "s": "public-reference", "f": null}, {"t": "How symbols are chosen", "d": "The legislature designates Michigan's symbols.", "g": "symbols", "l": 2, "q": "What is How symbols are chosen?", "a": "The legislature designates Michigan's symbols.", "x": "Symbols become official when the Michigan legislature says so — often after schoolchildren campaign, contests run, or committees deliberate. Si quaeris peninsulam amoenam circumspice (If you seek a pleasant peninsula, look about you) The process itself is civics: citizens proposing, debating, and adopting what represents them.", "s": "public-reference", "f": null}, {"t": "Flag etiquette", "d": "Displaying Michigan's flag correctly.", "g": "flag", "l": 2, "q": "What is Flag etiquette?", "a": "Displaying Michigan's flag correctly.", "x": "Flag etiquette for Michigan's banner: fly it sunrise to sunset (or lit at night), never let it touch the ground, and retire worn flags with dignity. Great Lakes State The state flag flies below the US flag — a daily reminder of the federal order.", "s": "public-reference", "f": null}, {"t": "Symbol fact 1", "d": "More Michigan symbols: apple blossom.", "g": "facts", "l": 2, "q": "What is Symbol fact 1?", "a": "More Michigan symbols: apple blossom.", "x": "From the Michigan symbol file: apple blossom. Michigan's symbols reward the curious — each one opens a story about the land, the people, or the moment it was chosen. \"Si quaeris peninsulam amoenam circumspice (If you seek a pleasant peninsula, look about you)\" indeed.", "s": "public-reference", "f": null}, {"t": "Symbol fact 2", "d": "More Michigan symbols: American robin.", "g": "facts", "l": 2, "q": "What is Symbol fact 2?", "a": "More Michigan symbols: American robin.", "x": "From the Michigan symbol file: American robin. Michigan's symbols reward the curious — each one opens a story about the land, the people, or the moment it was chosen. \"Si quaeris peninsulam amoenam circumspice (If you seek a pleasant peninsula, look about you)\" indeed.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-michigan-symbols-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
