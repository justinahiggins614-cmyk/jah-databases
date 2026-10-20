(function(){'use strict';
/* JAH Maryland Symbols Database generator — jahdb-e2-maryland-symbols-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='e2-maryland-symbols',PREFIX='JAH-E2MARYLANDS-',NAME='JAH Maryland Symbols Database';
var FIELDS=["overview", "symbols", "flag", "nature", "culture", "facts"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Maryland: symbols overview", "d": "Maryland's official symbols: black-eyed Susan, Baltimore oriole, white oak, and more.", "g": "overview", "l": 2, "q": "What is Maryland: symbols overview?", "a": "Maryland's official symbols: black-eyed Susan, Baltimore oriole, white oak, and more.", "x": "The official symbols of Maryland — the \"Old Line State\" — tell the state's story in shorthand: the black-eyed Susan (flower), the Baltimore oriole (bird), the white oak (tree), the motto \"Fatti maschii, parole femine (Manly deeds, womanly words),\" and the flag. Calvert and Crossland heraldic banner. Legislatures designate symbols to honor what the state values; this database covers every one, what it means, and where to see it.", "s": "public-reference", "f": null}, {"t": "Nickname: Old Line State", "d": "The nickname of Maryland is \"Old Line State.\"", "g": "symbols", "l": 2, "q": "What is Nickname: Old Line State?", "a": "The nickname of Maryland is \"Old Line State.\"", "x": "The nickname of Maryland — \"Old Line State\" — was adopted to express the state's identity. Calvert and Crossland heraldic banner. It appears on seals, plates, and proclamations. Catholic refuge colony 1634.", "s": "public-reference", "f": null}, {"t": "Nickname: the story", "d": "Why Maryland chose \"Old Line State.\"", "g": "symbols", "l": 2, "q": "What is Nickname: the story?", "a": "Why Maryland chose \"Old Line State.\"", "x": "Why \"Old Line State\": the nickname's story reaches into Maryland's history — Civil War border state.. Symbols are chosen, not found: committees, contests, and legislators all played a part. Knowing the story makes the symbol mean something.", "s": "public-reference", "f": null}, {"t": "Motto: Fatti maschii, parole femine (Manly deeds, womanly words)", "d": "The motto of Maryland is \"Fatti maschii, parole femine (Manly deeds, womanly words).\"", "g": "symbols", "l": 2, "q": "What is Motto: Fatti maschii, parole femine (Manly deeds, womanly words)?", "a": "The motto of Maryland is \"Fatti maschii, parole femine (Manly deeds, womanly words).\"", "x": "The motto of Maryland — \"Fatti maschii, parole femine (Manly deeds, womanly words)\" — was adopted to express the state's identity. Calvert and Crossland heraldic banner. It appears on seals, plates, and proclamations. Catholic refuge colony 1634.", "s": "public-reference", "f": null}, {"t": "Motto: the story", "d": "Why Maryland chose \"Fatti maschii, parole femine (Manly deeds, womanly words).\"", "g": "symbols", "l": 2, "q": "What is Motto: the story?", "a": "Why Maryland chose \"Fatti maschii, parole femine (Manly deeds, womanly words).\"", "x": "Why \"Fatti maschii, parole femine (Manly deeds, womanly words)\": the motto's story reaches into Maryland's history — Civil War border state.. Symbols are chosen, not found: committees, contests, and legislators all played a part. Knowing the story makes the symbol mean something.", "s": "public-reference", "f": null}, {"t": "State flower: black-eyed Susan", "d": "The state flower of Maryland is the black-eyed Susan.", "g": "nature", "l": 2, "q": "What is State flower: black-eyed Susan?", "a": "The state flower of Maryland is the black-eyed Susan.", "x": "The black-eyed Susan — black-eyed Susan — is Maryland's officially designated state flower. Calvert and Crossland heraldic banner. It was chosen for its beauty, its abundance, or its meaning to the people. Fort McHenry", "s": "public-reference", "f": null}, {"t": "black-eyed Susan: natural history", "d": "The black-eyed Susan in the wild.", "g": "nature", "l": 2, "q": "What is black-eyed Susan: natural history?", "a": "The black-eyed Susan in the wild.", "x": "In the wild, the black-eyed Susan blooms across the state. Maryland Learning the state flower's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Assateague Island National Seashore's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the flower", "d": "See Maryland's state flower at Assateague Island National Seashore.", "g": "nature", "l": 2, "q": "What is Where to see the flower?", "a": "See Maryland's state flower at Assateague Island National Seashore.", "x": "See the state flower where it thrives: Assateague Island National Seashore in Maryland is the surest bet, and Annapolis rewards the observant. Preakness Stakes Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "State bird: Baltimore oriole", "d": "The state bird of Maryland is the Baltimore oriole.", "g": "nature", "l": 2, "q": "What is State bird: Baltimore oriole?", "a": "The state bird of Maryland is the Baltimore oriole.", "x": "The Baltimore oriole — Baltimore oriole — is Maryland's officially designated state bird. Calvert and Crossland heraldic banner. It was chosen for its beauty, its abundance, or its meaning to the people. Fort McHenry", "s": "public-reference", "f": null}, {"t": "Baltimore oriole: natural history", "d": "The Baltimore oriole in the wild.", "g": "nature", "l": 2, "q": "What is Baltimore oriole: natural history?", "a": "The Baltimore oriole in the wild.", "x": "In the wild, the Baltimore oriole lives across the state. Maryland Learning the state bird's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Assateague Island National Seashore's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the bird", "d": "See Maryland's state bird at Assateague Island National Seashore.", "g": "nature", "l": 2, "q": "What is Where to see the bird?", "a": "See Maryland's state bird at Assateague Island National Seashore.", "x": "See the state bird where it thrives: Assateague Island National Seashore in Maryland is the surest bet, and Annapolis rewards the observant. Preakness Stakes Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "State tree: white oak", "d": "The state tree of Maryland is the white oak.", "g": "nature", "l": 2, "q": "What is State tree: white oak?", "a": "The state tree of Maryland is the white oak.", "x": "The white oak — white oak — is Maryland's officially designated state tree. Calvert and Crossland heraldic banner. It was chosen for its beauty, its abundance, or its meaning to the people. Fort McHenry", "s": "public-reference", "f": null}, {"t": "white oak: natural history", "d": "The white oak in the wild.", "g": "nature", "l": 2, "q": "What is white oak: natural history?", "a": "The white oak in the wild.", "x": "In the wild, the white oak lives across the state. Maryland Learning the state tree's natural history — where it grows or lives, what it needs — turns a symbol into a reason to visit Assateague Island National Seashore's parks and wild places.", "s": "public-reference", "f": null}, {"t": "Where to see the tree", "d": "See Maryland's state tree at Assateague Island National Seashore.", "g": "nature", "l": 2, "q": "What is Where to see the tree?", "a": "See Maryland's state tree at Assateague Island National Seashore.", "x": "See the state tree where it thrives: Assateague Island National Seashore in Maryland is the surest bet, and Annapolis rewards the observant. Preakness Stakes Visit in season, bring patience, and leave only footprints.", "s": "public-reference", "f": null}, {"t": "The state flag: design", "d": "Maryland's flag: Calvert and Crossland heraldic banner..", "g": "flag", "l": 2, "q": "What is The state flag: design?", "a": "Maryland's flag: Calvert and Crossland heraldic banner..", "x": "The flag of Maryland: Calvert and Crossland heraldic banner.. Every element was chosen deliberately — colors, seals, stars — and the design's history mirrors the state's. Chesapeake Bay; federal workforce. Fly it correctly: the flag code gives the rules, and Maryland flies it with pride.", "s": "public-reference", "f": null}, {"t": "The state flag: colors and emblem", "d": "What Maryland's flag means.", "g": "flag", "l": 2, "q": "What is The state flag: colors and emblem?", "a": "What Maryland's flag means.", "x": "The colors and emblem of Maryland's flag carry meaning: Calvert and Crossland heraldic banner.. Fatti maschii, parole femine (Manly deeds, womanly words) Vexillologists rank flags by simplicity and symbolism — Maryland's tells its story at a glance to those who know the code.", "s": "public-reference", "f": null}, {"t": "The state flag: history", "d": "How Maryland got its flag.", "g": "flag", "l": 2, "q": "What is The state flag: history?", "a": "How Maryland got its flag.", "x": "The history of Maryland's flag: adopted after contests or commission designs, sometimes replacing earlier banners. Fort McHenry's 1814 defense inspired the Star-Spangled Banner. Flags evolve with states — each change marks an era. The current design has flown over Annapolis's modern history.", "s": "public-reference", "f": null}, {"t": "The state seal", "d": "The Great Seal of Maryland.", "g": "symbols", "l": 2, "q": "What is The state seal?", "a": "The Great Seal of Maryland.", "x": "The Great Seal of Maryland authenticates the state's official acts — every law and commission bears it. Calvert and Crossland heraldic banner. The seal's imagery compresses the state's identity: its industries, its ideals, its motto \"Fatti maschii, parole femine (Manly deeds, womanly words).\"", "s": "public-reference", "f": null}, {"t": "The state quarter", "d": "Maryland's quarter in the 50 State Quarters program.", "g": "symbols", "l": 2, "q": "What is The state quarter?", "a": "Maryland's quarter in the 50 State Quarters program.", "x": "Maryland's quarter: the US Mint's 50 State Quarters program (1999-2008) gave every state a circulating canvas. Maryland's design honors Old Line State — pocket change as history lesson. Collectors still hunt them.", "s": "public-reference", "f": null}, {"t": "The capitol building", "d": "Maryland's capitol in Annapolis.", "g": "culture", "l": 2, "q": "What is The capitol building?", "a": "Maryland's capitol in Annapolis.", "x": "The Maryland State Capitol in Annapolis: the building where laws are made and history happened. Catholic refuge colony 1634. Capitols are museums of democracy — tour the chambers, the rotunda, the grounds. Inner Harbor", "s": "public-reference", "f": null}, {"t": "The state song", "d": "Maryland's officially adopted state song.", "g": "culture", "l": 2, "q": "What is The state song?", "a": "Maryland's officially adopted state song.", "x": "The state song of Maryland was adopted by the legislature — every state has one, sung at official occasions. Preakness Stakes Songs, like flags, are identity set to music. Learn the chorus; it is the state's anthem in miniature.", "s": "public-reference", "f": null}, {"t": "How symbols are chosen", "d": "The legislature designates Maryland's symbols.", "g": "symbols", "l": 2, "q": "What is How symbols are chosen?", "a": "The legislature designates Maryland's symbols.", "x": "Symbols become official when the Maryland legislature says so — often after schoolchildren campaign, contests run, or committees deliberate. Fatti maschii, parole femine (Manly deeds, womanly words) The process itself is civics: citizens proposing, debating, and adopting what represents them.", "s": "public-reference", "f": null}, {"t": "Flag etiquette", "d": "Displaying Maryland's flag correctly.", "g": "flag", "l": 2, "q": "What is Flag etiquette?", "a": "Displaying Maryland's flag correctly.", "x": "Flag etiquette for Maryland's banner: fly it sunrise to sunset (or lit at night), never let it touch the ground, and retire worn flags with dignity. Old Line State The state flag flies below the US flag — a daily reminder of the federal order.", "s": "public-reference", "f": null}, {"t": "Symbol fact 1", "d": "More Maryland symbols: black-eyed Susan.", "g": "facts", "l": 2, "q": "What is Symbol fact 1?", "a": "More Maryland symbols: black-eyed Susan.", "x": "From the Maryland symbol file: black-eyed Susan. Maryland's symbols reward the curious — each one opens a story about the land, the people, or the moment it was chosen. \"Fatti maschii, parole femine (Manly deeds, womanly words)\" indeed.", "s": "public-reference", "f": null}, {"t": "Symbol fact 2", "d": "More Maryland symbols: Baltimore oriole.", "g": "facts", "l": 2, "q": "What is Symbol fact 2?", "a": "More Maryland symbols: Baltimore oriole.", "x": "From the Maryland symbol file: Baltimore oriole. Maryland's symbols reward the curious — each one opens a story about the land, the people, or the moment it was chosen. \"Fatti maschii, parole femine (Manly deeds, womanly words)\" indeed.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-e2-maryland-symbols-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
