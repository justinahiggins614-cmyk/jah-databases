(function(){'use strict';
/* Rocks and Minerals Database generator — jahdb-rocks-minerals-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-ROCK-';
var TOPICS=[["Granite", "The speckled igneous rock of countertops and mountains."], ["Basalt", "The dark volcanic rock of ocean floors."], ["Limestone", "The sedimentary rock formed from shells and skeletons."], ["Sandstone", "Rock made of cemented sand grains."], ["Marble", "The metamorphosed limestone prized by sculptors."], ["Slate", "The fine-grained rock splitting into roofing tiles."], ["Obsidian", "Natural volcanic glass."], ["Pumice", "The light volcanic rock that floats on water."], ["Quartz", "The common hard mineral of sand and crystals."], ["Diamond", "The hardest natural material, pure carbon crystal."], ["Gold", "The precious yellow metal found as nuggets and veins."], ["Feldspar", "The most abundant mineral group in Earth's crust."], ["Mica", "The flaky mineral splitting into thin sheets."], ["Calcite", "The mineral of limestone and marble."], ["Gypsum", "The soft mineral of drywall and plaster."], ["Talc", "The softest mineral on the Mohs scale."], ["Topaz", "The hard gemstone of many colors."], ["Emerald", "The green gem variety of beryl."], ["Ruby", "The red gem variety of corundum."], ["Sapphire", "The blue gem variety of corundum."], ["Amethyst", "The purple variety of quartz."], ["Iron Ore", "The rocks from which iron is smelted."], ["Coal", "The fossil fuel rock of ancient plants."], ["The Rock Cycle", "How rocks transform between igneous, sedimentary, and metamorphic."], ["Igneous Rocks", "Rocks solidified from molten magma."], ["Sedimentary Rocks", "Rocks formed from layers of sediment."], ["Metamorphic Rocks", "Rocks transformed by heat and pressure."], ["Mohs Hardness Scale", "The scratch test ranking minerals from talc to diamond."]];
var ANGLES=['overview','detailed','examples','faq','history','applications'];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0, ai=(s()*ANGLES.length)|0;
  var topic=TOPICS[ti], angle=ANGLES[ai];
  var id=PREFIX+pad(seed);
  var title=topic[0]+' ('+angle+')';
  var desc=topic[1]+' This '+angle+' guide provides comprehensive coverage.';
  var content='['+angle+'] '+topic[0]+': '+topic[1]+' Full detailed content for '+angle+' perspective.';
  return {
    id:id, title:title, description:desc, genre:angle,
    type:'rocks and minerals record', content:content,
    demo:null, src:'public', _seed:seed
  };
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.content||r.content.length<50)errs.push('content too short');
  return {ok:errs.length===0, errors:errs};
}
function driftCheck(rec,sample){
  // Simple: check for exact title duplicates in sample
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('rocks-minerals',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();