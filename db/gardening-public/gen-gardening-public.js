(function(){'use strict';
/* Public Gardening Database generator — jahdb-gardening-public-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-GARD-PUB-';
var TOPICS=[["Soil", "Types, testing, and amendment."], ["Compost", "Hot and cold composting methods."], ["Seeds", "Starting, saving, and germination."], ["Transplanting", "Moving seedlings without shock."], ["Watering", "Deep, infrequent, and efficient irrigation."], ["Vegetable Gardening", "Beds, spacing, and succession planting."], ["Herb Gardens", "Culinary and medicinal herbs."], ["Flower Gardens", "Annuals, perennials, and design."], ["Container Gardening", "Growing in pots on patios and balconies."], ["Raised Beds", "Building and filling productive beds."], ["Companion Planting", "Plants that help each other."], ["Crop Rotation", "Preventing disease through rotation."], ["Pest Management", "Organic approaches to garden pests."], ["Weeding", "Strategies for staying ahead of weeds."], ["Mulching", "Retaining moisture and suppressing weeds."], ["Pruning", "Techniques for trees and shrubs."], ["Fruit Trees", "Planting, training, and harvesting."], ["Berries", "Blueberries, raspberries, strawberries."], ["Pollinators", "Gardening for bees and butterflies."], ["Native Plants", "Gardening with local species."], ["Greenhouses", "Extending the season under cover."], ["Cold Frames", "Simple season extension."], ["Garden Planning", "Layout, sun mapping, and calendars."], ["Tool Care", "Keeping tools sharp and clean."], ["Harvesting", "Picking at peak ripeness and storage."]];
var ANGLES=['overview','detailed','examples','faq','history','applications'];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0, ai=(s()*ANGLES.length)|0;
  var topic=TOPICS[ti], angle=ANGLES[ai];
  var id=PREFIX+pad(seed);
  var title=topic[0]+' ('+angle+')';
  var desc=topic[1];
  var content=topic[0]+' \u2014 '+topic[1];
  return {
    id:id, title:title, description:desc, genre:angle,
    type:'gardening knowledge record', content:content, content_completeness:'stub',
    stub_note:'Topic stub: the topic title and its one-line brief are real; the full guide article is not yet written. This record does not present shell text as a complete guide.',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('gardening-public',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();