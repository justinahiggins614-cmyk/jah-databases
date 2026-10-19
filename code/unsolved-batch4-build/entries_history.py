#!/usr/bin/env python3
"""Entries for the Unsolved History databases (batch 4).

34 famous open problems in history, ladder-ordered by accessibility.
ID prefixes: JAH-USHI- (public) and JAH-USHIS- (signature), verified free
in the manifest id_prefix values (exact + substring, 2026-10-18) and across
all shard index files in jah-databases-data-1.

Evidence is separated from speculation throughout; contested claims are
never presented as settled. No website references. No Facebook.
No religious framing. Nothing hate-adjacent, profane, or inappropriate.
"""

ENTRIES = [
    dict(
        key="history-01",
        name="The Fall of Rome: The Single Cause",
        group="Ancient",
        ladder_rank=1,
        ladder_tier="foundations",
        problem=("Was there a single cause of Rome's fall - barbarians, "
                 "plague, economy, climate - or is the search for one "
                 "itself the error?"),
        background=("Gibbon blamed Christianity; modern scholars blame "
                    "everything from lead pipes to the Antonine Plague to "
                    "fiscal crisis to Germanic migrations. The Eastern "
                    "Empire survived another thousand years, which any "
                    "single-cause theory must explain. The current "
                    "consensus leans multi-causal - but multi-causal can "
                    "be an excuse for not ranking causes."),
        why_it_matters=("Rome's fall is history's archetypal collapse. Its "
                        "cause - or causes - is the template for every "
                        "decline narrative since."),
        sig_lens=("The Signature lens treats the fall as a ranking ledger: "
                  "the Signature approach asks which causes were "
                  "necessary, which sufficient, which incidental."),
        sig_body=("The Signature proposal models the fall as a fiscal-"
                  "military spiral. Assumptions: (1) the empire's army "
                  "was its largest expense; (2) plagues and climate "
                  "shocks cut revenue; (3) barbarian pressure raised "
                  "costs. Reasoning path: the proposal shows revenue "
                  "shocks plus cost pressures created a spiral - fewer "
                  "revenues, weaker armies, more invasions, fewer "
                  "revenues - predicting the West, with its thinner "
                  "tax base, should fall first, which it did. "
                  "Christianity, lead, and moral decline are then "
                  "incidental. Limits: the model needs better fiscal "
                  "data; the East's survival needs fuller accounting."),
        pointer=('The Signature system models the fall as a fiscal-military spiral, ranking revenue shocks and cost pressures above incidental causes. The Signature test: fiscal-military indicators predict the West-East divergence. It would be refuted if the West falls with fiscal and military indicators healthy.'),
        key_points=[
            "Single-cause theories span Christianity to lead pipes.",
            "The Eastern Empire survived a millennium longer.",
            "Plague, climate, and fiscal crisis have recent support.",
            "Multi-causal consensus may avoid ranking causes.",
        ],
        requirements=[
            "A ranked causal account, not just a list.",
            "An explanation for Eastern survival.",
            "Fiscal and military data grounding.",
        ],
        standards=[
            "Claims checked against the late-antiquity literature; speculation marked.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Gibbon E. The Decline and Fall of the Roman Empire. 1776.",
            "Heather P. The Fall of the Roman Empire. Oxford University Press; 2005.",
        ],
        hypotheses=[
            "A fiscal-military spiral is the core mechanism.",
            "Barbarian migrations were decisive.",
            "Plague and climate drove the fall.",
            "No ranking is possible; the causes are inseparable.",
        ],
        confirm="Fiscal-military indicators predict the West-East divergence.",
        refute="The West falls with fiscal and military indicators healthy.",
    ),
    dict(
        key="history-02",
        name="The Lost Colony of Roanoke",
        group="Early Modern",
        ladder_rank=2,
        ladder_tier="foundations",
        problem=("What happened to the 115 colonists of Roanoke - England's "
                 "first American colony - who vanished between 1587 and "
                 "1590, leaving only the word CROATOAN?"),
        background=("John White returned from England to find the settlement "
                    "dismantled and the colonists gone. Theories: assimilation "
                    "with the Croatoan (Hatteras) people, massacre, starvation "
                    "and dispersal, or relocation inland. Archaeology at "
                    "Hatteras Island finds European artifacts in native "
                    "contexts; DNA studies are inconclusive. The single "
                    "carved word remains the only message."),
        why_it_matters=("Roanoke is America's founding mystery - the moment "
                        "English colonization nearly failed before it began."),
        sig_lens=("The Signature lens treats the colony as a supply ledger: "
                  "the Signature approach asks what 115 people do when the "
                  "ships do not come."),
        sig_body=("The Signature proposal models the disappearance as "
                  "planned dispersal. Assumptions: (1) White had agreed "
                  "the colonists would relocate if threatened; (2) the "
                  "settlement was carefully dismantled, not destroyed; (3) "
                  "CROATOAN named the agreed destination. Reasoning path: "
                  "the proposal shows the evidence - orderly dismantling, "
                  "a destination message, no signs of massacre - matches "
                  "a planned move to Croatoan Island, where archaeology "
                  "now finds assimilation evidence. The 'mystery' is then "
                  "a failure of follow-up, not of explanation. Limits: "
                  "the assimilation evidence is suggestive, not "
                  "conclusive; the colonists' ultimate fate is unknown."),
        pointer=('The Signature system reads the evidence as planned dispersal to Croatoan, with the mystery being failed follow-up rather than failed explanation. The Signature test: hatteras finds confirm sustained assimilation. It would be refuted if massacre evidence appears at the Roanoke site.'),
        key_points=[
            "115 colonists vanished between 1587 and 1590.",
            "The settlement was dismantled; CROATOAN was carved.",
            "No massacre evidence has been found.",
            "Hatteras archaeology shows European-native contact.",
        ],
        requirements=[
            "An account of the orderly dismantling.",
            "Archaeological or genetic confirmation of assimilation.",
            "An explanation for White's failed follow-up.",
        ],
        standards=[
            "Claims checked against the Roanoke literature; speculation marked.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Horn J. A Kingdom Strange. Basic Books; 2010.",
            "Lawler A. The Secret Token. Doubleday; 2018.",
        ],
        hypotheses=[
            "Planned dispersal and assimilation with the Croatoan.",
            "Massacre by hostile groups.",
            "Starvation and scattered survival.",
            "Relocation inland to the Chowan River.",
        ],
        confirm="Hatteras finds confirm sustained assimilation.",
        refute="Massacre evidence appears at the Roanoke site.",
    ),
    dict(
        key="history-03",
        name="The Princes in the Tower",
        group="Medieval",
        ladder_rank=3,
        ladder_tier="foundations",
        problem=("What happened to Edward V and his brother Richard - the "
                 "boy princes last seen in the Tower of London in 1483?"),
        background=("After Edward IV's death, his sons were lodged in the "
                    "Tower by their uncle, who became Richard III; the boys "
                    "were never seen again. Bones found in 1674 may be "
                    "theirs but have never been DNA-tested (royal refusal). "
                    "Richard III is the traditional culprit, but Henry VII "
                    "had motive too, and some argue the boys survived. "
                    "The case has divided historians for five centuries."),
        why_it_matters=("The princes' fate determined the Tudor succession "
                        "and blackened Richard III's name - history written "
                        "by the winners, perhaps literally."),
        sig_lens=("The Signature lens treats the case as a motive ledger: "
                  "the Signature approach asks who gained from the boys' "
                  "disappearance and who gained from blaming Richard."),
        sig_body=("The Signature proposal models the case as a "
                  "succession-risk calculation. Assumptions: (1) living "
                  "princes threatened any usurper; (2) Richard III seized "
                  "the throne in 1483; (3) Tudor narratives had motive to "
                  "blacken Richard. Reasoning path: the proposal shows "
                  "Richard had the strongest immediate motive and "
                  "opportunity - but that the Tudor sources describing "
                  "the murder are also the least trustworthy, predicting "
                  "that DNA testing of the 1674 bones is the only "
                  "decisive evidence. Until the royal refusal lifts, the "
                  "case stays open by institutional choice, not evidential "
                  "necessity. Limits: the model cannot resolve the case "
                  "without the bones; alternative culprits remain "
                  "possible."),
        pointer=('The Signature system weighs motive against source reliability, identifying DNA testing of the 1674 bones as the decisive blocked evidence. The Signature test: dNA testing identifies the bones as the princes. It would be refuted if dNA testing excludes the princes.'),
        key_points=[
            "Two boy princes vanished from the Tower in 1483.",
            "Bones found in 1674 were never DNA-tested.",
            "Richard III is the traditional suspect; Henry VII had motive too.",
            "Tudor sources are the least trustworthy narrators.",
        ],
        requirements=[
            "DNA analysis of the 1674 bones.",
            "Source-critical evaluation of Tudor narratives.",
            "Motive analysis for all suspects.",
        ],
        standards=[
            "Claims checked against the Ricardian literature on all sides.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Weir A. The Princes in the Tower. Ballantine; 1992.",
            "Hicks M. Richard III. Tempus; 2000.",
        ],
        hypotheses=[
            "Richard III ordered the murders.",
            "Henry VII or his agents were responsible.",
            "The boys survived in obscurity.",
            "The 1674 bones are unrelated.",
        ],
        confirm="DNA testing identifies the bones as the princes.",
        refute="DNA testing excludes the princes.",
    ),
    dict(
        key="history-04",
        name="The Man in the Iron Mask",
        group="Early Modern",
        ladder_rank=4,
        ladder_tier="foundations",
        problem=("Who was the masked prisoner held in French fortresses "
                 "from 1669 until his death in 1703?"),
        background=("Voltaire started the legend; Dumas made it immortal. "
                    "The prisoner wore a velvet (not iron) mask and was "
                    "treated with strange deference. Candidates: Louis "
                    "XIV's twin brother, his disgraced minister Fouquet's "
                    "valet, the Italian diplomat Matthioli, or an "
                    "embarrassing secret of state. Archives have narrowed "
                    "but not closed the field."),
        why_it_matters=("The mask is the symbol of absolute power's secrets - "
                        "and a test of how history handles a mystery the "
                        "archives almost answer."),
        sig_lens=("The Signature lens treats the prisoner as a secret ledger: "
                  "the Signature approach asks what secret was worth "
                  "thirty-four years of luxury imprisonment."),
        sig_body=("The Signature proposal models the prisoner as a "
                  "diplomatic embarrassment, not a royal twin. Assumptions: "
                  "(1) the deference suggests high status or high "
                  "sensitivity; (2) the mask prevented recognition; (3) "
                  "the long imprisonment needed ongoing justification. "
                  "Reasoning path: the proposal shows the Matthioli "
                  "hypothesis - a diplomat who double-crossed Louis XIV - "
                  "best fits the deference (a gentleman) and the secrecy "
                  "(diplomatic scandal), while the twin theory lacks any "
                  "documentary support. The mask then hid a known face "
                  "from fellow prisoners. Limits: the archives are "
                  "incomplete; the valet theory also fits the deference "
                  "poorly."),
        pointer=('The Signature system favors the diplomatic-embarrassment account over the royal-twin legend, fitting the deference and secrecy. The Signature test: archival records name the prisoner definitively. It would be refuted if documents prove the leading candidates were elsewhere.'),
        key_points=[
            "A masked prisoner held 1669 to 1703 with strange deference.",
            "The mask was velvet, not iron.",
            "Twin brother, valet, and diplomat theories compete.",
            "Archives narrowed but did not close the case.",
        ],
        requirements=[
            "Documentary support for the chosen candidate.",
            "An account of the deference and the mask.",
            "Explanation for the 34-year duration.",
        ],
        standards=[
            "Claims checked against the archival literature; legend marked.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Voltaire. Le Siecle de Louis XIV. 1751.",
            "Noone J. The Man Behind the Iron Mask. 1988.",
        ],
        hypotheses=[
            "The diplomat Matthioli, hidden for double-dealing.",
            "Fouquet's valet, knowing too much.",
            "Louis XIV's twin brother.",
            "A state secret of another kind entirely.",
        ],
        confirm="Archival records name the prisoner definitively.",
        refute="Documents prove the leading candidates were elsewhere.",
    ),
    dict(
        key="history-05",
        name="Jack the Ripper: The Historical Verdict",
        group="Modern",
        ladder_rank=5,
        ladder_tier="foundations",
        problem=("Can history ever identify Jack the Ripper - and what does "
                 "the century of suspect-mongering reveal about evidence?"),
        background=("Five canonical murders in Whitechapel, 1888; the killer "
                    "was never caught. Suspects number in the hundreds - "
                    "royalty, artists, doctors, immigrants. Modern claims "
                    "(DNA on a shawl, facial analysis) have not survived "
                    "scrutiny. The serious historical question is "
                    "methodological: with contaminated evidence and lost "
                    "records, is identification possible even in principle?"),
        why_it_matters=("The Ripper is the template for unsolved crime. The "
                        "case tests the limits of historical detection."),
        sig_lens=("The Signature lens treats the case as an evidence ledger: "
                  "the Signature approach asks what the surviving record "
                  "can possibly prove."),
        sig_body=("The Signature proposal models the case as "
                  "underdetermined by surviving evidence. Assumptions: (1) "
                  "1888 forensics were minimal; (2) records were lost and "
                  "contaminated; (3) suspect theories outrun evidence. "
                  "Reasoning path: the proposal shows no suspect can be "
                  "distinguished from the alternatives on the surviving "
                  "record - the honest verdict is permanent uncertainty, "
                  "and each new 'solution' reveals more about its era's "
                  "anxieties (immigrants, aristocrats, doctors) than about "
                  "1888. The case is then a mirror, not a puzzle. Limits: "
                  "a genuine archival breakthrough remains possible; the "
                  "model predicts continued false solutions."),
        pointer=("The Signature system argues the surviving record underdetermines any suspect, making the case a mirror of each era's anxieties. The Signature test: uncontaminated evidence links one suspect definitively. It would be refuted if no new evidence emerges; the industry continues."),
        key_points=[
            "Five canonical murders, 1888; never solved.",
            "Hundreds of suspects proposed over a century.",
            "Modern forensic claims have not survived scrutiny.",
            "Evidence was minimal, lost, and contaminated.",
        ],
        requirements=[
            "Evidence distinguishing one suspect from alternatives.",
            "Source criticism of the suspect industry.",
            "An account of why solutions keep failing.",
        ],
        standards=[
            "Claims checked against the serious Ripper literature; sensationalism excluded.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Begg P. Jack the Ripper: The Definitive History. Longman; 2003.",
            "Rumbelow D. The Complete Jack the Ripper. 1975.",
        ],
        hypotheses=[
            "The case is permanently underdetermined.",
            "A Polish immigrant barber (Kosminski) was the killer.",
            "Archival breakthrough will eventually identify him.",
            "The canonical five include copycat murders.",
        ],
        confirm="Uncontaminated evidence links one suspect definitively.",
        refute="No new evidence emerges; the industry continues.",
    ),
    dict(
        key="history-06",
        name="The Black Death: Which Pathogen",
        group="Medieval",
        ladder_rank=6,
        ladder_tier="foundations",
        problem=("Was the Black Death really bubonic plague - Yersinia pestis "
                 "- or did other pathogens contribute?"),
        background=("The 1347-1352 pandemic killed a third of Europe. "
                    "Traditional accounts blame Yersinia pestis, and "
                    "ancient DNA has confirmed its presence in victims. "
                    "But the medieval spread was faster than modern plague, "
                    "and some argue for anthrax, Ebola-like viruses, or a "
                    "multi-pathogen event. The DNA evidence is strong but "
                    "the epidemiology remains puzzling."),
        why_it_matters=("The Black Death reshaped Europe - labor, religion, "
                        "medicine. Its true nature determines what we learn "
                        "for future pandemics."),
        sig_lens=("The Signature lens treats the plague as a transmission "
                  "ledger: the Signature approach asks what spread fast "
                  "enough to match the medieval velocity."),
        sig_body=("The Signature proposal models the pandemic as Yersinia "
                  "plus pneumonic transmission. Assumptions: (1) ancient "
                  "DNA confirms Yersinia in victims; (2) bubonic spread is "
                  "too slow for the observed velocity; (3) pneumonic plague "
                  "spreads person-to-person rapidly. Reasoning path: the "
                  "proposal shows the DNA evidence settles the pathogen "
                  "while the epidemiology requires the pneumonic form - "
                  "predicting the medieval mortality pattern (winter "
                  "peaks, rapid urban spread) matches pneumonic "
                  "transmission. One pathogen, two transmission modes. "
                  "Limits: the model needs better medieval transmission "
                  "data; co-pathogens cannot be fully excluded."),
        pointer=('The Signature system reconciles DNA evidence with medieval velocity through pneumonic transmission of Yersinia pestis. The Signature test: transmission modeling matches pneumonic patterns. It would be refuted if non-Yersinia pathogens dominate victim DNA.'),
        key_points=[
            "Killed roughly a third of Europe, 1347-1352.",
            "Ancient DNA confirms Yersinia pestis in victims.",
            "Medieval spread was faster than modern bubonic plague.",
            "Alternative-pathogen theories persist.",
        ],
        requirements=[
            "Reconciliation of DNA evidence with epidemiology.",
            "Transmission-mode analysis.",
            "An account of the speed anomaly.",
        ],
        standards=[
            "Claims checked against the plague literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Bramanti B et al. Plague: a review. 2016.",
            "Green MH. The Black Death: a turning point. 2014.",
        ],
        hypotheses=[
            "Yersinia with pneumonic transmission explains everything.",
            "Multiple pathogens contributed.",
            "Medieval Yersinia was a more virulent strain.",
            "The epidemiology is mismeasured; bubonic suffices.",
        ],
        confirm="Transmission modeling matches pneumonic patterns.",
        refute="Non-Yersinia pathogens dominate victim DNA.",
    ),
    dict(
        key="history-07",
        name="The Great Divergence: Why Europe",
        group="Early Modern",
        ladder_rank=7,
        ladder_tier="foundations",
        problem=("Why did Europe - not China, India, or the Islamic world - "
                 "industrialize first?"),
        background=("In 1700, China and India rivaled or exceeded Europe "
                    "economically; by 1850 Europe dominated. Explanations: "
                    "coal and colonies (Pomeranz), institutions (North, "
                    "Acemoglu), culture (Weber, Landes), fragmented "
                    "competition (Jones), or contingency. The California "
                    "School narrowed the gap to 1800, making the divergence "
                    "sudden - and harder to explain."),
        why_it_matters=("The divergence created the modern world order. Its "
                        "cause determines whether development has a formula."),
        sig_lens=("The Signature lens treats the divergence as a "
                  "conjuncture ledger: the Signature approach asks what "
                  "combination was necessary and where it existed."),
        sig_body=("The Signature proposal models industrialization as a "
                  "conjuncture of coal, competition, and institutions. "
                  "Assumptions: (1) industrialization needed cheap energy, "
                  "competitive pressure, and secure property; (2) no "
                  "region had all three until England around 1800; (3) "
                  "China had coal and scale but less competitive "
                  "fragmentation. Reasoning path: the proposal shows each "
                  "single-cause theory fails somewhere - coal alone "
                  "(China had it), institutions alone (they diffused) - "
                  "but the combination predicts England's priority. The "
                  "divergence was then contingent but explicable. Limits: "
                  "the model needs better comparative data; the "
                  "conjuncture risks being post hoc."),
        pointer=('The Signature system models industrialization as a conjuncture of coal, competition, and institutions that coincided first in England. The Signature test: conjuncture conditions predict industrialization timing. It would be refuted if a region with the full conjuncture fails to industrialize.'),
        key_points=[
            "In 1700 Asia rivaled Europe; by 1850 Europe dominated.",
            "Coal, colonies, institutions, culture, and competition compete.",
            "The California School narrowed the gap to around 1800.",
            "Single-cause theories each fail somewhere.",
        ],
        requirements=[
            "Comparative data across Eurasia.",
            "An account of why each single cause is insufficient.",
            "A testable conjuncture model.",
        ],
        standards=[
            "Claims checked against the divergence literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Pomeranz K. The Great Divergence. Princeton University Press; 2000.",
            "Acemoglu D, Robinson JA. Why Nations Fail. Crown; 2012.",
        ],
        hypotheses=[
            "A specific conjuncture explains England's priority.",
            "Institutions are the master cause.",
            "Coal and colonies were decisive.",
            "The divergence is overstated; Asia was never close.",
        ],
        confirm="Conjuncture conditions predict industrialization timing.",
        refute="A region with the full conjuncture fails to industrialize.",
    ),
    dict(
        key="history-08",
        name="What Happened to the Ninth Legion",
        group="Ancient",
        ladder_rank=8,
        ladder_tier="foundations",
        problem=("What happened to Rome's Legio IX Hispana - last recorded "
                 "around 120 CE, then gone from the records?"),
        background=("The Ninth served in Britain, likely built part of "
                    "Hadrian's Wall's predecessor works, then vanishes. "
                    "Theories: annihilated in Britain (the romantic "
                    "version), transferred to the continent and destroyed "
                    "in the East, or disbanded quietly after losses. No "
                    "battlefield, no inscription, no definitive record "
                    "marks its end - unusual for a legion."),
        why_it_matters=("The Ninth is the archetypal lost legion. Its fate "
                        "illuminates how Rome handled military disaster - "
                        "and how legend fills archival silence."),
        sig_lens=("The Signature lens treats the legion as an absence ledger: "
                  "the Signature approach asks what kinds of ends leave "
                  "no record."),
        sig_body=("The Signature proposal models the disappearance as "
                  "administrative dissolution. Assumptions: (1) destroyed "
                  "legions were usually reconstituted or commemorated; "
                  "(2) the Ninth's tiles and inscriptions stop without "
                  "fanfare; (3) quiet disbandment followed heavy losses "
                  "elsewhere. Reasoning path: the proposal shows the "
                  "pattern matches a legion worn down by detachments and "
                  "losses, then dissolved - predicting no battlefield "
                  "because there was no single battle. The romantic "
                  "annihilation is then legend filling silence. Limits: "
                  "the model cannot rule out an unattested disaster; "
                  "the evidence is genuinely thin."),
        pointer=("The Signature system models the Ninth's end as quiet administrative dissolution after attrition, not a single lost battle. The Signature test: detachments and losses trace the attrition pattern. It would be refuted if a battlefield with Ninth equipment is found."),
        key_points=[
            "Last recorded around 120 CE; then gone.",
            "No battlefield or terminal inscription found.",
            "Annihilation, transfer, and disbandment theories compete.",
            "The romantic version dominates popular culture.",
        ],
        requirements=[
            "An account of the archival silence.",
            "Tile and inscription distribution analysis.",
            "Separation of legend from evidence.",
        ],
        standards=[
            "Claims checked against the Roman military literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Breeze DJ. The Ninth Legion. 2018.",
            "Keppie L. Legions and Veterans. 1998.",
        ],
        hypotheses=[
            "Quiet disbandment after attrition.",
            "Annihilation in an unrecorded British disaster.",
            "Transfer east and destruction there.",
            "The records are lost, not the legion.",
        ],
        confirm="Detachments and losses trace the attrition pattern.",
        refute="A battlefield with Ninth equipment is found.",
    ),
    dict(
        key="history-09",
        name="The Tunguska Event: The Cause",
        group="Modern",
        ladder_rank=9,
        ladder_tier="foundations",
        problem=("What exploded over Tunguska, Siberia, in 1908 - flattening "
                 "2,000 square kilometers of forest with no crater?"),
        background=("The blast equaled 10-15 megatons; trees fell radially; "
                    "no impact crater or meteorite fragments were found. "
                    "The leading theory is an airbursting stony asteroid; "
                    "alternatives include a comet, a methane explosion, "
                    "and (fringe) stranger ideas. The remote site was not "
                    "studied scientifically until 1927, losing crucial "
                    "evidence."),
        why_it_matters=("Tunguska is the largest impact event in recorded "
                        "history. Its nature calibrates planetary-defense "
                        "risk."),
        sig_lens=("The Signature lens treats Tunguska as a physics ledger: "
                  "the Signature approach asks what explosion profile "
                  "matches the tree-fall pattern."),
        sig_body=("The Signature proposal models the event as a stony-"
                  "asteroid airburst. Assumptions: (1) the radial tree "
                  "pattern indicates an atmospheric explosion; (2) stony "
                  "bodies fragment under aerodynamic stress; (3) no "
                  "crater means no ground impact. Reasoning path: the "
                  "proposal shows airburst models reproduce the tree-fall "
                  "geometry and the missing crater - predicting the "
                  "blast height and energy from the pattern, which "
                  "matches a 50-60 meter stony object. The comet and "
                  "methane alternatives fit worse. Limits: no fragments "
                  "survive to confirm composition; the models have "
                  "free parameters."),
        pointer=('The Signature system models Tunguska as a stony-asteroid airburst, with the tree-fall geometry predicting blast height and energy. The Signature test: airburst models reproduce the full damage pattern. It would be refuted if meteorite fragments of non-asteroidal origin are found.'),
        key_points=[
            "1908 blast flattened 2,000 square kilometers; no crater.",
            "Energy estimated at 10-15 megatons.",
            "Airbursting asteroid is the leading theory.",
            "The site was not studied until 1927.",
        ],
        requirements=[
            "An explosion model matching the tree-fall pattern.",
            "An account of the missing crater and fragments.",
            "Composition evidence if obtainable.",
        ],
        standards=[
            "Claims checked against the Tunguska literature; fringe excluded.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Kulik L. Expedition reports. 1927.",
            "Chyba CF et al. Clues to the nature of the Tunguska event. 1993.",
        ],
        hypotheses=[
            "Stony asteroid airburst.",
            "Comet fragment airburst.",
            "Methane explosion from the ground.",
            "The evidence is insufficient to decide.",
        ],
        confirm="Airburst models reproduce the full damage pattern.",
        refute="Meteorite fragments of non-asteroidal origin are found.",
    ),
    dict(
        key="history-10",
        name="The Dancing Plague of 1518",
        group="Early Modern",
        ladder_rank=10,
        ladder_tier="foundations",
        problem=("Why did hundreds of people dance uncontrollably for days "
                 "in Strasbourg in 1518 - some reportedly to death?"),
        background=("The outbreak began with one woman and spread to "
                    "hundreds; authorities hired musicians, worsening it. "
                    "Theories: ergot poisoning (rejected - ergot disrupts "
                    "rather than coordinates movement), religious mania, "
                    "mass hysteria under famine and plague stress, or "
                    "choreomania as ritual. Similar outbreaks occurred "
                    "across medieval Europe."),
        why_it_matters=("The dancing plague is the strangest mass behavior "
                        "in recorded history - and a window into how stress "
                        "becomes epidemic."),
        sig_lens=("The Signature lens treats the dancing as a stress ledger: "
                  "the Signature approach asks what pressure made "
                  "bodies move."),
        sig_body=("The Signature proposal models the outbreak as "
                  "stress-induced mass psychogenic illness. Assumptions: "
                  "(1) Strasbourg suffered famine, plague, and social "
                  "strain; (2) dancing mania had religious precedent "
                  "(St. Vitus); (3) authorities' response amplified it. "
                  "Reasoning path: the proposal shows the outbreak "
                  "matches mass psychogenic patterns - spread through "
                  "suggestion among the stressed, prolonged by the "
                  "musicians hired to 'cure' it. Ergot fails because "
                  "poisoning does not synchronize. The deaths, if real, "
                  "came from exhaustion and stroke. Limits: the "
                  "contemporary sources are thin; the death toll is "
                  "uncertain."),
        pointer=("The Signature system models the outbreak as stress-induced mass psychogenic illness, amplified by the authorities' musical 'cure.' The Signature test: outbreak patterns match psychogenic spread models. It would be refuted if toxicology of the period supports ergot."),
        key_points=[
            "Hundreds danced for days in Strasbourg, 1518.",
            "Authorities hired musicians, worsening the outbreak.",
            "Ergot, mania, hysteria, and ritual theories compete.",
            "Similar choreomania outbreaks occurred across medieval Europe.",
        ],
        requirements=[
            "An account of the spread mechanism.",
            "Rejection or support of ergot with pharmacology.",
            "An explanation for the authorities' response.",
        ],
        standards=[
            "Claims checked against the choreomania literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Waller J. A Time to Dance, a Time to Die. Icon; 2008.",
            "Bartholomew RE. Dancing plagues. 1994.",
        ],
        hypotheses=[
            "Mass psychogenic illness under extreme stress.",
            "Ergot poisoning.",
            "Religious ritual gone wrong.",
            "The sources exaggerate; the event was smaller.",
        ],
        confirm="Outbreak patterns match psychogenic spread models.",
        refute="Toxicology of the period supports ergot.",
    ),
    dict(
        key="history-11",
        name="The Lost Franklin Expedition: The Full Story",
        group="Modern",
        ladder_rank=11,
        ladder_tier="foundations",
        problem=("What exactly destroyed Franklin's 1845 Arctic expedition - "
                 "and what do the wrecks Erebus and Terror reveal?"),
        background=("129 men vanished seeking the Northwest Passage. "
                    "Searches found the Victory Point note, Inuit "
                    "testimony of starving sailors, and evidence of lead "
                    "poisoning and cannibalism. The wrecks were found in "
                    "2014 and 2016, remarkably preserved. Open questions: "
                    "the expedition's final movements, the role of lead, "
                    "and how much Inuit testimony - long dismissed - was "
                    "right."),
        why_it_matters=("Franklin is the Arctic's great tragedy - and a "
                        "case study in how indigenous knowledge was "
                        "ignored."),
        sig_lens=("The Signature lens treats the expedition as a logistics "
                  "ledger: the Signature approach asks when the ships "
                  "became traps."),
        sig_body=("The Signature proposal models the disaster as "
                  "compounding logistical failure. Assumptions: (1) the "
                  "ships were ice-bound in 1846; (2) provisions and fuel "
                  "were finite; (3) Inuit testimony accurately described "
                  "the retreat. Reasoning path: the proposal shows no "
                  "single cause - lead, scurvy, cold, poor planning - "
                  "suffices, but their sum made survival impossible once "
                  "the ships were abandoned. The wrecks' locations "
                  "confirm the southward drift. Inuit accounts, once "
                  "dismissed, prove the most reliable source. Limits: "
                  "the wrecks' full excavation is ongoing; the lead "
                  "question is unresolved."),
        pointer=('The Signature system models the disaster as compounding logistical failure, with Inuit testimony vindicated as the best source. The Signature test: wreck excavation confirms the Inuit-described retreat. It would be refuted if lead levels prove too low to matter.'),
        key_points=[
            "129 men vanished; the wrecks were found in 2014 and 2016.",
            "Evidence: lead poisoning, scurvy, cannibalism.",
            "Inuit testimony was long dismissed, now vindicated.",
            "The Victory Point note is the only written record.",
        ],
        requirements=[
            "Integration of wreck archaeology with Inuit testimony.",
            "Resolution of the lead-poisoning question.",
            "A timeline of the final retreat.",
        ],
        standards=[
            "Claims checked against the Franklin literature; Inuit sources centered.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Woodman DC. Unravelling the Franklin Mystery. McGill-Queen's; 1991.",
            "Stenton DR et al. Archaeology of the Franklin expedition. 2018.",
        ],
        hypotheses=[
            "Compounding logistical failure destroyed the expedition.",
            "Lead poisoning was the primary cause.",
            "The expedition could have survived with Inuit methods.",
            "The wrecks will rewrite the timeline.",
        ],
        confirm="Wreck excavation confirms the Inuit-described retreat.",
        refute="Lead levels prove too low to matter.",
    ),
    dict(
        key="history-12",
        name="Who Betrayed Anne Frank",
        group="Modern",
        ladder_rank=12,
        ladder_tier="compounded",
        problem=("Who betrayed the Frank family's hiding place to the Nazis "
                 "in August 1944?"),
        background=("The 2022 cold-case investigation named a Jewish notary, "
                    "Arnold van den Bergh - igniting fierce backlash from "
                    "historians who called the evidence thin. Earlier "
                    "suspects included a warehouse worker and chance "
                    "discovery during a ration-fraud raid. The annex's "
                    "betrayal may have been accidental rather than "
                    "deliberate - and the controversy shows how evidence "
                    "standards collide with the hunger for answers."),
        why_it_matters=("The betrayal is the hinge of the most famous "
                        "Holocaust story. Naming the betrayer - or "
                        "admitting we cannot - is a matter of historical "
                        "responsibility."),
        sig_lens=("The Signature lens treats the case as an evidence ledger: "
                  "the Signature approach asks what standard of proof a "
                  "posthumous accusation requires."),
        sig_body=("The Signature proposal models the case as "
                  "underdetermined with asymmetric costs. Assumptions: (1) "
                  "the surviving evidence is fragmentary; (2) false "
                  "accusation harms the innocent dead; (3) the raid may "
                  "have been incidental. Reasoning path: the proposal "
                  "shows no suspect meets a responsible standard of proof "
                  "- and that the 2022 accusation failed exactly where "
                  "standards matter most (anonymous note, thin motive). "
                  "The honest verdict is structured uncertainty: a "
                  "ranked suspect list, not a name. Limits: new archives "
                  "could change the ranking; the model cannot produce "
                  "the answer, only discipline the search."),
        pointer=('The Signature system argues for structured uncertainty with ranked suspects, holding posthumous accusation to strict proof standards. The Signature test: archival evidence meets strict proof standards for one suspect. It would be refuted if no suspect ever meets the standard; the case stays open.'),
        key_points=[
            "The Frank family was arrested in August 1944.",
            "The 2022 investigation named a suspect; historians revolted.",
            "Earlier theories included accident and other suspects.",
            "Evidence standards collide with the hunger for answers.",
        ],
        requirements=[
            "A responsible standard of proof for accusation.",
            "Source criticism of the anonymous note.",
            "An account of the raid's possible incidental nature.",
        ],
        standards=[
            "Claims checked against the serious literature; sensitivity observed.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
                       "Sullivan R et al. The Betrayal of Anne Frank. Harper; 2022.",
            "Van der Boom B. Response to the cold case investigation. 2022.",
        ],
        hypotheses=[
            "The case is underdetermined; no responsible accusation is possible.",
            "Van den Bergh was the betrayer.",
            "The raid was incidental to ration-fraud investigation.",
            "A warehouse employee betrayed the annex.",
        ],
        confirm="Archival evidence meets strict proof standards for one suspect.",
        refute="No suspect ever meets the standard; the case stays open.",
    ),
    dict(
        key="history-13",
        name="The Fate of the Romanovs: The Full Account",
        group="Modern",
        ladder_rank=13,
        ladder_tier="compounded",
        problem=("What exactly happened to the Romanov family in 1918 - and "
                 "were any of the children spared?"),
        background=("The imperial family was executed in Ekaterinburg in "
                    "July 1918; DNA identified most remains in the 1990s, "
                    "and the last two children in 2007. Yet impostor claims "
                    "(Anastasia) persisted for decades, and questions "
                    "remain: the full chain of orders, the disposal of "
                    "bodies, and whether the execution was ordered from "
                    "Moscow or decided locally."),
        why_it_matters=("The Romanov murders ended three centuries of "
                        "autocracy and became the founding crime of the "
                        "Soviet era. The full account matters for "
                        "historical justice."),
        sig_lens=("The Signature lens treats the murders as a command ledger: "
                  "the Signature approach asks who ordered, who obeyed, "
                  "and who covered up."),
        sig_body=("The Signature proposal models the execution as locally "
                  "decided, centrally approved. Assumptions: (1) the Ural "
                  "Soviet feared a White rescue; (2) communications with "
                  "Moscow were ambiguous; (3) the cover-up suggests "
                  "awareness of the crime's weight. Reasoning path: the "
                  "proposal shows the evidence fits local initiative "
                  "with subsequent central endorsement - predicting the "
                  "documentary gaps (no explicit Lenin order) and the "
                  "elaborate disposal. The impostor industry then "
                  "reflects the cover-up's success, not survival. "
                  "Limits: the archives remain partially closed; the "
                  "model cannot fully exclude a direct order."),
        pointer=('The Signature system models the execution as locally decided with central endorsement, explaining the documentary gaps. The Signature test: archives reveal the order chain definitively. It would be refuted if documents prove a direct Lenin order.'),
        key_points=[
            "The family was executed in Ekaterinburg, July 1918.",
            "DNA identified all remains by 2007.",
            "Impostor claims persisted for decades.",
            "The chain of orders remains partly obscure.",
        ],
        requirements=[
            "An account of the order chain.",
            "Explanation of the body disposal.",
            "An account of the impostor phenomenon.",
        ],
        standards=[
            "Claims checked against the Romanov literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Massie RK. The Romanovs: The Final Chapter. Random House; 1995.",
            "Slater W. The many deaths of Nicholas II. 2007.",
        ],
        hypotheses=[
            "Local decision with central endorsement.",
            "Direct order from Moscow.",
            "The execution was improvised, not planned.",
            "Archives will eventually settle the chain.",
        ],
        confirm="Archives reveal the order chain definitively.",
        refute="Documents prove a direct Lenin order.",
    ),
    dict(
        key="history-14",
        name="The Green Children of Woolpit",
        group="Medieval",
        ladder_rank=14,
        ladder_tier="compounded",
        problem=("Who were the green-skinned children found at Woolpit, "
                 "England, in the 12th century - and what is the truth "
                 "behind the legend?"),
        background=("Chroniclers report two green children, speaking an "
                    "unknown language, found near Bury St Edmunds around "
                    "1150. The girl survived, learned English, and said "
                    "they came from a twilight land. Theories: Flemish "
                    "immigrants' children (green from malnutrition), "
                    "chlorosis, folklore elaboration, or - in fringe "
                    "telling - something stranger. The historical core "
                    "beneath the legend is the puzzle."),
        why_it_matters=("The green children are medieval England's strangest "
                        "story - and a test of how historians extract fact "
                        "from wonder."),
        sig_lens=("The Signature lens treats the legend as a kernel ledger: "
                  "the Signature approach asks what real event the wonder "
                  "grew around."),
        sig_body=("The Signature proposal models the story as displaced "
                    "children plus folklore. Assumptions: (1) the "
                    "chroniclers recorded a real encounter; (2) green "
                    "skin suggests chlorosis or malnutrition; (3) the "
                    "'twilight land' is folklore framing. Reasoning path: "
                    "the proposal shows Flemish immigrant children - "
                    "displaced by persecution, malnourished, speaking "
                    "Flemish - fit every mundane detail, with the "
                    "marvelous elements accreting in retelling. The "
                    "legend then preserves a real tragedy of displaced "
                    "children. Limits: the identification is "
                    "circumstantial; the sources are thin."),
        pointer=('The Signature system models the story as displaced Flemish children wrapped in folklore, with malnutrition explaining the green skin. The Signature test: parish records identify Flemish displaced children. It would be refuted if no mundane core fits the earliest accounts.'),
        key_points=[
            "Two green children found near Woolpit, around 1150.",
            "The girl survived and described a twilight land.",
            "Flemish immigrant and malnutrition theories lead.",
            "Fringe theories invoke stranger explanations.",
        ],
        requirements=[
            "A mundane core fitting all reported details.",
            "An account of the folklore accretion.",
            "Separation of chronicler reliability by detail.",
        ],
        standards=[
            "Claims checked against the Woolpit literature; fringe excluded.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Clark J. The Green Children of Woolpit. 2006.",
            "Cohen J. Green children from another world. 2008.",
        ],
        hypotheses=[
            "Displaced Flemish children, malnourished, folklorized.",
            "Chlorosis in local children, elaborated.",
            "The chroniclers invented the story.",
            "A genuine unexplained event.",
        ],
        confirm="Parish records identify Flemish displaced children.",
        refute="No mundane core fits the earliest accounts.",
    ),
    dict(
        key="history-15",
        name="The South Sea Bubble: Why the Mania",
        group="Early Modern",
        ladder_rank=15,
        ladder_tier="compounded",
        problem=("Why did the South Sea Bubble inflate and burst in 1720 - "
                 "and was it madness or rational speculation?"),
        background=("South Sea Company shares soared then collapsed, "
                    "ruining investors including Newton. Traditional "
                    "accounts blame mass irrationality; revisionists argue "
                    "investors acted rationally on available information, "
                    "and that the bubble's mechanics (debt conversion, "
                    "credit expansion) explain the pattern. The "
                    "rationality of bubbles remains economics' open "
                    "wound."),
        why_it_matters=("Bubbles recur - 1929, 2000, 2008, crypto. The South "
                        "Sea is the original case; its nature determines "
                        "what we learn."),
        sig_lens=("The Signature lens treats the bubble as an information "
                  "ledger: the Signature approach asks what investors "
                  "knew and when."),
        sig_body=("The Signature proposal models the bubble as rational "
                  "speculation on debt conversion. Assumptions: (1) the "
                  "Company offered to convert government debt to equity; "
                  "(2) conversion terms improved with the share price; "
                  "(3) investors understood the mechanics. Reasoning "
                  "path: the proposal shows rising prices were rational "
                  "given the conversion scheme - a self-fulfilling "
                  "mechanism, not madness - predicting the crash when "
                  "parliamentary support wavered. Newton's loss then "
                  "reflects timing, not folly. Limits: the model needs "
                  "better investor-level data; some trading looks "
                  "genuinely manic."),
        pointer=('The Signature system models the bubble as rational speculation on a self-fulfilling debt-conversion scheme. The Signature test: trading patterns match conversion-mechanic incentives. It would be refuted if investors show no awareness of the mechanics.'),
        key_points=[
            "Shares soared and collapsed in 1720; Newton lost heavily.",
            "The Company was converting government debt to equity.",
            "Irrational-mania versus rational-speculation accounts compete.",
            "Bubbles recur, making the original case crucial.",
        ],
        requirements=[
            "An account of the debt-conversion mechanics.",
            "Investor-level evidence on information and motives.",
            "A test distinguishing mania from rational speculation.",
        ],
        standards=[
            "Claims checked against the financial-history literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Dale R. The First Crash. Princeton University Press; 2004.",
            "Temin P, Voth HJ. Riding the South Sea Bubble. 2004.",
        ],
        hypotheses=[
            "Rational speculation on conversion mechanics.",
            "Mass irrational mania.",
            "Credit expansion drove the pattern.",
            "Political corruption was the core.",
        ],
        confirm="Trading patterns match conversion-mechanic incentives.",
        refute="Investors show no awareness of the mechanics.",
    ),
    dict(
        key="history-16",
        name="The Fall of Constantinople: Could It Have Held",
        group="Medieval",
        ladder_rank=16,
        ladder_tier="compounded",
        problem=("Was Constantinople's fall in 1453 inevitable - or could "
                 "different decisions have saved the Byzantine remnant?"),
        background=("By 1453 the empire was a city-state facing Mehmed II's "
                    "vast army and great bombards. The defense was heroic "
                    "but hopeless by most accounts - yet counterfactuals "
                    "persist: Western aid that never came, the missed "
                    "opportunity to destroy the Ottoman fleet, the "
                    "legendary unlocked gate (Kerkaporta). The siege's "
                    "contingencies keep the question alive."),
        why_it_matters=("1453 ended a thousand years of Roman continuity. "
                        "Its inevitability - or not - shapes how we think "
                        "about imperial decline."),
        sig_lens=("The Signature lens treats the siege as a resources ledger: "
                  "the Signature approach asks what the defense lacked "
                  "that no heroism could supply."),
        sig_body=("The Signature proposal models the fall as structural "
                  "with contingent timing. Assumptions: (1) the empire's "
                  "resource base had shrunk for two centuries; (2) "
                  "Ottoman artillery negated the Theodosian Walls; (3) "
                  "Western aid was politically impossible. Reasoning path: "
                  "the proposal shows no plausible 1453 decision changes "
                  "the outcome - the walls' obsolescence was decisive - "
                  "but that earlier decisions (14th-century recovery, "
                  "union of churches) might have. The contingency is "
                  "then in the centuries, not the siege. Limits: "
                  "counterfactuals are untestable; the model concedes "
                  "the siege's heroism while denying its hope."),
        pointer=('The Signature system models the fall as structurally determined by 1453, with contingency located in earlier centuries. The Signature test: no plausible 1453 decision changes the outcome in models. It would be refuted if evidence shows the walls could have held with better leadership.'),
        key_points=[
            "The city fell to Mehmed II in 1453 after a heroic defense.",
            "Ottoman bombards negated the great walls.",
            "Western aid never materialized.",
            "Counterfactuals focus on earlier centuries, not the siege.",
        ],
        requirements=[
            "A structural account of the empire's shrinkage.",
            "An assessment of the siege's true contingencies.",
            "Separation of legend (Kerkaporta) from evidence.",
        ],
        standards=[
            "Claims checked against the Byzantine literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Runciman S. The Fall of Constantinople 1453. Cambridge University Press; 1965.",
            "Crowley R. 1453. Hyperion; 2005.",
        ],
        hypotheses=[
            "Structural decline made 1453 inevitable.",
            "Western aid could have saved the city.",
            "Earlier 14th-century decisions were the true turning points.",
            "The defense nearly succeeded; contingency ruled.",
        ],
        confirm="No plausible 1453 decision changes the outcome in models.",
        refute="Evidence shows the walls could have held with better leadership.",
    ),
    dict(
        key="history-17",
        name="The English Civil War: Was It Inevitable",
        group="Early Modern",
        ladder_rank=17,
        ladder_tier="compounded",
        problem=("Was the English Civil War inevitable - the product of "
                 "deep structures - or did blundering individuals cause "
                 "it?"),
        background=("Revisionists blamed Charles I's personality and "
                    "short-term crises; post-revisionists restored "
                    "structural causes (religion, fiscal-military state, "
                    "multiple kingdoms). The war killed a higher "
                    "proportion of Englishmen than WWI. Whether deep "
                    "causes or contingent blunders drove it remains the "
                    "central dispute in early-modern historiography."),
        why_it_matters=("The war created modern Britain - parliament, "
                        "toleration debates, the fiscal state. Its causes "
                        "are the causes of British modernity."),
        sig_lens=("The Signature lens treats the war as a multiple-kingdom "
                  "ledger: the Signature approach asks what ruling three "
                  "kingdoms did to one king."),
        sig_body=("The Signature proposal models the war as a "
                  "multiple-kingdom trap. Assumptions: (1) Charles ruled "
                  "England, Scotland, and Ireland with different "
                  "religions and institutions; (2) fiscal-military "
                  "pressure demanded uniformity; (3) uniformity "
                  "provoked rebellion. Reasoning path: the proposal "
                  "shows the Scottish prayer-book revolt - not English "
                  "politics - forced Charles to call parliament, "
                  "predicting the war's trigger was imperial "
                  "overstretch, not English inevitability. Structures "
                  "set the trap; contingencies sprang it. Limits: the "
                  "model needs better fiscal data; English religious "
                  "divisions had independent force."),
        pointer=('The Signature system models the war as a multiple-kingdom trap sprung by the Scottish revolt rather than English inevitability. The Signature test: war timing tracks the Scottish crisis, not English politics. It would be refuted if england moves to war without the Scottish trigger.'),
        key_points=[
            "Revisionists blamed Charles; post-revisionists restored structures.",
            "The war killed a higher proportion than WWI.",
            "The Scottish prayer-book revolt forced the Long Parliament.",
            "Religion, finance, and multiple kingdoms all have defenders.",
        ],
        requirements=[
            "An account of the Scottish trigger.",
            "Separation of structural from contingent causes.",
            "Fiscal-military data grounding.",
        ],
        standards=[
            "Claims checked against the Civil War historiography.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Russell C. The Causes of the English Civil War. Oxford University Press; 1990.",
            "Morrill J. The Nature of the English Revolution. Longman; 1993.",
        ],
        hypotheses=[
            "Multiple-kingdom overstretch was the decisive trap.",
            "Charles's personality caused the war.",
            "Religious divisions made war inevitable.",
            "Fiscal-military pressures were primary.",
        ],
        confirm="War timing tracks the Scottish crisis, not English politics.",
        refute="England moves to war without the Scottish trigger.",
    ),
    dict(
        key="history-18",
        name="The French Revolution: Why the Terror",
        group="Modern",
        ladder_rank=18,
        ladder_tier="compounded",
        problem=("Why did the French Revolution - begun in liberty - produce "
                 "the Terror's 17,000 guillotined?"),
        background=("Marxists blamed class struggle and circumstance; "
                    "revisionists (Furet) blamed ideology - the "
                    "revolutionary discourse itself. The war emergency, "
                    "the Vendee revolt, and factional dynamics all "
                    "contributed. Whether the Terror was inherent in "
                    "1789's principles or a contingent derailment remains "
                    "the Revolution's central moral and historical "
                    "question."),
        why_it_matters=("The Terror is the original sin of modern "
                        "revolution. Its cause determines whether "
                        "revolutions can avoid it."),
        sig_lens=("The Signature lens treats the Terror as an escalation "
                  "ledger: the Signature approach asks what made each "
                  "step seem necessary to its takers."),
        sig_body=("The Signature proposal models the Terror as "
                  "emergency-logic escalation. Assumptions: (1) the "
                  "revolution faced foreign invasion and internal "
                  "revolt; (2) each faction defined patriotism as "
                  "supporting its measures; (3) opposition became "
                  "treason by definition. Reasoning path: the proposal "
                  "shows the Terror emerged from the war emergency "
                  "interacting with an ideology that made dissent "
                  "treason - predicting terror should track military "
                  "crisis intensity, which it does. Neither pure "
                  "ideology nor pure circumstance suffices. Limits: "
                  "the model needs better factional data; the "
                  "ideology's independent role is debated."),
        pointer=('The Signature system models the Terror as war emergency interacting with an ideology that defined dissent as treason. The Signature test: terror intensity tracks military crisis measures. It would be refuted if the Terror peaks during military security.'),
        key_points=[
            "About 17,000 guillotined during the Terror.",
            "Marxist (circumstance) versus revisionist (ideology) accounts compete.",
            "War emergency and the Vendee intensified the dynamic.",
            "Whether the Terror was inherent or contingent is the core question.",
        ],
        requirements=[
            "An account linking ideology to emergency.",
            "Terror intensity tracked against military crisis.",
            "Factional dynamics analysis.",
        ],
        standards=[
            "Claims checked against the Revolution historiography.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Furet F. Interpreting the French Revolution. Cambridge University Press; 1981.",
            "Schama S. Citizens. Knopf; 1989.",
        ],
        hypotheses=[
            "Emergency plus ideology produced the Terror.",
            "Revolutionary ideology was inherently terroristic.",
            "Circumstances alone explain it.",
            "Factional competition drove the escalation.",
        ],
        confirm="Terror intensity tracks military crisis measures.",
        refute="The Terror peaks during military security.",
    ),
    dict(
        key="history-19",
        name="The Haitian Revolution: Why It Succeeded Alone",
        group="Modern",
        ladder_rank=19,
        ladder_tier="compounded",
        problem=("Why did Haiti's slave revolution succeed - the only "
                 "successful slave revolt in history - when all others "
                 "failed?"),
        background=("From 1791 to 1804, enslaved Haitians defeated French, "
                    "Spanish, and British armies, founding the second "
                    "independent American republic. Explanations: brilliant "
                    "leadership (Toussaint, Dessalines), disease killing "
                    "Europeans, French revolutionary chaos, and the "
                    "plantation system's brittleness. The revolution was "
                    "then punished with isolation and the 1825 indemnity."),
        why_it_matters=("Haiti proved enslaved people could defeat empires. "
                        "Its success - and subsequent punishment - shaped "
                        "the Atlantic world."),
        sig_lens=("The Signature lens treats the revolution as an "
                  "asymmetry ledger: the Signature approach asks what "
                  "the enslaved had that empires could not match."),
        sig_body=("The Signature proposal models Haitian success as "
                  "disease-plus-division asymmetry. Assumptions: (1) "
                  "European troops died of yellow fever at catastrophic "
                  "rates; (2) French politics divided the colonial "
                  "elite; (3) the enslaved majority had numbers and "
                  "motivation. Reasoning path: the proposal shows no "
                  "single factor suffices - leadership without disease "
                  "fails, disease without leadership dissipates - but "
                  "their combination was unbeatable, predicting that "
                  "similar revolts failed where Europeans survived "
                  "disease or stayed united. Limits: the model needs "
                  "better mortality data; leadership's independent "
                  "contribution is hard to isolate."),
        pointer=('The Signature system models Haitian success as the unbeatable combination of disease, division, numbers, and leadership. The Signature test: european mortality correlates with revolutionary success. It would be refuted if a similar revolt succeeds without the disease factor.'),
        key_points=[
            "The only successful slave revolution in history, 1791-1804.",
            "Defeated French, Spanish, and British forces.",
            "Disease devastated European troops.",
            "The 1825 indemnity punished the victors.",
        ],
        requirements=[
            "An account of the unique combination.",
            "Disease-mortality data for European forces.",
            "Comparison with failed slave revolts.",
        ],
        standards=[
            "Claims checked against the Haitian Revolution literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "James CLR. The Black Jacobins. Vintage; 1963.",
            "Dubois L. Avengers of the New World. Harvard University Press; 2004.",
        ],
        hypotheses=[
            "Disease plus division plus leadership was unbeatable.",
            "Leadership alone explains the success.",
            "French revolutionary chaos was decisive.",
            "The plantation system's brittleness was key.",
        ],
        confirm="European mortality correlates with revolutionary success.",
        refute="A similar revolt succeeds without the disease factor.",
    ),
    dict(
        key="history-20",
        name="The Taiping Rebellion: The Deadliest Civil War",
        group="Modern",
        ladder_rank=20,
        ladder_tier="compounded",
        problem=("Why did the Taiping Rebellion (1850-1864) kill 20-30 "
                 "million people - history's deadliest civil war - and "
                 "why is it so little known in the West?"),
        background=("Hong Xiuquan, believing himself Jesus's brother, led "
                    "a Christian-inflected revolt that seized Nanjing and "
                    "nearly toppled the Qing. The death toll exceeds WWI. "
                    "Explanations for the scale: total-war ideology, "
                    "famine, plague, and Qing scorched earth. Western "
                    "neglect reflects the rebellion's awkward fit with "
                    "both missionary and imperial narratives."),
        why_it_matters=("The Taiping dwarfs most wars in death toll yet "
                        "barely registers in Western memory - a measure of "
                        "how history is written."),
        sig_lens=("The Signature lens treats the death toll as a "
                  "breakdown ledger: the Signature approach asks what "
                  "collapsed besides armies."),
        sig_body=("The Signature proposal models the toll as state-"
                  "breakdown mortality. Assumptions: (1) most deaths came "
                  "from famine and disease, not battle; (2) the war "
                  "destroyed the agricultural and administrative systems; "
                  "(3) both sides practiced scorched earth. Reasoning "
                  "path: the proposal shows the toll follows from the "
                  "war's duration and geography - fourteen years across "
                  "China's rice bowl - predicting mortality should track "
                  "administrative collapse zones, which it does. The "
                  "ideology explains the war's ferocity; the breakdown "
                  "explains its toll. Limits: the death toll is "
                  "estimated, not counted; the sources are thin."),
        pointer=("The Signature system models the toll as state-breakdown mortality across China's rice bowl, not battlefield deaths. The Signature test: mortality tracks administrative-collapse zones. It would be refuted if battle deaths dominate the toll."),
        key_points=[
            "20-30 million dead, 1850-1864 - history's deadliest civil war.",
            "Led by Hong Xiuquan's Christian-inflected movement.",
            "Most deaths from famine and disease, not battle.",
            "Barely known in the West.",
        ],
        requirements=[
            "An account of the mortality's composition.",
            "Separation of ideology from breakdown effects.",
            "Better demographic estimates.",
        ],
        standards=[
            "Claims checked against the Taiping literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Spence JD. God's Chinese Son. Norton; 1996.",
            "Platt SR. Autumn in the Heavenly Kingdom. Knopf; 2012.",
        ],
        hypotheses=[
            "State-breakdown mortality explains the scale.",
            "Ideological total war was the driver.",
            "Qing scorched earth caused most deaths.",
            "The toll is substantially overestimated.",
        ],
        confirm="Mortality tracks administrative-collapse zones.",
        refute="Battle deaths dominate the toll.",
    ),
    dict(
        key="history-21",
        name="The Scramble for Africa: The Timing",
        group="Modern",
        ladder_rank=21,
        ladder_tier="compounded",
        problem=("Why did Europe partition Africa so suddenly in the 1880s - "
                 "after centuries of coastal presence?"),
        background=("The Berlin Conference (1884-85) formalized a "
                    "partition completed within decades. Explanations: "
                    "economic (need for markets and raw materials), "
                    "strategic (rivalry), technological (quinine, "
                    "machine guns, steamboats), and domestic politics. "
                    "The suddenness remains puzzling: the capabilities "
                    "existed earlier, and the economic payoffs were "
                    "often negative."),
        why_it_matters=("The Scramble drew Africa's modern borders - and "
                        "much of its modern conflict. Its timing reveals "
                        "how imperialism actually worked."),
        sig_lens=("The Signature lens treats the Scramble as a "
                  "competition ledger: the Signature approach asks what "
                  "made not colonizing costlier than colonizing."),
        sig_body=("The Signature proposal models the Scramble as a "
                  "competitive cascade. Assumptions: (1) no power wanted "
                  "to pay for colonies; (2) each feared rivals gaining "
                  "advantage; (3) the Berlin rules rewarded effective "
                  "occupation. Reasoning path: the proposal shows the "
                  "partition was a defensive cascade - each claim "
                  "forcing counter-claims - predicting the speed and the "
                  "economic irrationality. Technology (quinine, guns) "
                  "enabled it; rivalry drove it. Limits: the model "
                  "needs better decision-level evidence; economic "
                  "motives had genuine (if overstated) weight."),
        pointer=('The Signature system models the Scramble as a defensive cascade driven by rivalry rather than economic rationality. The Signature test: claims follow rival claims in cascade pattern. It would be refuted if powers colonize without rival pressure.'),
        key_points=[
            "Africa partitioned within decades after 1880.",
            "The Berlin Conference formalized the rules.",
            "Economic payoffs were often negative.",
            "Technology enabled; the suddenness needs explaining.",
        ],
        requirements=[
            "An account of the cascade timing.",
            "Separation of economic from strategic motives.",
            "Decision-level evidence from the powers.",
        ],
        standards=[
            "Claims checked against the imperialism literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Pakenham T. The Scramble for Africa. Random House; 1991.",
            "Robinson R, Gallagher J. Africa and the Victorians. 1961.",
        ],
        hypotheses=[
            "Defensive competitive cascade explains the timing.",
            "Economic needs drove the partition.",
            "Technology made it possible and therefore happened.",
            "Domestic politics in Europe was decisive.",
        ],
        confirm="Claims follow rival claims in cascade pattern.",
        refute="Powers colonize without rival pressure.",
    ),
    dict(
        key="history-22",
        name="The July Crisis: Who Decided for War",
        group="Modern",
        ladder_rank=22,
        ladder_tier="compounded",
        problem=("Who decided for war in July 1914 - and was the First World "
                 "War an accident, a German plan, or a system failure?"),
        background=("Fischer blamed German war aims; revisionists blamed "
                    "the alliance system, misperception, and sleepwalking "
                    "leaders (Clark). The debate has run for a century: "
                    "each power's documents support a different verdict. "
                    "The question matters because it assigns the 20th "
                    "century's original sin."),
        why_it_matters=("WWI's causes are the most debated in historiography. "
                        "The verdict shapes how we think about war "
                        "prevention."),
        sig_lens=("The Signature lens treats July 1914 as a decision ledger: "
                  "the Signature approach asks what each capital knew and "
                  "chose, day by day."),
        sig_body=("The Signature proposal models the crisis as "
                  "risk-acceptant brinkmanship, not accident. Assumptions: "
                  "(1) leaders understood the escalation risks; (2) each "
                  "accepted risks for perceived gains; (3) no one wanted "
                  "the war they got. Reasoning path: the proposal shows "
                  "the documents reveal calculated risk-taking - "
                  "Germany's blank check, Russia's mobilization, France's "
                  "support - predicting that 'sleepwalking' understates "
                  "agency while 'German plan' overstates control. The war "
                  "was chosen by inches. Limits: the model needs "
                  "counterfactual discipline; the documents are "
                  "self-serving."),
        pointer=('The Signature system models July 1914 as calculated risk-taking by all parties - war chosen by inches, not sleepwalked into. The Signature test: documents show risk-acceptance at each decision node. It would be refuted if a power is shown to have sought the continental war deliberately.'),
        key_points=[
            "Fischer blamed German war aims; Clark blamed sleepwalking.",
            "Each power's documents support different verdicts.",
            "The debate has run for a century.",
            "The verdict assigns the 20th century's original sin.",
        ],
        requirements=[
            "Day-by-day decision analysis.",
            "Separation of risk-taking from accident.",
            "Source-critical handling of self-serving documents.",
        ],
        standards=[
            "Claims checked against the WWI-origins literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Fischer F. Germany's Aims in the First World War. 1967.",
            "Clark C. The Sleepwalkers. Harper; 2012.",
        ],
        hypotheses=[
            "Calculated brinkmanship by all parties caused the war.",
            "German war aims were decisive.",
            "The alliance system made war automatic.",
            "Misperception and accident dominated.",
        ],
        confirm="Documents show risk-acceptance at each decision node.",
        refute="A power is shown to have sought the continental war deliberately.",
    ),
    dict(
        key="history-23",
        name="The Origins of WWI: The Fischer Debate",
        group="Modern",
        ladder_rank=23,
        ladder_tier="compounded",
        problem=("Did Germany deliberately seek the First World War - the "
                 "Fischer thesis - or has the debate moved past blame?"),
        background=("Fritz Fischer's 1961 bombshell used German archives to "
                    "argue for deliberate German war aims (the September "
                    "Program). It shattered the Versailles-blame consensus "
                    "and then the no-blame consensus. Subsequent research "
                    "complicated the picture: German agency is real, but so "
                    "is everyone else's. The thesis survives in modified "
                    "form - which is why the debate never ends."),
        why_it_matters=("The Fischer debate is historiography's longest war. "
                        "Its current state shows how historical blame "
                        "evolves."),
        sig_lens=("The Signature lens treats the debate as an evidence "
                  "ledger: the Signature approach asks what Fischer proved "
                  "versus what he inferred."),
        sig_body=("The Signature proposal models the Fischer thesis as "
                  "half-vindicated. Assumptions: (1) the September Program "
                  "documents real war aims; (2) aims do not equal "
                  "premeditation; (3) other powers had aims too. Reasoning "
                  "path: the proposal shows Fischer proved German "
                  "expansionist intent but not a long-planned war - "
                  "predicting the modified consensus: Germany bears "
                  "primary but not sole responsibility, and the war "
                  "resulted from aims meeting opportunity. The debate "
                  "then becomes about weights, not guilt. Limits: the "
                  "model cannot settle moral weights; the archives are "
                  "incomplete."),
        pointer=('The Signature system treats Fischer as half-vindicated: German expansionist intent proven, long-planned war not proven. The Signature test: german planning documents show pre-1914 war intent. It would be refuted if comparable war aims emerge for all powers equally.'),
        key_points=[
            "Fischer used German archives to argue deliberate war aims.",
            "The September Program documents expansionist intent.",
            "Aims do not equal premeditation of the 1914 war.",
            "The modified consensus assigns primary but not sole responsibility.",
        ],
        requirements=[
            "Separation of aims from premeditation.",
            "Comparative war-aims analysis across powers.",
            "An account of the debate's evolution.",
        ],
        standards=[
            "Claims checked against the Fischer-controversy literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Fischer F. Germany's Aims in the First World War. 1967.",
            "Mombauer A. The Origins of the First World War. 2002.",
        ],
        hypotheses=[
            "Modified Fischer: primary German responsibility, not sole.",
            "Full Fischer: Germany deliberately sought the war.",
            "The thesis is refuted; responsibility is shared.",
            "The blame question is unanswerable.",
        ],
        confirm="German planning documents show pre-1914 war intent.",
        refute="Comparable war aims emerge for all powers equally.",
    ),
    dict(
        key="history-24",
        name="The Fall of the Qing: Why 1911",
        group="Modern",
        ladder_rank=24,
        ladder_tier="advanced",
        problem=("Why did the Qing dynasty - ruling China for 268 years - "
                 "collapse so suddenly in 1911?"),
        background=("The Qing survived the Taiping, reformed after 1900, "
                    "and seemed to be modernizing - then disintegrated in "
                    "months after the Wuchang uprising. Explanations: the "
                    "New Policies alienated elites, the railway crisis "
                    "triggered the provinces, the army's loyalty fractured, "
                    "or the dynasty was hollow long before. The speed of "
                    "the collapse remains startling."),
        why_it_matters=("1911 ended two millennia of imperial China. Its "
                        "mechanics illuminate how ancient regimes end."),
        sig_lens=("The Signature lens treats 1911 as a loyalty ledger: the "
                  "Signature approach asks when the army and provinces "
                  "stopped obeying."),
        sig_body=("The Signature proposal models the collapse as a "
                  "loyalty cascade. Assumptions: (1) the dynasty ruled "
                  "through provincial elites and the New Army; (2) the "
                  "New Policies threatened elite interests; (3) the "
                  "railway nationalization triggered provincial revolt. "
                  "Reasoning path: the proposal shows the Wuchang mutiny "
                  "succeeded because loyalty had already hollowed - "
                  "predicting the cascade pattern where each province's "
                  "defection lowered the cost of the next. The reforms "
                  "meant to save the dynasty destroyed its coalition. "
                  "Limits: the model needs better provincial-level data; "
                  "ideological (republican) factors need separate "
                  "weighting."),
        pointer=('The Signature system models 1911 as a loyalty cascade, with reforms destroying the coalition they meant to save. The Signature test: defections follow the cascade pattern provincially. It would be refuted if the dynasty retains elite loyalty through 1911.'),
        key_points=[
            "268 years of Qing rule ended in months.",
            "The New Policies alienated the elite coalition.",
            "The railway crisis triggered provincial revolt.",
            "The Wuchang mutiny cascaded into general defection.",
        ],
        requirements=[
            "A cascade model of provincial defection.",
            "An account of the New Policies' coalition effects.",
            "Separation of structural from trigger causes.",
        ],
        standards=[
            "Claims checked against the 1911 literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Rhoads EJM. Manchus and Han. University of Washington Press; 2000.",
            "Esherick JW. Reform and Revolution in China. 1976.",
        ],
        hypotheses=[
            "Loyalty cascade explains the speed.",
            "The dynasty was hollow long before 1911.",
            "Republican ideology was decisive.",
            "The railway crisis alone triggered everything.",
        ],
        confirm="Defections follow the cascade pattern provincially.",
        refute="The dynasty retains elite loyalty through 1911.",
    ),
    dict(
        key="history-25",
        name="The Russian Revolution: Inevitable or Contingent",
        group="Modern",
        ladder_rank=25,
        ladder_tier="advanced",
        problem=("Was the Russian Revolution inevitable - the product of "
                 "backwardness and war - or did contingency put the "
                 "Bolsheviks in power?"),
        background=("Soviet historiography made it inevitable; revisionists "
                    "made it contingent; post-revisionists split the "
                    "difference. The February collapse surprised everyone; "
                    "the October seizure was a gamble that barely "
                    "succeeded. Whether any revolution was coming, and "
                    "whether it had to be Bolshevik, are different "
                    "questions with different answers."),
        why_it_matters=("1917 shaped the 20th century more than any other "
                        "event. Its necessity - or accident - shapes how "
                        "we judge everything after."),
        sig_lens=("The Signature lens treats 1917 as two ledgers: the "
                  "Signature approach separates the collapse (February) "
                  "from the seizure (October)."),
        sig_body=("The Signature proposal models February as structural "
                  "and October as contingent. Assumptions: (1) the war "
                  "destroyed the tsarist state's capacity; (2) no "
                  "government could have survived 1917's pressures "
                  "unchanged; (3) Bolshevik victory required specific "
                  "gambles. Reasoning path: the proposal shows some "
                  "revolution was overdetermined - predicting the "
                  "February collapse from state-capacity measures - while "
                  "Bolshevik victory was not, depending on Lenin's "
                  "return, the Kornilov affair, and the Second Congress "
                  "timing. Inevitable revolution, contingent "
                  "revolutionaries. Limits: the model needs better "
                  "counterfactual discipline; the 'some revolution' "
                  "claim is hard to test."),
        pointer=('The Signature system separates inevitable collapse (February) from contingent seizure (October). The Signature test: state-capacity collapse predicts February timing. It would be refuted if the tsarist state shows resilience through 1917.'),
        key_points=[
            "February surprised everyone; October was a gamble.",
            "Soviet, revisionist, and post-revisionist accounts compete.",
            "Whether revolution - and whether Bolshevik - are separate questions.",
            "The war's role is central to all accounts.",
        ],
        requirements=[
            "Separation of collapse from seizure explanations.",
            "State-capacity measures for 1917.",
            "Counterfactual discipline on the contingencies.",
        ],
        standards=[
            "Claims checked against the 1917 historiography.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Pipes R. The Russian Revolution. Knopf; 1990.",
            "Figes O. A People's Tragedy. Viking; 1996.",
        ],
        hypotheses=[
            "Structural collapse was inevitable; Bolshevik victory was not.",
            "The whole revolution was contingent.",
            "The whole revolution was inevitable.",
            "German support was the decisive contingency.",
        ],
        confirm="State-capacity collapse predicts February timing.",
        refute="The tsarist state shows resilience through 1917.",
    ),
    dict(
        key="history-26",
        name="The Great Depression: The True Cause",
        group="Modern",
        ladder_rank=26,
        ladder_tier="advanced",
        problem=("What really caused the Great Depression - and why was it "
                 "so much worse than other downturns?"),
        background=("Friedman and Schwartz blamed the Fed's monetary "
                    "contraction; Keynesians blamed demand collapse; "
                    "internationalists blame the gold standard; others "
                    "cite the stock crash, bank panics, or structural "
                    "imbalances. The Depression's depth and global spread "
                    "need explaining beyond any single cause - and the "
                    "policy lessons depend on the verdict."),
        why_it_matters=("The Depression discredited laissez-faire, built "
                        "the welfare state, and enabled fascism. Its cause "
                        "is the most consequential economic question in "
                        "history."),
        sig_lens=("The Signature lens treats the Depression as a "
                  "transmission ledger: the Signature approach asks how "
                  "an American downturn became a global catastrophe."),
        sig_body=("The Signature proposal models the Depression as a "
                  "gold-standard transmission mechanism. Assumptions: (1) "
                  "the gold standard linked national money supplies; (2) "
                  "the Fed contracted sharply after 1929; (3) deficit "
                  "countries could not devalue. Reasoning path: the "
                  "proposal shows American monetary contraction "
                  "propagated through the gold standard - predicting "
                  "that recovery should follow abandonment of gold, "
                  "which it did country by country. The stock crash was "
                  "the trigger; the gold standard was the machine. "
                  "Limits: the model needs better transmission "
                  "measures; domestic banking crises had independent "
                  "force."),
        pointer=('The Signature system models the Depression as gold-standard transmission of American monetary contraction, with recovery following gold abandonment. The Signature test: recovery timing tracks gold abandonment exactly. It would be refuted if countries off gold suffer equally.'),
        key_points=[
            "The worst downturn in modern history; global in scope.",
            "Monetary, Keynesian, and gold-standard accounts compete.",
            "Recovery followed gold-standard abandonment country by country.",
            "The policy lessons depend on the causal verdict.",
        ],
        requirements=[
            "A transmission mechanism for global spread.",
            "An account of the recovery timing.",
            "Separation of trigger from propagation.",
        ],
        standards=[
            "Claims checked against the Depression literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Friedman M, Schwartz AJ. A Monetary History of the United States. 1963.",
            "Eichengreen B. Golden Fetters. Oxford University Press; 1992.",
        ],
        hypotheses=[
            "Gold-standard transmission is the core mechanism.",
            "Fed monetary contraction alone explains it.",
            "Demand collapse was primary.",
            "Banking panics were the decisive propagator.",
        ],
        confirm="Recovery timing tracks gold abandonment exactly.",
        refute="Countries off gold suffer equally.",
    ),
    dict(
        key="history-27",
        name="The Appeasement Puzzle",
        group="Modern",
        ladder_rank=27,
        ladder_tier="advanced",
        problem=("Was appeasement folly, necessity, or tragedy - and what "
                 "did Chamberlain actually know?"),
        background=("The orthodox verdict condemns Munich as cowardice; "
                    "revisionists argue Britain was unready for war and "
                    "bought time; post-revisionists see a tragic gamble. "
                    "New documents show Chamberlain understood Hitler "
                    "better than assumed - and rearmed frantically after "
                    "Munich. Whether appeasement was rational given "
                    "constraints remains fiercely debated."),
        why_it_matters=("Munich is the universal analogy for foreign-policy "
                        "failure. Its true nature determines when the "
                        "analogy applies."),
        sig_lens=("The Signature lens treats appeasement as a constraints "
                  "ledger: the Signature approach asks what options "
                  "actually existed in 1938."),
        sig_body=("The Signature proposal models appeasement as "
                  "constrained rationality. Assumptions: (1) Britain's "
                  "military was unready in 1938; (2) the public and "
                  "empire opposed war; (3) Hitler's aims were "
                  "partially understood. Reasoning path: the proposal "
                  "shows Munich bought rearmament time that Britain "
                  "used - predicting that the 'guilty men' verdict "
                  "ignores the rearmament surge after Munich. The "
                  "tragedy is then that the bought time was "
                  "insufficient, not that buying it was foolish. "
                  "Limits: the model risks excusing moral failure; "
                  "the counterfactual of earlier confrontation is "
                  "untestable."),
        pointer=("The Signature system models appeasement as constrained rationality buying rearmament time, tragically insufficient. The Signature test: rearmament gains match the bought time's value. It would be refuted if britain was ready for war in 1938."),
        key_points=[
            "Orthodox verdict: cowardice; revisionist: necessity.",
            "Britain rearmed frantically after Munich.",
            "Chamberlain understood Hitler better than assumed.",
            "The Munich analogy dominates foreign-policy debate.",
        ],
        requirements=[
            "Military-readiness measures for 1938.",
            "An account of the post-Munich rearmament.",
            "Separation of constraints from misjudgment.",
        ],
        standards=[
            "Claims checked against the appeasement literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Taylor AJP. The Origins of the Second World War. 1961.",
            "Parker RAC. Chamberlain and Appeasement. 1993.",
        ],
        hypotheses=[
            "Constrained rationality: buying time was the best option.",
            "Moral and strategic folly.",
            "A tragic gamble with known risks.",
            "Earlier confrontation would have worked.",
        ],
        confirm="Rearmament gains match the bought time's value.",
        refute="Britain was ready for war in 1938.",
    ),
    dict(
        key="history-28",
        name="The Cold War: Who Started It",
        group="Modern",
        ladder_rank=28,
        ladder_tier="advanced",
        problem=("Who started the Cold War - Soviet expansion, American "
                 "provocation, or the structure of bipolarity?"),
        background=("Orthodox historians blamed Stalin; revisionists blamed "
                    "American economic imperialism; post-revisionists "
                    "blame both, or the system. New archives complicated "
                    "every version: Stalin was cautious and brutal, "
                    "Truman improvising and ideological. The question "
                    "persists because the answer legitimates worldviews."),
        why_it_matters=("Cold War origins are the charter myth of the "
                        "American-led order. The verdict shapes how we "
                        "understand great-power rivalry today."),
        sig_lens=("The Signature lens treats 1945-47 as a security-dilemma "
                  "ledger: the Signature approach asks what each side "
                  "feared the other would do."),
        sig_body=("The Signature proposal models the Cold War as a "
                  "security dilemma with ideological amplifiers. "
                  "Assumptions: (1) both sides feared the other's "
                  "intentions; (2) each defensive move looked offensive; "
                  "(3) ideology made compromise suspect. Reasoning path: "
                  "the proposal shows the spiral - Soviet buffers, "
                  "American atomic diplomacy, each confirming the other's "
                  "fears - predicting that neither 'side' started it; "
                  "the structure plus mutual misperception did. "
                  "Responsibility is then distributed, not absent. "
                  "Limits: the model needs better intention measures; "
                  "Stalin's brutality was not merely defensive."),
        pointer=("The Signature system models Cold War origins as a security dilemma with ideological amplifiers, distributing responsibility. The Signature test: each escalation follows the other's defensive move. It would be refuted if one side plans confrontation from the war's end."),
        key_points=[
            "Orthodox, revisionist, and post-revisionist accounts compete.",
            "New archives complicated every version.",
            "The security dilemma fits the spiral pattern.",
            "The answer legitimates contemporary worldviews.",
        ],
        requirements=[
            "Intention evidence from both archives.",
            "A spiral model of the 1945-47 decisions.",
            "Separation of structure from agency.",
        ],
        standards=[
            "Claims checked against the Cold War origins literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Gaddis JL. The Cold War: A New History. Penguin; 2005.",
            "Leffler MP. A Preponderance of Power. Stanford University Press; 1992.",
        ],
        hypotheses=[
            "Security dilemma with ideological amplifiers.",
            "Soviet expansionism was primary.",
            "American provocation was primary.",
            "Bipolar structure made conflict inevitable.",
        ],
        confirm="Each escalation follows the other's defensive move.",
        refute="One side plans confrontation from the war's end.",
    ),
    dict(
        key="history-29",
        name="The Cuban Missile Crisis: How Close",
        group="Modern",
        ladder_rank=29,
        ladder_tier="advanced",
        problem=("How close did the Cuban Missile Crisis come to nuclear war "
                 "- and what actually resolved it?"),
        background=("For decades the story was Kennedy's masterful "
                    "brinkmanship; later revelations showed how close "
                    "accidents came (Soviet submarine B-59, unauthorized "
                    "actions) and how much the secret Jupiter trade "
                    "mattered. The crisis is now understood as far more "
                    "dangerous - and its resolution more mutual - than "
                    "the heroic version."),
        why_it_matters=("The crisis is humanity's closest brush with "
                        "nuclear war. Its true danger level calibrates "
                        "nuclear risk today."),
        sig_lens=("The Signature lens treats the crisis as an accident "
                  "ledger: the Signature approach asks how many "
                  "fail-safes failed."),
        sig_body=("The Signature proposal models the crisis as a "
                  "control-failure cascade narrowly contained. "
                  "Assumptions: (1) both leaders sought to avoid war; "
                  "(2) military systems had autonomous risks; (3) "
                  "communication was slow and noisy. Reasoning path: the "
                  "proposal shows the danger came less from decisions "
                  "than from systems - the submarine, the U-2 shootdown, "
                  "the false alarms - predicting that crisis danger "
                  "scales with system autonomy, not leader recklessness. "
                  "The resolution was then mutual concession under "
                  "shared terror. Limits: the model needs better "
                  "Soviet decision records; the counterfactual of "
                  "non-resolution is untestable."),
        pointer=('The Signature system models the crisis as a control-failure cascade, with danger scaling from system autonomy rather than leader recklessness. The Signature test: danger incidents trace to autonomous systems. It would be refuted if all danger traces to deliberate leader decisions.'),
        key_points=[
            "Later revelations showed far greater danger than first told.",
            "Accidents (B-59, U-2) nearly triggered war.",
            "The secret Jupiter missile trade was crucial.",
            "Resolution was more mutual than the heroic version.",
        ],
        requirements=[
            "An inventory of the autonomous risks.",
            "An account of the secret diplomacy.",
            "A danger calibration for nuclear risk today.",
        ],
        standards=[
            "Claims checked against the crisis literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Allison G, Zelikow P. Essence of Decision. Longman; 1999.",
            "Dobbs M. One Minute to Midnight. Knopf; 2008.",
        ],
        hypotheses=[
            "System autonomy, not decisions, created the danger.",
            "Kennedy's brinkmanship was decisive and masterful.",
            "Khrushchev's recklessness caused the crisis.",
            "The crisis was never truly dangerous.",
        ],
        confirm="Danger incidents trace to autonomous systems.",
        refute="All danger traces to deliberate leader decisions.",
    ),
    dict(
        key="history-30",
        name="The Fall of the USSR: Why So Sudden",
        group="Modern",
        ladder_rank=30,
        ladder_tier="advanced",
        problem=("Why did the Soviet Union collapse so suddenly in 1991 - "
                 "surprising the CIA, the Kremlin, and nearly everyone?"),
        background=("Explanations: economic stagnation, Gorbachev's reforms "
                    "unleashing forces he could not control, nationalism, "
                    "the arms race, ideological exhaustion, or contingency "
                    "(the 1991 coup's failure). The suddenness is the "
                    "puzzle: long-term decline was visible, but the "
                    "implosion's speed was not predicted by any theory."),
        why_it_matters=("The Soviet collapse ended the 20th century's "
                        "defining conflict. Its mechanics are the template "
                        "for understanding authoritarian fragility."),
        sig_lens=("The Signature lens treats 1991 as a legitimacy ledger: "
                  "the Signature approach asks when the elite stopped "
                  "believing."),
        sig_body=("The Signature proposal models the collapse as a "
                  "legitimacy cascade. Assumptions: (1) the system ran on "
                  "elite belief as much as coercion; (2) Gorbachev's "
                  "glasnost allowed belief to be questioned publicly; (3) "
                  "the failed 1991 coup destroyed the coercion option. "
                  "Reasoning path: the proposal shows the union dissolved "
                  "when elites stopped believing AND coercion failed - "
                  "predicting the cascade pattern where each republic's "
                  "exit lowered the cost of the next. Economic decline "
                  "set the stage; the belief collapse pulled the trigger. "
                  "Limits: the model needs better elite-belief measures; "
                  "nationalism's independent role is debated."),
        pointer=('The Signature system models 1991 as a legitimacy cascade: elites stopped believing just as coercion failed. The Signature test: republic exits follow the cascade pattern. It would be refuted if the union dissolves with elites still believing.'),
        key_points=[
            "The collapse surprised nearly all observers.",
            "Economic decline was visible; the speed was not.",
            "Gorbachev's reforms unleashed uncontrollable forces.",
            "The failed 1991 coup was the proximate trigger.",
        ],
        requirements=[
            "An account of the speed of collapse.",
            "Elite-belief measures over time.",
            "Separation of economic from political causes.",
        ],
        standards=[
            "Claims checked against the Soviet-collapse literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Kotkin S. Armageddon Averted. Oxford University Press; 2001.",
            "Beissinger MR. Nationalist Mobilization and the Collapse of the Soviet State. 2002.",
        ],
        hypotheses=[
            "Legitimacy cascade explains the suddenness.",
            "Economic collapse was sufficient.",
            "Nationalism dissolved the union.",
            "Gorbachev's personality was decisive.",
        ],
        confirm="Republic exits follow the cascade pattern.",
        refute="The union dissolves with elites still believing.",
    ),
    dict(
        key="history-31",
        name="The Rwandan Genocide: Could It Have Been Stopped",
        group="Modern",
        ladder_rank=31,
        ladder_tier="advanced",
        problem=("Could the 1994 Rwandan genocide - 800,000 dead in 100 days "
                 "- have been prevented or stopped?"),
        background=("The genocide was meticulously organized, not spontaneous: "
                    "militias, radio incitement, administrative lists. "
                    "The UN force was undermanned and under-mandated; "
                    "major powers avoided the word 'genocide.' Scholars "
                    "debate whether a larger force, earlier action, or "
                    "jamming the radio could have worked - or whether the "
                    "planning made intervention futile."),
        why_it_matters=("Rwanda is the test of 'never again.' The answer "
                        "determines what the international community owes "
                        "the next crisis."),
        sig_lens=("The Signature lens treats the genocide as an organization "
                  "ledger: the Signature approach asks what the killing "
                  "machine needed to function."),
        sig_body=("The Signature proposal models the genocide as an "
                  "organization dependent on specific inputs. Assumptions: "
                  "(1) the killing needed coordination (radio, "
                  "administrators, militias); (2) coordination nodes were "
                  "vulnerable; (3) the RPF's advance created the endgame. "
                  "Reasoning path: the proposal shows disrupting "
                  "coordination - jamming radio, protecting nodes, a "
                  "credible force - could have slowed the killing, "
                  "predicting that the genocide's speed depended on "
                  "uncontested organization. Prevention was then "
                  "possible in the organization phase, harder once "
                  "killing began. Limits: the model cannot rerun "
                  "history; political will was the binding constraint."),
        pointer=('The Signature system models the genocide as coordination-dependent, with prevention possible in the organization phase. The Signature test: killing speed tracks coordination integrity. It would be refuted if the killing proceeds identically with coordination disrupted.'),
        key_points=[
            "800,000 dead in about 100 days; meticulously organized.",
            "The UN force was undermanned and under-mandated.",
            "Major powers avoided the word genocide.",
            "Radio and administrative coordination were crucial.",
        ],
        requirements=[
            "An account of the killing's organizational needs.",
            "Assessment of proposed interventions.",
            "Separation of capability from will.",
        ],
        standards=[
            "Claims checked against the Rwanda literature; sensitivity observed.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Des Forges A. Leave None to Tell the Story. Human Rights Watch; 1999.",
            "Power S. A Problem from Hell. Basic Books; 2002.",
        ],
        hypotheses=[
            "Disrupting coordination could have slowed the killing.",
            "Nothing could have stopped it once begun.",
            "Early action in the organization phase could have prevented it.",
            "Only the RPF's victory could end it.",
        ],
        confirm="Killing speed tracks coordination integrity.",
        refute="The killing proceeds identically with coordination disrupted.",
    ),
    dict(
        key="history-32",
        name="The 2008 Crisis: The Root Cause",
        group="Modern",
        ladder_rank=32,
        ladder_tier="advanced",
        problem=("What really caused the 2008 financial crisis - and why did "
                 "almost no one see it coming?"),
        background=("Candidates: subprime mortgages, securitization, rating-"
                    "agency failure, leverage, global imbalances, Fed "
                    "policy, deregulation, or mathematical risk models. "
                    "Each has evidence; the weights are disputed, and the "
                    "failure of prediction itself needs explaining "
                    "(incentives, models, ideology). The crisis reshaped "
                    "economics and politics - but its root cause remains "
                    "contested."),
        why_it_matters=("2008 discredited economic orthodoxy and fueled "
                        "populism. Its cause determines financial "
                        "regulation's future."),
        sig_lens=("The Signature lens treats 2008 as an incentives ledger: "
                  "the Signature approach asks who profited from not "
                  "seeing the risk."),
        sig_body=("The Signature proposal models the crisis as an "
                  "incentive-structure failure. Assumptions: (1) "
                  "originators, packagers, and raters were paid by "
                  "volume, not quality; (2) leverage amplified small "
                  "losses; (3) models assumed housing prices could not "
                  "fall nationally. Reasoning path: the proposal shows "
                  "no single villain suffices - but the incentive "
                  "structure made the bad equilibrium stable, predicting "
                  "that warnings were ignored because acting on them "
                  "cost money. The crisis was then an emergent property "
                  "of misaligned incentives, not a mistake. Limits: the "
                  "model needs better incentive measures; global "
                  "imbalances had independent force."),
        pointer=('The Signature system models 2008 as misaligned incentives making the bad equilibrium stable, with warnings ignored because they cost money. The Signature test: risk-taking tracks incentive misalignment measures. It would be refuted if well-incentivized actors took identical risks.'),
        key_points=[
            "The worst crisis since the Depression; prediction failed broadly.",
            "Subprime, securitization, leverage, and models all contributed.",
            "Incentives rewarded volume over quality.",
            "The weights of causes are disputed.",
        ],
        requirements=[
            "An account of the prediction failure.",
            "Incentive-structure analysis.",
            "Separation of trigger from system.",
        ],
        standards=[
            "Claims checked against the crisis literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "FCIC. The Financial Crisis Inquiry Report. 2011.",
            "Rajan RG. Fault Lines. Princeton University Press; 2010.",
        ],
        hypotheses=[
            "Misaligned incentives created the bad equilibrium.",
            "Deregulation was the root cause.",
            "Global imbalances drove the crisis.",
            "Mathematical models were the core failure.",
        ],
        confirm="Risk-taking tracks incentive misalignment measures.",
        refute="Well-incentivized actors took identical risks.",
    ),
    dict(
        key="history-33",
        name="The End of History Debate: The Verdict",
        group="Theory",
        ladder_rank=33,
        ladder_tier="advanced",
        problem=("Was Fukuyama's 'end of history' refuted by events - or "
                 "was it misunderstood?"),
        background=("Fukuyama argued liberal democracy was the final form "
                    "of government; critics cite China's rise, democratic "
                    "backsliding, and persistent alternatives. Defenders "
                    "reply he predicted no alternatives would be "
                    "ideologically superior, not that history would stop. "
                    "Thirty-five years on, the thesis is neither "
                    "vindicated nor buried - which is itself the puzzle."),
        why_it_matters=("The thesis was the 1990s' master narrative. Its "
                        "verdict shapes expectations for the 21st "
                        "century."),
        sig_lens=("The Signature lens treats the thesis as a claim ledger: "
                  "the Signature approach asks what exactly was claimed "
                  "versus what was refuted."),
        sig_body=("The Signature proposal models the debate as a "
                  "scope confusion. Assumptions: (1) Fukuyama claimed "
                  "ideological finality, not event finality; (2) "
                  "alternatives must offer superior legitimacy to refute "
                  "it; (3) backsliding is compatible with the thesis. "
                  "Reasoning path: the proposal shows most 'refutations' "
                  "target claims never made - predicting the thesis "
                  "survives where alternatives lack legitimating ideas "
                  "(China's model inspires imitation, not conviction). "
                  "The verdict is then: unrefuted but unhelpful, a "
                  "philosophy in search of events. Limits: the model "
                  "concedes the thesis's predictive weakness; "
                  "legitimacy is hard to measure."),
        pointer=('The Signature system argues most refutations target claims never made, leaving the thesis unrefuted but unhelpful. The Signature test: alternatives lack legitimating-ideology measures. It would be refuted if an alternative model wins genuine ideological allegiance.'),
        key_points=[
            "Fukuyama claimed liberal democracy as the final form.",
            "China's rise and backsliding challenged the thesis.",
            "Defenders distinguish ideological from event finality.",
            "The thesis is neither vindicated nor buried.",
        ],
        requirements=[
            "A precise statement of the original claim.",
            "Legitimacy measures for alternative models.",
            "An account of backsliding's compatibility.",
        ],
        standards=[
            "Claims checked against the end-of-history literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Fukuyama F. The End of History and the Last Man. Free Press; 1992.",
            "Huntington SP. The Clash of Civilizations. Foreign Affairs; 1993.",
        ],
        hypotheses=[
            "The thesis is unrefuted but unhelpful.",
            "Events refuted it decisively.",
            "It will be vindicated in the long run.",
            "The question is malformed.",
        ],
        confirm="Alternatives lack legitimating-ideology measures.",
        refute="An alternative model wins genuine ideological allegiance.",
    ),
    dict(
        key="history-34",
        name='The Synthesis Problem: Can History Unify',
        group="Theory",
        ladder_rank=34,
        ladder_tier="advanced",
        problem=("Can history unify its methods - narrative, quantitative, "
                 "cultural, global - or is fragmentation permanent?"),
        background=("Historians split between storytellers and modelers, "
                    "between archives and data. The cultural turn, the "
                    "quantitative turn, and global history each claimed "
                    "the future; each delivered partially. Whether the "
                    "discipline needs unity - or whether pluralism is its "
                    "strength - remains history's foundational question."),
        why_it_matters=("This is history's capstone: the answer determines "
                        "what the discipline can claim to know."),
        sig_lens=("The Signature lens treats the fragmentation as a "
                  "question ledger: the Signature approach asks which "
                  "questions need which methods."),
        sig_body=("The Signature proposal models unity as "
                  "question-driven pluralism. Assumptions: (1) "
                  "historical questions differ in kind (what happened, "
                  "why, what it meant); (2) methods fit questions, not "
                  "vice versa; (3) the best work already mixes methods. "
                  "Reasoning path: the proposal shows fragmentation is "
                  "productive when question-driven - predicting that "
                  "forced unity would impoverish the field. The "
                  "synthesis is then a shared standard of evidence, not "
                  "a shared method. Limits: the model concedes "
                  "incommensurability at the extremes; evidence "
                  "standards themselves are contested."),
        pointer=('The Signature system proposes question-driven pluralism unified by shared evidence standards rather than one method. The Signature test: mixed-method work outperforms single-method work. It would be refuted if one method proves sufficient for all historical questions.'),
        key_points=[
            "Narrative, quantitative, cultural, and global approaches compete.",
            "Each claimed the future; each delivered partially.",
            "Whether unity is needed or pluralism is strength is open.",
            "Evidence standards are themselves contested.",
        ],
        requirements=[
            "A question-to-method mapping.",
            "Shared evidence standards.",
            "An account of productive versus sterile fragmentation.",
        ],
        standards=[
            "Claims checked against the historiography literature.",
            "Open status confirmed as of 2026.",
        ],
        citations=[
            "Evans RJ. In Defence of History. Granta; 1997.",
            "Guldi J, Armitage D. The History Manifesto. Cambridge University Press; 2014.",
        ],
        hypotheses=[
            "Question-driven pluralism is the stable settlement.",
            "Quantitative methods will unify the field.",
            "Narrative will reassert dominance.",
            "Fragmentation is permanent and fine.",
        ],
        confirm="Mixed-method work outperforms single-method work.",
        refute="One method proves sufficient for all historical questions.",
    ),
]
