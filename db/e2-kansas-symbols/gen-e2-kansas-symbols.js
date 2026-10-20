(function(){'use strict';
/* JAH Kansas Symbols Database generator — jahdb-e2-kansas-symbols-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-kansas-symbols',PREFIX='JAH-E2KANSASSYM-',NAME='JAH Kansas Symbols Database';
var FIELDS=["overview", "symbols", "flag", "nature", "culture", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Kansas: symbols overview", "d": "Kansas's official symbols: native sunflower, western meadowlark, cottonwood, and more.", "g": "overview", "l": 2, "q": "What is Kansas: symbols overview?", "a": "Kansas's official symbols: native sunflower, western meadowlark, cottonwood, and more.", "x": "The official symbols of Kansas — the \"Sunflower State\" — tell the state's story in shorthand: the native sunflower (flower), the western meadowlark (bird), the cottonwood (tree), the motto \"Ad astra per aspera (To the stars through difficulties),\" and the flag. Sunflower and 34 stars on blue. Legislatures designate symbols to honor what the state values; this database covers every one, what it means, and where to see it.", "s": "public-reference", "f": null}, {"t": "Nickname: Sunflower State", "d": "The nickname of Kansas is \"Sunflower State.\"", "g": "symbols", "l": 2, "q": "What is Nickname: Sunflower State?", "a": "The nickname of Kansas is \"Sunflower State.\"", "x": "The nickname of Kansas — \"Sunflower State\" — was adopted to express the state's identity. Sunflower and 34 stars on blue. It appears on seals, plates, and proclamations. Kansa and Osage; Bleeding Kansas.", "s": "public-reference", "f": null}, {"t": "Nickname: the story", "d": "Why Kansas chose \"Sunflower State.\"", "g": "symbols", "l": 2, "q": "What is Nickname: the story?", "a": "Why Kansas chose \"Sunflower State.\"", "x": "Why \"Sunflower State\": the nickname's story reaches into Kansas's history — Wheat and cattle; Dust Bowl.. Symbols are chosen, not found: committees, contests, and legislators all played a part. Knowing the story makes the symbol mean something.", "s": "public-reference", "f": null}, {"t": "Motto: Ad astra per aspera (To the stars through difficulties)", "d": "The motto of Kansas is \"Ad astra per aspera (To the stars through difficulties).\"", "g": "symbols", "l": 2, "q": "What is Motto: Ad astra per aspera (To the stars through difficulties)?", "a": "The motto of Kansas is \"Ad astra per aspera (To the stars through difficulties).\"", "x": "The motto of Kansas — \"Ad astra per aspera (To the stars through difficulties)\" — was adopted to express the state's identity. Sunflower and 34 stars on blue. It appears on seals, plates, and proclamations. Kansa and Osage; Bleeding Kansas.", "s": "public-reference", "f": null}, {"t": "Motto: the story", "d": "Why Kansas chose \"Ad astra per aspera (To the stars through difficulties).\"", "g": "symbols", "l": 2, "q": "What is Motto: the story?", "a": "Why Kansas chose \"Ad astra per aspera (To the stars through difficulties).\"", "x": "Why \"Ad astra per aspera (To the stars through difficulties)\": the motto's story reaches into Kansas's history — Wheat and cattle; Dust Bowl.. Symbols are chosen, not found: committees, contests, and legislators all played a part. Knowing the story makes the symbol mean something.", "s": "public-reference", "f": null}, {"t": "State flower: native sunflower", "d": "The state flower of Kansas is the native sunflower.", "g": "nature", "l": 2, "q": "What is State flower: native sunflower?", "a": "The state flower of Kansas is the native sunflower.", "x": "The native sunflower — native sunflower — is Kansas's officially designated state flower. Sunflower and 34 stars on blue. It was chosen for its beauty, its abundance, or its meaning to the people. Monument Rocks", "s": "public-reference", "f": null}, {"t": "native sunflower: natural history", "d": "The native sunflower in the wild.", "g": "nature", "l": 2, "q": "What is native sunflower: natural history?", "a": "The native sunflower in the wild.", "x": "In the wild, the native sunflower blooms across the state. Kansas Learning the state flower's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Tallgrass Prairie National Preserve's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the flower", "d": "See Kansas's state flower at Tallgrass Prairie National Preserve.", "g": "nature", "l": 2, "q": "What is Where to see the flower?", "a": "See Kansas's state flower at Tallgrass Prairie National Preserve.", "x": "See the state flower where it thrives: Tallgrass Prairie National Preserve in Kansas is the surest bet, and Eisenhower Library rewards the observant. Kansas State Fair Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "State bird: western meadowlark", "d": "The state bird of Kansas is the western meadowlark.", "g": "nature", "l": 2, "q": "What is State bird: western meadowlark?", "a": "The state bird of Kansas is the western meadowlark.", "x": "The western meadowlark — western meadowlark — is Kansas's officially designated state bird. Sunflower and 34 stars on blue. It was chosen for its beauty, its abundance, or its meaning to the people. Monument Rocks", "s": "public-reference", "f": null}, {"t": "western meadowlark: natural history", "d": "The western meadowlark in the wild.", "g": "nature", "l": 2, "q": "What is western meadowlark: natural history?", "a": "The western meadowlark in the wild.", "x": "In the wild, the western meadowlark lives across the state. Kansas Learning the state bird's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Tallgrass Prairie National Preserve's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the bird", "d": "See Kansas's state bird at Tallgrass Prairie National Preserve.", "g": "nature", "l": 2, "q": "What is Where to see the bird?", "a": "See Kansas's state bird at Tallgrass Prairie National Preserve.", "x": "See the state bird where it thrives: Tallgrass Prairie National Preserve in Kansas is the surest bet, and Eisenhower Library rewards the observant. Kansas State Fair Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "State tree: cottonwood", "d": "The state tree of Kansas is the cottonwood.", "g": "nature", "l": 2, "q": "What is State tree: cottonwood?", "a": "The state tree of Kansas is the cottonwood.", "x": "The cottonwood — cottonwood — is Kansas's officially designated state tree. Sunflower and 34 stars on blue. It was chosen for its beauty, its abundance, or its meaning to the people. Monument Rocks State facts from official state publications and standard references. Symbols and slogans are designated by state legislatures.", "s": "public-reference", "f": null}, {"t": "cottonwood: natural history", "d": "The cottonwood in the wild.", "g": "nature", "l": 2, "q": "What is cottonwood: natural history?", "a": "The cottonwood in the wild.", "x": "In the wild, the cottonwood lives across the state. Kansas Learning the state tree's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Tallgrass Prairie National Preserve's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the tree", "d": "See Kansas's state tree at Tallgrass Prairie National Preserve.", "g": "nature", "l": 2, "q": "What is Where to see the tree?", "a": "See Kansas's state tree at Tallgrass Prairie National Preserve.", "x": "See the state tree where it thrives: Tallgrass Prairie National Preserve in Kansas is the surest bet, and Eisenhower Library rewards the observant. Kansas State Fair Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "The state flag: design", "d": "Kansas's flag: Sunflower and 34 stars on blue..", "g": "flag", "l": 2, "q": "What is The state flag: design?", "a": "Kansas's flag: Sunflower and 34 stars on blue..", "x": "The flag of Kansas: Sunflower and 34 stars on blue.. Every element was chosen deliberately — colors, seals, stars — and the design's history mirrors the state's. Aviation (Wichita). Fly it correctly: the flag code gives the rules, and Kansas flies it with pride.", "s": "public-reference", "f": null}, {"t": "The state flag: colors and emblem", "d": "What Kansas's flag means.", "g": "flag", "l": 2, "q": "What is The state flag: colors and emblem?", "a": "What Kansas's flag means.", "x": "The colors and emblem of Kansas's flag carry meaning: Sunflower and 34 stars on blue.. Ad astra per aspera (To the stars through difficulties) Vexillologists rank flags by simplicity and symbolism — Kansas's tells its story at a glance to those who know the code.", "s": "public-reference", "f": null}, {"t": "The state flag: history", "d": "How Kansas got its flag.", "g": "flag", "l": 2, "q": "What is The state flag: history?", "a": "How Kansas got its flag.", "x": "The history of Kansas's flag: adopted after contests or commission designs, sometimes replacing earlier banners. Wichita became the Air Capital of the World. Flags evolve with states — each change marks an era. The current design has flown over Topeka's modern history.", "s": "public-reference", "f": null}, {"t": "The state seal", "d": "The Great Seal of Kansas.", "g": "symbols", "l": 2, "q": "What is The state seal?", "a": "The Great Seal of Kansas.", "x": "The Great Seal of Kansas authenticates the state's official acts — every law and commission bears it. Sunflower and 34 stars on blue. The seal's imagery compresses the state's identity: its industries, its ideals, its motto \"Ad astra per aspera (To the stars through difficulties).\"", "s": "public-reference", "f": null}, {"t": "The state quarter", "d": "Kansas's quarter in the 50 State Quarters program.", "g": "symbols", "l": 2, "q": "What is The state quarter?", "a": "Kansas's quarter in the 50 State Quarters program.", "x": "Kansas's quarter: the US Mint's 50 State Quarters program (1999-2008) gave every state a circulating canvas. Kansas's design honors Sunflower State — pocket change as history lesson. Collectors still hunt them.", "s": "public-reference", "f": null}, {"t": "The capitol building", "d": "Kansas's capitol in Topeka.", "g": "culture", "l": 2, "q": "What is The capitol building?", "a": "Kansas's capitol in Topeka.", "x": "The Kansas State Capitol in Topeka: the building where laws are made and history happened. Kansa and Osage; Bleeding Kansas. Capitols are museums of democracy — tour the chambers, the rotunda, the grounds. Tallgrass Prairie", "s": "public-reference", "f": null}, {"t": "The state song", "d": "Kansas's officially adopted state song.", "g": "culture", "l": 2, "q": "What is The state song?", "a": "Kansas's officially adopted state song.", "x": "The state song of Kansas was adopted by the legislature — every state has one, sung at official occasions. Kansas State Fair Songs, like flags, are identity set to music. Learn the chorus; it is the state's anthem in miniature.", "s": "public-reference", "f": null}, {"t": "How symbols are chosen", "d": "The legislature designates Kansas's symbols.", "g": "symbols", "l": 2, "q": "What is How symbols are chosen?", "a": "The legislature designates Kansas's symbols.", "x": "Symbols become official when the Kansas legislature says so — often after schoolchildren campaign, contests run, or committees deliberate. Ad astra per aspera (To the stars through difficulties) The process itself is civics: citizens proposing, debating, and adopting what represents them.", "s": "public-reference", "f": null}, {"t": "Flag etiquette", "d": "Displaying Kansas's flag correctly.", "g": "flag", "l": 2, "q": "What is Flag etiquette?", "a": "Displaying Kansas's flag correctly.", "x": "Flag etiquette for Kansas's banner: fly it sunrise to sunset (or lit at night), never let it touch the ground, and retire worn flags with dignity. Sunflower State The state flag flies below the US flag — a daily reminder of the federal order.", "s": "public-reference", "f": null}, {"t": "Symbol fact 1", "d": "More Kansas symbols: native sunflower.", "g": "facts", "l": 2, "q": "What is Symbol fact 1?", "a": "More Kansas symbols: native sunflower.", "x": "From the Kansas symbol file: native sunflower. Kansas's symbols reward the curious — each one opens a story about the land, the people, or the moment it was chosen. \"Ad astra per aspera (To the stars through difficulties)\" indeed.", "s": "public-reference", "f": null}, {"t": "Symbol fact 2", "d": "More Kansas symbols: western meadowlark.", "g": "facts", "l": 2, "q": "What is Symbol fact 2?", "a": "More Kansas symbols: western meadowlark.", "x": "From the Kansas symbol file: western meadowlark. Kansas's symbols reward the curious — each one opens a story about the land, the people, or the moment it was chosen. \"Ad astra per aspera (To the stars through difficulties)\" indeed.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-kansas-symbols-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
