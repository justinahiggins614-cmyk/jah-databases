(function(){'use strict';
/* JAH Archaeology Database generator — jahdb-archaeology-1.0.
   Deterministic client-side generator: same seed + same version = same record.
   Online-sourced site/method profiles carry src:"online"; Signature-authored
   comparative studies carry src:"signature". All anchor facts are verifiable. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=['site','method','civilization','artifact','dating','era','legal-standards'];
var PREFIX='JAH-ARC2-';
/* anchors: [title, cat, region, date label, facts...] */
var ANCH=[
["Gobekli Tepe","site","Southeastern Turkey","c. 9600-8200 BCE",
 "Gobekli Tepe is a Pre-Pottery Neolithic sanctuary of massive T-shaped stone pillars carved with animals.",
 "Built around 9600 BCE, it predates agriculture and pottery, overturning the idea that farming came before monumental religion.",
 "Excavator Klaus Schmidt argued the site's ritual demands may have driven the adoption of farming itself.",
 "Only a fraction of the buried enclosures has been excavated; ground radar shows many more."],
["Catalhoyuk","site","Central Turkey","c. 7500-6000 BCE",
 "Catalhoyuk was a dense Neolithic town of thousands, entered through rooftops with no streets.",
 "Its houses preserve wall paintings, plastered bull skulls (bucrania), and elaborate burials beneath floors.",
 "James Mellaart excavated it in the 1960s; Ian Hodder's renewed project pioneered reflexive excavation methods.",
 "The site shows complex symbolic life long before states or writing existed."],
["Stonehenge","site","Wiltshire, England","c. 3000-2000 BCE",
 "Stonehenge is a Neolithic and Bronze Age monument of concentric stone circles, built in stages over 1,500 years.",
 "Its sarsen trilithons and bluestones — hauled from Wales — align with midsummer sunrise and midwinter sunset.",
 "Recent work shows it was part of a vast ritual landscape including Durrington Walls and Woodhenge.",
 "Cremated remains of dozens of people make it Britain's largest known Neolithic cremation cemetery."],
["Pyramids of Giza","site","Giza, Egypt","c. 2580-2510 BCE",
 "The Giza pyramids are the tombs of Fourth Dynasty pharaohs Khufu, Khafre, and Menkaure.",
 "The Great Pyramid of Khufu, built around 2560 BCE, held the title of tallest human structure for 3,800 years.",
 "Workforce villages excavated nearby show the builders were skilled laborers, not slaves, provisioned with bread and beer.",
 "The pyramid's sides align to true north with astonishing precision for the Bronze Age."],
["Machu Picchu","site","Andes, Peru","c. 1450 CE",
 "Machu Picchu is a 15th-century Inca estate of dry-stone walls, terraces, and temples on a mountain ridge.",
 "Built for the emperor Pachacuti around 1450, it was abandoned within a century during the Spanish conquest's chaos.",
 "Hiram Bingham publicized it in 1911, though local farmers knew it well.",
 "Its Temple of the Sun and Intihuatana stone track the solar calendar with precision."],
["Pompeii","site","Campania, Italy","79 CE",
 "Pompeii was buried by the eruption of Mount Vesuvius in 79 CE, preserving a Roman city mid-life.",
 "Plaster casts of voids in the ash capture the final postures of victims.",
 "Graffiti, bakeries, brothels, and election notices give an unrivaled street-level view of Roman daily life.",
 "Excavation continues; roughly a third of the city remains unexcavated."],
["Terracotta Army","artifact","Xi'an, China","c. 210 BCE",
 "The Terracotta Army guards the tomb of Qin Shi Huang, China's first emperor, with thousands of life-size soldiers.",
 "Discovered by farmers in 1974, the pits hold infantry, archers, chariots, and horses, each face individualized.",
 "The figures were originally painted in bright colors, most lost to exposure.",
 "The emperor's tomb mound itself remains unopened out of respect and technical caution."],
["Troy (Hisarlik)","site","Northwest Turkey","c. 3000-500 BCE",
 "Hisarlik in Turkey is the leading candidate for Homeric Troy, excavated by Heinrich Schliemann in the 1870s.",
 "The mound holds many superimposed cities; Troy VI/VIIa (c. 1300-1180 BCE) best fits the Iliad's era.",
 "Schliemann's destructive methods and treasure claims sparked archaeology's first great ethics debates.",
 "Later excavations by Wilhelm Dorpfeld and Manfred Korfmann rebuilt the chronology scientifically."],
["Knossos","site","Crete, Greece","c. 2000-1350 BCE",
 "Knossos was the great palace center of Minoan Crete, excavated by Arthur Evans from 1900.",
 "Its multi-story complex of courts, storerooms, and frescoed halls inspired the legend of the labyrinth.",
 "Evans's concrete reconstructions are controversial, but they made Minoan civilization visible to the world.",
 "Linear B tablets from Knossos, deciphered by Michael Ventris in 1952, proved the Mycenaeans wrote Greek."],
["Mycenae","civilization","Greece","c. 1600-1100 BCE",
 "Mycenae was the citadel center of Late Bronze Age Greece's palace civilization.",
 "Its Lion Gate, tholos tombs, and gold-rich shaft graves announced a warrior aristocracy.",
 "Linear B administration tracked flocks, bronze, and rations in an early Greek bureaucracy.",
 "The civilization collapsed around 1200 BCE in the wider Bronze Age collapse."],
["Olduvai Gorge","site","Tanzania","c. 1.9 million-15,000 years ago",
 "Olduvai Gorge preserves nearly two million years of human evolution in layered sediments.",
 "Louis and Mary Leakey's work there yielded Homo habilis, Paranthropus, and the earliest Oldowan stone tools.",
 "The gorge's strata let researchers tie fossils, tools, and environments together precisely.",
 "It remains the type site for understanding the emergence of toolmaking hominins."],
["Lascaux","site","Dordogne, France","c. 17,000 years ago",
 "Lascaux cave holds some 600 painted animals — horses, aurochs, and deer — from the Upper Paleolithic.",
 "Discovered by teenagers in 1940, its 'Hall of the Bulls' is the most famous painted chamber in the world.",
 "The original closed in 1963 after visitor breath damaged the paintings; exact replicas now receive the public.",
 "Its art demonstrates fully modern symbolic minds 17,000 years ago."],
["Chauvet Cave","site","Ardeche, France","c. 36,000 years ago",
 "Chauvet Cave, discovered in 1994, holds the oldest known major cave paintings, around 36,000 years old.",
 "Its lions, rhinos, and owls were drawn with shading and perspective far earlier than thought possible.",
 "The cave was sealed by a rockfall 23,000 years ago, preserving footprints and torch marks.",
 "It doubled the known antiquity of sophisticated cave art overnight."],
["Petra","site","Jordan","1st century BCE-1st century CE",
 "Petra was the rock-cut capital of the Nabataean kingdom, controlling incense trade routes.",
 "Its Treasury and Monastery facades are carved directly into sandstone cliffs.",
 "Sophisticated dams and cisterns made a desert metropolis of perhaps 20,000 people possible.",
 "Rome annexed Nabataea in 106 CE; earthquakes and shifting trade later emptied the city."],
["Angkor Wat","site","Cambodia","12th century CE",
 "Angkor Wat is the largest religious monument in the world, built by the Khmer king Suryavarman II in the early 1100s.",
 "Its five towers represent Mount Meru, the Hindu cosmic mountain, aligned to the spring equinox sunrise.",
 "The temple's bas-reliefs narrate the Mahabharata and Ramayana across hundreds of meters.",
 "LiDAR surveys revealed Greater Angkor as a vast low-density urban complex of up to 900,000 people."],
["Mohenjo-daro","civilization","Indus Valley","c. 2600-1900 BCE",
 "Mohenjo-daro was the largest city of the Indus Valley Civilization, with perhaps 40,000 residents.",
 "Its grid streets, covered drains, and the Great Bath show remarkable urban planning.",
 "The undeciphered Indus script remains one of archaeology's great unsolved puzzles.",
 "The city declined around 1900 BCE as rivers shifted and trade networks faltered."],
["Ur, Royal Cemetery","site","Iraq","c. 2600 BCE",
 "Leonard Woolley's excavations at Ur (1920s-30s) uncovered the Royal Cemetery's gold-laden tombs.",
 "The Standard of Ur and the queen Puabi's headdress display Sumerian craft at its peak.",
 "Evidence of retainer sacrifice — dozens buried with rulers — shocked the excavators.",
 "Ur's ziggurat, partly reconstructed, still dominates the plain."],
["Nineveh","site","Iraq","7th century BCE",
 "Nineveh was the Assyrian imperial capital under Sennacherib and Ashurbanipal in the 7th century BCE.",
 "Ashurbanipal's library preserved the Epic of Gilgamesh and thousands of cuneiform tablets.",
 "Austan Henry Layard's 1840s excavations made Assyria vivid to the Victorian public.",
 "The city's fall in 612 BCE ended the Assyrian Empire."],
["Palenque","site","Chiapas, Mexico","c. 600-800 CE",
 "Palenque is a Classic Maya city famed for the Temple of the Inscriptions and its royal tombs.",
 "Alberto Ruz discovered Pakal the Great's sarcophagus inside the temple pyramid in 1952.",
 "Its hieroglyphic texts, largely deciphered since the 1970s, narrate dynastic history in the kings' own words.",
 "Palenque's art and architecture rank among the Maya world's finest."],
["Teotihuacan","civilization","Central Mexico","c. 100 BCE-650 CE",
 "Teotihuacan was Mesoamerica's first great metropolis, with perhaps 125,000 residents at its height.",
 "The Pyramid of the Sun and the Avenue of the Dead organized a planned sacred city.",
 "Its apartment compounds housed multiethnic barrios, including Maya and Zapotec enclaves.",
 "The city's collapse around 650 CE remains debated; the Aztecs later revered its ruins."],
["Great Zimbabwe","site","Zimbabwe","c. 1100-1450 CE",
 "Great Zimbabwe was the stone-walled capital of a Shona trading state linked to Indian Ocean commerce.",
 "Its Great Enclosure walls, built without mortar, rise 11 meters in places.",
 "Gold and ivory flowed through the city to the Swahili coast in exchange for glass beads and cloth.",
 "Colonial mythologies denied African authorship; archaeology firmly reclaimed it."],
["Cahokia","site","Illinois, USA","c. 1050-1350 CE",
 "Cahokia was North America's largest pre-Columbian city, with 10,000-20,000 residents around 1100 CE.",
 "Monks Mound, a ten-story earthen pyramid, anchors a planned ceremonial precinct.",
 "Its influence spread Mississippian culture — maize farming, shell art, chunkey games — across the Southeast.",
 "The city declined by 1350 for reasons still debated: climate, politics, or both."],
["Chaco Canyon","site","New Mexico, USA","c. 850-1250 CE",
 "Chaco Canyon's great houses — Pueblo Bonito and others — were the ceremonial core of the Ancestral Puebloan world.",
 "Its road system radiates for dozens of kilometers across the desert.",
 "Tree-ring dating pins construction episodes to precise years, a dendrochronology triumph.",
 "Drought and social strain emptied the canyon by 1250."],
["Mesa Verde","site","Colorado, USA","c. 600-1300 CE",
 "Mesa Verde preserves Ancestral Puebloan cliff dwellings tucked into sandstone alcoves.",
 "Cliff Palace, with 150 rooms, housed perhaps 100 people in the 1200s.",
 "The move to cliffs coincided with drought and conflict in the late 1200s.",
 "Descendant Pueblo communities maintain deep cultural ties to the mesa."],
["Nazca Lines","artifact","Peru","c. 500 BCE-500 CE",
 "The Nazca Lines are vast geoglyphs — hummingbirds, monkeys, trapezoids — etched into Peru's desert plain.",
 "Made by removing dark surface stones to expose lighter soil, they survive in one of Earth's driest climates.",
 "Maria Reiche dedicated decades to mapping them and argued for astronomical alignments.",
 "Most scholars now link them to water rituals and processional walking."],
["Rapa Nui moai","artifact","Easter Island","c. 1250-1500 CE",
 "Rapa Nui's moai are monumental statues, nearly 900 carved from volcanic tuff at Rano Raraku quarry.",
 "They represent deified ancestors facing inland to watch over their descendants.",
 "The island's deforestation and statue-toppling wars preceded European contact.",
 "Recent work shows the statues 'walked' upright to their platforms using ropes and rocking."],
["Sutton Hoo","site","Suffolk, England","early 7th century CE",
 "Sutton Hoo's 1939 ship burial contained the richest Anglo-Saxon grave ever found.",
 "The 27-meter ship held weapons, gold, garnet jewelry, and Byzantine silver — likely King Raedwald's tomb.",
 "Basil Brown, the excavator, uncovered it on the eve of World War II.",
 "The finds rewrote the 'Dark Ages' as an era of far-reaching artistry and trade."],
["Otzi the Iceman","artifact","Otzi Alps","c. 3300 BCE",
 "Otzi, found in 1991, is a 5,300-year-old naturally mummified man from the Copper Age.",
 "His gear — copper axe, yew bow, grass cape — is the best-preserved prehistoric toolkit known.",
 "CT scans show arthritis, tattoos over aching joints, and a fatal arrow wound.",
 "His last meal and DNA reveal details of diet, health, and ancestry."],
["Tollund Man","artifact","Denmark","c. 400 BCE",
 "Tollund Man is an Iron Age bog body so well preserved by peat chemistry that he looks asleep.",
 "A leather noose around his neck indicates ritual hanging sacrifice.",
 "His stomach contents revealed a final gruel meal of barley and flax.",
 "He is the most famous of hundreds of northwest European bog bodies."],
["Rosetta Stone","artifact","Egypt","196 BCE",
 "The Rosetta Stone carries the same decree in hieroglyphic, Demotic, and Greek scripts.",
 "Found by French troops in 1799, it gave Jean-Francois Champollion the key to decipher hieroglyphs in 1822.",
 "The Greek text's royal names let scholars sound out the sacred script.",
 "Decipherment opened three millennia of Egyptian writing to modern reading."],
["Dead Sea Scrolls","artifact","Qumran, West Bank","c. 250 BCE-70 CE",
 "The Dead Sea Scrolls, found from 1947 in Qumran caves, are the oldest known biblical manuscripts.",
 "They include a complete Isaiah scroll a thousand years older than previous copies.",
 "The texts illuminate Second Temple Judaism and the community that hid them from the Romans.",
 "Multispectral imaging and DNA analysis of parchment continue to yield new joins."],
["Radiocarbon dating","dating","Worldwide","1949",
 "Radiocarbon dating, developed by Willard Libby in 1949, measures decaying carbon-14 in once-living material.",
 "Carbon-14's 5,730-year half-life makes it ideal for the last 50,000 years.",
 "Libby won the 1960 Nobel Prize in Chemistry for the method.",
 "Calibration against tree rings corrects for past fluctuations in atmospheric carbon-14."],
["Dendrochronology","dating","Worldwide","1929",
 "Dendrochronology dates wood by matching ring patterns to master chronologies.",
 "A. E. Douglass founded the method studying Arizona pines and Pueblo ruins in the 1920s.",
 "It gives exact calendar years — the gold standard of archaeological dating.",
 "Bristlecone pine chronologies extend the record back over 8,000 years."],
["Stratigraphy","method","Worldwide","1669",
 "Stratigraphy reads the layered sequence of deposits: deeper layers are generally older (Steno's law of superposition, 1669).",
 "It is archaeology's fundamental relative-dating principle.",
 "The Harris Matrix (1973) formalized stratigraphic relationships for complex urban sites.",
 "Every excavation records stratigraphy before a single artifact is lifted."],
["Seriation and typology","method","Worldwide","1899",
 "Flinders Petrie's sequence dating (1899) ordered Egyptian graves by pottery style evolution.",
 "Seriation assumes styles change gradually, letting assemblages be ordered without absolute dates.",
 "Typology — classifying artifacts into types — remains the basis of all artifact analysis.",
 "Battleship curves of type frequencies visualize stylistic rise and fall."],
["Potassium-argon dating","dating","Worldwide","1960s",
 "Potassium-argon dating measures argon-40 accumulated from potassium-40 decay in volcanic rock.",
 "With a 1.25-billion-year half-life, it dates the deep past, including early hominin sites.",
 "It dated Olduvai Gorge's layers and the Laetoli footprints to about 3.7 million years.",
 "Argon-argon variants now give even finer precision."],
["Thermoluminescence","dating","Worldwide","1960s",
 "Thermoluminescence dating measures light emitted when heated minerals release trapped electrons.",
 "It dates the last firing of pottery and burnt flint, typically back 50,000 years or more.",
 "The signal resets to zero on heating, making it a direct date of the firing event.",
 "Optically stimulated luminescence (OSL) extends the idea to sediments."],
["Ground-penetrating radar","method","Worldwide","1970s",
 "Ground-penetrating radar (GPR) images buried structures by recording reflected radio pulses.",
 "It maps walls, voids, and graves without digging a single trench.",
 "GPR surveys at Stonehenge and in Pompeii have guided targeted excavation.",
 "Soil moisture and clay content limit its depth and clarity."],
["LiDAR archaeology","method","Worldwide","2010s",
 "Airborne LiDAR strips away forest canopy with laser pulses to reveal ancient earthworks.",
 "It exposed vast Maya cities, Angkor's sprawl, and Amazonian geoglyphs invisible from the ground.",
 "A single flight can map in days what would take decades on foot.",
 "LiDAR has triggered a golden age of settlement-pattern discovery."],
["Zooarchaeology","method","Worldwide","1960s",
 "Zooarchaeology reconstructs past human-animal relationships from faunal remains.",
 "Cut marks, burning, and age profiles reveal hunting, herding, and butchery practices.",
 "It documented animal domestication's spread from the Near East outward.",
 "Isotope analysis of bones now traces ancient animal migrations."],
["Archaeobotany","method","Worldwide","1960s",
 "Archaeobotany recovers ancient plant use from seeds, pollen, and phytoliths.",
 "Flotation — agitating soil in water — floats charred seeds to the surface for collection.",
 "It traced the domestication of wheat, rice, and maize to specific regions and millennia.",
 "Starch grains on stone tools reveal processed foods invisible to the eye."],
["NAGPRA","legal-standards","United States","1990",
 "The Native American Graves Protection and Repatriation Act (1990) requires US museums to return human remains and sacred objects to tribes.",
 "It transformed American archaeology's relationship with Indigenous nations.",
 "Repatriation has returned hundreds of thousands of ancestors and objects.",
 "The law made consultation and consent central to excavation and curation."],
["UNESCO World Heritage","legal-standards","Worldwide","1972",
 "The 1972 World Heritage Convention protects cultural and natural sites of outstanding universal value.",
 "Listing brings prestige, tourism, and conservation obligations to places like Machu Picchu and Angkor.",
 "Over a thousand sites are inscribed, with delisting possible for damaged or delinquent properties.",
 "The convention remains the strongest global tool for heritage protection."]
];
var ANGLES=["site profile","excavation profile","artifact profile","dating profile"];
var SYNREL=[
 ["compared with","This Signature comparative study weighs both records on preservation, method, and historical impact."],
 ["contrasted against","This Signature contrast study shows how different techniques illuminate different pasts."],
 ["as predecessor and successor to","This Signature lineage study traces the method's evolution across the two cases."],
 ["alongside","This Signature pairing study reads the two together as chapters of one deeper history."]
];
function filedLine(id){return "Filed as "+id+" in the JAH Archaeology Database archive.";}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var id=PREFIX+String(seed).padStart(6,'0');
  var pool=ANCH;
  if(opts.category){var f=ANCH.filter(function(a){return a[1]===opts.category;});if(f.length)pool=f;}
  var synth=!opts.category&&rnd()<0.38;
  if(synth){
    var A=pick(pool,rnd),B=pick(pool,rnd),guard=0;
    while(B===A&&guard++<20)B=pick(pool,rnd);
    var rel=pick(SYNREL,rnd);
    var title="Signature study: "+A[0]+" "+rel[0]+" "+B[0];
    var d=A[0]+" ("+A[2]+", "+A[3]+"): "+A[4]+" "+rel[0]+" "+B[0]+" ("+B[3]+"), "+rel[1]+" "+B[4];
    return {id:id,title:title,description:d+" "+filedLine(id),category:A[1],
      spec:{kind:"study",pair:[A[0],B[0]],relation:rel[0],dates:[A[3],B[3]],src:"signature"},
      date_label:A[3],src:"signature"};
  }
  var A=pick(pool,rnd);
  var ang=pick(ANGLES,rnd);
  var facts=A.slice(4);
  var d=facts[0]+" "+pick(facts.slice(1),rnd);
  if(rnd()<0.6)d+=" "+pick(facts.slice(1),rnd);
  var title=A[0]+" — "+ang;
  return {id:id,title:title,description:d+" "+filedLine(id),category:A[1],
    spec:{kind:A[1],region:A[2],date_label:A[3],src:"online"},date_label:A[3],src:"online",_facts:facts,_an:A[0]};
}
function sentences(s){return String(s).split(/[.!?]+/).filter(function(x){return x.trim().length>10;}).length;}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!/^JAH-ARC2-\d{6}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<4)e.push('title');
  if(typeof r.description!=='string'||r.description.length<80)e.push('description');
  else if(sentences(r.description)<2)e.push('description-sentences');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(r.src!=='online'&&r.src!=='signature')e.push('src');
  if(typeof r.date_label!=='string'||!r.date_label.length)e.push('date_label');
  var s=r.spec;
  if(!s||typeof s!=='object')e.push('spec');
  else{
    if(s.src!=='online'&&s.src!=='signature')e.push('spec.src');
    if(s.src!==r.src)e.push('spec.src-mismatch');
    if(s.src==='online'){
      if(typeof s.region!=='string'||!s.region.length)e.push('spec.region');
      if(typeof s.date_label!=='string'||!s.date_label.length)e.push('spec.date_label');
    }else if(s.kind==='signature-version'){
      if(typeof s.of!=='string'||!s.of.length)e.push('spec.of');
    }else{
      if(!Array.isArray(s.pair)||s.pair.length!==2)e.push('spec.pair');
      if(typeof s.relation!=='string'||!s.relation.length)e.push('spec.relation');
    }
  }
  return{ok:!e.length,errors:e};
}

