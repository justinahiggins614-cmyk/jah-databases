(function(){'use strict';
/* All Events in History Database generator — jahdb-all-events-history-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-EVENT-';
var TOPICS=[["Neolithic Revolution", "The shift from hunting and gathering to farming, around 10,000 BCE, reshaping human society."], ["Rise of Mesopotamia", "The first cities and writing systems emerge in the Fertile Crescent."], ["The Egyptian Pyramids", "Monumental tombs of the Old Kingdom, built around 2600-2500 BCE."], ["Code of Hammurabi", "One of the earliest written legal codes, Babylon circa 1754 BCE."], ["First Olympic Games", "Traditionally dated to 776 BCE in Olympia, Greece."], ["Founding of the Roman Republic", "Rome overthrows its kings circa 509 BCE, beginning republican rule."], ["Alexander the Great", "His conquests (336-323 BCE) spread Hellenistic culture across three continents."], ["Great Wall of China Begins", "Early walls unified under Qin Shi Huang around 220 BCE."], ["Fall of Western Rome", "The Western Roman Empire ends in 476 CE, marking the close of antiquity in Europe."], ["Islamic Golden Age", "Centers of science and scholarship flourish from the 8th to 13th centuries."], ["Charlemagne Crowned", "Crowned emperor in 800 CE, shaping medieval Europe."], ["Viking Age", "Norse expansion across Europe and the Atlantic, roughly 793-1066."], ["Norman Conquest of England", "William the Conqueror's victory at Hastings in 1066."], ["Magna Carta", "King John seals the charter at Runnymede in 1215, limiting royal power."], ["The Black Death", "The plague of 1347-1351 kills a third of Europe's population."], ["The Renaissance", "Revival of art, science, and learning in Europe from the 14th century."], ["Gutenberg's Printing Press", "Movable type printing around 1440 revolutionizes knowledge spread."], ["Columbus Reaches the Americas", "1492 voyage connects the Eastern and Western Hemispheres."], ["Protestant Reformation", "Martin Luther's 1517 theses spark religious transformation in Europe."], ["The Scientific Revolution", "Copernicus to Newton reshape humanity's understanding of nature."], ["American Revolution", "Thirteen colonies win independence, 1775-1783."], ["French Revolution", "1789 uprising topples the monarchy and spreads revolutionary ideals."], ["Industrial Revolution", "Mechanization transforms economies from the late 18th century."], ["Abolition of Slavery", "Britain abolishes slavery in 1833; the US follows in 1865."], ["World War I", "The 1914-1918 global conflict redraws maps and topples empires."], ["World War II", "The 1939-1945 war, the deadliest conflict in human history."], ["Moon Landing 1969", "Apollo 11 lands humans on the Moon on July 20, 1969."], ["Fall of the Berlin Wall", "November 9, 1989: the Cold War's symbolic end."], ["September 11 Attacks", "The 2001 terrorist attacks reshape global security policy."], ["COVID-19 Pandemic", "The 2020 pandemic transforms public health worldwide."]];
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
})();