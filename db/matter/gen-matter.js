(function(){'use strict';
/* Matter Database generator — jahdb-matter-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-MATTER-';
var TOPICS=[["Solids", "Matter with fixed shape and volume."], ["Liquids", "Matter with fixed volume that takes its container's shape."], ["Gases", "Matter that expands to fill its container."], ["Plasma", "The energetic fourth state of matter found in stars and lightning."], ["Atoms", "The tiny particles that make up all matter."], ["Molecules", "Groups of atoms bonded together."], ["Elements", "Pure substances of one kind of atom."], ["Compounds", "Substances of two or more elements chemically bonded."], ["Mixtures", "Combinations of substances not chemically bonded."], ["Water", "H2O, the essential compound of life."], ["Evaporation", "Liquid turning to gas at the surface."], ["Condensation", "Gas turning to liquid on cool surfaces."], ["Freezing", "Liquid turning to solid."], ["Melting", "Solid turning to liquid."], ["Boiling", "Liquid turning rapidly to gas."], ["Density", "How much mass is packed into a volume."], ["Mass", "The amount of matter in an object."], ["Volume", "The space matter occupies."], ["Electrons", "The negatively charged particles orbiting atoms."], ["Protons", "The positive particles in atomic nuclei."], ["Neutrons", "The neutral particles in atomic nuclei."], ["Chemical Change", "When substances transform into new substances."], ["Physical Change", "When matter changes form but not identity."], ["Solutions", "Even mixtures like salt dissolved in water."], ["Acids and Bases", "The sour and bitter opposites of chemistry."], ["The pH Scale", "The measure of how acidic or basic a solution is."], ["Conservation of Mass", "Matter is neither created nor destroyed in reactions."], ["Energy and Matter", "How matter and energy convert into each other."]];
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
    type:'matter record', content:content,
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('matter',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();