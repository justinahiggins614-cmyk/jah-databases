#!/usr/bin/env python3
"""Entries for the History Quiz databases (Manon's 2026-10-17 16:15 order:
test then quiz databases with answers at the bottom).

Two NEW databases, 34 ladder-ordered records each. Every record is ONE
complete quiz: 10 fact-checked history questions, then the 10 answers at
the bottom of the record (his explicit requirement). Ladder order:
easy (ranks 1-3, foundations) -> medium (ranks 4-6, compounded) ->
hard (ranks 7-10, advanced).

  quiz-history             - The History Quiz Database
                             (public-harvest: real, fact-checked history
                             quizzes - ancient, medieval, modern, and world
                             history - every record a full 10-question quiz
                             with answers at the bottom)
  quiz-history-signature   - The History Quiz Signature Database
                             (his original Signature reading of history:
                             every era a signature mark, every quiz a
                             covenant of memory; src signature, titles
                             suffixed " (Signature Edition)", clearly
                             labeled Signature-made, never presented as
                             authentic public record)

ID prefixes: JAH-QZHI- (public) and JAH-QZHIS- (signature), verified free
in the manifest id_prefix values (zero hits) and in every shard index
file in jah-databases-data-1 (zgrep zero hits, 2026-10-17).

Slug quiz-history verified free in the manifest (zero hits, 2442
databases scanned, 2026-10-17).

All 68 titles run through the whole-system dedupe gate BEFORE authoring;
zero collisions (see build.py pre-pass).

Never the words "bat belt" anywhere. No website references. No Facebook.
Screened: nothing hate-adjacent, profane, or inappropriate; no religious
talk - questions are factual history only.
"""

SIG_TAIL = ("Signature original - his original Signature reading of "
            "history: every era leaves a signature mark, every quiz a "
            "covenant of memory, every answer a seal on what was learned. "
            "Clearly labeled Signature-made, never presented as authentic "
            "public record.")

CIT_EGYPT = ("Shaw I, editor. The Oxford History of Ancient Egypt. Oxford "
             "University Press; 2000.")
CIT_GREECE = ("Hornblower S, Spawforth A, editors. The Oxford Classical "
              "Dictionary. 4th ed. Oxford University Press; 2012.")
CIT_ROME = ("Beard M. SPQR: A History of Ancient Rome. Liveright; 2015.")
CIT_MESOP = ("Leick G. Mesopotamia: The Invention of the City. Penguin; "
             "2002.")
CIT_CHINA = ("Fairbank JK, Goldman M. China: A New History. 2nd ed. Harvard "
             "University Press; 2006.")
CIT_PERSIA = ("Briant P. From Cyrus to Alexander: A History of the Persian "
              "Empire. Eisenbrauns; 2002.")
CIT_MEDIEVAL = ("Backman CR. The Worlds of Medieval Europe. 3rd ed. Oxford "
                "University Press; 2014.")
CIT_VIKING = ("Winroth A. The Age of the Vikings. Princeton University "
              "Press; 2014.")
CIT_BYZ = ("Herrin J. Byzantium: The Surprising Life of a Medieval Empire. "
           "Princeton University Press; 2008.")
CIT_CRUSADE = ("Tyerman C. God's War: A New History of the Crusades. Harvard "
               "University Press; 2006.")
CIT_MONGOL = ("Weatherford J. Genghis Khan and the Making of the Modern "
              "World. Crown; 2004.")
CIT_REN = ("Burckhardt J. The Civilization of the Renaissance in Italy. "
           "1860; Penguin Classics edition.")
CIT_EXPLOR = ("Parry JH. The Discovery of the Sea. University of California "
              "Press; 1981.")
CIT_REFORM = ("MacCulloch D. The Reformation: A History. Viking; 2003.")
CIT_AMREV = ("Middlekauff R. The Glorious Cause: The American Revolution, "
             "1763-1789. Oxford University Press; 2005.")
CIT_FRREV = ("Schama S. Citizens: A Chronicle of the French Revolution. "
             "Knopf; 1989.")
CIT_INDREV = ("Mokyr J. The Lever of Riches: Technological Creativity and "
              "Economic Progress. Oxford University Press; 1990.")
CIT_WWI = ("Keegan J. The First World War. Knopf; 1999.")
CIT_WWII = ("Weinberg GL. A World at Arms: A Global History of World War "
            "II. 2nd ed. Cambridge University Press; 2005.")
CIT_COLDWAR = ("Gaddis JL. The Cold War: A New History. Penguin; 2005.")
CIT_AMERICAS = ("Mann CC. 1491: New Revelations of the Americas Before "
                "Columbus. Knopf; 2005.")
CIT_AFRICA = ("Oliver R, Fage JD. A Short History of Africa. 6th ed. "
              "Penguin; 1988.")
CIT_SILK = ("Wood F. The Silk Road: Two Thousand Years in the Heart of "
            "Asia. University of California Press; 2002.")
CIT_REVS = ("Goldstone JA, editor. Revolutions: Theoretical, Comparative, "
            "and Historical Studies. 3rd ed. Cengage; 2015.")
CIT_C20 = ("Hobsbawm E. The Age of Extremes: A History of the World, "
           "1914-1991. Pantheon; 1994.")


def _HOW(name):
    return ("How to take this quiz. Read the ten questions in order and "
            "answer each one from memory before looking at the answers, "
            "which sit at the bottom of this record. Score yourself one "
            "point per correct answer: 9 to 10 is mastery of %s, 7 to 8 is "
            "strong, 5 to 6 is a fair start, and below 5 means the era "
            "deserves another pass. Take the quiz again after study and "
            "watch the score climb - that climb is the whole point." % name)


