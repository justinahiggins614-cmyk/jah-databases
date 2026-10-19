#!/usr/bin/env python3
"""Entries for the Unsolved Microbiology databases (Manon's 16:15 orders, Unsolved Problems Solved batch).

34 famous unsolved microbial problems, ladder-ordered by accessibility (rank 1 = most
approachable, rank 34 = most complex). Public half: JAH-USMB- (real, fact-checked problems
as the world knows them). Signature half: JAH-USMBS- (same 34 problems through the
Signature lens; titles suffixed " (Signature Edition)", src signature, clearly labeled
Signature-made, never presented as authentic public record).

Field scope: the uncultured majority, the human microbiome's causal roles, viral dark
matter, antibiotic resistance evolution, the origin of eukaryotes, microbial contributions
to climate.

ID prefixes JAH-USMB- / JAH-USMBS- verified free 2026-10-17: zero hits in the manifest
id_prefix values and zero hits in every shard index file of jah-databases-data-1.

The Signature solution in every record opens with the EXACT label
"Signature-generated proposed solution - not established science."
Public halves carry a short pointer; signature halves carry the full treatment.
Honesty rule: no claims of proof, no implied peer acceptance, speculation never
presented as settled.

Never the words "bat belt" anywhere. No website references. No Facebook.
No religious talk. All records human-readable sentences/paragraphs.
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

SIG_TAIL = ("Signature original - his original Signature Method applied to microbiology: "
            "every unsolved microbial problem a covenant question, the solution explorer the "
            "Signature system's walkthrough, confirm-and-refute panels the oath of "
            "honesty. Clearly labeled Signature-made, never presented as established "
            "science or authentic public record.")

CIT_ANOMALY = ("Staley JT, Konopka A. Measurement of in situ activities of nonphotosynthetic "
               "microorganisms in aquatic and terrestrial habitats. Annu Rev Microbiol. "
               "1985;39:321-346; Amann RI et al. Phylogenetic identification and in situ detection "
               "of individual microbial cells without cultivation. Microbiol Rev. 1995;59:143-169.")
CIT_ALIVE = ("Koonin EV, Starokadomsky P. Are viruses alive? The replicator paradigm sheds "
             "decisive light on an old but misguided question. Stud Hist Philos Biol Biomed Sci. "
             "2016;59:125-134; Raoult D, Forterre P. Redefining viruses: lessons from Mimivirus. "
             "Nat Rev Microbiol. 2008;6:315-319.")
CIT_SPECIES = ("Rossello-Mora R, Amann R. The species concept for prokaryotes. FEMS Microbiol "
               "Rev. 2001;25:39-67; Achtman M, Wagner M. Microbial diversity and the genetic "
               "nature of microbial species. Nat Rev Microbiol. 2008;6:431-440.")
CIT_GUTCULT = ("Qin J et al. A human gut microbial gene catalogue established by metagenomic "
               "sequencing. Nature. 2010;464:59-65; Browne HP et al. Culturing of 'unculturable' "
               "human microbiota reveals novel taxa and extensive sporulation. Nature. "
               "2016;533:543-546.")
CIT_VBNC = ("Oliver JD. The viable but nonculturable state in bacteria. J Microbiol. "
            "2005;43:93-100; Pinto D et al. The viable but nonculturable state in clinical "
            "microbiology. J Appl Microbiol. 2015;118:1275-1282.")
CIT_CAUSAL = ("Lynch SV, Pedersen O. The human intestinal microbiome in health and disease. "
              "N Engl J Med. 2016;375:2369-2379; Sze MA, Schloss PD. Looking for a signal in the "
              "noise: revisiting obesity and the microbiome. mBio. 2016;7:e01018-16.")
CIT_HEALTHY = ("Human Microbiome Project Consortium. Structure, function and diversity of the "
               "healthy human microbiome. Nature. 2012;486:207-214; Lloyd-Price J et al. "
               "Strains, functions and dynamics in the expanded Human Microbiome Project. "
               "Nature. 2017;550:61-66.")
CIT_ANTIECO = ("Davies J. Specialized microbial metabolites: functions and origins. J Antibiot. "
               "2013;66:361-364; Linares JF et al. Antibiotics as intermicrobial signaling agents "
               "instead of weapons. PNAS. 2006;103:19484-19489.")
CIT_PERSIST = ("Lewis K. Persister cells. Annu Rev Microbiol. 2010;64:357-372; Balaban NQ et al. "
               "Bacterial persistence as a phenotypic switch. Science. 2004;305:1622-1625.")
CIT_HGT = ("Smillie CS et al. Ecology drives a global network of gene exchange connecting the "
           "human microbiome. Nature. 2011;480:241-244; Davies J, Davies D. Origins and "
           "evolution of antibiotic resistance. Microbiol Mol Biol Rev. 2010;74:417-433.")
CIT_VOID = ("Fischbach MA, Walsh CT. Antibiotics for emerging pathogens. Science. "
            "2009;325:1089-1093; Lewis K. Platforms for antibiotic discovery. Nat Rev Drug "
            "Discov. 2013;12:371-387.")
CIT_FMT = ("van Nood E et al. Duodenal infusion of donor feces for recurrent Clostridium "
           "difficile. N Engl J Med. 2013;368:407-415; Khoruts A, Sadowsky MJ. Understanding the "
           "mechanisms of faecal microbiota transplantation. Nat Rev Gastroenterol Hepatol. "
           "2016;13:508-516.")

ENTRIES = [
 {
  "key": "plate-count-anomaly",
  "name": "The Great Plate Count Anomaly",
  "group": "The Uncultured Majority",
  "ladder_rank": 1, "ladder_tier": "foundations",
  "description": ("Look at seawater under a microscope and you will count millions of bacterial cells per "
                  "milliliter. Spread that same water on a petri dish and a few thousand colonies grow. The "
                  "Great Plate Count Anomaly - named by Staley and Konopka in 1985 - is the gap between "
                  "cells we can see and cells we can grow: routinely less than one percent of environmental "
                  "microbes form colonies in the laboratory. The most approachable mystery in microbiology: "
                  "the overwhelming majority of microbial life refuses to grow on our plates."),
  "problem": "Why do fewer than one percent of environmental microbes grow in laboratory culture when microscopes show they are alive and abundant?",
  "background": ("The anomaly was formalized by James Staley and Alexander Konopka in their 1985 review, "
                 "though microbiologists had noticed the count mismatch for decades before. The gap widened "
                 "in the 1990s when ribosomal RNA surveys - pioneered by Norman Pace and colleagues - "
                 "revealed entire branches of the tree of life with no cultured representative at all. "
                 "Candidate explanations multiplied: standard media deliver the wrong nutrients at the wrong "
                 "concentrations, agar itself inhibits some organisms, many microbes need chemical signals "
                 "from neighbors, and some grow so slowly that a two-day plate incubation ends before they "
                 "start. Cultivation breakthroughs such as the diffusion chamber of Kim Lewis and Slava "
                 "Epstein, which grows cells in their native environment, proved many uncultured organisms "
                 "can grow given the right conditions. Yet after forty years the anomaly stands: most "
                 "microbes remain uncultured, and nobody fully knows why."),
  "why_it_matters": ("Every uncultured microbe is a locked library of genes, enzymes, and drugs we cannot "
                      "read directly. New antibiotics, industrial enzymes, and biocatalysts have all come "
                      "from the small cultured minority; the uncultured majority is the largest unexplored "
                      "genetic reservoir on Earth. Solving the anomaly would open that reservoir to medicine "
                      "and biotechnology."),
  "sig_lens": ("The Signature lens treats the plate as a foreign country and the microbe as a traveler who "
               "will not speak until it hears its own language: culture fails because we hand out phrasebooks "
               "written for someone else."),
  "sol_public": ("The Signature system proposes the anomaly is mostly a signaling failure: microbes wait for "
                 "community chemical cues before dividing, and sterile rich media scream the wrong message. "
                 "Cultivation should mimic the chemical conversation of the native habitat, not just its "
                 "nutrients. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) most environmental microbes are competent to divide but gated by "
              "chemical permission signals from their community; (2) standard media provide nutrients but "
              "destroy or omit those signals; (3) slow growth plus wrong signals explains the one-percent "
              "yield, not cell death. Reasoning path: treat cultivation as communication, not feeding. A "
              "microbe that evolved in a dense biofilm hears a constant chemical murmur - quorum signals, "
              "metabolic byproducts, neighbor waste it eats. A sterile agar plate is deafening silence plus "
              "an overdose of food, and many cells interpret silence as danger and stay dormant. This fits "
              "the diffusion-chamber result: cells grow when separated from neighbors by a membrane that "
              "lets chemistry through but not cells. Proposed mechanism: a two-stage cultivation protocol - "
              "first, capture the native chemical milieu by incubating sterile medium in the source "
              "environment to absorb its signal molecules; second, dilute to single cells in that "
              "\"conversation-conditioned\" medium and wait weeks, not days. What would confirm it: "
              "systematic sequencing of the signal molecules in successful conditioned media, and a "
              "demonstration that adding identified signals to sterile media raises culturability across "
              "diverse uncultured lineages. What would kill it: conditioned media that work without any "
              "detectable signal molecules, or proof that most uncultured cells are simply dead or dormant "
              "beyond revival. What it does NOT claim: that every uncultured microbe will grow this way, "
              "that dormancy does not exist, or that this replaces single-cell genomics. Where the honest "
              "answer is unknown - the full vocabulary of microbial permission signals - we say so: mapping "
              "that vocabulary is the missing measurement."),
  "key_points": [
   "Microscopy counts millions of cells per milliliter of seawater; plates grow thousands - under one percent.",
   "Named by Staley and Konopka in 1985; rRNA surveys in the 1990s revealed whole uncultured branches of life.",
   "Suspected causes: wrong nutrients, inhibitory agar, missing neighbor signals, too-short incubations.",
   "Diffusion chambers that let native chemistry through have cultured previously unculturable organisms.",
   "The uncultured majority is Earth's largest unexplored genetic reservoir for drugs and enzymes."],
  "requirements": [
   "Sequence the signal molecules present in successful conversation-conditioned media.",
   "Confirm: identified signals raise culturability across diverse uncultured lineages on sterile media.",
   "Refute: conditioned media work with no detectable signal molecules present.",
   "Refute: prove most uncultured cells are dead or irreversibly dormant rather than signal-gated."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim all uncultured microbes will grow, nor that dormancy is unreal.",
   "It must survive the vocabulary question: the signal set must be identified, not assumed."],
  "citations": [CIT_ANOMALY],
 },
 {
  "key": "viruses-alive",
  "name": "Are Viruses Alive?",
  "group": "Viral Dark Matter",
  "ladder_rank": 2, "ladder_tier": "foundations",
  "description": ("Ask a classroom whether viruses are alive and you will start an argument that has run for "
                  "a century. Viruses carry genes and evolve, but outside a host cell they do nothing at all: "
                  "no metabolism, no growth, no response. They sit on the exact boundary of every definition "
                  "of life, and biologists still cannot agree which side they fall on - or whether the "
                  "question itself is broken."),
  "problem": "Are viruses living organisms, or nonliving particles - and does the question even have a right answer?",
  "background": ("The debate began the moment viruses were discovered: Ivanovsky and Beijerinck showed in the "
                 "1890s that tobacco mosaic disease passed through bacteria-proof filters, and Wendell Stanley "
                 "crystallized the virus in 1935 - something no living thing was supposed to do. Textbooks "
                 "settled on \"not alive\" because viruses lack cells and metabolism. Then giant viruses were "
                 "found starting with Mimivirus in 2003, carrying hundreds of genes including translation "
                 "machinery once thought exclusive to cellular life, and the \"not alive\" camp had to "
                 "renegotiate. Eugene Koonin and Patrick Forterre reframed the question around the "
                 "\"replicator paradigm\": viruses are not organisms, but the virus factory inside an "
                 "infected cell is a living process. Others argue life should be defined by evolution, in "
                 "which case viruses qualify fully. The argument persists because every definition of life "
                 "was written about cells."),
  "why_it_matters": ("The answer decides how we teach biology's most basic concept, how we search for life "
                      "on other worlds - a strict cellular definition could blind us to virus-like entities "
                      "elsewhere - and how we classify the virosphere, which may hold more genetic diversity "
                      "than all cellular life combined. Definitions steer funding, textbooks, and missions."),
  "sig_lens": ("The Signature lens treats the question as a category error: we are asking a particle to "
               "answer for a process, like asking whether a seed is a forest."),
  "sol_public": ("The Signature system proposes the alive-or-not framing is the wrong unit of analysis: the "
                 "living thing is the virus factory - the temporary virus-controlled cell - while the "
                 "virion is its dormant spore. Classify the process, not the particle. Full treatment: the "
                 "Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) \"alive\" usefully describes processes that metabolize, maintain "
              "themselves, and evolve - not inert particles; (2) an infected cell under viral control meets "
              "those criteria; (3) a free virion meets none. Reasoning path: stop asking about the virion and "
              "ask about the virocell - the infected cell reorganized into a virus factory, a concept "
              "developed by Patrick Forterre. The virocell eats, builds, defends itself against competing "
              "viruses, and reproduces its kind; the virion is the dispersal stage, exactly as a bacterial "
              "endospore is dormant but the bacterium is alive. This dissolves the paradox without new "
              "biology: spores are not called nonliving, so virions should not be either - both are paused "
              "life, and the active phase is where \"alive\" applies. Proposed mechanism: formalize a "
              "two-phase ontology in virology - virion phase (dormant, particle physics and chemistry apply) "
              "and virocell phase (living, cell biology applies) - and rewrite definitions of life around "
              "the phase, not the entity. What would confirm it: virocells showing regulated metabolism "
              "distinct from both host and virion across diverse virus families, and predictive success - "
              "virocell biology predicting infection outcomes better than virion properties alone. What would "
              "kill it: viruses that replicate with no metabolically active factory phase, or proof that "
              "virocell metabolism is entirely host-run with no viral regulation. What it does NOT claim: "
              "that this settles philosophy of life, that prions or viroids fit the same frame, or that "
              "textbooks must change tomorrow. Where the honest answer is unknown - whether any natural "
              "entity exists that is only ever a virion with no active phase - we say so: the virosphere "
              "survey is incomplete."),
  "key_points": [
   "Viruses were discovered as filterable agents (1890s) and crystallized like chemicals (Stanley, 1935).",
   "Giant viruses found since 2003 carry translation genes once thought exclusive to cellular life.",
   "The virocell concept: the infected cell reorganized into a virus factory may be the true living phase.",
   "Koonin and Forterre reframed the debate around replicators and the virus factory rather than the particle.",
   "The definition matters for astrobiology: a cell-only definition of life could miss alien virus-like entities."],
  "requirements": [
   "Survey virocell metabolism across diverse virus families for virus-regulated active phases.",
   "Confirm: virocell biology predicts infection outcomes better than virion properties alone.",
   "Refute: find replicating viruses with no metabolically active factory phase.",
   "Refute: show virocell metabolism is entirely host-run with zero viral regulation."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim to settle the philosophy of life or to cover prions and viroids.",
   "It must survive the ontology test: the two-phase scheme must classify edge cases without special pleading."],
  "citations": [CIT_ALIVE],
 },
 {
  "key": "bacterial-species",
  "name": "What Is a Bacterial Species?",
  "group": "The Uncultured Majority",
  "ladder_rank": 3, "ladder_tier": "foundations",
  "description": ("Every biology student learns what a species is: for animals and plants, it is a group that "
                  "breeds together and not with outsiders. Bacteria do not breed - they copy themselves and "
                  "freely swap genes with strangers, even distant relatives. So the most basic unit of "
                  "biology, the species, has no agreed definition for the most abundant organisms on Earth, "
                  "and microbiologists argue about it to this day."),
  "problem": "What is a bacterial species, when bacteria reproduce without sex and trade genes across supposed species boundaries?",
  "background": ("The problem is as old as bacterial taxonomy. Early classification used shape and staining - "
                 "rods, spheres, Gram-positive, Gram-negative - which grouped unrelated organisms and split "
                 "close relatives. DNA hybridization in the 1980s gave a 70 percent similarity cutoff that "
                 "was pragmatic but arbitrary. The ribosomal RNA revolution let Carl Woese redraw the tree of "
                 "life, and genome sequencing replaced hybridization with average nucleotide identity - "
                 "typically 95 percent - as the working species boundary. But bacteria exchange DNA "
                 "horizontally across those boundaries constantly: antibiotic resistance genes cross genera, "
                 "and some \"species\" share less of their genome with each other than with outsiders. "
                 "Rossello-Mora and Amann, Achtman and Wagner, and others have proposed genomic, ecological, "
                 "and population-genetic definitions, but no single concept commands consensus."),
  "why_it_matters": ("Without a species definition, we cannot count microbial diversity, name new organisms "
                      "coherently, track pathogens across outbreaks, or write regulations about genetically "
                      "modified microbes. Medicine, ecology, and law all assume species exist; for bacteria, "
                      "the foundation is a working convention, not a settled fact."),
  "sig_lens": ("The Signature lens treats bacterial species as weather systems rather than animal breeds: "
               "real, nameable, but defined by flows and boundaries that move."),
  "sol_public": ("The Signature system proposes a dual definition: a genomic core that is stable plus an "
                 "ecological job description. A bacterial species is a population sharing a coherent core "
                 "genome AND occupying one ecological niche. Either criterion alone fails; together they "
                 "draw the working line. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) gene flow in bacteria is real but not random - it follows ecological "
              "contact; (2) the core genome tracks vertical descent while the accessory genome tracks "
              "ecological adaptation; (3) a definition must serve both naming and prediction. Reasoning "
              "path: the animal species concept fails for bacteria because it was built on reproductive "
              "isolation, which bacteria never had. Replace isolation with two observable axes. Axis one: "
              "core-genome coherence - the set of genes every member carries, diverging slowly and "
              "vertically. Axis two: ecological distinctness - the niche the population actually occupies, "
              "measured by where it is found and what it does. A species is then a cluster that is "
              "tight on both axes: members share a core genome above the 95 percent ANI line AND stably "
              "occupy one niche. Strains that share a genome but live in different niches are ecotypes "
              "awaiting speciation; populations sharing a niche but with scrambled cores are "
              "gene-exchange communities, not species. Proposed mechanism: formalize the dual criterion in "
              "taxonomy - require both genomic and ecological evidence for species descriptions, with "
              "machine-readable niche data attached to every type genome. What would confirm it: the dual "
              "criterion resolving disputed cases - splitting lumped pathogens or merging split ones - in "
              "ways that predict phenotype better than either axis alone. What would kill it: large "
              "populations tight on both axes that still behave as multiple species by every practical "
              "test, or proof that ecological niche cannot be measured reproducibly for microbes. What it "
              "does NOT claim: that horizontal gene transfer stops at species borders, that the 95 percent "
              "line is God-given, or that this ends all taxonomic disputes. Where the honest answer is "
              "unknown - how to measure a microbial niche reproducibly at scale - we say so: the niche "
              "measurement is the missing instrument."),
  "key_points": [
   "Animals define species by breeding; bacteria reproduce asexually and swap genes with strangers.",
   "Working cutoffs (70% DNA hybridization, 95% average nucleotide identity) are pragmatic, not principled.",
   "Horizontal gene transfer moves genes across genus boundaries, scrambling genome-based definitions.",
   "Competing proposals - genomic, ecological, population-genetic - each explain part of the data.",
   "Medicine, ecology, and law all assume bacterial species exist; the foundation is convention."],
  "requirements": [
   "Apply the dual criterion to disputed taxa and test whether it predicts phenotype better than either axis alone.",
   "Confirm: populations tight on both axes behave as single species in practice.",
   "Refute: find populations tight on both axes that still behave as multiple species.",
   "Refute: show microbial ecological niche cannot be measured reproducibly at scale."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim gene transfer respects species borders or that 95 percent ANI is fundamental.",
   "It must survive the measurement test: niche data must be reproducible, not anecdotal."],
  "citations": [CIT_SPECIES],
 },
 {
  "key": "gut-unculturable",
  "name": "Why Can't We Grow Most Gut Microbes?",
  "group": "The Uncultured Majority",
  "ladder_rank": 4, "ladder_tier": "foundations",
  "description": ("Your gut holds trillions of bacteria from hundreds of species, and DNA sequencing can list "
                  "them all. But try to grow them in the lab - the step needed to test what any one of them "
                  "actually does - and most refuse. Even from the best-studied microbial community on Earth, "
                  "the human gut, the majority of species resist cultivation, leaving medicine with a parts "
                  "list and no spare parts."),
  "problem": "Why do most gut microbes refuse to grow in laboratory culture even though they thrive by the trillion inside us?",
  "background": ("The Human Microbiome Project and the MetaHIT catalog showed the gut holds hundreds of "
                 "bacterial species per person and thousands across humanity, yet culture collections held a "
                 "small fraction. The obstacles are specific: the gut is strictly oxygen-free, and even "
                 "brief oxygen exposure kills many residents; they eat each other's waste products in "
                 "obligate cross-feeding chains, so no single species grows alone; and they depend on host "
                 "signals - mucus, bile, immune molecules - that no bottle reproduces. Browne and colleagues "
                 "showed in 2016 that many \"unculturable\" gut bacteria are spore-formers that simply needed "
                 "their dormancy broken, culturing dozens of novel taxa with ethanol shock and targeted "
                 "media. Culturomics - high-throughput culturing with hundreds of conditions - has since "
                 "recovered many more. Still, a large fraction resists every protocol tried."),
  "why_it_matters": ("You cannot test a microbe's effect on health, screen it for drugs, or build it into a "
                      "probiotic if you cannot grow it. The uncultured gut fraction may hold the organisms "
                      "behind inflammatory disease, obesity, and treatment responses - medicine's most wanted "
                      "microbes are the ones it cannot hold in a tube."),
  "sig_lens": ("The Signature lens treats the gut as a city and the lab as a wilderness camp: citizens do "
               "not survive when you deport them alone into the woods without the city's services."),
  "sol_public": ("The Signature system proposes cultivation must reproduce the gut's service economy - "
                 "oxygen-free cross-feeding chains plus host secretions - by growing defined communities, "
                 "not isolates. Stop deporting citizens; build miniature cities. Full treatment: the "
                 "Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) most uncultured gut species are obligate community members, not "
              "failed isolates; (2) their growth requirements are services provided by neighbors and host, "
              "not just nutrients; (3) spores and dormancy explain a large additional fraction. Reasoning "
              "path: the isolate-first tradition assumes every species is self-sufficient, which the gut "
              "actively selects against - in a dense, stable community, shedding metabolic independence and "
              "relying on neighbors is efficient. So the unit of cultivation should be the minimal "
              "supporting community, not the single strain. Proposed mechanism: a community-first pipeline - "
              "sequence the community, identify cross-feeding dependencies from genomes, then culture "
              "minimal synthetic consortia in gut-on-chip devices with mucus, bile gradients, and strict "
              "anoxia, subtracting members until the minimal viable city is found. Spore-formers get "
              "dormancy-breaking pretreatments first. What would confirm it: minimal consortia that grow "
              "species never grown alone, with the dependency map predicting exactly which members are "
              "indispensable. What would kill it: species that grow alone once a single missing nutrient is "
              "found - proving isolation was never the problem - or consortia that still fail despite "
              "complete dependency maps. What it does NOT claim: that every gut microbe needs a community, "
              "that gut-on-chip reproduces the gut, or that spores explain everything. Where the honest "
              "answer is unknown - the complete dependency map of the gut community - we say so: it must be "
              "measured, not assumed."),
  "key_points": [
   "The gut holds hundreds of species per person, yet culture collections long held only a fraction.",
   "Killers of cultivation: oxygen exposure, obligate cross-feeding, missing host signals like mucus and bile.",
   "Many unculturables proved to be spore-formers needing dormancy-breaking, not impossible organisms.",
   "Culturomics with hundreds of conditions has recovered many novel taxa, but a large fraction still resists.",
   "Uncultured gut species may drive inflammatory disease, obesity, and drug responses."],
  "requirements": [
   "Build minimal synthetic consortia that grow species never grown in isolation.",
   "Confirm: dependency maps predict exactly which community members are indispensable.",
   "Refute: species grow alone once a single missing nutrient is identified.",
   "Refute: complete dependency maps still fail to yield growth in gut-on-chip consortia."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim every gut microbe needs a community or that chips reproduce the gut.",
   "It must survive the subtraction test: minimal consortia must be truly minimal, not lucky mixtures."],
  "citations": [CIT_GUTCULT],
 },
 {
  "key": "vbnc-state",
  "name": "The VBNC State: Dead or Dormant?",
  "group": "The Uncultured Majority",
  "ladder_rank": 5, "ladder_tier": "foundations",
  "description": ("Starve or chill many bacteria and they stop growing on plates - yet stains show their "
                  "membranes intact and their genes still active. They have entered the viable but "
                  "nonculturable state: VBNC. Are these cells alive and waiting, or corpses that have not "
                  "finished dying? The answer decides whether our water, food, and hospitals are safer than "
                  "our tests say."),
  "problem": "Are VBNC bacteria alive and capable of revival, or irreversibly dying - and how can we tell the difference?",
  "background": ("The VBNC state was described in the early 1980s when researchers found that Vibrio and "
                 "other pathogens persisted in water long after plate counts fell to zero. Since then dozens "
                 "of species - including cholera, tuberculosis, and foodborne pathogens - have been shown to "
                 "enter the state under starvation, cold, chlorine, or antibiotics. Some VBNC populations "
                 "have been \"resuscitated\" back to culturability with fresh nutrients or specific signals, "
                 "and VBNC pathogens have caused disease in animal models, suggesting real danger. Skeptics "
                 "counter that many resuscitation claims reflect a few undetected culturable cells "
                 "multiplying, not true revival, and that membrane-intact staining overcounts the living. "
                 "The field still lacks a universal marker separating dormant-but-viable from dead."),
  "why_it_matters": ("If VBNC pathogens are alive, then water treatment, food safety testing, and hospital "
                      "disinfection protocols that rely on plate counts are systematically underestimating "
                      "risk. Cholera, tuberculosis, and Listeria all have VBNC reports; public health "
                      "decisions rest on which interpretation is right."),
  "sig_lens": ("The Signature lens treats VBNC as hibernation with a combination lock: the cell is alive "
               "but the key that wakes it is specific, and we keep trying the wrong keys."),
  "sol_public": ("The Signature system proposes VBNC is a regulated program with specific wake keys, and "
                 "that single-cell tracking - watching one cell wake, not populations - is the decisive test. "
                 "Stop counting crowds; watch individuals. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) VBNC is an evolved stress program, not random damage; (2) entry and "
              "exit are regulated by specific molecular signals; (3) population-level resuscitation data are "
              "confounded by rare culturable survivors. Reasoning path: the forty-year stalemate comes from "
              "measuring populations. If one cell in a million is secretly culturable, it will overgrow and "
              "fake a resuscitation. The only clean test is single-cell: trap individual VBNC cells in "
              "microfluidic chambers, verify zero division for weeks, then apply candidate wake signals and "
              "watch. A cell that divides after verified dormancy was alive; one that never does was not. "
              "Proposed mechanism: build a VBNC single-cell observatory - microfluidic arrays holding tens of "
              "thousands of individually tracked cells, screened against libraries of candidate resuscitation "
              "signals (nutrients, quorum molecules, host factors, temperature shifts), with viability dyes "
              "and gene-expression reporters read per cell. Map which signals wake which species and the "
              "molecular lock each opens. What would confirm it: reproducible single-cell revival with "
              "defined signals across multiple pathogens, plus identification of the wake-signal receptors. "
              "What would kill it: zero single-cell revivals across exhaustive signal screens - implying "
              "VBNC is terminal - or revival that always traces to pre-existing culturable contaminants. "
              "What it does NOT claim: that all VBNC cells revive, that staining equals life, or that every "
              "pathogen uses the same lock. Where the honest answer is unknown - the wake keys for most "
              "species - we say so: the screen must discover them, not assume them."),
  "key_points": [
   "Dozens of species including cholera, TB, and foodborne pathogens enter VBNC under stress.",
   "VBNC cells keep intact membranes and gene activity but will not grow on plates.",
   "Some populations resuscitate and cause disease in animals; skeptics blame hidden culturable survivors.",
   "No universal marker separates dormant-but-viable from dead cells.",
   "Plate-count-based safety testing may systematically underestimate pathogen risk."],
  "requirements": [
   "Demonstrate verified single-cell revival: one tracked dormant cell dividing after defined signals.",
   "Confirm: wake-signal receptors identified for multiple pathogens with reproducible revival.",
   "Refute: exhaustive signal screens yield zero single-cell revivals in any species.",
   "Refute: all apparent revivals trace to pre-existing culturable contaminants."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim all VBNC cells revive or that membrane staining equals life.",
   "It must survive the contamination test: single-cell tracking must rule out hidden growers."],
  "citations": [CIT_VBNC],
 },
 {
  "key": "microbiome-causation",
  "name": "Correlation or Causation in the Microbiome",
  "group": "Microbiome and Health",
  "ladder_rank": 6, "ladder_tier": "foundations",
  "description": ("Study after study reports that sick people carry different gut microbes than healthy "
                  "people - in obesity, diabetes, depression, autism, and dozens more conditions. But do the "
                  "microbes cause the disease, does the disease reshape the microbes, or does some third "
                  "factor move both? This is the central credibility crisis of microbiome science: thousands "
                  "of correlations, and causation proven in only a handful of cases."),
  "problem": "When disease and microbiome changes travel together, how do we prove which causes which?",
  "background": ("The correlation flood began with the Human Microbiome Project era around 2007: obesity "
                 "linked to a shifted Firmicutes-to-Bacteroidetes ratio (Ley 2006), then diabetes, "
                 "inflammatory bowel disease, depression, Parkinson's, and autism each got their microbial "
                 "signature. But signatures wobbled - the obesity ratio failed replication in large cohorts "
                 "(Sze and Schloss 2016), and many signatures turned out to track diet, drugs, or geography "
                 "rather than disease. The gold standard, transplanting human microbes into germ-free mice "
                 "and transferring the trait, has worked for a few cases but mice are not people, and "
                 "germ-free mice have broken immune systems. Fecal transplant cures recurrent C. difficile "
                 "in humans - genuine causal proof - but for nearly every other condition, causation remains "
                 "unproven. The field now demands longitudinal studies, Mendelian randomization, and "
                 "mechanistic experiments before claiming cause."),
  "why_it_matters": ("Billions flow into probiotics, microbiome drugs, and diagnostics on the promise that "
                      "microbes drive disease. If most signatures are consequences or confounders, that money "
                      "chases mirages - and patients get false hope. A causation standard separates real "
                      "microbial medicine from expensive storytelling."),
  "sig_lens": ("The Signature lens treats correlation as a footprint and causation as the foot: you do not "
               "convict the footprint until you have seen the foot press the ground."),
  "sol_public": ("The Signature system proposes a causation ladder with four rungs - prediction, "
                 "transplantability, mechanism, and reversibility - and no causal claim without climbing all "
                 "four. Footprints are evidence; only feet convict. Full treatment: the Signature edition "
                 "record."),
  "sol_sig": (LABEL + " Assumptions: (1) most microbiome-disease links are real associations whose direction "
              "is unknown; (2) confounders - diet, drugs, transit time - explain many signatures; (3) true "
              "causal microbes must satisfy multiple independent tests. Reasoning path: the field's error was "
              "treating one strong correlation as enough. Replace it with an explicit four-rung ladder. Rung "
              "one, prediction: the microbial signature must predict disease onset in longitudinal cohorts "
              "before symptoms appear. Rung two, transplantability: moving the community transfers a "
              "measurable trait in a controlled model. Rung three, mechanism: a specific molecule or pathway "
              "from specific microbes must produce the effect when given alone. Rung four, reversibility: "
              "removing or blocking that mechanism must improve the condition. C. difficile has climbed all "
              "four; obesity has stalled at rung two in mice. Proposed mechanism: institutionalize the "
              "ladder - journals and funders require rung-three mechanism for any causal language, and build "
              "prospective human cohorts with dense pre-disease sampling to test rung one at scale. What "
              "would confirm it: the ladder correctly sorting known cases - C. difficile at the top, failed "
              "signatures at the bottom - and new rung-four successes producing real therapies. What would "
              "kill it: diseases where all four rungs are climbed yet interventions still fail in humans, "
              "proving even full ladders do not guarantee translation - or a causal microbe that works "
              "through no identifiable mechanism, breaking rung three. What it does NOT claim: that "
              "correlations are worthless, that mouse work is useless, or that every disease needs all four "
              "rungs before research begins. Where the honest answer is unknown - how many current "
              "signatures will survive the ladder - we say so: the prospective cohorts must be run."),
  "key_points": [
   "Thousands of disease-microbiome correlations exist; causation is proven in only a handful of cases.",
   "Famous signatures like the obesity Firmicutes ratio failed replication in large cohorts.",
   "Germ-free mouse transplants transfer some traits but mice are not people.",
   "Fecal transplant for recurrent C. difficile is the rare human causal proof.",
   "Confounders - diet, medications, geography - explain many published signatures."],
  "requirements": [
   "Show the ladder sorts known cases: C. difficile at rung four, failed signatures at rung one.",
   "Confirm: new rung-four successes produce real human therapies.",
   "Refute: full four-rung cases whose interventions still fail in humans.",
   "Refute: a causal microbe acting through no identifiable mechanism, breaking rung three."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim correlations are worthless or mouse work useless.",
   "It must survive the translation test: rung four must predict human outcomes, not just models."],
  "citations": [CIT_CAUSAL],
 },
 {
  "key": "healthy-microbiome",
  "name": "What Is a Healthy Microbiome?",
  "group": "Microbiome and Health",
  "ladder_rank": 7, "ladder_tier": "foundations",
  "description": ("Doctors can define healthy blood pressure, healthy cholesterol, healthy weight. But ask "
                  "for the definition of a healthy gut microbiome and the field goes quiet. Healthy people "
                  "carry wildly different microbes - by diet, geography, age, and birth history - and no "
                  "universal microbial fingerprint of health has ever been found. Medicine wants to fix "
                  "broken microbiomes, but it cannot say what unbroken looks like."),
  "problem": "What defines a healthy human microbiome, given that healthy people carry completely different microbial communities?",
  "background": ("The Human Microbiome Project (2012) profiled hundreds of healthy Americans and found the "
                 "opposite of a standard: community composition varied enormously between healthy "
                 "individuals, while microbial gene functions were far more consistent. Follow-up work showed "
                 "diet dominates - Hadza hunter-gatherers, rural Africans, and urban Europeans carry "
                 "strikingly different gut communities, all healthy. Proposed definitions have cycled "
                 "through diversity (more is better - contradicted by the low-diversity but healthy infant "
                 "gut), stability over time, resilience after disturbance, and presence of \"keystone\" "
                 "species. Each captures something real and fails as a universal rule. The emerging view is "
                 "functional: health may be defined by what the community does - its genes and metabolites - "
                 "not who is there. But functional baselines are still being mapped."),
  "why_it_matters": ("Every probiotic, microbiome drug, and \"gut health\" test implicitly assumes a target "
                      "to aim for. Without a definition of healthy, treatments aim at a guess, diagnostics "
                      "flag normal variation as disease, and consumers buy products optimizing a number nobody "
                      "understands. The definition is the missing ruler for the entire field."),
  "sig_lens": ("The Signature lens treats health as a job well done rather than a staff roster: a healthy "
               "microbiome is defined by the work it performs, not the workers on shift."),
  "sol_public": ("The Signature system proposes health be defined functionally - by metabolic outputs like "
                 "short-chain fatty acids and bile-acid conversion - measured against personal baselines, not "
                 "population averages. Judge the work, not the roster. Full treatment: the Signature edition "
                 "record."),
  "sol_sig": (LABEL + " Assumptions: (1) taxonomic composition is too variable across healthy people to "
              "define health; (2) microbial functions - genes and metabolites - are more conserved; (3) "
              "health is partly personal, so baselines must be individual. Reasoning path: the roster "
              "approach failed because different species do the same jobs - functional redundancy means "
              "ten different communities can all ferment fiber into butyrate. So define health as a "
              "functional profile: the community must produce a set of key metabolites within personal "
              "reference ranges, resist invasion by pathogens, and rebound after disturbance. The personal "
              "part matters: a Hadza farmer and a Chicago office worker can both be healthy with different "
              "profiles, so each person is compared to their own history, like heart-rate variability. "
              "Proposed mechanism: build functional health panels - standardized measurements of fecal and "
              "blood microbial metabolites, metagenomic functional capacity, and resilience assays (response "
              "to a defined dietary challenge) - then run decade-long cohorts to learn which functional "
              "deviations actually predict disease. What would confirm it: functional profiles predicting "
              "disease onset better than any taxonomic signature, across diets and geographies. What would "
              "kill it: healthy people with stably \"broken\" functional profiles by every measure, or "
              "proof that functions are as individually variable as taxonomy. What it does NOT claim: that "
              "taxonomy is irrelevant, that one panel fits all humanity, or that function alone captures "
              "pathogen risk. Where the honest answer is unknown - which functions belong in the core panel "
              "- we say so: the cohorts must discover them."),
  "key_points": [
   "Healthy people carry enormously different gut microbes; no universal taxonomic fingerprint of health exists.",
   "Microbial gene functions are far more consistent across healthy people than species lists.",
   "Diet and geography dominate composition: hunter-gatherers and urbanites differ yet are all healthy.",
   "Candidate definitions - diversity, stability, resilience, keystones - each fail as universal rules.",
   "The field is shifting to functional definitions: health as what the community does, not who is there."],
  "requirements": [
   "Build functional health panels and test them in decade-long prospective cohorts.",
   "Confirm: functional profiles predict disease onset across diets and geographies.",
   "Refute: healthy people with stably broken functional profiles by every measure.",
   "Refute: microbial functions prove as individually variable as taxonomy."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim taxonomy is irrelevant or that one panel fits all humanity.",
   "It must survive the prediction test: functions must forecast disease, not just describe health."],
  "citations": [CIT_HEALTHY],
 },
 {
  "key": "antibiotic-ecology",
  "name": "Why Do Bacteria Make Antibiotics?",
  "group": "Antibiotic Resistance",
  "ladder_rank": 8, "ladder_tier": "foundations",
  "description": ("Soil bacteria manufacture some of humanity's most powerful medicines - penicillin, "
                  "streptomycin, vancomycin all began as microbial products. The textbook story says they "
                  "are weapons for killing competitors. But in real soil, antibiotics exist at "
                  "concentrations far too low to kill anything, and they change bacterial behavior instead. "
                  "So why do microbes spend precious energy building chemical weapons they never fire?"),
  "problem": "What is the true ecological function of antibiotics in nature, if natural concentrations are too low to kill?",
  "background": ("Selman Waksman coined \"antibiotic\" and built the screening programs that found "
                 "streptomycin, assuming these molecules were weapons in microbial warfare. The warfare view "
                 "dominated for half a century. Then measurements showed natural antibiotic concentrations "
                 "in soil are typically orders of magnitude below killing doses - sub-inhibitory. At those "
                 "doses, antibiotics do something stranger: they alter gene expression, trigger biofilm "
                 "formation, and modulate quorum sensing. Julian Davies and others proposed antibiotics are "
                 "ancient signaling molecules - a chemical language - and killing is a side effect seen only "
                 "at the unnaturally high doses of medicine and lab assays. Supporting the signal view, "
                 "antibiotic production genes are widespread and ancient, and producers often gain no "
                 "competitive advantage from them in soil experiments. The warfare-versus-signal debate "
                 "remains unresolved."),
  "why_it_matters": ("If antibiotics are signals, then resistance genes are not just shields against weapons "
                      "but parts of a communication network - and our massive medical use of antibiotics is "
                      "shouting in a language we do not speak, with unpredictable ecological fallout. "
                      "Understanding the true function rewrites resistance strategy and could reveal new "
                      "drug targets in the signaling pathways."),
  "sig_lens": ("The Signature lens treats antibiotics as words before weapons: microbes invented a language, "
               "and humans mistook shouting for the whole conversation."),
  "sol_public": ("The Signature system proposes antibiotics are primarily dose-dependent signals - words at "
                 "low dose, weapons only at high dose - and that resistance genes originally tuned the "
                 "conversation. Read the language to predict resistance. Full treatment: the Signature "
                 "edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) natural antibiotic concentrations are usually sub-inhibitory; (2) "
              "sub-inhibitory doses measurably change microbial behavior; (3) signaling functions predate "
              "the warfare use. Reasoning path: evolution rarely maintains expensive molecules for a "
              "function used almost never. If killing required concentrations rarely reached in soil, the "
              "molecules must pay their metabolic rent another way - and the observed behavioral effects at "
              "low dose are the rent being paid. The dose-response curve then has two regimes: low-dose "
              "signaling (gene regulation, biofilm cues, developmental triggers) and high-dose killing "
              "(medicine's regime). Resistance genes in this view are partly signal-tuning knobs - "
              "efflux pumps and modifying enzymes that set local concentrations. Proposed mechanism: map "
              "the \"antibiotic lexicon\" - for major natural antibiotics, measure the full dose-response "
              "from picomolar to lethal across diverse soil communities, cataloging behavioral and "
              "transcriptional effects at each dose, and test whether resistance genes track signal "
              "regulation better than killing protection in the wild. What would confirm it: resistance "
              "genes whose wild-type function is demonstrably signal tuning, and lexicon maps predicting "
              "community responses to new molecules. What would kill it: proof that natural micro-niches "
              "routinely reach killing concentrations, making warfare the real function after all - or "
              "antibiotics with no behavioral effects at any sub-lethal dose. What it does NOT claim: that "
              "killing never happens in nature, that all antibiotics are signals, or that medicine should "
              "stop using them. Where the honest answer is unknown - the true concentration landscape of "
              "soil at microbial scales - we say so: it must be measured in situ."),
  "key_points": [
   "Major drugs - penicillin, streptomycin, vancomycin - began as microbial natural products.",
   "Natural soil concentrations of antibiotics are typically far below killing doses.",
   "At sub-lethal doses antibiotics alter gene expression, biofilms, and quorum sensing.",
   "The signal hypothesis: antibiotics are an ancient chemical language; killing is a high-dose side effect.",
   "Resistance genes may be signal-tuning knobs, not just shields."],
  "requirements": [
   "Map full dose-response lexicons for major natural antibiotics across soil communities.",
   "Confirm: wild-type resistance genes demonstrably tune signaling rather than just block killing.",
   "Refute: natural micro-niches routinely reach killing concentrations.",
   "Refute: antibiotics with zero behavioral effects at any sub-lethal dose."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim killing never occurs in nature or that medicine should abandon antibiotics.",
   "It must survive the concentration test: real in-situ dose measurements, not lab extrapolations."],
  "citations": [CIT_ANTIECO],
 },
 {
  "key": "persister-cells",
  "name": "Persister Cells: Tolerance Without Resistance",
  "group": "Antibiotic Resistance",
  "ladder_rank": 9, "ladder_tier": "foundations",
  "description": ("Treat a bacterial infection with antibiotics and 99.9 percent of cells die. Stop the drug "
                  "and the infection roars back - from survivors that carry no resistance genes at all. These "
                  "are persister cells: dormant variants that simply wait out the attack, then wake and "
                  "rebuild. They explain why some infections need weeks of drugs, and science still cannot "
                  "fully explain how they form or how to kill them."),
  "problem": "How do persister cells survive antibiotics without resistance genes, and how can they be eliminated?",
  "background": ("Joseph Bigger noticed in 1944 that penicillin left a tiny surviving fraction of "
                 "staphylococci that were not resistant mutants. The phenomenon was largely ignored until Kim "
                 "Lewis revived it, showing persisters are phenotypic variants - genetically identical to "
                 "their dead siblings but dormant. Nathalie Balaban proved in 2004 with single-cell "
                 "microscopy that persisters pre-exist antibiotics as slow-growing variants. Toxin-antitoxin "
                 "modules, the stringent response, and ATP depletion have all been implicated in persister "
                 "formation, but no universal mechanism covers all species, and persisters look different in "
                 "every organism studied. They underlie chronic infections - tuberculosis, urinary tract "
                 "infections, device biofilms - where drugs kill the active majority but the dormant "
                 "minority reseeds disease. No approved drug specifically targets persisters."),
  "why_it_matters": ("Persisters turn curable infections into chronic ones and force long, toxic antibiotic "
                      "courses that breed true genetic resistance. Tuberculosis treatment takes six months "
                      "largely because of persisters. A persister-killing drug would shorten treatments, cut "
                      "resistance evolution, and save millions of treatment failures."),
  "sig_lens": ("The Signature lens treats persisters as bunkers, not armor: you cannot shoot what is "
               "underground, so the answer is not a bigger gun but a way to force the doors open."),
  "sol_public": ("The Signature system proposes persisters are an energy-state bunker - cells that drop ATP "
                 "below the threshold antibiotics need - and the kill strategy is forced wake-up: raise their "
                 "metabolism, then strike. Open the bunker doors before firing. Full treatment: the "
                 "Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) most antibiotics corrupt active processes - wall building, protein "
              "synthesis, DNA replication; (2) dormant cells run none of these, so the drugs find no "
              "target; (3) dormancy is a reversible low-energy state, not damage. Reasoning path: "
              "resistance is armor - it blocks the bullet. Persistence is a bunker - it removes the target. "
              "Armor is defeated by better bullets; bunkers are defeated by forcing occupants out. The "
              "forced-wake strategy: first administer a metabolic stimulant - specific carbon sources, "
              "electron acceptors, or signaling molecules that raise persister ATP and restart target "
              "processes - then apply the antibiotic while the cells are awake. This has worked in "
              "proof-of-concept studies where sugars potentiated aminoglycoside killing of persisters. "
              "Proposed mechanism: build a persister wake-key atlas - for major pathogens, screen metabolite "
              "and signal libraries for compounds that specifically raise persister metabolism without "
              "feeding the infection, then pair each key with its antibiotic in timed two-step dosing, "
              "validated in biofilm and animal models. What would confirm it: wake-key plus antibiotic "
              "pairs that sterilize chronic-infection models where antibiotics alone fail, with persisters "
              "measurably re-entering metabolism before dying. What would kill it: persisters that survive "
              "despite full metabolic reactivation - proving dormancy is not the shield - or wake keys that "
              "cannot be found without also fueling pathogen growth. What it does NOT claim: that all "
              "persisters share one mechanism, that wake-ups are safe in patients, or that this replaces "
              "resistance control. Where the honest answer is unknown - the complete wake-key set per "
              "pathogen - we say so: the screens must discover them."),
  "key_points": [
   "Persisters are dormant variants, genetically identical to killed siblings, that survive antibiotics.",
   "Described by Bigger in 1944; Balaban proved in 2004 they pre-exist treatment as slow growers.",
   "Toxin-antitoxin systems, stringent response, and ATP depletion are implicated; no universal mechanism exists.",
   "They drive chronic infections: TB, UTIs, device biofilms - and long treatments that breed resistance.",
   "No approved drug specifically targets persister cells."],
  "requirements": [
   "Build wake-key atlases: metabolites that reactivate persisters per major pathogen.",
   "Confirm: wake-key plus antibiotic sterilizes chronic-infection models where drugs alone fail.",
   "Refute: persisters survive despite verified full metabolic reactivation.",
   "Refute: wake keys cannot be found without fueling pathogen growth."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim one universal persister mechanism or proven patient safety.",
   "It must survive the sterilization test: models must be truly sterilized, not just suppressed."],
  "citations": [CIT_PERSIST],
 },
 {
  "key": "resistance-spread",
  "name": "Why Does Resistance Spread So Fast?",
  "group": "Antibiotic Resistance",
  "ladder_rank": 10, "ladder_tier": "foundations",
  "description": ("Penicillin arrived in the 1940s; resistant staphylococci followed within years. Every new "
                  "antibiotic in history has met resistance with shocking speed - sometimes before the drug "
                  "even reaches wide use. Bacteria do not wait for lucky mutations: they trade resistance "
                  "genes like cards, passing them between species, genera, and ecosystems at a pace that "
                  "defies classical evolution."),
  "problem": "How does antibiotic resistance move between bacterial species and ecosystems so much faster than mutation alone allows?",
  "background": ("The speed record belongs to horizontal gene transfer. Resistance genes ride plasmids, "
                 "transposons, and integrons - mobile DNA that jumps between cells by conjugation, "
                 "transformation, and viral transduction. Smillie and colleagues showed in 2011 that the "
                 "human microbiome hosts a global gene-exchange network, with ecology - who lives near whom "
                 "- predicting transfer better than relatedness. Hospitals, farms, and wastewater plants "
                 "act as mixing vessels where diverse bacteria meet under antibiotic selection. The "
                 "mobilome - the total mobile gene pool - means a resistance gene that evolves once, "
                 "anywhere, can reach pathogens everywhere. Selection then does the rest: even low "
                 "antibiotic levels enrich resistant carriers. The result is a worldwide resistance "
                 "economy operating far faster than vertical evolution."),
  "why_it_matters": ("Resistance already kills over a million people yearly and threatens to make routine "
                      "surgery, childbirth, and chemotherapy lethally risky. If we cannot slow the trade in "
                      "resistance genes, every new antibiotic is a depreciating asset - and the pipeline of "
                      "new drugs is nearly empty."),
  "sig_lens": ("The Signature lens treats resistance genes as currency and bacteria as traders: the question "
               "is not how the mint prints money but how the markets move it."),
  "sol_public": ("The Signature system proposes the spread be fought at the market level: map the transfer "
                 "hubs - the mixing vessels and hub species - and disrupt exchange itself rather than "
                 "chasing each gene. Close the markets, not just the mints. Full treatment: the Signature "
                 "edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) horizontal transfer, not mutation, sets the speed limit of spread; "
              "(2) transfer is concentrated in ecological hubs and hub species, not uniform; (3) blocking "
              "transfer is evolutionarily harder to evade than killing cells. Reasoning path: chasing "
              "individual resistance genes is whack-a-mole - the mobilome holds thousands. But trade needs "
              "infrastructure: conjugative plasmids with their transfer machinery, competent recipients, and "
              "mixing-vessel environments. Target the infrastructure. Conjugation inhibitors - compounds that "
              "jam plasmid transfer without killing bacteria - would slow the market without the selection "
              "pressure that breeds resistance to the inhibitor itself, since non-transferring cells are not "
              "killed. Proposed mechanism: map the global transfer network to find hub plasmids and hub "
              "environments (hospital effluent, farm runoff, wastewater), then deploy conjugation blockers "
              "and plasmid-curing strategies at hubs, measuring resistance-gene flow rates before and after "
              "with metagenomic tracking. What would confirm it: measurable drops in inter-species gene flow "
              "at treated hubs and slower emergence of new resistant pathogen strains downstream. What would "
              "kill it: transfer proving too diffuse to have targetable hubs, or bacteria rapidly evolving "
              "around conjugation blockers despite the weak selection pressure. What it does NOT claim: that "
              "transfer can be stopped entirely, that mutation is irrelevant, or that blockers are ready for "
              "use. Where the honest answer is unknown - the true map of global transfer hubs - we say so: "
              "the metagenomic tracking must draw it."),
  "key_points": [
   "Every antibiotic in history has met resistance with shocking speed, sometimes before wide use.",
   "Resistance genes ride mobile DNA - plasmids, transposons, integrons - between species and genera.",
   "The human microbiome hosts a global gene-exchange network predicted by ecology, not relatedness.",
   "Hospitals, farms, and wastewater plants are mixing vessels under antibiotic selection.",
   "A gene evolving once anywhere can reach pathogens everywhere via the mobilome."],
  "requirements": [
   "Map global transfer hubs: hub plasmids, hub species, hub environments via metagenomic tracking.",
   "Confirm: conjugation blockers measurably reduce inter-species gene flow at treated hubs.",
   "Refute: transfer proves too diffuse for any targetable hub structure.",
   "Refute: bacteria rapidly evolve around blockers despite weak selection pressure."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim transfer can be stopped or that mutation is irrelevant.",
   "It must survive the flow test: gene-flow rates must be measured directly, not inferred."],
  "citations": [CIT_HGT],
 },
 {
  "key": "antibiotic-void",
  "name": "The Antibiotic Discovery Void",
  "group": "Antibiotic Resistance",
  "ladder_rank": 11, "ladder_tier": "foundations",
  "description": ("No entirely new class of antibiotics for serious infections has reached patients since the "
                  "1980s. The golden age that gave us penicillin, tetracycline, and vancomycin ended, and "
                  "decades of industrial screening have mostly rediscovered the same old molecules. "
                  "Meanwhile resistance climbs. Why did the well run dry - and is there water deeper down?"),
  "problem": "Why has no new antibiotic class reached the clinic in decades despite massive screening, and where could new ones come from?",
  "background": ("Waksman's soil-screening platform found most of our antibiotic classes between the 1940s "
                 "and 1960s by growing soil actinomycetes and testing their products. By the 1980s the "
                 "approach hit the rediscovery wall: the easy molecules had been found, and screens kept "
                 "returning known compounds. Pharma largely abandoned antibiotic R&D in the 1990s-2000s as "
                 "unprofitable. Genomics promised a way out - mine bacterial genomes for silent biosynthetic "
                 "gene clusters - and revealed microbes carry far more antibiotic-making genes than "
                 "chemistry ever showed, most switched off in the lab. Kim Lewis's group broke the "
                 "cultivation barrier with the iChip and found teixobactin in 2015 from a previously "
                 "uncultured soil bacterium - proof the well is not dry. Yet teixobactin and its cousins "
                 "remain years from patients, and the economic model for antibiotics is still broken."),
  "why_it_matters": ("Without new classes, medicine faces a post-antibiotic era where resistant infections "
                      "defeat every drug. The void is both a scientific problem - where are the molecules? - "
                      "and an economic one - who pays to develop drugs used briefly and held in reserve? "
                      "Solving the scientific half is prerequisite to everything else."),
  "sig_lens": ("The Signature lens treats the void as a listening problem: the molecules exist in silent "
               "gene clusters, and we have been shouting into the soil instead of learning what switches "
               "the factories on."),
  "sol_public": ("The Signature system proposes systematic factory-switching: wake silent biosynthetic gene "
                 "clusters with ecological triggers - competitor signals, nutrient stress, co-culture - and "
                 "screen the awakened chemistry, prioritizing uncultured producers. Turn the factories on, "
                 "then listen. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) most antibiotic gene clusters are silent under lab conditions; (2) "
              "they switch on in response to ecological cues; (3) uncultured organisms hold the most novel "
              "chemistry. Reasoning path: the rediscovery wall was a cultivation-and-expression wall, not a "
              "chemistry wall. Genomes show the blueprints are everywhere - Streptomyces genomes carry "
              "twenty-plus clusters but express a few. The missing step is the on-switch: in nature these "
              "clusters fire during competition, starvation, or developmental transitions. So the discovery "
              "platform should be ecological: co-culture producers with competitors, apply the stresses of "
              "their native habitat, and read out chemistry with mass spectrometry, guided by genome mining "
              "to know which silent cluster to watch. Proposed mechanism: build trigger libraries - panels "
              "of ecological cues (competitor supernatants, quorum signals, metal starvation, surface "
              "growth) - applied systematically to strain collections and iChip-cultivated unculturables, "
              "with metabolomics flagging novel products from awakened clusters. What would confirm it: a "
              "pipeline yielding multiple novel scaffolds per year with new mechanisms of action, including "
              "from previously uncultured taxa. What would kill it: awakened clusters producing only "
              "variants of known scaffolds - suggesting truly novel chemistry is exhausted - or triggers "
              "that cannot be found for most clusters. What it does NOT claim: that discovery alone fixes "
              "the broken antibiotic economy, that every cluster yields a drug, or that resistance will not "
              "follow. Where the honest answer is unknown - the full trigger vocabulary per cluster family "
              "- we say so: the libraries must discover it empirically."),
  "key_points": [
   "No new antibiotic class for serious infections has reached patients since the 1980s.",
   "Classic soil screening hit the rediscovery wall: the easy molecules were already found.",
   "Genomes reveal far more antibiotic gene clusters than chemistry ever showed - most silent in the lab.",
   "Teixobactin (2015), from a previously uncultured bacterium, proved novel chemistry remains.",
   "The antibiotic business model is broken: new drugs are used briefly and held in reserve."],
  "requirements": [
   "Build ecological trigger libraries and apply them to strain collections and uncultured producers.",
   "Confirm: pipeline yields multiple novel scaffolds yearly with new mechanisms of action.",
   "Refute: awakened clusters yield only variants of known scaffolds.",
   "Refute: triggers cannot be found for most silent clusters."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim discovery fixes the antibiotic economy or that resistance will not follow.",
   "It must survive the novelty test: scaffolds must be truly new, not rediscoveries."],
  "citations": [CIT_VOID],
 },
 {
  "key": "fmt-mechanism",
  "name": "Why Do Fecal Transplants Work?",
  "group": "Microbiome and Health",
  "ladder_rank": 12, "ladder_tier": "foundations",
  "description": ("For recurrent Clostridioides difficile infection - a gut disease that antibiotics often "
                  "cannot finish - transplanting stool from a healthy donor cures roughly 9 in 10 patients. "
                  "It is the most dramatic microbiome therapy ever demonstrated. And nobody knows why it "
                  "works: which microbes matter, which molecules do the job, or why results are "
                  "inconsistent for every other disease tried."),
  "problem": "What is the actual mechanism by which fecal microbiota transplant cures C. difficile, and why does it fail more often elsewhere?",
  "background": ("Fecal transplant is ancient - fourth-century Chinese medicine used it - but modern proof "
                 "came with van Nood's 2013 randomized trial: donor stool infusion cured 94 percent of "
                 "recurrent C. difficile cases versus 31 percent for antibiotics alone. Hypotheses for the "
                 "mechanism include restoration of bile-acid-converting bacteria (C. difficile spores "
                 "germinate in primary bile acids and are suppressed by secondary ones), nutrient "
                 "competition, direct inhibition by commensals, and immune recalibration. Yet defined "
                 "bacterial cocktails meant to replace donor stool have had mixed results, and the active "
                 "fraction - bacteria, viruses, metabolites, or something else - is unidentified. For "
                 "ulcerative colitis, results are modest and donor-dependent; for obesity and metabolic "
                 "disease, effects are weak and transient. The therapy works brilliantly in one disease and "
                 "mysteriously everywhere else."),
  "why_it_matters": ("Cracking the mechanism turns a crude, donor-dependent procedure into defined, safe, "
                      "manufacturable medicines - and tells us whether the same principles can treat "
                      "inflammatory bowel disease, where patients desperately need options. It is also the "
                      "test case for all microbiome therapeutics: if we cannot explain our one big success, "
                      "the field is guessing."),
  "sig_lens": ("The Signature lens treats donor stool as a sealed toolbox: we know the toolbox fixes the "
               "engine, but we have never inventoried the tools - so we keep shipping the whole heavy box."),
  "sol_public": ("The Signature system proposes mechanism-first deconstruction: fractionate donor material, "
                 "test each fraction's anti-C. difficile activity, and rebuild the minimal effective "
                 "consortium plus its key molecules. Inventory the toolbox, then ship only the tools. Full "
                 "treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) the effect is decomposable into identifiable active agents; (2) "
              "bile-acid conversion is a leading but unproven candidate mechanism; (3) donor variability "
              "reflects variable doses of the active agents. Reasoning path: the field has run the therapy "
              "as a black box because it worked before it was understood. Reverse the order: take highly "
              "effective donor preparations and fractionate - bacteria by taxa, then by function; sterile "
              "filtrates for metabolites and viruses; purified bile-acid profiles. Test each fraction in "
              "standardized C. difficile models, then recombine minimally. The donor-dependence problem "
              "becomes a dosing problem once the actives are known. Proposed mechanism: a fractionation "
              "pipeline from super-donor stool - metagenomic plus metabolomic inventory, activity-guided "
              "fractionation, minimal consortium reconstitution - validated in gnotobiotic mice and then "
              "human trials against whole-stool transplant. What would confirm it: a defined consortium or "
              "molecule set matching whole-stool cure rates, with dose-response and a predictive assay for "
              "donor potency. What would kill it: activity that vanishes on every fractionation - proving "
              "the effect needs the whole undivided community - or defined consortia that work in mice and "
              "fail in humans. What it does NOT claim: that one mechanism fits all diseases, that whole "
              "stool has no advantages, or that defined products will be risk-free. Where the honest answer "
              "is unknown - the active fraction - we say so: the fractionation must find it."),
  "key_points": [
   "Donor stool cures about 9 in 10 recurrent C. difficile cases; antibiotics alone cure about 3 in 10.",
   "Candidate mechanisms: bile-acid conversion, nutrient competition, direct inhibition, immune effects.",
   "The active fraction - bacteria, viruses, metabolites - remains unidentified.",
   "Defined bacterial cocktails have had mixed results; donor stool stays superior.",
   "Results for colitis, obesity, and other conditions are modest and donor-dependent."],
  "requirements": [
   "Fractionate super-donor stool and identify fractions with anti-C. difficile activity.",
   "Confirm: a defined consortium or molecule set matches whole-stool cure rates with dose-response.",
   "Refute: activity vanishes on every fractionation attempted.",
   "Refute: defined consortia work in mice but fail in humans."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim one mechanism fits all diseases or that defined products are risk-free.",
   "It must survive the non-inferiority test: defined products must match whole stool in humans."],
  "citations": [CIT_FMT],
 },
]

CIT_GUTBRAIN = ("Cryan JF, Dinan TG. Mind-altering microorganisms: the impact of the gut microbiota on "
                "brain and behaviour. Nat Rev Neurosci. 2012;13:701-712; Mayer EA et al. Gut microbes "
                "and the brain: paradigm shift in neuroscience. J Neurosci. 2014;34:15490-15496.")
CIT_OBESITY = ("Ley RE et al. Microbial ecology: human gut microbes associated with obesity. Nature. "
               "2006;444:1022-1023; Ridaura VK et al. Gut microbiota from twins discordant for obesity "
               "modulate metabolism in mice. Science. 2013;341:1241214.")
CIT_CENSUS = ("Locey KJ, Lennon JT. Scaling laws predict global microbial diversity. PNAS. "
              "2016;113:5970-5975; Curtis TP et al. Estimating prokaryotic diversity and its limits. "
              "PNAS. 2002;99:10494-10499; Whitman WB et al. Prokaryotes: the unseen majority. PNAS. "
              "1998;95:6578-6583.")
CIT_CPR = ("Hug LA et al. A new view of the tree of life. Nature Microbiology. 2016;1:16048; Rinke C "
           "et al. Insights into the phylogeny and coding potential of microbial dark matter. Nature. "
           "2013;499:431-437; Brown CT et al. Unusual biology across a group comprising more than 15% of "
           "domain Bacteria. Nature. 2015;523:208-211.")
CIT_VDARK = ("Breitbart M, Rohwer F. Here a virus, there a virus, everywhere the same virus? Trends "
             "Microbiol. 2005;13:278-284; Roux S et al. Ecogenomics and potential biogeochemical impacts "
             "of globally abundant ocean viruses. Nature. 2016;537:689-693.")
CIT_GIANT = ("Raoult D, Forterre P. Redefining viruses: lessons from Mimivirus. Nat Rev Microbiol. "
             "2008;6:315-319; Philippe N et al. Pandoraviruses: amoeba viruses with genomes up to 2.5 Mb "
             "reaching that of parasitic eukaryotes. Science. 2013;341:281-286.")

ENTRIES += [
 {
  "key": "gut-brain-axis",
  "name": "How Do Gut Microbes Reach the Brain?",
  "group": "Microbiome and Health",
  "ladder_rank": 13, "ladder_tier": "compounded",
  "description": ("Germ-free mice behave differently: more anxious or less, depending on the study, with "
                  "altered brain chemistry. Probiotics are marketed for mood. The gut-brain axis - the "
                  "two-way conversation between trillions of gut microbes and the brain - is one of the "
                  "hottest ideas in neuroscience. But the actual wires of the conversation, the molecules "
                  "and nerves that carry microbial messages to the brain, remain largely unmapped."),
  "problem": "By what molecular and neural mechanisms do gut microbes influence brain function and behavior?",
  "background": ("The modern gut-brain field grew from germ-free mouse studies in the 2000s-2010s showing "
                 "altered stress responses, neurotransmitter levels, and behavior in microbe-free animals, "
                 "partially normalized by colonization. Candidate routes multiplied: the vagus nerve, which "
                 "carries gut signals to the brainstem and whose cutting abolishes some probiotic effects in "
                 "mice; microbial metabolites such as short-chain fatty acids and tryptophan derivatives "
                 "that enter circulation; immune signaling, since gut microbes train the immune system that "
                 "talks to the brain; and direct neurotransmitter production - gut bacteria make GABA, "
                 "serotonin precursors, and dopamine. Human evidence lags far behind: small trials suggest "
                 "mood effects of probiotics, and Parkinson's and autism show microbial associations, but no "
                 "complete causal chain from microbe to molecule to human brain outcome has been established "
                 "for any condition."),
  "why_it_matters": ("If microbial signals shape mood, anxiety, and neurodegeneration, they are drug targets "
                      "of an entirely new kind - and dietary or probiotic interventions could become "
                      "psychiatry. If the effects are mostly mouse artifacts, a booming industry sells "
                      "placebos. Mapping the real wires decides which future we get."),
  "sig_lens": ("The Signature lens treats the gut-brain axis as a postal system with four possible routes - "
               "nerve, blood, immune, and local - and insists on tracking individual letters, not just "
               "counting mailbags."),
  "sol_public": ("The Signature system proposes molecule-first mapping: trace specific microbial products "
                 "from gut to brain receptor in living animals, then test each route by blocking it. Follow "
                 "the letters through the postal system. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) real microbial effects on the brain travel by identifiable "
              "molecules or nerves; (2) mouse findings partially translate but need human validation; (3) "
              "multiple routes operate simultaneously. Reasoning path: the field correlates microbial "
              "communities with behaviors - mailbags with moods. The fix is postal tracking: pick one "
              "candidate molecule (say, a specific tryptophan metabolite), label it, and follow it from "
              "microbial production through absorption, circulation, blood-brain barrier crossing, to "
              "receptor binding - then block each step and watch the behavior change. Do this route by route: "
              "vagotomy for the nerve route, receptor knockouts for the blood route, immune depletion for "
              "the immune route. Only routes surviving blockade tests count as real wires. Proposed "
              "mechanism: a gut-brain wire atlas - for each major microbial metabolite class, complete "
              "pharmacokinetic tracing plus stepwise blockade in standardized behavioral models, then "
              "human validation via labeled-metabolite imaging and vagus-nerve studies. What would confirm "
              "it: complete traced routes - molecule to receptor to behavior - that survive blockade and "
              "replicate in humans, yielding druggable targets. What would kill it: effects that vanish "
              "under every blockade - proving the axis is an emergent community property with no "
              "traceable wires - or human studies showing zero translation of mouse routes. What it does "
              "NOT claim: that probiotics work, that any human condition is microbially caused, or that "
              "mice predict humans. Where the honest answer is unknown - which routes are real in humans - "
              "we say so: the human tracing must be done."),
  "key_points": [
   "Germ-free mice show altered behavior and brain chemistry, partially normalized by colonization.",
   "Candidate routes: vagus nerve, circulating metabolites, immune signaling, microbial neurotransmitters.",
   "Vagus nerve cutting abolishes some probiotic behavioral effects in mice.",
   "Human evidence is thin: small mood trials, disease associations, no complete causal chain.",
   "No microbe-to-molecule-to-human-brain pathway is fully established for any condition."],
  "requirements": [
   "Trace candidate molecules from microbial production to brain receptor with stepwise blockade.",
   "Confirm: traced routes survive blockade, replicate in humans, and yield druggable targets.",
   "Refute: behavioral effects vanish under every route blockade attempted.",
   "Refute: human studies show zero translation of established mouse routes."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim probiotics work or that mice predict human outcomes.",
   "It must survive the blockade test: each claimed wire must break when cut."],
  "citations": [CIT_GUTBRAIN],
 },
 {
  "key": "obesity-microbes",
  "name": "Do Gut Microbes Cause Obesity?",
  "group": "Microbiome and Health",
  "ladder_rank": 14, "ladder_tier": "compounded",
  "description": ("Obese mice carry different gut microbes than lean mice - and transplanting the obese "
                  "microbes into germ-free mice makes the recipients gain more fat. The 2006 discovery "
                  "electrified medicine: maybe obesity is partly a microbial disease. Two decades later the "
                  "human picture is murky, the famous bacterial ratio failed replication, and nobody can say "
                  "whether microbes cause human obesity or merely follow it."),
  "problem": "Do gut microbes causally contribute to human obesity, or do they only reflect diet and weight?",
  "background": ("Jeffrey Gordon's group showed in 2006 that obese mice have a shifted gut community and "
                 "that transplanting it transfers extra fat gain to germ-free recipients. The proposed "
                 "mechanism was energy harvest: obese-type microbes extract more calories from food. Human "
                 "studies found associations - including the Firmicutes-to-Bacteroidetes ratio - but large "
                 "cohorts failed to replicate the ratio (Sze and Schloss 2016), and effects shrank once diet "
                 "was controlled. Ridaura's 2013 twin study was the strongest human evidence: microbes from "
                 "the obese twin made mice fatter than microbes from the lean twin, and co-housing "
                 "transferred the lean protection. Yet human fecal transplants for obesity have shown weak, "
                 "transient metabolic effects at best. Diet confounds everything: it changes both weight "
                 "and microbes simultaneously, and no study has fully separated the two in humans."),
  "why_it_matters": ("Obesity affects hundreds of millions and drives diabetes, heart disease, and cancer. "
                      "If microbes are causal levers, they offer therapies beyond diet and willpower - "
                      "probiotics, targeted antimicrobials, microbial metabolites as drugs. If they are "
                      "passengers, the field must stop promising microbial weight-loss cures."),
  "sig_lens": ("The Signature lens treats the obesity-microbe link as a thermostat question: do microbes "
               "set the temperature, or does the room's heat merely rattle the thermostat's casing?"),
  "sol_public": ("The Signature system proposes diet-clamped causation trials: fix diet exactly, vary only "
                 "the microbes, and measure weight - in humans, not just mice. Hold the room's heat constant "
                 "and watch the thermostat. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) diet confounds every observational obesity-microbiome study; (2) "
              "mouse transfer proves possibility, not human causality; (3) real causal microbes must work "
              "through measurable energy or signaling mechanisms. Reasoning path: the field keeps comparing "
              "free-living obese and lean people who eat differently - the room's heat is never held "
              "constant. The decisive design is diet-clamped: house volunteers in metabolic wards on "
              "identical controlled diets, then vary only the microbiome - via defined consortia, targeted "
              "depletion, or transplant - and measure energy harvest by bomb calorimetry of food and stool "
              "plus weight and metabolic outcomes. If microbes matter independently of diet, the effect must "
              "appear with diet fixed. Proposed mechanism: run diet-clamped human trials testing defined "
              "microbial interventions, with energy-balance chambers measuring exactly where calories go, "
              "paired with mechanistic work on candidate pathways (short-chain fatty acids, bile acids, "
              "gut-brain satiety signals). What would confirm it: diet-fixed weight or energy-harvest "
              "differences from microbial interventions alone, with an identified molecular mechanism. What "
              "would kill it: zero microbial effect under strict diet control across multiple interventions "
              "- proving microbes are passengers - or effects that always vanish when calories are "
              "precisely matched. What it does NOT claim: that diet does not matter, that mouse work was "
              "wrong, or that a microbial obesity cure exists. Where the honest answer is unknown - whether "
              "any human effect survives diet clamping - we say so: the wards must be run."),
  "key_points": [
   "Obese mouse microbes transplanted into germ-free mice transfer extra fat gain (2006).",
   "Proposed mechanism: obese-type communities harvest more energy from food.",
   "The famous Firmicutes-to-Bacteroidetes ratio failed replication in large human cohorts.",
   "Twin studies show lean microbes can protect mice; human transplants show weak, transient effects.",
   "Diet changes both weight and microbes simultaneously, confounding every observational study."],
  "requirements": [
   "Run diet-clamped human trials: identical diets, varied microbes, measured energy harvest.",
   "Confirm: microbial interventions change weight or energy harvest with diet fixed, via identified mechanism.",
   "Refute: zero microbial effect under strict diet control across multiple interventions.",
   "Refute: effects always vanish when calories are precisely matched."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim diet is irrelevant or that a microbial cure exists.",
   "It must survive the clamp test: diet must be truly fixed, not self-reported."],
  "citations": [CIT_OBESITY],
 },
 {
  "key": "microbial-census",
  "name": "How Many Microbial Species Exist?",
  "group": "The Uncultured Majority",
  "ladder_rank": 15, "ladder_tier": "compounded",
  "description": ("How many kinds of microbes live on Earth? Estimates range from millions to trillions - a "
                  "spread so wide it is barely an estimate at all. In 2016, Locey and Lennon applied scaling "
                  "laws and arrived at roughly one trillion microbial species, of which science has named "
                  "perhaps a hundred thousand. The census of Earth's dominant life forms is the most "
                  "uncertain headcount in biology."),
  "problem": "How many microbial species exist on Earth, and how can we count organisms we cannot see or grow?",
  "background": ("Early estimates were humble: a few million, extrapolated from known-to-unknown ratios. "
                 "Whitman and colleagues in 1998 estimated about 10^30 microbial cells on Earth - the "
                 "\"unseen majority\" - but species counts stayed speculative. Curtis and colleagues (2002) "
                 "used log-normal species abundance models to argue for vast diversity. Then Locey and "
                 "Lennon (2016) combined massive sequencing datasets with ecological scaling laws - the "
                 "relationship between total individuals and species richness - and predicted around 10^12 "
                 "microbial taxa on Earth. Critics noted the scaling laws were calibrated on larger "
                 "organisms and that sequencing error inflates rare-species counts. Meanwhile only about "
                 "20,000 bacterial species have valid published names. The gap between named species and "
                 "predicted species spans seven orders of magnitude."),
  "why_it_matters": ("You cannot protect, study, or use what you cannot count. The census sets the scale of "
                      "microbial dark matter, guides how much sequencing is enough, and tells biotechnology "
                      "how large the unexplored gene pool is. A trillion species means the genomic "
                      "revolution has sampled a rounding error."),
  "sig_lens": ("The Signature lens treats the census as a mapmaker's problem: we are estimating the number "
               "of islands on Earth by counting the ones near shore and extrapolating the fog beyond."),
  "sol_public": ("The Signature system proposes calibrating the extrapolation directly: exhaustively census "
                 "small closed volumes - a liter of seawater, a gram of soil - with error-proof sequencing, "
                 "then scale up with measured, not assumed, laws. Map the shoreline before guessing the "
                 "fog. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) current trillion-scale estimates rest on uncalibrated scaling laws; "
              "(2) sequencing error inflates rare-species counts; (3) small volumes can be censused "
              "near-exhaustively. Reasoning path: every global estimate extrapolates from local samples "
              "using assumed mathematical laws. The fix is to measure the extrapolation itself: take "
              "nested volumes - milliliters, liters, cubic meters of one habitat - and census each to "
              "saturation with high-accuracy long-read sequencing plus single-cell genomics, controlling "
              "error with spike-in standards. Plot the real species-volume curve for microbes the way "
              "ecologists did for plants, then extend it with measured confidence instead of borrowed "
              "laws. Proposed mechanism: a census calibration campaign across representative habitats "
              "(open ocean, soil, deep subsurface, animal guts), each with nested-volume saturation "
              "curves and error quantification, feeding a new generation of estimates with honest "
              "uncertainty bars. What would confirm it: measured curves converging on consistent global "
              "estimates with quantified uncertainty, and scaling laws validated or corrected for "
              "microbes. What would kill it: saturation proving unreachable - diversity rising without "
              "limit at every scale - which would make any finite estimate meaningless, or error "
              "correction collapsing most \"rare species\" into artifacts. What it does NOT claim: that "
              "the answer is near one trillion, that all predicted species are real, or that naming them "
              "all is feasible. Where the honest answer is unknown - the true global number - we say so: "
              "the calibration campaign must measure it."),
  "key_points": [
   "Estimates of Earth's microbial species span millions to trillions - barely an estimate at all.",
   "Locey and Lennon (2016) used scaling laws to predict roughly one trillion microbial taxa.",
   "Only about 20,000 bacterial species have valid published names - a seven-order-of-magnitude gap.",
   "Critics warn scaling laws were calibrated on larger organisms and sequencing error inflates counts.",
   "Whitman et al. (1998) established microbes as Earth's unseen majority by cell count."],
  "requirements": [
   "Census nested volumes to saturation with error-controlled sequencing across representative habitats.",
   "Confirm: measured species-volume curves converge on consistent global estimates with quantified uncertainty.",
   "Refute: diversity rises without limit at every scale, making finite estimates meaningless.",
   "Refute: error correction collapses most rare species into sequencing artifacts."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim the trillion estimate is right or that naming all species is feasible.",
   "It must survive the error test: rare species must be distinguished from sequencing noise."],
  "citations": [CIT_CENSUS],
 },
 {
  "key": "candidate-phyla",
  "name": "Microbial Dark Matter: The Candidate Phyla",
  "group": "The Uncultured Majority",
  "ladder_rank": 16, "ladder_tier": "compounded",
  "description": ("DNA surveys of the environment keep finding the same embarrassment: enormous branches of "
                  "the tree of life with no cultured member, no photograph, no known lifestyle - some "
                  "accounting for a large fraction of all bacterial diversity. The Candidate Phyla "
                  "Radiation alone may comprise over 15 percent of bacterial domain diversity. We know "
                  "their genes; we do not know what they do for a living."),
  "problem": "What do the uncultured candidate phyla - possibly a large fraction of all bacterial diversity - actually do in nature?",
  "background": ("The dark matter emerged from 16S rRNA surveys in the 1990s-2000s: sequences clustering "
                 "into deep branches with no cultured relatives, given placeholder names like OP11, OD1, "
                 "TM7. Single-cell genomics (Rinke 2013) and metagenomic binning finally produced genomes "
                 "for these ghosts. Hug and colleagues' 2016 tree of life showed the Candidate Phyla "
                 "Radiation - tiny-genomed, tiny-celled bacteria - expanding bacterial diversity "
                 "dramatically. Brown and colleagues (2015) found CPR organisms with minimal genomes "
                 "lacking basic biosynthetic pathways, suggesting symbiotic or parasitic lifestyles. Yet "
                 "almost none have been seen alive doing anything: their hosts are unknown, their "
                 "metabolism is inferred from incomplete genomes, and their ecological roles - abundant in "
                 "groundwater, sediments, and even the human mouth - remain guesses."),
  "why_it_matters": ("If a large fraction of bacterial diversity is symbiotic dark matter, our picture of "
                      "microbial ecology is missing its biggest chapter - and our models of nutrient cycles, "
                      "which assume free-living microbes doing known chemistry, may be systematically "
                      "wrong. Their streamlined genomes may also hold minimal-life blueprints for synthetic "
                      "biology."),
  "sig_lens": ("The Signature lens treats candidate phyla as tenants, not homeowners: organisms that gave "
               "up independence for a room inside someone else's metabolism - and we keep looking for "
               "their houses instead of their landlords."),
  "sol_public": ("The Signature system proposes host-first discovery: find candidate-phyla cells physically "
                 "attached to hosts with imaging, then co-culture the pair. Stop hunting houses; find the "
                 "landlords. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) tiny CPR genomes lacking biosynthesis imply obligate dependence on "
              "other cells; (2) physical association in the environment reveals the host; (3) pairs can be "
              "co-cultured even when individuals cannot. Reasoning path: we have tried to culture these "
              "organisms as isolates and failed for decades - exactly what obligate symbionts would do. "
              "The genomes themselves are the clue: missing amino-acid and nucleotide synthesis means "
              "someone else provides them. So the discovery unit is the partnership. Use fluorescence in "
              "situ hybridization with CPR-specific probes plus super-resolution microscopy to find what "
              "cells they touch in groundwater, sediment, and oral biofilms; then use optical tweezers or "
              "microfluidics to isolate attached pairs and grow them together. Proposed mechanism: a "
              "host-mapping campaign - imaging-based partner identification for major CPR lineages, "
              "followed by pair co-culture and metabolic handoff mapping (who feeds whom what), building "
              "the first symbiosis network of microbial dark matter. What would confirm it: reproducible "
              "host partnerships with demonstrated metabolic exchange, and co-cultures that finally grow "
              "dark-matter lineages. What would kill it: CPR cells found living fully independently with "
              "complete metabolisms after all - genome incompleteness was the artifact - or partners that "
              "cannot be co-cultured by any method. What it does NOT claim: that all dark matter is "
              "symbiotic, that every CPR has one host, or that free-living CPR do not exist. Where the "
              "honest answer is unknown - the host map - we say so: the imaging must draw it."),
  "key_points": [
   "Environmental DNA reveals deep bacterial branches with no cultured members and no known lifestyle.",
   "The Candidate Phyla Radiation may comprise over 15 percent of bacterial domain diversity.",
   "CPR genomes are tiny and lack basic biosynthetic pathways, suggesting symbiotic lifestyles.",
   "They are abundant in groundwater, sediments, and the human mouth - yet almost never seen alive.",
   "Ecological roles are inferred from incomplete genomes, not observed."],
  "requirements": [
   "Image CPR cells in situ to identify physical host partners for major lineages.",
   "Confirm: reproducible partnerships with demonstrated metabolic exchange and successful pair co-cultures.",
   "Refute: CPR cells living independently with complete metabolisms - genomes were the artifact.",
   "Refute: identified partners cannot be co-cultured by any method."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim all dark matter is symbiotic or that free-living CPR do not exist.",
   "It must survive the exchange test: partnerships must show real metabolic handoffs, not just proximity."],
  "citations": [CIT_CPR],
 },
 {
  "key": "viral-dark-matter",
  "name": "Viral Dark Matter",
  "group": "Viral Dark Matter",
  "ladder_rank": 17, "ladder_tier": "compounded",
  "description": ("Sequence all the virus-like particles in a liter of seawater and most of the sequences "
                  "match nothing in any database - not any known virus, not any known gene. This is viral "
                  "dark matter: the virosphere is Earth's largest genetic reservoir, and the overwhelming "
                  "majority of it is unidentified. We are surrounded by an ocean of viruses we cannot name."),
  "problem": "What are the millions of unidentified viral sequences in every environment - and what do they infect?",
  "background": ("The dark matter appeared when metagenomics reached viruses: Breitbart and Rohwer showed "
                 "in 2005 that most viral metagenome sequences had no database matches, a pattern repeated "
                 "in every environment since - oceans, soils, guts, even the air. The problem compounds "
                 "because viruses have no universal marker gene like bacterial 16S rRNA; each discovery "
                 "method finds a different slice. Roux and colleagues (2016) used large-scale ocean "
                 "surveys to assemble thousands of viral genomes, yet unknowns still dominated. Linking "
                 "viruses to hosts is the hardest part: CRISPR spacers, tRNA matches, and co-occurrence "
                 "give hints, but most viral dark matter floats hostless. The unknown virosphere may "
                 "outnumber known viruses by orders of magnitude."),
  "why_it_matters": ("Viruses kill an estimated 20 percent of ocean microbes daily, shunting carbon through "
                      "ecosystems; unknown viruses may control unknown processes. Viral dark matter also "
                      "hides potential phage therapies, gene-transfer agents shaping evolution, and possibly "
                      "pathogens. We cannot manage what we cannot identify."),
  "sig_lens": ("The Signature lens treats viral dark matter as an uncatalogued postal fleet: trillions of "
               "delivery vehicles whose senders, recipients, and cargo are all unknown - and the catalog "
               "must start with who receives the mail."),
  "sol_public": ("The Signature system proposes host-first virology at scale: link every viral sequence to "
                 "its host with single-virus genomics plus CRISPR-spacer matching, then read the cargo. "
                 "Find the recipients to identify the fleet. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) most dark-matter viruses infect abundant, often uncultured hosts; "
              "(2) host linkage is the key that unlocks function; (3) single-virus methods can scale. "
              "Reasoning path: a viral sequence without a host is a letter without an address - "
              "uninterpretable. But hosts keep records: CRISPR spacer arrays are mugshots of past viral "
              "attackers, and single-cell genomics can catch viruses inside their hosts red-handed. The "
              "program: sort single virus particles, sequence them individually, and match each to hosts "
              "via CRISPR spacers, integrated proviruses, and co-occurrence across samples - building a "
              "host-virus map for whole environments. Then read function from host context: a virus of a "
              "methanogen matters differently than a virus of a cyanobacterium. Proposed mechanism: a "
              "global host-virus mapping campaign - standardized single-virus genomics across oceans, "
              "soils, and guts, with automated host assignment and cargo annotation, feeding an open atlas "
              "of who infects whom. What would confirm it: host assignments for the majority of abundant "
              "viral populations and validated predictions of viral ecological roles. What would kill it: "
              "viral populations with no detectable host signal by any method - true orphans - dominating "
              "the data, or host assignments that never validate experimentally. What it does NOT claim: "
              "that every virus will be linked, that databases will ever be complete, or that all dark "
              "matter is ecologically important. Where the honest answer is unknown - the host map - we say "
              "so: the campaign must draw it."),
  "key_points": [
   "Most viral metagenome sequences match nothing in any database, in every environment tested.",
   "Viruses lack a universal marker gene, so each method samples a different slice of the virosphere.",
   "Linking viruses to hosts is the hardest step; most dark matter floats hostless.",
   "Ocean viruses kill an estimated 20 percent of marine microbes daily.",
   "The unknown virosphere may outnumber known viruses by orders of magnitude."],
  "requirements": [
   "Build host-virus maps via single-virus genomics plus CRISPR-spacer matching across environments.",
   "Confirm: host assignments for most abundant viral populations with validated ecological roles.",
   "Refute: true orphan viruses with no host signal dominate despite exhaustive methods.",
   "Refute: host assignments systematically fail experimental validation."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim every virus will be linked or that databases will ever be complete.",
   "It must survive the validation test: assignments must be confirmed, not just computed."],
  "citations": [CIT_VDARK],
 },
 {
  "key": "giant-viruses",
  "name": "Giant Viruses: What Are They?",
  "group": "Viral Dark Matter",
  "ladder_rank": 18, "ladder_tier": "compounded",
  "description": ("In 2003, researchers studying a pneumonia outbreak found something in amoebae that looked "
                  "like a bacterium under the microscope - but it was a virus, Mimivirus, with a genome "
                  "larger than some bacteria and genes for translation once thought exclusive to cellular "
                  "life. Then came pandoraviruses with genomes reaching 2.5 million bases. Giant viruses "
                  "shattered the definition of \"virus\" - and raised the question of what they really are."),
  "problem": "What are giant viruses - degraded cells, a fourth domain of life, or something else entirely?",
  "background": ("Mimivirus was initially mistaken for a Gram-positive bacterium because its 400-nanometer "
                 "particle stains like one; its 1.2-megabase genome held nearly a thousand genes including "
                 "aminoacyl-tRNA synthetases. Pandoraviruses (Philippe 2013) pushed genomes to 2.5 "
                 "megabases, larger than some parasitic eukaryotes - though most of their genes match "
                 "nothing known. Two camps formed. The reduction camp, led by Eugene Koonin, argues giant "
                 "viruses evolved from smaller viruses by gene accretion, or from cells by reductive "
                 "evolution - no fourth domain needed. The fourth-domain camp, including Jean-Michel "
                 "Claverie and Didier Raoult, points to deep-branching translation genes suggesting giant "
                 "viruses descend from an ancient cellular lineage that became parasitic. Phylogenies of "
                 "the shared genes give conflicting answers depending on the genes and methods chosen."),
  "why_it_matters": ("If giant viruses are a fourth domain, textbooks gain a branch of life and the tree "
                      "of life gets rewritten; if they are overgrown ordinary viruses, the episode is a "
                      "lesson in how definitions fail. Either way, their mostly-unknown genes are a "
                      "treasure chest - pandoravirus genomes are over 90 percent ORFans with no known "
                      "function."),
  "sig_lens": ("The Signature lens treats giant viruses as castles with unknown rooms: whether the castle "
               "was built big or shrank from a city matters less than mapping the rooms - the genes - "
               "because the rooms are where the treasure is."),
  "sol_public": ("The Signature system proposes function-first giant virology: systematically determine "
                 "what the thousands of unknown giant-virus genes do, and let the functions - not the "
                 "phylogenies - reveal what these entities are. Map the rooms; the architecture will "
                 "follow. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) gene function is more informative than disputed phylogenies; (2) "
              "most giant-virus genes are currently ORFans with no known function; (3) functions reveal "
              "lifestyle, and lifestyle reveals origin. Reasoning path: the fourth-domain debate has "
              "stalled because both camps can cherry-pick genes supporting their tree. Functions do not "
              "lie as easily: if the unknown genes turn out to encode a coherent cellular-like "
              "physiology - energy metabolism, division machinery - the reduction story weakens; if they "
              "encode mostly host-manipulation and viral processes, the accretion story wins. The program: "
              "high-throughput functional screening of giant-virus ORFans - expression, structure "
              "prediction, interaction mapping, knockout in cultivable giant-virus systems - building the "
              "first functional atlas of a pandoravirus. Proposed mechanism: a giant-virus function "
              "initiative - prioritized ORFan characterization pipelines, amoeba infection models with "
              "reporter systems, and comparative atlases across Mimiviridae and Pandoraviridae. What would "
              "confirm it: functional patterns decisively favoring one origin story, or a novel biology "
              "fitting neither - either would be progress. What would kill it: functions proving "
              "uncharacterizable at scale - genes with no detectable activity in any assay - leaving the "
              "debate exactly where it stands. What it does NOT claim: that phylogeny is useless, that one "
              "study settles a domain of life, or that all giant viruses share one origin. Where the honest "
              "answer is unknown - what 90 percent of pandoravirus genes do - we say so: the screens must "
              "find out."),
  "key_points": [
   "Mimivirus (2003) was first mistaken for a bacterium; its genome exceeds some bacteria.",
   "Pandoraviruses reach 2.5-megabase genomes, larger than some parasitic eukaryotes.",
   "Over 90 percent of pandoravirus genes match nothing known - pure genetic dark matter.",
   "The fourth-domain camp sees an ancient cellular lineage; the reduction camp sees overgrown viruses.",
   "Shared-gene phylogenies give conflicting answers depending on genes and methods."],
  "requirements": [
   "Build functional atlases of giant-virus ORFans via high-throughput screening.",
   "Confirm: functional patterns decisively favor one origin story or reveal a novel biology.",
   "Refute: ORFans prove uncharacterizable at scale in every assay attempted.",
   "Refute: functions split evenly with no coherent pattern favoring any story."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim phylogeny is useless or that all giant viruses share one origin.",
   "It must survive the function test: assays must detect real activities, not artifacts."],
  "citations": [CIT_GIANT],
 },
]

CIT_VIRORIGIN = ("Forterre P. The origin of viruses and their possible roles in major evolutionary "
                 "transitions. Virus Res. 2006;117:5-16; Krupovic M, Koonin EV. Multiple origins of viral "
                 "capsid proteins from cellular ancestors. PNAS. 2007;104:14285-14290.")
CIT_PHAGE = ("Ptashne M. A Genetic Switch: Phage Lambda Revisited. 3rd ed. Cold Spring Harbor "
             "Laboratory Press; 2004; Erez Z et al. Communication between viruses guides lysis-lysogeny "
             "decisions. Nature. 2017;541:488-493.")
CIT_ANCIENTR = ("DCosta VM et al. Antibiotic resistance is ancient. Nature. 2011;477:457-461; Bhullar K "
                "et al. Antibiotic resistance is prevalent in an isolated cave microbiome. PLoS One. "
                "2012;7:e34953.")
CIT_REVERSE = ("Andersson DI, Hughes D. Antibiotic resistance and its cost: is it possible to reverse "
               "resistance? Nat Rev Microbiol. 2010;8:260-271; Sommer MOA et al. Functional "
               "characterization of the antibiotic resistance reservoir in the human microflora. Science. "
               "2009;325:1128-1131.")
CIT_EUKORIGIN = ("Spang A et al. Complex archaea that bridge the gap between prokaryotes and eukaryotes. "
                 "Nature. 2015;521:173-179; Zaremba-Niedzwiedzka K et al. Asgard archaea illuminate the "
                 "origin of eukaryotic cellular complexity. Nature. 2017;541:353-358; Martin WF et al. "
                 "Endosymbiotic theories for eukaryote origin. Philos Trans R Soc B. 2015;370:20140330.")
CIT_MITOFIRST = ("Lane N, Martin W. The energetics of genome complexity. Nature. 2010;467:929-934; Pittis "
                 "AA, Gabaldon T. Late acquisition of mitochondria by a host with chimaeric prokaryotic "
                 "ancestry. Nature. 2016;531:101-104.")

ENTRIES += [
 {
  "key": "virus-origins",
  "name": "Where Did Viruses Come From?",
  "group": "Viral Dark Matter",
  "ladder_rank": 19, "ladder_tier": "compounded",
  "description": ("Every living thing has viruses - bacteria, archaea, plants, animals, even other viruses. "
                  "They must be ancient. But did viruses come before cells, escape from cells, or shrink "
                  "from cells? Three rival origin stories compete, each with evidence, and the deepest "
                  "question in virology - what viruses fundamentally are - has no agreed answer."),
  "problem": "What is the evolutionary origin of viruses: did they predate cells, escape from cells, or degenerate from cells?",
  "background": ("Three hypotheses dominate. Virus-first says self-replicating RNA molecules in the "
                 "pre-cellular world became viruses before cells existed - supported by RNA viruses that "
                 "may preserve that ancient world. Escape (or progressive) says viruses are runaway genes "
                 "- pieces of cellular genomes that learned to travel - supported by the patchwork of "
                 "cellular genes in many viral genomes. Reduction (or regressive) says viruses were once "
                 "cells that shed everything but replication - supported by giant viruses with "
                 "cellular-like genes. Krupovic and Koonin (2007) showed viral capsid proteins trace to a "
                 "small set of ancient folds, suggesting a few deep viral lineages rather than countless "
                 "independent origins - but whether those lineages predate the last universal common "
                 "ancestor is unknown. Patrick Forterre proposed viruses drove major transitions, even the "
                 "origin of DNA itself. No hypothesis explains all viruses; different virus groups may "
                 "have different origins."),
  "why_it_matters": ("Virus origins touch the origin of life itself: if viruses predate cells, they are "
                      "witnesses to life's beginning and may have invented DNA. The answer also guides "
                      "pandemic prediction - escaped genes behave differently than ancient parasites - and "
                      "decides whether a universal virus taxonomy is even possible."),
  "sig_lens": ("The Signature lens treats the three hypotheses as three doors into the same dark building: "
               "different virus families may have entered through different doors, and insisting on one "
               "door for all is the error."),
  "sol_public": ("The Signature system proposes polyphyletic origins tested per lineage: reconstruct each "
                 "major viral lineage's history independently with capsid-fold phylogenies plus host-range "
                 "fossils, and stop demanding one origin for all viruses. Different doors for different "
                 "families. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) \"viruses\" may be several independently originated groups, not "
              "one; (2) capsid protein folds preserve the deepest history; (3) host genomes contain fossil "
              "records of ancient infections. Reasoning path: the debate stalls because each camp defends "
              "its hypothesis for ALL viruses. Drop the monophyly assumption. Reconstruct origins "
              "lineage by lineage: for each major viral realm, build phylogenies from the ancient capsid "
              "folds, date them against host divergences, and mine host genomes for endogenous viral "
              "elements as fossils. Some lineages may resolve as pre-cellular (virus-first), others as "
              "escaped genes, others as reduced cells - and a mixed answer is still an answer. Proposed "
              "mechanism: a per-realm origin atlas - standardized deep-phylogeny plus endogenous-element "
              "fossil dating for each ICTV viral realm, with explicit tests of the three hypotheses per "
              "realm. What would confirm it: realms sorting cleanly into different origin stories with "
              "dated, fossil-supported histories. What would kill it: all realms converging on one origin "
              "- which would actually resolve the debate the other way - or deep phylogenies proving "
              "unresolvable, with signal erased beyond recovery. What it does NOT claim: that every "
              "virus's origin is knowable, that the three hypotheses exhaust the possibilities, or that "
              "origins predict future pandemics. Where the honest answer is unknown - the deep dates - we "
              "say so: the fossils must be found and dated."),
  "key_points": [
   "Three rival hypotheses: virus-first (before cells), escape (runaway genes), reduction (degenerate cells).",
   "Viral capsid proteins trace to a small set of ancient folds - a few deep lineages, not countless origins.",
   "Forterre proposed viruses may have invented DNA and driven major evolutionary transitions.",
   "Host genomes contain endogenous viral elements - fossils of ancient infections.",
   "No single hypothesis explains all viruses; different groups may have different origins."],
  "requirements": [
   "Build per-realm origin atlases: deep capsid-fold phylogenies plus fossil dating.",
   "Confirm: viral realms sort into distinct origin stories with dated, fossil-supported histories.",
   "Refute: all realms converge on a single origin - resolving the debate monophyletically.",
   "Refute: deep phylogenetic signal proves erased beyond recovery for every realm."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim every origin is knowable or that origins predict pandemics.",
   "It must survive the fossil test: endogenous elements must date consistently with the phylogenies."],
  "citations": [CIT_VIRORIGIN],
 },
 {
  "key": "phage-decision",
  "name": "The Phage Decision: Lysis or Lysogeny?",
  "group": "Viral Dark Matter",
  "ladder_rank": 20, "ladder_tier": "compounded",
  "description": ("A temperate phage infecting a bacterium faces a choice: explode the cell now and release "
                  "hundreds of copies, or slip quietly into the genome and wait. The lambda phage switch is "
                  "the best-studied decision circuit in biology - yet in real environments, with real "
                  "bacterial communities, we still cannot predict which choice phages will make, or why "
                  "entire viromes seem to shift strategies with conditions."),
  "problem": "What controls the lysis-versus-lysogeny decision in natural environments, and can we predict or steer it?",
  "background": ("Mark Ptashne's work on phage lambda revealed the genetic switch: the cI repressor "
                 "maintains silent lysogeny, Cro triggers lytic explosion, and the circuit integrates "
                 "signals about cell health. In the lab the decision is well mapped. In nature it is not: "
                 "metagenomic surveys show lysogeny dominating in some environments and lysis in others, "
                 "with shifts that do not match lab rules. The 2017 discovery of the arbitrium system - "
                 "phages communicating with peptide signals to coordinate lysis-lysogeny choices across "
                 "infections (Erez 2017) - revealed phages as social decision-makers, not lone circuits. "
                 "Yet for the vast uncultured virosphere, we have no idea what fraction is temperate, what "
                 "signals they read, or what flips whole communities between strategies. This matters "
                 "because lysogenic phages carry toxin and resistance genes, waking them can release "
                 "pathogens' weapons, and phage therapy depends on strictly lytic phages."),
  "why_it_matters": ("The decision controls bacterial mortality in every ecosystem, the spread of toxins "
                      "and resistance genes by temperate phages, and the safety of phage therapy - a "
                      "lysogenic phage in a therapeutic cocktail can donate dangerous genes instead of "
                      "killing. Predicting the switch is prerequisite to managing the virosphere."),
  "sig_lens": ("The Signature lens treats the phage decision as a vote, not a reflex: each phage polls "
               "its neighbors through chemical ballots, and the election rules - not the individual voter "
               "- decide the outcome."),
  "sol_public": ("The Signature system proposes election-rule mapping: catalog the communication signals "
                 "phages use to coordinate decisions, then predict community strategy from signal "
                 "landscapes. Read the ballots to forecast the vote. Full treatment: the Signature edition "
                 "record."),
  "sol_sig": (LABEL + " Assumptions: (1) many temperate phages integrate social signals, not just cell "
              "state; (2) signal landscapes differ systematically between environments; (3) decisions are "
              "predictable from signals plus host physiology. Reasoning path: lambda's circuit was "
              "decoded in pure culture - one phage, one cell type, no neighbors. Nature adds the "
              "electorate: arbitrium peptides, host quorum signals, nutrient status, co-infecting phages. "
              "The predictive model must therefore be ecological: measure the signal landscape of an "
              "environment (peptide signals, host density, growth state), and forecast the community's "
              "lysis-lysogeny balance from it. Then steer it: adding synthetic arbitrium signals should "
              "push communities toward lysogeny, useful for keeping therapeutic phages lytic or keeping "
              "toxin phages asleep. Proposed mechanism: build signal-decision maps - for model temperate "
              "phages, dose-response surfaces of lysis probability across signal combinations, then "
              "metagenomic surveys testing whether environmental signal landscapes predict community "
              "strategy, then steering trials in bioreactors. What would confirm it: signal landscapes "
              "predicting lysis-lysogeny ratios in new environments, and synthetic signals steering "
              "communities as predicted. What would kill it: decisions proving dominated by unmeasurable "
              "intracellular noise, or environments where signals exist but predict nothing. What it does "
              "NOT claim: that all phages are social, that lambda's circuit generalizes, or that steering "
              "is clinically ready. Where the honest answer is unknown - the signal vocabulary of the "
              "uncultured virosphere - we say so: it must be discovered, not assumed."),
  "key_points": [
   "Phage lambda's cI/Cro switch is the best-mapped decision circuit in biology - in the lab.",
   "Natural lysis-lysogeny balances do not match lab rules and shift unpredictably.",
   "The 2017 arbitrium discovery showed phages communicating to coordinate decisions socially.",
   "Lysogenic phages carry toxin and resistance genes; waking them can arm pathogens.",
   "Phage therapy requires strictly lytic phages - misjudging the switch is dangerous."],
  "requirements": [
   "Map signal-decision surfaces for model temperate phages across signal combinations.",
   "Confirm: environmental signal landscapes predict community lysis-lysogeny ratios in new environments.",
   "Refute: decisions dominated by unmeasurable intracellular noise in all systems tested.",
   "Refute: signals present but predicting nothing across environments."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim all phages are social or that steering is clinically ready.",
   "It must survive the prediction test: forecasts must work in new environments, not just fitted ones."],
  "citations": [CIT_PHAGE],
 },
 {
  "key": "ancient-resistome",
  "name": "Ancient Resistance: The 30,000-Year-Old Resistome",
  "group": "Antibiotic Resistance",
  "ladder_rank": 21, "ladder_tier": "compounded",
  "description": ("In 2011, researchers drilled into 30,000-year-old permafrost and found something "
                  "startling: bacteria carrying resistance genes against modern antibiotics - vancomycin, "
                  "tetracycline, beta-lactams - tens of millennia before humans invented the drugs. "
                  "Resistance is ancient. But if these genes existed long before medicine, what were they "
                  "for - and what does their age mean for our fight against them?"),
  "problem": "What was the original function of antibiotic resistance genes that predate human antibiotic use by tens of millennia?",
  "background": ("D'Costa and colleagues' 2011 Nature paper analyzed permafrost DNA and cultured ancient "
                 "bacteria, finding a diverse resistome - efflux pumps, modifying enzymes, target "
                 "protection - effective against modern drugs. Isolated cave microbiomes cut off for "
                 "millions of years showed the same pattern (Bhullar 2012). The genes are not recent "
                 "inventions; they are ancient equipment. Two interpretations compete. The warfare view: "
                 "antibiotic producers and their neighbors have fought for eons, and resistance genes are "
                 "old shields. The signaling view: if antibiotics were ancient signals, resistance genes "
                 "were tuning knobs in microbial communication networks - only drafted as shields when "
                 "humans flooded the world with lethal doses. Distinguishing them requires knowing what "
                 "these genes did in their original context, which no longer exists."),
  "why_it_matters": ("If resistance genes are ancient, versatile equipment rather than recent adaptations, "
                      "then resistance is not a problem we created and can un-create - it is a permanent "
                      "feature of the microbial world that medicine must outmaneuver forever. Strategy "
                      "changes completely: from eradication thinking to permanent management."),
  "sig_lens": ("The Signature lens treats the ancient resistome as a toolbox inherited from a forgotten "
               "trade: the tools are old, but we found them being used for a new job and assumed the new "
               "job was the original one."),
  "sol_public": ("The Signature system proposes paleo-functional reconstruction: resurrect ancient "
                 "resistance genes, test what they actually did at natural antibiotic doses, and separate "
                 "original functions from drafted ones. Read the toolbox's original manual. Full treatment: "
                 "the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) ancient resistance genes can be accurately reconstructed from "
              "permafrost DNA; (2) their original context involved natural, mostly sub-lethal antibiotic "
              "doses; (3) original function leaves detectable biochemical signatures. Reasoning path: we "
              "judge these genes by what they do in hospitals - at drug doses nature never made. The "
              "honest test is paleo-context: synthesize the ancient genes, express them, and measure their "
              "effects across the full dose range from environmental traces to clinical floods. A gene that "
              "fine-tunes signaling at low doses but blocks killing at high doses was a tuner drafted as a "
              "shield; one that only matters at lethal doses was always a shield. Proposed mechanism: a "
              "resistome paleontology program - reconstruct dated resistance genes from permafrost and cave "
              "isolates across eras, characterize dose-response functions biochemically, and map when "
              "shield-like versus tuner-like functions dominate through time. What would confirm it: "
              "ancient genes showing clear low-dose regulatory functions distinct from modern clinical "
              "alleles, with a historical shift toward pure shield function after the antibiotic era. What "
              "would kill it: ancient genes functioning identically to modern ones at all doses - proving "
              "they were always shields - or reconstructions too uncertain to test. What it does NOT "
              "claim: that knowing the origin stops resistance, that ancient genes are harmless, or that "
              "every resistance gene has a non-shield past. Where the honest answer is unknown - the true "
              "ancient dose landscape - we say so: it must be inferred, not assumed."),
  "key_points": [
   "30,000-year-old permafrost holds resistance genes effective against modern antibiotics.",
   "Isolated cave microbiomes, cut off for millions of years, carry similar resistomes.",
   "Resistance genes are ancient equipment, not recent human-caused inventions.",
   "Warfare view: old shields. Signaling view: communication tuners drafted as shields.",
   "The original context no longer exists, so original function must be reconstructed."],
  "requirements": [
   "Reconstruct dated ancient resistance genes and characterize full dose-response functions.",
   "Confirm: ancient genes show low-dose regulatory functions distinct from modern clinical alleles.",
   "Refute: ancient genes function identically to modern ones at all doses.",
   "Refute: reconstructions prove too uncertain for functional testing."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim origins stop resistance or that ancient genes are harmless.",
   "It must survive the reconstruction test: ancient sequences must be validated, not contaminated."],
  "citations": [CIT_ANCIENTR],
 },
 {
  "key": "reverse-resistance",
  "name": "Can Antibiotic Resistance Be Reversed?",
  "group": "Antibiotic Resistance",
  "ladder_rank": 22, "ladder_tier": "compounded",
  "description": ("Resistance genes carry a cost: in a drug-free world, resistant bacteria should grow "
                  "slower than susceptible ones and lose. So banning an antibiotic should, in theory, "
                  "bring back susceptibility. In practice it often does not - resistance lingers for "
                  "decades after drugs are withdrawn. Why does evolution refuse to refund the cost?"),
  "problem": "Why does antibiotic resistance persist long after antibiotic use stops, and can susceptibility ever be restored?",
  "background": ("The cost argument is textbook: resistance mutations and plasmids burden their hosts, so "
                 "removing selection should reverse resistance. Reality disagreed. When Sweden restricted "
                 "antibiotics, some resistances declined slowly; others never budged. Andersson and Hughes "
                 "(2010) explained why: compensatory mutations - second mutations that cancel the cost "
                 "while keeping resistance - lock the trait in, and some resistance mechanisms cost almost "
                 "nothing to begin with. Plasmids evolved addiction systems that kill cells losing them. "
                 "Worse, co-selection keeps resistance alive: a plasmid carrying resistance to five drugs "
                 "is maintained by any one of them, and heavy metals and biocides can select for "
                 "antibiotic resistance too. Reversal has worked in narrow cases but never as a general "
                 "strategy, and nobody knows the full inventory of cost-canceling tricks."),
  "why_it_matters": ("Antibiotic stewardship - using fewer drugs to preserve them - rests on the hope that "
                      "restraint buys back susceptibility. If resistance is largely irreversible, stewardship "
                      "only slows the loss, and policy must plan for permanent resistance plus alternatives. "
                      "The reversibility question sets the strategy for the entire antibiotic era."),
  "sig_lens": ("The Signature lens treats resistance as a ratchet, not a spring: evolution clicks forward "
               "through compensatory mutations, and each click removes the path back - so the question is "
               "where the ratchet can be jammed, not whether springs exist."),
  "sol_public": ("The Signature system proposes ratchet-mapping plus jamming: catalog the compensatory "
                 "mutations and addiction systems locking each resistance in, then design interventions - "
                 "plasmid curing, collateral-sensitivity cycling - that break specific locks. Map the "
                 "ratchet, then jam its teeth. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) persistence is caused by identifiable lock-in mechanisms, not "
              "magic; (2) locks differ per resistance gene and host; (3) some locks are breakable. "
              "Reasoning path: \"resistance is irreversible\" is too coarse - each resistance persists via "
              "specific mechanisms: zero-cost alleles, compensatory mutations, plasmid addiction, "
              "co-selection. Each lock suggests its own key. Collateral sensitivity - where resistance to "
              "drug A creates vulnerability to drug B - offers cycling strategies that steer evolution "
              "into traps. Plasmid-curing compounds and phages can strip mobile resistance. The program: "
              "for each major clinical resistance, map its lock-in mechanisms, then test targeted "
              "reversal - drug cycling designed from collateral-sensitivity maps, anti-plasmid "
              "interventions, and selection inversions that make susceptibility advantageous again. "
              "Proposed mechanism: a reversal trial platform - in vitro evolution mapping locks per "
              "resistance, then controlled community trials (hospital wards, farms) testing whether "
              "targeted cycling restores susceptibility where blanket bans failed. What would confirm it: "
              "documented susceptibility restoration for specific resistances via designed interventions, "
              "with lock mechanisms verified. What would kill it: locks proving unbreakable in practice - "
              "every targeted reversal failing despite correct lock identification - or compensatory "
              "evolution outpacing every cycling strategy. What it does NOT claim: that all resistance "
              "is reversible, that stewardship is useless, or that reversal replaces new drugs. Where the "
              "honest answer is unknown - the complete lock inventory - we say so: it must be mapped "
              "resistance by resistance."),
  "key_points": [
   "Theory says resistance should fade without drugs; practice shows it lingers for decades.",
   "Compensatory mutations cancel resistance costs while keeping the trait - locking it in.",
   "Plasmid addiction systems kill cells that lose them; co-selection maintains multi-drug plasmids.",
   "Blanket antibiotic bans have rarely restored susceptibility; narrow reversals have worked.",
   "Stewardship policy depends on whether resistance is a spring or a ratchet."],
  "requirements": [
   "Map lock-in mechanisms per major clinical resistance: costs, compensations, addictions, co-selection.",
   "Confirm: targeted interventions restore susceptibility where blanket bans failed.",
   "Refute: every targeted reversal fails despite correct lock identification.",
   "Refute: compensatory evolution outpaces all cycling strategies."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim all resistance is reversible or that stewardship is useless.",
   "It must survive the ward test: reversals must work in real communities, not just flasks."],
  "citations": [CIT_REVERSE],
 },
]

CIT_EUKGAP = ("Eme L et al. Archaea and the origin of eukaryotes. Nat Rev Microbiol. 2017;15:711-723; "
              "Lopez-Garcia P, Moreira D. The Syntrophy hypothesis for the origin of eukaryotes revisited. "
              "Nat Microbiol. 2020;5:655-667.")
CIT_MEMBRANE = ("Koga Y, Morii H. Biosynthesis of ether-type polar lipids in archaea and evolutionary "
                "considerations. Microbiol Mol Biol Rev. 2007;71:97-120; Villanueva L et al. Bridging the "
                "membrane lipid divide: bacteria of the FCB group superphylum have hetero-chiral "
                "membranes. bioRxiv. 2020.")
CIT_DEEPBIO = ("Kallmeyer J et al. Global distribution of microbial abundance and biomass in subseafloor "
               "sediment. PNAS. 2012;109:16213-16216; Inagaki F et al. Exploring deep microbial life in "
               "coal-bearing sediment down to ~2.5 km below the seafloor. Science. 2015;349:420-424.")
CIT_CARBONPUMP = ("Jiao N et al. Microbial production of recalcitrant dissolved organic matter: "
                  "long-term carbon storage in the global ocean. Nat Rev Microbiol. 2010;8:593-599; "
                  "Suttle CA. Marine viruses - major players in the global ecosystem. Nat Rev Microbiol. "
                  "2007;5:801-812.")
CIT_METHANE = ("Thauer RK et al. Methanogenic archaea: ecologically relevant differences in energy "
               "conservation. Nat Rev Microbiol. 2008;6:579-591; Knittel K, Boetius A. Anaerobic oxidation "
               "of methane: progress with an unknown process. Annu Rev Microbiol. 2009;63:311-334.")
CIT_PERMAFROST = ("Schuur EAG et al. Climate change and the permafrost carbon feedback. Nature. "
                  "2015;520:171-179; Mackelprang R et al. Permafrost meta-omics and climate change. Annu "
                  "Rev Earth Planet Sci. 2016;44:439-462.")

ENTRIES += [
 {
  "key": "eukaryote-origin",
  "name": "How Did Eukaryotes Originate?",
  "group": "Origins of Complexity",
  "ladder_rank": 23, "ladder_tier": "advanced",
  "description": ("Every animal, plant, fungus, and protist descends from one ancestor that did something "
                  "no bacterium ever did: it swallowed another cell and kept it alive inside as the "
                  "mitochondrion, then built a nucleus, internal membranes, and complex cell biology. This "
                  "happened once in four billion years. How a simple archaeon became a eukaryote - the "
                  "single greatest cellular transition in life's history - remains unsolved."),
  "problem": "How did the first eukaryotic cell arise from prokaryotic ancestors, and what was the sequence of events?",
  "background": ("Lynn Margulis championed endosymbiosis in the 1960s: mitochondria were once free bacteria. "
                 "Genomes proved her right. But the host's identity stayed mysterious until 2015, when Spang "
                 "and colleagues discovered Lokiarchaeota - archaea carrying eukaryotic-like genes for "
                 "membrane remodeling - and the Asgard archaea superphylum grew (Zaremba-Niedzwiedzka "
                 "2017), placing eukaryotes inside the archaea, not beside them. Competing scenarios "
                 "multiply: the syntrophy hypothesis (Lopez-Garcia and Moreira) has an archaeon and a "
                 "bacterium in metabolic partnership before engulfment; phagocytosis-first models need a "
                 "cytoskeleton before mitochondria; mitochondria-early models (Lane and Martin) argue only "
                 "mitochondrial energy could power eukaryotic complexity. Each scenario fits some data and "
                 "contradicts other. No living intermediate survives to interrogate."),
  "why_it_matters": ("Eukaryogenesis is the bottleneck all complex life passed through - understanding it "
                      "reveals what complex life requires, which guides the search for life beyond Earth. "
                      "It also illuminates mitochondria's role in disease and the deep logic of the cell "
                      "biology every medicine manipulates."),
  "sig_lens": ("The Signature lens treats eukaryogenesis as a merger, not an invention: two companies "
               "joined, and the mystery is the negotiation - who offered what, and in which order the "
               "contracts were signed."),
  "sol_public": ("The Signature system proposes contract-order reconstruction: use Asgard archaea as "
                 "living proxies for the host, test which eukaryotic features work without mitochondria, "
                 "and order the merger's steps experimentally. Reconstruct the negotiation from the "
                 "surviving parties. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) Asgard archaea approximate the host lineage's capabilities; (2) "
              "eukaryotic features can be tested for mitochondria-dependence; (3) the merger had an "
              "order, and the order left traces. Reasoning path: the scenarios differ in predictions. "
              "Mitochondria-early predicts no complex archaeon without an energy symbiont - test by "
              "culturing Asgard archaea and measuring their energetic and structural limits. "
              "Phagocytosis-first predicts cytoskeletal machinery working in an archaeon without "
              "mitochondria - test by characterizing Asgard cytoskeletons functionally. Syntrophy-first "
              "predicts stable archaeon-bacterium partnerships exchanging metabolites - test by building "
              "them in the lab and watching for integration. Each experiment eliminates scenarios "
              "regardless of which wins. Proposed mechanism: a eukaryogenesis test program - Asgard "
              "cultivation and cell biology, synthetic syntrophic partnerships with long-term evolution, "
              "and energetic modeling of each scenario's feasibility - converging on the ordered contract. "
              "What would confirm it: one scenario surviving all experimental eliminations with positive "
              "evidence for each step's order. What would kill it: Asgard archaea proving incapable of any "
              "proposed host role - forcing the host search back to zero - or all scenarios failing "
              "energetic feasibility. What it does NOT claim: that Asgard archaea are the host, that the "
              "merger can be replayed, or that one experiment settles four billion years. Where the honest "
              "answer is unknown - the step order - we say so: the eliminations must run."),
  "key_points": [
   "Eukaryogenesis happened once in four billion years: an archaeon plus a bacterium became all complex life.",
   "Asgard archaea (found 2015-2017) carry eukaryotic-like genes and sit as eukaryotes' closest relatives.",
   "Rival scenarios: syntrophy-first, phagocytosis-first, mitochondria-early - each fits some data.",
   "Mitochondrial energy may have been the prerequisite for all eukaryotic complexity (Lane and Martin).",
   "No living intermediate survives; the host's exact nature must be inferred."],
  "requirements": [
   "Culture Asgard archaea and test their energetic and structural limits as host proxies.",
   "Confirm: one scenario survives all experimental eliminations with positive step-order evidence.",
   "Refute: Asgard archaea prove incapable of any proposed host role.",
   "Refute: all scenarios fail energetic feasibility modeling."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim Asgard archaea are the host or that the merger can be replayed.",
   "It must survive the elimination test: scenarios must be falsifiable, not just narrated."],
  "citations": [CIT_EUKORIGIN],
 },
 {
  "key": "mito-first",
  "name": "Mitochondria First or Nucleus First?",
  "group": "Origins of Complexity",
  "ladder_rank": 24, "ladder_tier": "advanced",
  "description": ("The first eukaryote needed two revolutions: an energy symbiont (the mitochondrion) and "
                  "a control center (the nucleus). Which came first changes everything. If mitochondria "
                  "came first, energy unlocked complexity; if the nucleus came first, complexity evolved "
                  "and then captured an engine. The order of the two greatest cellular inventions is "
                  "unknown."),
  "problem": "Did mitochondria arrive before the nucleus and complex cell biology, or did a complex archaeon capture mitochondria late?",
  "background": ("The mitochondria-early case, argued by Nick Lane and William Martin, is energetic: a "
                 "prokaryote's energy budget scales with its membrane area, and only internalized "
                 "bioenergetic membranes - mitochondria - break the limit, permitting the huge genomes "
                 "and protein budgets of eukaryotes. Without mitochondria, they argue, archaeal complexity "
                 "hits a wall. The mitochondria-late case (Pittis and Gabaldon 2016) is phylogenomic: "
                 "eukaryotic genes of archaeal origin branch deeper than those of mitochondrial origin, "
                 "suggesting the host was already complex - already on the eukaryotic road - when it "
                 "acquired the symbiont. Asgard archaea with eukaryotic-like features but no mitochondria "
                 "support the late view; energetic calculations support the early view. Both cannot be "
                 "fully right, and the field has not reconciled them."),
  "why_it_matters": ("The order decides what complex life fundamentally requires: if energy came first, "
                      "then the search for complex alien life should look for energy revolutions; if "
                      "complexity came first, look for information revolutions. It also frames mitochondrial "
                      "disease - are mitochondria the cell's engine or its late add-on?"),
  "sig_lens": ("The Signature lens treats the dispute as a chicken-and-egg audit: instead of arguing "
               "about the egg, measure exactly how much energy a chicken needs - and whether any egg "
               "could afford it."),
  "sol_public": ("The Signature system proposes an energy-budget tribunal: measure what Asgard-like hosts "
                 "can actually afford energetically, and test whether proposed pre-mitochondrial "
                 "complexities fit inside that budget. Audit the energy before arguing the order. Full "
                 "treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) cellular complexity has a measurable ATP cost; (2) archaeal energy "
              "budgets can be measured in cultured Asgard relatives; (3) phylogenomic branch order "
              "reflects acquisition order. Reasoning path: the two camps argue past each other because "
              "they use different currencies - energy versus gene trees. Force both into one tribunal: "
              "enumerate the eukaryotic features claimed as pre-mitochondrial (nucleus-like organization, "
              "cytoskeleton, endomembranes), price each in ATP per cell per generation using measured "
              "archaeal metabolic rates, and ask whether an Asgard-grade host budget covers them. If the "
              "budget fails, mitochondria-early wins regardless of gene trees; if it covers them, the "
              "late view survives and the gene trees decide. Proposed mechanism: quantitative "
              "bioenergetic accounting - measured Asgard metabolism, costed complexity features, "
              "phylogenomic dating of acquisitions - integrated into one model with explicit uncertainty. "
              "What would confirm it: budget and trees agreeing on one order with quantified confidence. "
              "What would kill it: budgets with uncertainties so wide both orders fit - proving the "
              "question unanswerable by energetics - or gene trees collapsing under better models. What "
              "it does NOT claim: that energy is the only constraint, that Asgard metabolism equals the "
              "host's, or that the tribunal ends debate. Where the honest answer is unknown - the true "
              "cost of each complexity feature - we say so: the measurements must be made."),
  "key_points": [
   "Mitochondria-early: only internalized energy membranes permit eukaryotic-scale complexity (Lane and Martin).",
   "Mitochondria-late: archaeal-origin genes branch deeper than mitochondrial genes (Pittis and Gabaldon 2016).",
   "Asgard archaea show eukaryotic-like features without mitochondria, supporting the late view.",
   "Energetic calculations support the early view; both camps use different currencies.",
   "The order decides what complex life fundamentally requires - energy or information first."],
  "requirements": [
   "Price pre-mitochondrial complexity features in ATP against measured Asgard-grade budgets.",
   "Confirm: budget and phylogenomic trees converge on one order with quantified confidence.",
   "Refute: budget uncertainties leave both orders feasible.",
   "Refute: gene trees collapse under improved evolutionary models."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim energy is the only constraint or that Asgard equals the host.",
   "It must survive the currency test: both camps' evidence must be weighed in one model."],
  "citations": [CIT_MITOFIRST],
 },
 {
  "key": "eukaryotic-gap",
  "name": "The Eukaryotic Gap: No Living Intermediates",
  "group": "Origins of Complexity",
  "ladder_rank": 25, "ladder_tier": "advanced",
  "description": ("Between bacteria and eukaryotes yawns the largest unbridged gap in the tree of life. "
                  "Every known eukaryote already has mitochondria, a nucleus, and complex cell biology; "
                  "every prokaryote has none of it. No living organism sits halfway. Why did the "
                  "greatest transition in cellular history leave no survivors in between?"),
  "problem": "Why are there no living intermediates between prokaryotes and eukaryotes, and did any ever exist?",
  "background": ("Darwin worried about missing intermediates in animal evolution; microbiology has a "
                 "worse case. The gap has two possible explanations. One: intermediates existed but went "
                 "extinct - outcompeted by their own successful descendants, the way early hominins "
                 "vanished. Two: the transition was fast and singular, a rare merger that left no "
                 "halfway lineage because halfway was not viable. Asgard archaea narrowed the gap from "
                 "the archaeal side - they have eukaryotic signature proteins - but they are still "
                 "prokaryotes with no nucleus or mitochondria. Some researchers hunt for "
                 "\"archezoa\"-like reduced eukaryotes or deep-branching protists as echoes of early "
                 "stages, but every eukaryote found so far descends from the same fully-formed ancestor. "
                 "The gap may be telling us the transition was effectively instantaneous on geological "
                 "timescales - or that we have not looked in the right places."),
  "why_it_matters": ("The gap's cause reveals how evolution crosses its deepest valleys: by gradual "
                      "climbing (implying intermediates we should find) or by rare leaps (implying "
                      "complex life is improbable). That distinction shapes estimates of life's "
                      "abundance in the universe more than any other single fact."),
  "sig_lens": ("The Signature lens treats the gap as a burned bridge: either the builders tore it down "
               "behind them, or they crossed in one jump - and the ashes, if any, are in the deep "
               "biosphere we have barely sampled."),
  "sol_public": ("The Signature system proposes a two-pronged search: hunt the least-sampled habitats "
                 "for surviving intermediates with targeted single-cell genomics, while testing whether "
                 "halfway states are even viable in synthetic merger experiments. Search the ashes and "
                 "test the jump. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) if intermediates survive, they hide in undersampled habitats; (2) "
              "viability of halfway states can be tested synthetically; (3) extinction and fast-transition "
              "make different predictions. Reasoning path: the two explanations diverge testably. If "
              "intermediates went extinct through competition, the transition was survivable stepwise - so "
              "synthetic halfway states (archaea with partial endosymbionts, engineered in the lab) should "
              "be viable and even competitive. If the transition was a singular leap, halfway states "
              "should be inviable or unstable, collapsing back or dying. Meanwhile, targeted hunting - "
              "single-cell genomics of deep subsurface, anoxic sediments, and extreme environments - "
              "tests whether any lineage escaped the extinction. Proposed mechanism: parallel programs - "
              "deep-habitat single-cell surveys aimed at deep-branching lineages, plus synthetic "
              "intermediate construction with long-term competition assays. What would confirm it: either "
              "a genuine intermediate lineage found alive, or synthetic halfway states proving inviable - "
              "each answer resolves the gap's cause. What would kill it: surveys that never saturate "
              "(absence of evidence never becoming evidence of absence) combined with synthetic "
              "intermediates that are merely mediocre - leaving both explanations alive forever. What it "
              "does NOT claim: that intermediates must exist, that synthetic constructs replay history, "
              "or that one survey ends the search. Where the honest answer is unknown - whether the "
              "transition was gradual or leaping - we say so: the two prongs must report."),
  "key_points": [
   "No living organism sits halfway between prokaryotes and eukaryotes - the deepest unbridged gap in biology.",
   "Asgard archaea narrowed the gap from the archaeal side but remain prokaryotes.",
   "Two explanations: intermediates existed and went extinct, or the transition was a singular fast leap.",
   "Every known eukaryote descends from the same fully-formed ancestor.",
   "The gap's cause shapes estimates of complex life's cosmic abundance."],
  "requirements": [
   "Survey deep, undersampled habitats with single-cell genomics for deep-branching intermediates.",
   "Confirm: a genuine intermediate lineage found alive, or synthetic halfway states proving inviable.",
   "Refute: surveys never saturate while synthetic intermediates are merely mediocre.",
   "Refute: halfway states prove robustly viable and competitive, contradicting the leap view."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim intermediates must exist or that constructs replay history.",
   "It must survive the viability test: synthetic states must be tested in competition, not isolation."],
  "citations": [CIT_EUKGAP],
 },
 {
  "key": "membrane-divide",
  "name": "The Membrane Lipid Divide",
  "group": "Origins of Complexity",
  "ladder_rank": 26, "ladder_tier": "advanced",
  "description": ("Bacteria and eukaryotes build their cell membranes from fatty acids linked one way; "
                  "archaea build theirs from isoprenoids linked the mirror-image way. This \"lipid divide\" "
                  "is one of the sharpest chemical splits in biology. Since eukaryotes descend from "
                  "archaea, their ancestor must have crossed from archaeal membranes to bacterial ones - "
                  "and nobody knows how a cell survives switching its entire membrane chemistry."),
  "problem": "How did the archaeal ancestor of eukaryotes switch from archaeal to bacterial-type membrane lipids without dying?",
  "background": ("The divide was characterized by Koga and Morii: archaeal lipids are ether-linked "
                 "isoprenoids with sn-glycerol-1-phosphate stereochemistry; bacterial and eukaryotic "
                 "lipids are ester-linked fatty acids with the mirror-image sn-glycerol-3-phosphate. The "
                 "two chemistries were long thought mutually exclusive - a cell mixing them might suffer "
                 "unstable membranes. Yet eukaryotes, archaeal by descent, use bacterial-type lipids, so "
                 "a transition happened. Recent discoveries softened the wall: some bacteria of the FCB "
                 "superphylum make mixed hetero-chiral membranes (Villanueva 2020), proving mixed "
                 "membranes can work. Hypotheses for the switch include gradual replacement during "
                 "endosymbiosis (the bacterial symbiont donating lipid genes), a heterochiral intermediate "
                 "stage, and selection for ester lipids' properties. No consensus exists on the path or "
                 "its timing relative to other eukaryotic features."),
  "why_it_matters": ("Membranes are the cell's border with the world; the divide's crossing was a "
                      "chemical reinvention of that border during eukaryogenesis. Understanding it reveals "
                      "how deeply cellular chemistry can be remodeled - relevant to synthetic biology's "
                      "ambitions to build novel cells - and pins down the order of eukaryotic innovations."),
  "sig_lens": ("The Signature lens treats the membrane as a ship rebuilt at sea: the planks were swapped "
               "one by one while the ship stayed afloat - and the question is which planks went first."),
  "sol_public": ("The Signature system proposes plank-by-plank reconstruction: engineer archaea to "
                 "express bacterial lipid genes stepwise and find the viable transition path. Rebuild the "
                 "ship at sea in the lab. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) mixed membranes are viable, as FCB bacteria prove; (2) lipid "
              "genes are transferable; (3) the transition path left a viable sequence of intermediates. "
              "Reasoning path: the \"impossible switch\" framing assumed an all-at-once conversion. "
              "Biology rarely works that way - it works plank by plank. Engineer a cultivable archaeon to "
              "express bacterial lipid synthesis genes incrementally: first the opposite-stereochemistry "
              "backbone, then ester linkages, then fatty-acid chains - measuring membrane stability, "
              "permeability, and growth at each step. The viable path through this landscape is a "
              "candidate for the historical route; inviable steps eliminate proposed orders. Proposed "
              "mechanism: stepwise lipid-remodeling in a model archaeon with biophysical characterization "
              "at each stage, plus surveys of natural heterochiral membranes as existence proofs. What "
              "would confirm it: a complete viable stepwise path from archaeal to bacterial-type membranes "
              "with measured properties at each stage. What would kill it: no viable path - every "
              "intermediate collapsing - suggesting the historical transition used unknown tricks or "
              "different starting chemistry. What it does NOT claim: that the lab path is the historical "
              "path, that one archaeon models the ancestor, or that endosymbiosis played no role. Where "
              "the honest answer is unknown - the actual step order - we say so: the landscape must be "
              "mapped."),
  "key_points": [
   "Archaeal and bacterial membrane lipids are mirror-image chemistries, long thought incompatible.",
   "Eukaryotes descend from archaea but use bacterial-type lipids - a switch occurred.",
   "Some FCB bacteria make mixed hetero-chiral membranes, proving mixtures can work.",
   "Candidate routes: gradual replacement, heterochiral intermediates, symbiont-donated lipid genes.",
   "No consensus on the path or its timing among eukaryotic innovations."],
  "requirements": [
   "Engineer stepwise lipid remodeling in a model archaeon with biophysical checks per stage.",
   "Confirm: a complete viable stepwise path from archaeal to bacterial-type membranes.",
   "Refute: every intermediate collapses - no viable path exists.",
   "Refute: natural heterochiral membranes prove mechanistically unrelated to the transition."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim the lab path is the historical path.",
   "It must survive the viability test: each intermediate must grow, not just survive briefly."],
  "citations": [CIT_MEMBRANE],
 },
 {
  "key": "deep-biosphere-energy",
  "name": "What Powers the Deep Biosphere?",
  "group": "Microbes and Climate",
  "ladder_rank": 27, "ladder_tier": "advanced",
  "description": ("Kilometers beneath the seafloor, in sediments millions of years old, microbes live at "
                  "densities of thousands per cubic centimeter - barely active, dividing perhaps once per "
                  "thousand years. They constitute a huge fraction of Earth's biomass. What do they eat? "
                  "Sunlight never reaches them, organic matter is nearly exhausted, and yet they persist. "
                  "The energy budget of the deep biosphere does not add up."),
  "problem": "What energy sources sustain microbial life kilometers underground over geological timescales?",
  "background": ("Ocean drilling revealed the deep biosphere's scale: Kallmeyer and colleagues (2012) "
                 "estimated subseafloor sediments hold a large share of Earth's microbial cells, and "
                 "Inagaki's team (2015) found active communities 2.5 kilometers down in 20-million-year-old "
                 "coal beds. Candidate energy sources include the slow fermentation of ancient buried "
                 "organic matter, hydrogen from water-rock reactions (radiolysis and serpentinization), and "
                 "redox gradients at interfaces. But measured metabolic rates are so low - near the "
                 "theoretical minimum for life - that contamination and measurement artifacts haunt every "
                 "result. Some cells may be dormant for millennia between rare energy pulses; others may "
                 "run on reactions chemistry has not fully described. The deep biosphere's total energy "
                 "demand versus the available supply has never been balanced in any site."),
  "why_it_matters": ("The deep biosphere may be Earth's largest ecosystem by biomass and its most alien - "
                      "a model for life on Mars and icy moons, where similar energy-starved conditions "
                      "prevail. Its microbes also mediate deep carbon burial, affecting climate over "
                      "geological time. And its enzymes, evolved for extreme energy frugality, are "
                      "biotechnological prizes."),
  "sig_lens": ("The Signature lens treats deep microbes as misers in a dark vault: they spend almost "
               "nothing, so the audit must find income streams invisible at surface scales - pennies of "
               "hydrogen, interest on ancient carbon."),
  "sol_public": ("The Signature system proposes a full energy audit per site: measure every candidate "
                 "income - radiolytic hydrogen, rock reactions, ancient organics - against the community's "
                 "metered spending, until the books balance. Audit the vault until every penny is traced. "
                 "Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) energy supply and demand must balance - no perpetual motion; (2) "
              "current measurements miss some income streams; (3) dormancy cycling complicates the books. "
              "Reasoning path: treat each deep site as an economy. Meter the spending: single-cell "
              "metabolic rates via isotope tracers, scaled by cell counts. Then inventory every income: "
              "hydrogen fluxes from radiolysis and serpentinization, fermentable organics in the "
              "sediment, redox interfaces, even natural radioactivity-driven chemistry. Where books do "
              "not balance, the gap is a discovery - either an unknown energy source or overestimated "
              "demand (dormancy). Close sites one by one until the pattern generalizes. Proposed "
              "mechanism: deep-site energy audits - co-located measurement of all candidate fluxes plus "
              "single-cell activity, at reference drill sites spanning sediment ages and geologies. What "
              "would confirm it: balanced books at multiple sites with identified dominant incomes, and "
              "predictive power for new sites. What would kill it: persistent imbalance despite "
              "exhaustive measurement - implying unknown physics or chemistry - or demand estimates "
              "collapsing as contamination artifacts. What it does NOT claim: that one income fits all "
              "sites, that dormancy is understood, or that Mars follows Earth. Where the honest answer is "
              "unknown - the dominant income at most sites - we say so: the audits must measure it."),
  "key_points": [
   "Subseafloor sediments hold a huge share of Earth's microbial cells, some dividing once per millennium.",
   "Active communities exist 2.5 km down in 20-million-year-old coal beds.",
   "Candidate incomes: ancient organics, radiolytic hydrogen, water-rock reactions, redox interfaces.",
   "Measured metabolic rates sit near the theoretical minimum for life.",
   "No site has ever balanced deep energy supply against demand."],
  "requirements": [
   "Perform full energy audits at reference drill sites: all candidate fluxes plus single-cell activity.",
   "Confirm: balanced books at multiple sites with identified dominant incomes, predictive for new sites.",
   "Refute: persistent imbalance despite exhaustive measurement.",
   "Refute: demand estimates collapse as contamination artifacts."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim one income fits all sites or that Mars follows Earth.",
   "It must survive the contamination test: deep samples must be proven pristine."],
  "citations": [CIT_DEEPBIO],
 },
 {
  "key": "microbial-carbon-pump",
  "name": "The Microbial Carbon Pump",
  "group": "Microbes and Climate",
  "ladder_rank": 28, "ladder_tier": "advanced",
  "description": ("The ocean holds more carbon than the atmosphere, and microbes decide how much stays "
                  "there. The microbial carbon pump - microbes converting digestible carbon into "
                  "long-lasting dissolved forms - may sequester carbon for millennia. But its strength, "
                  "its controls, and how climate change will alter it are among the least constrained "
                  "numbers in climate science."),
  "problem": "How much carbon does the microbial carbon pump sequester, what controls it, and how will warming change it?",
  "background": ("Jiao and colleagues formalized the microbial carbon pump in 2010: marine microbes "
                 "process dissolved organic carbon, and a fraction becomes recalcitrant - resistant to "
                 "further breakdown - persisting in the deep ocean for thousands of years. The viral shunt "
                 "(Suttle, Wilhelm) adds a parallel route: viruses lyse cells, releasing organic matter "
                 "that partly becomes recalcitrant. Together these microbial processes may rival the "
                 "biological carbon pump (sinking particles) in long-term sequestration. But recalcitrant "
                 "carbon is defined by what microbes cannot eat - a negative definition - and its "
                 "production rates, chemical identities, and temperature sensitivity are poorly measured. "
                 "Warming could strengthen the pump (faster microbial processing) or weaken it (changed "
                 "communities, stratification starving the surface), and models cannot tell which."),
  "why_it_matters": ("The ocean is humanity's largest carbon sink; the microbial pump's response to "
                      "warming is a first-order uncertainty in every climate projection. If the pump "
                      "weakens, more CO2 stays airborne and warming accelerates - a feedback missing from "
                      "most models. Getting the number right changes emissions arithmetic."),
  "sig_lens": ("The Signature lens treats the pump as a refinery with unknown yield: microbes take crude "
               "carbon in and the refinery outputs both fuel (recycled) and asphalt (sequestered) - and "
               "we have never metered either stream properly."),
  "sol_public": ("The Signature system proposes metering the refinery: track carbon atoms from uptake "
                 "through microbial processing to recalcitrant output with isotope labeling across ocean "
                 "regimes, then test temperature response experimentally. Meter both streams, then heat "
                 "the refinery. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) recalcitrant carbon production is measurable via long incubations; "
              "(2) temperature responses can be tested experimentally; (3) the pump varies by ocean "
              "regime. Reasoning path: the pump's uncertainty comes from measuring stocks, not flows. "
              "Fix it with flow metering: add isotopically labeled organic carbon to seawater from "
              "diverse regimes, track its fate through microbial processing with high-resolution mass "
              "spectrometry, and quantify the recalcitrant fraction over months. Repeat across "
              "temperature gradients - natural and experimental - to map the pump's thermal response. "
              "Combine with viral-shunt measurements (lysis rates, lysate fate) for the parallel route. "
              "Proposed mechanism: a pump-metering campaign - standardized isotope incubations across "
              "ocean provinces plus mesocosm warming experiments, feeding recalcitrant-production "
              "functions into Earth system models. What would confirm it: consistent production "
              "functions predicting recalcitrant stocks, and models with the pump outperforming those "
              "without on historical data. What would kill it: recalcitrant fractions proving "
              "unmeasurable - production indistinguishable from background - or temperature responses so "
              "variable that no function generalizes. What it does NOT claim: that the pump dominates "
              "the carbon budget, that models are currently wrong, or that geoengineering should "
              "manipulate it. Where the honest answer is unknown - the pump's true strength - we say so: "
              "the metering must measure it."),
  "key_points": [
   "Marine microbes convert digestible carbon into recalcitrant forms persisting for millennia.",
   "The viral shunt - lysis releasing organic matter - is a parallel sequestration route.",
   "Recalcitrant carbon is defined negatively: what microbes cannot eat.",
   "Production rates, chemical identities, and temperature sensitivity are poorly measured.",
   "Warming could strengthen or weaken the pump; models cannot currently tell."],
  "requirements": [
   "Meter carbon flows with isotope labeling across ocean regimes plus mesocosm warming experiments.",
   "Confirm: consistent production functions predicting stocks; pump-inclusive models beating pump-free ones.",
   "Refute: recalcitrant production indistinguishable from background in all tests.",
   "Refute: temperature responses too variable for any generalizing function."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim the pump dominates the carbon budget or that models are wrong.",
   "It must survive the flow test: flows must be measured, not inferred from stocks."],
  "citations": [CIT_CARBONPUMP],
 },
]

CIT_NITROGEN = ("Canfield DE et al. The evolution and future of Earth's nitrogen cycle. Science. "
                "2010;330:192-196; Gruber N, Galloway JN. An Earth-system perspective of the global "
                "nitrogen cycle. Nature. 2008;451:293-296.")
CIT_LUCA = ("Weiss MC et al. The physiology and habitat of the last universal common ancestor. Nature "
            "Microbiology. 2016;1:16116; Gogarten JP, Deamer D. Is LUCA a thermophilic progenote? Nature "
            "Microbiology. 2016;1:16229.")
CIT_PANGENOME = ("Tettelin H et al. Genome analysis of multiple pathogenic isolates of Streptococcus "
                 "agalactiae: implications for the microbial 'pan-genome'. PNAS. 2005;102:13950-13955; "
                 "McInerney JO et al. The public goods hypothesis for the evolution of life on Earth. "
                 "Biol Direct. 2011;6:41.")
CIT_TREEVWEB = ("Doolittle WF. Phylogenetic classification and the universal tree. Science. "
                "1999;284:2124-2128; Koonin EV. The turbulent network dynamics of microbial evolution "
                "and the statistical tree of life. J Mol Evol. 2015;80:244-250.")

ENTRIES += [
 {
  "key": "methane-budget",
  "name": "Methane: Microbial Source and Sink",
  "group": "Microbes and Climate",
  "ladder_rank": 29, "ladder_tier": "advanced",
  "description": ("Methane is the second most important greenhouse gas, and microbes are both its largest "
                  "natural source and a major sink. Methanogens make it in wetlands, rice paddies, and guts; "
                  "methanotrophs consume it in soils and oceans. The two microbial guilds wage a tug-of-war "
                  "that sets atmospheric methane - and the budget does not balance cleanly, with mysterious "
                  "surges in recent years."),
  "problem": "Can we close the microbial methane budget - and explain the recent unexplained surges in atmospheric methane?",
  "background": ("Methanogenic archaea produce methane as their energy metabolism's waste product; they "
                 "are among Earth's oldest metabolisms (Thauer 2008). Aerobic methanotrophs in soils and "
                 "anaerobic methane oxidizers (ANME archaea, often partnered with sulfate reducers) consume "
                 "it - anaerobic oxidation of methane (AOM) was confirmed in marine sediments by Boetius "
                 "and colleagues, a process once thought impossible. The global budget roughly balances "
                 "sources against sinks, but uncertainties are large on both sides, and atmospheric methane "
                 "has surged since 2007 with no agreed cause: tropical wetlands, fossil leaks, or weakened "
                 "sinks are all suspects. Isotopic fingerprints should distinguish microbial from fossil "
                 "methane, but the fingerprints overlap and shift. Microbial feedbacks add danger: warming "
                 "thawing permafrost could awaken methanogens faster than methanotrophs respond."),
  "why_it_matters": ("Methane drives a large share of near-term warming and has a short atmospheric "
                      "lifetime - cutting it cools the planet fast. But you cannot manage what you cannot "
                      "attribute: without a closed microbial budget, methane policy targets the wrong "
                      "sources and misses the feedbacks that could accelerate warming."),
  "sig_lens": ("The Signature lens treats the methane budget as a ledger with two microbial bookkeepers - "
               "one writing checks (methanogens), one cashing them (methanotrophs) - and the books will "
               "not balance until both are audited in the field, not the lab."),
  "sol_public": ("The Signature system proposes dual-guild field auditing: measure methanogen and "
                 "methanotroph activity simultaneously at matched sites with isotopes, and attribute "
                 "atmospheric surges by fingerprinting. Audit both bookkeepers together. Full treatment: "
                 "the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) budget uncertainty comes from measuring guilds separately; (2) "
              "isotopic fingerprints can attribute sources if calibrated; (3) feedbacks are the critical "
              "unknown. Reasoning path: current budgets combine lab rates, sparse field data, and model "
              "assumptions - the bookkeepers are audited in different offices. The fix is paired "
              "measurement: at wetlands, rice paddies, thawing permafrost, and ocean seeps, measure "
              "methanogenesis and methane oxidation simultaneously with stable-isotope tracers, so net "
              "flux is observed, not subtracted from uncertain grosses. Calibrate isotopic fingerprints "
              "against these paired sites, then apply them to atmospheric surge attribution. Finally, "
              "warm the sites experimentally and watch which guild responds faster - the feedback "
              "experiment. Proposed mechanism: a methane-ledger campaign - paired guild measurements "
              "across representative sources, fingerprint calibration, and warming experiments feeding a "
              "closed budget with honest uncertainty. What would confirm it: a budget that closes within "
              "measured uncertainty and attributes recent surges to specific guild responses. What would "
              "kill it: paired measurements with uncertainties still too large to close the budget, or "
              "fingerprints that cannot distinguish sources despite calibration. What it does NOT claim: "
              "that microbes are the sole surge driver, that fossil sources are innocent, or that the "
              "budget will stay closed as climate shifts. Where the honest answer is unknown - the surge's "
              "cause - we say so: the attribution must earn it."),
  "key_points": [
   "Microbes are methane's largest natural source (methanogens) and a major sink (methanotrophs).",
   "Anaerobic oxidation of methane by ANME archaea was once thought impossible; now it is a major sink.",
   "Atmospheric methane has surged since 2007 with no agreed cause.",
   "Isotopic fingerprints should separate microbial from fossil methane but overlap and shift.",
   "Warming could awaken methanogens faster than methanotrophs respond - a dangerous feedback."],
  "requirements": [
   "Measure methanogenesis and oxidation simultaneously with isotope tracers at matched sites.",
   "Confirm: a budget closing within measured uncertainty that attributes recent surges.",
   "Refute: paired measurements still too uncertain to close the budget.",
   "Refute: fingerprints cannot distinguish sources despite field calibration."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim microbes are the sole surge driver or fossil sources innocent.",
   "It must survive the net-flux test: net emissions must be observed, not subtracted."],
  "citations": [CIT_METHANE],
 },
 {
  "key": "permafrost-carbon",
  "name": "Permafrost Thaw: The Microbial Carbon Bomb",
  "group": "Microbes and Climate",
  "ladder_rank": 30, "ladder_tier": "advanced",
  "description": ("Permafrost holds roughly twice as much carbon as the atmosphere - frozen plant matter "
                  "accumulated over millennia. As it thaws, microbes wake and eat it, releasing CO2 and "
                  "methane. This permafrost carbon feedback could add a country-sized emissions source "
                  "that no climate policy controls. But which microbes wake, what they release, and how "
                  "fast remain deeply uncertain."),
  "problem": "Which microbes drive permafrost carbon release, what gases do they produce, and how fast will the feedback run?",
  "background": ("Schuur and colleagues (2015) synthesized the feedback's scale: permafrost carbon dwarfs "
                 "atmospheric carbon, and thaw is accelerating across the Arctic. Meta-omics studies "
                 "(Mackelprang 2016) revealed thaw awakens complex communities - fermenters, methanogens, "
                 "methanotrophs - whose balance decides whether carbon leaves as CO2 or the far more "
                 "potent methane. The critical unknowns are kinetic: how fast do different carbon pools "
                 "decompose, does thaw produce abrupt thaw-lake methane bursts or gradual CO2, and do "
                 "nutrient releases fertilize plant growth enough to offset some loss? Abrupt thaw "
                 "processes - thermokarst, coastal erosion - are poorly represented in models, and "
                 "microbial community shifts under thaw have rarely been measured at the process level. "
                 "Estimates of the feedback's 21st-century impact span an order of magnitude."),
  "why_it_matters": ("The permafrost feedback is the largest uncontrolled carbon source in climate "
                      "projections - it could consume a significant fraction of the remaining carbon "
                      "budget for 1.5 degrees. Every ton of its uncertainty is a ton of ambiguity in "
                      "humanity's emissions allowance. Microbes pull the trigger; we need their timing."),
  "sig_lens": ("The Signature lens treats thawing permafrost as a freezer failure in a vast warehouse: "
               "the inventory is known approximately, but which stock spoils first, into what gases, "
               "and how fast depends on the staff - the microbes - waking shift by shift."),
  "sol_public": ("The Signature system proposes shift-by-shift thaw watching: instrument thaw gradients "
                 "with microbial process measurements - who wakes, what gas, how fast - and scale with "
                 "remote sensing. Watch each shift clock in. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) gas outcome depends on which microbial guilds activate; (2) thaw "
              "is heterogeneous - gradual versus abrupt - and guilds differ between them; (3) process "
              "rates can be measured in situ. Reasoning path: models treat permafrost carbon as a pool "
              "with a decay rate, but the rate is set by biology - fermenters making CO2 and substrates, "
              "methanogens making methane where oxygen is absent, methanotrophs intercepting some of it. "
              "The program: instrument natural thaw gradients (frozen to fully thawed) with gas flux "
              "chambers, isotope tracers for process rates, and metagenomic guild tracking - measuring "
              "the microbial shift shift-by-shift. Cover abrupt thaw features (thermokarst lakes, "
              "erosion) explicitly, since they may dominate. Scale point measurements with satellite "
              "thaw mapping. Proposed mechanism: a permafrost process network - standardized thaw-gradient "
              "observatories across the Arctic with microbial process data feeding next-generation "
              "feedback models. What would confirm it: models with microbial processes predicting thaw "
              "emissions at new sites better than pool-decay models, with narrowed uncertainty. What "
              "would kill it: guild activity proving unpredictable from thaw state - chaos at every site "
              "- or abrupt-thaw emissions dwarfing gradual processes beyond measurement. What it does NOT "
              "claim: that the feedback can be stopped, that plants will offset it, or that models are "
              "currently useless. Where the honest answer is unknown - the feedback's true speed - we say "
              "so: the observatories must clock it."),
  "key_points": [
   "Permafrost holds roughly twice the atmosphere's carbon; thaw is accelerating.",
   "Thaw awakens fermenters, methanogens, and methanotrophs; their balance sets CO2 versus methane.",
   "Abrupt thaw (thermokarst, erosion) is poorly represented in models and may dominate.",
   "Feedback estimates for this century span an order of magnitude.",
   "The feedback could consume much of the remaining 1.5-degree carbon budget."],
  "requirements": [
   "Instrument thaw gradients with gas flux, isotope process rates, and guild tracking.",
   "Confirm: microbial-process models predict new-site emissions better than pool-decay models.",
   "Refute: guild activity unpredictable from thaw state at every site.",
   "Refute: abrupt-thaw emissions dwarf gradual processes beyond measurement."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim the feedback can be stopped or that plants offset it.",
   "It must survive the scale test: point processes must scale to pan-Arctic budgets."],
  "citations": [CIT_PERMAFROST],
 },
 {
  "key": "nitrogen-budget",
  "name": "Closing the Nitrogen Budget",
  "group": "Microbes and Climate",
  "ladder_rank": 31, "ladder_tier": "advanced",
  "description": ("Nitrogen fertilizer feeds half of humanity - and microbes move every atom of it. They "
                  "fix nitrogen from the air, convert it through nitrification and denitrification, and "
                  "leak nitrous oxide, a greenhouse gas nearly 300 times more potent than CO2. The global "
                  "nitrogen cycle is microbially run, human-doubled in scale, and its books do not "
                  "balance: sources and sinks disagree, and N2O keeps rising."),
  "problem": "Can we close the global nitrogen budget and account for rising nitrous oxide emissions?",
  "background": ("Humans now fix more nitrogen industrially and agriculturally than all natural processes "
                 "combined (Gruber and Galloway 2008) - the cycle has been doubled. Microbes run every "
                 "transformation: nitrogen fixers, ammonia oxidizers (bacteria and archaea), and "
                 "denitrifiers that return nitrogen to the air - leaking N2O at each step. Canfield and "
                 "colleagues (2010) traced the cycle's evolution and future, but the modern budget has "
                 "persistent gaps: denitrification in oceans and soils is hard to measure directly, "
                 "agricultural N2O emission factors vary wildly by soil and practice, and the atmospheric "
                 "N2O rise is not fully attributed. New microbial players keep appearing - anammox "
                 "bacteria, comammox Nitrospira doing complete nitrification alone - each discovery "
                 "rewriting process maps. The budget's imbalance is a measurement problem with "
                 "planetary stakes."),
  "why_it_matters": ("N2O is the third most important greenhouse gas and the largest remaining threat to "
                      "the ozone layer; nitrogen runoff creates dead zones in coastal waters. Closing the "
                      "budget tells farmers how to fertilize with less leakage, tells climate models their "
                      "N2O future, and tells policymakers where the cheapest cuts hide."),
  "sig_lens": ("The Signature lens treats the nitrogen cycle as a factory where every workstation is "
               "microbial and the inventory never reconciles: the fix is not better accounting tricks "
               "but meters on every workstation."),
  "sol_public": ("The Signature system proposes workstation metering: measure each microbial nitrogen "
                 "transformation in situ with isotopes across representative systems, then assemble the "
                 "budget from measured flows. Put meters on every workstation. Full treatment: the "
                 "Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) budget gaps come from unmeasured processes, not unknown "
              "chemistry; (2) new microbial players (anammox, comammox) must be included; (3) in-situ "
              "rates beat lab extrapolations. Reasoning path: the budget is assembled from mismatched "
              "pieces - lab rates scaled up, sparse field data, model residuals. Replace it with direct "
              "flow measurement: 15N tracers quantifying fixation, nitrification, anammox, and "
              "denitrification simultaneously in representative soils, sediments, and ocean zones, with "
              "N2O isotopomers fingerprinting which step leaks. New players get their own meters rather "
              "than being folded into old categories. Proposed mechanism: a nitrogen workstations "
              "campaign - standardized multi-process isotope measurements across agricultural, natural "
              "terrestrial, and marine systems, feeding a flow-based budget with quantified uncertainty. "
              "What would confirm it: a budget that closes within measurement uncertainty and attributes "
              "the N2O rise to specific processes and regions. What would kill it: flows proving too "
              "heterogeneous to generalize - every field its own budget - or N2O fingerprints that cannot "
              "resolve leaking steps. What it does NOT claim: that the budget stays closed under "
              "change, that all N2O is agricultural, or that measurement alone cuts emissions. Where the "
              "honest answer is unknown - the true process attribution - we say so: the meters must "
              "report."),
  "key_points": [
   "Humans now fix more nitrogen than all natural processes combined; microbes run every transformation.",
   "N2O is nearly 300 times more potent than CO2 and threatens the ozone layer.",
   "Ocean and soil denitrification are hard to measure; agricultural emission factors vary wildly.",
   "New players - anammox, comammox - keep rewriting the process map.",
   "The atmospheric N2O rise is not fully attributed to sources."],
  "requirements": [
   "Measure all nitrogen transformations simultaneously with 15N tracers across representative systems.",
   "Confirm: a flow-based budget closing within uncertainty, attributing the N2O rise.",
   "Refute: flows too heterogeneous to generalize beyond individual fields.",
   "Refute: N2O isotopomers cannot resolve which steps leak."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim the budget stays closed or that measurement cuts emissions.",
   "It must survive the generalization test: site flows must scale to global budgets."],
  "citations": [CIT_NITROGEN],
 },
 {
  "key": "luca-nature",
  "name": "What Was LUCA Like?",
  "group": "Origins of Complexity",
  "ladder_rank": 32, "ladder_tier": "advanced",
  "description": ("All life on Earth - every bacterium, archaeon, mushroom, and human - descends from one "
                  "population: LUCA, the Last Universal Common Ancestor, alive roughly four billion years "
                  "ago. What did it look like? Was it a simple cell or a complex community? Did it live "
                  "in a hot vent or a warm pond? Reconstructing our ultimate ancestor from the genes its "
                  "descendants kept is one of the deepest detective stories in science - and the portrait "
                  "keeps changing."),
  "problem": "What was the physiology, habitat, and complexity of LUCA, the ancestor of all known life?",
  "background": ("LUCA is reconstructed by comparing genomes across bacteria and archaea: genes shared by "
                 "both domains were probably in LUCA. Weiss and colleagues (2016) analyzed 6.1 million "
                 "genes and assigned 355 to LUCA, painting it as an anaerobic, hydrogen-dependent "
                 "thermophile living in hydrothermal vents, using the ancient Wood-Ljungdahl pathway - "
                 "geochemically powered, half-alive by modern standards. Critics counter that shared genes "
                 "may reflect later horizontal transfers, not inheritance, and that 355 genes is a "
                 "minimalist portrait missing much. Gogarten and Deamer debated whether LUCA was even a "
                 "cell or a community of replicators in vent compartments. The vent hypothesis fits the "
                 "chemistry - vents provide the gradients life needs - but surface warm-pond models have "
                 "their own chemical logic. LUCA's portrait swings between a simple vent-dwelling "
                 "progenote and a fairly sophisticated cell."),
  "why_it_matters": ("LUCA's nature constrains the origin of life: if LUCA was already complex and "
                      "vent-dwelling, life's origin must produce such cells quickly in such places - "
                      "guiding both origin-of-life experiments and the search for life on ocean worlds "
                      "like Enceladus. It is also the root of the tree everything hangs from."),
  "sig_lens": ("The Signature lens treats LUCA reconstruction as restoring a burned manuscript: the "
               "surviving copies share passages, but scribes (horizontal transfer) inserted their own "
               "lines - and the restoration must separate original text from later edits."),
  "sol_public": ("The Signature system proposes edit-aware reconstruction: date every candidate LUCA "
                 "gene's arrival with transfer-aware phylogenies, keep only the pre-divergence core, then "
                 "test the portrait's viability in simulated vent chemistry. Separate original text from "
                 "scribal edits. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) some shared genes are later transfers, not inheritance; (2) "
              "transfer-aware methods can distinguish them; (3) the portrait must be chemically viable. "
              "Reasoning path: the 355-gene portrait assumes shared means ancestral, but horizontal "
              "transfer between bacteria and archaea after their split plants false LUCA genes. The fix "
              "is edit-aware phylogeny: for each candidate gene, test whether its tree matches the "
              "species split or shows transfer - keep only genes whose history is clean. Then take the "
              "cleaned portrait seriously as a hypothesis: can an organism with exactly that metabolism "
              "actually live in simulated vent conditions - the predicted chemistry, gradients, and "
              "energy? Viability testing turns the portrait from a list into a testable organism model. "
              "Proposed mechanism: a LUCA restoration pipeline - transfer-aware gene dating across "
              "thousands of genomes, metabolic reconstruction of the cleaned core, and experimental "
              "viability testing in vent-simulating reactors. What would confirm it: a cleaned gene set "
              "yielding a coherent, experimentally viable vent organism model. What would kill it: "
              "transfer-aware cleaning leaving too few genes for any coherent metabolism - proving LUCA "
              "is unrecoverable - or the cleaned portrait proving inviable in every simulated habitat. "
              "What it does NOT claim: that LUCA was the first life, that vents are proven, or that the "
              "portrait will ever be complete. Where the honest answer is unknown - LUCA's true gene "
              "set - we say so: the pipeline must earn every gene."),
  "key_points": [
   "LUCA, alive ~4 billion years ago, is the ancestor of all known cellular life.",
   "Weiss et al. (2016) assigned 355 genes to LUCA: anaerobic, hydrogen-dependent, vent-dwelling.",
   "Critics warn shared genes may be later horizontal transfers, not inheritance.",
   "Alternative views: LUCA as a community of replicators, or a warm-pond rather than vent organism.",
   "LUCA's nature constrains origin-of-life scenarios and the search for life on ocean worlds."],
  "requirements": [
   "Date candidate LUCA genes with transfer-aware phylogenies; keep only the pre-divergence core.",
   "Confirm: a cleaned gene set yielding a coherent, experimentally viable organism model.",
   "Refute: cleaning leaves too few genes for any coherent metabolism.",
   "Refute: the cleaned portrait proves inviable in every simulated habitat."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim LUCA was the first life or that vents are proven.",
   "It must survive the viability test: the portrait must live, at least in simulation."],
  "citations": [CIT_LUCA],
 },
 {
  "key": "open-pangenome",
  "name": "The Open Pan-Genome",
  "group": "The Uncultured Majority",
  "ladder_rank": 33, "ladder_tier": "advanced",
  "description": ("Sequence one E. coli and you get 5,000 genes. Sequence a hundred E. coli and the "
                  "combined gene pool - the pan-genome - keeps growing with no sign of stopping: over "
                  "100,000 gene families and counting. For many bacteria, the species' gene pool appears "
                  "open - infinite. How many genes does a bacterial species actually have, and what does "
                  "an unbounded genome mean for the species concept itself?"),
  "problem": "Is the pan-genome of a bacterial species finite or effectively infinite - and what maintains its openness?",
  "background": ("Tettelin and colleagues coined the pan-genome in 2005 studying Streptococcus agalactiae: "
                 "the core genome shared by all strains plus the dispensable genome varying between them. "
                 "For some species (Buchnera) the pan-genome closes quickly; for E. coli, Streptococcus "
                 "pneumoniae, and many environmental bacteria it stays open - every new genome adds new "
                 "genes, following a power law with no plateau in sight. The public-goods hypothesis "
                 "(McInerney 2011) proposes genes are communal resources: the pan-genome is the species' "
                 "shared toolbox, with individuals carrying subsets. But sampling bias haunts the "
                 "question: we sequence clinical and convenient strains, and rare genes may be "
                 "sequencing artifacts or transient DNA. Whether any pan-genome is truly infinite, and "
                 "what evolutionary forces keep it open, remains unanswered - with implications for "
                 "everything from vaccine design (which genes are stable targets?) to the species "
                 "problem."),
  "why_it_matters": ("Vaccines and diagnostics target genes assumed stable; if the pan-genome is open and "
                      "genes flow freely, today's target may be gone tomorrow. The question also decides "
                      "whether bacterial species are meaningful genetic units or temporary coalitions - "
                      "with consequences for how we name, track, and regulate microbes."),
  "sig_lens": ("The Signature lens treats the pan-genome as a public library with no catalog limit: the "
               "question is not how many books the library holds but the rules by which books enter, "
               "circulate, and are never discarded."),
  "sol_public": ("The Signature system proposes library-rule discovery: track gene gain and loss in "
                 "real time in natural populations, measure the circulation rules, and test whether "
                 "openness persists under unbiased sampling. Learn the library's rules, not just its "
                 "size. Full treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) openness is a biological property, not just sampling bias; (2) "
              "gene flow follows discoverable rules; (3) real-time tracking is now feasible. Reasoning "
              "path: the field argues from accumulated genome collections - static snapshots with biased "
              "sampling. Replace snapshots with movies: densely sample natural populations over time "
              "(wastewater, long-term gut cohorts, ocean time series), sequence deeply, and watch genes "
              "enter, spread, and vanish. Measure the circulation rules directly: which genes persist, "
              "which are transient, what drives acquisition. Then test openness properly: does the "
              "discovery curve flatten under unbiased, saturated sampling, or hold its power law? "
              "Proposed mechanism: pan-genome observatories - longitudinal deep-sequencing of model "
              "populations with gene-flow tracking, plus saturation-sequencing tests of the discovery "
              "curve. What would confirm it: measured circulation rules predicting gene persistence, "
              "and discovery curves definitively flattening or holding under unbiased sampling. What "
              "would kill it: curves that always reflect sampling effort - proving openness is an "
              "artifact - or gene flow too chaotic for any rules. What it does NOT claim: that all "
              "pan-genomes are open, that core genes are unimportant, or that vaccines are doomed. "
              "Where the honest answer is unknown - whether any pan-genome is truly infinite - we say "
              "so: the observatories must watch long enough to tell."),
  "key_points": [
   "E. coli's pan-genome exceeds 100,000 gene families and keeps growing with each new genome.",
   "Some species have closed pan-genomes; many have open ones following a power law.",
   "The public-goods hypothesis: genes are communal resources, individuals carry subsets.",
   "Sampling bias haunts the question: we sequence convenient strains, and rare genes may be artifacts.",
   "Openness affects vaccine targets, diagnostics, and whether species are real genetic units."],
  "requirements": [
   "Track gene gain and loss in real time in longitudinally sampled natural populations.",
   "Confirm: measured circulation rules predict gene persistence; discovery curves flatten or hold under unbiased sampling.",
   "Refute: curves always reflect sampling effort - openness is pure artifact.",
   "Refute: gene flow too chaotic for any discoverable rules."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim all pan-genomes are open or that vaccines are doomed.",
   "It must survive the saturation test: sampling must be unbiased and deep enough to decide."],
  "citations": [CIT_PANGENOME],
 },
 {
  "key": "tree-or-web",
  "name": "Tree or Web? The Shape of Microbial Evolution",
  "group": "Origins of Complexity",
  "ladder_rank": 34, "ladder_tier": "advanced",
  "description": ("The tree of life is biology's central image - but for microbes it may be the wrong "
                  "shape. Horizontal gene transfer weaves genes between branches so pervasively that some "
                  "biologists argue microbial evolution is a web, not a tree. After decades of debate, the "
                  "deepest question about life's history - what shape it even has - is still open."),
  "problem": "Is microbial evolution fundamentally tree-like with horizontal noise, or a network in which the tree is the noise?",
  "background": ("Carl Woese's ribosomal RNA tree gave microbiology its backbone, but whole genomes "
                 "told a messier story: different genes give different trees. Ford Doolittle argued in "
                 "1999 that rampant transfer makes a single universal tree impossible in principle - "
                 "\"phylogenetic classification and the universal tree\" may be a category error for "
                 "prokaryotes. The counter-movement found a \"statistical tree of life\": Eugene Koonin "
                 "showed that despite transfer, a consistent central trend - mostly ribosomal and core "
                 "informational genes - recovers the same deep topology, suggesting a real tree with "
                 "web-like noise. The debate now turns on quantification: what fraction of genes follow "
                 "the tree, does the answer change with depth and lineage, and do the transferred genes "
                 "carry the ecologically important functions while the tree carries only the machinery? "
                 "No agreed metric settles it."),
  "why_it_matters": ("The shape of evolution decides how we classify all microbes, reconstruct ancestors "
                      "like LUCA, and interpret every genome: a web means genes have independent "
                      "histories and species are temporary coalitions; a tree means vertical descent still "
                      "rules. Textbooks, taxonomy, and evolutionary theory all hang on the answer."),
  "sig_lens": ("The Signature lens treats the debate as a signal-processing problem: the tree is a "
               "low-frequency signal, transfer is high-frequency noise - and the argument is really "
               "about which frequency carries the meaning."),
  "sol_public": ("The Signature system proposes frequency decomposition: quantify tree-signal versus "
                 "transfer-signal per gene, per lineage, per depth - and let the measured spectrum, not "
                 "philosophy, declare the shape. Decompose the signal before naming the shape. Full "
                 "treatment: the Signature edition record."),
  "sol_sig": (LABEL + " Assumptions: (1) tree-signal and transfer-signal are both real and measurable; "
              "(2) their balance varies by gene class, lineage, and depth; (3) an agreed metric can be "
              "defined. Reasoning path: both camps are partly right, which is why the debate never ends "
              "- Doolittle is right that many genes ignore the tree, Koonin is right that a central "
              "trend persists. Stop arguing extremes and measure the spectrum: for thousands of gene "
              "families across the prokaryotic tree, compute tree-congruence scores - how well each "
              "gene's history matches the ribosomal backbone - and map how congruence varies with gene "
              "function, evolutionary depth, and ecological lifestyle. The result is not a slogan but a "
              "measured decomposition: X percent of the genome is tree-like, Y percent is web-like, and "
              "here is which functions live in each. Proposed mechanism: a tree-web atlas - standardized "
              "congruence metrics computed over the full prokaryotic genome set, stratified by function "
              "and depth, with explicit tests of whether informational versus operational genes split "
              "as predicted. What would confirm it: a stable, reproducible spectrum - the field's first "
              "quantitative answer - showing where tree thinking works and where web thinking is "
              "required. What would kill it: congruence scores proving method-dependent, with every "
              "metric giving a different spectrum - leaving the shape a matter of taste. What it does NOT "
              "claim: that the spectrum ends the debate by itself, that one shape fits all microbes, or "
              "that the tree is dead. Where the honest answer is unknown - the true spectrum - we say so: "
              "the atlas must measure it."),
  "key_points": [
   "Woese's rRNA tree gave microbiology its backbone; whole genomes tell a messier story.",
   "Doolittle (1999) argued rampant transfer makes a universal tree impossible in principle.",
   "Koonin's statistical tree: core informational genes still recover a consistent deep topology.",
   "Open questions: what fraction of genes follow the tree, and do transferred genes carry the important functions?",
   "No agreed metric currently settles tree versus web."],
  "requirements": [
   "Compute tree-congruence spectra for thousands of gene families across prokaryotes.",
   "Confirm: a stable, reproducible spectrum showing where tree versus web thinking applies.",
   "Refute: congruence scores prove method-dependent with every metric disagreeing.",
   "Refute: the spectrum collapses to triviality - all genes tree-like or all web-like."],
  "standards": [
   "This approach is a proposed path, not an established result; it claims no proof and no peer acceptance.",
   "It does not claim the spectrum ends debate or that one shape fits all microbes.",
   "It must survive the metric test: results must be robust across methods, not metric artifacts."],
  "citations": [CIT_TREEVWEB],
 },
]
