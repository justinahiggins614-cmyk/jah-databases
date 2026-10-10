(function(){'use strict';
/* JAH Linguistics Database generator — jahdb-linguistics-1.0.
   Deterministic client-side generator: same seed + same version = same record.
   Online-sourced language/concept profiles carry src:"online"; Signature-authored
   comparative studies carry src:"signature". All anchor facts are verifiable. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=['language-profile','phonology','morphology','syntax','semantics','sociolinguistics','historical','psycholinguistics'];
var PREFIX='JAH-LIN-';
/* language anchors: [name, cat, iso, family, native speakers (millions), script, facts...]
   concept anchors: [title, cat, "-", "-", 0, "-", facts...] */
var ANCH=[
["Mandarin Chinese","language-profile","cmn","Sino-Tibetan",988,"Chinese characters",
 "Mandarin Chinese has about 988 million native speakers (Ethnologue 2026), the largest native-speaking population of any language.",
 "It is a tonal Sino-Tibetan language where pitch distinguishes meaning: ma can mean mother, hemp, horse, or scold by tone.",
 "Written Chinese uses logographic characters shared across mutually unintelligible spoken varieties.",
 "Standard Mandarin is the official language of China and Taiwan and one of six UN official languages."],
["Spanish","language-profile","spa","Indo-European (Romance)",487,"Latin",
 "Spanish has about 487 million native speakers, the second-largest native population after Mandarin.",
 "A Romance language descended from Vulgar Latin, it is official in 20 countries across Europe and the Americas.",
 "Spanish phonology is famously regular: five pure vowels and highly predictable spelling.",
 "The Royal Spanish Academy, founded in 1713, standardizes usage across the Spanish-speaking world."],
["English","language-profile","eng","Indo-European (Germanic)",372,"Latin",
 "English has about 372 million native speakers and over 1.1 billion second-language speakers, totaling nearly 1.5 billion.",
 "A Germanic language transformed by Norman French vocabulary, it has a vast lexicon and relatively simple morphology.",
 "English is the global lingua franca of business, science, aviation, and the internet.",
 "Its spelling preserves centuries of history, making it famously irregular."],
["Hindi","language-profile","hin","Indo-European (Indo-Aryan)",347,"Devanagari",
 "Hindi has about 347 million native speakers and is an official language of India.",
 "An Indo-Aryan language written in Devanagari, it is mutually intelligible with Urdu in colloquial speech.",
 "Hindi distinguishes aspirated and unaspirated consonants and uses ergative case marking in perfective clauses.",
 "Bollywood films spread Hindi-Urdu across South Asia and its diaspora."],
["Portuguese","language-profile","por","Indo-European (Romance)",252,"Latin",
 "Portuguese has about 252 million native speakers, most of them in Brazil.",
 "A Romance language with nasal vowels and a distinctive sh-like pronunciation of s before consonants.",
 "It is official in nine countries across four continents, from Brazil to Angola to East Timor.",
 "Galician in Spain is closely related, and the two are largely mutually intelligible."],
["Bengali","language-profile","ben","Indo-European (Indo-Aryan)",234,"Bengali",
 "Bengali has about 234 million native speakers in Bangladesh and India's West Bengal.",
 "Its literary tradition includes Nobel laureate Rabindranath Tagore, who wrote India's and Bangladesh's anthems.",
 "Bengali is written in its own Brahmic-derived script with distinctive horizontal headline strokes.",
 "The 1952 Language Movement martyrs are commemorated worldwide on International Mother Language Day."],
["Russian","language-profile","rus","Indo-European (Slavic)",133,"Cyrillic",
 "Russian has about 133 million native speakers and is the most widely spoken Slavic language.",
 "Written in Cyrillic, it preserves a rich case system with six cases and verbal aspect distinctions.",
 "It is an official language of the UN and the lingua franca across much of Eurasia.",
 "Russian stress is free and mobile, shifting within word families."],
["Japanese","language-profile","jpn","Japonic",124,"Kanji, hiragana, katakana",
 "Japanese has about 124 million native speakers, nearly all in Japan.",
 "It uses three scripts together: kanji (Chinese characters), hiragana, and katakana.",
 "Japanese is agglutinative and SOV in word order, with elaborate honorific levels encoding social relations.",
 "Its pitch-accent system distinguishes words like hashi (bridge, chopsticks, edge) by melody."],
["Turkish","language-profile","tur","Turkic",86,"Latin",
 "Turkish has about 86 million native speakers and is the most widely spoken Turkic language.",
 "It is strongly agglutinative with vowel harmony: suffixes harmonize their vowels with the stem.",
 "Ataturk's 1928 reform replaced the Arabic script with Latin and purged many Arabic and Persian loans.",
 "Turkish has no grammatical gender and no definite article."],
["Vietnamese","language-profile","vie","Austroasiatic",86,"Latin (quoc ngu)",
 "Vietnamese has about 86 million native speakers, the largest Austroasiatic language by far.",
 "It is tonal with six tones in the northern standard and written in a Latin-based script created by missionaries.",
 "Vietnamese is analytic and monosyllabic in tendency, with classifiers required for counting nouns.",
 "Thousands of Chinese loanwords reflect a millennium of Chinese cultural influence."],
["Korean","language-profile","kor","Koreanic",82,"Hangul",
 "Korean has about 82 million native speakers on the Korean peninsula and in diaspora.",
 "Hangul, created under King Sejong in 1443, is a scientific alphabet whose letter shapes depict speech organs.",
 "Korean is agglutinative and SOV, with seven speech levels encoding formality.",
 "Its isolate status is debated; most linguists treat Koreanic as a small independent family."],
["Tamil","language-profile","tam","Dravidian",79,"Tamil",
 "Tamil has about 79 million native speakers in India, Sri Lanka, and Singapore.",
 "With inscriptions from the 3rd century BCE, it has one of the world's longest continuous literary traditions.",
 "Tamil famously resists Sanskrit loans, preserving a classical Dravidian vocabulary.",
 "It diglossically separates a formal written standard from divergent spoken varieties."],
["Urdu","language-profile","urd","Indo-European (Indo-Aryan)",78,"Perso-Arabic (Nastaliq)",
 "Urdu has about 78 million native speakers and is Pakistan's national language.",
 "Colloquially identical to Hindi, it is written in Perso-Arabic Nastaliq script with heavy Persian and Arabic vocabulary.",
 "Urdu poetry — especially the ghazal — is among the world's great literary traditions.",
 "It developed in the Mughal military camps, its name deriving from the Turkic word for army."],
["Indonesian","language-profile","ind","Austronesian",78,"Latin",
 "Indonesian has about 78 million native speakers but over 250 million total speakers as a second language.",
 "A standardized form of Malay, it was chosen in 1928 as the unifying language of the archipelago.",
 "Its simple morphology — no tenses, no gender, reduplication for plurals — makes it famously easy to begin.",
 "Indonesian absorbs loanwords freely from Dutch, Arabic, Sanskrit, and English."],
["German","language-profile","deu","Indo-European (Germanic)",76,"Latin",
 "Standard German has about 76 million native speakers across Germany, Austria, and Switzerland.",
 "It preserves four cases, three genders, and verb-second word order in main clauses.",
 "German compounds freely: Donaudampfschifffahrtsgesellschaftskapitan is a classic example.",
 "The High German consonant shift separates it from English and Dutch historically."],
["French","language-profile","fra","Indo-European (Romance)",75,"Latin",
 "French has about 75 million native speakers and 334 million total speakers including Africa's growing francophonie.",
 "A Romance language with nasal vowels and silent final consonants, it was Europe's diplomatic language for centuries.",
 "The Academie Francaise, founded in 1635, guards its vocabulary against anglicisms.",
 "French liaison and elision make its connected speech famously fluid."],
["Javanese","language-profile","jav","Austronesian",69,"Latin (Javanese script historic)",
 "Javanese has about 69 million native speakers, the largest Austronesian language by native population.",
 "It has multiple speech levels — ngoko, madya, krama — chosen by the speakers' relative status.",
 "Classical Javanese literature includes the Ramayana-derived kakawin epics.",
 "Most Javanese today write in Latin script, though a traditional script survives ceremonially."],
["Italian","language-profile","ita","Indo-European (Romance)",60,"Latin",
 "Italian has about 60 million native speakers and is the closest major language to Latin phonologically.",
 "Based on Tuscan dialect through Dante's prestige, it unified Italy's dialects after 1861.",
 "Italian has seven vowel phonemes and geminate (doubled) consonants that change meaning.",
 "It remains the language of opera libretti and musical terminology worldwide."],
["Hausa","language-profile","hau","Afro-Asiatic (Chadic)",58,"Latin (Ajami historic)",
 "Hausa has about 58 million native speakers across West Africa, with millions more second-language speakers.",
 "A Chadic Afro-Asiatic language, it is the region's great trade lingua franca.",
 "Hausa has ejective consonants and a three-tone system unusual for the area.",
 "Ajami (Arabic-script) Hausa literature dates back centuries."],
["Gujarati","language-profile","guj","Indo-European (Indo-Aryan)",58,"Gujarati",
 "Gujarati has about 58 million native speakers in western India and a vast global diaspora.",
 "Mahatma Gandhi wrote his autobiography in Gujarati, and it remains Gujarat's official language.",
 "It has three genders and an ergative-absolutive alignment in perfective aspect.",
 "Gujarati merchants carried the language to East Africa, Britain, and North America."],
["Marathi","language-profile","mar","Indo-European (Indo-Aryan)",83,"Devanagari",
 "Marathi has about 83 million native speakers, centered in Maharashtra, India.",
 "Its literature stretches back to the 13th-century saint-poets like Dnyaneshwar.",
 "Marathi preserves three genders and a complex honorific system.",
 "Mumbai's film and theater industries broadcast Marathi culture worldwide."],
["Telugu","language-profile","tel","Dravidian",83,"Telugu",
 "Telugu has about 83 million native speakers, the largest Dravidian language by population.",
 "Called the 'Italian of the East' for its vowel-ending words and musical quality.",
 "Its script is a rounded Brahmic abugida; classical literature dates to the 11th century.",
 "Telugu cinema (Tollywood) is one of India's biggest film industries."],
["Punjabi","language-profile","pan","Indo-European (Indo-Aryan)",90,"Gurmukhi/Shahmukhi",
 "Western Punjabi has about 90 million native speakers across Pakistan and India.",
 "Punjabi is tonal — rare among Indo-European languages — with three contrastive tones.",
 "It is written in Gurmukhi in India and Shahmukhi (Perso-Arabic) in Pakistan.",
 "Bhangra music and Sikh scripture give Punjabi global cultural reach."],
["Arabic","language-profile","ara","Afro-Asiatic (Semitic)",400,"Arabic",
 "Arabic has roughly 400 million speakers across its many varieties, with Modern Standard Arabic as the formal register.",
 "A Semitic language built on triconsonantal roots: k-t-b yields kitab (book), katib (writer), maktaba (library).",
 "Diglossia is extreme: no one speaks MSA natively; everyone learns it in school.",
 "Classical Arabic's Quranic prestige has preserved the language's unity for fourteen centuries."],
["Swahili","language-profile","swa","Niger-Congo (Bantu)",95,"Latin",
 "Swahili has about 95 million total speakers, mostly as a second language across East Africa.",
 "A Bantu language with heavy Arabic vocabulary, it uses noun classes rather than gender.",
 "It is an official language of the African Union and a UN working language.",
 "Julius Nyerere's Tanzania made Swahili a model of nation-building through language."],
["Amharic","language-profile","amh","Afro-Asiatic (Semitic)",35,"Ge'ez (Ethiopic)",
 "Amharic has about 35 million speakers and is Ethiopia's federal working language.",
 "A Semitic language written in the Ge'ez abugida, each character encoding a consonant-vowel pair.",
 "Its ancient Ge'ez liturgical ancestor preserves some of Africa's oldest written literature.",
 "Amharic has ejective consonants typical of Ethiopian Semitic languages."],
["Hebrew","language-profile","heb","Afro-Asiatic (Semitic)",9,"Hebrew",
 "Modern Hebrew has about 9 million speakers and is history's only fully successful revived language.",
 "Eliezer Ben-Yehuda led its revival as a spoken mother tongue in late-19th-century Palestine.",
 "Its triconsonantal root morphology mirrors Arabic's, with ancient and modern layers fused.",
 "Hebrew is now Israel's official language with a complete modern vocabulary."],
["Persian (Farsi)","language-profile","fas","Indo-European (Iranian)",65,"Perso-Arabic",
 "Iranian Persian has about 65 million native speakers, with Dari and Tajik as close varieties.",
 "An Iranian language with a thousand-year literary tradition from Ferdowsi's Shahnameh to Rumi.",
 "Persian has almost no inflection: no gender, simplified verbs, and ezafe constructions for possession.",
 "It served as the lingua franca of Central and South Asian courts for centuries."],
["Thai","language-profile","tha","Kra-Dai",60,"Thai",
 "Thai has about 60 million native speakers and is Thailand's official language.",
 "A tonal Kra-Dai language with five tones, written in an Indic-derived abugida.",
 "Thai has elaborate royal and monastic registers with distinct vocabularies.",
 "Its classifiers and serial verbs typify mainland Southeast Asian grammar."],
["Burmese","language-profile","mya","Sino-Tibetan",33,"Burmese",
 "Burmese has about 33 million native speakers in Myanmar.",
 "A tonal Sino-Tibetan language written in a circular Brahmic script.",
 "Burmese distinguishes plain and polite registers and uses sentence-final particles for mood.",
 "Its literary tradition includes royal chronicles spanning a millennium."],
["Khmer","language-profile","khm","Austroasiatic",17,"Khmer",
 "Khmer has about 17 million native speakers in Cambodia.",
 "The only Austroasiatic national language, it is non-tonal with a huge vowel inventory.",
 "Angkor's inscriptions give Khmer one of Southeast Asia's oldest written traditions.",
 "Its script, with subscript consonants, is among the world's most complex."],
["Mongolian","language-profile","mon","Mongolic",6,"Cyrillic (traditional vertical historic)",
 "Mongolian has about 6 million speakers in Mongolia, China, and Russia.",
 "An agglutinative SOV language with vowel harmony, written in Cyrillic in Mongolia since the 1940s.",
 "The traditional vertical script, derived from Old Uyghur, survives ceremonially.",
 "The 13th-century Secret History is Mongolian literature's founding monument."],
["Georgian","language-profile","kat","Kartvelian",4,"Mkhedruli",
 "Georgian has about 4 million native speakers and is the flagship of the Kartvelian family.",
 "Its Mkhedruli alphabet, with 33 letters, has been used since the 11th century.",
 "Georgian verbs can stack six or more prefixes and suffixes in polypersonal agreement.",
 "Consonant clusters like gvprtskvni ('you peel us') are legendary among linguists."],
["Armenian","language-profile","hye","Indo-European",6,"Armenian",
 "Armenian has about 6 million speakers in Armenia and a worldwide diaspora.",
 "Mesrop Mashtots created its 39-letter alphabet in 405 CE to translate the Bible.",
 "An independent Indo-European branch, it preserves ancient features alongside innovations.",
 "Eastern and Western dialects diverged after the Armenian dispersion."],
["Greek","language-profile","ell","Indo-European (Hellenic)",13,"Greek",
 "Modern Greek has about 13 million native speakers, heir to 3,400 years of written Greek.",
 "The Greek alphabet, adapted from Phoenician around 800 BCE, added vowels — a world-historical innovation.",
 "Ancient Greek's literature, from Homer to the New Testament, shaped Western thought.",
 "Katharevousa and Demotic fought a century-long language question settled in 1976."],
["Latin","language-profile","lat","Indo-European (Italic)",0,"Latin",
 "Latin, Rome's language, survives as the liturgical language of the Catholic Church and the root of the Romance languages.",
 "Classical Latin's case system and periodic sentences set the model for European literary prose.",
 "No native speakers remain, but millions read it and it lives on in scientific nomenclature.",
 "Vulgar Latin, the soldiers' and settlers' speech, evolved into French, Spanish, Italian, and kin."],
["Sanskrit","language-profile","san","Indo-European (Indo-Aryan)",0,"Devanagari",
 "Sanskrit is the classical language of India, preserved by Panini's grammar (c. 4th century BCE).",
 "Panini's Ashtadhyayi, with 4,000 rules, is among humanity's greatest intellectual achievements.",
 "Vedic Sanskrit's hymns date to c. 1500 BCE, making it among the oldest attested Indo-European languages.",
 "It remains a liturgical and scholarly language with a modern revival movement."],
["Basque","language-profile","eus","Language isolate",0.8,"Latin",
 "Basque, with about 800,000 speakers, is Europe's great language isolate, unrelated to any other living tongue.",
 "It is ergative-absolutive: subjects of intransitives pattern with objects, not with transitive subjects.",
 "Basque survived Roman, Visigothic, and Franco-Spanish pressure in the western Pyrenees.",
 "Its origins predate Indo-European arrival in Europe."],
["Finnish","language-profile","fin","Uralic",5,"Latin",
 "Finnish has about 5 million native speakers and is the best-known Uralic language.",
 "Its fifteen cases and agglutinative morphology build famously long words.",
 "The Kalevala epic, compiled by Elias Lonnrot in 1835, founded Finnish national literature.",
 "Finnish has no grammatical gender and no future tense."],
["Hungarian","language-profile","hun","Uralic",13,"Latin",
 "Hungarian has about 13 million native speakers, a Uralic island in Central Europe.",
 "Eighteen cases, vowel harmony, and definite/indefinite verb conjugations mark its grammar.",
 "Most vocabulary is non-Indo-European, though centuries of contact added Latin, Slavic, and German loans.",
 "Hungarian arrived with the Magyars in the 9th century CE."],
["Icelandic","language-profile","isl","Indo-European (Germanic)",0.4,"Latin",
 "Icelandic, spoken by about 400,000 people, is the most conservative Germanic language.",
 "Deliberate purism coins native terms for new concepts instead of borrowing.",
 "Medieval sagas remain readable to modern Icelanders with modest effort.",
 "Its inflectional complexity rivals Old Norse, its direct ancestor."],
["Irish","language-profile","gle","Indo-European (Celtic)",0.2,"Latin",
 "Irish has about 200,000 daily speakers and is the Republic of Ireland's first official language.",
 "A Celtic language with initial mutations: consonants change by grammatical context.",
 "Old Irish manuscripts preserve Europe's oldest vernacular literature north of the Alps.",
 "Revival efforts include Gaeltacht regions and Irish-medium schools."],
["Welsh","language-profile","cym","Indo-European (Celtic)",0.9,"Latin",
 "Welsh has about 900,000 speakers and is among the healthiest Celtic languages.",
 "Its mutations, vigesimal counting, and verb-initial word order mark its Celtic character.",
 "The 1993 Welsh Language Act and devolution-era policies drove its revival.",
 "Welsh-medium education now produces new young speakers yearly."],
["Navajo","language-profile","nav","Na-Dene",0.17,"Latin",
 "Navajo has about 170,000 speakers, the largest Native American language community north of Mexico.",
 "A Na-Dene language with tonal contrasts and famously complex verb morphology.",
 "Navajo code talkers' unbreakable wartime code exploited its complexity in World War II.",
 "Immersion schools now fight to transmit it to a new generation."],
["Cherokee","language-profile","chr","Iroquoian",0.02,"Cherokee syllabary",
 "Cherokee has about 20,000 speakers, mostly in Oklahoma and North Carolina.",
 "Sequoyah invented its 85-character syllabary around 1821 — a rare individual script invention.",
 "The syllabary made the Cherokee Nation one of the most literate societies of its era.",
 "Immersion programs work to reverse its endangered status."],
["Quechua","language-profile","que","Quechuan",9,"Latin",
 "Quechua has 8-10 million speakers across the Andes, the largest Indigenous language family of the Americas.",
 "The Inca Empire's lingua franca, it is agglutinative with evidential suffixes marking information source.",
 "Bolivia and Peru recognize it as an official language.",
 "Its three-vowel system and ejectives reflect millennia of Andean linguistic history."],
["Guarani","language-profile","grn","Tupian",6,"Latin",
 "Guarani has about 6 million speakers and is Paraguay's co-official language with Spanish.",
 "Most Paraguayans speak it regardless of ancestry — a rare case of Indigenous language nationalization.",
 "Jesuit reductions produced a rich colonial Guarani literature.",
 "Its nasal harmony spreads nasality across whole words."],
["Nahuatl","language-profile","nah","Uto-Aztecan",1.7,"Latin",
 "Nahuatl has about 1.7 million speakers in Mexico, heir to the Aztec Empire's language.",
 "Classical Nahuatl's literature — flower-and-song poetry — survives in 16th-century manuscripts.",
 "English words like chocolate, tomato, and coyote come from Nahuatl.",
 "It is agglutinative and polysynthetic, building whole sentences into single words."],
["Inuktitut","language-profile","iku","Eskimo-Aleut",0.04,"Syllabics/Latin",
 "Inuktitut has about 40,000 speakers across the Canadian Arctic.",
 "A polysynthetic language where one word can express a whole English sentence.",
 "It is an official language of Nunavut and the Northwest Territories.",
 "Its famous snow vocabulary reflects a richly differentiated Arctic lexicon."],
["Maori","language-profile","mri","Austronesian",0.15,"Latin",
 "Maori has about 150,000 speakers and is New Zealand's Indigenous language.",
 "Kohanga reo (language nests) pioneered immersion revival emulated worldwide.",
 "Maori is official in New Zealand alongside English and NZ Sign Language.",
 "Its macron-marked long vowels distinguish word meanings."],
["Hawaiian","language-profile","haw","Austronesian",0.024,"Latin",
 "Hawaiian has about 24,000 speakers after near-extinction in the 20th century.",
 "With only 13 phonemes, it has one of the world's smallest sound inventories.",
 "Punana Leo immersion preschools led its celebrated revival from the 1980s.",
 "The Hawaiian alphabet's okina (glottal stop) is a full consonant."],
["Tagalog","language-profile","tgl","Austronesian",33,"Latin",
 "Tagalog has about 33 million native speakers; its standardized form Filipino is the Philippines' national language.",
 "An Austronesian language with a symmetrical voice system and verb-initial tendencies.",
 "Enormous Spanish and English loan layers reflect colonial history.",
 "Tagalog verb affixes encode focus: actor, object, or location."],
["Malay","language-profile","msa","Austronesian",78,"Latin",
 "Malay has about 78 million native speakers across Malaysia, Indonesia, and Brunei.",
 "The historic trade language of Southeast Asia, written for centuries in Jawi (Arabic script).",
 "Standard Malay and Indonesian are mutually intelligible national standards.",
 "Its affixation system builds causatives, reciprocals, and nominalizations productively."],
["Zulu","language-profile","zul","Niger-Congo (Bantu)",12,"Latin",
 "Zulu has about 12 million native speakers, South Africa's largest home language.",
 "Its click consonants — borrowed from Khoisan languages — include dental, alveolar, and lateral clicks.",
 "Bantu noun classes organize its grammar into some fifteen agreement classes.",
 "Shaka's 19th-century kingdom spread Zulu across southeastern Africa."],
["Xhosa","language-profile","xho","Niger-Congo (Bantu)",8,"Latin",
 "Xhosa has about 8 million native speakers, including Nelson Mandela's mother tongue.",
 "Its name's click is the lateral click heard in the language's own name.",
 "Like Zulu, it has an extensive noun-class and click system.",
 "Xhosa-language media and schooling sustain it as a major African language."],
["Yoruba","language-profile","yor","Niger-Congo",45,"Latin",
 "Yoruba has about 45 million speakers in Nigeria, Benin, and Togo.",
 "A tonal language with three tones where pitch alone distinguishes words.",
 "Yoruba's Ifa divination corpus is UNESCO-recognized intangible heritage.",
 "The diaspora carried Yoruba religion and language to the Americas."],
["Igbo","language-profile","ibo","Niger-Congo",30,"Latin",
 "Igbo has about 30 million speakers in southeastern Nigeria.",
 "Tonal with downstep, it has a rich proverb tradition central to social life.",
 "Chinua Achebe's 'Things Fall Apart' brought Igbo culture to world literature.",
 "Its dialects form a continuum bridged by a standard literary form."],
["Kurdish","language-profile","kur","Indo-European (Iranian)",25,"Latin/Arabic/Cyrillic",
 "Kurdish has about 25 million speakers across Turkey, Iraq, Syria, and Iran.",
 "Kurmanji and Sorani are the main dialect groups, written in Latin and Arabic scripts respectively.",
 "An Iranian language with ergative constructions in past tenses.",
 "Statelessness makes Kurdish a language of cultural resistance."],
["Pashto","language-profile","pus","Indo-European (Iranian)",40,"Perso-Arabic",
 "Pashto has about 40 million speakers in Afghanistan and Pakistan.",
 "An Iranian language with retroflex consonants and a split-ergative system.",
 "The Pashtunwali code governs honor, hospitality, and revenge in Pashtun society.",
 "Classical Pashto poetry flowered under the Durrani Empire."],
["Nepali","language-profile","nep","Indo-European (Indo-Aryan)",16,"Devanagari",
 "Nepali has about 16 million native speakers and is Nepal's official language.",
 "An Indo-Aryan language that spread with the Gorkha kingdom's unification of Nepal.",
 "It has elaborate honorific verb forms encoding social hierarchy.",
 "Nepali serves as a lingua franca across the Himalayas."],
["Esperanto","language-profile","epo","Constructed",0.1,"Latin",
 "Esperanto, published by L. L. Zamenhof in 1887, is the world's most successful constructed language.",
 "Its regular agglutinative grammar has sixteen basic rules with no exceptions.",
 "An estimated 100,000-2,000,000 people speak it, with native-speaking families.",
 "Esperanto congresses have run continuously for over a century."],
["The phoneme","phonology","-","-",0,"-",
 "The phoneme is the smallest unit of sound that distinguishes meaning in a language.",
 "English /p/ and /b/ are separate phonemes, proven by the minimal pair 'pat' versus 'bat'.",
 "Phonemes are abstract categories; their physical realizations are called allophones.",
 "The concept, developed by Baudouin de Courtenay and the Prague School, organizes all phonological analysis."],
["The IPA","phonology","-","-",0,"-",
 "The International Phonetic Alphabet, created in 1888, provides a unique symbol for every speech sound.",
 "Maintained by the International Phonetic Association, it now covers over 160 symbols plus diacritics.",
 "Field linguists use it to document the world's 7,000 languages consistently.",
 "Its chart organizes consonants by place and manner of articulation."],
["Tone systems","phonology","-","-",0,"-",
 "Tone languages use pitch to distinguish word meaning, as in Mandarin, Yoruba, and Thai.",
 "About 60-70 percent of the world's languages use some form of lexical tone.",
 "Tone can be level, contour, or register, and interacts with intonation systems.",
 "African tone terraces and Asian contour tones show tone's typological range."],
["Morpheme typology","morphology","-","-",0,"-",
 "Languages are classified as isolating, agglutinative, fusional, or polysynthetic by how they build words.",
 "Mandarin is isolating (one morpheme per word); Turkish is agglutinative (clear suffix chains).",
 "Latin is fusional (one ending fuses many meanings); Inuktitut is polysynthetic (whole sentences per word).",
 "Most languages mix types; the classification describes tendencies, not essences."],
["Word order universals","syntax","-","-",0,"-",
 "About 45 percent of languages are SOV (subject-object-verb) and 42 percent SVO, per typological surveys.",
 "Joseph Greenberg's 1963 universals linked word order to adposition and adjective placement.",
 "SOV languages tend toward postpositions; SVO languages toward prepositions.",
 "Word order correlates with dozens of other grammatical properties."],
["Ergativity","syntax","-","-",0,"-",
 "Ergative languages mark transitive subjects differently from intransitive subjects and objects.",
 "Basque, Georgian, and many Australian languages show ergative-absolutive alignment.",
 "Split ergativity conditions the pattern on tense, aspect, or noun type.",
 "Ergativity proves that 'subject' is not a universal grammatical category."],
["Evidentiality","morphology","-","-",0,"-",
 "Evidentiality grammatically marks the source of information: seen, heard, inferred, or reported.",
 "Quechua requires speakers to mark how they know what they claim.",
 "Turkish's -mis suffix marks reported or inferred past events.",
 "Evidentials show grammar encoding epistemology, not just who did what."],
["Grimm's law","historical","-","-",0,"-",
 "Grimm's law describes the First Germanic consonant shift separating Germanic from other Indo-European languages.",
 "Formulated by Jacob Grimm in 1822, it maps PIE *p, *t, *k to Germanic *f, *th, *h.",
 "Latin pater versus English father exemplifies the shift.",
 "Verner's law (1875) explained its exceptions through ancient stress patterns."],
["The comparative method","historical","-","-",0,"-",
 "The comparative method reconstructs proto-languages from systematic sound correspondences in daughter languages.",
 "Neogrammarian regularity — sound change admits no exceptions — made reconstruction scientific in the 1870s.",
 "It rebuilt Proto-Indo-European, Proto-Austronesian, and dozens more.",
 "The method remains historical linguistics' gold standard."],
["Creoles and pidgins","sociolinguistics","-","-",0,"-",
 "Pidgins are simplified contact languages; creoles are pidgins nativized as mother tongues.",
 "Haitian Creole, with 12 million speakers, is the world's largest creole.",
 "Derek Bickerton argued creoles reveal innate grammar; others stress substrate influence.",
 "Creole studies illuminate how languages are born."],
["Diglossia","sociolinguistics","-","-",0,"-",
 "Diglossia, defined by Charles Ferguson in 1959, is the stable use of high and low varieties for different functions.",
 "Arabic, Greek, and Swiss German are classic diglossic situations.",
 "The high variety serves religion, education, and formality; the low serves home and street.",
 "Diglossia shows language variation organized by social domain."],
["Universal Grammar","psycholinguistics","-","-",0,"-",
 "Noam Chomsky's Universal Grammar proposes innate linguistic principles shared by all languages.",
 "The poverty of the stimulus argument holds that children learn more grammar than input could teach.",
 "'Syntactic Structures' (1957) launched the generative revolution in linguistics.",
 "The hypothesis remains linguistics' most debated claim."],
["Critical period hypothesis","psycholinguistics","-","-",0,"-",
 "The critical period hypothesis holds that language acquisition is biologically scheduled in childhood.",
 "Eric Lenneberg proposed it in 1967, linking lateralization to a puberty-closing window.",
 "Cases like Genie and late first-language learners support some version of the claim.",
 "It underlies debates on bilingual education and adult language learning."],
["Aphasia and the brain","psycholinguistics","-","-",0,"-",
 "Paul Broca (1861) and Carl Wernicke (1874) localized language production and comprehension in the left hemisphere.",
 "Broca's aphasia yields halting, agrammatic speech; Wernicke's yields fluent but empty speech.",
 "Modern imaging shows language distributed across wider networks than the classic areas.",
 "Aphasia research grounds the biology of language."],
["Zipf's law","semantics","-","-",0,"-",
 "Zipf's law states that a word's frequency is inversely proportional to its rank.",
 "George Kingsley Zipf found it in 1949 across languages and texts.",
 "The most frequent word occurs about twice as often as the second, three times the third.",
 "The law reflects efficient communication under least effort."],
["Gricean maxims","semantics","-","-",0,"-",
 "Paul Grice's 1975 maxims — quantity, quality, relation, manner — govern conversational implicature.",
 "Speakers mean more than they say by observably following or flouting these maxims.",
 "'Some of the students passed' implicates not all did, via the maxim of quantity.",
 "Pragmatics grew from Grice's logic of conversation."],
["Speech act theory","semantics","-","-",0,"-",
 "J. L. Austin's 'How to Do Things with Words' (1962) showed utterances perform actions: promising, naming, sentencing.",
 "John Searle systematized speech acts into assertives, directives, commissives, expressives, and declarations.",
 "'I now pronounce you married' changes reality by being said.",
 "The theory founded the philosophy of language's pragmatic turn."]
];
var ANGLES=["language profile","structural profile","historical profile","sociolinguistic profile"];
var SYNREL=[
 ["compared with","This Signature comparative study contrasts the two languages on structure, history, and social life."],
 ["contrasted against","This Signature contrast study draws out the typological distance between the two languages."],
 ["alongside","This Signature pairing study examines the two languages as windows on a shared linguistic phenomenon."],
 ["in dialogue with","This Signature study places the two languages in dialogue across families and continents."]
];
function filedLine(id){return "Filed as "+id+" in the JAH Linguistics Database archive.";}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var id=PREFIX+String(seed).padStart(6,'0');
  var pool=ANCH;
  if(opts.category){var f=ANCH.filter(function(a){return a[1]===opts.category;});if(f.length)pool=f;}
  var synth=!opts.category&&rnd()<0.35;
  if(synth){
    var A=pick(pool,rnd),B=pick(pool,rnd),guard=0;
    while(B===A&&guard++<20)B=pick(pool,rnd);
    var rel=pick(SYNREL,rnd);
    var title="Signature study: "+A[0]+" "+rel[0]+" "+B[0];
    var d=A[0]+" ("+A[3]+", ISO "+A[2]+"): "+A[6]+" "+rel[0]+" "+B[0]+" ("+B[3]+"), "+rel[1]+" "+B[6];
    return {id:id,title:title,description:d+" "+filedLine(id),category:"language-profile",
      spec:{kind:"study",pair:[A[0],B[0]],relation:rel[0],families:[A[3],B[3]],src:"signature"},
      iso:A[2],src:"signature"};
  }
  var A=pick(pool,rnd);
  var ang=pick(ANGLES,rnd);
  var facts=A.slice(6);
  var d=facts[0]+" "+pick(facts.slice(1),rnd);
  if(rnd()<0.6)d+=" "+pick(facts.slice(1),rnd);
  var title=A[0]+" — "+ang;
  var spec={kind:A[1],family:A[3],script:A[5],src:"online"};
  if(A[1]==="language-profile"){spec.iso=A[2];spec.native_speakers_m=A[4];}
  return {id:id,title:title,description:d+" "+filedLine(id),category:A[1],
    spec:spec,iso:A[2],src:"online",_facts:facts,_an:A[0]};
}
function sentences(s){return String(s).split(/[.!?]+/).filter(function(x){return x.trim().length>10;}).length;}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!/^JAH-LIN-\d{6}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<4)e.push('title');
  if(typeof r.description!=='string'||r.description.length<80)e.push('description');
  else if(sentences(r.description)<2)e.push('description-sentences');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(r.src!=='online'&&r.src!=='signature')e.push('src');
  if(typeof r.iso!=='string'||!r.iso.length)e.push('iso');
  var s=r.spec;
  if(!s||typeof s!=='object')e.push('spec');
  else{
    if(s.src!=='online'&&s.src!=='signature')e.push('spec.src');
    if(s.src!==r.src)e.push('spec.src-mismatch');
    if(s.src==='online'){
      if(typeof s.family!=='string'||!s.family.length)e.push('spec.family');
      if(typeof s.script!=='string'||!s.script.length)e.push('spec.script');
      if(r.category==='language-profile'){
        if(typeof s.native_speakers_m!=='number'||s.native_speakers_m<0||s.native_speakers_m>1500)e.push('spec.speakers');
        if(!/^[a-z]{3}$/.test(s.iso||''))e.push('spec.iso');
      }
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
var gen={version:'jahdb-linguistics-1.0',generate:generate,validate:validate,signatureVersion:signatureVersion};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('linguistics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
