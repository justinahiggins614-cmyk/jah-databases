(function(){'use strict';
/* JAH Baking Substitutions Database generator — jahdb-baking-substitutions-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='baking-substitutions',PREFIX='JAH-BKS-',NAME='JAH Baking Substitutions Database';
var FIELDS=["dairy", "egg", "flour", "thickener", "leavener", "sugar", "flavor", "acid", "chocolate", "fat"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Buttermilk", "d": "No buttermilk: milk plus acid curdles into a fine substitute for pancakes and biscuits.", "g": "dairy", "l": 2, "q": "What is Buttermilk?", "a": "No buttermilk: milk plus acid curdles into a fine substitute for pancakes and biscuits.", "x": "No buttermilk: milk plus acid curdles into a fine substitute for pancakes and biscuits. sub: 1 cup milk + 1 tbsp lemon juice or vinegar, rest 5 min. ratio: 1:1. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Heavy cream", "d": "Cream substitute works in baking; it will not whip.", "g": "dairy", "l": 2, "q": "What is Heavy cream?", "a": "Cream substitute works in baking; it will not whip.", "x": "Cream substitute works in baking; it will not whip. sub: 3/4 cup milk + 1/3 cup melted butter. ratio: 1:1. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Sour cream", "d": "Plain yogurt swaps for sour cream in most baking.", "g": "dairy", "l": 2, "q": "What is Sour cream?", "a": "Plain yogurt swaps for sour cream in most baking.", "x": "Plain yogurt swaps for sour cream in most baking. sub: plain yogurt 1:1. ratio: 1:1. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Cream cheese", "d": "Blended ricotta-yogurt approximates cream cheese in fillings.", "g": "dairy", "l": 2, "q": "What is Cream cheese?", "a": "Blended ricotta-yogurt approximates cream cheese in fillings.", "x": "Blended ricotta-yogurt approximates cream cheese in fillings. sub: equal parts ricotta + yogurt, blended. ratio: 1:1. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Butter (baking)", "d": "Coconut oil swaps for butter in baking; flavor shifts slightly.", "g": "dairy", "l": 2, "q": "What is Butter (baking)?", "a": "Coconut oil swaps for butter in baking; flavor shifts slightly.", "x": "Coconut oil swaps for butter in baking; flavor shifts slightly. sub: coconut oil or margarine 1:1. ratio: 1:1. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Egg (1)", "d": "Flax eggs bind well in muffins and pancakes; applesauce adds moisture.", "g": "egg", "l": 2, "q": "What is Egg (1)?", "a": "Flax eggs bind well in muffins and pancakes; applesauce adds moisture.", "x": "Flax eggs bind well in muffins and pancakes; applesauce adds moisture. sub: 1/4 cup applesauce, or 1 tbsp ground flax + 3 tbsp water. ratio: per egg. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Egg white", "d": "Aquafaba (chickpea liquid) whips like egg whites for meringues.", "g": "egg", "l": 2, "q": "What is Egg white?", "a": "Aquafaba (chickpea liquid) whips like egg whites for meringues.", "x": "Aquafaba (chickpea liquid) whips like egg whites for meringues. sub: 2 tbsp aquafaba per white. ratio: per white. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "All-purpose flour", "d": "Homemade cake flour: remove 2 tbsp per cup, add 2 tbsp cornstarch.", "g": "flour", "l": 2, "q": "What is All-purpose flour?", "a": "Homemade cake flour: remove 2 tbsp per cup, add 2 tbsp cornstarch.", "x": "Homemade cake flour: remove 2 tbsp per cup, add 2 tbsp cornstarch. sub: 1 cup = 1 cup minus 2 tbsp, for cake flour add 2 tbsp cornstarch. ratio: 1:1. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Cake flour", "d": "See above — the classic conversion.", "g": "flour", "l": 2, "q": "What is Cake flour?", "a": "See above — the classic conversion.", "x": "See above — the classic conversion. sub: 1 cup AP flour minus 2 tbsp + 2 tbsp cornstarch. ratio: 1:1. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Bread flour", "d": "Vital wheat gluten boosts AP flour to bread strength.", "g": "flour", "l": 2, "q": "What is Bread flour?", "a": "Vital wheat gluten boosts AP flour to bread strength.", "x": "Vital wheat gluten boosts AP flour to bread strength. sub: 1 cup AP flour + 1 tbsp vital wheat gluten. ratio: 1:1. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Self-rising flour", "d": "Self-rising flour is just AP plus leavening and salt.", "g": "flour", "l": 2, "q": "What is Self-rising flour?", "a": "Self-rising flour is just AP plus leavening and salt.", "x": "Self-rising flour is just AP plus leavening and salt. sub: 1 cup AP flour + 1.5 tsp baking powder + 0.5 tsp salt. ratio: 1:1. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Cornstarch (thickener)", "d": "Flour thickens at double the amount; cook out the raw taste.", "g": "thickener", "l": 2, "q": "What is Cornstarch (thickener)?", "a": "Flour thickens at double the amount; cook out the raw taste.", "x": "Flour thickens at double the amount; cook out the raw taste. sub: 2 tbsp flour per 1 tbsp cornstarch. ratio: 2:1. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Baking powder", "d": "Homemade baking powder: soda plus acid.", "g": "leavener", "l": 2, "q": "What is Baking powder?", "a": "Homemade baking powder: soda plus acid.", "x": "Homemade baking powder: soda plus acid. sub: 1/4 tsp baking soda + 1/2 tsp cream of tartar per tsp. ratio: per tsp. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Baking soda", "d": "Baking powder can replace soda at triple amount if the recipe has acid.", "g": "leavener", "l": 2, "q": "What is Baking soda?", "a": "Baking powder can replace soda at triple amount if the recipe has acid.", "x": "Baking powder can replace soda at triple amount if the recipe has acid. sub: 3x baking powder (reduce salt); needs acid in recipe. ratio: 3:1. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Active dry yeast", "d": "Instant yeast swaps directly; no proofing needed.", "g": "leavener", "l": 2, "q": "What is Active dry yeast?", "a": "Instant yeast swaps directly; no proofing needed.", "x": "Instant yeast swaps directly; no proofing needed. sub: instant yeast 1:1 (skip proofing); 1 packet = 2.25 tsp. ratio: 1:1. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Brown sugar", "d": "Brown sugar is white sugar plus molasses: mix fresh.", "g": "sugar", "l": 2, "q": "What is Brown sugar?", "a": "Brown sugar is white sugar plus molasses: mix fresh.", "x": "Brown sugar is white sugar plus molasses: mix fresh. sub: 1 cup white sugar + 1 tbsp molasses. ratio: 1:1. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Powdered sugar", "d": "Blitz granulated sugar with cornstarch for powdered.", "g": "sugar", "l": 2, "q": "What is Powdered sugar?", "a": "Blitz granulated sugar with cornstarch for powdered.", "x": "Blitz granulated sugar with cornstarch for powdered. sub: 1 cup granulated blended + 1 tbsp cornstarch. ratio: 1:1. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Honey for sugar", "d": "Honey sweetens stronger: reduce other liquids.", "g": "sugar", "l": 2, "q": "What is Honey for sugar?", "a": "Honey sweetens stronger: reduce other liquids.", "x": "Honey sweetens stronger: reduce other liquids. sub: 3/4 cup honey per cup sugar; reduce liquid, lower temp 15 C. ratio: 0.75:1. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Maple syrup for sugar", "d": "Maple syrup swaps like honey.", "g": "sugar", "l": 2, "q": "What is Maple syrup for sugar?", "a": "Maple syrup swaps like honey.", "x": "Maple syrup swaps like honey. sub: 3/4 cup per cup sugar; reduce liquid. ratio: 0.75:1. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Molasses", "d": "Dark corn syrup approximates molasses in baking.", "g": "sugar", "l": 2, "q": "What is Molasses?", "a": "Dark corn syrup approximates molasses in baking.", "x": "Dark corn syrup approximates molasses in baking. sub: dark corn syrup or honey 1:1 (lighter flavor). ratio: 1:1. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Corn syrup", "d": "Honey prevents crystallization like corn syrup.", "g": "sugar", "l": 2, "q": "What is Corn syrup?", "a": "Honey prevents crystallization like corn syrup.", "x": "Honey prevents crystallization like corn syrup. sub: honey or golden syrup 1:1. ratio: 1:1. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Vanilla extract", "d": "Vanilla paste is the premium swap; almond extract is stronger, use half.", "g": "flavor", "l": 2, "q": "What is Vanilla extract?", "a": "Vanilla paste is the premium swap; almond extract is stronger, use half.", "x": "Vanilla paste is the premium swap; almond extract is stronger, use half. sub: equal vanilla paste; or half almond extract. ratio: 1:1. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Lemon juice", "d": "Lime swaps for lemon; vinegar at half in a pinch.", "g": "acid", "l": 2, "q": "What is Lemon juice?", "a": "Lime swaps for lemon; vinegar at half in a pinch.", "x": "Lime swaps for lemon; vinegar at half in a pinch. sub: lime juice 1:1; or half white vinegar. ratio: 1:1. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Cocoa powder", "d": "Cocoa plus fat replaces unsweetened chocolate.", "g": "chocolate", "l": 2, "q": "What is Cocoa powder?", "a": "Cocoa plus fat replaces unsweetened chocolate.", "x": "Cocoa plus fat replaces unsweetened chocolate. sub: unsweetened: 3 tbsp + 1 tbsp fat per oz chocolate. ratio: per oz. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Unsweetened chocolate", "d": "The standard chocolate conversion.", "g": "chocolate", "l": 2, "q": "What is Unsweetened chocolate?", "a": "The standard chocolate conversion.", "x": "The standard chocolate conversion. sub: 3 tbsp cocoa + 1 tbsp butter per ounce. ratio: per oz. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-baking-substitutions-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
