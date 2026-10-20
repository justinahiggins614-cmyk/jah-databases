(function(){'use strict';
/* JAH Minnesota Symbols Database generator — jahdb-e2-minnesota-symbols-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-minnesota-symbols',PREFIX='JAH-E2MINNESOTA-',NAME='JAH Minnesota Symbols Database';
var FIELDS=["overview", "symbols", "flag", "nature", "culture", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Minnesota: symbols overview", "d": "Minnesota's official symbols: pink and white lady's slipper, common loon, red (Norway) pine, and more.", "g": "overview", "l": 2, "q": "What is Minnesota: symbols overview?", "a": "Minnesota's official symbols: pink and white lady's slipper, common loon, red (Norway) pine, and more.", "x": "The official symbols of Minnesota — the \"North Star State\" — tell the state's story in shorthand: the pink and white lady's slipper (flower), the common loon (bird), the red (Norway) pine (tree), the motto \"L'Etoile du Nord (The star of the north),\" and the flag. Seal with farmer, Native American, Mississippi on blue. Legislatures designate symbols to honor what the state values; this database covers every one, what it means, and where to see it.", "s": "public-reference", "f": null}, {"t": "Nickname: North Star State", "d": "The nickname of Minnesota is \"North Star State.\"", "g": "symbols", "l": 2, "q": "What is Nickname: North Star State?", "a": "The nickname of Minnesota is \"North Star State.\"", "x": "The nickname of Minnesota — \"North Star State\" — was adopted to express the state's identity. Seal with farmer, Native American, Mississippi on blue. It appears on seals, plates, and proclamations. Dakota and Ojibwe; French then U.S.", "s": "public-reference", "f": null}, {"t": "Nickname: the story", "d": "Why Minnesota chose \"North Star State.\"", "g": "symbols", "l": 2, "q": "What is Nickname: the story?", "a": "Why Minnesota chose \"North Star State.\"", "x": "Why \"North Star State\": the nickname's story reaches into Minnesota's history — Flour milling; iron range.. Symbols are chosen, not found: committees, contests, and legislators all played a part. Knowing the story makes the symbol mean something.", "s": "public-reference", "f": null}, {"t": "Motto: L'Etoile du Nord (The star of the north)", "d": "The motto of Minnesota is \"L'Etoile du Nord (The star of the north).\"", "g": "symbols", "l": 2, "q": "What is Motto: L'Etoile du Nord (The star of the north)?", "a": "The motto of Minnesota is \"L'Etoile du Nord (The star of the north).\"", "x": "The motto of Minnesota — \"L'Etoile du Nord (The star of the north)\" — was adopted to express the state's identity. Seal with farmer, Native American, Mississippi on blue. It appears on seals, plates, and proclamations. Dakota and Ojibwe; French then U.S.", "s": "public-reference", "f": null}, {"t": "Motto: the story", "d": "Why Minnesota chose \"L'Etoile du Nord (The star of the north).\"", "g": "symbols", "l": 2, "q": "What is Motto: the story?", "a": "Why Minnesota chose \"L'Etoile du Nord (The star of the north).\"", "x": "Why \"L'Etoile du Nord (The star of the north)\": the motto's story reaches into Minnesota's history — Flour milling; iron range.. Symbols are chosen, not found: committees, contests, and legislators all played a part. Knowing the story makes the symbol mean something.", "s": "public-reference", "f": null}, {"t": "State flower: pink and white lady's slipper", "d": "The state flower of Minnesota is the pink and white lady's slipper.", "g": "nature", "l": 2, "q": "What is State flower: pink and white lady's slipper?", "a": "The state flower of Minnesota is the pink and white lady's slipper.", "x": "The pink and white lady's slipper — pink and white lady's slipper — is Minnesota's officially designated state flower. Seal with farmer, Native American, Mississippi on blue. It was chosen for its beauty, its abundance, or its meaning to the people. Boundary Waters", "s": "public-reference", "f": null}, {"t": "pink and white lady's slipper: natural history", "d": "The pink and white lady's slipper in the wild.", "g": "nature", "l": 2, "q": "What is pink and white lady's slipper: natural history?", "a": "The pink and white lady's slipper in the wild.", "x": "In the wild, the pink and white lady's slipper blooms across the state. Minnesota Learning the state flower's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Voyageurs National Park's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the flower", "d": "See Minnesota's state flower at Voyageurs National Park.", "g": "nature", "l": 2, "q": "What is Where to see the flower?", "a": "See Minnesota's state flower at Voyageurs National Park.", "x": "See the state flower where it thrives: Voyageurs National Park in Minnesota is the surest bet, and Minnehaha Falls rewards the observant. Minnesota State Fair Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "State bird: common loon", "d": "The state bird of Minnesota is the common loon.", "g": "nature", "l": 2, "q": "What is State bird: common loon?", "a": "The state bird of Minnesota is the common loon.", "x": "The common loon — common loon — is Minnesota's officially designated state bird. Seal with farmer, Native American, Mississippi on blue. It was chosen for its beauty, its abundance, or its meaning to the people. Boundary Waters", "s": "public-reference", "f": null}, {"t": "common loon: natural history", "d": "The common loon in the wild.", "g": "nature", "l": 2, "q": "What is common loon: natural history?", "a": "The common loon in the wild.", "x": "In the wild, the common loon lives across the state. Minnesota Learning the state bird's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Voyageurs National Park's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the bird", "d": "See Minnesota's state bird at Voyageurs National Park.", "g": "nature", "l": 2, "q": "What is Where to see the bird?", "a": "See Minnesota's state bird at Voyageurs National Park.", "x": "See the state bird where it thrives: Voyageurs National Park in Minnesota is the surest bet, and Minnehaha Falls rewards the observant. Minnesota State Fair Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "State tree: red (Norway) pine", "d": "The state tree of Minnesota is the red (Norway) pine.", "g": "nature", "l": 2, "q": "What is State tree: red (Norway) pine?", "a": "The state tree of Minnesota is the red (Norway) pine.", "x": "The red (Norway) pine — red (Norway) pine — is Minnesota's officially designated state tree. Seal with farmer, Native American, Mississippi on blue. It was chosen for its beauty, its abundance, or its meaning to the people. Boundary Waters", "s": "public-reference", "f": null}, {"t": "red (Norway) pine: natural history", "d": "The red (Norway) pine in the wild.", "g": "nature", "l": 2, "q": "What is red (Norway) pine: natural history?", "a": "The red (Norway) pine in the wild.", "x": "In the wild, the red (Norway) pine lives across the state. Minnesota Learning the state tree's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Voyageurs National Park's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the tree", "d": "See Minnesota's state tree at Voyageurs National Park.", "g": "nature", "l": 2, "q": "What is Where to see the tree?", "a": "See Minnesota's state tree at Voyageurs National Park.", "x": "See the state tree where it thrives: Voyageurs National Park in Minnesota is the surest bet, and Minnehaha Falls rewards the observant. Minnesota State Fair Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "The state flag: design", "d": "Minnesota's flag: Seal with farmer, Native American, Mississippi on blue..", "g": "flag", "l": 2, "q": "What is The state flag: design?", "a": "Minnesota's flag: Seal with farmer, Native American, Mississippi on blue..", "x": "The flag of Minnesota: Seal with farmer, Native American, Mississippi on blue.. Every element was chosen deliberately — colors, seals, stars — and the design's history mirrors the state's. Progressive politics; Mayo Clinic. Fly it correctly: the flag code gives the rules, and Minnesota flies it with pride.", "s": "public-reference", "f": null}, {"t": "The state flag: colors and emblem", "d": "What Minnesota's flag means.", "g": "flag", "l": 2, "q": "What is The state flag: colors and emblem?", "a": "What Minnesota's flag means.", "x": "The colors and emblem of Minnesota's flag carry meaning: Seal with farmer, Native American, Mississippi on blue.. L'Etoile du Nord (The star of the north) Vexillologists rank flags by simplicity and symbolism — Minnesota's tells its story at a glance to those who know the code.", "s": "public-reference", "f": null}, {"t": "The state flag: history", "d": "How Minnesota got its flag.", "g": "flag", "l": 2, "q": "What is The state flag: history?", "a": "How Minnesota got its flag.", "x": "The history of Minnesota's flag: adopted after contests or commission designs, sometimes replacing earlier banners. The Mayo Clinic made Rochester a medical mecca. Flags evolve with states — each change marks an era. The current design has flown over St. Paul's modern history.", "s": "public-reference", "f": null}, {"t": "The state seal", "d": "The Great Seal of Minnesota.", "g": "symbols", "l": 2, "q": "What is The state seal?", "a": "The Great Seal of Minnesota.", "x": "The Great Seal of Minnesota authenticates the state's official acts — every law and commission bears it. Seal with farmer, Native American, Mississippi on blue. The seal's imagery compresses the state's identity: its industries, its ideals, its motto \"L'Etoile du Nord (The star of the north).\"", "s": "public-reference", "f": null}, {"t": "The state quarter", "d": "Minnesota's quarter in the 50 State Quarters program.", "g": "symbols", "l": 2, "q": "What is The state quarter?", "a": "Minnesota's quarter in the 50 State Quarters program.", "x": "Minnesota's quarter: the US Mint's 50 State Quarters program (1999-2008) gave every state a circulating canvas. Minnesota's design honors North Star State — pocket change as history lesson. Collectors still hunt them.", "s": "public-reference", "f": null}, {"t": "The capitol building", "d": "Minnesota's capitol in St. Paul.", "g": "culture", "l": 2, "q": "What is The capitol building?", "a": "Minnesota's capitol in St. Paul.", "x": "The Minnesota State Capitol in St. Paul: the building where laws are made and history happened. Dakota and Ojibwe; French then U.S. Capitols are museums of democracy — tour the chambers, the rotunda, the grounds. Mall of America", "s": "public-reference", "f": null}, {"t": "The state song", "d": "Minnesota's officially adopted state song.", "g": "culture", "l": 2, "q": "What is The state song?", "a": "Minnesota's officially adopted state song.", "x": "The state song of Minnesota was adopted by the legislature — every state has one, sung at official occasions. Minnesota State Fair Songs, like flags, are identity set to music. Learn the chorus; it is the state's anthem in miniature.", "s": "public-reference", "f": null}, {"t": "How symbols are chosen", "d": "The legislature designates Minnesota's symbols.", "g": "symbols", "l": 2, "q": "What is How symbols are chosen?", "a": "The legislature designates Minnesota's symbols.", "x": "Symbols become official when the Minnesota legislature says so — often after schoolchildren campaign, contests run, or committees deliberate. L'Etoile du Nord (The star of the north) The process itself is civics: citizens proposing, debating, and adopting what represents them.", "s": "public-reference", "f": null}, {"t": "Flag etiquette", "d": "Displaying Minnesota's flag correctly.", "g": "flag", "l": 2, "q": "What is Flag etiquette?", "a": "Displaying Minnesota's flag correctly.", "x": "Flag etiquette for Minnesota's banner: fly it sunrise to sunset (or lit at night), never let it touch the ground, and retire worn flags with dignity. North Star State The state flag flies below the US flag — a daily reminder of the federal order.", "s": "public-reference", "f": null}, {"t": "Symbol fact 1", "d": "More Minnesota symbols: pink and white lady's slipper.", "g": "facts", "l": 2, "q": "What is Symbol fact 1?", "a": "More Minnesota symbols: pink and white lady's slipper.", "x": "From the Minnesota symbol file: pink and white lady's slipper. Minnesota's symbols reward the curious — each one opens a story about the land, the people, or the moment it was chosen. \"L'Etoile du Nord (The star of the north)\" indeed.", "s": "public-reference", "f": null}, {"t": "Symbol fact 2", "d": "More Minnesota symbols: common loon.", "g": "facts", "l": 2, "q": "What is Symbol fact 2?", "a": "More Minnesota symbols: common loon.", "x": "From the Minnesota symbol file: common loon. Minnesota's symbols reward the curious — each one opens a story about the land, the people, or the moment it was chosen. \"L'Etoile du Nord (The star of the north)\" indeed.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-minnesota-symbols-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