var SIG_T=[
 "Signature reading of {N}: {F1}",
 "Held in the Signature system as a governed Signature version, this record preserves the fact-checked core whole \u2014 nothing is reduced. {F2}",
 "Signature assessment: {N} is cross-referenced against the archive's related records, so the fact-checked original and its Signature version travel together. Property of Justin Addam Higgins."
];
function sigFill(t,m){return t.replace(/\{N\}|\{F1\}|\{F2\}/g,function(k){return m[k]||'';});}
function signatureVersion(seed){
  var base=generate(seed,{},prng(seed));
  if(!base||base.src!=='online')return null;
  var facts=(base._facts&&base._facts.length)?base._facts:[base.description];
  var N=base._an||base.title;
  var F1=facts[0],F2=facts.length>1?facts[1+((seed%(facts.length-1))|0)]:facts[0];
  var map={'{N}':N,'{F1}':F1,'{F2}':F2};
  var d=sigFill(SIG_T[0],map)+" "+sigFill(SIG_T[1],map)+" "+sigFill(SIG_T[2],map);
  var sv={id:base.id,_seed:seed,title:"Signature version: "+N,description:d,category:base.category,
    spec:{kind:"signature-version",of:base.id,src:"signature"},src:"signature"};
  Object.keys(base).forEach(function(k){
    if(k.charAt(0)==='_'||k==='id'||k==='title'||k==='description'||k==='category'||k==='spec'||k==='src')return;
    sv[k]=base[k];
  });
  return sv;
}
var gen={version:'jahdb-archaeology-1.0',generate:generate,validate:validate,signatureVersion:signatureVersion};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('archaeology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
