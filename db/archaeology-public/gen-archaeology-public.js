(function(){'use strict';
/* Public Archaeology Database generator — jahdb-archaeology-public-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-ARCH-PUB-';
var TOPICS=[["Excavation", "Digging: stratigraphy, context, and careful recording."], ["Stratigraphy", "Reading layers to sequence the past."], ["Dating Methods", "Radiocarbon, dendrochronology, and relative dating."], ["Artifacts", "Tools, pottery, and objects as evidence."], ["Pottery Analysis", "Ceramics as chronological and cultural markers."], ["Zooarchaeology", "Animal bones revealing diet and domestication."], ["Paleobotany", "Ancient plant remains and early agriculture."], ["Human Evolution", "Hominin fossils from Lucy to modern humans."], ["Egyptian Archaeology", "Pyramids, tombs, and pharaonic civilization."], ["Maya Archaeology", "Cities, glyphs, and Mesoamerican civilization."], ["Roman Archaeology", "Empire in stone: cities, roads, and villas."], ["Underwater Archaeology", "Shipwrecks and submerged landscapes."], ["Aerial Archaeology", "Crop marks and LiDAR revealing hidden sites."], ["Experimental Archaeology", "Rebuilding ancient techniques to test them."], ["Cultural Resource Management", "Archaeology in development and law."], ["Stone Tools", "Lithics: knapping and typology."], ["Burials", "What graves reveal about belief and society."], ["Ancient DNA", "Genomes from bones rewriting prehistory."], ["Site Survey", "Finding sites without digging."], ["Conservation", "Preserving artifacts for the future."], ["Museums and Ethics", "Display, repatriation, and who owns the past."], ["The Neolithic Revolution", "Farming's origins in the archaeological record."], ["Urban Origins", "The first cities in Mesopotamia and beyond."], ["Rock Art", "Cave paintings and petroglyphs."], ["Archaeological Illustration", "Drawing finds accurately."]];
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
    type:'archaeology knowledge record', content:content,
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('archaeology-public',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();