ENTRIES = [
    {
        "key": "qz_01", "name": "Ancient Egypt Basics Quiz",
        "group": "Ancient History", "ladder_rank": 1, "ladder_tier": "foundations",
        "description": ("An easy first quiz on ancient Egypt, the "
                        "civilization of the Nile that lasted more than "
                        "three thousand years. Ten friendly questions cover "
                        "the river, the pharaohs, the pyramids, hieroglyphs, "
                        "and the famous boy king whose tomb stunned the "
                        "world in 1922. A gentle doorway into the ancient "
                        "world."),
        "how_it_works": "",
        "questions": [
            "Which river was the lifeline of ancient Egypt?",
            "What were the kings of ancient Egypt called?",
            "What is the picture-writing system of ancient Egypt called?",
            "Which famous stone helped scholars decode hieroglyphs?",
            "The Great Pyramid of Giza was built for which pharaoh?",
            "Which jackal-headed god guarded mummification and the dead?",
            "What is the name of the boy king whose nearly intact tomb was found in 1922?",
            "Which vast desert covers most of Egypt?",
            "Ancient Egyptians wrote on a paper-like material made from which plant?",
            "Which queen of Egypt allied first with Julius Caesar and then with Mark Antony?",
        ],
        "answers": [
            "The Nile River.",
            "Pharaohs.",
            "Hieroglyphs.",
            "The Rosetta Stone.",
            "Pharaoh Khufu, called Cheops by the Greeks.",
            "Anubis.",
            "Tutankhamun, known as King Tut.",
            "The Sahara Desert.",
            "Papyrus.",
            "Cleopatra VII.",
        ],
        "standards": ["Era: Ancient Egypt, c. 3100-30 BCE",
                      "Difficulty: easy - foundations",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_EGYPT],
        "sig_lens": ("Through the Signature lens, ancient Egypt is the "
                     "first signature mark pressed into human memory: a "
                     "river that writes the same line every year, a people "
                     "who sealed their kings against time itself. This quiz "
                     "reads Egypt as the original covenant - what a "
                     "civilization chooses to remember forever."),
    },
    {
        "key": "qz_02", "name": "Ancient Greece Origins Quiz",
        "group": "Ancient History", "ladder_rank": 1, "ladder_tier": "foundations",
        "description": ("An easy first quiz on ancient Greece, the world of "
                        "city-states, myths, and the first democracy. Ten "
                        "friendly questions cover Athens and Sparta, the "
                        "gods, the Olympic Games, and the blind poet of the "
                        "Iliad. A gentle doorway into classical antiquity."),
        "how_it_works": "",
        "questions": [
            "What sea lies between Greece and the coast of Asia Minor?",
            "Which city-state is known as the birthplace of democracy?",
            "Which warlike city-state trained its boys as soldiers from childhood?",
            "The Olympic Games were held in honor of which Greek god?",
            "Which poet is credited with the Iliad and the Odyssey?",
            "What was the marketplace and civic center of a Greek city called?",
            "Which temple on the Athenian Acropolis was dedicated to Athena?",
            "Who was the king of the Greek gods?",
            "The Minoan civilization was centered on which island?",
            "What long poem tells the story of the Trojan War?",
        ],
        "answers": [
            "The Aegean Sea.",
            "Athens.",
            "Sparta.",
            "Zeus.",
            "Homer.",
            "The agora.",
            "The Parthenon.",
            "Zeus.",
            "Crete.",
            "The Iliad.",
        ],
        "standards": ["Era: Ancient Greece, c. 3000-146 BCE",
                      "Difficulty: easy - foundations",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_GREECE],
        "sig_lens": ("Through the Signature lens, Greece is the signature "
                     "of the questioning mind: a small rocky land that "
                     "signed its name on democracy, theater, and philosophy "
                     "for all time. This quiz reads the Greek miracle as "
                     "the covenant of curiosity itself."),
    },
    {
        "key": "qz_03", "name": "Roman Empire Foundations Quiz",
        "group": "Ancient History", "ladder_rank": 2, "ladder_tier": "foundations",
        "description": ("An easy quiz on the foundations of Rome, from the "
                        "legend of Romulus to the first emperor. Ten "
                        "questions cover the language, the legions, the "
                        "Colosseum, and the volcano that buried Pompeii. "
                        "The ground floor of Roman history."),
        "how_it_works": "",
        "questions": [
            "According to legend, who founded Rome in 753 BCE?",
            "What language did the Romans speak?",
            "Which river flows through the city of Rome?",
            "What was the great arena in Rome used for gladiator contests?",
            "Julius Caesar was assassinated in which year?",
            "Who was the first Roman emperor?",
            "What was the meeting place of the Roman senate called?",
            "Which volcano destroyed Pompeii in 79 CE?",
            "What did the Romans call the Mediterranean Sea, meaning Our Sea?",
            "Roman soldiers were organized into large units of about five thousand men called what?",
        ],
        "answers": [
            "Romulus.",
            "Latin.",
            "The Tiber River.",
            "The Colosseum.",
            "44 BCE, on the Ides of March.",
            "Augustus, formerly Octavian.",
            "The Curia, in the Roman Forum.",
            "Mount Vesuvius.",
            "Mare Nostrum.",
            "Legions.",
        ],
        "standards": ["Era: Rome, 753 BCE - 476 CE",
                      "Difficulty: easy - foundations",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_ROME],
        "sig_lens": ("Through the Signature lens, Rome is the signature of "
                     "endurance pressed across three continents: roads, "
                     "law, and language carrying one mark for a thousand "
                     "years. This quiz reads Rome as the covenant of order "
                     "itself."),
    },
    {
        "key": "qz_04", "name": "Mesopotamia First Civilizations Quiz",
        "group": "Ancient History", "ladder_rank": 2, "ladder_tier": "foundations",
        "description": ("An easy quiz on Mesopotamia, the land between the "
                        "rivers where cities, writing, and the wheel were "
                        "born. Ten questions cover Sumer, Babylon, "
                        "Hammurabi, and the clay tablets that carried the "
                        "first words. Where civilization itself began."),
        "how_it_works": "",
        "questions": [
            "Mesopotamia means the land between which two rivers?",
            "Which wedge-shaped writing system was invented in Sumer?",
            "The Sumerians built stepped temple towers called what?",
            "Which Babylonian king is famous for one of the earliest law codes?",
            "In which region was the wheel invented?",
            "Which city is often called the first true city in history?",
            "What did Mesopotamians write on?",
            "Which empire built its capital at Nineveh?",
            "The Hanging Gardens are traditionally associated with which city?",
            "Which people conquered Babylon in 539 BCE?",
        ],
        "answers": [
            "The Tigris and the Euphrates.",
            "Cuneiform.",
            "Ziggurats.",
            "Hammurabi.",
            "Mesopotamia, in Sumer.",
            "Uruk.",
            "Clay tablets.",
            "The Assyrian Empire.",
            "Babylon.",
            "The Persians, under Cyrus the Great.",
        ],
        "standards": ["Era: Mesopotamia, c. 4000-539 BCE",
                      "Difficulty: easy - foundations",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_MESOP],
        "sig_lens": ("Through the Signature lens, Mesopotamia is the first "
                     "signature of organization: the first cities, the "
                     "first writing, the first laws pressed into clay. This "
                     "quiz reads the land between the rivers as the "
                     "covenant of civilization itself."),
    },
    {
        "key": "qz_05", "name": "Pharaohs and Pyramids Quiz",
        "group": "Ancient History", "ladder_rank": 3, "ladder_tier": "foundations",
        "description": ("A foundations quiz that goes deeper into the "
                        "pharaohs and their monuments. Ten questions cover "
                        "the Old Kingdom pyramid builders, the warrior "
                        "pharaohs of the New Kingdom, the Valley of the "
                        "Kings, and the queens who ruled as kings. Egypt "
                        "beyond the basics."),
        "how_it_works": "",
        "questions": [
            "The pyramids of Giza were built during which period of Egyptian history?",
            "Besides Khufu, which two pharaohs have pyramids at Giza?",
            "Which pharaoh built the great rock temples at Abu Simbel?",
            "Which woman ruled Egypt as pharaoh in the fifteenth century BCE?",
            "Which pharaoh briefly moved Egypt to the worship of one god, the Aten?",
            "What is the lion-bodied statue guarding the Giza pyramids called?",
            "In which valley were the pharaohs of the New Kingdom buried?",
            "What small figurines were placed in tombs to serve the dead in the afterlife?",
            "Alexander the Great conquered Egypt in which year?",
            "Who was the last active ruler of Ptolemaic Egypt?",
        ],
        "answers": [
            "The Old Kingdom, around 2600-2500 BCE.",
            "Khafre, called Chephren by the Greeks, and Menkaure, called Mykerinos.",
            "Ramesses II, called Ramesses the Great.",
            "Hatshepsut.",
            "Akhenaten.",
            "The Great Sphinx.",
            "The Valley of the Kings.",
            "Shabti, also called ushabti, funerary figurines.",
            "332 BCE.",
            "Cleopatra VII.",
        ],
        "standards": ["Era: Ancient Egypt, Old Kingdom to Ptolemaic, c. 2686-30 BCE",
                      "Difficulty: easy - foundations",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_EGYPT],
        "sig_lens": ("Through the Signature lens, the pharaohs are the "
                     "signature of ambition carved in stone: each monument "
                     "a name refused to let time erase. This quiz reads the "
                     "pyramid age as the covenant of remembrance."),
    },
    {
        "key": "qz_06", "name": "Athens and Sparta Quiz",
        "group": "Ancient History", "ladder_rank": 3, "ladder_tier": "foundations",
        "description": ("A foundations quiz on the two great rivals of "
                        "classical Greece. Ten questions cover the "
                        "Peloponnesian War, the Persian Wars, Pericles, "
                        "Socrates, and the battle where three hundred "
                        "Spartans made their stand. The Greek world at its "
                        "height."),
        "how_it_works": "",
        "questions": [
            "The Peloponnesian War was fought between which two alliances?",
            "Who was the leading Athenian statesman of the Golden Age?",
            "Which battle in 490 BCE saw Athens defeat a Persian invasion?",
            "Which naval battle in 480 BCE destroyed the Persian fleet?",
            "Three hundred Spartans made their famous stand at which mountain pass?",
            "Who was the tutor of Alexander the Great?",
            "The Athenian council of five hundred was called what?",
            "Which philosopher was sentenced to drink hemlock in 399 BCE?",
            "Sparta's enslaved laborer class was called what?",
            "Which Macedonian king conquered Greece at Chaeronea in 338 BCE?",
        ],
        "answers": [
            "Athens and its Delian League against Sparta and its Peloponnesian League.",
            "Pericles.",
            "The Battle of Marathon.",
            "The Battle of Salamis.",
            "Thermopylae.",
            "Aristotle.",
            "The Boule.",
            "Socrates.",
            "The helots.",
            "Philip II of Macedon.",
        ],
        "standards": ["Era: Classical Greece, c. 500-338 BCE",
                      "Difficulty: easy - foundations",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_GREECE],
        "sig_lens": ("Through the Signature lens, Athens and Sparta are "
                     "twin signatures of the same hand: one signing in "
                     "words and votes, the other in discipline and shields. "
                     "This quiz reads their rivalry as the covenant of "
                     "choice between two ways to be strong."),
    },
    {
        "key": "qz_07", "name": "Renaissance Quiz",
        "group": "Modern History", "ladder_rank": 3, "ladder_tier": "foundations",
        "description": ("A foundations quiz on the Renaissance, the rebirth "
                        "of art and learning in Europe. Ten questions cover "
                        "Italy, the Medici, Leonardo and Michelangelo, "
                        "Gutenberg's press, and what the word renaissance "
                        "actually means. The doorway to the modern age."),
        "how_it_works": "",
        "questions": [
            "The Renaissance began in which European country?",
            "Which powerful family dominated Florence during the Renaissance?",
            "Who painted the Mona Lisa?",
            "Who painted the ceiling of the Sistine Chapel?",
            "Who introduced movable-type printing to Europe around 1440?",
            "What was Gutenberg's most famous printed book?",
            "Which Renaissance thinker wrote The Prince?",
            "Humanism centered on the study of what?",
            "Which architect engineered the great dome of Florence Cathedral?",
            "What does the French word renaissance mean?",
        ],
        "answers": [
            "Italy.",
            "The Medici family.",
            "Leonardo da Vinci.",
            "Michelangelo.",
            "Johannes Gutenberg.",
            "The Bible, known as the Gutenberg Bible.",
            "Niccolo Machiavelli.",
            "Classical Greek and Roman learning and literature.",
            "Filippo Brunelleschi.",
            "Rebirth.",
        ],
        "standards": ["Era: Renaissance, c. 1350-1600",
                      "Difficulty: easy - foundations",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_REN],
        "sig_lens": ("Through the Signature lens, the Renaissance is the "
                     "signature of rebirth: a whole civilization picking up "
                     "an ancient pen and signing its name again, bolder. "
                     "This quiz reads the age as the covenant of renewal."),
    },
    {
        "key": "qz_08", "name": "Roman Republic Quiz",
        "group": "Ancient History", "ladder_rank": 4, "ladder_tier": "compounded",
        "description": ("A medium quiz on the Roman Republic, the five "
                        "centuries of senates, consuls, and civil wars "
                        "before the emperors. Ten questions cover Hannibal, "
                        "Spartacus, Caesar, and the river crossing that "
                        "ended the Republic. Rome before the Caesars."),
        "how_it_works": "",
        "questions": [
            "The Roman Republic was founded in which year, after the kings were expelled?",
            "What were the two chief elected magistrates of the Republic called?",
            "Which Carthaginian general crossed the Alps with war elephants?",
            "The three Punic Wars were fought against which city?",
            "Which Roman general and dictator reformed the calendar?",
            "What were the common people of Rome called?",
            "Which enslaved gladiator led a great slave revolt in 73 BCE?",
            "The First Triumvirate joined Caesar and Pompey with whom?",
            "Caesar crossed which small river in 49 BCE, starting civil war?",
            "The Republic effectively ended with Augustus's victory at which 31 BCE battle?",
        ],
        "answers": [
            "509 BCE.",
            "Consuls.",
            "Hannibal Barca.",
            "Carthage.",
            "Julius Caesar, whose Julian calendar lasted over sixteen centuries.",
            "Plebeians.",
            "Spartacus.",
            "Marcus Licinius Crassus.",
            "The Rubicon.",
            "The Battle of Actium.",
        ],
        "standards": ["Era: Roman Republic, 509-27 BCE",
                      "Difficulty: medium - compounded",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_ROME],
        "sig_lens": ("Through the Signature lens, the Republic is the "
                     "signature of shared power: consuls, senates, and "
                     "assemblies signing the state together until one man "
                     "signed alone. This quiz reads the Republic as the "
                     "covenant of liberty, kept and broken."),
    },
    {
        "key": "qz_09", "name": "Early Middle Ages Quiz",
        "group": "Medieval History", "ladder_rank": 4, "ladder_tier": "compounded",
        "description": ("A medium quiz on the early Middle Ages, the "
                        "centuries between Rome's fall and the high medieval "
                        "world. Ten questions cover Charlemagne, the "
                        "Vikings, the monasteries that saved learning, and "
                        "the battle that halted an invasion at Tours. "
                        "Europe rebuilding itself."),
        "how_it_works": "",
        "questions": [
            "The Western Roman Empire is conventionally dated to fall in which year?",
            "Which Frankish king was crowned Emperor by the Pope in 800 CE?",
            "Charlemagne's empire is known by what name?",
            "Which region of France is named for the Norsemen who settled it?",
            "How did medieval monasteries preserve ancient learning?",
            "The Vikings came originally from which region?",
            "Which battle in 732 CE halted the Muslim advance into Frankish lands?",
            "The code of conduct for medieval knights was called what?",
            "What was the main language of scholarship in medieval Europe?",
            "The Treaty of Verdun in 843 CE divided whose empire?",
        ],
        "answers": [
            "476 CE.",
            "Charlemagne.",
            "The Carolingian Empire.",
            "Normandy.",
            "Monks copied manuscripts by hand in the scriptorium.",
            "Scandinavia.",
            "The Battle of Tours, also called Poitiers.",
            "Chivalry.",
            "Latin.",
            "Charlemagne's empire, divided among his grandsons.",
        ],
        "standards": ["Era: Early Middle Ages, c. 476-1000 CE",
                      "Difficulty: medium - compounded",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_MEDIEVAL],
        "sig_lens": ("Through the Signature lens, the early Middle Ages "
                     "are the signature of patience: monks copying by "
                     "candlelight, kings crowned in cold chapels, a "
                     "continent quietly signing its survival. This quiz "
                     "reads the age as the covenant of preservation."),
    },
    {
        "key": "qz_10", "name": "Vikings and Norse Voyages Quiz",
        "group": "Medieval History", "ladder_rank": 4, "ladder_tier": "compounded",
        "description": ("A medium quiz on the Vikings, the Norse seafarers "
                        "who raided, traded, and settled from North America "
                        "to the Black Sea. Ten questions cover Lindisfarne, "
                        "Leif Erikson, longships, runes, and the assembly "
                        "where free men made law. The Norse age in full "
                        "sail."),
        "how_it_works": "",
        "questions": [
            "The Viking Age is often dated from the raid on which monastery in 793 CE?",
            "Which Norse explorer reached North America around 1000 CE?",
            "What did the Norse call the North American lands they visited?",
            "What made Viking longships remarkable for their time?",
            "Which Norse god wielded the hammer Mjolnir?",
            "The Norse writing system used characters called what?",
            "Which Viking leader became the first Duke of Normandy?",
            "The Norse assembly of free men was called what?",
            "Which Irish city was founded by Vikings and became the capital?",
            "The last great Viking king of Norway died at which 1066 battle?",
        ],
        "answers": [
            "Lindisfarne, off the English coast.",
            "Leif Erikson.",
            "Vinland.",
            "Their long, shallow-draft hulls, which could sail oceans and rivers alike.",
            "Thor.",
            "Runes.",
            "Rollo.",
            "The Thing, in Iceland the Althing.",
            "Dublin.",
            "The Battle of Stamford Bridge.",
        ],
        "standards": ["Era: Viking Age, c. 793-1066 CE",
                      "Difficulty: medium - compounded",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_VIKING],
        "sig_lens": ("Through the Signature lens, the Vikings are the "
                     "signature of daring: small ships signing bold lines "
                     "across the whole map of the known world. This quiz "
                     "reads the Norse age as the covenant of the open sea."),
    },
    {
        "key": "qz_11", "name": "Age of Exploration Quiz",
        "group": "Modern History", "ladder_rank": 4, "ladder_tier": "compounded",
        "description": ("A medium quiz on the Age of Exploration, when "
                        "European sailors mapped the oceans and connected "
                        "the hemispheres. Ten questions cover Columbus, da "
                        "Gama, Magellan, the conquistadors, and the great "
                        "exchange that followed. The world becoming one."),
        "how_it_works": "",
        "questions": [
            "Christopher Columbus sailed in 1492 under the flag of which kingdom?",
            "What were the names of Columbus's three ships?",
            "Who first rounded the Cape of Good Hope in 1488?",
            "Vasco da Gama reached which country by sea in 1498?",
            "The 1494 treaty dividing the new lands between Spain and Portugal was what?",
            "Whose expedition first circumnavigated the globe in 1519 to 1522?",
            "Magellan was killed in which island group?",
            "Which conquistador conquered the Aztec Empire?",
            "Which conquistador conquered the Inca Empire?",
            "The exchange of crops, animals, and diseases between the hemispheres is called what?",
        ],
        "answers": [
            "Spain, under Ferdinand and Isabella.",
            "The Nina, the Pinta, and the Santa Maria.",
            "Bartolomeu Dias.",
            "India.",
            "The Treaty of Tordesillas.",
            "Ferdinand Magellan's expedition, completed by Juan Sebastian Elcano.",
            "The Philippines.",
            "Hernan Cortes.",
            "Francisco Pizarro.",
            "The Columbian Exchange.",
        ],
        "standards": ["Era: Age of Exploration, c. 1415-1600",
                      "Difficulty: medium - compounded",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_EXPLOR],
        "sig_lens": ("Through the Signature lens, the explorers are the "
                     "signature of the horizon: sails drawing the first "
                     "true outline of the whole earth. This quiz reads the "
                     "age as the covenant of the map."),
    },
    {
        "key": "qz_12", "name": "Ancient China Dynasties Quiz",
        "group": "Ancient History", "ladder_rank": 5, "ladder_tier": "compounded",
        "description": ("A medium quiz on ancient and imperial China, from "
                        "the first emperor to the last dynasty. Ten "
                        "questions cover the Qin, Han, Tang, and Ming, "
                        "Confucius, paper, the Great Wall, and the Silk "
                        "Road. Four thousand years of continuity."),
        "how_it_works": "",
        "questions": [
            "Who was the first emperor of a unified China?",
            "The Great Wall was first joined into one system under which dynasty?",
            "Which dynasty is remembered as a golden age of poetry and cosmopolitan culture?",
            "Paper was invented in China during which dynasty?",
            "Which Chinese philosopher taught the doctrines collected in the Analects?",
            "The Terracotta Army guards the tomb of which emperor?",
            "Which dynasty built the Forbidden City in Beijing?",
            "What was the last imperial dynasty of China?",
            "Which trade route connected China to the Mediterranean world?",
            "The civil service examination system matured under which dynasty?",
        ],
        "answers": [
            "Qin Shi Huang.",
            "The Qin dynasty.",
            "The Tang dynasty.",
            "The Han dynasty.",
            "Confucius.",
            "Qin Shi Huang.",
            "The Ming dynasty.",
            "The Qing dynasty, which ended in 1912.",
            "The Silk Road.",
            "The Tang dynasty, begun under the Sui.",
        ],
        "standards": ["Era: Imperial China, 221 BCE - 1912 CE",
                      "Difficulty: medium - compounded",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_CHINA],
        "sig_lens": ("Through the Signature lens, China is the signature "
                     "of continuity: dynasty after dynasty signing the "
                     "same long line across four millennia. This quiz reads "
                     "the Middle Kingdom as the covenant of endurance."),
    },
    {
        "key": "qz_13", "name": "Persian Empire Quiz",
        "group": "Ancient History", "ladder_rank": 5, "ladder_tier": "compounded",
        "description": ("A medium quiz on the Persian Empire, the first "
                        "great multi-continental empire of the ancient "
                        "world. Ten questions cover Cyrus, Darius, Xerxes, "
                        "Persepolis, the Royal Road, and the wars with "
                        "Greece. The empire Rome could never quite "
                        "forget."),
        "how_it_works": "",
        "questions": [
            "Who founded the Achaemenid Persian Empire?",
            "The great ceremonial capital of Persia was called what?",
            "Which Persian king led the invasion of Greece in 480 BCE?",
            "The Persian Empire fell to which conqueror in 330 BCE?",
            "The Persian system of provinces was organized into units called what?",
            "Which Persian-origin religion taught the struggle of good against evil?",
            "The Royal Road connected Susa to which western city?",
            "Which Persian king commissioned the great Behistun Inscription?",
            "At which 490 BCE battle did Persia first fail to conquer Greece?",
            "The Persian Wars were fought between Persia and whom?",
        ],
        "answers": [
            "Cyrus the Great.",
            "Persepolis.",
            "Xerxes I.",
            "Alexander the Great.",
            "Satrapies, each governed by a satrap.",
            "Zoroastrianism.",
            "Sardis.",
            "Darius I, called Darius the Great.",
            "The Battle of Marathon.",
            "The Greek city-states.",
        ],
        "standards": ["Era: Achaemenid Persia, c. 550-330 BCE",
                      "Difficulty: medium - compounded",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_PERSIA],
        "sig_lens": ("Through the Signature lens, Persia is the signature "
                     "of scale: the first hand to sign across three "
                     "continents, from the Indus to the Aegean. This quiz "
                     "reads the empire as the covenant of the road - "
                     "satrapies, couriers, and one king's peace."),
    },
    {
        "key": "qz_14", "name": "Byzantine Empire Quiz",
        "group": "Medieval History", "ladder_rank": 5, "ladder_tier": "compounded",
        "description": ("A medium quiz on the Byzantine Empire, Rome's "
                        "eastern heir that stood a thousand years after the "
                        "west fell. Ten questions cover Constantinople, "
                        "Justinian, the Hagia Sophia, Greek fire, and the "
                        "city's fall in 1453. The medieval Roman Empire."),
        "how_it_works": "",
        "questions": [
            "What was the capital of the Byzantine Empire?",
            "Constantinople was renamed by which emperor, its founder?",
            "Which emperor codified Roman law into the Corpus Juris Civilis?",
            "Justinian's great church, famed for its dome, is called what?",
            "The Byzantines spoke and wrote primarily in which language?",
            "Constantinople fell to the Ottomans in which year?",
            "What secret incendiary weapon aided the Byzantine navy?",
            "The Great Schism of 1054 divided Christianity into which two branches?",
            "Which empress was the powerful wife and partner of Justinian?",
            "The long-lived Byzantine gold coin was called what?",
        ],
        "answers": [
            "Constantinople.",
            "Constantine the Great.",
            "Justinian I.",
            "The Hagia Sophia.",
            "Greek.",
            "1453.",
            "Greek fire.",
            "The Roman Catholic Church and the Eastern Orthodox Church.",
            "Theodora.",
            "The solidus, later called the bezant.",
        ],
        "standards": ["Era: Byzantine Empire, 330-1453 CE",
                      "Difficulty: medium - compounded",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_BYZ],
        "sig_lens": ("Through the Signature lens, Byzantium is the "
                     "signature of survival: Rome's eastern hand still "
                     "signing a thousand years after the west let go of the "
                     "pen. This quiz reads the empire as the covenant of "
                     "the long watch."),
    },
    {
        "key": "qz_15", "name": "Reformation Quiz",
        "group": "Modern History", "ladder_rank": 5, "ladder_tier": "compounded",
        "description": ("A medium quiz on the Reformation, the sixteenth "
                        "century upheaval that split Western Christianity. "
                        "Ten questions cover Luther, Calvin, Henry VIII, the "
                        "Jesuits, and the wars of religion that followed. "
                        "Faith, power, and the printing press."),
        "how_it_works": "",
        "questions": [
            "Who posted the Ninety-five Theses in 1517?",
            "On the church door of which German town did Luther post his theses?",
            "Which reformer led the Reformation in Geneva?",
            "Henry VIII broke with Rome after the Pope refused to grant what?",
            "The national church Henry VIII established was called what?",
            "The Catholic response to the Reformation is known as what?",
            "The Jesuit order was founded by whom?",
            "The Council of Trent, the centerpiece of Catholic reform, met in which years?",
            "Luther translated the New Testament into which language?",
            "The Peace of Westphalia in 1648 ended which great war?",
        ],
        "answers": [
            "Martin Luther.",
            "Wittenberg.",
            "John Calvin.",
            "An annulment of his marriage to Catherine of Aragon.",
            "The Church of England, the Anglican Church.",
            "The Counter-Reformation.",
            "Ignatius of Loyola.",
            "1545 to 1563.",
            "German.",
            "The Thirty Years' War.",
        ],
        "standards": ["Era: Reformation, c. 1517-1648",
                      "Difficulty: medium - compounded",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_REFORM],
        "sig_lens": ("Through the Signature lens, the Reformation is the "
                     "signature of conscience: millions choosing to sign "
                     "their own name on faith instead of letting it be "
                     "signed for them. This quiz reads the age as the "
                     "covenant of the individual mind."),
    },
    {
        "key": "qz_16", "name": "Roman Emperors Quiz",
        "group": "Ancient History", "ladder_rank": 6, "ladder_tier": "compounded",
        "description": ("A medium quiz on the emperors of Rome, from "
                        "Augustus to the fall of the west. Ten questions "
                        "cover the Pax Romana, Hadrian's Wall, Constantine, "
                        "and the boy emperor whose deposition ended an "
                        "empire. Five centuries of absolute power."),
        "how_it_works": "",
        "questions": [
            "Augustus ruled during a long peace known by what name?",
            "Which emperor built the great wall across northern Britain?",
            "Nero is infamous for supposedly doing what during the Great Fire of Rome?",
            "Which emperor made Christianity legal throughout the empire in 313 CE?",
            "The last Western Roman emperor, deposed in 476 CE, was who?",
            "Which emperor's column in Rome depicts the Dacian Wars?",
            "Caligula's successor, known as a scholar among emperors, was who?",
            "Which emperor divided the administration of the empire between east and west?",
            "The Colosseum was completed under which emperor?",
            "Who was the last of the so-called Five Good Emperors?",
        ],
        "answers": [
            "The Pax Romana, the Roman Peace.",
            "Hadrian.",
            "Playing the lyre, or fiddling, while Rome burned.",
            "Constantine the Great, by the Edict of Milan.",
            "Romulus Augustulus.",
            "Trajan's Column.",
            "Claudius.",
            "Diocletian.",
            "Titus, who finished the work begun by his father Vespasian.",
            "Marcus Aurelius.",
        ],
        "standards": ["Era: Roman Empire, 27 BCE - 476 CE",
                      "Difficulty: medium - compounded",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_ROME],
        "sig_lens": ("Through the Signature lens, the emperors are the "
                     "signature of power concentrated to a point: one name "
                     "stamped on coins, laws, and legions from Britain to "
                     "Syria. This quiz reads the imperial age as the "
                     "covenant of the single seal."),
    },
    {
        "key": "qz_17", "name": "Crusades Quiz",
        "group": "Medieval History", "ladder_rank": 6, "ladder_tier": "compounded",
        "description": ("A medium quiz on the Crusades, two centuries of "
                        "holy war between Christendom and the Muslim world. "
                        "Ten questions cover Urban II, Jerusalem, Saladin, "
                        "Richard the Lionheart, and the Templars. The "
                        "medieval world's great collision."),
        "how_it_works": "",
        "questions": [
            "Who called the First Crusade at Clermont in 1095?",
            "The Crusaders captured which holy city in 1099?",
            "Which Muslim leader recaptured Jerusalem in 1187?",
            "The Third Crusade featured which English king?",
            "The order of monk-knights founded to protect pilgrims was called what?",
            "The Fourth Crusade infamously sacked which Christian city in 1204?",
            "The Children's Crusade took place in which year?",
            "The Crusader states in the Holy Land were collectively known as what?",
            "Which French king led two crusades and was later made a saint?",
            "The last great Crusader stronghold, Acre, fell in which year?",
        ],
        "answers": [
            "Pope Urban II.",
            "Jerusalem.",
            "Saladin.",
            "Richard I, called Richard the Lionheart.",
            "The Knights Templar.",
            "Constantinople.",
            "1212.",
            "Outremer, meaning the land overseas.",
            "Louis IX, called Saint Louis.",
            "1291.",
        ],
        "standards": ["Era: Crusades, 1095-1291",
                      "Difficulty: medium - compounded",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_CRUSADE],
        "sig_lens": ("Through the Signature lens, the Crusades are the "
                     "signature of conviction armed: two worlds signing "
                     "their names in the same holy dust. This quiz reads "
                     "the age as the covenant of belief tested by the "
                     "sword."),
    },
    {
        "key": "qz_18", "name": "Feudalism in Medieval Europe Quiz",
        "group": "Medieval History", "ladder_rank": 6, "ladder_tier": "compounded",
        "description": ("A medium quiz on feudalism, the system of lords, "
                        "vassals, and serfs that ordered medieval Europe. "
                        "Ten questions cover fiefs, homage, the Magna Carta, "
                        "guilds, and the Gothic cathedrals. How the Middle "
                        "Ages actually worked."),
        "how_it_works": "",
        "questions": [
            "In feudalism, land granted by a lord to a vassal was called what?",
            "The ceremony binding a vassal to his lord was called what?",
            "Peasants legally bound to the land were called what?",
            "The great charter limiting English royal power in 1215 was what?",
            "Which English king was forced to seal the Magna Carta?",
            "Medieval craft workers organized themselves into associations called what?",
            "The soaring architectural style of the great medieval cathedrals was what?",
            "Medieval universities grew from schools attached to what institutions?",
            "The three-field system was a medieval method for what?",
            "A lord's fortified residence was called what?",
        ],
        "answers": [
            "A fief.",
            "Homage, with the oath of fealty.",
            "Serfs.",
            "The Magna Carta.",
            "King John.",
            "Guilds.",
            "Gothic.",
            "Cathedrals and monasteries.",
            "Crop rotation in farming.",
            "A castle.",
        ],
        "standards": ["Era: High Middle Ages, c. 1000-1300",
                      "Difficulty: medium - compounded",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_MEDIEVAL],
        "sig_lens": ("Through the Signature lens, feudalism is the "
                     "signature of mutual oath: every bond sealed by homage, "
                     "every field by service, every stone by craft. This "
                     "quiz reads the system as the covenant of pledged "
                     "word."),
    },
    {
        "key": "qz_19", "name": "American Revolution Quiz",
        "group": "Modern History", "ladder_rank": 6, "ladder_tier": "compounded",
        "description": ("A medium quiz on the American Revolution, the "
                        "colonial rebellion that created the United States. "
                        "Ten questions cover Lexington, Saratoga, Yorktown, "
                        "Washington, and the French ally who crossed an "
                        "ocean for liberty. The birth of a republic."),
        "how_it_works": "",
        "questions": [
            "The first shots of the war were fired at which 1775 battles?",
            "The Declaration of Independence was adopted on what date?",
            "Who wrote the principal draft of the Declaration of Independence?",
            "The turning-point battle of 1777, which brought France into the war, was which?",
            "The last major battle of the war, in 1781, was which?",
            "Who commanded the Continental Army?",
            "Which young French nobleman became a beloved ally of the American cause?",
            "Washington's army endured the winter of 1777 to 1778 at which Pennsylvania camp?",
            "The treaty ending the war was signed in 1783 in which city?",
            "The slogan no taxation without representation protested taxes levied by which parliament?",
        ],
        "answers": [
            "Lexington and Concord.",
            "July 4, 1776.",
            "Thomas Jefferson.",
            "The Battle of Saratoga.",
            "The Siege of Yorktown.",
            "George Washington.",
            "The Marquis de Lafayette.",
            "Valley Forge.",
            "Paris, in the Treaty of Paris.",
            "The British Parliament.",
        ],
        "standards": ["Era: American Revolution, 1775-1783",
                      "Difficulty: medium - compounded",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_AMREV],
        "sig_lens": ("Through the Signature lens, the Revolution is the "
                     "signature of self-rule: thirteen colonies signing one "
                     "declaration that a people may choose its own "
                     "government. This quiz reads 1776 as the covenant of "
                     "the consenting citizen."),
    },
    {
        "key": "qz_20", "name": "Silk Road Quiz",
        "group": "World History", "ladder_rank": 6, "ladder_tier": "compounded",
        "description": ("A medium quiz on the Silk Road, the great web of "
                        "trade routes linking China to the Mediterranean. "
                        "Ten questions cover silk, paper, Buddhism, "
                        "Samarkand, and the desert crossings. Two thousand "
                        "years of caravans."),
        "how_it_works": "",
        "questions": [
            "The Silk Road connected China to which sea?",
            "The phrase Silk Road was coined by which German geographer?",
            "Which Chinese dynasty first opened the Silk Road?",
            "Besides silk, which Chinese invention traveled west along the road?",
            "Which religion spread from India to China along the Silk Road?",
            "The great oasis trading city of Samarkand lies in which modern country?",
            "Caravans on the northern routes crossed which fearsome desert?",
            "Marco Polo traveled the Silk Road during which Chinese dynasty?",
            "The Black Death reached Europe traveling along which routes?",
            "Ocean trade around which cape finally eclipsed the overland Silk Road?",
        ],
        "answers": [
            "The Mediterranean Sea.",
            "Ferdinand von Richthofen.",
            "The Han dynasty.",
            "Paper.",
            "Buddhism.",
            "Uzbekistan.",
            "The Taklamakan Desert.",
            "The Yuan dynasty, under Mongol rule.",
            "The Silk Road trade routes.",
            "The Cape of Good Hope.",
        ],
        "standards": ["Era: Silk Road, c. 130 BCE - 1500 CE",
                      "Difficulty: medium - compounded",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_SILK],
        "sig_lens": ("Through the Signature lens, the Silk Road is the "
                     "signature of connection: one long line signing goods, "
                     "faiths, and ideas across the whole of Asia. This quiz "
                     "reads the road as the covenant of exchange."),
    },
    {
        "key": "qz_21", "name": "Mongol Empire Quiz",
        "group": "Medieval History", "ladder_rank": 7, "ladder_tier": "advanced",
        "description": ("A hard quiz on the Mongol Empire, the largest "
                        "contiguous land empire in history. Ten questions "
                        "cover Genghis Khan, the tumens, Kublai Khan, the "
                        "Pax Mongolica, and the Golden Horde. The steppe "
                        "conquerors who remade the map."),
        "how_it_works": "",
        "questions": [
            "What was the birth name of the man who took the title Genghis Khan?",
            "Genghis Khan was proclaimed khan of the united Mongols in which year?",
            "Which Mongol ruler founded the Yuan dynasty in China?",
            "Mongol armies were organized into swift units of ten thousand horsemen called what?",
            "Which city did Kublai Khan make his capital, on the site of modern Beijing?",
            "Marco Polo served at the court of which khan?",
            "The Mongol peace that secured trade across Eurasia was called what?",
            "Which Mongol khanate ruled over Russia for two centuries?",
            "The Mongol advance into Europe halted after the death of which khan in 1241?",
            "Timur, called Tamerlane, claimed descent from whom?",
        ],
        "answers": [
            "Temujin.",
            "1206.",
            "Kublai Khan.",
            "Tumens.",
            "Khanbaliq, also called Dadu.",
            "Kublai Khan.",
            "The Pax Mongolica, the Mongol Peace.",
            "The Golden Horde.",
            "Ogedei Khan.",
            "Genghis Khan.",
        ],
        "standards": ["Era: Mongol Empire, 1206-1368",
                      "Difficulty: hard - advanced",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_MONGOL],
        "sig_lens": ("Through the Signature lens, the Mongols are the "
                     "signature of speed: horse and bow signing an empire "
                     "from the Pacific to Europe in a single lifetime. This "
                     "quiz reads the khanate as the covenant of the "
                     "unbroken horizon."),
    },
    {
        "key": "qz_22", "name": "Black Death Quiz",
        "group": "Medieval History", "ladder_rank": 7, "ladder_tier": "advanced",
        "description": ("A hard quiz on the Black Death, the plague that "
                        "killed a third of Europe and remade its society. "
                        "Ten questions cover the disease, its spread, the "
                        "flagellants, quarantine, and the labor shortage "
                        "that cracked serfdom. The medieval world's "
                        "greatest catastrophe."),
        "how_it_works": "",
        "questions": [
            "The Black Death peaked in Europe during which years?",
            "What disease caused the Black Death?",
            "The plague was spread to humans chiefly by what?",
            "Roughly what share of Europe's population died in the plague?",
            "The plague first reached Europe through which Mediterranean island?",
            "Which shortage after the plague weakened the system of serfdom?",
            "The flagellants believed they could stop the plague by doing what?",
            "Boccaccio's Decameron, written after the plague, is set in which city?",
            "Holding arriving ships offshore gave the English language which word?",
            "Which 1665 outbreak is remembered as the Great Plague of London?",
        ],
        "answers": [
            "1347 to 1351.",
            "Bubonic plague, caused by the bacterium Yersinia pestis.",
            "Fleas carried by rats.",
            "About one third, between thirty and fifty percent.",
            "Sicily.",
            "The shortage of peasant laborers, which raised wages.",
            "Publicly whipping themselves in penance.",
            "Florence.",
            "Quarantine, from the Italian quarantina.",
            "The Great Plague of London of 1665.",
        ],
        "standards": ["Era: Black Death, 1347-1351",
                      "Difficulty: hard - advanced",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_MEDIEVAL],
        "sig_lens": ("Through the Signature lens, the plague is the "
                     "signature of fragility: a whole civilization "
                     "discovering that its grandest works rest on living "
                     "hands. This quiz reads the Black Death as the "
                     "covenant of humility before nature."),
    },
    {
        "key": "qz_23", "name": "French Revolution Quiz",
        "group": "Modern History", "ladder_rank": 7, "ladder_tier": "advanced",
        "description": ("A hard quiz on the French Revolution, the decade "
                        "that toppled a monarchy and terrified Europe. Ten "
                        "questions cover the Bastille, the Terror, "
                        "Robespierre, and the general who ended it all with "
                        "a coup. Liberty, equality, and the guillotine."),
        "how_it_works": "",
        "questions": [
            "The French Revolution is conventionally dated to begin in which year?",
            "The storming of which prison on July 14, 1789 symbolized the Revolution?",
            "The device used for revolutionary executions was called what?",
            "Who was the leading figure of the Reign of Terror?",
            "The Terror ended with Robespierre's execution in which month of 1794?",
            "The Declaration of the Rights of Man and of the Citizen was adopted in which year?",
            "Which French king was executed in January 1793?",
            "Marie Antoinette was the queen of which country?",
            "Napoleon Bonaparte seized power in the coup of which year?",
            "The Napoleonic Code was a sweeping reform of what?",
        ],
        "answers": [
            "1789.",
            "The Bastille.",
            "The guillotine.",
            "Maximilien Robespierre.",
            "July 1794, in the month of Thermidor.",
            "1789.",
            "Louis XVI.",
            "France.",
            "1799, the coup of 18 Brumaire.",
            "The civil legal system.",
        ],
        "standards": ["Era: French Revolution, 1789-1799",
                      "Difficulty: hard - advanced",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_FRREV],
        "sig_lens": ("Through the Signature lens, the Revolution is the "
                     "signature of the people erupting: a nation seizing "
                     "the pen from its king and signing in blood before it "
                     "learned to sign in law. This quiz reads 1789 as the "
                     "covenant of the crowd and its cost."),
    },
    {
        "key": "qz_24", "name": "Great Empires of the Americas Quiz",
        "group": "World History", "ladder_rank": 7, "ladder_tier": "advanced",
        "description": ("A hard quiz on the great Indigenous empires of the "
                        "Americas. Ten questions cover the Aztec, Maya, and "
                        "Inca, Tenochtitlan and Cuzco, quipus and the Three "
                        "Sisters. Civilizations the textbooks once "
                        "skipped."),
        "how_it_works": "",
        "questions": [
            "What was the capital of the Aztec Empire called?",
            "Tenochtitlan stood on the site of which modern capital city?",
            "The Inca Empire was centered in which modern country?",
            "What was the capital of the Inca Empire?",
            "Inca engineers built rope bridges across which great mountain range?",
            "The Maya developed a writing system of what kind?",
            "Who was the Aztec ruler when the Spanish arrived?",
            "The Inca kept records with knotted cords called what?",
            "Cahokia, the great Mississippian city, stands in which modern American state?",
            "Maize, beans, and squash were known to Native farmers by what name?",
        ],
        "answers": [
            "Tenochtitlan.",
            "Mexico City.",
            "Peru.",
            "Cuzco.",
            "The Andes.",
            "A hieroglyphic script.",
            "Moctezuma II.",
            "Quipus.",
            "Illinois.",
            "The Three Sisters.",
        ],
        "standards": ["Era: Pre-Columbian Americas, c. 250-1533 CE",
                      "Difficulty: hard - advanced",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_AMERICAS],
        "sig_lens": ("Through the Signature lens, the American empires are "
                     "the signature of independence: great civilizations "
                     "that signed their own lines with no ink from the Old "
                     "World. This quiz reads them as the covenant of the "
                     "separate path."),
    },
    {
        "key": "qz_25", "name": "Hundred Years War Quiz",
        "group": "Medieval History", "ladder_rank": 8, "ladder_tier": "advanced",
        "description": ("A hard quiz on the Hundred Years' War, the long "
                        "duel between England and France. Ten questions "
                        "cover Crecy, Agincourt, Joan of Arc, and the "
                        "peasant girl who turned a war around. One hundred "
                        "sixteen years of arrows and armor."),
        "how_it_works": "",
        "questions": [
            "The Hundred Years' War was fought between which two kingdoms?",
            "How long did the war actually last?",
            "Which 1346 battle first showcased the power of the English longbow?",
            "Which peasant girl led French forces to victory and was later canonized?",
            "Joan of Arc was burned at the stake in which year?",
            "Which English king won the great victory at Agincourt in 1415?",
            "The war began over English claims to which throne?",
            "Which 1429 siege did Joan of Arc lift, turning the war?",
            "When the war ended, England held only which French port?",
            "Which new gunpowder weapon helped France win the late battles of the war?",
        ],
        "answers": [
            "England and France.",
            "One hundred sixteen years, from 1337 to 1453.",
            "The Battle of Crecy.",
            "Joan of Arc.",
            "1431.",
            "Henry V.",
            "The French throne.",
            "The Siege of Orleans.",
            "Calais.",
            "Cannon, field artillery.",
        ],
        "standards": ["Era: Hundred Years' War, 1337-1453",
                      "Difficulty: hard - advanced",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_MEDIEVAL],
        "sig_lens": ("Through the Signature lens, the Hundred Years' War "
                     "is the signature of endurance: two kingdoms signing "
                     "the same quarrel across five generations. This quiz "
                     "reads the war as the covenant of the long grudge."),
    },
    {
        "key": "qz_26", "name": "Ottoman Rise Quiz",
        "group": "Medieval History", "ladder_rank": 8, "ladder_tier": "advanced",
        "description": ("A hard quiz on the rise of the Ottoman Empire, from "
                        "a small Anatolian state to a three-continent power. "
                        "Ten questions cover Osman, Mehmed the Conqueror, "
                        "the Janissaries, Suleiman, and 1453. The empire "
                        "that outlived Byzantium."),
        "how_it_works": "",
        "questions": [
            "Who founded the Ottoman state around 1299?",
            "Which sultan conquered Constantinople in 1453?",
            "The Ottoman Empire's elite standing infantry corps was called what?",
            "Suleiman, who ruled at the empire's height, is known by what epithet?",
            "What became the Ottoman capital after 1453?",
            "The great 1571 defeat of the Ottoman fleet at Lepanto was what kind of battle?",
            "The empire's corps of legal and religious scholars was called what?",
            "Which 1526 battle gave the Ottomans control of Hungary?",
            "The Ottoman government was known in Europe as the Sublime what?",
            "After 1517 the Ottoman sultans also claimed which religious title?",
        ],
        "answers": [
            "Osman I.",
            "Mehmed II, called Mehmed the Conqueror.",
            "The Janissaries.",
            "Suleiman the Magnificent.",
            "Constantinople, called Istanbul by the Turks.",
            "A naval battle.",
            "The ulema.",
            "The Battle of Mohacs.",
            "The Sublime Porte.",
            "Caliph.",
        ],
        "standards": ["Era: Ottoman rise, c. 1299-1571",
                      "Difficulty: hard - advanced",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_MEDIEVAL],
        "sig_lens": ("Through the Signature lens, the Ottomans are the "
                     "signature of ascent: a frontier band signing its name "
                     "larger with every generation until it covered three "
                     "continents. This quiz reads the rise as the covenant "
                     "of the steady climb."),
    },
    {
        "key": "qz_27", "name": "Industrial Revolution Quiz",
        "group": "Modern History", "ladder_rank": 8, "ladder_tier": "advanced",
        "description": ("A hard quiz on the Industrial Revolution, the "
                        "transformation that moved humanity from farm to "
                        "factory. Ten questions cover Watt, Stephenson, "
                        "steel, the Luddites, and the cities that swallowed "
                        "the countryside. The machine age begins."),
        "how_it_works": "",
        "questions": [
            "The Industrial Revolution began in which country?",
            "Which invention did James Watt decisively improve?",
            "The spinning jenny belonged to which industry?",
            "Which fuel powered the early steam engines and ironworks?",
            "The first public steam railway opened in 1825 between which two towns?",
            "Who built the famous Rocket locomotive?",
            "The Bessemer process revolutionized the making of what?",
            "Workers who smashed factory machines in protest were called what?",
            "The electric telegraph was developed in the 1830s and 1840s by whom?",
            "The movement of workers into growing factory towns is called what?",
        ],
        "answers": [
            "Britain, beginning in England.",
            "The steam engine, with the separate condenser.",
            "The textile industry, cotton spinning.",
            "Coal.",
            "Stockton and Darlington.",
            "George Stephenson.",
            "Steel.",
            "Luddites.",
            "Samuel Morse.",
            "Urbanization.",
        ],
        "standards": ["Era: Industrial Revolution, c. 1760-1840",
                      "Difficulty: hard - advanced",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_INDREV],
        "sig_lens": ("Through the Signature lens, the Industrial "
                     "Revolution is the signature of the machine: iron "
                     "hands signing a new world of steam, steel, and speed. "
                     "This quiz reads the age as the covenant of the "
                     "engine."),
    },
    {
        "key": "qz_28", "name": "African Kingdoms Quiz",
        "group": "World History", "ladder_rank": 8, "ladder_tier": "advanced",
        "description": ("A hard quiz on the great kingdoms of Africa, from "
                        "Kush to Benin. Ten questions cover Mansa Musa's "
                        "famous pilgrimage, the scholars of Timbuktu, Great "
                        "Zimbabwe, the stelae of Aksum, and the bronze art "
                        "of Benin. Africa's own imperial age, too long left "
                        "out of the story."),
        "how_it_works": "",
        "questions": [
            "The Kingdom of Kush was centered in which modern country, south of Egypt?",
            "Kushite kings once ruled Egypt itself, as which numbered dynasty?",
            "The fabulously wealthy Mali emperor who made pilgrimage in 1324 was who?",
            "Mansa Musa's famous pilgrimage traveled to which holy city?",
            "Which great trading city served the Mali and Songhai empires as a center of learning?",
            "Great Zimbabwe was built by which people?",
            "The Aksumite Empire adopted which religion in the fourth century?",
            "Aksum is famous for towering carved stone monuments called what?",
            "The Kingdom of Benin lies in which modern country?",
            "Benin is celebrated for artworks cast in which metal?",
        ],
        "answers": [
            "Sudan.",
            "The Twenty-fifth Dynasty.",
            "Mansa Musa.",
            "Mecca.",
            "Timbuktu.",
            "The Shona people.",
            "Christianity.",
            "Stelae, sometimes called obelisks.",
            "Nigeria.",
            "Bronze.",
        ],
        "standards": ["Era: African kingdoms, c. 800 BCE - 1800 CE",
                      "Difficulty: hard - advanced",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_AFRICA],
        "sig_lens": ("Through the Signature lens, the African kingdoms are "
                     "the signature of gold and learning: Mansa Musa's "
                     "caravan signing wealth across the Sahara, Timbuktu's "
                     "scholars signing knowledge into manuscripts. This "
                     "quiz reads them as the covenant of the caravan."),
    },
    {
        "key": "qz_29", "name": "Late Medieval Culture Quiz",
        "group": "Medieval History", "ladder_rank": 9, "ladder_tier": "advanced",
        "description": ("A hard quiz on late medieval culture, the world of "
                        "Dante, Chaucer, and the first universities. Ten "
                        "questions cover the Divine Comedy, the Canterbury "
                        "Tales, Aquinas, Bologna, and the Wars of the Roses. "
                        "The Middle Ages at their most brilliant."),
        "how_it_works": "",
        "questions": [
            "Dante's Divine Comedy was written in which language?",
            "Chaucer's Canterbury Tales is written in what form of English?",
            "Which scholar wrote the great Summa Theologica?",
            "Europe's oldest university, founded in 1088, stands in which city?",
            "The Gothic style began at which abbey church near Paris?",
            "Medieval traveling poet-entertainers were known as what?",
            "The Hanseatic League was an alliance of what?",
            "Roger Bacon is remembered for promoting what approach to knowledge?",
            "Stained glass reached its height in which type of building?",
            "The Wars of the Roses were fought between which two noble houses?",
        ],
        "answers": [
            "Italian, the Tuscan dialect.",
            "Middle English.",
            "Thomas Aquinas.",
            "Bologna, in Italy.",
            "The Abbey of Saint-Denis.",
            "Minstrels, also called troubadours and jongleurs.",
            "Trading cities and their merchants.",
            "The experimental method, the early scientific method.",
            "Gothic cathedrals.",
            "The houses of Lancaster and York.",
        ],
        "standards": ["Era: Late Middle Ages, c. 1200-1500",
                      "Difficulty: hard - advanced",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_MEDIEVAL],
        "sig_lens": ("Through the Signature lens, late medieval culture "
                     "is the signature of the flowering mind: cathedrals "
                     "signing prayers in glass, poets signing epics in the "
                     "people's tongue. This quiz reads the age as the "
                     "covenant of the made beautiful."),
    },
    {
        "key": "qz_30", "name": "World War I Quiz",
        "group": "Modern History", "ladder_rank": 9, "ladder_tier": "advanced",
        "description": ("A hard quiz on World War I, the Great War that "
                        "shattered four empires. Ten questions cover the "
                        "assassination at Sarajevo, the trenches, the Somme, "
                        "the Lusitania, and the treaty that planted the "
                        "seeds of the next war. 1914 to 1918."),
        "how_it_works": "",
        "questions": [
            "World War I began in which year?",
            "The assassination that triggered the war killed whom?",
            "The assassin belonged to which Serbian secret society?",
            "The Western Front was dominated by what kind of warfare?",
            "Which 1916 battle became the war's great symbol of slaughter?",
            "The United States entered the war in which year?",
            "Germany's submarine campaign sank which famous liner in 1915?",
            "The treaty ending the war was signed at which palace?",
            "The League of Nations was proposed by which American president?",
            "The war guilt clause was part of which treaty?",
        ],
        "answers": [
            "1914.",
            "Archduke Franz Ferdinand of Austria and his wife Sophie.",
            "The Black Hand.",
            "Trench warfare.",
            "The Battle of the Somme.",
            "1917.",
            "The Lusitania.",
            "The Palace of Versailles.",
            "Woodrow Wilson.",
            "The Treaty of Versailles.",
        ],
        "standards": ["Era: World War I, 1914-1918",
                      "Difficulty: hard - advanced",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_WWI],
        "sig_lens": ("Through the Signature lens, the Great War is the "
                     "signature of the broken machine: empires signing "
                     "their own ends in mud and wire. This quiz reads 1914 "
                     "as the covenant of the warned and unheeding."),
    },
    {
        "key": "qz_31", "name": "World Revolutions Quiz",
        "group": "World History", "ladder_rank": 9, "ladder_tier": "advanced",
        "description": ("A hard quiz comparing the world's great "
                        "revolutions, from Haiti to Iran. Ten questions cover "
                        "Toussaint Louverture, Lenin, Mao, Castro, and the "
                        "Liberator of South America. Different continents, "
                        "different centuries, the same question: when do "
                        "peoples overthrow their rulers, and what comes next?"),
        "how_it_works": "",
        "questions": [
            "The Haitian Revolution of 1791 to 1804 was led by whom?",
            "Haiti was formerly which French colony?",
            "The Russian Revolution of 1917 overthrew which tsar?",
            "The Bolsheviks who seized power in Russia were led by whom?",
            "The Chinese Communist Revolution triumphed in which year?",
            "Who was the leader of China's Communist revolution?",
            "The Cuban Revolution brought which leader to power in 1959?",
            "The 1979 revolution in Iran overthrew which shah?",
            "South American independence was led by which general called the Liberator?",
            "The wave of revolutions in 1848 swept across which continent?",
        ],
        "answers": [
            "Toussaint Louverture.",
            "Saint-Domingue.",
            "Nicholas II.",
            "Vladimir Lenin.",
            "1949.",
            "Mao Zedong.",
            "Fidel Castro.",
            "Mohammad Reza Pahlavi.",
            "Simon Bolivar.",
            "Europe.",
        ],
        "standards": ["Era: Revolutions, 1791-1979",
                      "Difficulty: hard - advanced",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_REVS],
        "sig_lens": ("Through the Signature lens, revolutions are the "
                     "signature of the turning: peoples picking up the pen "
                     "of history and striking out the old line. This quiz "
                     "reads the revolutionary age as the covenant of the "
                     "fresh page."),
    },
    {
        "key": "qz_32", "name": "World War II Quiz",
        "group": "Modern History", "ladder_rank": 10, "ladder_tier": "advanced",
        "description": ("The hardest quiz tier opens with World War II, the "
                        "largest conflict in human history. Ten questions "
                        "cover Poland, D-Day, Stalingrad, Pearl Harbor, the "
                        "Manhattan Project, and the trials that followed. "
                        "The war that remade the world."),
        "how_it_works": "",
        "questions": [
            "World War II in Europe began with Germany's 1939 invasion of which country?",
            "The Allied invasion of Normandy on June 6, 1944 is known by what name?",
            "The turning-point battle on the Eastern Front in 1942 to 1943 was which?",
            "Japan attacked the American fleet at Pearl Harbor on what date?",
            "The Manhattan Project developed what weapon?",
            "The first atomic bomb used in war was dropped on which city?",
            "The Allied leaders set postwar plans at which 1945 conference?",
            "Germany surrendered in which month of 1945?",
            "The Nuremberg Trials prosecuted the leaders of which regime?",
            "The United Nations was founded in which year?",
        ],
        "answers": [
            "Poland.",
            "D-Day, Operation Overlord.",
            "The Battle of Stalingrad.",
            "December 7, 1941.",
            "The atomic bomb.",
            "Hiroshima.",
            "The Yalta Conference.",
            "May 1945.",
            "Nazi Germany.",
            "1945.",
        ],
        "standards": ["Era: World War II, 1939-1945",
                      "Difficulty: hard - advanced",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_WWII],
        "sig_lens": ("Through the Signature lens, the Second World War is "
                     "the signature of the abyss and the ascent: humanity "
                     "signing its darkest line and then, at terrible cost, "
                     "signing the charter of a new peace. This quiz reads "
                     "the war as the covenant of never again."),
    },
    {
        "key": "qz_33", "name": "Cold War Quiz",
        "group": "Modern History", "ladder_rank": 10, "ladder_tier": "advanced",
        "description": ("The hardest tier continues with the Cold War, the "
                        "half-century standoff that shaped the modern "
                        "world. Ten questions cover containment, Cuba, the "
                        "Berlin Wall, Korea, and the satellite that started "
                        "the space race. The long twilight struggle."),
        "how_it_works": "",
        "questions": [
            "The Cold War was a rivalry between which two superpowers?",
            "The 1962 standoff over Soviet missiles in Cuba is called what?",
            "The Berlin Wall was built in which year?",
            "The Berlin Wall fell in which year?",
            "The Soviet Union dissolved in which year?",
            "The North Atlantic Treaty Organization was founded in which year?",
            "The Soviet-led military alliance was called what?",
            "The American policy of preventing Soviet expansion was called what?",
            "The 1950 to 1953 war in Asia was fought in which country?",
            "The first artificial satellite, launched by the USSR in 1957, was called what?",
        ],
        "answers": [
            "The United States and the Soviet Union.",
            "The Cuban Missile Crisis.",
            "1961.",
            "1989.",
            "1991.",
            "1949.",
            "The Warsaw Pact.",
            "Containment.",
            "Korea.",
            "Sputnik 1.",
        ],
        "standards": ["Era: Cold War, 1947-1991",
                      "Difficulty: hard - advanced",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_COLDWAR],
        "sig_lens": ("Through the Signature lens, the Cold War is the "
                     "signature of the held breath: two giants signing "
                     "their rivalry in proxies and missiles but never the "
                     "final line. This quiz reads the standoff as the "
                     "covenant of the brink, walked back."),
    },
    {
        "key": "qz_34", "name": "Twentieth Century Milestones Quiz",
        "group": "World History", "ladder_rank": 10, "ladder_tier": "advanced",
        "description": ("The final quiz of the ladder: the twentieth "
                        "century's great milestones beyond the wars. Ten "
                        "questions cover flight, the vote, the Depression, "
                        "space, the end of apartheid, and the invention of "
                        "the web. A century of transformation."),
        "how_it_works": "",
        "questions": [
            "The first powered airplane flight was made by whom in 1903?",
            "The ocean liner Titanic sank in which year?",
            "American women won the vote with which constitutional amendment?",
            "The Great Depression began with the stock market crash in which year?",
            "The first human in space was who?",
            "Yuri Gagarin's historic flight took place in which year?",
            "The first crewed landing on the Moon happened in which year?",
            "Apartheid ended in South Africa with whose election as president in 1994?",
            "The World Wide Web was invented by whom?",
            "The fall of the Berlin Wall symbolized the end of what?",
        ],
        "answers": [
            "The Wright brothers, Orville and Wilbur.",
            "1912.",
            "The Nineteenth Amendment.",
            "1929.",
            "Yuri Gagarin.",
            "1961.",
            "1969.",
            "Nelson Mandela.",
            "Tim Berners-Lee.",
            "The Cold War.",
        ],
        "standards": ["Era: Twentieth century, 1900-1999",
                      "Difficulty: hard - advanced",
                      "Format: 10 questions, answers at the bottom"],
        "citations": [CIT_C20],
        "sig_lens": ("Through the Signature lens, the twentieth century "
                     "is the signature of acceleration: flight, the atom, "
                     "the chip, and the web signing change faster than any "
                     "age before. This quiz reads the century as the "
                     "covenant of the quickening world."),
    },
]

for _e in ENTRIES:
    _e["how_it_works"] = _HOW(_e["name"])
    assert len(_e["questions"]) == 10, "not 10 questions in %s" % _e["key"]
    assert len(_e["answers"]) == 10, "not 10 answers in %s" % _e["key"]
    assert all(q.strip().endswith("?") for q in _e["questions"]), "q mark in %s" % _e["key"]
    assert all(len(a) > 2 for a in _e["answers"]), "short answer in %s" % _e["key"]

_ranks = [_e["ladder_rank"] for _e in ENTRIES]
assert _ranks == sorted(_ranks), "entries not in ladder order"
assert len(ENTRIES) == 34, "need 34 entries, have %d" % len(ENTRIES)
assert len({_e["key"] for _e in ENTRIES}) == 34, "dup keys"
assert len({_e["name"] for _e in ENTRIES}) == 34, "dup names"
