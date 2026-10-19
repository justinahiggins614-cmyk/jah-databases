(function(){'use strict';
/* Islands Database generator — jahdb-islands-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-ISLAND-';
var TOPICS=[["Greenland", "The world's largest island, mostly covered in ice."], ["Madagascar", "The large island off Africa with unique wildlife."], ["Borneo", "The Southeast Asian island of rainforests shared by three nations."], ["Sumatra", "The large Indonesian island of volcanoes and rainforests."], ["Honshu", "Japan's largest island, home to Tokyo and Kyoto."], ["Great Britain", "The island of England, Scotland, and Wales."], ["Iceland", "The North Atlantic island of volcanoes, geysers, and glaciers."], ["Cuba", "The largest Caribbean island nation."], ["Hawaii", "The volcanic Pacific archipelago and American state."], ["The Galapagos", "The Ecuadorian islands famed for unique wildlife and Darwin's studies."], ["Easter Island", "The remote Pacific island of the giant moai statues."], ["Santorini", "The Greek island of white villages on a volcanic caldera."], ["Bali", "The Indonesian island known for beaches and temples."], ["The Maldives", "The Indian Ocean nation of low coral atolls."], ["Sicily", "The large Mediterranean island off Italy's toe."], ["Crete", "The largest Greek island, home of Minoan civilization."], ["New Guinea", "The large Pacific island of immense cultural diversity."], ["Tasmania", "The Australian island state of wilderness."], ["Sri Lanka", "The teardrop island nation off India."], ["Taiwan", "The island off China's southeast coast."], ["New Zealand", "The two-island Pacific nation of dramatic landscapes."], ["The Caribbean", "The tropical island region of the West Indies."], ["Volcanic Islands", "Islands built by erupting volcanoes."], ["Coral Atolls", "Ring-shaped islands built by coral reefs."], ["Archipelagos", "Chains and clusters of islands."], ["Island Biogeography", "Why islands grow such unique species."], ["Island Nations", "Countries made entirely of islands."], ["Tides and Islands", "How sea level shapes island life."], ["Surtsey: The Newborn Island", "Surtsey, off Iceland, was born in a 1963 volcanic eruption and has been a pristine natural laboratory ever since."], ["The Galapagos: Evolution's Showcase", "The Galapagos Islands' finches and tortoises inspired Darwin and remain evolution's most famous classroom."], ["Easter Island: The Mystery of Rapa Nui", "Easter Island's moai statues and deforestation are archaeology's great cautionary tale."], ["Socotra: The Alien Archipelago", "Socotra, off Yemen, hosts flora found nowhere else: dragon's blood trees and desert roses in a landscape like science fiction."], ["The Azores: The Green Atlantic", "The Azores, nine volcanic islands in the mid-Atlantic, are Portugal's green archipelago of crater lakes and hydrangeas."], ["Palau: The Conservation Pioneer", "Palau created one of the world's largest marine sanctuaries and requires visitors to sign an environmental pledge stamped in their passports."], ["The Faroe Islands: The Windy North", "The Faroe Islands, between Iceland and Norway, are 18 windswept islands of grass roofs and seabird cliffs."], ["Komodo: Dragon Island", "Komodo's dragons are the world's largest lizards, 3-meter predators that dominate their islands."], ["The Maldives: The Sinking Paradise", "The Maldives, averaging 1.5 meters above sea level, is the world's lowest nation and climate change's front line."], ["Iceland: The Fire Island", "Iceland sits on the Mid-Atlantic Ridge, where the island grows as the plates pull apart."], ["The Seychelles: The Granite Islands", "The Seychelles' inner islands are granite, the only oceanic granite islands in the world, with the coco de mer palm."], ["Tasmania: The Island Ark", "Tasmania's isolation preserved species extinct on the mainland, including the Tasmanian devil's last refuge."], ["The Hebrides: The Edge of Europe", "Scotland's Hebrides are islands of Gaelic culture, machair grasslands, and Atlantic storms."], ["Okinawa: The Island of Longevity", "Okinawa's residents are among the world's longest-lived, a Blue Zone of diet, community, and purpose."], ["The Falklands: The Windy South", "The Falkland Islands are South Atlantic outposts of penguins, albatrosses, and sheep stations."],
 ["Zanzibar: The Spice Island", "Zanzibar, the spice island off Tanzania, perfumed the world's trade for 500 years: cloves, cinnamon, and nutmeg from its plantations once supplied 80 percent..."],
 ["The Lofoten Islands: Arctic Light", "The Lofoten islands rise from the Norwegian Sea like a dragon's spine, 80 islands above the Arctic Circle where the Gulf Stream keeps the climate improbably ..."],
 ["Jeju: The Volcanic Island", "Jeju, South Korea's volcanic island, was born of fire 2 million years ago: Hallasan's 1,947-meter peak anchors the island, and 360 parasitic cones dot the la..."],
 ["The Orkney Islands: Neolithic Heart", "Orkney's 70 islands hold the densest concentration of Neolithic sites in Europe: Skara Brae, a 5,000-year-old village with stone furniture, predates Stonehen..."],
 ["Kauai: The Garden Isle", "Kauai, Hawaii's oldest island at 5 million years, is the Garden Isle: 97 percent of it is undeveloped, a green so intense it seems backlit, fed by Mount Waia..."],
 ["The Isle of Skye: Mist and Mountains", "Skye, Scotland's misty isle, wears weather like a mood: the Cuillin ridge, 12 kilometers of jagged gabbro, draws climbers into cloud, and the island's 10,000..."],
 ["Sri Lanka: The Teardrop Isle", "Sri Lanka, the teardrop isle off India's tip, packs 2,500 years of recorded history into 65,000 square kilometers: 8 UNESCO sites, from Sigiriya's rock fortr..."],
 ["The Channel Islands: Between Two Worlds", "The Channel Islands sit 20 kilometers off France but belong to the British Crown, a constitutional quirk 800 years old, with their own parliaments, currencie..."],
 ["Vancouver Island: The Pacific Rainforest", "Vancouver Island holds some of Earth's last great temperate rainforests: 800-year-old Douglas firs 90 meters tall in Cathedral Grove, and the island's 870,00..."],
 ["Naxos: The Cyclades' Green Heart", "Naxos, the largest Cyclade at 430 square kilometers, is the archipelago's green heart: while its neighbors are whitewashed rock, Naxos grows potatoes, olives..."]];
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
    type:'islands record', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('islands',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();