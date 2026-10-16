#!/usr/bin/env python3
"""PHASE D — Everything databases, entries part C: psychology, history,
geography, law, philosophy.
(key, group, title, desc, points, requirements, standards, citations, demo_kind, src)
"""

ENTRIES_C = [
# ============================== PSYCHOLOGY ==============================
("cognitive-psych", "Cognitive",
 "Cognitive Psychology: Memory and Attention",
 "Cognitive psychology studies mental processes: how we perceive, attend, remember, and decide. "
 "Sensory memory holds raw input briefly; working memory — about four chunks — manipulates it; long-term "
 "memory stores it through encoding, with retrieval depending on cues and context. Attention selects: "
 "focused, divided, and the famous inattentional blindness that misses the obvious when attention is "
 "elsewhere. Spacing, testing, and elaboration strengthen memory far more than rereading — findings with "
 "direct classroom application. Educational information about established research.",
 ["Sensory, working, and long-term memory systems",
  "Encoding and retrieval as the two memory gates",
  "Attention selects; inattentional blindness demonstrates limits",
  "Spacing and testing beat rereading for retention",
  "Findings applied directly to learning"],
 "General reading level.",
 ["APA terminology"],
 "Standard psychology literature (cognitive textbooks). Educational content.",
 "psych", "public-harvest"),
("developmental-psych", "Developmental",
 "Developmental Psychology: Lifespan Stages",
 "Developmental psychology charts human change from womb to old age. Piaget described children's thinking in "
 "stages — sensorimotor, preoperational, concrete operational, formal operational — each with characteristic "
 "logic. Attachment theory (Bowlby, Ainsworth) shows early bonds shape later relationships. Erikson's eight "
 "psychosocial crises span trust versus mistrust in infancy to integrity versus despair in old age. "
 "Adolescence brings identity formation; adulthood brings generativity; aging brings selective optimization — "
 "focusing effort where it matters most. Development is lifelong, not finished at eighteen.",
 ["Piaget's stages of cognitive development",
  "Attachment theory: early bonds shape later relating",
  "Erikson's eight psychosocial crises",
  "Identity formation in adolescence",
  "Lifelong development including aging"],
 "General reading level.",
 ["APA terminology"],
 "Standard psychology literature (developmental textbooks). Educational content.",
 "psych", "public-harvest"),
("social-psych", "Social",
 "Social Psychology: Groups, Conformity, Persuasion",
 "Social psychology studies how people influence each other. Asch's line experiments showed majorities sway "
 "judgment; Milgram's obedience studies showed authority sways action — findings that sobered a generation. "
 "Cognitive dissonance: we adjust beliefs to match actions, not only the reverse. Persuasion runs on "
 "central routes (arguments) and peripheral routes (liking, authority, scarcity). Stereotypes and prejudice "
 "are studied as measurable social cognitions with real consequences. The field's lesson: situations shape "
 "behavior far more than observers expect — the fundamental attribution error.",
 ["Conformity: majorities sway judgment (Asch)",
  "Obedience to authority shapes action (Milgram)",
  "Cognitive dissonance aligns beliefs with actions",
  "Persuasion: central and peripheral routes",
  "Situations shape behavior more than expected"],
 "General reading level.",
 ["APA terminology"],
 "Standard psychology literature (social psychology textbooks). Educational content.",
 "psych", "public-harvest"),
("personality", "Personality",
 "Personality: Traits and Theories",
 "Personality psychology asks what makes individuals stably different. The Big Five — openness, "
 "conscientiousness, extraversion, agreeableness, neuroticism — emerged from factor-analyzing trait words "
 "across languages and predicts outcomes from job performance to health. Freud proposed unconscious drives "
 "and psychosexual stages; humanists like Rogers emphasized self-actualization; behaviorists pointed to "
 "reinforcement histories. Twin studies partition variance into genes, shared environment, and the "
 "non-shared environment that makes siblings different. Traits describe tendencies, not destinies.",
 ["Big Five: the dominant trait taxonomy",
  "Traits predict life outcomes statistically",
  "Freud, humanists, behaviorists: competing theories",
  "Twin studies partition genetic and environmental variance",
  "Traits as tendencies, not destinies"],
 "General reading level.",
 ["APA terminology"],
 "Standard psychology literature (personality textbooks). Educational content.",
 "psych", "public-harvest"),
("abnormal-psych", "Clinical",
 "Abnormal Psychology: A Clinical Overview",
 "Abnormal psychology studies psychological disorders — patterns of thought, emotion, and behavior causing "
 "distress or impairment. The DSM-5-TR classifies disorders by symptom clusters: depressive, anxiety, "
 "trauma-related, psychotic, neurodevelopmental, personality disorders among them. The diathesis-stress "
 "model: vulnerability plus stressors produces disorder. Treatments include psychotherapy (CBT's strong "
 "evidence base), medication, and their combination. Stigma remains a barrier to care; disorders are health "
 "conditions, not character flaws. Educational information — not diagnosis, and not a substitute for "
 "professional evaluation.",
 ["Disorders as distressing, impairing patterns",
  "DSM-5-TR classification by symptom clusters",
  "Diathesis-stress: vulnerability plus stressors",
  "Psychotherapy and medication as treatments",
  "Health conditions, not character flaws"],
 "General reading level.",
 ["APA terminology; DSM-5-TR classification"],
 "Standard psychology literature (clinical textbooks). Educational content; not clinical advice.",
 "psych", "public-harvest"),
("behavioral-psych", "Behavioral",
 "Behavioral Psychology: Conditioning and Learning",
 "Behavioral psychology studies learning as observable change. Classical conditioning (Pavlov) pairs stimuli "
 "so neutral cues trigger responses — the bell that summons salivation. Operant conditioning (Skinner) "
 "shapes behavior by consequences: reinforcement strengthens, punishment weakens, with schedules of "
 "reinforcement controlling persistence — variable-ratio schedules, as in slot machines, resist extinction "
 "most. Observational learning (Bandura) adds imitation to the picture. Applied behavior analysis uses "
 "these principles in education and therapy with measurable results.",
 ["Classical conditioning: stimulus pairing",
  "Operant conditioning: consequences shape behavior",
  "Reinforcement schedules control persistence",
  "Observational learning through imitation",
  "Applied behavior analysis in education and therapy"],
 "General reading level.",
 ["APA terminology"],
 "Standard psychology literature (behavioral textbooks). Educational content.",
 "psych", "public-harvest"),
("biological-psych", "Biological",
 "Biological Psychology: Brain and Behavior",
 "Biological psychology links mind to nervous system. The neuron — dendrites, axon, synapses — fires "
 "action potentials and communicates chemically across synapses; neurotransmitters like dopamine, serotonin, "
 "and glutamate modulate mood, reward, and excitation. The brain's lobes specialize: frontal for planning, "
 "temporal for memory and language, parietal for space, occipital for vision. Split-brain and lesion studies "
 "map function to structure. Hormones and the endocrine system broadcast slower, body-wide signals. Genes "
 "build the brain; experience wires it.",
 ["Neurons: action potentials and synaptic chemistry",
  "Key neurotransmitters and their roles",
  "Lobes specialize: frontal, temporal, parietal, occipital",
  "Lesion and imaging studies map function",
  "Genes build; experience wires"],
 "Basic biology intuition helpful.",
 ["APA terminology"],
 "Standard psychology literature (biopsychology textbooks). Educational content.",
 "psych", "public-harvest"),
("psych-methods", "Methods",
 "Research Methods in Psychology",
 "Psychology's credibility rests on method. Experiments manipulate an independent variable and randomly "
 "assign participants, isolating cause from correlation — the gold standard for causal claims. Correlational "
 "studies measure association without manipulation; surveys and naturalistic observation describe. "
 "Operational definitions turn constructs like 'anxiety' into measurable procedures. Replication — "
 "independent teams reproducing results — separates robust findings from flukes, and the field's recent "
 "replication reckoning strengthened its standards. Ethics boards, informed consent, and debriefing protect "
 "participants. Statistics translate data into warranted conclusions.",
 ["Experiments isolate cause via manipulation and random assignment",
  "Correlation measures association without causation",
  "Operational definitions make constructs measurable",
  "Replication separates robust findings from flukes",
  "Ethics boards and consent protect participants"],
 "Basic statistics intuition helpful.",
 ["APA publication standards"],
 "Standard psychology literature (methods textbooks). Educational content.",
 "psych", "public-harvest"),
("sig-cognitive-pattern", "Signature Psychology",
 "Signature Cognitive Pattern Engine",
 "A Signature original instrument that models cognitive workflows as deterministic Signature patterns: "
 "attention allocation as a scheduled resource, memory encoding as staged records (sensory, working, "
 "long-term), retrieval as cue-matched lookup. Study schedules are generated from spacing principles as "
 "reproducible plans. The engine is an educational instrument for understanding established cognitive "
 "findings — it implements the science as transparent machinery, never as clinical assessment.",
 ["Attention as a scheduled resource",
  "Memory stages as explicit records",
  "Retrieval as cue-matched lookup",
  "Spacing-based study plans, reproducibly generated",
  "Educational instrument; never clinical assessment"],
 "Cognitive psychology basics.",
 ["Signature system conventions"],
 "Original Signature design; findings per standard psychology literature.",
 "psych", "signature"),
("sig-behavior-mapper", "Signature Psychology",
 "Signature Behavior Mapper",
 "A Signature original instrument that charts behavior-change plans as deterministic Signature maps: target "
 "behaviors defined operationally, antecedents and consequences logged as structured records, reinforcement "
 "schedules specified exactly. Progress is measured against baseline with reproducible charts. Built strictly "
 "as an educational planning instrument applying established behavioral principles — it coaches nothing "
 "clinical and diagnoses nothing.",
 ["Behaviors defined operationally",
  "Antecedents and consequences as structured records",
  "Reinforcement schedules specified exactly",
  "Baseline-to-progress charts, reproducible",
  "Educational planning instrument only"],
 "Behavioral psychology basics.",
 ["Signature system conventions"],
 "Original Signature design; principles per standard psychology literature.",
 "psych", "signature"),
("sig-learning-optimizer", "Signature Psychology",
 "Signature Learning Optimizer",
 "A Signature original engine that builds study plans from the established science of learning: spaced "
 "repetition intervals computed deterministically, interleaving scheduled by rule, retrieval practice "
 "placed before review. The learner's stated material becomes a Signature curriculum record; the engine "
 "outputs a day-by-day plan that is fully reproducible and openly reasoned. A Signature treatment of "
 "learning science as transparent scheduling machinery.",
 ["Spaced intervals computed deterministically",
  "Interleaving and retrieval practice by rule",
  "Curriculum as an explicit record",
  "Day-by-day plans, fully reproducible",
  "Learning science as transparent machinery"],
 "Cognitive psychology basics.",
 ["Signature system conventions"],
 "Original Signature design; findings per standard psychology literature.",
 "psych", "signature"),
("sig-mind-metrics", "Signature Psychology",
 "Signature Mind Metrics",
 "A Signature original framework that tracks self-reported wellness indicators — sleep hours, activity, "
 "mood ratings, focus sessions — as deterministic personal records with transparent aggregation: weekly "
 "averages, trend slopes, correlations computed reproducibly. The framework labels itself a self-tracking "
 "instrument, never a diagnostic one, and keeps all data local to the record. A Signature treatment of "
 "personal metrics as honest, reproducible arithmetic.",
 ["Self-reported indicators as personal records",
  "Transparent aggregation: averages, trends, correlations",
  "Self-tracking instrument; never diagnostic",
  "Data local to the record",
  "Honest reproducible arithmetic"],
 "Basic arithmetic.",
 ["Signature system conventions"],
 "Original Signature design. Educational content; not clinical advice.",
 "psych", "signature"),
# ============================== HISTORY ==============================
("ancient-mesopotamia-egypt", "Ancient",
 "Ancient Civilizations: Mesopotamia and Egypt",
 "Civilization began in Mesopotamia — 'the land between the rivers' Tigris and Euphrates — where irrigation "
 "agriculture supported cities like Uruk by 4000 BCE. Writing emerged there as cuneiform, pressed into clay; "
 "law was codified in Hammurabi's stele. Along the Nile, Egypt unified under pharaohs around 3100 BCE, "
 "building pyramids as royal tombs and developing hieroglyphic writing, a 365-day calendar, and monumental "
 "engineering. Both societies show the pattern: surplus food, specialized labor, writing, law, and "
 "monumental architecture — the civilization package.",
 ["Mesopotamia: cities, cuneiform, codified law",
  "Egypt: unified kingdom, pyramids, hieroglyphs",
  "Irrigation agriculture enabled the surplus",
  "Writing emerged for administration",
  "The civilization package: cities, labor, law, monuments"],
 "General reading level.",
 ["Standard historical conventions (BCE/CE)"],
 "Standard history literature (ancient history references).",
 "hist", "public-harvest"),
("classical-antiquity", "Ancient",
 "Classical Antiquity: Greece and Rome",
 "Classical Greece gave the West philosophy (Socrates, Plato, Aristotle), democracy in Athens, drama, and "
 "the Olympic games — while warring city-states eventually fell to Macedon and then Rome. Rome built an "
 "empire on law, engineering, and military organization: aqueducts, roads, concrete, and a legal tradition "
 "that still underpins civil-law systems. The Republic's institutions — senate, consuls, assemblies — "
 "informed later republics; the Empire's fall in the West (476 CE) closed antiquity. Greek and Latin remain "
 "embedded in science, law, and language today.",
 ["Greece: philosophy, democracy, drama, city-states",
  "Rome: law, engineering, military organization",
  "Republican institutions informed later republics",
  "476 CE: conventional close of western antiquity",
  "Classical legacy in language, law, science"],
 "General reading level.",
 ["Standard historical conventions (BCE/CE)"],
 "Standard history literature (classical references).",
 "hist", "public-harvest"),
("middle-ages", "Medieval",
 "The Middle Ages: 500-1500",
 "The medieval millennium runs from Rome's fall to the Renaissance. In Europe, feudalism organized land and "
 "loyalty; the Church provided institutional continuity; monasteries preserved texts; universities emerged at "
 "Bologna, Paris, Oxford. Byzantium carried Roman administration east for another thousand years. The "
 "Islamic Golden Age (8th-13th centuries) advanced mathematics, medicine, and astronomy while preserving "
 "Greek works. The Crusades, the Black Death (1347-1351, killing a third of Europe), and the Hundred Years' "
 "War reshaped the continent before print and exploration ended the era.",
 ["Feudalism, Church, monasteries, universities in Europe",
  "Byzantium continued Roman administration east",
  "Islamic Golden Age advanced science and preserved texts",
  "Black Death reshaped demography and labor",
  "Crusades and Hundred Years' War as era-shaping conflicts"],
 "General reading level.",
 ["Standard historical conventions (BCE/CE)"],
 "Standard history literature (medieval references).",
 "hist", "public-harvest"),
("renaissance-reformation", "Early Modern",
 "The Renaissance and Reformation",
 "The Renaissance — 'rebirth' — revived classical learning in 14th-16th century Italy and spread through "
 "Europe: perspective in art (Brunelleschi, Leonardo, Michelangelo), humanist scholarship, and the printing "
 "press (Gutenberg, c. 1440) that multiplied books. The Reformation followed: Luther's 95 Theses (1517) "
 "challenged indulgences and papal authority, Calvin systematized Protestant theology, Henry VIII broke "
 "England's church from Rome. The result — religious wars, the Counter-Reformation, and eventually "
 "toleration — reshaped European politics, education, and the relationship of church and state.",
 ["Classical revival in art, scholarship, architecture",
  "Printing press multiplied books and ideas",
  "Luther 1517: the Reformation's spark",
  "Religious wars and the Counter-Reformation",
  "Reshaped church-state relations permanently"],
 "General reading level.",
 ["Standard historical conventions (BCE/CE)"],
 "Standard history literature (early modern references).",
 "hist", "public-harvest"),
("age-of-exploration", "Early Modern",
 "The Age of Exploration",
 "From the 15th century, European powers sailed beyond known waters: Portuguese caravels down Africa and to "
 "India (da Gama, 1498), Columbus's 1492 Atlantic crossing under Spanish flag, Magellan's expedition "
 "circling the globe (1519-1522). The Columbian Exchange moved crops, animals, diseases, and peoples "
 "between hemispheres — with catastrophic demographic collapse among Indigenous Americans from Old World "
 "disease. Colonization, the transatlantic slave trade, and global silver flows followed. Navigation "
 "advances — compass, astrolabe, cartography — made it possible; competition for trade made it profitable.",
 ["Portuguese, Spanish voyages opened ocean routes",
  "Columbian Exchange moved biota between hemispheres",
  "Disease caused catastrophic Indigenous demographic loss",
  "Colonization and the slave trade followed",
  "Navigation advances enabled; trade competition drove"],
 "General reading level.",
 ["Standard historical conventions (BCE/CE)"],
 "Standard history literature (exploration references).",
 "hist", "public-harvest"),
("industrial-revolution", "Modern",
 "The Industrial Revolution",
 "Beginning in late-18th-century Britain, the Industrial Revolution mechanized production: Watt's improved "
 "steam engine, coke-smelted iron, the spinning jenny and power loom, then railways and steamships. "
 "Factories concentrated labor in growing cities; output per worker soared while working conditions — long "
 "hours, child labor, pollution — provoked reform movements and labor organization. The second wave "
 "(electricity, chemicals, steel) spread industrialization to Germany, the United States, and Japan. "
 "Productivity's rise lifted living standards unevenly and permanently altered work, cities, and the "
 "environment.",
 ["Steam, iron, textiles: the first wave in Britain",
  "Factories concentrated labor; cities grew",
  "Productivity soared; conditions provoked reform",
  "Second wave: electricity, chemicals, steel",
  "Permanently altered work, cities, environment"],
 "General reading level.",
 ["Standard historical conventions (BCE/CE)"],
 "Standard history literature (industrial references).",
 "hist", "public-harvest"),
("world-wars", "Modern",
 "The World Wars: 1914-1945",
 "World War I (1914-1918) began with the assassination in Sarajevo and consumed a generation in trench "
 "warfare; its settlement redrew maps and planted grievances. The interwar years saw depression and the "
 "rise of fascism. World War II (1939-1945) — Nazi Germany's invasions, Japan's Pacific war, the Holocaust's "
 "industrialized murder of six million Jews and millions of others — ended with Germany's defeat and atomic "
 "bombs over Hiroshima and Nagasaki. The United Nations, the Cold War blocs, and the nuclear age emerged "
 "from the rubble. Presented factually as established historical record.",
 ["WWI: Sarajevo spark, trench stalemate, map-redrawing settlement",
  "Interwar depression and the rise of fascism",
  "WWII: global theaters 1939-1945",
  "The Holocaust: established historical record",
  "Aftermath: UN, Cold War blocs, nuclear age"],
 "General reading level.",
 ["Standard historical conventions (BCE/CE)"],
 "Standard history literature (20th-century references). Factual scholarly tone.",
 "hist", "public-harvest"),
("cold-war-decolonization", "Contemporary",
 "The Cold War and Decolonization",
 "From 1945 to 1991, the United States and Soviet Union competed globally short of direct war: NATO versus "
 "the Warsaw Pact, proxy conflicts in Korea and Vietnam, the Cuban Missile Crisis (1962) bringing the world "
 "closest to nuclear war, and a space race that put humans on the Moon. Simultaneously, European empires "
 "dissolved: India (1947), dozens of African nations around 1960, as anti-colonial movements won "
 "independence. The Cold War ended with the Soviet Union's dissolution in 1991, leaving a unipolar moment "
 "that reshaped globalization.",
 ["Bipolar competition without direct superpower war",
  "Proxy wars, missile crisis, space race",
  "Decolonization: India 1947, Africa ~1960",
  "Anti-colonial movements won independence",
  "1991: Soviet dissolution ended the era"],
 "General reading level.",
 ["Standard historical conventions (BCE/CE)"],
 "Standard history literature (contemporary references).",
 "hist", "public-harvest"),
("sig-timeline-engine", "Signature History",
 "Signature Timeline Engine",
 "A Signature original engine that renders historical chronology as deterministic Signature timelines: "
 "events as dated records with stated precision (year, month, day — or century where sources allow no "
 "better), durations as measured spans, eras as bounded regions. The engine computes overlaps, gaps, and "
 "sequences exactly, and flags anachronisms where dates contradict. Every event carries its dating basis "
 "openly. A Signature treatment of chronology as computable, checkable structure.",
 ["Events as dated records with stated precision",
  "Durations as measured spans; eras as bounded regions",
  "Overlaps, gaps, sequences computed exactly",
  "Anachronisms flagged where dates contradict",
  "Dating basis carried openly per event"],
 "General reading level.",
 ["Signature system conventions; BCE/CE dating"],
 "Original Signature design; dates per standard historical references.",
 "hist", "signature"),
("sig-civilization-mapper", "Signature History",
 "Signature Civilization Mapper",
 "A Signature original instrument that maps civilizations as structured Signature records: territory over "
 "time, institutions, technologies, writing systems, and trade links carried as comparable fields. Rise "
 "and fall become readable trajectories rather than vague narratives; cross-civilization comparison runs "
 "on identical fields. The mapper keeps interpretation separate from attested fact, labeling each. A "
 "Signature treatment of comparative history as structured, comparable records.",
 ["Civilizations as structured comparable records",
  "Territory, institutions, technology as fields",
  "Trajectories readable; comparisons on identical fields",
  "Attested fact separated from interpretation",
  "Comparative history as structured records"],
 "Ancient history basics helpful.",
 ["Signature system conventions; BCE/CE dating"],
 "Original Signature design; facts per standard historical references.",
 "hist", "signature"),
("sig-cause-effect", "Signature History",
 "Signature Cause-and-Effect Analyzer",
 "A Signature original framework that diagrams historical causation as explicit networks: events as nodes, "
 "proposed causes as edges labeled with evidence strength and source basis. Competing explanations become "
 "comparable graphs; the analyzer flags single-cause simplifications where the evidence supports multiple "
 "contributing factors. Counterfactuals are labeled as such, never as fact. A Signature treatment of "
 "historical explanation as inspectable causal structure.",
 ["Causation as explicit labeled networks",
  "Edges carry evidence strength and basis",
  "Competing explanations as comparable graphs",
  "Multi-causality flagged against simplifications",
  "Counterfactuals labeled, never presented as fact"],
 "General reading level.",
 ["Signature system conventions"],
 "Original Signature design; method per standard historiography.",
 "hist", "signature"),
("sig-archive-harmonizer", "Signature History",
 "Signature Archive Harmonizer",
 "A Signature original instrument that organizes historical source material as a harmonized Signature "
 "archive: documents, artifacts, and records cataloged with provenance, date, and reliability notes. "
 "Duplicate and derivative sources are linked, not duplicated; contradictions between sources are surfaced "
 "side by side with their provenance. The harmonizer never invents sources — every record traces to an "
 "attested item. A Signature treatment of source criticism as working archival machinery.",
 ["Sources cataloged with provenance and reliability",
  "Derivatives linked, not duplicated",
  "Contradictions surfaced with provenance",
  "Every record traces to an attested item",
  "Source criticism as archival machinery"],
 "General reading level.",
 ["Signature system conventions"],
 "Original Signature design; method per standard historiography.",
 "hist", "signature"),
# ============================== GEOGRAPHY ==============================
("physical-geography", "Physical",
 "Physical Geography: Landforms and Processes",
 "Physical geography studies Earth's surface features and the processes shaping them. Tectonic forces build "
 "mountains and rift valleys; weathering breaks rock down; erosion by water, wind, and ice sculpts it into "
 "valleys, dunes, and coastlines; deposition rebuilds it as deltas and beaches. Glaciers carve U-shaped "
 "valleys and leave moraines; rivers grade their profiles toward base level; mass wasting moves slopes "
 "downhill in slides and creeps. Landforms are temporary truces between construction and destruction.",
 ["Tectonics builds; weathering breaks down",
  "Erosion sculpts; deposition rebuilds",
  "Glaciers carve valleys and leave moraines",
  "Rivers grade toward base level",
  "Landforms as truces between forces"],
 "Basic earth-science intuition.",
 ["Standard geographical terminology"],
 "Standard geography literature (physical geography textbooks).",
 "geo", "public-harvest"),
("cartography", "Physical",
 "Cartography: Maps, Scale, and Projections",
 "Cartography is the science of representing a round Earth on flat surfaces. Scale relates map distance to "
 "ground distance — large-scale maps show small areas in detail. No projection preserves everything: "
 "Mercator keeps direction true for navigation but inflates polar areas; equal-area projections preserve "
 "size at the cost of shape; compromise projections balance distortions. Thematic maps layer data — "
 "population, rainfall, election results — onto geography. Modern GIS digitized it all: every feature a "
 "geometry with attributes, every analysis a spatial query.",
 ["Scale: map distance to ground distance",
  "No projection preserves everything",
  "Mercator: direction true, areas distorted",
  "Thematic maps layer data onto geography",
  "GIS: features as geometry with attributes"],
 "Basic geometry intuition.",
 ["Standard cartographic conventions"],
 "Standard geography literature (cartography references).",
 "geo", "public-harvest"),
("climate-zones", "Physical",
 "Climate Zones of the World",
 "Climate zones classify Earth's long-term weather patterns. The Koppen system leads: tropical (A) — "
 "rainforest Af, monsoon Am, savanna Aw; arid (B) — desert BW, steppe BS; temperate (C) — Mediterranean Cs, "
 "humid subtropical Cfa; continental (D) with severe winters; polar (E) — tundra ET, ice cap EF. Latitude "
 "sets the template; altitude, continentality, and ocean currents modify it. Zones shift with climate "
 "change, and their boundaries are among the most-watched indicators in environmental monitoring.",
 ["Koppen A-E: tropical, arid, temperate, continental, polar",
  "Latitude sets the template",
  "Altitude and currents modify zones",
  "Mediterranean, monsoon, tundra as named subtypes",
  "Shifting boundaries as change indicators"],
 "Climate basics.",
 ["WMO/Koppen conventions"],
 "Standard geography literature (climatology references).",
 "geo", "public-harvest"),
("human-geography", "Human",
 "Human Geography: Population and Migration",
 "Human geography studies people across space. The demographic transition model traces societies from high "
 "birth and death rates through falling mortality to low fertility — the path most of the world is walking. "
 "Population pyramids reveal age structure at a glance: expansive, constrictive, stationary. Migration — "
 "voluntary and forced — redistributes people toward opportunity and away from danger; push and pull factors "
 "explain the flows. Urbanization concentrates humanity: over half the world now lives in cities, a share "
 "still rising. Carrying capacity debates ask how many the planet can support, and how.",
 ["Demographic transition: the common pathway",
  "Population pyramids reveal age structure",
  "Push and pull factors explain migration",
  "Urbanization: majority-urban world and rising",
  "Carrying capacity as open debate"],
 "Basic statistics intuition helpful.",
 ["UN demographic terminology"],
 "Standard geography literature (human geography textbooks).",
 "geo", "public-harvest"),
("urban-geography", "Human",
 "Urban Geography: The Growth of Cities",
 "Urban geography explains why cities locate, grow, and organize as they do. Site and situation — the "
 "physical spot and its regional connections — decide origins: river crossings, harbors, resource nodes. "
 "Models describe internal structure: concentric zones, sectors, multiple nuclei. Agglomeration economies "
 "explain clustering — firms benefit from proximity to suppliers, workers, and ideas. Suburbanization, "
 "gentrification, and informal settlements describe the modern dynamics. Megacities over ten million, "
 "mostly in the developing world, are the 21st century's dominant human habitat.",
 ["Site and situation decide city origins",
  "Concentric, sector, multi-nuclei structure models",
  "Agglomeration economies explain clustering",
  "Suburbanization and gentrification dynamics",
  "Megacities as the century's dominant habitat"],
 "Human geography basics helpful.",
 ["Standard geographical terminology"],
 "Standard geography literature (urban geography references).",
 "geo", "public-harvest"),
("economic-geography", "Human",
 "Economic Geography: Resources and Trade",
 "Economic geography maps production across space. Von Thunen's rings predicted land use around markets by "
 "transport cost — still visible in modern form. Weber located industry by minimizing transport and labor "
 "costs. Resource endowments shape specialization: oil states, manufacturing belts, financial centers. "
 "Global value chains split production across continents — designed in one country, assembled in another, "
 "sold everywhere. Special economic zones and trade corridors are policy tools for reshaping the map. "
 "Distance still matters, but its price keeps falling.",
 ["Land use organized by transport cost",
  "Industry located by cost minimization",
  "Endowments shape regional specialization",
  "Global value chains split production spatially",
  "Policy tools: zones and corridors"],
 "Economics basics helpful.",
 ["Standard economic-geography terminology"],
 "Standard geography literature (economic geography references).",
 "geo", "public-harvest"),
("political-geography", "Human",
 "Political Geography: Borders and Territory",
 "Political geography studies power inscribed on territory. States claim exclusive sovereignty within "
 "borders — lines that are negotiated, fought over, and sometimes arbitrary, as colonial straight-line "
 "borders in Africa show. Geopolitics analyzes how geography shapes strategy: Mackinder's Heartland theory, "
 "chokepoints like Hormuz and Malacca, exclusive economic zones at sea. Federal versus unitary systems "
 "divide power differently across the same territory. Electoral geography maps votes to districts, where "
 "gerrymandering shows boundaries themselves are political instruments.",
 ["Borders: negotiated, fought, sometimes arbitrary",
  "Sovereignty as exclusive territorial claim",
  "Chokepoints and EEZs in geopolitics",
  "Federal versus unitary power division",
  "Electoral boundaries as political instruments"],
 "General reading level.",
 ["UN terminology"],
 "Standard geography literature (political geography references).",
 "geo", "public-harvest"),
("biogeography", "Physical",
 "Biogeography: Biomes and Biodiversity",
 "Biogeography explains where life lives. Biomes — tundra, taiga, temperate forest, grassland, desert, "
 "tropical rainforest — are large life zones set by climate, each with characteristic vegetation and fauna. "
 "Latitude and altitude stack them predictably: climb a tropical mountain and you pass through the world's "
 "biomes. Island biogeography (MacArthur and Wilson) predicts species counts from island size and isolation. "
 "Biodiversity hotspots — small areas holding huge fractions of species — focus conservation where it counts "
 "most. Endemism marks species found nowhere else.",
 ["Biomes as climate-set life zones",
  "Altitude mirrors latitude in biome stacking",
  "Island biogeography: size and isolation predict richness",
  "Hotspots focus conservation efficiently",
  "Endemism: found nowhere else"],
 "Biology basics helpful.",
 ["Standard biogeographical terminology"],
 "Standard geography literature (biogeography references).",
 "geo", "public-harvest"),
("sig-map-geometry", "Signature Geography",
 "Signature Map Geometry",
 "A Signature original treatment that renders maps as exact geometric records: projections computed "
 "deterministically with distortion quantified at every point, scale carried as a verifiable property, "
 "features as precise geometries with attributes. Overlay operations — intersection, buffering, "
 "containment — execute as provable geometric computations. A Signature treatment of cartography where "
 "every map is a checkable geometric document.",
 ["Projections computed with quantified distortion",
  "Scale as a verifiable property",
  "Features as precise attributed geometries",
  "Overlays as provable geometric operations",
  "Maps as checkable geometric documents"],
 "Cartography basics.",
 ["Signature system conventions"],
 "Original Signature design; classical facts per standard geography literature.",
 "geo", "signature"),
("sig-population-mapper", "Signature Geography",
 "Signature Population Mapper",
 "A Signature original instrument that renders population data as deterministic geographic records: "
 "densities computed from stated counts and areas, pyramids drawn from age-sex tables, change rates from "
 "time series — all reproducible from the same inputs. The mapper works on public aggregate statistics and "
 "labels every figure with source and period. A Signature treatment of demographic numbers as transparent, "
 "auditable map records.",
 ["Densities from stated counts and areas",
  "Pyramids from age-sex tables",
  "Change rates from time series",
  "Aggregate statistics with source labels",
  "Transparent auditable demographic records"],
 "Basic statistics intuition.",
 ["Signature system conventions"],
 "Original Signature design; methods per standard demographic literature.",
 "geo", "signature"),
("sig-terrain-classifier", "Signature Geography",
 "Signature Terrain Classifier",
 "A Signature original engine that classifies landforms deterministically from elevation geometry: slopes, "
 "curvatures, and drainage patterns computed exactly, landform types assigned by stated rule sets — never "
 "by opaque judgment. Every classification carries the rules and thresholds that produced it, so any result "
 "can be audited and reproduced. A Signature treatment of geomorphometry as transparent rule-based "
 "classification.",
 ["Landforms from exact elevation geometry",
  "Slope, curvature, drainage as computed features",
  "Classification by stated rule sets",
  "Rules and thresholds carried with results",
  "Auditable reproducible classification"],
 "Physical geography basics.",
 ["Signature system conventions"],
 "Original Signature design; classical facts per standard geography literature.",
 "geo", "signature"),
("sig-route-optimizer", "Signature Geography",
 "Signature Route Optimizer",
 "A Signature original engine that solves routing as deterministic network optimization: road and path "
 "networks as weighted graphs, shortest paths by verified algorithms, multi-stop tours by stated "
 "heuristics with their approximation bounds declared. Every route carries its total cost and the method "
 "that found it. A Signature treatment of navigation where the path is provably the computed answer, "
 "not a black-box suggestion.",
 ["Networks as weighted graphs",
  "Shortest paths by verified algorithms",
  "Multi-stop tours with declared bounds",
  "Routes carry cost and method",
  "Provably computed paths"],
 "Basic graph intuition helpful.",
 ["Signature system conventions"],
 "Original Signature design; algorithms per standard CS literature.",
 "geo", "signature"),
# ============================== LAW ==============================
("constitutional-law", "Public Law",
 "Constitutional Law: Structure and Rights",
 "Constitutional law studies the supreme law's allocation of power and protection of rights. In the U.S. "
 "system: enumerated federal powers, reserved state powers, separation into legislative, executive, and "
 "judicial branches with checks and balances, and judicial review (Marbury v. Madison, 1803) letting courts "
 "void unconstitutional acts. Rights provisions — speech, religion, due process, equal protection — bind "
 "government action and are interpreted through centuries of precedent. Amendment is deliberately difficult, "
 "making the text both stable and contested. Educational reference — not legal advice.",
 ["Enumerated powers and federalism",
  "Separation of powers with checks and balances",
  "Judicial review of government acts",
  "Rights provisions bind government action",
  "Precedent interprets the text over time"],
 "General reading level.",
 ["Standard legal citation (Bluebook style concepts)"],
 "Standard legal literature (constitutional references). Educational content; not legal advice.",
 "law", "public-harvest"),
("criminal-law", "Criminal",
 "Criminal Law: Elements of a Crime",
 "Criminal law punishes conduct the state forbids. Most crimes require actus reus — a voluntary act (or "
 "omission where duty exists) — plus mens rea, the culpable mental state: purpose, knowledge, recklessness, "
 "or negligence, graded by blameworthiness. Causation and concurrence link mind to act to result. Defenses — "
 "self-defense, necessity, insanity, mistake — negate liability even when elements are met. Procedure "
 "protects the accused: presumption of innocence, proof beyond a reasonable doubt, the exclusionary rule. "
 "Educational reference — not legal advice.",
 ["Actus reus: the voluntary act",
  "Mens rea: purpose, knowledge, recklessness, negligence",
  "Causation and concurrence requirements",
  "Defenses negate liability",
  "Proof beyond a reasonable doubt"],
 "General reading level.",
 ["Standard legal citation concepts"],
 "Standard legal literature (criminal law references). Educational content; not legal advice.",
 "law", "public-harvest"),
("contract-law", "Civil",
 "Contract Law: Formation and Breach",
 "Contract law enforces voluntary exchanges. Formation needs offer, acceptance, and consideration — "
 "bargained-for exchange — with mutual assent on definite terms. Defenses to formation include incapacity, "
 "duress, fraud, and mistake. Breach — failure to perform without excuse — yields remedies: expectation "
 "damages putting the victim where performance would have, plus restitution and, rarely, specific "
 "performance. Interpretation seeks the parties' intent; the parol evidence rule limits outside evidence. "
 "The UCC governs sale-of-goods contracts specially. Educational reference — not legal advice.",
 ["Offer, acceptance, consideration: formation's trio",
  "Mutual assent on definite terms",
  "Defenses: incapacity, duress, fraud, mistake",
  "Expectation damages as the standard remedy",
  "UCC for sale-of-goods contracts"],
 "General reading level.",
 ["Standard legal citation concepts"],
 "Standard legal literature (contract references). Educational content; not legal advice.",
 "law", "public-harvest"),
("tort-law", "Civil",
 "Tort Law: Negligence and Liability",
 "Tort law compensates civil wrongs. Negligence — the workhorse — needs duty, breach, causation, and "
 "damages: did the defendant owe care, fall below the reasonable-person standard, and thereby cause "
 "foreseeable harm? Strict liability applies without fault to abnormally dangerous activities and defective "
 "products. Intentional torts — battery, assault, false imprisonment, defamation — protect bodily and "
 "reputational integrity. Damages compensate loss and deter; comparative fault apportions when the victim "
 "contributed. Educational reference — not legal advice.",
 ["Negligence: duty, breach, causation, damages",
  "Reasonable-person standard of care",
  "Strict liability without fault",
  "Intentional torts protect person and reputation",
  "Comparative fault apportions shared blame"],
 "General reading level.",
 ["Standard legal citation concepts"],
 "Standard legal literature (tort references). Educational content; not legal advice.",
 "law", "public-harvest"),
("property-law", "Civil",
 "Property Law: Ownership and Transfer",
 "Property law allocates rights in things. The 'bundle of sticks' — possess, use, exclude, transfer, "
 "destroy — describes ownership's divisible rights. Estates in land range from fee simple absolute (full "
 "ownership) through life estates to leaseholds; future interests schedule what follows. Adverse possession "
 "can transfer title to long-term occupiers meeting strict elements. Recording statutes order competing "
 "claims to the same parcel. Intellectual property — patents, copyrights, trademarks — extends the bundle "
 "to intangibles with time-limited rights. Educational reference — not legal advice.",
 ["Ownership as a bundle of divisible rights",
  "Estates: fee simple, life estate, leasehold",
  "Adverse possession's strict elements",
  "Recording statutes order competing claims",
  "Intellectual property extends rights to intangibles"],
 "General reading level.",
 ["Standard legal citation concepts"],
 "Standard legal literature (property references). Educational content; not legal advice.",
 "law", "public-harvest"),
("administrative-law", "Public Law",
 "Administrative Law: Agencies and Regulation",
 "Administrative law governs the agencies that write most modern regulation. Legislatures delegate "
 "authority with an 'intelligible principle'; agencies then make rules through notice-and-comment "
 "rulemaking, adjudicate cases, and enforce. Judicial review checks agency action for statutory authority, "
 "procedural regularity, and reasoned decision-making — deference doctrines calibrate how hard courts "
 "look. Freedom-of-information and open-meetings laws keep the process visible. From environmental permits "
 "to broadcast licenses, daily life runs on administrative law. Educational reference — not legal advice.",
 ["Delegation with an intelligible principle",
  "Notice-and-comment rulemaking",
  "Agency adjudication and enforcement",
  "Judicial review for authority and reason",
  "Transparency laws keep process visible"],
 "Constitutional law basics helpful.",
 ["Standard legal citation concepts"],
 "Standard legal literature (administrative references). Educational content; not legal advice.",
 "law", "public-harvest"),
("international-law", "Public Law",
 "International Law: Treaties and Institutions",
 "International law governs relations between states without a world sovereign. Treaties — written "
 "agreements, codified by the Vienna Convention — bind consenting states; custom, general principles, and "
 "scholarly writings complete the sources. Institutions apply it: the International Court of Justice settles "
 "state disputes, the ICC prosecutes atrocity crimes, the WTO adjudicates trade. Sovereignty, non-intervention, "
 "and self-determination are the field's load-bearing principles. Enforcement runs through reciprocity, "
 "reputation, and collective action rather than a global police force. Educational reference.",
 ["Treaties bind consenting states",
  "Custom and general principles complete the sources",
  "ICJ, ICC, WTO as applying institutions",
  "Sovereignty and self-determination as core principles",
  "Enforcement via reciprocity and collective action"],
 "General reading level.",
 ["Standard legal citation concepts"],
 "Standard legal literature (international law references). Educational content.",
 "law", "public-harvest"),
("legal-research", "Practice",
 "Legal Research: Finding and Citing the Law",
 "Legal research finds controlling authority: constitutions, statutes, regulations, and cases — in that "
 "hierarchy. Secondary sources (treatises, restatements, law reviews) explain; primary sources bind. "
 "Shepardizing or KeyCiting verifies a case is still good law — overruled precedent cited as live is the "
 "classic malpractice trap. IRAC (Issue, Rule, Application, Conclusion) organizes analysis; the Bluebook "
 "standardizes citation so any lawyer can find any source. Research memos answer questions with "
 "authority-backed reasoning, not opinion. Educational reference — not legal advice.",
 ["Authority hierarchy: constitution, statute, regulation, case",
  "Secondary sources explain; primary sources bind",
  "Verify cases are still good law",
  "IRAC organizes legal analysis",
  "Bluebook citation as the finding standard"],
 "General reading level.",
 ["The Bluebook citation system"],
 "Standard legal literature (research references). Educational content; not legal advice.",
 "law", "public-harvest"),
("sig-case-geometry", "Signature Law",
 "Signature Case Geometry",
 "A Signature original instrument that diagrams legal arguments as geometric Signature records: issues as "
 "nodes, authorities as supporting structures, holdings as resolved regions. The strength of a position "
 "becomes readable — how many authorities support each element, where the gaps are. Designed strictly as an "
 "educational study instrument for understanding legal reasoning structure; it gives no legal advice and "
 "makes no predictions about real cases.",
 ["Arguments as geometric records",
  "Issues, authorities, holdings as structures",
  "Support strength readable geometrically",
  "Gaps in reasoning made visible",
  "Educational instrument; no legal advice"],
 "Basic legal concepts.",
 ["Signature system conventions"],
 "Original Signature design. Educational content; not legal advice.",
 "law", "signature"),
("sig-contract-analyzer", "Signature Law",
 "Signature Contract Analyzer",
 "A Signature original instrument that parses contract structure as deterministic Signature records: parties, "
 "obligations, conditions, terms, and dates extracted as labeled fields; missing standard clauses flagged "
 "against a stated checklist. Every finding cites the exact clause text it came from. Built as an "
 "educational instrument for understanding contract anatomy — it explains structure, never advises on real "
 "agreements.",
 ["Contracts as labeled structural records",
  "Parties, obligations, conditions, dates extracted",
  "Missing clauses flagged against checklists",
  "Every finding cites its clause text",
  "Educational instrument; never legal advice"],
 "Contract law basics.",
 ["Signature system conventions"],
 "Original Signature design. Educational content; not legal advice.",
 "law", "signature"),
("sig-deadline-engine", "Signature Law",
 "Signature Deadline Engine",
 "A Signature original engine that computes legal-style deadlines as deterministic records: calendar-day and "
 "business-day arithmetic, weekend and holiday handling by stated rule sets, chains of dependent deadlines "
 "resolved in order. Every computed date carries the rule that produced it, auditable end to end. Built as "
 "an educational instrument for deadline arithmetic — real deadlines depend on jurisdiction-specific rules "
 "and professional judgment, which the engine labels clearly.",
 ["Calendar-day and business-day arithmetic",
  "Holiday handling by stated rule sets",
  "Dependent deadline chains resolved in order",
  "Every date carries its producing rule",
  "Educational instrument with clear limits"],
 "Basic date arithmetic.",
 ["Signature system conventions"],
 "Original Signature design. Educational content; not legal advice.",
 "law", "signature"),
("sig-legal-research-mapper", "Signature Law",
 "Signature Legal Research Mapper",
 "A Signature original instrument that organizes legal research as navigable Signature maps: issues linked "
 "to candidate authorities, authorities linked to their jurisdiction and date, reasoning chains drawn as "
 "checkable paths. The mapper structures the research process — it does not supply real legal authorities "
 "or advice. A Signature treatment of legal study as organized, inspectable inquiry.",
 ["Research organized as navigable maps",
  "Issues linked to candidate authorities",
  "Jurisdiction and date carried per authority",
  "Reasoning chains as checkable paths",
  "Study instrument; no real authorities supplied"],
 "Legal research basics.",
 ["Signature system conventions"],
 "Original Signature design. Educational content; not legal advice.",
 "law", "signature"),
# ============================== PHILOSOPHY ==============================
("logic", "Logic",
 "Logic: Arguments, Validity, and Fallacies",
 "Logic studies good reasoning. An argument is valid when the conclusion must be true if the premises are — "
 "validity concerns form, not truth. Deductive forms: modus ponens, modus tollens, disjunctive syllogism. "
 "Inductive arguments generalize from samples; abductive arguments infer the best explanation. Fallacies "
 "are tempting bad forms: ad hominem attacks the person, straw man attacks a caricature, begging the "
 "question assumes the conclusion. Propositional and predicate logic formalize all of this in symbols, "
 "making validity mechanically checkable.",
 ["Validity: conclusion must follow if premises hold",
  "Deductive forms: modus ponens, tollens, syllogism",
  "Induction generalizes; abduction explains",
  "Fallacies: ad hominem, straw man, begging the question",
  "Formal logic makes validity mechanically checkable"],
 "General reading level.",
 ["Standard logical notation"],
 "Standard philosophy literature (logic textbooks).",
 "phil", "public-harvest"),
("ethics", "Ethics",
 "Ethics: Consequentialism, Duty, and Virtue",
 "Ethics asks how we should act. Consequentialism (utilitarianism: maximize overall well-being) judges acts "
 "by outcomes. Deontology (Kant: act on maxims all could universalize) judges by duty and principle, "
 "forbidding using people as mere means. Virtue ethics (Aristotle) asks what the flourishing person would "
 "do, cultivating character over rule-following. Applied ethics takes these frameworks to medicine, "
 "business, and technology. Metaethics asks the deeper question: are moral claims true, and if so, what "
 "makes them true? Presented as scholarly overview of established positions.",
 ["Consequentialism judges by outcomes",
  "Deontology judges by duty and principle",
  "Virtue ethics cultivates character",
  "Applied ethics takes frameworks to real domains",
  "Metaethics asks what moral truth would be"],
 "General reading level.",
 ["Standard philosophical terminology"],
 "Standard philosophy literature (ethics references). Scholarly overview.",
 "phil", "public-harvest"),
("metaphysics", "Metaphysics",
 "Metaphysics: Being, Cause, and Identity",
 "Metaphysics studies reality's basic structure. What exists — material things only, or also minds, numbers, "
 "universals? Causation: is it constant conjunction (Hume) or real powers in things? Identity over time: "
 "what makes you the same person as your childhood self — body, memory, psychology? Free will debates whether "
 "determinism leaves room for responsibility; compatibilists say yes, incompatibilists divide over "
 "libertarianism and hard determinism. Time itself is contested: presentism, eternalism, the growing block. "
 "Presented as scholarly overview of established positions.",
 ["What exists: the ontology question",
  "Causation: conjunction versus real powers",
  "Personal identity over time",
  "Free will and determinism debates",
  "The nature of time contested"],
 "General reading level.",
 ["Standard philosophical terminology"],
 "Standard philosophy literature (metaphysics references). Scholarly overview.",
 "phil", "public-harvest"),
("epistemology", "Epistemology",
 "Epistemology: Knowledge, Belief, Justification",
 "Epistemology studies knowledge: traditionally justified true belief, though Gettier's counterexamples "
 "showed the analysis incomplete. Internalists locate justification in the believer's perspective; "
 "externalists (reliabilism) in the belief-forming process's reliability. Skepticism challenges whether we "
 "know anything about the external world, other minds, or the future — Descartes' demon, brains in vats. "
 "Responses range from foundationalism's basic beliefs to coherentism's webs of mutual support. Social "
 "epistemology studies testimony, expertise, and disagreement. Presented as scholarly overview.",
 ["Knowledge as justified true belief, Gettier-complicated",
  "Internalism versus externalism about justification",
  "Skeptical challenges: external world, other minds",
  "Foundationalism versus coherentism",
  "Testimony and expertise in social epistemology"],
 "General reading level.",
 ["Standard philosophical terminology"],
 "Standard philosophy literature (epistemology references). Scholarly overview.",
 "phil", "public-harvest"),
("philosophy-of-mind", "Metaphysics",
 "Philosophy of Mind: Consciousness and the Brain",
 "Philosophy of mind asks how mind relates to matter. Dualism (Descartes) separates mental and physical "
 "substance; physicalism identifies mind with brain, in varieties from identity theory to functionalism "
 "(mental states as functional roles, multiply realizable). The hard problem (Chalmers): why does brain "
 "activity feel like anything — why qualia? Intentionality — thought's aboutness — resists easy physical "
 "reduction. Thought experiments (Mary's room, Chinese room, zombies) probe the theories' limits. "
 "Presented as scholarly overview of established positions.",
 ["Dualism versus physicalism",
  "Functionalism: mental states as roles",
  "The hard problem of consciousness",
  "Intentionality: thought's aboutness",
  "Thought experiments probe theory limits"],
 "General reading level.",
 ["Standard philosophical terminology"],
 "Standard philosophy literature (mind references). Scholarly overview.",
 "phil", "public-harvest"),
("aesthetics", "Value Theory",
 "Aesthetics: Beauty, Art, and Taste",
 "Aesthetics studies beauty, art, and aesthetic experience. What makes something art — intention, "
 "institution, history, or indefinable family resemblance? Beauty: objective property, subjective response, "
 "or relation between the two? Kant analyzed aesthetic judgment as disinterested pleasure claiming universal "
 "voice. The philosophy of music, literature, and visual art each ask what their medium distinctively does. "
 "Taste's variation across cultures raises relativism questions aesthetics still debates. Presented as "
 "scholarly overview of established positions.",
 ["What makes something art: competing definitions",
  "Beauty: objective, subjective, or relational",
  "Kant on disinterested aesthetic judgment",
  "Medium-specific philosophies of the arts",
  "Cultural variation and relativism debates"],
 "General reading level.",
 ["Standard philosophical terminology"],
 "Standard philosophy literature (aesthetics references). Scholarly overview.",
 "phil", "public-harvest"),
("political-philosophy", "Value Theory",
 "Political Philosophy: Justice and the State",
 "Political philosophy asks when state power is legitimate and what justice requires. Social contract "
 "theories (Hobbes, Locke, Rousseau) ground authority in agreement — hypothetical or historical. Rawls' veil "
 "of ignorance asks what principles we'd choose not knowing our place; Nozick answered with libertarian "
 "entitlements. Distributive justice debates equality, need, desert, and liberty as allocation principles. "
 "Democracy's justification, civil disobedience's limits, and global justice extend the questions beyond "
 "borders. Presented as scholarly overview of established positions.",
 ["Legitimacy of state power questioned",
  "Social contract theories ground authority",
  "Rawls' veil of ignorance; Nozick's libertarian reply",
  "Distributive principles: equality, need, desert, liberty",
  "Democracy, disobedience, global justice"],
 "General reading level.",
 ["Standard philosophical terminology"],
 "Standard philosophy literature (political philosophy references). Scholarly overview.",
 "phil", "public-harvest"),
("philosophy-of-science", "Epistemology",
 "Philosophy of Science: Explanation and Method",
 "Philosophy of science examines how science knows. The covering-law model made explanation deduction from "
 "laws; causal and mechanistic accounts succeeded it. Popper's falsifiability drew the science line at "
 "testability; Kuhn's paradigms showed revolutions restructure fields, with normal science between. "
 "Underdetermination: data never picks exactly one theory. Realism versus anti-realism debates whether "
 "successful theories describe unobservable reality. Values in science — which questions get asked and funded "
 "— complete the picture of science as a human practice. Presented as scholarly overview.",
 ["Explanation: covering-law, causal, mechanistic",
  "Falsifiability as the demarcation proposal",
  "Kuhn: paradigms and scientific revolutions",
  "Underdetermination of theory by data",
  "Realism debates and values in science"],
 "General reading level.",
 ["Standard philosophical terminology"],
 "Standard philosophy literature (philosophy of science references). Scholarly overview.",
 "phil", "public-harvest"),
("sig-argument-engine", "Signature Philosophy",
 "Signature Argument Engine",
 "A Signature original engine that renders philosophical arguments as deterministic Signature structures: "
 "premises as stated nodes, inference steps as labeled links, conclusions as derived records. Validity is "
 "checked mechanically where the argument is formalizable; informal arguments get their structure mapped "
 "with gaps flagged. Competing positions on the same question become comparable structures. A Signature "
 "treatment of reasoning as inspectable architecture — scholarly, never preaching.",
 ["Arguments as deterministic structures",
  "Premises, inferences, conclusions explicitly mapped",
  "Mechanical validity checking where formalizable",
  "Gaps flagged in informal arguments",
  "Competing positions as comparable structures"],
 "Logic basics.",
 ["Signature system conventions"],
 "Original Signature design; positions per standard philosophy literature. Scholarly.",
 "phil", "signature"),
("sig-ethics-mapper", "Signature Philosophy",
 "Signature Ethics Mapper",
 "A Signature original instrument that maps ethical questions as structured Signature records: the "
 "stakeholders, the candidate principles (consequentialist, deontological, virtue-based), and how each "
 "principle evaluates the options — laid out side by side. The mapper presents established ethical "
 "frameworks' analyses without endorsing any; it clarifies structure, never prescribes conclusions. A "
 "Signature treatment of moral reasoning as scholarly cartography.",
 ["Ethical questions as structured records",
  "Frameworks applied side by side",
  "Stakeholders and options made explicit",
  "Clarifies structure; prescribes nothing",
  "Scholarly cartography, never preaching"],
 "Ethics basics.",
 ["Signature system conventions"],
 "Original Signature design; frameworks per standard philosophy literature. Scholarly.",
 "phil", "signature"),
("sig-concept-geometry", "Signature Philosophy",
 "Signature Concept Geometry",
 "A Signature original design that gives philosophical concepts geometric form on a Signature lattice: "
 "related concepts as neighboring regions, distinctions as boundaries, category hierarchies as nested "
 "spaces. Classic problems — universals, identity, causation — become navigable conceptual terrain where "
 "each position's commitments are stated openly. A Signature treatment of conceptual analysis as "
 "explorable geometry, scholarly throughout.",
 ["Concepts as regions on a Signature lattice",
  "Distinctions as boundaries; hierarchies as nested spaces",
  "Classic problems as navigable terrain",
  "Positions' commitments stated openly",
  "Conceptual analysis as explorable geometry"],
 "Philosophy basics helpful.",
 ["Signature system conventions"],
 "Original Signature design; concepts per standard philosophy literature. Scholarly.",
 "phil", "signature"),
("sig-wisdom-archive", "Signature Philosophy",
 "Signature Wisdom Archive",
 "A Signature original archive that collects philosophical insights as structured Signature records: the "
 "question, the proposed insight, the tradition it comes from, the reasoning behind it — each labeled with "
 "its source tradition and presented scholarly. The archive organizes across traditions comparatively without "
 "syncretism or preaching: Stoic, Confucian, Buddhist, and Western insights stand in their own contexts, "
 "comparable but never flattened. A Signature treatment of the philosophical heritage as a navigable "
 "comparative record.",
 ["Insights as structured records with provenance",
  "Question, insight, tradition, reasoning per record",
  "Traditions kept in their own contexts",
  "Comparative without syncretism",
  "Scholarly throughout; never preaching"],
 "General reading level.",
 ["Signature system conventions"],
 "Original Signature design; content per standard philosophy literature. Scholarly.",
 "phil", "signature"),
]
