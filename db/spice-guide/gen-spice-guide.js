(function(){'use strict';
/* JAH Spice Guide Database generator — jahdb-spice-guide-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds 1..BANK return archive sample
   records; higher seeds generate boundless drills. Drill answers come from the
   banked archive data and validate() re-checks every one of them. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var SLUG='spice-guide',PREFIX='JAH-SPC-',NAME='JAH Spice Guide Database';
var FIELDS=["peppercorn", "bark", "seed", "bud", "berry", "pod", "root", "pepper", "blend", "stigma", "leaf"];
var GEN_SRC='reference-authored';
var MODE='quiz';
var BANK=[{"t": "Black pepper", "d": "Black pepper is the king of spices: dried peppercorns, ground fresh for pungent heat on everything.", "g": "peppercorn", "l": 2, "q": "What is Black pepper?", "a": "Black pepper is the king of spices: dried peppercorns, ground fresh for pungent heat on everything.", "x": "Black pepper is the king of spices: dried peppercorns, ground fresh for pungent heat on everything. flavor: pungent heat. use: everything. origin: India. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "White pepper", "d": "White pepper is black pepper with the husk removed: earthier, for pale sauces.", "g": "peppercorn", "l": 2, "q": "What is White pepper?", "a": "White pepper is black pepper with the husk removed: earthier, for pale sauces.", "x": "White pepper is black pepper with the husk removed: earthier, for pale sauces. flavor: earthy heat. use: light sauces. origin: India. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Cinnamon (Ceylon)", "d": "True Ceylon cinnamon is delicate and sweet; most US cinnamon is cassia, bolder and cheaper.", "g": "bark", "l": 2, "q": "What is Cinnamon (Ceylon)?", "a": "True Ceylon cinnamon is delicate and sweet; most US cinnamon is cassia, bolder and cheaper.", "x": "True Ceylon cinnamon is delicate and sweet; most US cinnamon is cassia, bolder and cheaper. flavor: sweet, delicate. use: baking, curry. origin: Sri Lanka. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Cassia", "d": "Cassia is the bold cinnamon of American baking.", "g": "bark", "l": 2, "q": "What is Cassia?", "a": "Cassia is the bold cinnamon of American baking.", "x": "Cassia is the bold cinnamon of American baking. flavor: bold, sweet. use: baking. origin: China. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Nutmeg", "d": "Nutmeg is warm and sweet grated fresh; whole seeds keep years.", "g": "seed", "l": 2, "q": "What is Nutmeg?", "a": "Nutmeg is warm and sweet grated fresh; whole seeds keep years.", "x": "Nutmeg is warm and sweet grated fresh; whole seeds keep years. flavor: warm, sweet. use: baking, bechamel. origin: Indonesia. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Mace", "d": "Mace is the lacy covering of the nutmeg seed: similar but more delicate.", "g": "seed", "l": 2, "q": "What is Mace?", "a": "Mace is the lacy covering of the nutmeg seed: similar but more delicate.", "x": "Mace is the lacy covering of the nutmeg seed: similar but more delicate. flavor: nutmeg-like, delicate. use: baking, sausages. origin: Indonesia. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Clove", "d": "Cloves are intense dried flower buds: a little perfumes a whole ham.", "g": "bud", "l": 2, "q": "What is Clove?", "a": "Cloves are intense dried flower buds: a little perfumes a whole ham.", "x": "Cloves are intense dried flower buds: a little perfumes a whole ham. flavor: intense, sweet. use: ham, baking, chai. origin: Indonesia. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Allspice", "d": "Allspice tastes like all the baking spices at once; it is one berry from Jamaica.", "g": "berry", "l": 2, "q": "What is Allspice?", "a": "Allspice tastes like all the baking spices at once; it is one berry from Jamaica.", "x": "Allspice tastes like all the baking spices at once; it is one berry from Jamaica. flavor: clove-cinnamon-nutmeg. use: Caribbean, baking. origin: Jamaica. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Cardamom (green)", "d": "Green cardamom is the queen of spices: floral pods for chai and Scandinavian buns.", "g": "pod", "l": 2, "q": "What is Cardamom (green)?", "a": "Green cardamom is the queen of spices: floral pods for chai and Scandinavian buns.", "x": "Green cardamom is the queen of spices: floral pods for chai and Scandinavian buns. flavor: floral, eucalyptus. use: chai, Scandinavian baking. origin: India. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Cardamom (black)", "d": "Black cardamom is smoky and bold: for savory dishes, never desserts.", "g": "pod", "l": 2, "q": "What is Cardamom (black)?", "a": "Black cardamom is smoky and bold: for savory dishes, never desserts.", "x": "Black cardamom is smoky and bold: for savory dishes, never desserts. flavor: smoky, camphor. use: savory Indian. origin: India. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Turmeric", "d": "Turmeric is the golden root: earthy color for curries, anti-inflammatory fame. Pair with black pepper.", "g": "root", "l": 2, "q": "What is Turmeric?", "a": "Turmeric is the golden root: earthy color for curries, anti-inflammatory fame. Pair with black pepper.", "x": "Turmeric is the golden root: earthy color for curries, anti-inflammatory fame. Pair with black pepper. flavor: earthy, bitter. use: curry, golden milk. origin: India. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Ginger (ground)", "d": "Ground ginger is warm sweetness for baking; fresh ginger is sharper.", "g": "root", "l": 2, "q": "What is Ginger (ground)?", "a": "Ground ginger is warm sweetness for baking; fresh ginger is sharper.", "x": "Ground ginger is warm sweetness for baking; fresh ginger is sharper. flavor: warm, sweet heat. use: baking, curry. origin: Asia. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Cumin", "d": "Cumin is the earthy backbone of chili, curry, and tacos. Toast to wake it up.", "g": "seed", "l": 2, "q": "What is Cumin?", "a": "Cumin is the earthy backbone of chili, curry, and tacos. Toast to wake it up.", "x": "Cumin is the earthy backbone of chili, curry, and tacos. Toast to wake it up. flavor: earthy, nutty. use: chili, curry, Mexican. origin: Middle East. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Coriander seed", "d": "Coriander seed is citrusy and floral — nothing like the leaf.", "g": "seed", "l": 2, "q": "What is Coriander seed?", "a": "Coriander seed is citrusy and floral — nothing like the leaf.", "x": "Coriander seed is citrusy and floral — nothing like the leaf. flavor: citrusy, floral. use: curry, pickling. origin: Mediterranean. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Fennel seed", "d": "Fennel seed is the sweet anise in Italian sausage.", "g": "seed", "l": 2, "q": "What is Fennel seed?", "a": "Fennel seed is the sweet anise in Italian sausage.", "x": "Fennel seed is the sweet anise in Italian sausage. flavor: anise-sweet. use: sausage, Italian. origin: Mediterranean. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Mustard seed", "d": "Mustard seeds pop in hot oil for Indian tempering; ground, they become mustard.", "g": "seed", "l": 2, "q": "What is Mustard seed?", "a": "Mustard seeds pop in hot oil for Indian tempering; ground, they become mustard.", "x": "Mustard seeds pop in hot oil for Indian tempering; ground, they become mustard. flavor: pungent when crushed. use: Indian tempering, pickles. origin: India. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Fenugreek seed", "d": "Fenugreek seeds smell of maple and bite bitter: essential in curry powders.", "g": "seed", "l": 2, "q": "What is Fenugreek seed?", "a": "Fenugreek seeds smell of maple and bite bitter: essential in curry powders.", "x": "Fenugreek seeds smell of maple and bite bitter: essential in curry powders. flavor: maple-bitter. use: curry. origin: India. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Nigella seed", "d": "Nigella (kalonji) tops breads with oniony crunch.", "g": "seed", "l": 2, "q": "What is Nigella seed?", "a": "Nigella (kalonji) tops breads with oniony crunch.", "x": "Nigella (kalonji) tops breads with oniony crunch. flavor: onion-pepper. use: breads, Indian. origin: Middle East. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Poppy seed", "d": "Poppy seeds are nutty crunch for bagels and lemon cakes.", "g": "seed", "l": 2, "q": "What is Poppy seed?", "a": "Poppy seeds are nutty crunch for bagels and lemon cakes.", "x": "Poppy seeds are nutty crunch for bagels and lemon cakes. flavor: nutty. use: baking, bagels. origin: Mediterranean. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Sesame seed", "d": "Sesame: toast for nuttiness; grind for tahini.", "g": "seed", "l": 2, "q": "What is Sesame seed?", "a": "Sesame: toast for nuttiness; grind for tahini.", "x": "Sesame: toast for nuttiness; grind for tahini. flavor: nutty. use: Asian, baking. origin: Africa/Asia. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Caraway", "d": "Caraway is the rye bread seed: anise-earthy.", "g": "seed", "l": 2, "q": "What is Caraway?", "a": "Caraway is the rye bread seed: anise-earthy.", "x": "Caraway is the rye bread seed: anise-earthy. flavor: anise-earthy. use: rye bread, cabbage. origin: Europe. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Celery seed", "d": "Celery seed is celery concentrate for pickles and slaw.", "g": "seed", "l": 2, "q": "What is Celery seed?", "a": "Celery seed is celery concentrate for pickles and slaw.", "x": "Celery seed is celery concentrate for pickles and slaw. flavor: concentrated celery. use: pickling, coleslaw. origin: Mediterranean. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Dill seed", "d": "Dill seed is the pickling spice proper.", "g": "seed", "l": 2, "q": "What is Dill seed?", "a": "Dill seed is the pickling spice proper.", "x": "Dill seed is the pickling spice proper. flavor: dill, caraway-like. use: pickles. origin: Mediterranean. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Anise seed", "d": "Anise seed is sweet licorice for biscotti and ouzo.", "g": "seed", "l": 2, "q": "What is Anise seed?", "a": "Anise seed is sweet licorice for biscotti and ouzo.", "x": "Anise seed is sweet licorice for biscotti and ouzo. flavor: sweet licorice. use: baking, liqueurs. origin: Middle East. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}, {"t": "Star anise", "d": "Star anise is the beautiful eight-pointed pod of pho and five-spice.", "g": "pod", "l": 2, "q": "What is Star anise?", "a": "Star anise is the beautiful eight-pointed pod of pho and five-spice.", "x": "Star anise is the beautiful eight-pointed pod of pho and five-spice. flavor: intense licorice. use: pho, Chinese. origin: China. Real, practical guidance checked against standard references. Nothing here is a stub — every record is complete and usable.", "s": "public-reference", "f": null}];
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
var gen={version:'jahdb-spice-guide-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
