(function(){'use strict';
/* Signature Lost Civilizations Database generator — jahdb-lost-civilizations-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-LOST-CIV-';
var TOPICS=[["Atlantis: Plato's Allegory", "Plato described an island empire sunk in a day; scholars read it as political allegory, while seekers place it from Santorini to Antarctica."], ["The Santorini Hypothesis", "The Minoan eruption around 1600 BCE devastated a real Aegean civilization; some researchers link its memory to the Atlantis story."], ["Lemuria: A Sunken Continent", "19th-century zoologists proposed a land bridge for lemur fossils; theosophists turned it into a lost civilization of legend."], ["Mu and James Churchward", "A British occultist claimed tablets revealed a Pacific motherland; no such tablets have ever been produced for study."], ["Hyperborea of the Far North", "Greek writers placed a blessed people beyond the north wind; later mystics mapped it onto Arctic fantasies."], ["El Dorado: The Gilded Man", "A Muisca chief's golden ritual became a lost city; centuries of expeditions found only jungle and disappointment."], ["The Seven Cities of Cibola", "Spanish explorers sought golden cities in the American Southwest; they found Zuni pueblos of adobe and turquoise."], ["Paititi and the Inca Refuge", "Legends tell of a jungle city where Incas hid gold; lidar surveys keep the search technically alive."], ["The Lost City of Z", "Percy Fawcett vanished in 1925 seeking a Brazilian metropolis; archaeology later found real Amazonian earthworks nearby."], ["Great Zimbabwe's True Builders", "Colonial myth credited foreigners for the stone city; archaeology confirms Shona ancestors built it between 1100\u20131450 CE."], ["The Nok Culture's Mystery", "West Africa's iron-working Nok left stunning terracottas but no written records; their decline around 500 CE remains debated."], ["The Indus Valley Script", "Harappa and Mohenjo-daro's writing is still undeciphered; without bilingual texts, the civilization's voice stays silent."], ["G\u00f6bekli Tepe's Rewriting of History", "A 12,000-year-old temple complex predates agriculture; it suggests ritual drove civilization, not the reverse."], ["The Sea Peoples Enigma", "Around 1177 BCE, mysterious raiders helped topple Bronze Age kingdoms; their identity is still argued."], ["The Minoan Disappearance", "Crete's palace culture faded after 1450 BCE; Mycenaean takeover, eruption aftermath, or both remain candidates."], ["The Olmec Colossal Heads", "Seventeen basalt heads mark Mesoamerica's mother culture; how they moved 40-ton stones is still modeled."], ["Teotihuacan's Unknown Builders", "A metropolis of 100,000+ rose near modern Mexico City; even the Aztecs didn't know who built it."], ["The Nazca Lines' Purpose", "Giant geoglyphs best seen from above; ritual procession paths are the leading scholarly explanation."], ["Easter Island's Real Story", "Rapa Nui's moai builders did not simply ecocide themselves; new research emphasizes rats, disease, and resilience."], ["The Cahokia Mounds", "North America's largest pre-Columbian city held 15,000 people; its decline around 1350 CE is still investigated."], ["The Anasazi Abandonment", "Cliff dwellers left the Four Corners around 1300 CE; drought, conflict, and migration all factor into the leading models."], ["Angkor's Hydraulic Collapse", "The Khmer capital's vast waterworks may have failed in climate shifts; lidar revealed a far larger city than imagined."], ["The Library of Nalanda", "A great Indian university burned in the 1190s; Tibetan accounts say its manuscripts smoldered for months."], ["Tartessos of Iberia", "Greek sources describe a wealthy Atlantic kingdom; archaeologists debate whether its center lies under Seville's marshes."], ["The Etruscan Language Puzzle", "Rome's predecessors left inscriptions in a non-Indo-European tongue; only partially deciphered, it guards their literature."], ["Doggerland: Britain's Atlantis", "A inhabited North Sea plain drowned around 6500 BCE; fishing trawlers still pull up mammoth bones and tools."], ["Yonaguni's Underwater Steps", "Submerged rock terraces off Japan divide geologists; natural fracturing explains the forms, though some argue for carving."], ["Bimini Road's Stones", "Underwater limestone blocks off the Bahamas sparked Atlantis claims; geologists identify natural beachrock fracturing."]];
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
    type:'lost civilizations exploration', content:content,
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('lost-civilizations',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();