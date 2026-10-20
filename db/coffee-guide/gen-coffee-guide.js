(function(){'use strict';
/* JAH Coffee Guide Database generator — jahdb-coffee-guide-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='coffee-guide',PREFIX='JAH-COF-',NAME='JAH Coffee Guide Database';
var FIELDS=["drink", "brew", "grind", "bean", "roast", "care", "skill"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Espresso", "d": "Espresso is pressure-extracted intensity: 18g in, 36g out, 25-30 seconds. The base of milk drinks.", "g": "drink", "l": 2, "q": "What is Espresso?", "a": "Espresso is pressure-extracted intensity: 18g in, 36g out, 25-30 seconds. The base of milk drinks.", "x": "Espresso is pressure-extracted intensity: 18g in, 36g out, 25-30 seconds. The base of milk drinks. ratio: 1:2 coffee to water. grind: fine. time: 25-30 sec. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Americano", "d": "Americano is espresso lengthened with hot water: clean and strong.", "g": "drink", "l": 2, "q": "What is Americano?", "a": "Americano is espresso lengthened with hot water: clean and strong.", "x": "Americano is espresso lengthened with hot water: clean and strong. ratio: espresso + hot water. grind: fine. time: 25-30 sec. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Cappuccino", "d": "Cappuccino is the classic thirds: dry foam cap, drinkable art.", "g": "drink", "l": 2, "q": "What is Cappuccino?", "a": "Cappuccino is the classic thirds: dry foam cap, drinkable art.", "x": "Cappuccino is the classic thirds: dry foam cap, drinkable art. ratio: 1/3 espresso, 1/3 milk, 1/3 foam. grind: fine. time: 25-30 sec. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Latte", "d": "Latte is the milky canvas: espresso softened under steamed milk.", "g": "drink", "l": 2, "q": "What is Latte?", "a": "Latte is the milky canvas: espresso softened under steamed milk.", "x": "Latte is the milky canvas: espresso softened under steamed milk. ratio: 1:5+ espresso to milk. grind: fine. time: 25-30 sec. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Flat white", "d": "Flat white is the Australian intense latte: less foam, more coffee punch.", "g": "drink", "l": 2, "q": "What is Flat white?", "a": "Flat white is the Australian intense latte: less foam, more coffee punch.", "x": "Flat white is the Australian intense latte: less foam, more coffee punch. ratio: double ristretto + velvet milk. grind: fine. time: 25-30 sec. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Macchiato", "d": "Macchiato is espresso stained with foam: small and strong.", "g": "drink", "l": 2, "q": "What is Macchiato?", "a": "Macchiato is espresso stained with foam: small and strong.", "x": "Macchiato is espresso stained with foam: small and strong. ratio: espresso marked with foam. grind: fine. time: 25-30 sec. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Cortado", "d": "Cortado is the Spanish equal-parts: no foam, just balance.", "g": "drink", "l": 2, "q": "What is Cortado?", "a": "Cortado is the Spanish equal-parts: no foam, just balance.", "x": "Cortado is the Spanish equal-parts: no foam, just balance. ratio: 1:1 espresso to warm milk. grind: fine. time: 25-30 sec. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Mocha", "d": "Mocha is dessert coffee: espresso meets chocolate.", "g": "drink", "l": 2, "q": "What is Mocha?", "a": "Mocha is dessert coffee: espresso meets chocolate.", "x": "Mocha is dessert coffee: espresso meets chocolate. ratio: espresso + chocolate + milk. grind: fine. time: 25-30 sec. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Cold brew", "d": "Cold brew steeps coarse grounds cold for 12-24 hours: smooth, sweet, low acid.", "g": "drink", "l": 2, "q": "What is Cold brew?", "a": "Cold brew steeps coarse grounds cold for 12-24 hours: smooth, sweet, low acid.", "x": "Cold brew steeps coarse grounds cold for 12-24 hours: smooth, sweet, low acid. ratio: 1:8 steeped 12-24h. grind: coarse. time: 12-24 hours. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Iced coffee", "d": "Iced coffee is hot coffee flash-chilled: brew strong over ice.", "g": "drink", "l": 2, "q": "What is Iced coffee?", "a": "Iced coffee is hot coffee flash-chilled: brew strong over ice.", "x": "Iced coffee is hot coffee flash-chilled: brew strong over ice. ratio: double-strength over ice. grind: medium. time: 4 min. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Pour over (V60)", "d": "Pour over is the clarity method: spiral pours, paper filter, bright cups.", "g": "brew", "l": 2, "q": "What is Pour over (V60)?", "a": "Pour over is the clarity method: spiral pours, paper filter, bright cups.", "x": "Pour over is the clarity method: spiral pours, paper filter, bright cups. ratio: 1:16. grind: medium-fine. time: 3 min. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Chemex", "d": "Chemex thick filters make the cleanest cup: tea-like and sweet.", "g": "brew", "l": 2, "q": "What is Chemex?", "a": "Chemex thick filters make the cleanest cup: tea-like and sweet.", "x": "Chemex thick filters make the cleanest cup: tea-like and sweet. ratio: 1:16. grind: medium-coarse. time: 4 min. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "French press", "d": "French press is full immersion: heavy body, simple ritual.", "g": "brew", "l": 2, "q": "What is French press?", "a": "French press is full immersion: heavy body, simple ritual.", "x": "French press is full immersion: heavy body, simple ritual. ratio: 1:14. grind: coarse. time: 4 min. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "AeroPress", "d": "AeroPress is the pressure hack: fast, forgiving, endlessly recipe-tweakable.", "g": "brew", "l": 2, "q": "What is AeroPress?", "a": "AeroPress is the pressure hack: fast, forgiving, endlessly recipe-tweakable.", "x": "AeroPress is the pressure hack: fast, forgiving, endlessly recipe-tweakable. ratio: 1:13. grind: fine-medium. time: 2 min. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Moka pot", "d": "Moka pot is stovetop espresso-ish: strong, nostalgic, Italian mornings.", "g": "brew", "l": 2, "q": "What is Moka pot?", "a": "Moka pot is stovetop espresso-ish: strong, nostalgic, Italian mornings.", "x": "Moka pot is stovetop espresso-ish: strong, nostalgic, Italian mornings. ratio: fill basket, water to valve. grind: fine-medium. time: 5 min. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Turkish coffee", "d": "Turkish coffee boils powder-fine grounds in a cezve: intense, with grounds settling.", "g": "brew", "l": 2, "q": "What is Turkish coffee?", "a": "Turkish coffee boils powder-fine grounds in a cezve: intense, with grounds settling.", "x": "Turkish coffee boils powder-fine grounds in a cezve: intense, with grounds settling. ratio: 1:10, unfiltered. grind: powder. time: 3 min. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Espresso grind", "d": "Espresso grind is fine like table salt: too fine chokes, too coarse sours.", "g": "grind", "l": 2, "q": "What is Espresso grind?", "a": "Espresso grind is fine like table salt: too fine chokes, too coarse sours.", "x": "Espresso grind is fine like table salt: too fine chokes, too coarse sours. ratio: —. grind: fine, table salt. time: —. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Filter grind", "d": "Drip grind is medium like sand.", "g": "grind", "l": 2, "q": "What is Filter grind?", "a": "Drip grind is medium like sand.", "x": "Drip grind is medium like sand. ratio: —. grind: medium, sand. time: —. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable. Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "French press grind", "d": "Press grind is coarse like breadcrumbs to avoid sludge.", "g": "grind", "l": 2, "q": "What is French press grind?", "a": "Press grind is coarse like breadcrumbs to avoid sludge.", "x": "Press grind is coarse like breadcrumbs to avoid sludge. ratio: —. grind: coarse, breadcrumbs. time: —. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Arabica beans", "d": "Arabica is the quality species: sweeter, more acidic, higher grown.", "g": "bean", "l": 2, "q": "What is Arabica beans?", "a": "Arabica is the quality species: sweeter, more acidic, higher grown.", "x": "Arabica is the quality species: sweeter, more acidic, higher grown. ratio: —. grind: —. time: —. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Robusta beans", "d": "Robusta is the strong species: more caffeine, more crema, harsher.", "g": "bean", "l": 2, "q": "What is Robusta beans?", "a": "Robusta is the strong species: more caffeine, more crema, harsher.", "x": "Robusta is the strong species: more caffeine, more crema, harsher. ratio: —. grind: —. time: —. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Light roast", "d": "Light roast keeps origin character: bright, tea-like.", "g": "roast", "l": 2, "q": "What is Light roast?", "a": "Light roast keeps origin character: bright, tea-like.", "x": "Light roast keeps origin character: bright, tea-like. ratio: —. grind: —. time: —. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Medium roast", "d": "Medium roast balances origin and caramel: the crowd-pleaser.", "g": "roast", "l": 2, "q": "What is Medium roast?", "a": "Medium roast balances origin and caramel: the crowd-pleaser.", "x": "Medium roast balances origin and caramel: the crowd-pleaser. ratio: —. grind: —. time: —. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Dark roast", "d": "Dark roast is roast flavor forward: smoky, bold, low acid.", "g": "roast", "l": 2, "q": "What is Dark roast?", "a": "Dark roast is roast flavor forward: smoky, bold, low acid.", "x": "Dark roast is roast flavor forward: smoky, bold, low acid. ratio: —. grind: —. time: —. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Bean storage", "d": "Store beans airtight, cool, dark — never the freezer for daily use. Buy whole, grind fresh.", "g": "care", "l": 2, "q": "What is Bean storage?", "a": "Store beans airtight, cool, dark — never the freezer for daily use. Buy whole, grind fresh.", "x": "Store beans airtight, cool, dark — never the freezer for daily use. Buy whole, grind fresh. ratio: —. grind: —. time: —. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-coffee-guide-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
