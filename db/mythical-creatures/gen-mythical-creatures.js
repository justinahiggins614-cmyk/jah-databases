(function(){'use strict';
/* Signature Mythical Creatures Database generator — jahdb-mythical-creatures-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-MYTH-CRE-';
var TOPICS=[["Dragons of the East and West", "Chinese dragons bring rain and fortune while European dragons hoard and burn; both likely grew from fossil finds and snake awe."], ["The Phoenix Across Cultures", "Egypt's bennu, Greece's phoenix, and China's fenghuang all rise renewed; the firebird embodies civilization's hope of rebirth."], ["Kraken: Terror of the North Seas", "Norse sailors feared a beast that dragged ships down; giant squid specimens gave the legend a real anchor."], ["Unicorns in Medieval Bestiaries", "Bestiaries described a fierce one-horned beast tamable by virgins; narwhal tusks sold as 'alicorn' fueled the belief."], ["Griffins: Guardians of Gold", "Greek writers placed eagle-lion hybrids guarding Scythian gold; fossil protoceratops skulls may have inspired the form."], ["The Minotaur's Labyrinth", "Athens' tribute myth encoded Minoan bull rituals; archaeologists link the labyrinth to Knossos's maze-like palace."], ["Medusa and the Gorgons", "A gaze that turns flesh to stone punished and protected; the myth likely warns against looking directly at power."], ["Cerberus, Hound of Hades", "The multi-headed guard dog marked death's border; comparative myths give underworld guardians to many cultures."], ["Fenrir and Norse Monstrosities", "The bound wolf destined to kill Odin embodies chaos breaking loose; Ragnar\u00f6k made monsters cosmic."], ["J\u00f6rmungandr: The World Serpent", "Thor's destined foe encircles the world; the ouroboros image of a tail-biting serpent spans continents."], ["Kitsune: The Fox Spirits", "Japanese folklore grants foxes nine tails and shapeshifting; shrines to Inari still honor them as messengers."], ["Tengu of the Mountains", "Long-nosed mountain goblins taught swordsmen and punished the arrogant; they blend Shinto and Buddhist demonology."], ["The Naga Serpent Kings", "Hindu and Buddhist nagas rule waters and guard treasure; serpent veneration runs from India to Mesoamerica."], ["Garuda: The Bird Titan", "Vishnu's eagle mount battles the nagas; the figure became national symbols from Thailand to Indonesia."], ["Anansi the Trickster Spider", "West African tales made the spider a cunning culture hero; enslaved people carried Anansi to the Americas."], ["The Wendigo's Hunger", "Algonquian legend warns of a gaunt cannibal spirit of winter starvation; psychologists named a culture-bound syndrome after it."], ["Thunderbird Spirits", "Plains and Woodlands nations revere the great sky bird; its imagery appears on totem poles and in ceremony."], ["Selkies: The Seal People", "Celtic tales tell of seals shedding skins to become human lovers; the stories explore longing between worlds."], ["Banshees of Ireland", "A wailing woman foretells death in a household; folklorists link the cry to the traditional keening of mourners."], ["Leprechauns and Hidden Gold", "Solitary fairy cobblers guard their pots; the modern image owes more to 19th-century stage Irishness than folklore."], ["Changelings in European Folklore", "Fairies were said to steal infants and leave substitutes; historians read the belief against the realities of infant illness."], ["The Golem of Prague", "Rabbi Loew's clay protector defended the ghetto; the legend became the template for artificial-life stories."], ["Baba Yaga's Hut", "The Russian witch lives in a hut on chicken legs; she tests heroes with impossible tasks and ambiguous aid."], ["Djinn: The Smokeless Fire", "Islamic tradition holds djinn as free-willed beings of fire; the Thousand and One Nights made them global."], ["The Sphinx's Riddle", "Oedipus answered the man-beast's question; Egyptian sphinxes, unlike Greece's, were protective rather than riddling."], ["Mermaids: From Sirens to Ariel", "Sailors' sightings likely mixed manatees with longing; the siren's song evolved from deadly to romantic."], ["Cyclops and the Forge", "One-eyed giants built the gods' weapons; elephant skulls with central nasal cavities may have suggested the face."], ["Centaurs of Thessaly", "Horse-men embodied the wild edge of civilization; the image may recall first sightings of mounted riders."]];
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
    type:'mythical creatures exploration', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('mythical-creatures',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();