(function(){'use strict';
/* Signature Oddities Database generator — jahdb-oddities-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-ODD-';
var TOPICS=[["The Winchester Mystery House", "Sarah Winchester's San Jose mansion has stairs to nowhere and doors opening onto walls; historians debate whether grief, guilt, or showmanship drove the endless construction."], ["The Catacombs of Paris", "Tunnels hold the stacked bones of six million Parisians; unauthorized explorers, called cataphiles, still map uncharted sections."], ["The Dancing House of Prague", "A deconstructivist building looks mid-collapse; locals nicknamed it Fred and Ginger after the dancing pair."], ["Crooked Forest of Poland", "Hundreds of pines bend at identical right angles near Gryfino; theories include human shaping, snow damage, and gravitational anomaly \u2014 none confirmed."], ["The Door to Hell in Turkmenistan", "A natural-gas crater has burned since 1971 after Soviet engineers set it alight; the president has ordered it extinguished more than once."], ["The Floating Islands of Lake Titicaca", "The Uros people live on woven reed islands they continually rebuild; the buoyant totora construction has lasted centuries."], ["The Hill of Crosses in Lithuania", "Hundreds of thousands of crosses cover two hillocks despite Soviet bulldozing; it stands as a monument to peaceful resistance."], ["The Cat Island of Aoshima", "Cats outnumber humans on this Japanese island; the feline population arrived to control mice on fishing boats."], ["The Bunny Island of \u014ckunoshima", "Hundreds of rabbits roam an island once used for chemical weapons; the bunnies likely descend from test animals or released pets."], ["The Snake Island of Brazil", "Ilha da Queimada Grande hosts thousands of golden lanceheads; the navy bans visitors, and poachers risk death for the venom trade."], ["The Upside-Down House Craze", "Tourist attractions worldwide build fully inverted homes; the disorientation is a deliberate, engineered illusion."], ["The Longest Staircases", "Switzerland's Niesenbahn stairs climb 11,674 steps; the annual race up them is one of the world's most grueling."], ["The Narrowest Streets", "Germany's Spreuerhofstra\u00dfe narrows to 31 centimeters; traffic-light pedestrian systems manage single-file flow elsewhere."], ["The Church of Bones in Kutn\u00e1 Hora", "The Sedlec Ossuary decorates with the bones of 40,000 people; a 19th-century woodcarver arranged chandeliers and coats of arms from skeletons."], ["Capuchin Crypts of Rome", "Monks' bones form baroque patterns in a crypt beneath Santa Maria della Concezione; the arrangement was devotional, not morbid display."], ["The Hanging Coffins of Sagada", "Filipino elders are buried in coffins hung on cliffs; the practice keeps the dead closer to ancestral spirits, by local belief."], ["The Mummies of Guanajuato", "Naturally desiccated bodies, exhumed over unpaid burial taxes, now draw crowds; the mineral-rich soil did the preserving."], ["The Fairy Chimneys of Cappadocia", "Wind-carved rock spires house ancient cave dwellings; early Christians hid entire cities underground here."], ["The Salar de Uyuni Mirror Effect", "A thin water layer turns Bolivia's salt flat into a perfect mirror; lithium beneath it now powers batteries worldwide."], ["The Chocolate Hills of Bohol", "Over a thousand grass-covered mounds turn brown in dry season; geologists attribute them to uplifted coral limestone."], ["The Eye of the Sahara", "The Richat Structure's concentric rings are visible from space; once thought an impact crater, it's now mapped as an eroded dome."], ["Fly Geyser's Accidental Colors", "A 1960s well-drilling accident created a growing, algae-painted geyser in Nevada; thermophilic bacteria supply the rainbow palette."], ["The Wave Rock of Australia", "A granite cliff curls like a breaking wave; chemical weathering, not water, sculpted the 15-meter overhang."], ["Pamukkale's Travertine Terraces", "Hot springs deposit white calcium terraces in Turkey; Romans bathed here, and modern rules protect the fragile formations."], ["The Marble Caves of Chile", "Lake General Carrera's waves polished marble into swirling caverns; the blue color comes from glacial flour in the water."], ["Socotra's Alien Trees", "Dragon's blood trees and bottle trees evolved in isolation off Yemen; a third of the island's plants grow nowhere else."], ["The Valley of the Moon", "Bolivia's maze of clay spires erodes into lunar shapes; each rainy season redraws the labyrinth."], ["Odd Museums of the World", "From hair museums to lunchbox museums, niche collections reveal what ordinary people consider worth preserving."]];
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
    type:'oddities exploration', content:content,
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('oddities',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();