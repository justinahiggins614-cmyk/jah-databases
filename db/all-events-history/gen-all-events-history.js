(function(){'use strict';
/* All Events in History Database generator — jahdb-all-events-history-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-EVENT-';
var TOPICS=[["Neolithic Revolution", "The shift from hunting and gathering to farming, around 10,000 BCE, reshaping human society."], ["Rise of Mesopotamia", "The first cities and writing systems emerge in the Fertile Crescent."], ["The Egyptian Pyramids", "Monumental tombs of the Old Kingdom, built around 2600-2500 BCE."], ["Code of Hammurabi", "One of the earliest written legal codes, Babylon circa 1754 BCE."], ["First Olympic Games", "Traditionally dated to 776 BCE in Olympia, Greece."], ["Founding of the Roman Republic", "Rome overthrows its kings circa 509 BCE, beginning republican rule."], ["Alexander the Great", "His conquests (336-323 BCE) spread Hellenistic culture across three continents."], ["Great Wall of China Begins", "Early walls unified under Qin Shi Huang around 220 BCE."], ["Fall of Western Rome", "The Western Roman Empire ends in 476 CE, marking the close of antiquity in Europe."], ["Islamic Golden Age", "Centers of science and scholarship flourish from the 8th to 13th centuries."], ["Charlemagne Crowned", "Crowned emperor in 800 CE, shaping medieval Europe."], ["Viking Age", "Norse expansion across Europe and the Atlantic, roughly 793-1066."], ["Norman Conquest of England", "William the Conqueror's victory at Hastings in 1066."], ["Magna Carta", "King John seals the charter at Runnymede in 1215, limiting royal power."], ["The Black Death", "The plague of 1347-1351 kills a third of Europe's population."], ["The Renaissance", "Revival of art, science, and learning in Europe from the 14th century."], ["Gutenberg's Printing Press", "Movable type printing around 1440 revolutionizes knowledge spread."], ["Columbus Reaches the Americas", "1492 voyage connects the Eastern and Western Hemispheres."], ["Protestant Reformation", "Martin Luther's 1517 theses spark religious transformation in Europe."], ["The Scientific Revolution", "Copernicus to Newton reshape humanity's understanding of nature."], ["American Revolution", "Thirteen colonies win independence, 1775-1783."], ["French Revolution", "1789 uprising topples the monarchy and spreads revolutionary ideals."], ["Industrial Revolution", "Mechanization transforms economies from the late 18th century."], ["Abolition of Slavery", "Britain abolishes slavery in 1833; the US follows in 1865."], ["World War I", "The 1914-1918 global conflict redraws maps and topples empires."], ["World War II", "The 1939-1945 war, the deadliest conflict in human history."], ["Moon Landing 1969", "Apollo 11 lands humans on the Moon on July 20, 1969."], ["Fall of the Berlin Wall", "November 9, 1989: the Cold War's symbolic end."], ["September 11 Attacks", "The 2001 terrorist attacks reshape global security policy."], ["COVID-19 Pandemic", "The 2020 pandemic transforms public health worldwide."], ["The Roanoke Colony Vanishing of 1590", "In 1590, John White returned to the Roanoke colony off North Carolina to find all 115 settlers gone, with only the word CROATOAN carved into a fence post."], ["The Tunguska Blast of 1908", "On June 30, 1908, a blast flattened 2,000 square kilometers of Siberian forest with the force of 10 to 15 megatons, yet left no crater and no meteorite fragments."], ["The D.B. Cooper Skyjacking of 1971", "On November 24, 1971, a man calling himself Dan Cooper hijacked a Boeing 727 over the Pacific Northwest, collected $200,000 in ransom, and parachuted into a stormy night, never to be seen again."], ["The Mary Celeste Abandonment of 1872", "On December 4, 1872, the brigantine Mary Celeste was found adrift near the Azores, seaworthy and fully provisioned, but with all ten people aboard vanished."], ["The Somerton Man of 1948", "On December 1, 1948, an unidentified well-dressed man was found dead on Somerton Beach in Adelaide, Australia, with no cause of death determinable and all clothing labels removed."], ["The Hessdalen Lights of Norway", "Since the early 1980s, the Hessdalen valley in Norway has produced recurring unexplained lights, some tracked on radar moving at thousands of kilometers per hour."], ["The Green Children of Woolpit", "In 12th-century England, two children with green-tinged skin appeared in the village of Woolpit, speaking an unknown language and refusing all food but raw beans."], ["The Dancing Plague of 1518", "In July 1518, residents of Strasbourg began dancing uncontrollably in the streets for days, some reportedly dancing until collapse or death."], ["The Bloop of 1997", "In 1997, NOAA hydrophones picked up an ultra-low-frequency sound, dubbed the Bloop, powerful enough to be heard across 5,000 kilometers of the Pacific."], ["The Max Headroom Broadcast Intrusion of 1987", "On November 22, 1987, two Chicago television broadcasts were hijacked by a person in a Max Headroom mask, ranting incoherently for 90 seconds before engineers cut the signal."], ["The Lead Masks Case of 1966", "In August 1966, two Brazilian technicians were found dead on Vintem Hill near Rio de Janeiro, wearing lead eye masks, with no injuries and no clear cause of death."], ["The SS Ourang Medan Legend", "The story goes that in 1947 or 1948, ships near the Strait of Malacca received a distress call from the freighter Ourang Medan reporting the entire crew dead, followed by silence."], ["The 1561 Nuremberg Broadsheet", "On April 14, 1561, the people of Nuremberg reported a dawn sky full of strange shapes, crosses, globes, and cylinders apparently battling above the city, recorded in a famous woodcut broadsheet."], ["The Kentucky Meat Shower of 1876", "On March 3, 1876, chunks of meat fell from a clear sky over Bath County, Kentucky, covering an area roughly 100 by 50 yards."], ["The Vanishing of the Sodder Children", "On Christmas Eve 1945, the Sodder family home in Fayetteville, West Virginia, burned down; five of the ten Sodder children were never found, dead or alive."]];
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
    type:'historical event record', content:content, content_completeness:'stub',
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('all-events-history',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}

/* Group-0 expansion: 10 new topics. */
TOPICS.push(
["The Tunguska Event (1908)","June 30, 1908: an explosion over Siberia flattens 80 million trees — with no crater and no meteorite ever found."],
["The Dyatlov Pass Incident (1959)","Nine experienced hikers die in the Urals after fleeing their tent — cut open from the inside — into −30°C night."],
["The Voynich Manuscript","A 600-year-old book in an unknown language, full of unknown plants and naked nymphs — unreadable to this day."],
["The Wow! Signal (1977)","August 15, 1977: a 72-second blast of radio from deep space, thirty times louder than background — never repeated."],
["The Somerton Man (Tamam Shud)","December 1948: a well-dressed man is found dead on an Adelaide beach — no ID, no cause of death, and a scrap of Persian poetry in his pocket."],
["The Lead Masks Case","1966: two men found dead on a Brazilian hill wearing lead eye masks — with a note: “protect your face, wear the mask.”"],
["The Hessdalen Lights","Since the 1940s, glowing orbs have danced over a Norwegian valley — measured by science, explained by no one."],
["The Max Headroom Incident (1987)","November 22, 1987: a masked figure hijacks Chicago TV twice in one night — and is never caught."],
["The Disappearance of the Sodder Children (1945)","Christmas Eve 1945: the Sodder home burns down — five children vanish, no remains found, and the family never believes the official story."],
["The Bloop (1997)","Summer 1997: hydrophones catch an ultra-low-frequency sound louder than a blue whale — from the deep Pacific. NOAA never identified it."]
);
})();