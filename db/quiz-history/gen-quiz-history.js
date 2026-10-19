(function(){'use strict';
/* EXPANSION 2026-10-18 group-1: archive-shape branches added. */
/* JAH The History Quiz Database generator — jahdb-quiz-history-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-QZHI-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Ancient Egypt Basics Quiz - Ancient History",
  "Ancient Greece Origins Quiz - Ancient History",
  "Roman Empire Foundations Quiz - Ancient History",
  "Mesopotamia First Civilizations Quiz - Ancient History",
  "Pharaohs and Pyramids Quiz - Ancient History",
  "Athens and Sparta Quiz - Ancient History",
  "Renaissance Quiz - Modern History"
 ],
 "Compounded": [
  "Roman Republic Quiz - Ancient History",
  "Early Middle Ages Quiz - Medieval History",
  "Vikings and Norse Voyages Quiz - Medieval History",
  "Age of Exploration Quiz - Modern History",
  "Ancient China Dynasties Quiz - Ancient History",
  "Persian Empire Quiz - Ancient History",
  "Byzantine Empire Quiz - Medieval History",
  "Reformation Quiz - Modern History",
  "Roman Emperors Quiz - Ancient History",
  "Crusades Quiz - Medieval History",
  "Feudalism in Medieval Europe Quiz - Medieval History",
  "American Revolution Quiz - Modern History",
  "Silk Road Quiz - World History"
 ],
 "Advanced": [
  "Mongol Empire Quiz - Medieval History",
  "Black Death Quiz - Medieval History",
  "French Revolution Quiz - Modern History",
  "Great Empires of the Americas Quiz - World History",
  "Hundred Years War Quiz - Medieval History",
  "Ottoman Rise Quiz - Medieval History",
  "Industrial Revolution Quiz - Modern History",
  "African Kingdoms Quiz - World History",
  "Late Medieval Culture Quiz - Medieval History",
  "World War I Quiz - Modern History",
  "World Revolutions Quiz - World History",
  "World War II Quiz - Modern History",
  "Cold War Quiz - Modern History",
  "Twentieth Century Milestones Quiz - World History"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Quiz — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
/* === EXPANSION 2026-10-18 group-1: History Guessing Game Database ===
   10 "Guess the ..." quizzes in the stored archive schema
   (id,t,g,name,title,description,how_it_works,questions,answers,standards,citations,
   src,ladder_rank,ladder_tier,demo[python]). Deterministic by seed. */
function quizDemoProgram(id,title,g,questions,answers){
  function py(s){return s.replace(/\\/g,"\\\\").replace(/"/g,'\\"');}
  var L=[];
  L.push("#!/usr/bin/env python3");
  L.push('"""'+py(title)+" — working demonstration.");
  L.push("Record "+id+" ["+g+"]. Property of Justin Addam Higgins (JAH).");
  L.push('"""');
  L.push("QUESTIONS = [");
  for(var i=0;i<questions.length;i++) L.push('    "'+py(questions[i])+'",');
  L.push("]");
  L.push("ANSWERS = [");
  for(var j=0;j<answers.length;j++) L.push('    "'+py(answers[j])+'",');
  L.push("]");
  L.push("def main():");
  L.push('    print("=== '+py(title)+' ===")');
  L.push("    score = 0");
  L.push("    for i, q in enumerate(QUESTIONS):");
  L.push('        print("Q%d: %s" % (i+1, q))');
  L.push('        print("A%d: %s" % (i+1, ANSWERS[i]))');
  L.push("        score += 1  # demonstration run: all answers revealed");
  L.push('    print("score: %d/%d (answers at the bottom, as always)" % (score, len(QUESTIONS)))');
  L.push('    assert len(QUESTIONS) == 10 and len(ANSWERS) == 10');
  L.push('    assert all(isinstance(a, str) and len(a) > 0 for a in ANSWERS)');
  L.push('    print("OK: '+py(title).slice(0,40)+' quiz complete")');
  L.push('if __name__ == "__main__":');
  L.push("    main()");
  return L.join("\n")+"\n";
}
var GUESSING_QUIZZES=[
{t:"Guess the Monarch",g:"Medieval History",
 desc:"A guessing game through royal history: ten clues, ten monarchs — from the conquerors to the reformers. Read each clue, guess the ruler, then check your score at the bottom.",
 how:"How to take this quiz. Read the ten clues in order and guess each monarch before looking at the answers, which sit at the bottom of this record. Score yourself one point per correct answer: 9 to 10 is mastery, 7 to 8 is strong, 5 to 6 is solid, below 5 means the thrones need another visit.",
 q:["I was crowned in 1066 after winning a famous battle near Hastings. Who am I?",
    "I signed the Magna Carta in 1215 after my barons rebelled. Who am I?",
    "I had six wives and founded the Church of England. Who am I?",
    "I was the 'Sun King' who built Versailles and ruled France for 72 years. Who am I?",
    "I was Queen of England for 63 years, giving my name to an era of empire. Who am I?",
    "I conquered Persia and Egypt before dying at 32 in Babylon. Who am I?",
    "I was the first Holy Roman Emperor, crowned on Christmas Day 800. Who am I?",
    "I led the Mongols to build history's largest land empire. Who am I?",
    "I was the Macedonian king whose mother was Olympias — no, the other one: I ruled Egypt and founded a dynasty. Who am I?",
    "I was the Russian tsar who modernized Russia and built St. Petersburg. Who am I?"],
 a:["William the Conqueror.","King John.","Henry VIII.","Louis XIV.","Queen Victoria.","Alexander the Great.","Charlemagne.","Genghis Khan.","Ptolemy I Soter.","Peter the Great."],
 std:["Era: World monarchs, ancient to modern","Difficulty: medium - compounded","Format: 10 clues, answers at the bottom"],
 cit:["Roberts JM. The New Penguin History of the World. Penguin; 2004."],
 rank:4,tier:"compounded"},
{t:"Guess the Treaty",g:"Modern History",
 desc:"A guessing game through the treaties that redrew the world: ten clues, ten agreements — from Westphalia to the present. Guess each treaty, then check the answers.",
 how:"How to take this quiz. Read the ten clues in order and guess each treaty before looking at the answers, which sit at the bottom of this record. Score yourself one point per correct answer: 9 to 10 is mastery, 7 to 8 is strong, 5 to 6 is solid, below 5 means the diplomats need another visit.",
 q:["I ended the Thirty Years' War in 1648 and established state sovereignty. What am I?",
    "I ended World War I with Germany in 1919 and redrew the map of Europe. What am I?",
    "I was signed in 1215 between King John and his barons, limiting royal power. What am I?",
    "I was the 1783 agreement in which Britain recognized American independence. What am I?",
    "I was the 1945 charter that founded the United Nations. What am I?",
    "I was the 1868 agreement... no: I was the 1803 purchase that doubled the United States. What am I?",
    "I was the 1957 treaty that founded the European Economic Community. What am I?",
    "I was the 1978 agreement between Egypt and Israel brokered at a US presidential retreat. What am I?",
    "I was the 1848 treaty ending the Mexican-American War, ceding California. What am I?",
    "I was the 1993 agreement signed on the White House lawn between Israel and the PLO. What am I?"],
 a:["The Peace of Westphalia.","The Treaty of Versailles.","The Magna Carta.","The Treaty of Paris (1783).","The UN Charter.","The Louisiana Purchase.","The Treaty of Rome.","The Camp David Accords.","The Treaty of Guadalupe Hidalgo.","The Oslo I Accord."],
 std:["Era: Treaties, 1215 to present","Difficulty: medium - compounded","Format: 10 clues, answers at the bottom"],
 cit:["Roberts JM. The New Penguin History of the World. Penguin; 2004."],
 rank:5,tier:"compounded"},
{t:"Guess the Castle",g:"Medieval History",
 desc:"A guessing game through the world's great castles: ten clues, ten fortresses — from the Tower of London to Neuschwanstein. Guess each castle, then check the answers.",
 how:"How to take this quiz. Read the ten clues in order and guess each castle before looking at the answers, which sit at the bottom of this record. Score yourself one point per correct answer: 9 to 10 is mastery, 7 to 8 is strong, 5 to 6 is solid, below 5 means the battlements need another visit.",
 q:["I am the London fortress that has been a palace, prison, and home of the Crown Jewels. What am I?",
    "I am the fairy-tale Bavarian castle built by 'Mad' King Ludwig II. What am I?",
    "I am the French château in the Loire Valley with a famous double-helix staircase. What am I?",
    "I am the Scottish castle on an extinct volcano overlooking Edinburgh. What am I?",
    "I am the Japanese 'White Heron' castle, a UNESCO site of stunning white plaster. What am I?",
    "I am the Welsh castle built by Edward I, a masterpiece of concentric defense. What am I?",
    "I am the Prague fortress that is the largest ancient castle complex in the world. What am I?",
    "I am the Spanish Alcázar that inspired Disney's Cinderella castle. What am I?",
    "I am the Krak des Chevaliers — the great Crusader castle in Syria. What am I?",
    "I am the Windsor residence, the oldest and largest inhabited castle in the world. What am I?"],
 a:["The Tower of London.","Neuschwanstein Castle.","Château de Chambord.","Edinburgh Castle.","Himeji Castle.","Caernarfon Castle.","Prague Castle.","The Alcázar of Segovia.","Krak des Chevaliers.","Windsor Castle."],
 std:["Era: Castles worldwide, medieval to modern","Difficulty: easy-medium - foundations","Format: 10 clues, answers at the bottom"],
 cit:["Pettifer J. The Castles of the World. Various editions."],
 rank:2,tier:"foundations"},
{t:"Guess the Canal",g:"Modern History",
 desc:"A guessing game through the canals that connected the world: ten clues, ten waterways — from Suez to Panama. Guess each canal, then check the answers.",
 how:"How to take this quiz. Read the ten clues in order and guess each canal before looking at the answers, which sit at the bottom of this record. Score yourself one point per correct answer: 9 to 10 is mastery, 7 to 8 is strong, 5 to 6 is solid, below 5 means the waterways need another visit.",
 q:["I connect the Mediterranean to the Red Sea and opened in 1869. What am I?",
    "I connect the Atlantic to the Pacific across Panama and opened in 1914. What am I?",
    "I am the ancient Chinese waterway, the world's longest canal. What am I?",
    "I connect the North Sea to the Baltic through Germany. What am I?",
    "I was the Erie waterway that connected the Great Lakes to the Hudson in 1825. What am I?",
    "I connect the Mediterranean to the Atlantic across southern France. What am I?",
    "I am the Manchester waterway that made an inland city a seaport. What am I?",
    "I connect the Danube to the Main, linking the North Sea to the Black Sea. What am I?",
    "I am the Corinth waterway cut through the Greek isthmus. What am I?",
    "I was the proposed Nicaraguan canal that lost out to Panama. What am I?"],
 a:["The Suez Canal.","The Panama Canal.","The Grand Canal of China.","The Kiel Canal.","The Erie Canal.","The Canal du Midi.","The Manchester Ship Canal.","The Rhine-Main-Danube Canal.","The Corinth Canal.","The Nicaragua Canal (proposed)."],
 std:["Era: Canals, ancient to modern","Difficulty: medium - compounded","Format: 10 clues, answers at the bottom"],
 cit:["Roberts JM. The New Penguin History of the World. Penguin; 2004."],
 rank:5,tier:"compounded"},
{t:"Guess the Railroad",g:"Modern History",
 desc:"A guessing game through the railroads that shrank the world: ten clues, ten lines — from the Transcontinental to the Shinkansen. Guess each railroad, then check the answers.",
 how:"How to take this quiz. Read the ten clues in order and guess each railroad before looking at the answers, which sit at the bottom of this record. Score yourself one point per correct answer: 9 to 10 is mastery, 7 to 8 is strong, 5 to 6 is solid, below 5 means the railways need another visit.",
 q:["I was completed in 1869 at Promontory Summit, joining America's coasts by rail. What am I?",
    "I am the Russian line from Moscow to Vladivostok, the world's longest railway. What am I?",
    "I was Japan's 1964 bullet train, the first high-speed rail. What am I?",
    "I am the British line whose 1825 opening began the railway age. What am I?",
    "I was the Canadian Pacific line completed in 1885, binding Canada together. What am I?",
    "I am the Orient Express route, the legendary luxury train to Istanbul. What am I?",
    "I was the 19th-century American line famous for the 'golden spike' — no, the other one: I ran the Atchison, Topeka and the... What am I?",
    "I am the Indian railway network's most famous mountain line, a UNESCO toy train. What am I?",
    "I am the Channel Tunnel rail link between Britain and France. What am I?",
    "I was the Underground Railroad — not a railroad at all, but the secret network to freedom. What am I?"],
 a:["The First Transcontinental Railroad.","The Trans-Siberian Railway.","The Tokaido Shinkansen.","The Stockton and Darlington Railway.","The Canadian Pacific Railway.","The Orient Express.","The Atchison, Topeka and Santa Fe Railway.","The Darjeeling Himalayan Railway.","The Channel Tunnel (Eurotunnel).","The Underground Railroad."],
 std:["Era: Railroads, 1825 to present","Difficulty: medium - compounded","Format: 10 clues, answers at the bottom"],
 cit:["Wolmar C. Blood, Iron, and Gold: How the Railways Transformed the World. PublicAffairs; 2010."],
 rank:6,tier:"compounded"},
{t:"Guess the Ancient Library",g:"Ancient History",
 desc:"A guessing game through the great libraries of the ancient world: ten clues, ten collections — from Alexandria to Nalanda. Guess each library, then check the answers.",
 how:"How to take this quiz. Read the ten clues in order and guess each library before looking at the answers, which sit at the bottom of this record. Score yourself one point per correct answer: 9 to 10 is mastery, 7 to 8 is strong, 5 to 6 is solid, below 5 means the scrolls need another visit.",
 q:["I was the great library of Ptolemaic Egypt, the ancient world's most famous. What am I?",
    "I was the Assyrian king's library at Nineveh, with 30,000 clay tablets. What am I?",
    "I was the ancient Indian university library at Nalanda, burned in the 1190s. What am I?",
    "I was the Pergamene library, Alexandria's great rival in Asia Minor. What am I?",
    "I was the library of the Villa of the Papyri, buried by Vesuvius. What am I?",
    "I was the Imperial Library of Constantinople, keeper of Greek learning. What am I?",
    "I was the House of Wisdom in Baghdad, heart of the Islamic Golden Age. What am I?",
    "I was the library at Ephesus, its facade still standing in Turkey. What am I?",
    "I was the ancient Chinese imperial archive, burned by Xiang Yu in 206 BCE. What am I?",
    "I was the library of Aristotle's school, the Lyceum's collection. What am I?"],
 a:["The Library of Alexandria.","The Library of Ashurbanipal.","The Nalanda library.","The Library of Pergamum.","The Villa of the Papyri library.","The Imperial Library of Constantinople.","The House of Wisdom (Bayt al-Hikmah).","The Library of Celsus.","The Qin imperial archive.","The Lyceum library."],
 std:["Era: Ancient libraries worldwide","Difficulty: hard - advanced","Format: 10 clues, answers at the bottom"],
 cit:["Casson L. Libraries in the Ancient World. Yale University Press; 2001."],
 rank:8,tier:"advanced"},
{t:"Guess the Medieval Guild",g:"Medieval History",
 desc:"A guessing game through the medieval guilds: ten clues, ten crafts — from masons to merchants. Guess each guild, then check the answers.",
 how:"How to take this quiz. Read the ten clues in order and guess each guild before looking at the answers, which sit at the bottom of this record. Score yourself one point per correct answer: 9 to 10 is mastery, 7 to 8 is strong, 5 to 6 is solid, below 5 means the workshops need another visit.",
 q:["We built the cathedrals and kept our geometry secret. What guild are we?",
    "We wove the cloth and fulling mills finished our work. What guild are we?",
    "We were the merchants of the Hanseatic League, trading across the Baltic. What guild are we?",
    "We made the gold leaf and illuminated manuscripts glow. What guild are we?",
    "We were the barber-surgeons — we cut hair and set bones. What guild are we?",
    "We baked the bread and the Assize of Bread regulated our loaves. What guild are we?",
    "We were the goldsmiths whose hallmarks guaranteed the metal. What guild are we?",
    "We tanned the hides and our quarter stank for miles. What guild are we?",
    "We were the scriveners and notaries, the literate professionals. What guild are we?",
    "We brewed the ale — and many of our masters were women. What guild are we?"],
 a:["The Masons.","The Weavers.","The Hanseatic merchants.","The Goldbeaters (and illuminators).","The Barbers (barber-surgeons).","The Bakers.","The Goldsmiths.","The Tanners.","The Scriveners.","The Brewers."],
 std:["Era: Medieval guilds","Difficulty: medium - compounded","Format: 10 clues, answers at the bottom"],
 cit:["Epstein SR, Prak M, editors. Guilds, Innovation and the European Economy. Cambridge University Press; 2008."],
 rank:6,tier:"compounded"},
{t:"Guess the Expedition",g:"Age of Exploration",
 desc:"A guessing game through history's great expeditions: ten clues, ten journeys — from Magellan to Apollo. Guess each expedition, then check the answers.",
 how:"How to take this quiz. Read the ten clues in order and guess each expedition before looking at the answers, which sit at the bottom of this record. Score yourself one point per correct answer: 9 to 10 is mastery, 7 to 8 is strong, 5 to 6 is solid, below 5 means the explorers need another visit.",
 q:["I was the 1519-1522 voyage that first circumnavigated the globe. What am I?",
    "I was the 1969 mission that first landed humans on the Moon. What am I?",
    "I was Lewis and Clark's 1804-1806 journey to the Pacific. What am I?",
    "I was the 1911 race to the South Pole, won by Amundsen. What am I?",
    "I was Columbus's 1492 voyage to the 'Indies.' What am I?",
    "I was the 1845 Franklin voyage lost in the Arctic ice. What am I?",
    "I was Shackleton's 1914-1917 Antarctic survival epic. What am I?",
    "I was the 1807-1811 voyage that mapped the Pacific Northwest coast... no: I was Cook's 1768-1771 voyage to Tahiti and New Zealand. What am I?",
    "I was the 1977 launch of the two spacecraft now in interstellar space. What am I?",
    "I was Zheng He's early-1400s treasure voyages across the Indian Ocean. What am I?"],
 a:["The Magellan-Elcano expedition.","Apollo 11.","The Lewis and Clark Expedition.","The Amundsen South Pole expedition.","Columbus's first voyage.","The Franklin Expedition.","The Imperial Trans-Antarctic Expedition (Endurance).","Cook's first voyage (Endeavour).","The Voyager program.","The Zheng He voyages."],
 std:["Era: Expeditions, 1400s to present","Difficulty: medium - compounded","Format: 10 clues, answers at the bottom"],
 cit:["Fernandez-Armesto F. Pathfinders: A Global History of Exploration. Norton; 2006."],
 rank:7,tier:"advanced"},
{t:"Guess the Coin",g:"Ancient History",
 desc:"A guessing game through the coins that made history: ten clues, ten currencies — from the Lydian stater to the dollar. Guess each coin, then check the answers.",
 how:"How to take this quiz. Read the ten clues in order and guess each coin before looking at the answers, which sit at the bottom of this record. Score yourself one point per correct answer: 9 to 10 is mastery, 7 to 8 is strong, 5 to 6 is solid, below 5 means the mint needs another visit.",
 q:["I was the Lydian electrum coin, the first true coinage, around 600 BCE. What am I?",
    "I was the Athenian silver coin with the owl, the dollar of the ancient world. What am I?",
    "I was the Roman gold coin, 45 to the pound of gold. What am I?",
    "I was the Spanish silver coin that became the first global currency. What am I?",
    "I was the British gold sovereign's predecessor, named for an angel. What am I?",
    "I was the Dutch guilder's... no: I was the Florentine gold coin that financed the Renaissance. What am I?",
    "I was the American silver dollar of 1794, the first US dollar. What am I?",
    "I was the Byzantine gold solidus, stable for 700 years. What am I?",
    "I was the Chinese bronze coin with the square hole, used for 2,000 years. What am I?",
    "I was the 20-dollar US gold piece, the classic 'double eagle.' What am I?"],
 a:["The Lydian stater.","The Athenian tetradrachm.","The aureus.","The Spanish piece of eight (peso).","The angel.","The florin.","The Flowing Hair dollar.","The solidus (bezant).","The tongbao cash coin.","The double eagle."],
 std:["Era: Coins, 600 BCE to present","Difficulty: hard - advanced","Format: 10 clues, answers at the bottom"],
 cit:["Howgego C. Ancient History from Coins. Routledge; 1995."],
 rank:9,tier:"advanced"},
{t:"Guess the Coronation",g:"Medieval History",
 desc:"A guessing game through history's great coronations: ten clues, ten crownings — from Charlemagne to Elizabeth II. Guess each coronation, then check the answers.",
 how:"How to take this quiz. Read the ten clues in order and guess each coronation before looking at the answers, which sit at the bottom of this record. Score yourself one point per correct answer: 9 to 10 is mastery, 7 to 8 is strong, 5 to 6 is solid, below 5 means the abbeys need another visit.",
 q:["I was crowned on Christmas Day 800, founding an empire. Whose coronation am I?",
    "I was crowned in 1066 on Christmas Day, the Norman conquest's seal. Whose coronation am I?",
    "I was crowned in 1559, beginning England's golden age. Whose coronation am I?",
    "I crowned myself in 1804, taking the crown from the Pope's hands. Whose coronation am I?",
    "I was crowned in 1953, the first televised coronation. Whose coronation am I?",
    "I was crowned Holy Roman Emperor in 1220, the 'Stupor Mundi.' Whose coronation am I?",
    "I was crowned in 1272... no: I was anointed in 751, founding a dynasty. Whose coronation am I?",
    "I was crowned Tsar in 1547, the first Russian to take the title. Whose coronation am I?",
    "I was crowned in 1838... no: I was crowned King of Italy in 1861, unifying a nation. Whose coronation am I?",
    "I was crowned in 1901... no: my 1877 coronation as Empress of India was proclaimed at Delhi. Whose coronation am I?"],
 a:["Charlemagne's coronation.","William the Conqueror's coronation.","Elizabeth I's coronation.","Napoleon's coronation.","Elizabeth II's coronation.","Frederick II's coronation.","Pepin the Short's anointing.","Ivan IV (the Terrible)'s coronation.","Victor Emmanuel II's coronation.","Queen Victoria's proclamation as Empress of India (1877)."],
 std:["Era: Coronations, 751 to 1953","Difficulty: hard - advanced","Format: 10 clues, answers at the bottom"],
 cit:["Roberts JM. The New Penguin History of the World. Penguin; 2004."],
 rank:10,tier:"advanced"}
];


function quizRec(seed,cat){
  var tp=GUESSING_QUIZZES[(seed-1)%GUESSING_QUIZZES.length];
  var id=PREFIX+String(seed).padStart(6,'0');
  return {id:id,t:tp.t,g:tp.g,name:tp.t,title:tp.t,
    description:tp.desc,how_it_works:tp.how,questions:tp.q,answers:tp.a,
    standards:tp.std,citations:tp.cit,src:'public-harvest',
    ladder_rank:tp.rank,ladder_tier:tp.tier,
    demo:{kind:"python",language:"python",program:quizDemoProgram(id,tp.t,tp.g,tp.q,tp.a)},
    _seed:seed};
}

function validateArchive(r){
  var e=[];
  if(!new RegExp('^JAH-QZHI-'+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.t!=='string'||!r.t.length)e.push('t');
  if(typeof r.g!=='string'||!r.g.length)e.push('g');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(typeof r.how_it_works!=='string'||!r.how_it_works.length)e.push('how_it_works');
  if(!Array.isArray(r.questions)||r.questions.length!==10)e.push('questions');
  if(!Array.isArray(r.answers)||r.answers.length!==10)e.push('answers');
  if(!Array.isArray(r.standards)||!r.standards.length)e.push('standards');
  if(!Array.isArray(r.citations)||!r.citations.length)e.push('citations');
  if(r.src!=='public-harvest'&&r.src!=='signature')e.push('src');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=10))e.push('ladder_rank');
  if(['foundations','compounded','advanced'].indexOf(r.ladder_tier)<0)e.push('ladder_tier');
  if(!r.demo||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  return e;
}
function generate(seed,opts,rnd){
  opts=opts||{};
  if(opts.category==='history-guessing-games')return quizRec(seed,opts.category);

  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — quiz record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A quiz record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"quiz-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  if(r&&typeof r==='object'&&(r.ladder_rank||r.questions)){
    var ae=validateArchive(r);return {ok:!ae.length,errors:ae};
  }
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-quiz-history-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('quiz-history',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
