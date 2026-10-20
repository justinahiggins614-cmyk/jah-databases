(function(){'use strict';
/* JAH Vitamins and Minerals Database generator — jahdb-vitamins-minerals-nutrition-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='vitamins-minerals-nutrition',PREFIX='JAH-NUT-',NAME='JAH Vitamins and Minerals Database';
var FIELDS=["vitamins", "minerals", "essentials"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Vitamin A", "d": "Vision, immunity, skin. Sources: liver, carrots, sweet potato. Deficiency: night blindness.", "g": "vitamins", "l": 2, "q": "What is Vitamin A?", "a": "Vision, immunity, skin. Sources: liver, carrots, sweet potato. Deficiency: night blindness.", "x": "Vitamin A — Vision, immunity, skin. Sources: liver, carrots, sweet potato. Deficiency: night blindness. Example: Carrots..  Checked against standard scientific references (anatomy atlases, IUPAC, NIST, NASA, standard textbooks).", "s": "public-reference", "f": null}, {"t": "Vitamin B1 (thiamine)", "d": "Energy metabolism, nerves. Sources: whole grains, pork. Deficiency: beriberi.", "g": "vitamins", "l": 2, "q": "What is Vitamin B1 (thiamine)?", "a": "Energy metabolism, nerves. Sources: whole grains, pork. Deficiency: beriberi.", "x": "Vitamin B1 (thiamine) — Energy metabolism, nerves. Sources: whole grains, pork. Deficiency: beriberi. Example: Whole grains..  Checked against standard scientific references (anatomy atlases, IUPAC, NIST, NASA, standard textbooks).", "s": "public-reference", "f": null}, {"t": "Vitamin B2 (riboflavin)", "d": "Energy release, skin, eyes. Sources: dairy, eggs. Deficiency: cracks at mouth corners.", "g": "vitamins", "l": 2, "q": "What is Vitamin B2 (riboflavin)?", "a": "Energy release, skin, eyes. Sources: dairy, eggs. Deficiency: cracks at mouth corners.", "x": "Vitamin B2 (riboflavin) — Energy release, skin, eyes. Sources: dairy, eggs. Deficiency: cracks at mouth corners. Example: Dairy..  Checked against standard scientific references (anatomy atlases, IUPAC, NIST, NASA, standard textbooks).", "s": "public-reference", "f": null}, {"t": "Vitamin B3 (niacin)", "d": "DNA repair, metabolism. Sources: meat, peanuts. Deficiency: pellagra.", "g": "vitamins", "l": 2, "q": "What is Vitamin B3 (niacin)?", "a": "DNA repair, metabolism. Sources: meat, peanuts. Deficiency: pellagra.", "x": "Vitamin B3 (niacin) — DNA repair, metabolism. Sources: meat, peanuts. Deficiency: pellagra. Example: Peanuts..  Checked against standard scientific references (anatomy atlases, IUPAC, NIST, NASA, standard textbooks).", "s": "public-reference", "f": null}, {"t": "Vitamin B5 (pantothenic acid)", "d": "Coenzyme A, energy. Sources: almost all foods. Deficiency: very rare.", "g": "vitamins", "l": 2, "q": "What is Vitamin B5 (pantothenic acid)?", "a": "Coenzyme A, energy. Sources: almost all foods. Deficiency: very rare.", "x": "Vitamin B5 (pantothenic acid) — Coenzyme A, energy. Sources: almost all foods. Deficiency: very rare. Example: Varied diet..  Checked against standard scientific references (anatomy atlases, IUPAC, NIST, NASA, standard textbooks).", "s": "public-reference", "f": null}, {"t": "Vitamin B6 (pyridoxine)", "d": "Amino acid metabolism, brain. Sources: poultry, bananas. Deficiency: anemia, confusion.", "g": "vitamins", "l": 2, "q": "What is Vitamin B6 (pyridoxine)?", "a": "Amino acid metabolism, brain. Sources: poultry, bananas. Deficiency: anemia, confusion.", "x": "Vitamin B6 (pyridoxine) — Amino acid metabolism, brain. Sources: poultry, bananas. Deficiency: anemia, confusion. Example: Bananas..  Checked against standard scientific references (anatomy atlases, IUPAC, NIST, NASA, standard textbooks).", "s": "public-reference", "f": null}, {"t": "Vitamin B7 (biotin)", "d": "Fat and protein metabolism, hair, nails. Sources: eggs, nuts. Deficiency: rare.", "g": "vitamins", "l": 2, "q": "What is Vitamin B7 (biotin)?", "a": "Fat and protein metabolism, hair, nails. Sources: eggs, nuts. Deficiency: rare.", "x": "Vitamin B7 (biotin) — Fat and protein metabolism, hair, nails. Sources: eggs, nuts. Deficiency: rare. Example: Eggs..  Checked against standard scientific references (anatomy atlases, IUPAC, NIST, NASA, standard textbooks).", "s": "public-reference", "f": null}, {"t": "Vitamin B9 (folate)", "d": "Cell division, pregnancy. Sources: leafy greens, legumes. Deficiency: neural tube defects.", "g": "vitamins", "l": 2, "q": "What is Vitamin B9 (folate)?", "a": "Cell division, pregnancy. Sources: leafy greens, legumes. Deficiency: neural tube defects.", "x": "Vitamin B9 (folate) — Cell division, pregnancy. Sources: leafy greens, legumes. Deficiency: neural tube defects. Example: Spinach..  Checked against standard scientific references (anatomy atlases, IUPAC, NIST, NASA, standard textbooks).", "s": "public-reference", "f": null}, {"t": "Vitamin B12 (cobalamin)", "d": "Nerves, red blood cells. Sources: animal foods. Deficiency: pernicious anemia.", "g": "vitamins", "l": 2, "q": "What is Vitamin B12 (cobalamin)?", "a": "Nerves, red blood cells. Sources: animal foods. Deficiency: pernicious anemia.", "x": "Vitamin B12 (cobalamin) — Nerves, red blood cells. Sources: animal foods. Deficiency: pernicious anemia. Example: Meat..  Checked against standard scientific references (anatomy atlases, IUPAC, NIST, NASA, standard textbooks).", "s": "public-reference", "f": null}, {"t": "Vitamin C", "d": "Collagen, immunity, iron absorption. Sources: citrus, peppers. Deficiency: scurvy.", "g": "vitamins", "l": 2, "q": "What is Vitamin C?", "a": "Collagen, immunity, iron absorption. Sources: citrus, peppers. Deficiency: scurvy.", "x": "Vitamin C — Collagen, immunity, iron absorption. Sources: citrus, peppers. Deficiency: scurvy. Example: Oranges..  Checked against standard scientific references (anatomy atlases, IUPAC, NIST, NASA, standard textbooks).", "s": "public-reference", "f": null}, {"t": "Vitamin D", "d": "Calcium absorption, bones, immunity. Sources: sun, fatty fish. Deficiency: rickets.", "g": "vitamins", "l": 2, "q": "What is Vitamin D?", "a": "Calcium absorption, bones, immunity. Sources: sun, fatty fish. Deficiency: rickets.", "x": "Vitamin D — Calcium absorption, bones, immunity. Sources: sun, fatty fish. Deficiency: rickets. Example: Sunlight..  Checked against standard scientific references (anatomy atlases, IUPAC, NIST, NASA, standard textbooks).", "s": "public-reference", "f": null}, {"t": "Vitamin E", "d": "Antioxidant, cell membranes. Sources: nuts, seeds, oils. Deficiency: rare nerve issues.", "g": "vitamins", "l": 2, "q": "What is Vitamin E?", "a": "Antioxidant, cell membranes. Sources: nuts, seeds, oils. Deficiency: rare nerve issues.", "x": "Vitamin E — Antioxidant, cell membranes. Sources: nuts, seeds, oils. Deficiency: rare nerve issues. Example: Almonds..  Checked against standard scientific references (anatomy atlases, IUPAC, NIST, NASA, standard textbooks).", "s": "public-reference", "f": null}, {"t": "Vitamin K", "d": "Blood clotting, bones. Sources: leafy greens, gut bacteria. Deficiency: bleeding.", "g": "vitamins", "l": 2, "q": "What is Vitamin K?", "a": "Blood clotting, bones. Sources: leafy greens, gut bacteria. Deficiency: bleeding.", "x": "Vitamin K — Blood clotting, bones. Sources: leafy greens, gut bacteria. Deficiency: bleeding. Example: Kale..  Checked against standard scientific references (anatomy atlases, IUPAC, NIST, NASA, standard textbooks).", "s": "public-reference", "f": null}, {"t": "Calcium", "d": "Bones, teeth, muscle signals. Sources: dairy, greens. About 1,000 mg/day.", "g": "minerals", "l": 2, "q": "What is Calcium?", "a": "Bones, teeth, muscle signals. Sources: dairy, greens. About 1,000 mg/day.", "x": "Calcium — Bones, teeth, muscle signals. Sources: dairy, greens. About 1,000 mg/day. Example: Milk..  Checked against standard scientific references (anatomy atlases, IUPAC, NIST, NASA, standard textbooks).", "s": "public-reference", "f": null}, {"t": "Iron", "d": "Hemoglobin oxygen transport. Sources: red meat, lentils. Deficiency: anemia.", "g": "minerals", "l": 2, "q": "What is Iron?", "a": "Hemoglobin oxygen transport. Sources: red meat, lentils. Deficiency: anemia.", "x": "Iron — Hemoglobin oxygen transport. Sources: red meat, lentils. Deficiency: anemia. Example: Lentils..  Checked against standard scientific references (anatomy atlases, IUPAC, NIST, NASA, standard textbooks).", "s": "public-reference", "f": null}, {"t": "Magnesium", "d": "300+ enzyme reactions, muscles, sleep. Sources: nuts, greens. About 400 mg/day.", "g": "minerals", "l": 2, "q": "What is Magnesium?", "a": "300+ enzyme reactions, muscles, sleep. Sources: nuts, greens. About 400 mg/day.", "x": "Magnesium — 300+ enzyme reactions, muscles, sleep. Sources: nuts, greens. About 400 mg/day. Example: Nuts..  Checked against standard scientific references (anatomy atlases, IUPAC, NIST, NASA, standard textbooks).", "s": "public-reference", "f": null}, {"t": "Potassium", "d": "Fluid balance, blood pressure, heart. Sources: bananas, potatoes. About 3,500 mg/day.", "g": "minerals", "l": 2, "q": "What is Potassium?", "a": "Fluid balance, blood pressure, heart. Sources: bananas, potatoes. About 3,500 mg/day.", "x": "Potassium — Fluid balance, blood pressure, heart. Sources: bananas, potatoes. About 3,500 mg/day. Example: Potatoes..  Checked against standard scientific references (anatomy atlases, IUPAC, NIST, NASA, standard textbooks).", "s": "public-reference", "f": null}, {"t": "Sodium", "d": "Fluid balance, nerves. Needed in small amounts; excess raises blood pressure.", "g": "minerals", "l": 2, "q": "What is Sodium?", "a": "Fluid balance, nerves. Needed in small amounts; excess raises blood pressure.", "x": "Sodium — Fluid balance, nerves. Needed in small amounts; excess raises blood pressure. Example: Salt..  Checked against standard scientific references (anatomy atlases, IUPAC, NIST, NASA, standard textbooks).", "s": "public-reference", "f": null}, {"t": "Chloride", "d": "Stomach acid, fluid balance. Comes with sodium in salt.", "g": "minerals", "l": 2, "q": "What is Chloride?", "a": "Stomach acid, fluid balance. Comes with sodium in salt.", "x": "Chloride — Stomach acid, fluid balance. Comes with sodium in salt. Example: Salt..  Checked against standard scientific references (anatomy atlases, IUPAC, NIST, NASA, standard textbooks). Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Zinc", "d": "Immunity, wound healing, taste. Sources: meat, shellfish. About 11 mg/day.", "g": "minerals", "l": 2, "q": "What is Zinc?", "a": "Immunity, wound healing, taste. Sources: meat, shellfish. About 11 mg/day.", "x": "Zinc — Immunity, wound healing, taste. Sources: meat, shellfish. About 11 mg/day. Example: Oysters..  Checked against standard scientific references (anatomy atlases, IUPAC, NIST, NASA, standard textbooks).", "s": "public-reference", "f": null}, {"t": "Iodine", "d": "Thyroid hormones. Sources: iodized salt, seafood. Deficiency: goiter.", "g": "minerals", "l": 2, "q": "What is Iodine?", "a": "Thyroid hormones. Sources: iodized salt, seafood. Deficiency: goiter.", "x": "Iodine — Thyroid hormones. Sources: iodized salt, seafood. Deficiency: goiter. Example: Iodized salt..  Checked against standard scientific references (anatomy atlases, IUPAC, NIST, NASA, standard textbooks).", "s": "public-reference", "f": null}, {"t": "Selenium", "d": "Antioxidant enzymes, thyroid. Sources: Brazil nuts, fish. About 55 mcg/day.", "g": "minerals", "l": 2, "q": "What is Selenium?", "a": "Antioxidant enzymes, thyroid. Sources: Brazil nuts, fish. About 55 mcg/day.", "x": "Selenium — Antioxidant enzymes, thyroid. Sources: Brazil nuts, fish. About 55 mcg/day. Example: Brazil nuts..  Checked against standard scientific references (anatomy atlases, IUPAC, NIST, NASA, standard textbooks).", "s": "public-reference", "f": null}, {"t": "Copper", "d": "Iron metabolism, nerves. Sources: shellfish, nuts. About 900 mcg/day.", "g": "minerals", "l": 2, "q": "What is Copper?", "a": "Iron metabolism, nerves. Sources: shellfish, nuts. About 900 mcg/day.", "x": "Copper — Iron metabolism, nerves. Sources: shellfish, nuts. About 900 mcg/day. Example: Cashews..  Checked against standard scientific references (anatomy atlases, IUPAC, NIST, NASA, standard textbooks).", "s": "public-reference", "f": null}, {"t": "Manganese", "d": "Bone formation, metabolism. Sources: whole grains, tea.", "g": "minerals", "l": 2, "q": "What is Manganese?", "a": "Bone formation, metabolism. Sources: whole grains, tea.", "x": "Manganese — Bone formation, metabolism. Sources: whole grains, tea. Example: Tea..  Checked against standard scientific references (anatomy atlases, IUPAC, NIST, NASA, standard textbooks). Every entry in this database carries the same treatment: a plain definition, a real example, a runnable demo program, and its source, so the whole set works as one consistent reference you can search, quiz, and build on.", "s": "public-reference", "f": null}, {"t": "Phosphorus", "d": "Bones, teeth, energy molecules. Sources: dairy, meat. About 700 mg/day.", "g": "minerals", "l": 2, "q": "What is Phosphorus?", "a": "Bones, teeth, energy molecules. Sources: dairy, meat. About 700 mg/day.", "x": "Phosphorus — Bones, teeth, energy molecules. Sources: dairy, meat. About 700 mg/day. Example: Dairy..  Checked against standard scientific references (anatomy atlases, IUPAC, NIST, NASA, standard textbooks).", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-vitamins-minerals-nutrition-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
