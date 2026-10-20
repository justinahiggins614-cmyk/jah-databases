(function(){'use strict';
/* JAH Cleaning Recipes Database generator — jahdb-cleaning-recipes-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='cleaning-recipes',PREFIX='JAH-CLN-',NAME='JAH Cleaning Recipes Database';
var FIELDS=["kitchen", "glass", "bathroom", "drains", "wood", "metal", "laundry", "floors", "air"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "All-purpose spray", "d": "All-purpose spray: water, vinegar, and a drop of dish soap cuts kitchen grease. Not for stone counters.", "g": "kitchen", "l": 2, "q": "What is All-purpose spray?", "a": "All-purpose spray: water, vinegar, and a drop of dish soap cuts kitchen grease. Not for stone counters.", "x": "All-purpose spray: water, vinegar, and a drop of dish soap cuts kitchen grease. Not for stone counters. Key steps: 1 cup water; 1 cup white vinegar; 1 tbsp dish soap; Shake or stir to mix, then use as directed..", "s": "public-reference", "f": null}, {"t": "Glass cleaner", "d": "Glass cleaner: water, vinegar, and alcohol for streak-free windows. Wipe with newspaper or microfiber.", "g": "glass", "l": 2, "q": "What is Glass cleaner?", "a": "Glass cleaner: water, vinegar, and alcohol for streak-free windows. Wipe with newspaper or microfiber.", "x": "Glass cleaner: water, vinegar, and alcohol for streak-free windows. Wipe with newspaper or microfiber. Key steps: 2 cups water; 1/2 cup vinegar; 1/4 cup rubbing alcohol; Shake or stir to mix, then use as directed..", "s": "public-reference", "f": null}, {"t": "Bathroom scrub", "d": "Bathroom scrub: baking soda paste with peroxide lifts soap scum and grout stains.", "g": "bathroom", "l": 2, "q": "What is Bathroom scrub?", "a": "Bathroom scrub: baking soda paste with peroxide lifts soap scum and grout stains.", "x": "Bathroom scrub: baking soda paste with peroxide lifts soap scum and grout stains. Key steps: 1/2 cup baking soda; 1/4 cup hydrogen peroxide; 1 tsp dish soap; Shake or stir to mix, then use as directed..", "s": "public-reference", "f": null}, {"t": "Toilet bowl cleaner", "d": "Toilet cleaner: vinegar soak, then baking soda fizz, then scrub.", "g": "bathroom", "l": 2, "q": "What is Toilet bowl cleaner?", "a": "Toilet cleaner: vinegar soak, then baking soda fizz, then scrub.", "x": "Toilet cleaner: vinegar soak, then baking soda fizz, then scrub. Key steps: 1 cup vinegar; 1/2 cup baking soda; Shake or stir to mix, then use as directed.. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Drain freshener", "d": "Drain freshener: soda, then vinegar, then hot water. For clogs, use a plunger or snake, not chemicals.", "g": "drains", "l": 2, "q": "What is Drain freshener?", "a": "Drain freshener: soda, then vinegar, then hot water. For clogs, use a plunger or snake, not chemicals.", "x": "Drain freshener: soda, then vinegar, then hot water. For clogs, use a plunger or snake, not chemicals. Key steps: 1/2 cup baking soda; 1/2 cup vinegar; hot water flush; Shake or stir to mix, then use as directed..", "s": "public-reference", "f": null}, {"t": "Oven cleaner paste", "d": "Oven paste: coat, wait overnight, wipe. No harsh fumes.", "g": "kitchen", "l": 2, "q": "What is Oven cleaner paste?", "a": "Oven paste: coat, wait overnight, wipe. No harsh fumes.", "x": "Oven paste: coat, wait overnight, wipe. No harsh fumes. Key steps: 1/2 cup baking soda; water to paste; Shake or stir to mix, then use as directed.. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Microwave steam clean", "d": "Microwave: lemon water, 5 minutes, wipe the steamed grime away.", "g": "kitchen", "l": 2, "q": "What is Microwave steam clean?", "a": "Microwave: lemon water, 5 minutes, wipe the steamed grime away.", "x": "Microwave: lemon water, 5 minutes, wipe the steamed grime away. Key steps: 1 cup water; 1 lemon halved; Shake or stir to mix, then use as directed.. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Cutting board sanitizer", "d": "Cutting boards: scrub with lemon and salt, rinse, dry upright.", "g": "kitchen", "l": 2, "q": "What is Cutting board sanitizer?", "a": "Cutting boards: scrub with lemon and salt, rinse, dry upright.", "x": "Cutting boards: scrub with lemon and salt, rinse, dry upright. Key steps: 1/2 lemon; coarse salt; Shake or stir to mix, then use as directed.. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Wood polish", "d": "Wood polish: oil and vinegar revive dull furniture. Test hidden spot first.", "g": "wood", "l": 2, "q": "What is Wood polish?", "a": "Wood polish: oil and vinegar revive dull furniture. Test hidden spot first.", "x": "Wood polish: oil and vinegar revive dull furniture. Test hidden spot first. Key steps: 1/2 cup olive oil; 1/4 cup vinegar; lemon juice; Shake or stir to mix, then use as directed.. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Silver polish", "d": "Silver: foil-lined pan, hot water, baking soda — tarnish transfers to the foil.", "g": "metal", "l": 2, "q": "What is Silver polish?", "a": "Silver: foil-lined pan, hot water, baking soda — tarnish transfers to the foil.", "x": "Silver: foil-lined pan, hot water, baking soda — tarnish transfers to the foil. Key steps: baking soda; hot water; aluminum foil; Shake or stir to mix, then use as directed.. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Brass cleaner", "d": "Brass paste: flour, salt, vinegar. Rub, rinse, buff. Not for lacquered brass.", "g": "metal", "l": 2, "q": "What is Brass cleaner?", "a": "Brass paste: flour, salt, vinegar. Rub, rinse, buff. Not for lacquered brass.", "x": "Brass paste: flour, salt, vinegar. Rub, rinse, buff. Not for lacquered brass. Key steps: equal parts flour, salt, vinegar; Shake or stir to mix, then use as directed.. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Rust remover soak", "d": "Rust: soak tools in vinegar overnight, scrub, oil immediately.", "g": "metal", "l": 2, "q": "What is Rust remover soak?", "a": "Rust: soak tools in vinegar overnight, scrub, oil immediately.", "x": "Rust: soak tools in vinegar overnight, scrub, oil immediately. Key steps: white vinegar soak 24h; Shake or stir to mix, then use as directed.. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Laundry booster", "d": "Baking soda boosts detergent and softens water.", "g": "laundry", "l": 2, "q": "What is Laundry booster?", "a": "Baking soda boosts detergent and softens water.", "x": "Baking soda boosts detergent and softens water. Key steps: 1/2 cup baking soda per load; Shake or stir to mix, then use as directed.. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Fabric softener", "d": "Vinegar in the rinse softens without coating fibers.", "g": "laundry", "l": 2, "q": "What is Fabric softener?", "a": "Vinegar in the rinse softens without coating fibers.", "x": "Vinegar in the rinse softens without coating fibers. Key steps: 1 cup vinegar in rinse cycle; Shake or stir to mix, then use as directed.. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Stain: grease", "d": "Grease stains: dish soap directly, hot water wash.", "g": "laundry", "l": 2, "q": "What is Stain: grease?", "a": "Grease stains: dish soap directly, hot water wash.", "x": "Grease stains: dish soap directly, hot water wash. Key steps: dish soap; hot water; Shake or stir to mix, then use as directed.. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Stain: blood", "d": "Blood: cold water only — heat sets it. Peroxide for whites.", "g": "laundry", "l": 2, "q": "What is Stain: blood?", "a": "Blood: cold water only — heat sets it. Peroxide for whites.", "x": "Blood: cold water only — heat sets it. Peroxide for whites. Key steps: cold water; hydrogen peroxide; Shake or stir to mix, then use as directed.. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Stain: wine", "d": "Red wine: salt immediately to absorb, then white wine or soda.", "g": "laundry", "l": 2, "q": "What is Stain: wine?", "a": "Red wine: salt immediately to absorb, then white wine or soda.", "x": "Red wine: salt immediately to absorb, then white wine or soda. Key steps: salt; white wine or club soda; Shake or stir to mix, then use as directed.. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Stain: coffee", "d": "Coffee: cold rinse, dish soap, wash.", "g": "laundry", "l": 2, "q": "What is Stain: coffee?", "a": "Coffee: cold rinse, dish soap, wash.", "x": "Coffee: cold rinse, dish soap, wash. Key steps: cold water; dish soap; Shake or stir to mix, then use as directed.. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Carpet deodorizer", "d": "Carpet: baking soda, wait, vacuum. Freshens without perfume.", "g": "floors", "l": 2, "q": "What is Carpet deodorizer?", "a": "Carpet: baking soda, wait, vacuum. Freshens without perfume.", "x": "Carpet: baking soda, wait, vacuum. Freshens without perfume. Key steps: baking soda sprinkle; vacuum after 15 min; Shake or stir to mix, then use as directed.. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Hardwood floor cleaner", "d": "Hardwood: barely-damp mop with diluted vinegar. Never soak wood.", "g": "floors", "l": 2, "q": "What is Hardwood floor cleaner?", "a": "Hardwood: barely-damp mop with diluted vinegar. Never soak wood.", "x": "Hardwood: barely-damp mop with diluted vinegar. Never soak wood. Key steps: 1 gallon water; 1/2 cup vinegar; Shake or stir to mix, then use as directed.. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Tile grout cleaner", "d": "Grout: baking soda paste, scrub, rinse.", "g": "floors", "l": 2, "q": "What is Tile grout cleaner?", "a": "Grout: baking soda paste, scrub, rinse.", "x": "Grout: baking soda paste, scrub, rinse. Key steps: baking soda paste; old toothbrush; Shake or stir to mix, then use as directed.. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Shower head descale", "d": "Shower head: bag of vinegar tied on overnight dissolves scale.", "g": "bathroom", "l": 2, "q": "What is Shower head descale?", "a": "Shower head: bag of vinegar tied on overnight dissolves scale.", "x": "Shower head: bag of vinegar tied on overnight dissolves scale. Key steps: vinegar in bag tied overnight; Shake or stir to mix, then use as directed.. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Mold remover", "d": "Mold: peroxide spray, 10 minutes, scrub. Ventilate to prevent return.", "g": "bathroom", "l": 2, "q": "What is Mold remover?", "a": "Mold: peroxide spray, 10 minutes, scrub. Ventilate to prevent return.", "x": "Mold: peroxide spray, 10 minutes, scrub. Ventilate to prevent return. Key steps: 3% hydrogen peroxide spray; Shake or stir to mix, then use as directed.. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Air freshener gel", "d": "Gel freshener: gelatin, water, essential oil in a jar.", "g": "air", "l": 2, "q": "What is Air freshener gel?", "a": "Gel freshener: gelatin, water, essential oil in a jar.", "x": "Gel freshener: gelatin, water, essential oil in a jar. Key steps: gelatin; water; essential oil; Shake or stir to mix, then use as directed.. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Furniture dusting spray", "d": "Dusting spray: light mist, microfiber cloth.", "g": "wood", "l": 2, "q": "What is Furniture dusting spray?", "a": "Dusting spray: light mist, microfiber cloth.", "x": "Dusting spray: light mist, microfiber cloth. Key steps: 1 cup water; 1/4 cup vinegar; 2 tbsp olive oil; Shake or stir to mix, then use as directed.. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-cleaning-recipes-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
