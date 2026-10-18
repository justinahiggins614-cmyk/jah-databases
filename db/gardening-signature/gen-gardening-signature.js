(function(){'use strict';
/* Signature Gardening Database generator — jahdb-gardening-signature-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-GARD-SIG-';
var TOPICS=[["Signature Soil Jar Test", "A Signature-original shake-and-settle method for reading soil texture."], ["Signature No-Dig Beds", "An original layering method building beds without tilling."], ["Signature Compost Thermometer", "A Signature perspective managing hot piles by temperature."], ["Signature Seed Calendar", "An original local planting calendar anyone can build."], ["Signature Succession Chart", "A Signature-original chart keeping harvests continuous."], ["Signature Drip Irrigation DIY", "An original low-cost drip setup from hardware parts."], ["Signature Tomato Training", "A Signature perspective on pruning tomatoes for yield."], ["Signature Herb Spiral", "An original build stacking microclimates for herbs."], ["Signature Pollinator Corridor", "A Signature-original plan linking blooms across seasons."], ["Signature Pest Patrol", "An original scouting routine catching problems early."], ["Signature Beneficial Insects", "A Signature perspective recruiting predators, not pesticides."], ["Signature Mulch Math", "An original calculation for exactly how much mulch to buy."], ["Signature Rain Barrel System", "A Signature-original setup for harvesting roof water."], ["Signature Worm Bin", "An original indoor vermicomposting method without odor."], ["Signature Seed Saving", "A Signature perspective saving true-to-type seeds."], ["Signature Cut Flower Garden", "An original plan for bouquets all season."], ["Signature Fall Garden", "A Signature-original method for autumn harvests."], ["Signature Frost Protection", "An original cover-and-timing system for cold snaps."], ["Signature Garden Journal", "A Signature discipline recording what worked each season."], ["Signature Kids Garden", "An original fast-reward garden plan for children."], ["Signature Balcony Farm", "A Signature perspective maximizing tiny-space harvests."], ["Signature Fruit Tree Pruning", "An original winter pruning method for beginners."], ["Signature Berry Patch", "A Signature-original layout for easy berry harvests."], ["Signature Garden Tool Kit", "An original minimal set of tools that covers everything."], ["Signature Harvest Preservation", "A Signature perspective on canning, drying, and freezing."], ["Venus Flytrap: The Snap Trap", "Carnivorous plant: the Venus flytrap, the snap trap that counts."], ["Pitcher Plants: The Pitfall", "Carnivorous plant: the pitcher, the pitfall trap."], ["Sundews: The Sticky Tentacles", "Carnivorous plant: the sundew, the sticky flypaper."], ["Butterworts: The Greasy Leaf", "Carnivorous plant: the butterwort, the greasy leaf trap."], ["Bladderworts: The Vacuum Trap", "Carnivorous plant: the bladderwort, the fastest trap in nature."], ["Cobra Lily: The Lobster Pot", "Carnivorous plant: the cobra lily, the lobster-pot trap."], ["Tropical Pitchers: Nepenthes", "Carnivorous plant: the tropical pitchers, the giants."], ["Albany Pitcher: Cephalotus", "Carnivorous plant: the Albany pitcher, the monotypic marvel."], ["Roridula: The Symbiotic Sticky", "Carnivorous plant: the Roridula, the sticky plant that outsources digestion."], ["Brocchinia: The Carnivorous Bromeliad", "Carnivorous plant: the bromeliad that eats, Brocchinia reducta."], ["Growing Carnivores", "Carnivorous plants: the growing guide."], ["The Bog Garden", "Carnivorous plants: the bog garden, the habitat recreated."], ["Conservation", "Carnivorous plants: the conservation crisis."], ["Feeding Time", "Carnivorous plants: the feeding guide."], ["The Carnivore's Lure", "Carnivorous plants share a lure: the sweet promise."]];
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
    type:'signature gardening creation', content:content, content_completeness:'stub',
    stub_note:'Topic stub: the topic title and its one-line brief are real; the full guide article is not yet written. This record does not present shell text as a complete guide.',
    demo:null, src:'signature', _seed:seed
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('gardening-signature',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();