(function(){'use strict';
/* Signature Curiosities Database generator — jahdb-curiosities-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-CURIO-';
var TOPICS=[["The Library of Alexandria's True Fate", "The great library declined over centuries, not in one fire; scholars now see its loss as slow neglect rather than single catastrophe."], ["Antikythera Mechanism", "A 2,000-year-old Greek device predicted eclipses with bronze gears; nothing of comparable complexity appears again for a millennium."], ["Roman Concrete's Self-Healing", "Ancient harbor concrete grows stronger with seawater; MIT researchers found lime clasts that seal cracks, inspiring modern mixes."], ["Damascus Steel's Lost Recipe", "Crusader-era blades showed watery patterns from carbon nanotubes; the original wootz-steel supply chain collapsed, taking the method with it."], ["Greek Fire: The Secret Weapon", "Byzantine ships sprayed an unquenchable flame; the formula was a state secret so well kept that it vanished entirely."], ["The Baghdad Battery", "A 2,000-year-old clay pot with copper and iron parts could, in theory, hold a small charge; archaeologists debate whether it was a battery or a storage vessel."], ["Viking Sunstones", "Norse sailors may have navigated by polarized light through calcite crystals; experiments show the method works on overcast days."], ["The Phaistos Disc", "A Minoan clay disc stamped with pictographs remains undeciphered; its printing-like technique predates movable type by 3,000 years."], ["The Saqqara Bird", "A 2,200-year-old Egyptian wooden carving resembles a glider; aerodynamic tests suggest it could glide, though ritual purpose is more likely."], ["Nimrud Lens", "A 3,000-year-old rock-crystal lens from Assyria may have been a magnifier or a fire-starter; either use shows surprising optics knowledge."], ["The London Beer Flood", "In 1814 a vat burst released a tidal wave of porter through London streets; eight people died, and the brewery was ruled an act of God."], ["The Dancing Plague Revisited", "Strasbourg's 1518 dancing mania remains a case study; modern scholars weigh ergot poisoning against mass psychogenic illness."], ["The Great Molasses Flood", "A 1919 Boston tank burst sent molasses through the North End at 35 mph; the disaster reshaped industrial safety law."], ["The Tunguska Airburst", "Siberia's 1908 blast is now modeled as a stony meteoroid exploding midair; expeditions found no crater, only flattened forest."], ["Ball Lightning in the Lab", "Researchers have created glowing plasma orbs with silicon vapor; whether these match witness reports remains open."], ["The Taos Hum", "Some residents hear a persistent low drone; acoustic surveys found industrial sources for some hearers and nothing for others."], ["Spontaneous Glass Breakage", "Nickel sulfide inclusions can shatter tempered glass years after installation; engineers now heat-soak panels to force early failures."], ["The Money Pit of Oak Island", "Treasure hunters have dug for 200 years on a Nova Scotian island; every expedition finds tantalizing wood and stone, never treasure."], ["The Beale Ciphers", "Three coded texts allegedly point to buried Virginia gold; two ciphers remain unsolved, and skeptics doubt the treasure exists."], ["Forrest Fenn's Treasure Hunt", "A millionaire hid a chest in the Rockies in 2010; it was found in 2020, spawning lawsuits and copycat hunts."], ["The Amber Room", "Nazi-looted amber panels from Russia's Catherine Palace vanished in 1945; a replica was completed in 2003 while the original stays missing."], ["The Ark of the Covenant's Trail", "Ethiopian tradition holds the ark in Axum; historians trace the claim through medieval chronicles, not archaeology."], ["The Holy Grail Candidates", "Dozens of cups claim the title across Europe; scholars treat the grail as literary symbol rather than findable object."], ["El Dorado's Golden Origins", "A Muisca ritual of gold-dusted chiefs became a lost-city legend; conquistadors chased it for a century across South America."], ["The Seven Cities of Cibola", "Coronado marched thousands of miles seeking golden cities; he found adobe pueblos and returned empty-handed."], ["Paititi: The Lost Inca City", "Explorers still search Peruvian jungles for a refuge city; satellite lidar keeps the hope alive without confirmation."], ["The Curious Case of the Cardiff Giant", "An 1869 'petrified man' drew paying crowds; its carver confessed it was gypsum, making it America's great archaeological hoax."], ["Piltdown Man's Exposure", "A forged 'missing link' fooled Britain for 40 years; fluorine testing in 1953 exposed the orangutan-jaw fraud."]];
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
    type:'curiosities exploration', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('curiosities',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();