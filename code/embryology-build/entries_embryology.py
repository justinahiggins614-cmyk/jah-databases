#!/usr/bin/env python3
"""Authored records for the Embryology field databases (field #36, taxonomy order).

Field #36 Embryology (coverage n=538, domain B1. Basic Medical Sciences).
Verified 2026-10-17: manifest search (2,372 databases) zero 'embryolog*'
slugs/names; no db/embryolog* dirs; whole-system exact-title sweep over the
dedupe gate: zero collisions for all 34 planned titles (x2 editions = 68
variants). Near-neighbors confirmed different disciplines: 'anatomy' (gross
adult anatomy), 'histology' (microscopic tissues), 'cell-biology' (cell
biology as a field), 'pathology' (disease mechanisms). No pregnancy, fetus,
placenta, obstetrics, IVF, fertility, or reproduction databases exist at all.
ZERO full-record discipline coverage anywhere.

Two databases, 34 ladder-ordered records each:

  embryology                - The Embryology Database
                               (public-harvest: real, fact-checked prenatal
                               development; standard references Sadler
                               'Langman's Medical Embryology' 15th ed 2024;
                               Moore/Persaud/Torchia 'The Developing Human'
                               11th ed 2020; Schoenwolf et al. 'Larsen's
                               Human Embryology' 6th ed 2021; Gilbert/Barresi
                               'Developmental Biology' 13th ed 2023;
                               Carlson 'Human Embryology and Developmental
                               Biology' 6th ed 2019; Dudek 'Embryology (BRS)'
                               7th ed 2019; O'Rahilly/Mueller 'Human
                               Embryology & Teratology' 3rd ed 2001)
  embryology-signature      - The Embryology Signature Database
                               (his original Signature interpretation of
                               prenatal development as the timed construction
                               of the human body; src signature, titles
                               suffixed " (Signature Edition)", never
                               presented as authentic public record)

Scope: gametogenesis, fertilization, cleavage, blastulation, implantation,
bilaminar/trilaminar discs, gastrulation, neurulation, body axes,
somitogenesis, folding, placenta and membranes, organogenesis by system,
developmental genetics (Hox), teratology, twinning, the fetal timeline,
assisted reproduction. Distinct from histology (tissues) and anatomy
(gross adult).

Ladder: ranks 1-10 non-decreasing; Foundations (what embryology is,
gametogenesis, spermatogenesis, oogenesis, fertilization, cleavage,
blastulation, implantation, bilaminar disc, trilaminar disc, membranes)
-> Compounded (gastrulation, neurulation, body axes, somitogenesis,
folding, placenta, heart, vessels, skeleton, muscle, skin, lungs)
-> Advanced (gut, kidneys, genital system, brain, eye and ear, endocrine
glands, developmental genetics, teratology, twinning, fetal growth,
assisted reproduction).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos in build.py. Every demo prints its real computed values, asserts
tight bounds, and ends with the OK marker; the build machine-executes all
68 demos before commit.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature interpretation of "
            "embryology as the timed construction of the human body: every "
            "stage a build phase, every organ a system coming online on "
            "schedule. Clearly labeled Signature-made, never presented as "
            "authentic public record.")

ENTRIES = [
# ---------------------------------------------------------------- Foundations
dict(key="what_is",
     name="What Is Embryology: The Science of Prenatal Development",
     group="Foundations", ladder_rank=1, ladder_tier="foundations",
     description=(
        "Embryology is the science of prenatal development - the continuous, "
        "ordered transformation of a single fertilized cell into a newborn human "
        "over 280 days counted from the last menstrual period (266 days from "
        "fertilization itself). It studies gametogenesis, the making of eggs and "
        "sperm; fertilization, their fusion; the embryonic period, weeks 1 "
        "through 8, when every major organ system is founded; and the fetal "
        "period, weeks 9 through 38, when those systems grow, mature, and prepare "
        "for birth. The 23 Carnegie stages give the embryonic period a universal "
        "ruler, so a day-22 human embryo can be compared with any other. Because "
        "embryology maps how structures are built, it also explains how they "
        "break: teratology, the study of birth defects, is embryology read in "
        "reverse. This record frames the whole discipline and the ladder of "
        "records that follows."),
     how_it_works=(
        "Embryology works on two clocks that every student must keep straight. "
        "Gestational age counts from the first day of the last menstrual period, "
        "the convention of clinics and due dates; fertilization age counts from "
        "conception, two weeks later. A 'week 8' embryo is therefore 56 days "
        "gestational but only 42 days old. The embryonic period runs through the "
        "end of week 8: organogenesis, the founding of all systems. The fetal "
        "period runs week 9 to birth: growth and maturation. The demo works the "
        "calendar arithmetic that bounds the discipline: weeks, lunar months, "
        "and the share of gestation spent building versus growing."),
     key_points=[
        "Embryology = prenatal development: one cell to a newborn in 280 days (gestational) / 266 days (fertilization age).",
        "Embryonic period weeks 1-8: every organ system is founded. Fetal period weeks 9-38: growth and maturation.",
        "Gestational age = fertilization age + 14 days; clinics and due dates use gestational age.",
        "The 23 Carnegie stages stage the embryonic period by structure, not by calendar alone.",
        "Teratology is embryology in reverse: birth defects map onto the week their structure was built.",
        "Distinct from histology (tissues) and gross anatomy (the finished adult).",
     ],
     requirements=[
        "Both clocks kept straight: gestational age for the clinic, fertilization age for the biology.",
        "The Carnegie staging ruler for the embryonic period (23 stages).",
        "A week-by-week map of which systems found and which mature.",
        "The teratology mirror: every defect traced to its construction week.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024 - the discipline's standard text.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
        "O'Rahilly R, Muller F. Developmental Stages in Human Embryos. Carnegie Institution of Washington; 1987.",
     ],
     sig_lens=(
        "Signature lens: read gestation as the master build schedule of the "
        "human body - 280 days from order to delivery, with the first 56 as "
        "the tooling phase where every subsystem is founded and the rest as "
        "production ramp. The Signature embryologist treats the two clocks as "
        "the spec sheet's two datums: never mix them, never misread a "
        "milestone. Every later record in this database is one work package "
        "on that schedule.")),

dict(key="gametogenesis",
     name="Gametogenesis: Making the Reproductive Cells",
     group="Foundations", ladder_rank=1, ladder_tier="foundations",
     description=(
        "Gametogenesis is the production of the reproductive cells - sperm in "
        "the male, eggs in the female - by meiosis, the division that halves "
        "the chromosome number from 46 to 23. It is the only cell production "
        "line in the body whose product carries half a genome, so that "
        "fertilization restores the full 46 without doubling every generation. "
        "Meiosis also shuffles the deck twice: homologous chromosomes assort "
        "independently, and crossing over swaps segments between them, so no "
        "two gametes from one person are genetically identical. The male line "
        "runs continuously from puberty; the female line starts before birth, "
        "pauses for decades, and resumes one egg at a time. Everything in "
        "embryology begins with these two half-genomes."),
     how_it_works=(
        "Meiosis runs in two divisions. Meiosis I separates homologous "
        "chromosomes (reductional: 46 chromosomes as 23 pairs become 23 "
        "chromosomes in each daughter cell); meiosis II separates sister "
        "chromatids, like mitosis. Independent assortment means each of the 23 "
        "pairs orients randomly, giving 2 to the 23rd power genetically distinct "
        "gametes before crossing over is even counted. The demo computes that "
        "combinatorial space and the halving arithmetic that keeps the species "
        "chromosome number constant across generations."),
     key_points=[
        "Gametogenesis makes haploid cells (23 chromosomes) by meiosis so fertilization restores 46.",
        "Meiosis I separates homologs (reductional); meiosis II separates sister chromatids.",
        "Independent assortment yields 2^23 = 8,388,608 distinct gametes per person, before crossing over.",
        "Crossing over in prophase I swaps segments and multiplies the variation further.",
        "Male gametogenesis runs continuously from puberty; female starts fetally and pauses for decades.",
        "Without the halving step, chromosome number would double every generation.",
     ],
     requirements=[
        "Primordial germ cells migrated to the gonadal ridges by week 6.",
        "An intact two-division meiosis with homologous pairing and crossing over.",
        "Independent assortment across all 23 chromosome pairs.",
        "Sex-specific timing: continuous male production, arrested female stock.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Gilbert SF, Barresi MJF. Developmental Biology. 13th ed. Oxford University Press; 2023.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Gilbert SF, Barresi MJF. Developmental Biology. 13th ed. Oxford University Press; 2023.",
        "Carlson BM. Human Embryology and Developmental Biology. 6th ed. Elsevier; 2019.",
     ],
     sig_lens=(
        "Signature lens: treat the genome as a parts list that must be split "
        "exactly in half, twice, with the halves shuffled so no two kits are "
        "alike. The Signature reading of meiosis is a combinatorial engine: "
        "2^23 base variants per parent, times crossing over, is the variation "
        "budget of the whole species. Build the halving step wrong and the "
        "count drifts every generation.")),

dict(key="spermatogenesis",
     name="Spermatogenesis: Building Sperm, Step by Step",
     group="Foundations", ladder_rank=2, ladder_tier="foundations",
     description=(
        "Spermatogenesis is the male production line that turns spermatogonia, "
        "the stem cells of the testis, into spermatozoa inside the seminiferous "
        "tubules. It starts at puberty and never stops: each cycle takes about "
        "64 days from spermatogonium to finished sperm, plus roughly two weeks "
        "of maturation in the epididymis, and the testis runs many cycles in "
        "parallel to release on the order of 100 million sperm per day. Along "
        "the way, spermatogonia divide mitotically, primary spermatocytes run "
        "meiosis to make four spermatids each, and spermiogenesis rebuilds each "
        "round spermatid into a streamlined swimmer: condensed nucleus, acrosome "
        "cap, flagellum, and almost no cytoplasm. Sertoli cells nurse every "
        "step, and the blood-testis barrier keeps the immune system from ever "
        "meeting the half-genome cells it would attack."),
     how_it_works=(
        "The arithmetic of the line is fixed. One founder spermatogonium runs "
        "about five mitotic divisions to make 32 primary spermatocytes; meiosis "
        "then quadruples each one into 4 spermatids, so a single founder yields "
        "128 spermatozoa. Spermiogenesis reshapes without dividing: the Golgi "
        "builds the acrosome, the centriole grows the flagellum, mitochondria "
        "wrap the midpiece, and excess cytoplasm is shed. The demo runs the "
        "division tree and the pipeline stock implied by a 64-day cycle at 100 "
        "million sperm per day."),
     key_points=[
        "Spermatogenesis runs in seminiferous tubules from puberty onward, ~64 days per cycle plus epididymal maturation.",
        "One founder spermatogonium -> 32 primary spermatocytes (5 mitoses) -> 128 spermatozoa (meiosis x4 each).",
        "Spermiogenesis reshapes spermatids without dividing: acrosome, flagellum, condensed nucleus, shed cytoplasm.",
        "Output is on the order of 100 million sperm per day, cycles overlapping continuously.",
        "Sertoli cells nurse the line; the blood-testis barrier hides haploid cells from immunity.",
        "The acrosome built here is the drill bit fertilization will use.",
     ],
     requirements=[
        "Seminiferous tubules with an intact Sertoli-cell nursing epithelium.",
        "Five mitotic amplifications before meiosis, then two meiotic divisions per primary spermatocyte.",
        "A full spermiogenesis rebuild: acrosome, flagellum, mitochondrial midpiece, cytoplasm shedding.",
        "An intact blood-testis barrier for the whole 64-day cycle.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
        "Dudek RW. Embryology. 7th ed. (Board Review Series). Wolters Kluwer; 2019.",
     ],
     sig_lens=(
        "Signature lens: read the testis as a continuous-flow factory with a "
        "64-day takt time and a fixed 128x multiplication per founder cell. "
        "The Signature engineer prices the line by its division tree and its "
        "parallel cycles: throughput is founders times 128 divided by cycle "
        "time, and quality control is the Sertoli cell plus a barrier the "
        "immune system never crosses.")),

dict(key="oogenesis",
     name="Oogenesis: Building Eggs, From Fetus to Ovulation",
     group="Foundations", ladder_rank=2, ladder_tier="foundations",
     description=(
        "Oogenesis is the female production line, and it runs on the opposite "
        "schedule from the male's: it starts before birth, pauses for decades, "
        "and finishes one egg at a time. Oogonia multiply in the fetal ovary to "
        "about 7 million primary oocytes by the fifth month of gestation, then "
        "meiosis begins and arrests in prophase I - where every oocyte will wait, "
        "some for fifty years. By birth about 2 million remain, by puberty some "
        "300,000 to 400,000, and across a reproductive lifetime only 400 to 500 "
        "will ever ovulate; the rest are lost to atresia, a culling of 99.99 "
        "percent. Each menstrual cycle a cohort of primordial follicles awakens, "
        "one becomes dominant, its oocyte completes meiosis I to become a "
        "secondary oocyte arrested in metaphase II - and it completes meiosis II "
        "only if a sperm arrives. The follicle's granulosa and theca cells are "
        "the egg's life-support and hormone factory throughout."),
     how_it_works=(
        "The stock arithmetic is attrition arithmetic. Seven million primary "
        "oocytes at five fetal months fall to two million at birth, a few "
        "hundred thousand at puberty, and roughly four hundred ovulations per "
        "lifetime - each stage a fixed fraction of the last. Meiosis I produces "
        "one secondary oocyte and one first polar body (unequal division keeps "
        "the cytoplasm with the egg); meiosis II, triggered by fertilization, "
        "yields the ovum and a second polar body, the first polar body sometimes "
        "dividing again. The demo runs the attrition fractions and the polar "
        "body accounting."),
     key_points=[
        "Oogenesis starts fetally (~7M oocytes at 5 months), arrests in prophase I, and resumes one egg per cycle.",
        "Stock falls: 7M fetal -> ~2M at birth -> ~300-400K at puberty -> ~400-500 lifetime ovulations.",
        "Atresia claims ~99.99% of oocytes; ovulation is the rare exception, not the rule.",
        "Meiosis I makes a secondary oocyte + first polar body; meiosis II completes only at fertilization.",
        "Unequal divisions keep nearly all cytoplasm with the egg; polar bodies carry away the spare chromosomes.",
        "Follicle stages: primordial -> primary -> secondary (antral) -> mature Graafian, with theca and granulosa support.",
     ],
     requirements=[
        "A fetal oogonia pool established by the 5th gestational month (~7 million).",
        "Prophase I arrest (dictyotene) maintained for decades until the LH surge.",
        "Follicular life-support: granulosa, theca, zona pellucida, cumulus oophorus.",
        "Completion of meiosis II strictly conditional on sperm entry.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Schoenwolf GC, Bleyl SB, Brauer PR, Francis-West PH. Larsen's Human Embryology. 6th ed. Elsevier; 2021.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Schoenwolf GC, Bleyl SB, Brauer PR, Francis-West PH. Larsen's Human Embryology. 6th ed. Elsevier; 2021.",
        "Carlson BM. Human Embryology and Developmental Biology. 6th ed. Elsevier; 2019.",
     ],
     sig_lens=(
        "Signature lens: read the ovary as a strategic reserve, not a "
        "factory - the entire lifetime stock is minted before birth and then "
        "rationed by attrition at 99.99 percent. The Signature reading prices "
        "the reserve at every audit point (fetal, birth, puberty, ovulation) "
        "and treats the decades-long meiotic pause as suspended animation "
        "with a single wake-up condition: the LH surge.")),

dict(key="fertilization",
     name="Fertilization: The Moment of Conception",
     group="Foundations", ladder_rank=2, ladder_tier="foundations",
     description=(
        "Fertilization is the fusion of sperm and egg in the ampulla of the "
        "uterine tube, usually within a day of ovulation, and it accomplishes "
        "three things at once: it restores the diploid chromosome number to "
        "46, it determines the genetic sex of the embryo, and it triggers the "
        "start of cleavage. Of the roughly 300 million sperm deposited, only "
        "hundreds reach the ampulla; capacitation in the female tract primes "
        "them, the acrosome reaction drills through the zona pellucida, and "
        "one sperm's membrane fuses with the oocyte's. The cortical reaction "
        "then hardens the zona against polyspermy within minutes. The oocyte "
        "completes meiosis II, male and female pronuclei form and fuse, and "
        "the zygote - a single totipotent cell - begins its first division "
        "about 24 hours later."),
     how_it_works=(
        "The selection arithmetic is brutal: hundreds of survivors from 300 "
        "million is a pass rate near two in ten million. Zona binding is "
        "species-specific (ZP3 receptor), the acrosome releases hyaluronidase "
        "and acrosin, and membrane fusion admits exactly one nucleus; the "
        "cortical granule exocytosis that follows makes polyspermy nearly "
        "impossible. Pronuclear fusion reconstitutes 23 pairs, and the sex "
        "chromosome contributed by the sperm - X or Y - sets male or female. "
        "The demo computes the selection ratio and the chromosome accounting."),
     key_points=[
        "Fertilization happens in the ampulla of the uterine tube, within ~24 hours of ovulation.",
        "~300 million sperm deposited; only hundreds reach the egg - selection is extreme.",
        "Capacitation, acrosome reaction, zona penetration (ZP3), membrane fusion, in that order.",
        "The cortical reaction blocks polyspermy; one sperm nucleus is the rule.",
        "Three results at once: diploidy restored (46), sex determined (sperm's X or Y), cleavage triggered.",
        "The oocyte finishes meiosis II only after sperm entry; pronuclei fuse into the zygote.",
     ],
     requirements=[
        "A capacitated sperm cohort that survived the tract to the ampulla.",
        "An intact zona pellucida with functional ZP3 binding and a working cortical reaction.",
        "A secondary oocyte arrested in metaphase II, ready to complete division on entry.",
        "Pronuclear formation and fusion reconstituting 23 chromosome pairs.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
        "Gilbert SF, Barresi MJF. Developmental Biology. 13th ed. Oxford University Press; 2023.",
     ],
     sig_lens=(
        "Signature lens: treat conception as a three-output transaction that "
        "must clear atomically - restore the count to 46, set the sex bit, "
        "start the division clock - or abort. The Signature design admires "
        "the cortical reaction most: a one-shot lock that fires in minutes "
        "and makes a second entry nearly impossible, because two genomes is "
        "exactly right and three is fatal.")),

dict(key="cleavage",
     name="Cleavage: The First Divisions of the Zygote",
     group="Foundations", ladder_rank=2, ladder_tier="foundations",
     description=(
        "Cleavage is the zygote's first divisions: rapid mitoses with no cell "
        "growth between them, so the embryo subdivides its fixed volume into "
        "ever-smaller cells called blastomeres. Two cells, then four, then "
        "eight - at the eight-cell stage the blastomeres compact, maximizing "
        "contact and polarizing into outer and inner populations, the first "
        "decision the embryo ever makes. By day 3 to 4 the embryo is a solid "
        "ball of about 16 cells, the morula, still small enough to drift down "
        "the uterine tube. Early blastomeres are totipotent: each one, isolated, "
        "could still build a whole embryo, which is why splitting at this stage "
        "makes identical twins. Cleavage ends where blastulation begins."),
     how_it_works=(
        "With no growth, volume is conserved: each division halves the volume "
        "per cell, and cell diameter shrinks by the cube root of two per round. "
        "Starting from a ~100-micrometer zygote, four rounds give 16 blastomeres "
        "each near 40 micrometers across - the morula. Compaction at the "
        "eight-cell stage is driven by E-cadherin adhesion: outer cells "
        "polarize toward trophectoderm fate, inner cells toward the inner cell "
        "mass. The demo runs the 2^n census and the shrinking-cell geometry."),
     key_points=[
        "Cleavage = mitosis without growth: the zygote subdivides a fixed volume into blastomeres.",
        "2 -> 4 -> 8 -> ~16 cells (morula, day 3-4); cell diameter shrinks by the cube root of 2 per division.",
        "Compaction at the 8-cell stage: first polarization, outer vs inner cell fate.",
        "Early blastomeres are totipotent - splitting here yields identical twins.",
        "The morula enters the uterus around day 4, still wrapped in the zona pellucida.",
        "Cleavage sets up blastulation; volume is conserved throughout.",
     ],
     requirements=[
        "A totipotent zygote with an intact zona pellucida containing the divisions.",
        "Mitotic cycles with no G1/G2 growth phases between them.",
        "E-cadherin-mediated compaction at the 8-cell stage.",
        "Totipotency maintained through the morula so each blastomere stays fully potent.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Gilbert SF, Barresi MJF. Developmental Biology. 13th ed. Oxford University Press; 2023.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Gilbert SF, Barresi MJF. Developmental Biology. 13th ed. Oxford University Press; 2023.",
        "Dudek RW. Embryology. 7th ed. (Board Review Series). Wolters Kluwer; 2019.",
     ],
     sig_lens=(
        "Signature lens: read cleavage as subdividing a fixed budget with "
        "zero new material - every division spends volume to buy cell count. "
        "The Signature engineer notes the elegance: totipotency is conserved "
        "until compaction, so the system stays fully re-partitionable through "
        "the 8-cell stage, and the first real decision (inside vs outside) is "
        "made by geometry, not by genes.")),

dict(key="blastulation",
     name="Blastulation: Forming the Blastocyst",
     group="Foundations", ladder_rank=3, ladder_tier="foundations",
     description=(
        "Blastulation turns the solid morula into the blastocyst, a hollow ball "
        "of about 100 cells with its first two cell populations assigned. The "
        "outer trophectoderm will build the placenta and membranes; the inner "
        "cell mass, or embryoblast, will build the embryo itself; and the "
        "fluid-filled blastocoel cavity separates them. This happens around day "
        "5 as the embryo floats free in the uterus. On day 5 to 6 the blastocyst "
        "hatches from the zona pellucida - the shell that contained cleavage - "
        "so the trophectoderm can touch the uterine lining and implantation can "
        "begin. The inner cell mass is pluripotent, the source of embryonic "
        "stem cells, and its position against one wall of the cavity already "
        "marks the embryonic pole."),
     how_it_works=(
        "Trophectoderm cells pump sodium and water inward, inflating the "
        "blastocoel; the inner cell mass compacts at the embryonic pole while "
        "the trophectoderm thins into an epithelium. Roughly a quarter of the "
        "~100 cells become inner cell mass and three quarters trophectoderm - "
        "the placenta gets the larger founding crew because its job starts "
        "first. Hatching is enzymatic and mechanical: the blastocyst pulses, "
        "the zona thins, and the embryo squeezes out. The demo computes the "
        "cell census split and the cavity geometry of a day-5 blastocyst."),
     key_points=[
        "Blastulation (~day 5) converts the solid morula into a hollow ~100-cell blastocyst.",
        "Two lineages: trophectoderm (placenta/membranes) and inner cell mass (the embryo proper).",
        "The blastocoel cavity is inflated by trophectoderm fluid transport.",
        "Roughly 1/4 of cells form the inner cell mass; 3/4 form trophectoderm.",
        "Hatching from the zona pellucida (day 5-6) frees the embryo for implantation.",
        "The inner cell mass is pluripotent - the natural source of embryonic stem cells.",
     ],
     requirements=[
        "A compacted morula with polarized outer and inner blastomere populations.",
        "Trophectoderm tight junctions and fluid transport to inflate the blastocoel.",
        "An inner cell mass correctly positioned at the embryonic pole.",
        "Enzymatic hatching from the zona pellucida on schedule, day 5-6.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Schoenwolf GC, Bleyl SB, Brauer PR, Francis-West PH. Larsen's Human Embryology. 6th ed. Elsevier; 2021.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Schoenwolf GC, Bleyl SB, Brauer PR, Francis-West PH. Larsen's Human Embryology. 6th ed. Elsevier; 2021.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
     ],
     sig_lens=(
        "Signature lens: the blastocyst is the first org chart - two "
        "divisions, support staff (trophectoderm) outnumbering the core team "
        "(inner cell mass) three to one, because life support must be built "
        "before the product. The Signature reading treats hatching as the "
        "hand-off milestone: the shell that protected the build is discarded "
        "the moment the embryo is ready to dock.")),

dict(key="implantation",
     name="Implantation: Burrowing Into the Uterus",
     group="Foundations", ladder_rank=3, ladder_tier="foundations",
     description=(
        "Implantation is the week the free-floating blastocyst burrows into "
        "the uterine wall and plugs into the maternal blood supply, days 6 "
        "through 12. The trophectoderm differentiates into an inner "
        "cytotrophoblast and an invasive outer syncytiotrophoblast - a "
        "multinucleated battering ram that digests decidua, taps maternal "
        "capillaries, and opens the lacunar blood spaces that will become the "
        "placenta. The syncytiotrophoblast also secretes human chorionic "
        "gonadotropin (hCG), the hormone pregnancy tests detect, which rescues "
        "the corpus luteum and keeps progesterone flowing. Implantation "
        "usually lands on the upper posterior wall; landing in the tube gives "
        "an ectopic pregnancy, and low landing over the cervix gives placenta "
        "previa. By day 12 the embryo is fully buried and the implantation "
        "site heals over."),
     how_it_works=(
        "The timing is a hormone clock. Implantation starts day 6-7; hCG "
        "secretion begins almost immediately and doubles about every 48 hours, "
        "so from a few mIU/mL at implantation it crosses the ~25 mIU/mL urine "
        "test threshold around day 11-12 - the first missed period. The "
        "endometrium is receptive only in the implantation window, roughly days "
        "20-24 of the cycle, synchronized by estrogen then progesterone. The "
        "demo runs the hCG doubling curve and the window arithmetic."),
     key_points=[
        "Implantation runs days 6-12: the blastocyst burrows fully into the decidua.",
        "Syncytiotrophoblast invades, taps maternal blood, and secretes hCG.",
        "hCG doubles ~every 48 hours; pregnancy tests turn positive around day 11-12.",
        "The implantation window is cycle days ~20-24, set by estrogen then progesterone.",
        "Wrong address, wrong outcome: tubal implantation = ectopic; cervical = previa.",
        "Rescued by hCG, the corpus luteum keeps progesterone up until the placenta takes over (~week 8-9).",
     ],
     requirements=[
        "A hatched blastocyst with invasive syncytiotrophoblast capability.",
        "A receptive decidua inside the implantation window (cycle days ~20-24).",
        "Maternal spiral arteries tappable for the lacunar circulation.",
        "hCG signaling strong enough to rescue the corpus luteum.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
        "Carlson BM. Human Embryology and Developmental Biology. 6th ed. Elsevier; 2019.",
     ],
     sig_lens=(
        "Signature lens: implantation is docking and commissioning - the "
        "embryo plugs into maternal infrastructure and immediately starts "
        "broadcasting its keep-alive signal, hCG, on a strict 48-hour "
        "doubling schedule. The Signature engineer reads the doubling curve "
        "as a heartbeat: on-schedule doubling means the build is proceeding; "
        "a flat line means it has stalled.")),

dict(key="bilaminar_disc",
     name="The Bilaminar Disc: Two Layers, One Future Body",
     group="Foundations", ladder_rank=3, ladder_tier="foundations",
     description=(
        "In week 2 the inner cell mass flattens into the bilaminar disc: two "
        "layers of cells, epiblast above and hypoblast below, that are the "
        "entire embryo proper. The epiblast is the real founder - it will "
        "generate all three germ layers and the amnion; the hypoblast mostly "
        "lines the yolk sac and then is displaced. Meanwhile the disc's "
        "surroundings are built: the amniotic cavity opens above the epiblast, "
        "the yolk sac balloons below the hypoblast, the chorionic cavity "
        "forms, and the connecting stalk - the future umbilical cord - tethers "
        "embryo to chorion. Week 2 is famously the 'all-or-none' period: an "
        "insult either kills the conceptus or is fully repaired, because no "
        "organ foundations exist yet to be half-built."),
     how_it_works=(
        "Geometry first: a disc about half a millimeter across, epiblast "
        "columnar cells on top, hypoblast cuboidal cells beneath, area near "
        "0.2 square millimeters. Cavitation splits the inner cell mass: cells "
        "above the split become amniotic epithelium, the disc stays in the "
        "middle, and hypoblast cells migrate to line the yolk sac. The "
        "trophoblast shell around all of it keeps thickening into the chorion. "
        "The demo computes the disc area and the cavity layout of the week-2 "
        "conceptus."),
     key_points=[
        "Week 2: the inner cell mass becomes a two-layered disc - epiblast (above) and hypoblast (below).",
        "The epiblast founds the embryo proper, all germ layers, and the amnion; the hypoblast lines the yolk sac.",
        "Built around it: amniotic cavity above, yolk sac below, chorionic cavity outside, connecting stalk tethering.",
        "Disc diameter ~0.5 mm: the whole future body is a speck.",
        "Week 2 is the all-or-none window: insults kill or are fully repaired - no partial organ defects yet.",
        "The bilaminar disc is the launch pad gastrulation will act on.",
     ],
     requirements=[
        "An inner cell mass correctly split into epiblast and hypoblast sheets.",
        "Cavitation forming the amniotic cavity above and yolk sac below on schedule.",
        "A chorionic cavity and connecting stalk linking embryo to chorion.",
        "Trophoblast integrity throughout - the shell holds while the disc organizes.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "O'Rahilly R, Muller F. Human Embryology & Teratology. 3rd ed. Wiley-Liss; 2001.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "O'Rahilly R, Muller F. Human Embryology & Teratology. 3rd ed. Wiley-Liss; 2001.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
     ],
     sig_lens=(
        "Signature lens: week 2 is site preparation - two foundation slabs "
        "poured (epiblast, hypoblast), utilities trenched (cavities, stalk), "
        "perimeter fenced (trophoblast). The Signature reading honors the "
        "all-or-none rule as the cleanest quality gate in the schedule: "
        "before any system is founded, the only verdicts are pass or scrap, "
        "never rework.")),

dict(key="trilaminar_disc",
     name="The Trilaminar Disc: Three Germ Layers",
     group="Foundations", ladder_rank=3, ladder_tier="foundations",
     description=(
        "In week 3 gastrulation converts the two-layered disc into three germ "
        "layers - ectoderm, mesoderm, and endoderm - and that trio builds "
        "every tissue in the body. The fate map is worth memorizing: ectoderm "
        "makes skin, nervous system, and sense organs; mesoderm makes muscle, "
        "bone, blood, heart, kidneys, and gonads; endoderm makes the lining of "
        "the gut tube and the liver, pancreas, and lung linings that bud from "
        "it. The layers form as epiblast cells dive through the primitive "
        "streak and spread between epiblast (now ectoderm) and hypoblast "
        "(displaced by endoderm). By the end of week 3 the disc is trilaminar "
        "along most of its length, the notochord runs down the midline, and "
        "the embryo has its first body axes."),
     how_it_works=(
        "Epiblast cells undergo epithelial-to-mesenchymal transition at the "
        "primitive streak, ingress, and migrate: the first wave displaces the "
        "hypoblast as definitive endoderm, the next spreads as mesoderm, and "
        "the epiblast that stays put becomes ectoderm. The primitive streak "
        "occupies roughly the caudal half of the ~2 mm disc at its peak, then "
        "regresses. The demo computes the streak's share of the disc and the "
        "three-layer fate accounting that every later organ record will "
        "reference."),
     key_points=[
        "Week 3: gastrulation builds the three germ layers - ectoderm, mesoderm, endoderm.",
        "Ectoderm -> skin, nervous system, sense organs. Mesoderm -> muscle, bone, blood, heart, kidneys, gonads.",
        "Endoderm -> gut lining plus liver, pancreas, and respiratory linings.",
        "Epiblast cells ingress through the primitive streak; the streak occupies ~half the disc at peak.",
        "The hypoblast is displaced by definitive endoderm; remaining epiblast becomes ectoderm.",
        "The trilaminar disc plus notochord is the substrate for neurulation and organogenesis.",
     ],
     requirements=[
        "A primitive streak with an active epithelial-to-mesenchymal transition zone.",
        "Ordered ingression: endoderm first (displacing hypoblast), then mesoderm, epiblast retained as ectoderm.",
        "A midline notochord laid down as the streak regresses.",
        "Cranial and caudal integrity: buccopharyngeal and cloacal membranes stay bilaminar.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Gilbert SF, Barresi MJF. Developmental Biology. 13th ed. Oxford University Press; 2023.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Gilbert SF, Barresi MJF. Developmental Biology. 13th ed. Oxford University Press; 2023.",
        "Schoenwolf GC, Bleyl SB, Brauer PR, Francis-West PH. Larsen's Human Embryology. 6th ed. Elsevier; 2021.",
     ],
     sig_lens=(
        "Signature lens: three material stocks issued from one warehouse - "
        "every organ in the catalog draws from ectoderm, mesoderm, or "
        "endoderm, no exceptions, no fourth supplier. The Signature bill of "
        "materials starts here: memorize the fate map and every later build "
        "record becomes a sourcing trace back to week 3.")),

dict(key="membranes",
     name="Extraembryonic Membranes: The Support System",
     group="Foundations", ladder_rank=3, ladder_tier="foundations",
     description=(
        "The extraembryonic membranes are the embryo's life-support package, "
        "built from the same zygote but never part of the baby: the amnion, a "
        "fluid-filled sac that cushions and lets the embryo move; the yolk sac, "
        "the first blood factory and the highway primordial germ cells travel; "
        "the allantois, a small outpouching whose vessels become the umbilical "
        "cord's and whose remnant becomes the median umbilical ligament; and "
        "the chorion, the outer shell that becomes the fetal half of the "
        "placenta. The umbilical cord - two arteries carrying waste out, one "
        "vein bringing oxygen and nutrients in, all bedded in Wharton's jelly - "
        "is the finished cable. Amniotic fluid grows from about 30 mL at week "
        "10 to a liter near term, and the fetus drinks and recycles it "
        "constantly."),
     how_it_works=(
        "Each membrane has a job and a schedule. The amnion expands to line "
        "the whole chorionic cavity; the yolk sac makes the first blood "
        "islands (day 17-18) and then shrinks; the allantoic vessels grow into "
        "the connecting stalk, which lengthens into the cord. Fluid volume "
        "rises roughly 4-5 mL per day between weeks 10 and 20 as fetal urine "
        "production starts and swallowing begins. The demo runs the fluid "
        "growth curve and the cord's cable geometry."),
     key_points=[
        "Four membranes: amnion (cushion + movement), yolk sac (first blood, germ-cell highway), allantois (cord vessels), chorion (placenta shell).",
        "The cord carries 2 arteries + 1 vein in Wharton's jelly - arteries out, vein in.",
        "Amniotic fluid: ~30 mL at week 10 -> ~350 mL at week 20 -> ~1000 mL near term.",
        "The fetus swallows and recycles amniotic fluid; urine production drives late volume.",
        "Allantois remnant becomes the median umbilical ligament; yolk sac remnant can persist as Meckel diverticulum.",
        "None of the membranes join the baby - all are delivered as afterbirth.",
     ],
     requirements=[
        "Amnion expansion tracking the growing embryo without rupture.",
        "Yolk-sac hematopoiesis active days 17-18 through week 6, then orderly regression.",
        "Allantoic vessels integrated into the connecting stalk / cord.",
        "Chorion differentiated into villous (placental) and smooth zones.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
        "Cochard LR, ed. Netter's Atlas of Human Embryology. Icon Learning Systems; 2002.",
     ],
     sig_lens=(
        "Signature lens: the membranes are the temporary site infrastructure "
        "- scaffolding, water supply, and waste lines that are demolished at "
        "handover and never appear in the finished building. The Signature "
        "planner budgets them like formwork: essential, precisely timed, and "
        "designed for clean removal at delivery.")),
]

# ---------------------------------------------------------------- Compounded
ENTRIES += [
dict(key="gastrulation",
     name="Gastrulation: The Primitive Streak and the Body Plan",
     group="Compounded", ladder_rank=4, ladder_tier="compounded",
     description=(
        "Gastrulation is the week-3 event that turns the flat bilaminar disc "
        "into the three-layered embryo with a head end, a tail end, a back, a "
        "belly, and a midline - the body plan in first draft. It starts around "
        "day 15 when the primitive streak appears at the caudal end of the "
        "epiblast: a groove down which epiblast cells dive into the interior, "
        "emerging as mesoderm and endoderm. At the streak's cranial tip sits "
        "the primitive node, which lays down the notochord - the stiff midline "
        "rod that will pattern the neural tube above it and become the nuclei "
        "of the intervertebral discs. As ingression proceeds the streak "
        "regresses tailward and is gone by about day 26. A streak that fails "
        "to regress can seed a sacrococcygeal teratoma, the commonest newborn "
        "tumor, and a doubled streak can produce conjoined twins."),
     how_it_works=(
        "The streak is a moving construction front. It elongates to about "
        "1 mm at peak - roughly half the 2-mm disc - then the node regresses "
        "caudally at roughly 140 micrometers per day, laying notochord behind "
        "it like a surveyor's chalk line. Cells ingressing through the streak's "
        "cranial half become axial and paraxial mesoderm; through the caudal "
        "half, lateral plate and extraembryonic mesoderm. The demo computes the "
        "regression rate and the streak's peak share of the disc."),
     key_points=[
        "Gastrulation (week 3, from ~day 15) builds the trilaminar embryo and the body plan.",
        "The primitive streak is the ingression groove; the primitive node at its tip lays the notochord.",
        "Epiblast -> mesoderm + endoderm via epithelial-to-mesenchymal transition at the streak.",
        "The streak peaks ~1 mm, then regresses tailward at ~140 um/day, gone by ~day 26.",
        "The notochord patterns the neural tube and becomes the disc nuclei.",
        "Streak failures: persistent remnants -> sacrococcygeal teratoma; duplicated streak -> conjoined twinning.",
     ],
     requirements=[
        "A caudal primitive streak appearing on schedule around day 15.",
        "An active primitive node laying notochord as it regresses.",
        "Ordered mesoderm patterning: axial, paraxial, intermediate, lateral plate.",
        "Complete streak regression by ~day 26 with no persistent remnants.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Gilbert SF, Barresi MJF. Developmental Biology. 13th ed. Oxford University Press; 2023.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Gilbert SF, Barresi MJF. Developmental Biology. 13th ed. Oxford University Press; 2023.",
        "Schoenwolf GC, Bleyl SB, Brauer PR, Francis-West PH. Larsen's Human Embryology. 6th ed. Elsevier; 2021.",
     ],
     sig_lens=(
        "Signature lens: the primitive streak is the groundbreaking ceremony "
        "that is also the construction - one moving front that both digs the "
        "foundation and pours the centerline. The Signature scheduler treats "
        "its regression as the critical path of week 3: the front must sweep "
        "the full length and demobilize cleanly, because anything left behind "
        "becomes a tumor and anything doubled becomes two bodies.")),

dict(key="neurulation",
     name="Neurulation: Building the Neural Tube",
     group="Compounded", ladder_rank=4, ladder_tier="compounded",
     description=(
        "Neurulation builds the central nervous system from a flat sheet. "
        "Around day 18 the notochord signals the ectoderm above it to thicken "
        "into the neural plate; the plate's edges rise as neural folds, the "
        "center sinks as the neural groove, and the folds meet and fuse into "
        "the neural tube - the future brain and spinal cord - while the "
        "surface ectoderm reseals above it. Closure starts mid-embryo and "
        "zips both ways: the cranial neuropore closes around day 25, the "
        "caudal around day 28. As the folds rise, neural crest cells delaminate "
        "from their tips and migrate everywhere - they will become sensory "
        "neurons, Schwann cells, melanocytes, adrenal medulla, and much of the "
        "face. Failed closure gives neural tube defects: anencephaly "
        "cranially, spina bifida caudally, at about 1 in 1,000 births - "
        "roughly halved by periconceptional folic acid."),
     how_it_works=(
        "Closure is a zipper with two deadlines: cranial day 25, caudal day "
        "28, a three-day window after the folds first meet around day 22. The "
        "cranial tube balloons into the three primary brain vesicles while the "
        "caudal tube stays narrow as spinal cord. Neural crest migration is "
        "the embryo's great diaspora, dispatched in waves from the dorsal "
        "tube. The demo runs the closure calendar and the defect-rate "
        "arithmetic with folic acid protection."),
     key_points=[
        "Neural plate (day 18) -> neural groove -> neural tube; surface ectoderm reseals above.",
        "Closure zips from the middle outward: cranial neuropore ~day 25, caudal ~day 28.",
        "The cranial tube becomes brain; the caudal tube becomes spinal cord.",
        "Neural crest cells leave the fold tips and build PNS, melanocytes, adrenal medulla, facial structures.",
        "Open defects: anencephaly (cranial) and spina bifida (caudal), ~1/1000 births.",
        "Periconceptional folic acid (0.4 mg) cuts neural tube defect risk by about half to two-thirds.",
     ],
     requirements=[
        "Notochord signaling sufficient to induce the neural plate on schedule.",
        "Neural fold apposition and fusion progressing cranially and caudally without delay.",
        "Both neuropores closed by day 28 - the non-negotiable deadline.",
        "Neural crest delamination and migration waves dispatched from the dorsal tube.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
        "O'Rahilly R, Muller F. Human Embryology & Teratology. 3rd ed. Wiley-Liss; 2001.",
     ],
     sig_lens=(
        "Signature lens: neurulation is rolling a flat sheet into a sealed "
        "pressure vessel on a ten-day schedule with two hard close-out "
        "dates. The Signature inspector watches the zippers - day 25 "
        "cranial, day 28 caudal - because a tube left open is the costliest "
        "defect in the catalog, and the cheapest prevention ever found is a "
        "vitamin taken before the build starts.")),

dict(key="body_axes",
     name="Body Axes: Head, Tail, Back, and Belly",
     group="Compounded", ladder_rank=4, ladder_tier="compounded",
     description=(
        "Before any organ forms, the embryo must know which way is up: three "
        "body axes are laid down in week 3. The cranial-caudal axis (head to "
        "tail) is set by the primitive streak's position and later refined by "
        "Hox genes; the dorsal-ventral axis (back to belly) is set by the "
        "notochord below and the surface ectoderm above, pitting Sonic "
        "hedgehog signals from the floor against BMP signals from the roof; "
        "and the left-right axis is set by rotating cilia at the node, whose "
        "leftward flow breaks symmetry and starts the asymmetric cascade. "
        "Morphogen gradients - diffusible signals read as concentration - tell "
        "each cell its coordinates: Wolpert's French flag model shows how one "
        "gradient with two thresholds paints three territories. Get an axis "
        "wrong and organs form in the wrong place: situs inversus mirrors the "
        "body left-right."),
     how_it_works=(
        "A morphogen gradient is positional arithmetic. With a source at one "
        "pole decaying across the field, two thresholds divide the field into "
        "three fates at the one-third and two-third marks - the French flag. "
        "Hox genes then stamp the cranial-caudal address: their order on the "
        "chromosome matches their order of expression along the body "
        "(colinearity), 39 genes in 4 clusters each reading 180 base pairs of "
        "homeobox. The demo computes the French-flag thresholds and the Hox "
        "cluster accounting."),
     key_points=[
        "Three axes are set in week 3: cranial-caudal, dorsal-ventral, left-right.",
        "Cranial-caudal: primitive streak position, refined by Hox colinearity.",
        "Dorsal-ventral: notochord/Shh (ventral) vs ectoderm/BMP (dorsal).",
        "Left-right: nodal cilia drive leftward flow, breaking symmetry.",
        "Morphogen gradients + thresholds = positional information (French flag model).",
        "Axis errors mirror or misplace organs: situs inversus, holoprosencephaly spectrum.",
     ],
     requirements=[
        "A primitive streak defining the caudal pole and the midline.",
        "Opposing Shh (floor plate/notochord) and BMP (roof plate/ectoderm) gradients.",
        "Motile nodal cilia generating leftward flow at the node.",
        "Intact Hox clusters preserving 3-prime to 5-prime colinearity.",
     ],
     standards=[
        "Gilbert SF, Barresi MJF. Developmental Biology. 13th ed. Oxford University Press; 2023.",
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
     ],
     citations=[
        "Gilbert SF, Barresi MJF. Developmental Biology. 13th ed. Oxford University Press; 2023.",
        "Mallo M, Wellik DM, Deschamps J. Hox genes and regional patterning of the vertebrate body plan. Dev Biol. 2010;344(1):7-15.",
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
     ],
     sig_lens=(
        "Signature lens: axes are the coordinate system every later "
        "instruction is written in - no part can be placed until the datum "
        "lines exist. The Signature surveyor stakes three lines in week 3 "
        "and never moves them again; the French flag is the simplest "
        "possible addressing scheme, one gradient and two thresholds, and "
        "the whole body plan is addressed mail sent to those coordinates.")),

dict(key="somitogenesis",
     name="Somitogenesis: Segmenting the Body",
     group="Compounded", ladder_rank=5, ladder_tier="compounded",
     description=(
        "Somitogenesis carves the paraxial mesoderm into 42 to 44 pairs of "
        "somites - the segments the whole body is built from, laid down head "
        "to tail like boxcars. Each somite differentiates into three "
        "compartments with lifelong jobs: the sclerotome becomes vertebrae and "
        "ribs, the myotome becomes skeletal muscle, the dermatome becomes the "
        "dermis of the back. The count breaks down as 4 occipital, 8 cervical, "
        "12 thoracic, 5 lumbar, 5 sacral, and 8 to 10 coccygeal pairs. Because "
        "somites appear in strict order, embryologists stage young embryos by "
        "somite number the way others use the calendar. The segmentation clock "
        "- oscillating Notch and Wnt signals sweeping down the presomitic "
        "mesoderm - times each cut, and Hox genes then give each segment its "
        "regional identity: neck, thorax, or lower back."),
     how_it_works=(
        "The clock-and-wavefront model is the mechanism: a molecular "
        "oscillator ticks in the presomitic mesoderm while a maturation "
        "wavefront moves tailward, and each tick at the wavefront pinches off "
        "one somite pair. The regional census adds to 43 in the standard "
        "account (4+8+12+5+5+9), inside the 42-44 range; the occipital four "
        "mostly disperse, leaving the familiar vertebral column. The demo "
        "verifies the somite census arithmetic and the three-compartment fate "
        "split."),
     key_points=[
        "Paraxial mesoderm segments into 42-44 somite pairs, cranial to caudal.",
        "Each somite -> sclerotome (vertebrae/ribs) + myotome (muscle) + dermatome (dermis).",
        "Census: 4 occipital + 8 cervical + 12 thoracic + 5 lumbar + 5 sacral + 8-10 coccygeal.",
        "Somite number stages the embryo (Carnegie staging uses the count).",
        "The segmentation clock (Notch/Wnt oscillation) times each cut; Hox genes assign regional identity.",
        "Sclerotome resegments to build each vertebra from halves of two adjacent somites.",
     ],
     requirements=[
        "Paraxial mesoderm flanking the notochord, competent to segment.",
        "A running segmentation clock with a clean cranial-to-caudal wavefront.",
        "Three-compartment differentiation in every somite: sclerotome, myotome, dermatome.",
        "Hox-coded regional identity so cervical stays cervical and thoracic stays thoracic.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Gilbert SF, Barresi MJF. Developmental Biology. 13th ed. Oxford University Press; 2023.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Gilbert SF, Barresi MJF. Developmental Biology. 13th ed. Oxford University Press; 2023.",
        "O'Rahilly R, Muller F. Developmental Stages in Human Embryos. Carnegie Institution of Washington; 1987.",
     ],
     sig_lens=(
        "Signature lens: somitogenesis is the body run through a "
        "cookie-cutter 43 times on a metronome - identical segments stamped "
        "in order, then customized by address. The Signature manufacturer "
        "loves this pattern: one tool, one rhythm, mass-produced modules, "
        "with the Hox code as the only customization step. Count the "
        "segments and you can date the build.")),

dict(key="folding",
     name="Folding of the Embryo: From Disc to Tube",
     group="Compounded", ladder_rank=5, ladder_tier="compounded",
     description=(
        "Folding converts the flat trilaminar disc into a cylindrical body, "
        "and it happens in week 4 through four coordinated folds: the head "
        "fold tucks the future brain downward, the tail fold tucks the tail, "
        "and the two lateral folds roll the sides together underneath. As the "
        "edges meet, the endoderm-lined yolk sac is drawn inside to become the "
        "gut tube, the amniotic cavity expands to surround the whole embryo, "
        "and the connecting stalk is carried to the belly to become the "
        "umbilical cord. The embryo ends the month curled into a C-shape with "
        "a crown-rump length of just 2 to 3 millimeters. Folding failures leave "
        "the body wall open: gastroschisis and omphalocele are lateral-fold "
        "defects with very different coverings and prognoses."),
     how_it_works=(
        "The folds are growth differentials: the head and the neural tube "
        "grow faster than the disc beneath, so the cranial end overhangs and "
        "tucks; lateral growth rolls the edges ventrally until they meet at "
        "the midline, zippering the gut tube shut except at the vitelline "
        "duct. The yolk sac connection narrows to a stalk, the amnion "
        "balloons outward, and the embryo that began as a 2-mm disc becomes a "
        "curved cylinder. The demo computes the fold inventory and the "
        "resulting body proportions."),
     key_points=[
        "Week 4: head fold + tail fold + paired lateral folds convert disc to cylinder.",
        "Lateral folding internalizes the gut tube and brings the cord to the belly.",
        "The amnion expands to enclose the embryo; the yolk sac connection narrows to the vitelline duct.",
        "End of week 4: C-shaped embryo, crown-rump length ~2-3 mm.",
        "Lateral-fold failures: gastroschisis (no covering sac) vs omphalocele (covered by amnion/peritoneum).",
        "Folding positions every organ's raw material for organogenesis.",
     ],
     requirements=[
        "Differential growth driving head, tail, and lateral folds on schedule in week 4.",
        "Ventral midline fusion zippering the gut tube with only the vitelline duct left open.",
        "Amniotic expansion keeping pace so the embryo is never constricted.",
        "Connecting stalk carried ventrally to form the umbilical cord insertion.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
        "Dudek RW. Embryology. 7th ed. (Board Review Series). Wolters Kluwer; 2019.",
     ],
     sig_lens=(
        "Signature lens: folding is the sheet-metal operation of the build - "
        "a flat blank folded into a tube in four bends, with the plumbing "
        "(gut) captured inside the fold and the umbilical drawn to the "
        "belly seam. The Signature fabricator checks the seam: a lateral "
        "fold that does not close is a body wall left open, and the "
        "difference between a covered and uncovered defect is the difference "
        "between a patch and a crisis.")),

dict(key="placenta",
     name="The Placenta: The Organ That Feeds Two",
     group="Compounded", ladder_rank=5, ladder_tier="compounded",
     description=(
        "The placenta is the only disposable organ: built jointly by fetus "
        "(chorionic villi) and mother (decidua), run for nine months, then "
        "delivered and discarded. Its core is the chorionic villus tree - "
        "tertiary villi with fetal capillaries inside, bathed outside in "
        "maternal blood filling the intervillous space. This is a hemochorial "
        "arrangement: maternal blood directly bathes fetal tissue, separated "
        "only by the placental barrier (syncytiotrophoblast, cytotrophoblast, "
        "connective tissue, fetal endothelium). The placenta breathes, feeds, "
        "and excretes for the fetus; it manufactures hCG, progesterone, "
        "estrogens, and human placental lactogen; and it shields with selective "
        "immune tolerance. At term it weighs about 500 grams across a 20-cm "
        "disc, exchanges across 10-14 square meters of villous surface, and "
        "receives some 600 mL of maternal blood per minute."),
     how_it_works=(
        "Exchange is flow-limited arithmetic. About 150 mL of maternal blood "
        "sits in the intervillous space at any moment; at 600 mL/min inflow it "
        "turns over four times per minute, keeping the gradient steep. The "
        "villous surface of ~12 square meters is over 300 times the disc's own "
        "footprint - the placenta is a heat exchanger folded into a pancake. "
        "Hormone output ramps until the placenta takes over progesterone from "
        "the corpus luteum around weeks 8-9. The demo runs the turnover and "
        "surface-amplification numbers."),
     key_points=[
        "The placenta is fetomaternal and disposable: built for the pregnancy, delivered after.",
        "Hemochorial design: maternal blood bathes chorionic villi across a four-layer barrier.",
        "Jobs: gas/nutrient/waste exchange, endocrine (hCG, progesterone, estrogens, hPL), immune tolerance.",
        "Term specs: ~500 g, ~20 cm disc, 10-14 m^2 exchange surface, ~600 mL/min maternal flow.",
        "Intervillous blood (~150 mL) turns over ~4x per minute - gradients stay steep.",
        "Failure modes: previa (wrong site), abruption (early separation), insufficiency (poor exchange).",
     ],
     requirements=[
        "Tertiary chorionic villi with fetal capillaries throughout the villous tree.",
        "An intervillous space continuously perfused by maternal spiral arteries.",
        "A four-layer placental barrier intact but thin enough for exchange.",
        "Endocrine ramp-up handing progesterone off from the corpus luteum by weeks 8-9.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
        "Carlson BM. Human Embryology and Developmental Biology. 6th ed. Elsevier; 2019.",
     ],
     sig_lens=(
        "Signature lens: the placenta is a leased utility plant - designed, "
        "built, and demolished inside one contract, serving two customers "
        "with opposing interests across one membrane. The Signature systems "
        "engineer prices it by turnover: 150 mL of working fluid exchanged "
        "four times a minute across 12 square meters of folded surface, and "
        "when the lease ends the whole plant ships out as afterbirth.")),

dict(key="heart",
     name="The Heart: The First Working Organ",
     group="Compounded", ladder_rank=5, ladder_tier="compounded",
     description=(
        "The heart is the first organ to work: two endothelial tubes fuse into "
        "a single heart tube around day 20-21, and it starts beating around "
        "day 22-23, before most mothers know they are pregnant. The tube then "
        "loops - bending rightward in the D-loop - to drag the future chambers "
        "into position, and septation through weeks 4-7 divides it into four "
        "chambers with valves. Fetal circulation runs on three shunts that "
        "bypass the fluid-filled lungs: the foramen ovale (right to left "
        "atrium), the ductus arteriosus (pulmonary trunk to aorta), and the "
        "ductus venosus (umbilical vein past the liver). At birth the shunts "
        "close - the first breath drops pulmonary resistance, the cord is cut "
        "- and the circulation converts to the adult pattern in minutes. Heart "
        "rate climbs from ~100 bpm at week 5 to ~170 by weeks 9-10."),
     how_it_works=(
        "The workload arithmetic starts early. Averaging ~135 bpm across weeks "
        "5-8, the embryonic heart fires over five million beats before the "
        "fetal period even begins - the pump is load-tested from day one. "
        "Looping is topological: a straight tube cannot make four chambers in "
        "series, so the D-loop folds inflow and outflow tracts into adjacency "
        "for septation. The three shunts are pressure logic: with the lungs "
        "collapsed, blood takes the low-resistance shortcuts, and rising "
        "oxygen at birth flips every valve. The demo counts the embryonic "
        "beats and the shunt inventory."),
     key_points=[
        "First functional organ: heart tube day 20-21, beating by day 22-23.",
        "Looping (D-loop) positions the chambers; septation (weeks 4-7) builds four chambers + valves.",
        "Three fetal shunts bypass the lungs: foramen ovale, ductus arteriosus, ductus venosus.",
        "At birth the shunts close and pulmonary + systemic circuits separate within minutes.",
        "Fetal heart rate: ~100 bpm (week 5) rising to ~170 bpm (weeks 9-10).",
        ">5 million beats fired during the embryonic period alone.",
     ],
     requirements=[
        "Paired cardiogenic tubes fused into a single beating heart tube by day 21.",
        "Rightward D-looping completed before septation begins.",
        "Septation of atria, ventricles, and outflow tracts finished by week 7.",
        "Three shunts patent through gestation and closable at birth.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Schoenwolf GC, Bleyl SB, Brauer PR, Francis-West PH. Larsen's Human Embryology. 6th ed. Elsevier; 2021.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Schoenwolf GC, Bleyl SB, Brauer PR, Francis-West PH. Larsen's Human Embryology. 6th ed. Elsevier; 2021.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
     ],
     sig_lens=(
        "Signature lens: the heart is commissioned before the building has "
        "walls - pumping at day 22 to a body that is mostly blueprint. The "
        "Signature commissioning engineer notes the brilliance of the "
        "changeover: three bypasses that run for nine months, then seal "
        "themselves within minutes of the first breath, converting the "
        "plumbing from series to parallel without stopping the pump.")),

dict(key="vascular",
     name="Vascular Development: Growing the Blood Vessels",
     group="Compounded", ladder_rank=6, ladder_tier="compounded",
     description=(
        "The vasculature grows by two processes: vasculogenesis, where "
        "angioblasts assemble brand-new vessels from scratch, and "
        "angiogenesis, where new vessels sprout from existing ones. Blood "
        "islands appear in the yolk sac around days 17-18 - the first blood "
        "and the first vessels together - while inside the embryo paired "
        "dorsal aortae fuse into one. Six pairs of aortic arch arteries thread "
        "through the pharyngeal arches, then remodel ruthlessly: arches I and "
        "II mostly vanish, III becomes the carotid system, the left IV becomes "
        "the aortic arch, and VI becomes the pulmonary arteries plus the "
        "ductus arteriosus on the left. Vitelline and umbilical vessels "
        "rewire into the portal and umbilical systems. Arch remodeling errors "
        "produce the classic vascular rings and double aortic arch."),
     how_it_works=(
        "Branching is exponential plumbing: twelve generations of dichotomous "
        "branching from the dorsal aorta yield 4,096 terminal branches, and "
        "angiogenic sprouting follows VEGF gradients the way roots follow "
        "water. The arch arteries are a six-pair manifold installed whole and "
        "then selectively demolished - persistence of a demolished arch, or "
        "loss of a kept one, is read directly as the adult anomaly. The demo "
        "runs the branching census and the six-arch fate table."),
     key_points=[
        "Two build modes: vasculogenesis (new vessels from angioblasts) and angiogenesis (sprouting).",
        "First vessels: yolk-sac blood islands (days 17-18); dorsal aortae fuse inside the embryo.",
        "Six aortic arch pairs remodel: I-II regress, III->carotids, left IV->aortic arch, VI->pulmonary + ductus arteriosus.",
        "~12 branching generations from the aorta give ~4,000 terminal branches.",
        "VEGF gradients steer sprouting; remodeling errors make vascular rings.",
        "The umbilical and vitelline systems rewire into umbilical and portal circulation.",
     ],
     requirements=[
        "Yolk-sac blood islands producing the first hematopoietic and endothelial cells.",
        "Fusion of the paired dorsal aortae into a single midline vessel.",
        "All six arch pairs installed, then remodeled to the asymmetric adult pattern.",
        "VEGF-guided angiogenesis extending the tree to the tissues.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Gilbert SF, Barresi MJF. Developmental Biology. 13th ed. Oxford University Press; 2023.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Gilbert SF, Barresi MJF. Developmental Biology. 13th ed. Oxford University Press; 2023.",
        "Carlson BM. Human Embryology and Developmental Biology. 6th ed. Elsevier; 2019.",
     ],
     sig_lens=(
        "Signature lens: the vasculature is installed like temporary "
        "scaffolding that becomes permanent - six arch pairs erected whole, "
        "then selectively demolished to the final asymmetric manifold. The "
        "Signature plumber keeps the demolition schedule taped to the wall: "
        "every adult arch anomaly is just a line on that schedule that was "
        "skipped or double-executed.")),

dict(key="skeletal",
     name="Skeletal Development: Cartilage First, Bone Later",
     group="Compounded", ladder_rank=6, ladder_tier="compounded",
     description=(
        "The skeleton is built by two methods. Intramembranous ossification "
        "turns mesenchyme directly into bone - the flat bones of the skull "
        "and the clavicle. Endochondral ossification, used by the long bones, "
        "first sculpts a cartilage model, then replaces it with bone from the "
        "inside out: primary ossification centers appear in the diaphysis "
        "around weeks 8-12, secondary centers in the epiphyses mostly after "
        "birth, and the growth plate between them drives lengthening until the "
        "teens. The axial skeleton comes from somite sclerotomes (vertebrae, "
        "ribs), the limbs from lateral-plate mesoderm limb buds. A newborn has "
        "about 300 bones - many are separate pieces that fuse into the adult "
        "206. Fontanelles, the soft spots of the skull, let the head compress "
        "for birth and close over the first two years."),
     how_it_works=(
        "The fusion arithmetic: ~300 bones at birth minus 206 adult = about 94 "
        "fusions, mostly in skull, sacrum, and coccyx. In endochondral "
        "ossification, hypertrophic chondrocytes calcify their matrix and die, "
        "blood vessels invade, and osteoblasts lay bone on the cartilage "
        "scaffolding - a replacement operation, not a transformation. The "
        "femur grows from ~75 mm at birth to ~450 mm adult, a sixfold "
        "extension at the growth plates. The demo runs the fusion census and "
        "the ossification-center schedule."),
     key_points=[
        "Two methods: intramembranous (mesenchyme -> bone: skull, clavicle) and endochondral (cartilage model -> bone: long bones).",
        "Primary ossification centers: diaphysis, weeks 8-12. Secondary: epiphyses, mostly postnatal.",
        "Growth plates lengthen long bones into the teens; then they fuse and growth stops.",
        "Axial skeleton from somite sclerotomes; appendicular from limb-bud mesoderm.",
        "~300 bones at birth fuse to 206 adult - about 94 fusions.",
        "Fontanelles permit birth molding and brain growth; they close by ~age 2.",
     ],
     requirements=[
        "Mesenchyme competent for intramembranous ossification at the skull and clavicle.",
        "Cartilage models complete before endochondral replacement begins.",
        "Primary centers on schedule (weeks 8-12) with vascular invasion of hypertrophic cartilage.",
        "Growth plates preserved until adolescence, then orderly fusion.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
        "Cochard LR, ed. Netter's Atlas of Human Embryology. Icon Learning Systems; 2002.",
     ],
     sig_lens=(
        "Signature lens: the skeleton is prototyped in a soft material and "
        "then replaced in a hard one - cartilage first as the sacrificial "
        "pattern, bone as the production part. The Signature manufacturer "
        "recognizes lost-pattern casting when it sees it: build the shape "
        "in something easy, invade it, and swap the material without moving "
        "the geometry.")),

dict(key="muscle",
     name="Muscle Development: From Myoblasts to Muscle",
     group="Compounded", ladder_rank=6, ladder_tier="compounded",
     description=(
        "Skeletal muscle is built by fusion: myoblasts from the somite "
        "myotomes line up and merge their membranes, making long "
        "multinucleated myotubes that mature into muscle fibers - one fiber "
        "can hold a thousand nuclei along a centimeter. Head muscles come "
        "from unsegmented somitomeres instead, smooth muscle from splanchnic "
        "lateral-plate mesoderm wrapping the gut and vessels, and cardiac "
        "muscle from the cardiogenic splanchnic mesoderm. The myogenic "
        "regulatory factors - MyoD, Myf5, myogenin, MRF4 - switch the program "
        "on in sequence. Because muscle and its tendon and nerve arrive on "
        "different schedules, the system self-wires: fibers that never get "
        "innervated are pruned, and the survivors are the ones that found "
        "their nerve."),
     how_it_works=(
        "The fusion arithmetic sets fiber scale. A 1-cm fiber 50 micrometers "
        "in diameter holds about 20 million cubic micrometers of cytoplasm; "
        "with each nucleus governing roughly 20,000 cubic micrometers (the "
        "myonuclear domain), the fiber needs on the order of a thousand "
        "nuclei - a thousand myoblasts fused. Innervation then sculpts: "
        "polyneuronal innervation is pruned to single-motor-unit control in "
        "early development. The demo computes the myonuclear census of a "
        "model fiber."),
     key_points=[
        "Skeletal muscle: myoblasts fuse into multinucleated myotubes -> muscle fibers.",
        "Sources: somite myotomes (trunk/limbs), somitomeres (head), splanchnic mesoderm (smooth, cardiac).",
        "MyoD/Myf5/myogenin/MRF4 switch the myogenic program on in order.",
        "~1000 nuclei per centimeter of fiber at a ~20,000 um^3 myonuclear domain.",
        "Innervation prunes: fibers without nerves are lost; survivors wire to motor units.",
        "Tendons (from sclerotome/lateral plate) and nerves arrive on separate schedules and integrate.",
     ],
     requirements=[
        "Myotome myoblasts competent to exit the cell cycle and fuse.",
        "Sequential myogenic regulatory factor expression (MyoD -> myogenin -> MRF4).",
        "Motor innervation reaching fibers before the pruning window closes.",
        "Tendon primordia positioned to receive the muscle attachments.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Gilbert SF, Barresi MJF. Developmental Biology. 13th ed. Oxford University Press; 2023.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Gilbert SF, Barresi MJF. Developmental Biology. 13th ed. Oxford University Press; 2023.",
        "Schoenwolf GC, Bleyl SB, Brauer PR, Francis-West PH. Larsen's Human Embryology. 6th ed. Elsevier; 2021.",
     ],
     sig_lens=(
        "Signature lens: muscle is assembled by merging subcontractors - a "
        "thousand single-nucleus myoblasts dissolve their boundaries into "
        "one continuous fiber, pooling their control centers. The Signature "
        "integrator prices the merger by the myonuclear domain: each nucleus "
        "buys about 20,000 cubic micrometers of fiber, and the fiber keeps "
        "hiring until the territory is covered.")),

dict(key="integument",
     name="Skin Development: Building the Barrier",
     group="Compounded", ladder_rank=6, ladder_tier="compounded",
     description=(
        "Skin is two tissues laminated: the epidermis from surface ectoderm, "
        "the dermis from mesoderm (somite dermatomes for the back, lateral "
        "plate elsewhere). Early on the epidermis is a single layer plus a "
        "temporary periderm - a nonstick coating that is shed around week 21 "
        "into the amniotic fluid. Stratification runs weeks 8-16, building the "
        "layered barrier; from week 20 the vernix caseosa, a cheesy biofilm of "
        "sebum and shed cells, waterproofs the skin against months of "
        "immersion. Melanocytes migrate in from the neural crest and take up "
        "station in the basal layer; hair follicles, nails (from week 10), and "
        "glands bud downward. Lanugo, the fine fetal hair, appears and mostly "
        "sheds before birth."),
     how_it_works=(
        "Barrier construction is layering plus waterproofing. Two layers at "
        "week 8 become four-plus by week 16 as keratinocytes stratify and "
        "cornify; the periderm is jettisoned at week 21 once the true "
        "epidermis can hold; vernix from week 20 seals against amniotic "
        "maceration. Melanin production starts but stays low until sun "
        "exposure after birth - newborn color is not the final color. The "
        "demo runs the stratification and waterproofing schedule."),
     key_points=[
        "Epidermis from ectoderm; dermis from mesoderm (dermatomes + lateral plate).",
        "Periderm: temporary nonstick layer, shed ~week 21 into the amniotic fluid.",
        "Stratification weeks 8-16 builds the cornified barrier.",
        "Vernix caseosa from week 20 waterproofs the skin for the long immersion.",
        "Melanocytes arrive from the neural crest; hair, nails (week 10+), and glands bud in.",
        "Lanugo appears mid-gestation and mostly sheds before birth.",
     ],
     requirements=[
        "Surface ectoderm committed to epidermis with dermal mesoderm beneath.",
        "Periderm maintained until week 21, then fully shed.",
        "Stratification and cornification complete by week 16+.",
        "Vernix production from week 20 protecting the barrier to term.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
        "Carlson BM. Human Embryology and Developmental Biology. 6th ed. Elsevier; 2019.",
     ],
     sig_lens=(
        "Signature lens: skin is the pressure hull - laminated, waterproofed, "
        "and fitted with sensors before launch. The Signature outfitter runs "
        "it like a shipyard schedule: temporary nonstick coating while the "
        "real hull cures, then a wax seal (vernix) for the months at sea, "
        "with pigment crews and hair follicles installed as the hull goes "
        "up.")),

dict(key="respiratory",
     name="Lung Development: Branching Into Breathing",
     group="Compounded", ladder_rank=6, ladder_tier="compounded",
     description=(
        "The lungs bud from the gut: in week 4 the laryngotracheal groove "
        "pushes out of the foregut endoderm, splits into two lung buds, and "
        "branches dichotomously about 23 generations into the bronchial tree. "
        "Development runs in five stages - embryonic (weeks 4-7), "
        "pseudoglandular (5-17), canalicular (16-25), saccular (24 to birth), "
        "alveolar (36 weeks to ~8 years) - and only in the canalicular stage "
        "do the airways meet capillaries closely enough for gas exchange. "
        "Type II pneumocytes start making surfactant around week 24, the "
        "milestone that makes viability possible; before that the alveoli "
        "would collapse on first breath. Fetal lungs are fluid-filled and "
        "practice breathing movements for months; at birth the fluid clears "
        "and air takes over in minutes."),
     how_it_works=(
        "Branching is binary: 23 generations give 2^23 - over 8 million - "
        "terminal airways, of which the first 16 generations (65,536 branches) "
        "are purely conducting and the last 7 do the exchange. Surfactant "
        "lowers surface tension by an order of magnitude; without it, the "
        "Law of Laplace says small alveoli collapse into big ones. The "
        "viability threshold near week 24 is really a surfactant threshold. "
        "The demo runs the branching census and the stage calendar."),
     key_points=[
        "Lung buds sprout from foregut endoderm in week 4 and branch ~23 generations (2^23 airways).",
        "Five stages: embryonic -> pseudoglandular -> canalicular -> saccular -> alveolar (into childhood).",
        "Gas exchange becomes possible in the canalicular stage (weeks 16-25).",
        "Surfactant from type II pneumocytes (~week 24+) prevents alveolar collapse - the viability milestone.",
        "Fetal lungs are fluid-filled; breathing movements are practice, not ventilation.",
        "At birth fluid clears and air exchange starts within minutes.",
     ],
     requirements=[
        "A foregut endoderm bud competent to branch under FGF10 signaling.",
        "All 23 branching generations completed with conducting vs respiratory zoning.",
        "Capillary apposition to airways by the canalicular stage.",
        "Surfactant production sufficient for the first breath by ~week 24+.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Schoenwolf GC, Bleyl SB, Brauer PR, Francis-West PH. Larsen's Human Embryology. 6th ed. Elsevier; 2021.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Schoenwolf GC, Bleyl SB, Brauer PR, Francis-West PH. Larsen's Human Embryology. 6th ed. Elsevier; 2021.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
     ],
     sig_lens=(
        "Signature lens: the lung is a fractal air manifold - one inlet "
        "branched 23 times into 8 million outlets, with the last seven "
        "generations doing the actual business. The Signature HVAC engineer "
        "notes the commissioning sequence: ducts first, then the "
        "anti-collapse coating (surfactant), then a months-long dry run on "
        "fluid before the system ever sees air.")),
]

# ------------------------------------------------------------------ Advanced
ENTRIES += [
dict(key="digestive",
     name="Digestive System Development: The Rotating Gut",
     group="Advanced", ladder_rank=7, ladder_tier="advanced",
     description=(
        "The digestive tract is a single tube with regional ambitions, built "
        "from endoderm (the lining) wrapped in splanchnic mesoderm (the "
        "muscle and connective tissue). The foregut gives the pharynx, lower "
        "airways, esophagus, stomach, liver, pancreas, and upper duodenum; "
        "the midgut, fed by the superior mesenteric artery, gives the rest of "
        "the small intestine and the colon to the splenic flexure; the hindgut "
        "gives the rest. In week 6 the midgut herniates into the umbilical "
        "cord - growing too fast for the abdomen - rotates 270 degrees "
        "counterclockwise around the superior mesenteric artery, and returns "
        "in week 10. The liver buds from the hepatic diverticulum in week 4 "
        "and becomes the great hematopoietic organ of the fetus; the pancreas "
        "forms from dorsal and ventral buds that fuse. A vitelline-duct "
        "remnant persists as Meckel diverticulum in about 2 percent of people."),
     how_it_works=(
        "The rotation is the famous 270 degrees: 90 during herniation, 180 "
        "during return - three-quarters of a full turn that parks the cecum in "
        "the right lower quadrant and drapes the transverse colon across. "
        "Failed rotation leaves malrotation and volvulus risk; failed return "
        "leaves omphalocele. The liver's week-4 bud grows so fast it fills "
        "much of the abdomen by week 10, making blood while the marrow "
        "matures. Meckel's rule of 2s: 2% of people, 2 feet from the "
        "ileocecal valve, 2 inches long. The demo runs the rotation and the "
        "Meckel arithmetic."),
     key_points=[
        "Endoderm lines the tube; splanchnic mesoderm builds its muscle and connective tissue.",
        "Foregut / midgut / hindgut map to their vitelline artery territories.",
        "Midgut herniates (week 6), rotates 270 deg counterclockwise, returns (week 10).",
        "Liver buds week 4 and becomes the fetal blood factory; pancreas forms from two buds that fuse.",
        "Meckel diverticulum: vitelline remnant in ~2% of people (rule of 2s).",
        "Rotation failures: malrotation/volvulus; return failures: omphalocele.",
     ],
     requirements=[
        "Endoderm tube with foregut/midgut/hindgut regional identity.",
        "Midgut herniation with a full 270-degree counterclockwise rotation about the SMA.",
        "Return of the herniated loops to the abdomen by week 10-11.",
        "Hepatic and pancreatic buds outgrowing and differentiating on schedule.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
        "Dudek RW. Embryology. 7th ed. (Board Review Series). Wolters Kluwer; 2019.",
     ],
     sig_lens=(
        "Signature lens: the gut is installed like a ship's engine room - "
        "built oversize outside the hull, rotated three-quarters of a turn, "
        "and craned back in through a temporary hatch. The Signature "
        "rigger's rule: the rotation must total exactly 270 degrees and the "
        "hatch must close by week 10, because a tube parked wrong will twist "
        "and a hatch left open is an omphalocele.")),

dict(key="urinary",
     name="Urinary System Development: Three Kidneys in a Row",
     group="Advanced", ladder_rank=7, ladder_tier="advanced",
     description=(
        "The embryo builds three kidneys in sequence and keeps the last. The "
        "pronephros appears in week 4 in the neck region and vanishes, a "
        "vestige. The mesonephros runs weeks 4-8 in the thoracolumbar region "
        "as the interim kidney, and its duct is recycled: in males it becomes "
        "the genital duct system. The metanephros, the permanent kidney, "
        "starts in week 5 when the ureteric bud grows out of the mesonephric "
        "duct into the metanephric mesenchyme - an inductive handshake where "
        "each tissue tells the other to build: the bud branches into "
        "collecting ducts, the mesenchyme becomes nephrons. By birth each "
        "kidney holds about a million nephrons, two million total, and fetal "
        "urine from weeks 10-12 becomes the main source of amniotic fluid. "
        "The cloaca, meanwhile, is divided by the urorectal septum into the "
        "urogenital sinus and the anorectal canal."),
     how_it_works=(
        "The ureteric bud is a branching program: each tip induces a nephron "
        "in the surrounding mesenchyme, then bifurcates, iterating to about "
        "a million nephrons per kidney. Fetal urine output reaches roughly a "
        "liter a day at term - about 0.7 mL per minute - and that flow is what "
        "keeps amniotic fluid volume up; blocked output gives oligohydramnios "
        "and the Potter sequence. The demo runs the nephron census and the "
        "urine-flow budget."),
     key_points=[
        "Three systems in sequence: pronephros (transient) -> mesonephros (interim) -> metanephros (permanent).",
        "Metanephros: ureteric bud + metanephric mesenchyme induce each other from week 5.",
        "Bud branching iterates to ~1 million nephrons per kidney (~2 million total).",
        "Fetal urine (from weeks 10-12) becomes the main amniotic fluid source; ~1 L/day at term.",
        "The mesonephric duct is recycled into the male genital ducts.",
        "The urorectal septum splits the cloaca into urogenital sinus and anorectal canal.",
     ],
     requirements=[
        "Pronephric and mesonephric systems appearing and regressing on schedule.",
        "Ureteric bud outgrowth meeting competent metanephric mesenchyme in week 5.",
        "Iterative bud branching with nephron induction at every tip.",
        "Urorectal septation completing the cloacal division.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Schoenwolf GC, Bleyl SB, Brauer PR, Francis-West PH. Larsen's Human Embryology. 6th ed. Elsevier; 2021.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Schoenwolf GC, Bleyl SB, Brauer PR, Francis-West PH. Larsen's Human Embryology. 6th ed. Elsevier; 2021.",
        "Carlson BM. Human Embryology and Developmental Biology. 6th ed. Elsevier; 2019.",
     ],
     sig_lens=(
        "Signature lens: the urinary system is built by successive "
        "prototyping - three kidneys attempted, the first scrapped, the "
        "second kept as a parts donor for the male ducts, the third shipped. "
        "The Signature engineer admires the metanephric handshake most: two "
        "tissues that each refuse to build until the other signals, then "
        "iterate a million nephrons by a branching loop.")),

dict(key="genital",
     name="Genital Development: The Path to Male or Female",
     group="Advanced", ladder_rank=7, ladder_tier="advanced",
     description=(
        "Every embryo starts with the indifferent stage: identical gonadal "
        "ridges, two duct systems (Wolffian and Mullerian), and identical "
        "external genitalia through week 7. Then the SRY gene on the Y "
        "chromosome flips the switch: the ridge becomes a testis, Sertoli "
        "cells secrete anti-Mullerian hormone to dissolve the female ducts, "
        "and Leydig cells make testosterone to build the Wolffian ducts into "
        "epididymis, vas deferens, and seminal vesicles. Without SRY the "
        "ridge becomes an ovary, the Mullerian ducts become uterus, tubes, "
        "and upper vagina, and the Wolffian ducts regress. Externally, the "
        "genital tubercle, folds, and swellings sculpt into penis and scrotum "
        "under dihydrotestosterone, or clitoris and labia without it. The "
        "testes then descend - transabdominal then inguinoscrotal - usually "
        "arriving before birth; about 3 percent have not, most resolving in "
        "the first year."),
     how_it_works=(
        "It is a binary switch with hormonal amplifiers. SRY at week 7 -> "
        "SOX9 -> testis; no SRY -> WNT4/RSPO1 -> ovary. AMH removes the "
        "Mullerian option in males; testosterone keeps the Wolffian option; "
        "DHT sculpts the exterior. Descent is two-phase: INSL3 shortens the "
        "gubernaculum (transabdominal), androgens drive the inguinoscrotal "
        "passage. Per 1,000 male births ~30 are cryptorchid at birth and "
        "about three-quarters descend spontaneously within a year. The demo "
        "runs the switch logic and the descent statistics."),
     key_points=[
        "Indifferent stage to week 7: identical ridges, dual ducts, identical externals.",
        "SRY (Y chromosome) -> testis; no SRY -> ovary. The switch is genetic; the build-out is hormonal.",
        "Sertoli AMH dissolves Mullerian ducts; Leydig testosterone builds Wolffian ducts.",
        "DHT sculpts male externals; without it the same primordia become female.",
        "Testicular descent is two-phase (INSL3, then androgen-driven).",
        "~3% cryptorchid at birth per 1,000 males; ~75% resolve in year one.",
     ],
     requirements=[
        "An indifferent gonadal ridge with both duct systems present to week 7.",
        "SRY expression (or its absence) read correctly by the ridge.",
        "AMH sufficient to regress Mullerians; testosterone/DHT sufficient to build male structures.",
        "Two-phase descent completed, testes in the scrotum by birth in ~97%.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
        "Gilbert SF, Barresi MJF. Developmental Biology. 13th ed. Oxford University Press; 2023.",
     ],
     sig_lens=(
        "Signature lens: sex development is one chassis with two option "
        "packages and a single-bit select line - SRY present or absent at "
        "week 7. The Signature product manager notes the elegance: the "
        "unselected duct system is not left installed but demolished "
        "(AMH), the exterior is sculpted by a stronger hormone (DHT), and "
        "the finished testes are shipped to an external housing for thermal "
        "reasons.")),

dict(key="nervous",
     name="Nervous System Development: Wiring the Brain",
     group="Advanced", ladder_rank=7, ladder_tier="advanced",
     description=(
        "From the neural tube, the brain builds itself in three acts: the "
        "cranial tube swells into forebrain, midbrain, and hindbrain "
        "vesicles, which subdivide into telencephalon, diencephalon, "
        "mesencephalon, metencephalon, and myelencephalon; neurons are born "
        "along the ventricles and migrate outward along radial glia to their "
        "cortical layers; then axons wire up, synapses overproduce, and "
        "experience prunes. Cortical neurogenesis peaks in weeks 8-16 at an "
        "astonishing quarter-million neurons per minute. The cortex ends up "
        "with about 16 billion neurons of the brain's 86 billion, matched by "
        "roughly as many glia. Myelination begins in the third trimester and "
        "runs for years - the prefrontal cortex is still myelinating into the "
        "twenties. The neural crest's diaspora (from the neurulation record) "
        "supplies the peripheral nervous system throughout."),
     how_it_works=(
        "The production arithmetic is the marvel: 16 billion cortical neurons "
        "at 250,000 per minute needs about 64,000 minutes - roughly 44 days "
        "of peak output, fitting inside the weeks 8-16 window. Migration is "
        "inside-out: later-born neurons climb past earlier ones to form the "
        "six cortical layers. Then comes the great pruning: synaptic density "
        "peaks in early childhood at about twice adult levels, and use keeps "
        "what it needs. The demo runs the neurogenesis production schedule."),
     key_points=[
        "Three primary vesicles -> five secondary vesicles -> the adult brain plan.",
        "Cortical neurogenesis peaks weeks 8-16 at ~250,000 neurons/minute.",
        "~16B cortical neurons of ~86B total; glia roughly match neurons one for one.",
        "Migration is inside-out along radial glia, forming six cortical layers.",
        "Synapses overproduce then prune; myelination runs from the third trimester into adulthood.",
        "The neural crest supplies the peripheral nervous system in parallel.",
     ],
     requirements=[
        "Neural tube regionalized into the five secondary vesicles.",
        "Ventricular-zone proliferation at peak rate through weeks 8-16.",
        "Radial-glia-guided inside-out migration completing the six layers.",
        "Myelination and pruning programs running from the third trimester onward.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Schoenwolf GC, Bleyl SB, Brauer PR, Francis-West PH. Larsen's Human Embryology. 6th ed. Elsevier; 2021.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Schoenwolf GC, Bleyl SB, Brauer PR, Francis-West PH. Larsen's Human Embryology. 6th ed. Elsevier; 2021.",
        "Carlson BM. Human Embryology and Developmental Biology. 6th ed. Elsevier; 2019.",
     ],
     sig_lens=(
        "Signature lens: the brain is manufactured at a quarter-million "
        "units per minute, installed inside-out along temporary scaffolding "
        "(radial glia), then wired by overproduction and pruned by use. The "
        "Signature production chief reads the schedule - 44 days of peak "
        "output inside a nine-week window - and the quality doctrine: build "
        "twice what you need, then let the workload decide what survives.")),

dict(key="eye_ear",
     name="Eye and Ear Development: The Senses Take Shape",
     group="Advanced", ladder_rank=8, ladder_tier="advanced",
     description=(
        "The eye builds itself by invitation: the optic vesicle grows out "
        "from the forebrain around day 22, touches the surface ectoderm, and "
        "induces the lens placode - which thickens, pits, and pinches off as "
        "the lens vesicle by day 33 - while the vesicle itself folds into the "
        "double-walled optic cup, its inner layer becoming the neural retina "
        "and the outer the pigment epithelium. The choroid fissure must close "
        "by week 7 or coloboma results. The ear builds in three parts: the "
        "otic placode invaginates to the otic vesicle in week 4 and sculpts "
        "the membranous labyrinth (cochlea with its two-and-a-half turns, "
        "vestibule, semicircular canals); the middle-ear ossicles - malleus, "
        "incus from first-arch cartilage, stapes from second-arch - assemble "
        "in the tubotympanic recess; the external ear rises from six hillocks "
        "around the first cleft. The retina's ten layers wire before birth; "
        "hearing is functional in the third trimester."),
     how_it_works=(
        "Induction is the mechanism: each part summons the next. Optic vesicle "
        "-> lens placode (day 27) -> lens vesicle (day 33): six days from "
        "invitation to a detached lens. The optic cup's inner wall "
        "proliferates into the full neural retina while the outer wall "
        "pigments; the fissure closure at week 7 seals the cup. In the ear, "
        "the otic vesicle partitions into dorsal (vestibular) and ventral "
        "(cochlear) divisions, the cochlear duct coiling 2.5 turns - 900 "
        "degrees of frequency map. The demo runs the induction timeline and "
        "the cochlear coil geometry."),
     key_points=[
        "Eye: optic vesicle (day 22) induces lens placode (day 27) -> lens vesicle (day 33); vesicle folds into the optic cup.",
        "Retina from the cup's inner wall (neural), pigment epithelium from the outer; choroid fissure closes week 7.",
        "Inner ear: otic placode -> otic vesicle (week 4) -> membranous labyrinth.",
        "Cochlea coils 2.5 turns (900 degrees); ossicles come from arch 1 (malleus, incus) and arch 2 (stapes) cartilage.",
        "External ear from six hillocks; the retina wires its ten layers before birth.",
        "Induction cascades build both organs: each structure summons the next.",
     ],
     requirements=[
        "Optic vesicle contact inducing the lens placode on schedule.",
        "Optic cup formation with choroid fissure closure by week 7.",
        "Otic vesicle partitioning into vestibular and cochlear divisions.",
        "Arch-cartilage ossicles assembled in the middle-ear space; hillocks fused into the auricle.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
        "Cochard LR, ed. Netter's Atlas of Human Embryology. Icon Learning Systems; 2002.",
     ],
     sig_lens=(
        "Signature lens: the senses are built by invitation chains - no part "
        "forms until its predecessor taps it on the shoulder. The Signature "
        "systems integrator maps the dependency graph: vesicle summons "
        "placode, placode becomes lens, cup becomes retina, and a single "
        "missed handshake (fissure open past week 7) leaves a permanent gap "
        "in the finished sensor.")),

dict(key="endocrine",
     name="Endocrine Development: Glands of Growth and Control",
     group="Advanced", ladder_rank=8, ladder_tier="advanced",
     description=(
        "The endocrine glands assemble from scattered origins and wire into "
        "the control system before birth. The pituitary is a two-part merger: "
        "Rathke's pouch grows up from oral ectoderm in week 4 while the "
        "infundibulum grows down from neuroectoderm, meeting to form anterior "
        "and posterior lobes. The thyroid descends from the foramen cecum of "
        "the tongue down the thyroglossal duct, and begins trapping iodine "
        "and making hormone around weeks 10-12 - maternal thyroid hormone "
        "covers the gap before that. Parathyroids and thymus come from the "
        "third and fourth pharyngeal pouches; the adrenals pair mesodermal "
        "cortex with neural-crest medulla, and the fetal cortex is enormous "
        "relative to body size, making DHEA for placental estrogen. Pancreatic "
        "islets differentiate from week 12, and the pineal buds from the "
        "diencephalon roof."),
     how_it_works=(
        "The scale story is the fetal adrenal: at term the combined adrenals "
        "weigh roughly as much as an adult's (~8 g) on a body twenty times "
        "smaller - a twentyfold relative investment in the fetal zone that "
        "feeds placental estrogen synthesis and then involutes after birth. "
        "The pituitary merger must align portal vessels between hypothalamus "
        "and anterior lobe, or control never connects. Thyroid descent leaves "
        "the thyroglossal duct; remnants become cysts. The demo runs the "
        "adrenal scale ratio and the gland-origin inventory."),
     key_points=[
        "Pituitary: Rathke's pouch (oral ectoderm, week 4) + infundibulum (neuroectoderm) merge into two lobes.",
        "Thyroid descends from the tongue's foramen cecum; hormone synthesis starts weeks 10-12.",
        "Parathyroids/thymus from pharyngeal pouches 3-4; adrenals = mesoderm cortex + neural crest medulla.",
        "Fetal adrenal cortex is ~20x adult relative size, feeding placental estrogen; it involutes after birth.",
        "Pancreatic islets from week 12; pineal from the diencephalon roof.",
        "Maternal thyroid hormone bridges the gap until the fetal gland works.",
     ],
     requirements=[
        "Rathke's pouch meeting the infundibulum with portal vessels aligned.",
        "Thyroid descent complete with the thyroglossal duct obliterated.",
        "Pouch derivatives (parathyroids, thymus) migrated to final positions.",
        "Fetal adrenal zone built large, then involuted on schedule after birth.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Schoenwolf GC, Bleyl SB, Brauer PR, Francis-West PH. Larsen's Human Embryology. 6th ed. Elsevier; 2021.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Schoenwolf GC, Bleyl SB, Brauer PR, Francis-West PH. Larsen's Human Embryology. 6th ed. Elsevier; 2021.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
     ],
     sig_lens=(
        "Signature lens: the endocrine system is the control plane, "
        "assembled from parts built in different shops - oral ectoderm, "
        "neuroectoderm, pharyngeal pouches, mesoderm, neural crest - and "
        "bolted together before launch. The Signature controls engineer "
        "flags the fetal adrenal as the tell: a twentyfold oversized "
        "auxiliary power unit installed for one mission (placental estrogen) "
        "and decommissioned the week after delivery.")),
]

ENTRIES += [
dict(key="dev_genetics",
     name="Developmental Genetics: Hox Genes and the Body Plan Code",
     group="Advanced", ladder_rank=8, ladder_tier="advanced",
     description=(
        "Developmental genetics is the code beneath the construction: the "
        "genes that tell each cell where it is and what to become. The stars "
        "are the Hox genes - 39 in humans, arranged in 4 clusters (HOXA on "
        "chromosome 7, HOXB on 17, HOXC on 12, HOXD on 2) - with a stunning "
        "property called colinearity: the order of genes on the chromosome "
        "matches the order of their expression along the head-to-tail axis. "
        "Each Hox gene carries a 180-base-pair homeobox encoding a 60-amino-"
        "acid DNA-binding domain. Around them work the signaling families: "
        "Sonic hedgehog (ventral patterning, limb polarity), BMPs (dorsal), "
        "Wnts and FGFs (growth and axes), retinoic acid (posteriorizing "
        "gradient) - morphogens whose concentrations are read as coordinates. "
        "Mutate a Hox gene and body parts transform: Antennapedia in the fly "
        "grows legs where antennae belong; human HOX mutations misplace "
        "vertebrae and limbs."),
     how_it_works=(
        "The cluster accounting is exact: 11 + 10 + 9 + 9 = 39 genes across "
        "the four clusters, grouped into 13 paralog families. Colinearity "
        "runs in space and time: 3-prime genes switch on first and most "
        "cranially, 5-prime genes later and more caudally. The homeobox math "
        "is 180 / 3 = 60 amino acids of DNA-binding domain - the most "
        "conserved 60 in the animal kingdom. Morphogen reading is threshold "
        "logic on the gradients from the body-axes record. The demo verifies "
        "the cluster census and the homeobox arithmetic."),
     key_points=[
        "39 Hox genes in 4 clusters (chr 7, 17, 12, 2): 11 + 10 + 9 + 9.",
        "Colinearity: chromosomal order = head-to-tail expression order, in space and time.",
        "Homeobox = 180 bp = 60 amino acids of DNA-binding domain.",
        "Morphogens (Shh, BMP, Wnt, FGF, retinoic acid) are read as positional coordinates.",
        "Hox mutations cause homeotic transformations - body parts built in the wrong place.",
        "13 paralog groups let the four clusters subdivide the axis redundantly and robustly.",
     ],
     requirements=[
        "All four Hox clusters intact with 3-prime to 5-prime order preserved.",
        "Morphogen sources positioned: Shh ventral, BMP dorsal, retinoic acid posterior.",
        "Threshold-reading machinery in every responding cell.",
        "Temporal colinearity: 3-prime genes on first, 5-prime later.",
     ],
     standards=[
        "Gilbert SF, Barresi MJF. Developmental Biology. 13th ed. Oxford University Press; 2023.",
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
     ],
     citations=[
        "Gilbert SF, Barresi MJF. Developmental Biology. 13th ed. Oxford University Press; 2023.",
        "Mallo M, Wellik DM, Deschamps J. Hox genes and regional patterning of the vertebrate body plan. Dev Biol. 2010;344(1):7-15.",
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
     ],
     sig_lens=(
        "Signature lens: the Hox clusters are the addressing ROM of the "
        "body - 39 entries in four banks, wired so that physical order on "
        "the chip equals spatial order in the product. The Signature "
        "firmware engineer calls colinearity the most elegant addressing "
        "scheme in biology: no lookup tables, no pointers, just position as "
        "address, burned into the chromosome.")),

dict(key="teratology",
     name="Teratology: When Development Goes Wrong",
     group="Advanced", ladder_rank=8, ladder_tier="advanced",
     description=(
        "Teratology is the study of birth defects - what breaks development, "
        "when, and how. About 3 percent of newborns have a major congenital "
        "anomaly, and the great organizer of risk is timing: the embryonic "
        "period (weeks 3-8), when organs are founded, is the critical window "
        "for structural defects, while the fetal period risks growth and "
        "functional damage. Wilson's six principles govern the field: "
        "susceptibility depends on genotype, developmental stage, dose, and "
        "mechanism; manifestations are death, malformation, growth "
        "retardation, or functional deficit. The classic teratogens each have "
        "a signature window: thalidomide days 20-36 (limb reduction), "
        "isotretinoin (craniofacial, cardiac, CNS), alcohol (fetal alcohol "
        "spectrum), rubella (cataracts, deafness, cardiac), valproate (neural "
        "tube), warfarin (nasal and limb hypoplasia), maternal diabetes and "
        "uncontrolled phenylketonuria. Most anomalies are multifactorial - "
        "genes loading the gun, environment pulling the trigger."),
     how_it_works=(
        "Risk is window arithmetic. Thalidomide's sensitive window is days "
        "20-36 - just 16 days - and exposure inside it carries on the order "
        "of 20 percent malformation risk against a 3 percent background: a "
        "relative risk near seven. Outside the window the same dose does far "
        "less, because the vulnerable structures are already built or not yet "
        "started. Dose-response, genotype susceptibility, and placental "
        "transfer complete the equation. The demo runs the window and "
        "relative-risk numbers that make timing the master variable."),
     key_points=[
        "~3% of newborns have a major congenital anomaly; most are multifactorial.",
        "Critical window for structural defects: embryonic weeks 3-8; fetal period: growth/functional risk.",
        "Wilson's principles: genotype, stage, dose, and mechanism determine outcome.",
        "Thalidomide window days 20-36: ~20% malformation risk vs 3% background (RR ~7).",
        "Classic teratogens: isotretinoin, alcohol, rubella, valproate, warfarin, maternal diabetes.",
        "Same dose, different week, different outcome - timing is the master variable.",
     ],
     requirements=[
        "Exposure timed against the organogenesis calendar (weeks 3-8 for structural defects).",
        "Dose above the threshold with placental transfer to the embryo.",
        "A susceptible genotype - teratogens exploit genetic vulnerability.",
        "Mechanism matched to the developmental process underway that week.",
     ],
     standards=[
        "Brent RL. Environmental causes of human congenital malformations. Pediatrics. 2004;113(4 Suppl):957-968.",
        "Wilson JG. Environment and Birth Defects. Academic Press; 1973.",
     ],
     citations=[
        "Brent RL. Environmental causes of human congenital malformations: the pediatrician's role in dealing with these complex clinical problems caused by a multiplicity of environmental and genetic factors. Pediatrics. 2004;113(4 Suppl):957-968.",
        "Wilson JG. Environment and Birth Defects. New York: Academic Press; 1973.",
        "Shepard TH, Lemire RJ. Catalog of Teratogenic Agents. 13th ed. Johns Hopkins University Press; 2013.",
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
     ],
     sig_lens=(
        "Signature lens: teratology is failure analysis on the build "
        "schedule - every defect is a timestamped incident report pointing at "
        "the exact week the process was disturbed. The Signature quality "
        "engineer files each case under Wilson's principles: when, how much, "
        "by what mechanism, on which genotype. The thalidomide window is the "
        "case study that rewrote the industry's safety doctrine.")),

dict(key="twins",
     name="Twinning: One Embryo Becomes Two",
     group="Advanced", ladder_rank=9, ladder_tier="advanced",
     description=(
        "Twinning comes in two kinds with different biology. Dizygotic twins "
        "- fraternal - are two separate fertilizations, genetically ordinary "
        "siblings sharing a womb; their rate varies with maternal age, family "
        "history, and assisted reproduction. Monozygotic twins - identical - "
        "are one zygote splitting into two embryos, at a steady ~1 in 250 "
        "births worldwide regardless of age or race. When the split happens "
        "determines the membranes: days 0-3 gives dichorionic-diamniotic "
        "(separate everything, ~25-30%), days 4-8 gives monochorionic-"
        "diamniotic (shared placenta, ~70-75%), days 9-12 gives "
        "monochorionic-monoamniotic (shared sac, 1-2%), and day 13 or later "
        "gives incomplete separation - conjoined twins. Shared placentas risk "
        "twin-to-twin transfusion syndrome, where unbalanced blood sharing "
        "starves one twin and overloads the other."),
     how_it_works=(
        "The membrane arithmetic follows the split date because membranes "
        "form on schedule: chorion by ~day 3-4, amnion by ~day 8-9. Split "
        "before a membrane forms and each twin makes its own; split after and "
        "they share it. Per 1,000 monozygotic pregnancies the split-table "
        "predicts roughly 275 DCDA, 700 MCDA, 20 MCMA, and a handful "
        "conjoined. The demo runs the timing table and the chorionicity "
        "census."),
     key_points=[
        "Dizygotic: two fertilizations (fraternal); rate varies with age, heredity, ART.",
        "Monozygotic: one zygote splits (identical); steady ~1/250 births.",
        "Split timing sets membranes: 0-3d DCDA, 4-8d MCDA, 9-12d MCMA, 13+d conjoined.",
        "Membranes form on schedule (chorion ~day 3-4, amnion ~day 8-9) - split before = separate, after = shared.",
        "Shared placentas risk twin-to-twin transfusion syndrome.",
        "Per 1000 MZ pregnancies: ~275 DCDA / ~700 MCDA / ~20 MCMA / few conjoined.",
     ],
     requirements=[
        "For DZ: two ovulations fertilized independently in one cycle.",
        "For MZ: a complete split of the inner cell mass / embryonic disc before day 13.",
        "Membrane formation proceeding on schedule to fix the chorionicity.",
        "Placental sharing balanced enough to avoid transfusion syndrome.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Hall JG. Twinning. Lancet. 2003;362(9385):735-743.",
     ],
     citations=[
        "Hall JG. Twinning. Lancet. 2003;362(9385):735-743.",
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
     ],
     sig_lens=(
        "Signature lens: twinning is an unscheduled fork of the build - one "
        "work order duplicated mid-process, with the infrastructure sharing "
        "determined by how far the site was when the fork happened. The "
        "Signature project manager reads the membrane table as a sharing "
        "agreement: fork early and each twin gets its own utilities; fork "
        "late and they share the plant, with all the load-balancing risk "
        "that implies.")) ,

dict(key="fetal_timeline",
     name="The Fetal Period: Growth, Week by Week",
     group="Advanced", ladder_rank=9, ladder_tier="advanced",
     description=(
        "The fetal period - week 9 to birth - is when the founded organ "
        "systems grow, mature, and rehearse for the outside. The numbers tell "
        "the story: crown-rump length ~2.3 cm at week 9, ~5.4 cm at week 12, "
        "~16 cm and 300 g at week 20, ~25 cm and 1,000 g at week 28, ~32 cm "
        "and 2,500 g at week 36, ~36 cm CRL (51 cm total length) and ~3,400 g "
        "at term. Milestones punctuate the growth: eyelids open ~week 26, "
        "surfactant adequate ~week 24-26 (the viability threshold), rapid "
        "brain growth and fat deposition in the third trimester, testes "
        "descending, lanugo shedding. Weight gain peaks late: roughly 29 "
        "grams per day across weeks 28-40. The fetus practices breathing, "
        "swallowing, and sleep-wake cycles for months before they count."),
     how_it_works=(
        "Growth is exponential early and linear late. From 300 g at week 20 "
        "to 3,400 g at term is more than an elevenfold gain; the last twelve "
        "weeks add 2,400 g at about 28.6 g per day - nearly an ounce a day of "
        "mostly fat and brain. Length follows CRL until week 20, then "
        "standing length takes over. Viability near week 24 is a systems "
        "threshold: lungs with surfactant, a brainstem that can drive "
        "breathing, and skin that can hold water. The demo runs the growth "
        "curve and the daily-gain budget."),
     key_points=[
        "Fetal period: weeks 9-38 - growth, maturation, and rehearsal of all systems.",
        "Landmarks: 300 g (wk 20), 1,000 g (wk 28), 2,500 g (wk 36), ~3,400 g at term.",
        "Viability threshold ~week 24: surfactant, brainstem drive, skin barrier.",
        "Late weight gain ~29 g/day (weeks 28-40) - mostly fat and brain.",
        "Eyelids open ~week 26; testes descend; lanugo sheds; sleep-wake cycles appear.",
        "Breathing and swallowing movements are months of practice before birth.",
     ],
     requirements=[
        "Placental exchange capacity scaling with fetal mass through term.",
        "Surfactant sufficiency by weeks 24-26 for the viability threshold.",
        "Third-trimester fat deposition and brain growth spurt on schedule.",
        "Rehearsal behaviors (breathing, swallowing, sleep-wake) established before birth.",
     ],
     standards=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
     ],
     citations=[
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
        "Moore KL, Persaud TVN, Torchia MG. The Developing Human: Clinically Oriented Embryology. 11th ed. Elsevier; 2020.",
        "O'Rahilly R, Muller F. Human Embryology & Teratology. 3rd ed. Wiley-Liss; 2001.",
     ],
     sig_lens=(
        "Signature lens: the fetal period is production ramp after the "
        "prototype is proven - elevenfold mass gain, systems brought online "
        "one by one, and months of dry runs before launch. The Signature "
        "program manager tracks two curves: the weight budget (28.6 grams a "
        "day at peak) and the readiness milestones, because the launch "
        "window - viability at week 24, term at 40 - is set by the slowest "
        "system, the lungs.")),

dict(key="art",
     name="Assisted Reproduction: Science at Conception",
     group="Advanced", ladder_rank=10, ladder_tier="advanced",
     description=(
        "Assisted reproductive technology moves the first week of embryology "
        "into the laboratory. The standard in-vitro fertilization sequence: "
        "ovarian stimulation to mature a cohort of follicles, ultrasound-"
        "guided egg retrieval, fertilization in the dish (or by intracytoplasmic "
        "sperm injection, ICSI, for male factor), culture to the blastocyst "
        "stage at day 5, grading, and transfer of one (usually) embryo to the "
        "uterus - with the rest cryopreserved. Since Louise Brown's birth in "
        "1978 the field has scaled enormously; CDC national reports track "
        "hundreds of thousands of cycles a year in the US, with live-birth "
        "rates per cycle falling steeply as maternal age rises - the oocyte "
        "attrition from the oogenesis record, priced in the clinic. "
        "Preimplantation genetic testing can screen blastocyst biopsies; "
        "single-embryo transfer has cut the multiple-birth epidemic the field once caused."),
     how_it_works=(
        "The laboratory pipeline is attrition arithmetic the embryologist "
        "runs daily. A typical retrieval yields ~12 oocytes; ~70 percent "
        "fertilize normally (~8-9); ~40-50 percent of those reach blastocyst "
        "(~4); one is transferred. Each step's fraction is the clinic's "
        "quality metric, and maternal age degrades every step - the decades-"
        "paused oocytes from the oogenesis record do not pause their aging. "
        "Cryopreservation (vitrification) banks the surplus at >90 percent "
        "survival. The demo runs the pipeline fractions for a model cohort."),
     key_points=[
        "IVF sequence: stimulation -> retrieval -> fertilization (or ICSI) -> day-5 blastocyst culture -> transfer.",
        "Pipeline: ~12 oocytes -> ~70% fertilize -> ~40-50% blastulate -> usually 1 transferred.",
        "First IVF birth 1978 (Louise Brown); ICSI added 1992 for male-factor infertility.",
        "Live-birth rates per cycle fall steeply with maternal age (CDC national reports).",
        "Vitrification banks surplus embryos at >90% survival; PGT can screen blastocyst biopsies.",
        "Single-embryo transfer ended the era of routine IVF triplets.",
     ],
     requirements=[
        "Controlled ovarian stimulation producing a mature multi-follicle cohort.",
        "Laboratory fertilization with normal pronuclear development.",
        "Culture to day-5 blastocyst with grading and selection.",
        "A receptive uterus and single-embryo transfer policy.",
     ],
     standards=[
        "Centers for Disease Control and Prevention. 2021 Assisted Reproductive Technology Fertility Clinic and National Summary Report. US DHHS; 2023.",
        "Steptoe PC, Edwards RG. Birth after the reimplantation of a human embryo. Lancet. 1978;2(8085):366.",
     ],
     citations=[
        "Steptoe PC, Edwards RG. Birth after the reimplantation of a human embryo. Lancet. 1978;2(8085):366.",
        "Centers for Disease Control and Prevention. 2021 Assisted Reproductive Technology Fertility Clinic and National Summary Report. Atlanta: US Department of Health and Human Services; 2023.",
        "Sadler TW. Langman's Medical Embryology. 15th ed. Wolters Kluwer; 2024.",
     ],
     sig_lens=(
        "Signature lens: ART is the first week of the build moved off-site - "
        "the clean room replaces the uterine tube, and every step is "
        "instrumented, graded, and banked. The Signature manufacturing "
        "engineer recognizes the discipline instantly: controlled inputs, "
        "measured yields at each station, surplus inventoried in "
        "cryostorage, and a strict one-unit-per-shipment policy to end the "
        "era of accidental triple batches.")),
]
