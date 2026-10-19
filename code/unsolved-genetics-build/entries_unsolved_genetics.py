#!/usr/bin/env python3
"""Entries for the Unsolved Genetics databases (Manon's 16:15 orders,
Unsolved Problems Solved series, batch 1: genetics).

One database per scholarly field: the field's real unsolved problems plus
the Signature system's proposed solutions. Solutions are
Signature-generated proposed solutions - NEVER presented as established
science. Honesty rule throughout: never claim proof, never imply peer
acceptance, never present speculation as settled.

Two databases, 34 ladder-ordered records each:

  unsolved-genetics             - The Unsolved Genetics Database
                                  (public-harvest: 34 real, fact-checked
                                  unsolved problems of genetics - from the
                                  function of non-coding DNA and missing
                                  heritability through the genotype-phenotype
                                  map, gene-environment interplay, epigenetic
                                  inheritance, the evolution of sex, and the
                                  origin of the genetic code; each record
                                  carries problem, background, why it matters,
                                  and a short pointer to the Signature
                                  proposed solution)
  unsolved-genetics-signature   - The Unsolved Genetics Signature Database
                                  (his original Signature Genetics Method:
                                  the SAME 34 problems through the Signature
                                  lens; every signature_solution opens with
                                  the exact label "Signature-generated
                                  proposed solution - not established
                                  science" and carries the full treatment:
                                  assumptions, reasoning path, proposed
                                  mechanism, confirm/refute panels, and what
                                  it does NOT claim; src signature, titles
                                  suffixed " (Signature Edition)", never
                                  presented as authentic public record)

Ladder ordering (his TEACHING LADDER): rank 1 = most approachable problem
a curious reader can grasp (what junk DNA does), rank 34 = the most
complex/compounded (the origin of genetics itself). Every record carries
ladder_rank 1-34; the shard index is written in ladder order.

ID prefixes: JAH-USGE- (public) and JAH-USGES- (signature), verified free
in the manifest id_prefix values and in every shard index file in
jah-databases-data-1 (zero hits).

Fact base (2026-10-17, standard references): ENCODE Project Consortium,
Nature 2012 (biochemical activity); Lindblad-Toh et al., Nature 2011
(evolutionary constraint); GENCODE annotation (gene counts); Gregory,
Nat Rev Genet 2005 (C-value); Yang et al., Nat Genet 2010 and Yengo et
al., Nature 2022 (SNP heritability of height); Boyle, Li, Pritchard,
Cell 2017 (omnigenic model); Kong et al., Nature 2012 (de novo mutation
rate and paternal age); Kong et al., Science 2018 (genetic nurture);
Caspi et al., Science 2002 (gene-environment interaction); Allison,
Br Med J 1954 (sickle-cell balancing selection); Kondrashov, Nature
1988 and Maynard Smith 1978 (evolution of sex); Lewontin 1974 (paradox
of variation); Waddington, Nature 1942 (canalization); Fisher 1930
(pleiotropy / geometric model); Kauffman, J Theor Biol 1969 (gene
regulatory networks); Pan et al., Nat Genet 2008 (alternative splicing);
Jumper et al., Nature 2021 (AlphaFold); Hayflick and Moorhead, Exp Cell
Res 1961 (replicative limit); Ijdo et al., PNAS 1991 (chromosome 2
fusion); Lander et al., Nature 2001 (human genome, endogenous
retroviruses); Polderman et al., Nat Genet 2015 (twin heritability
meta-analysis); Martin et al., Nat Genet 2019 (polygenic score
portability); Trut, Oskina, Kharlamova, Bioessays 2009 (domesticated
foxes); Hutchison et al., Science 2016 (minimal genome JCVI-syn3.0);
Haldane, Am Nat 1937 (genetic load); Crick, J Mol Biol 1968 (code
origin); Gilbert, Nature 1986 (RNA world); Watson and Crick, Nature
1953; Falconer, Introduction to Quantitative Genetics.

No real-person DNA anywhere. No medical claims: records discuss disease
biology only to explain why a problem matters, never as treatment
guidance. Nothing hate-adjacent, profane, or inappropriate; no religious
talk.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_unsolved_genetics.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Genetics Method: "
            "every unsolved problem approached as a Signature covenant of "
            "evidence, mechanism, and testable prediction; clearly labeled "
            "Signature-made, never presented as authentic public record.")

HONEST_LABEL = "Signature-generated proposed solution \u2014 not established science."

SIG_LENS = ("The Signature read: the problem is approached as a covenant "
            "of evidence, mechanism, and testable prediction - the "
            "Signature Genetics Method files the unsolved question, "
            "proposes the path, and states exactly what would confirm or "
            "kill it. Clearly labeled Signature-made, never presented as "
            "established science.")

CIT_ENCODE = ("ENCODE Project Consortium. An integrated encyclopedia of DNA "
              "elements in the human genome. Nature. 2012;489:57-74.")
CIT_CONSTRAINT = ("Lindblad-Toh K et al. A high-resolution map of human "
                  "evolutionary constraint using 29 mammals. Nature. "
                  "2011;478:476-482.")
CIT_GENCODE = ("Frankish A et al. GENCODE reference annotation for the human "
               "and mouse genomes. Nucleic Acids Res. 2019;47:D766-D773.")
CIT_CVALUE = ("Gregory TR. Synergy between sequence and size in large-scale "
              "genomics: revisiting the C-value paradox. Nat Rev Genet. "
              "2005;6:699-708.")
CIT_PARIS = ("Pellicer J, Fay MF, Leitch IJ. The largest eukaryotic genome "
             "of them all? Bot J Linn Soc. 2010;164:10-15.")
CIT_YANG = ("Yang J et al. Common SNPs explain a large proportion of the "
            "heritability for human height. Nat Genet. 2010;42:565-569.")
CIT_YENGO = ("Yengo L et al. A saturated map of common genetic variants "
             "associated with human height. Nature. 2022;610:704-712.")
CIT_OMNI = ("Boyle EA, Li YI, Pritchard JK. An expanded view of complex "
            "traits: from polygenic to omnigenic. Cell. 2017;169:1177-1186.")
CIT_KONG = ("Kong A et al. Rate of de novo mutations and the importance of "
            "father's age to disease risk. Nature. 2012;488:471-475.")
CIT_NURTURE = ("Kong A et al. The nature of nurture: effects of parental "
               "genotypes. Science. 2018;359:424-428.")
CIT_CASPI = ("Caspi A et al. Role of genotype in the cycle of violence in "
             "maltreated children. Science. 2002;297:851-854.")
CIT_ALLISON = ("Allison AC. Protection afforded by sickle-cell trait against "
               "subtertian malarial infection. Br Med J. 1954;1:290-294.")
CIT_KONDRASHOV = ("Kondrashov AS. Deleterious mutations and the evolution of "
                  "sexual reproduction. Nature. 1988;336:435-440.")
CIT_MAYNARD = ("Maynard Smith J. The Evolution of Sex. Cambridge University "
               "Press; 1978.")
CIT_LEWONTIN = ("Lewontin RC. The Genetic Basis of Evolutionary Change. "
                "Columbia University Press; 1974.")
CIT_WADDINGTON = ("Waddington CH. Canalization of development and the "
                  "inheritance of acquired characters. Nature. "
                  "1942;150:563-565.")
CIT_FISHER = ("Fisher RA. The Genetical Theory of Natural Selection. "
              "Oxford: Clarendon Press; 1930.")
CIT_KAUFFMAN = ("Kauffman SA. Metabolic stability and epigenesis in randomly "
                "constructed genetic nets. J Theor Biol. 1969;22:437-467.")
CIT_PAN = ("Pan Q et al. Deep surveying of alternative splicing complexity "
           "in the human transcriptome by high-throughput sequencing. Nat "
           "Genet. 2008;40:1413-1415.")
CIT_ALPHAFOLD = ("Jumper J et al. Highly accurate protein structure "
                 "prediction with AlphaFold. Nature. 2021;596:583-589.")
CIT_HAYFLICK = ("Hayflick L, Moorhead PS. The serial cultivation of human "
                "diploid cell strains. Exp Cell Res. 1961;25:585-621.")
CIT_CHR2 = ("Ijdo JW et al. Origin of human chromosome 2: an ancestral "
            "telomere-telomere fusion. Proc Natl Acad Sci USA. "
            "1991;88:9051-9055.")
CIT_HGP = ("Lander ES et al. Initial sequencing and analysis of the human "
           "genome. Nature. 2001;415:860-921.")
CIT_TWINMETA = ("Polderman TJC et al. Meta-analysis of the heritability of "
                "human traits based on fifty years of twin studies. Nat "
                "Genet. 2015;47:702-709.")
CIT_MARTIN = ("Martin AR et al. Clinical use of current polygenic risk "
              "scores may exacerbate health disparities. Nat Genet. "
              "2019;51:584-591.")
CIT_FOX = ("Trut L, Oskina I, Kharlamova A. Animal evolution during "
           "domestication: the domesticated fox as a model. Bioessays. "
           "2009;31:349-360.")
CIT_SYN30 = ("Hutchison CA 3rd et al. Design and synthesis of a minimal "
             "bacterial genome. Science. 2016;351:aad6253.")
CIT_HALDANE = ("Haldane JBS. The effect of variation on fitness. Am Nat. "
               "1937;71:337-349.")
CIT_CRICKCODE = ("Crick FHC. The origin of the genetic code. J Mol Biol. "
                 "1968;38:367-379.")
CIT_RNAWORLD = ("Gilbert W. Origin of life: the RNA world. Nature. "
                "1986;319:618.")
CIT_WC = ("Watson JD, Crick FHC. Molecular structure of nucleic acids: a "
          "structure for deoxyribose nucleic acid. Nature. "
          "1953;171:737-738.")
CIT_FALCONER = ("Falconer DS, Mackay TFC. Introduction to Quantitative "
                "Genetics. 4th ed. Longman; 1996.")

SIG_LENS = ("The Signature read: the problem is approached as a covenant "
            "of evidence, mechanism, and testable prediction - the Signature "
            "Genetics Method files the unsolved question, proposes the "
            "path, and states exactly what would confirm or kill it. "
            "Clearly labeled Signature-made, never presented as established "
            "science.")

ENTRIES = [
    {
        "key": "junk_dna",
        "name": "What Does All the Non-Coding DNA Actually Do",
        "group": "Genome Structure and Size",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "problem": ("Only about 1 to 2 percent of the human genome codes for "
                    "proteins, yet the ENCODE project reported biochemical "
                    "activity across roughly 80 percent of it, while "
                    "evolutionary comparison finds only about 8 percent "
                    "under selection. What is the rest of the DNA doing - "
                    "and how much of it is doing anything at all?"),
        "background": (
            "When the human genome was sequenced, the shock was how little "
            "of it made proteins: barely 1 to 2 percent. The rest was "
            "dismissed by some as junk DNA, leftover baggage from evolution. "
            "In 2012 the ENCODE consortium reported that about 80 percent "
            "of the genome shows some biochemical activity - transcription, "
            "protein binding, chemical marks - which was announced as the "
            "death of junk DNA. Evolutionary biologists objected: activity "
            "is not function, and comparisons across 29 mammals show only "
            "about 8.2 percent of the genome under purifying selection, "
            "meaning mutations there are weeded out because they matter. "
            "The gap is enormous: roughly 72 percent of the genome is "
            "biochemically active but not detectably conserved. Some of it "
            "is surely regulatory - switches and dimmers for genes - some is "
            "structural, and some may truly be tolerated noise that the "
            "cell transcribes at low cost. The debate continues because the "
            "two camps measure different things: ENCODE measures what the "
            "genome does, evolution measures what the genome cannot afford "
            "to lose."
        ),
        "why_it_matters": (
            "If most disease-linked genetic variants sit outside "
            "protein-coding genes - and genome-wide studies say they do - "
            "then understanding non-coding DNA is understanding the "
            "instructions behind most inherited disease risk. It also "
            "decides how we read any genome: a parts list of genes, or a "
            "full operating manual. Settling what the dark matter of the "
            "genome does would rewrite textbooks on what a gene even is."
        ),
        "sig_pointer": (
            "The Signature approach proposes treating the genome as a "
            "layered signal system and testing each layer against an "
            "explicit cost model of transcription: details live in the "
            "Signature Edition record, labeled as a proposed solution."
        ),
        "sig_steps": [
            "Assume the genome carries layered signals: code, regulation, structure, and tolerated noise, each with a distinct cost signature.",
            "Model transcription cost per base per cell type and compare it against measured low-level transcription rates.",
            "Predict that truly neutral transcribed regions drift freely between species while regulatory regions preserve binding-site grammar even when the sequence drifts.",
            "Test the prediction by comparing binding-site turnover against expression conservation across mammals.",
            "Assign every region a Signature function score: conservation weight plus regulatory grammar weight minus transcription-cost penalty.",
        ],
        "sig_assumptions": {
            "biochemically_active_fraction": 0.80,
            "constrained_fraction": 0.082,
            "gap_fraction": 0.718,
            "genome_bp": 3200000000,
        },
        "sig_confirm": [
            "Binding-site grammar is conserved in regions where raw sequence is not, matching the layered-signal prediction.",
            "Regions with high transcription cost and no grammar show no fitness effect when deleted in cell models.",
        ],
        "sig_refute": [
            "Large-scale deletion screens show most active-but-unconserved regions are individually essential.",
            "Transcription cost turns out to be effectively zero, removing the penalty the model relies on.",
        ],
        "sig_scope": (
            "This does not claim that any particular non-coding region is "
            "functional or junk; it proposes a scoring framework and the "
            "experiments that would validate it. The true functional "
            "fraction of the genome remains unknown."
        ),
        "scenario": {
            "observed_confirm": ["binding-site grammar conserved where sequence drifts"],
            "observed_refute": [],
        },
        "description": (
            "Only 1 to 2 percent of the human genome codes for proteins, "
            "yet ENCODE found biochemical activity across about 80 percent "
            "while evolution constrains only about 8 percent. This record "
            "frames the most approachable great mystery of genetics: what "
            "is all that non-coding DNA doing, and how much of it is doing "
            "anything at all? Includes the history from junk DNA to ENCODE "
            "to the selectionist reply, why it matters for reading disease "
            "variants, and a pointer to the Signature proposed solution."
        ),
        "key_points": [
            "Protein-coding DNA is only 1 to 2 percent of the human genome; the other 98 percent is the mystery.",
            "ENCODE (2012) reported biochemical activity across ~80% of the genome; mammalian comparisons find ~8.2% under purifying selection.",
            "Activity is not function: transcription and binding can occur without fitness consequence.",
            "The ~72% gap between activity and conservation is where the entire debate lives.",
            "Resolution requires separating regulatory signal, structural roles, and tolerated noise with experiments, not definitions.",
        ],
        "requirements": [
            "A problem statement grounded in the published numbers (80% activity, 8.2% constraint), not in slogans.",
            "A background covering both the ENCODE claim and the evolutionary counterargument fairly.",
            "A why-it-matters section tied to disease variants in non-coding regions.",
            "A signature pointer that labels the proposed solution as proposed, never settled.",
        ],
        "standards": [
            "Fractions stated with their sources: ENCODE 2012 for activity, Lindblad-Toh 2011 for constraint.",
            "No claim that any specific region is functional without experimental evidence.",
            "Honesty label present on every signature_solution field.",
        ],
        "citations": [CIT_ENCODE, CIT_CONSTRAINT, CIT_HGP],
    },
    {
        "key": "gene_count",
        "name": "Why Do Humans Have So Few Genes",
        "group": "Genome Structure and Size",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "problem": ("Humans build brains, languages, and civilizations with "
                    "about 20,000 protein-coding genes - roughly the same "
                    "count as a mouse and fewer than some plants. If genes "
                    "are the instructions for life, why does complexity not "
                    "come with more of them?"),
        "background": (
            "Before the genome was sequenced, estimates of the human gene "
            "count ran as high as 100,000; surely a being this complex "
            "needed a vast parts list. The draft sequence in 2001 cut that "
            "to roughly 30,000, and refined annotation has settled near "
            "20,000 protein-coding genes - about the same as the mouse "
            "genome, and far fewer than the roughly 25,000 in the small weed "
            "Arabidopsis or the tens of thousands in some amphibians. This "
            "is the gene-count paradox: organismal complexity is decoupled "
            "from gene number. The resolution most geneticists favor is "
            "that complexity lives in regulation - when and where genes are "
            "turned on, how their messages are spliced, and how proteins "
            "combine - rather than in the raw count of genes. But that "
            "answer is qualitative: nobody has a complete quantitative "
            "accounting that derives a human from 20,000 genes plus "
            "regulatory logic, and the exact gene count still shifts as "
            "annotation improves."
        ),
        "why_it_matters": (
            "If complexity is in the wiring rather than the parts, then "
            "medicine and biotechnology must target regulatory circuits, "
            "not just broken genes - most disease variants already point "
            "there. A real accounting of how 20,000 genes build a human "
            "would also tell us what minimal instruction sets are possible, "
            "which matters for synthetic biology."
        ),
        "sig_pointer": (
            "The Signature approach proposes a regulation-first complexity "
            "budget that counts control states instead of genes; the full "
            "treatment is in the Signature Edition record, labeled as a "
            "proposed solution."
        ),
        "sig_steps": [
            "Replace the gene count with a control-state count: genes times regulatory elements times splice forms.",
            "Estimate the budget from annotation: ~20,000 genes, ~900,000 candidate regulatory elements, ~10 isoforms per gene.",
            "Predict that organism complexity tracks the regulatory budget across species, not the gene count.",
            "Test by correlating regulatory-element counts with measures of cell-type diversity across sequenced animals.",
        ],
        "sig_assumptions": {
            "human_protein_coding_genes": 19932,
            "mouse_protein_coding_genes": 21590,
            "mouse_human_ratio": 1.0832,
        },
        "sig_confirm": [
            "Regulatory-element counts predict cell-type diversity across species better than gene counts do.",
        ],
        "sig_refute": [
            "Some complex lineages show small regulatory budgets, breaking the correlation.",
        ],
        "sig_scope": (
            "This does not claim a complete derivation of human complexity; "
            "it proposes the budget metric and the cross-species test that "
            "would support or sink it."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "Humans run on about 20,000 protein-coding genes - about as "
            "many as a mouse. This record explores the gene-count paradox: "
            "why complexity does not come with more genes, how regulation "
            "is thought to fill the gap, and why the quantitative "
            "accounting is still missing. Includes the history from "
            "100,000-gene estimates to modern annotation and a pointer to "
            "the Signature proposed solution."
        ),
        "key_points": [
            "Early estimates put human genes near 100,000; annotation now sits near 20,000.",
            "Mice carry a similar count (~21,590), yet build very different bodies and brains.",
            "The favored resolution is regulation: control logic, not parts count, builds complexity.",
            "The resolution is qualitative - no complete quantitative derivation exists.",
            "Gene counts still shift as annotation methods improve.",
        ],
        "requirements": [
            "Current gene-count numbers from GENCODE annotation for human and mouse.",
            "Fair presentation of the regulation-first resolution and its limits.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "Gene counts cited from the GENCODE reference annotation.",
            "No claim that regulation fully explains complexity as established fact.",
        ],
        "citations": [CIT_GENCODE, CIT_HGP],
    },
    {
        "key": "cvalue",
        "name": "The C-Value Paradox: Genome Size Versus Complexity",
        "group": "Genome Structure and Size",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "problem": ("Genome size does not track organismal complexity: the "
                    "flowering plant Paris japonica carries about 149 "
                    "billion base pairs, roughly 47 times the human genome, "
                    "and some amoebas dwarf both. Why do genomes vary so "
                    "wildly in size, and what sets the size at all?"),
        "background": (
            "The C-value is the amount of DNA in a haploid genome, and the "
            "paradox named for it is old: genome size spans orders of "
            "magnitude with no respect for complexity. Humans carry 3.2 "
            "billion base pairs; an onion carries about 16 billion; the "
            "lungfish carries around 130 billion; and Paris japonica, a "
            "modest woodland flower, holds the recorded extreme near 149 "
            "billion. Much of the bulk is repetitive DNA and transposable "
            "elements - genomic parasites that copy themselves - plus "
            "duplicated segments and vast non-coding stretches. Population "
            "genetics offers the leading explanation: species with small "
            "effective population sizes cannot efficiently purge mildly "
            "harmful DNA bloat, so genomes inflate by drift, while large "
            "populations keep genomes lean. This explains part of the "
            "pattern, but the full accounting - what caps genome size, why "
            "some lineages purge and others bloat - remains an open "
            "quantitative problem."
        ),
        "why_it_matters": (
            "Genome size sets the cost and difficulty of sequencing, "
            "editing, and synthesizing any organism. Understanding what "
            "controls it would guide which species we can engineer and "
            "reveal how much of any genome is load versus machinery."
        ),
        "sig_pointer": (
            "The Signature approach proposes a drift-versus-purge budget "
            "equation for genome size; the full treatment is in the "
            "Signature Edition record, labeled as a proposed solution."
        ),
        "sig_steps": [
            "Write genome size as an equilibrium between transposon insertion rate and deletion/purge rate.",
            "Parameterize purge efficiency by effective population size, following the drift-barrier logic.",
            "Predict each lineage's size from its insertion rate and long-term population size.",
            "Test against the sequenced extremes: Paris japonica, lungfish, onion, human.",
        ],
        "sig_assumptions": {
            "human_Gb": 3.2,
            "onion_Gb": 16.0,
            "lungfish_Gb": 133.0,
            "paris_japonica_Gb": 149.0,
            "paris_human_ratio": 46.5625,
        },
        "sig_confirm": [
            "Predicted sizes from insertion rate and population size match observed extremes within a factor of two.",
        ],
        "sig_refute": [
            "Lineages with large populations and high insertion rates still bloat, contradicting the purge term.",
        ],
        "sig_scope": (
            "This does not claim to predict any single species' genome "
            "size; it proposes the equilibrium framework and the test "
            "against extremes."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "A woodland flower carries 47 times more DNA than a human. This "
            "record covers the C-value paradox: why genome size ignores "
            "complexity, the roles of transposons and population size, and "
            "the leading drift-based explanation. Includes the record "
            "extremes from onion to lungfish to Paris japonica and a pointer "
            "to the Signature proposed solution."
        ),
        "key_points": [
            "Human genome: 3.2 Gb; onion: ~16 Gb; lungfish: ~130 Gb; Paris japonica: ~149 Gb.",
            "Bulk DNA is largely repeats, transposons, and duplications, not genes.",
            "Small effective population sizes weaken selection against DNA bloat.",
            "The drift-barrier explanation covers part of the pattern, not all of it.",
            "What caps genome size in any lineage is still not fully quantified.",
        ],
        "requirements": [
            "Record genome-size numbers with sources.",
            "Present the drift-barrier explanation as leading but incomplete.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "Extreme values cited from the botanical genome-size literature.",
            "No claim that population size explains all genome-size variation.",
        ],
        "citations": [CIT_CVALUE, CIT_PARIS],
    },
    {
        "key": "human_mouse",
        "name": "Same Genes, Different Animal: The Human-Mouse Puzzle",
        "group": "Genome Structure and Size",
        "ladder_rank": 4,
        "ladder_tier": "foundations",
        "problem": ("Humans and mice share a similar gene count and most "
                    "genes are recognizably the same, yet one builds a "
                    "primate brain and the other a rodent. If the parts "
                    "list is nearly identical, where is the difference "
                    "written?"),
        "background": (
            "The mouse was the second mammal sequenced precisely because "
            "its genes mirror ours: the great majority of human "
            "protein-coding genes have a mouse counterpart, and the counts "
            "- about 20,000 in human, about 21,500 in mouse - are close. "
            "Divergence came roughly 75 million years ago, and since then "
            "the two lineages have edited regulation far more than parts. "
            "Comparative studies show that gene expression patterns, "
            "enhancer usage, and developmental timing differ dramatically "
            "even where the protein sequences are nearly identical. The "
            "unsolved part is quantitative: we have catalogs of differences "
            "- millions of regulatory variants, rewired enhancers, shifted "
            "timing - but no compact account that says which subset of "
            "regulatory changes is sufficient to turn a mouse developmental "
            "program toward a primate one. The ENCODE and Roadmap projects "
            "cataloged on the order of 900,000 candidate regulatory "
            "elements in human - about 45 per protein-coding gene - yet "
            "mapping which elements drive which species differences is "
            "still underway."
        ),
        "why_it_matters": (
            "Mice are the workhorse of disease research; knowing exactly "
            "which regulatory differences separate mouse from human biology "
            "decides when a mouse result will translate and when it will "
            "mislead. It is also the clearest test case for the idea that "
            "evolution edits switches, not genes."
        ),
        "sig_pointer": (
            "The Signature approach proposes ranking regulatory elements by "
            "a divergence-impact score and testing the top set in "
            "developmental models; the full treatment is in the Signature "
            "Edition record, labeled as a proposed solution."
        ),
        "sig_steps": [
            "Catalog candidate regulatory elements in both species (~900,000 in human).",
            "Score each element by sequence divergence times chromatin-state divergence in matched tissues.",
            "Rank elements and predict that the top-ranked set explains most expression divergence.",
            "Test by editing top-ranked elements in cell models and measuring expression shifts.",
        ],
        "sig_assumptions": {
            "candidate_regulatory_elements": 900000,
            "protein_coding_genes": 19932,
            "elements_per_gene": 45.1535,
            "divergence_MYA": 75,
        },
        "sig_confirm": [
            "Editing top-ranked elements shifts expression toward the other species' pattern.",
        ],
        "sig_refute": [
            "Expression divergence is spread evenly across all elements, so no ranked subset dominates.",
        ],
        "sig_scope": (
            "This does not claim mice can be reprogrammed toward primate "
            "development; it proposes a scoring and testing framework for "
            "regulatory divergence."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "Humans and mice carry nearly the same gene list, yet build "
            "utterly different animals. This record traces the human-mouse "
            "puzzle from the sequencing surprises through the "
            "regulation-first answer to the still-missing quantitative "
            "accounting. Includes divergence history, the ~900,000-element "
            "regulatory catalog, and a pointer to the Signature proposed "
            "solution."
        ),
        "key_points": [
            "Most human protein-coding genes have a direct mouse counterpart.",
            "Lineages diverged ~75 million years ago; regulation diverged more than protein sequences.",
            "About 900,000 candidate regulatory elements are cataloged in human - ~45 per gene.",
            "No compact account yet says which regulatory changes suffice to explain the species gap.",
            "The gap matters directly for translating mouse disease research to humans.",
        ],
        "requirements": [
            "Gene-count and regulatory-element numbers with sources.",
            "Clear statement that the quantitative mapping is unfinished.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "Regulatory element counts attributed to the ENCODE/Roadmap catalogs.",
            "No claim that editing elements can convert developmental programs.",
        ],
        "citations": [CIT_GENCODE, CIT_ENCODE],
    },
    {
        "key": "missing_heritability",
        "name": "The Missing Heritability Problem",
        "group": "Inheritance and Variation",
        "ladder_rank": 5,
        "ladder_tier": "foundations",
        "problem": ("Twin studies say height is about 80 percent heritable, "
                    "yet the common genetic variants found by genome-wide "
                    "studies long explained far less. Where is the rest of "
                    "the heritability hiding?"),
        "background": (
            "Heritability measures how much of the variation in a trait "
            "across a population comes from genetic differences, and twin "
            "studies have long put height near 80 percent. When "
            "genome-wide association studies arrived, they found hundreds "
            "of variants for height - but together the common ones explained "
            "only a fraction of that 80 percent, leaving the famous gap "
            "called missing heritability. In 2010 Yang and colleagues "
            "showed that considering all common SNPs together, not just the "
            "genome-wide-significant hits, recovered about 45 percent of "
            "height variance - the heritability had been hiding below the "
            "significance threshold in thousands of tiny effects. Later "
            "whole-genome and rare-variant studies pushed the explained "
            "share higher still, and by 2022 saturated maps covered much of "
            "the common-variant contribution. The problem is not fully "
            "closed: rare variants, structural variants, interactions, and "
            "the exact architecture of the remaining gap are still being "
            "mapped, and for many traits the gap remains wide."
        ),
        "why_it_matters": (
            "Closing the gap decides how well we can predict traits and "
            "disease risk from DNA - the entire premise of polygenic "
            "prediction. It also settled a methodological lesson for all of "
            "genetics: strict significance thresholds were discarding real "
            "biology by the thousands of variants."
        ),
        "sig_pointer": (
            "The Signature approach proposes a threshold-free heritability "
            "budget that partitions variance across variant classes; the "
            "full treatment is in the Signature Edition record, labeled as "
            "a proposed solution."
        ),
        "sig_steps": [
            "Take twin heritability (0.80 for height) as the total to be partitioned.",
            "Partition it across variant classes: genome-wide-significant, sub-threshold common, rare, structural.",
            "Fit each class without significance thresholds, using whole-genome relatedness.",
            "Predict the residual gap and which class should close it as sample sizes grow.",
        ],
        "sig_assumptions": {
            "twin_heritability": 0.80,
            "snp_heritability": 0.45,
            "missing": 0.35,
            "fraction_explained": 0.5625,
        },
        "sig_confirm": [
            "Each predicted class closes its assigned share of the gap as cohorts grow.",
        ],
        "sig_refute": [
            "The gap persists unchanged at very large sample sizes, implying a non-additive source.",
        ],
        "sig_scope": (
            "This does not claim heritability is fully found; it proposes "
            "the partitioning budget and the growth-based test."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "Twin studies put height heritability near 80 percent, but "
            "early genome scans found only a fraction of it. This record "
            "covers the missing heritability problem from its naming "
            "through the 2010 discovery that thousands of sub-threshold "
            "variants held the missing share, to the still-open remainder. "
            "Includes the key numbers, why thresholds hid the biology, and "
            "a pointer to the Signature proposed solution."
        ),
        "key_points": [
            "Twin heritability of height is ~0.80; early GWAS hits explained far less.",
            "Yang et al. (2010) recovered ~0.45 using all common SNPs together - the gap was hiding below significance thresholds.",
            "Missing fraction at that point: 0.35 of 0.80, about 44% of the heritability.",
            "Rare and structural variants plus interactions hold much of the remainder.",
            "For many traits the gap is still wide open.",
        ],
        "requirements": [
            "The 0.80 / 0.45 / 0.35 numbers with sources.",
            "Clear statement that the problem is narrowed, not closed.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "Heritability figures attributed to twin studies and the cited GWAS literature.",
            "No claim that prediction from DNA is solved.",
        ],
        "citations": [CIT_YANG, CIT_YENGO, CIT_FALCONER],
    },
    {
        "key": "genotype_phenotype",
        "name": "The Genotype-Phenotype Map: Reading Traits from DNA",
        "group": "Health, Behavior, and Prediction",
        "ladder_rank": 6,
        "ladder_tier": "foundations",
        "problem": ("Given a person's complete genome, can we predict their "
                    "traits - height, disease risk, drug response? The map "
                    "from genotype to phenotype is the central prediction "
                    "problem of genetics, and for most traits it remains "
                    "stubbornly incomplete."),
        "background": (
            "Mendel showed that single genes predict single traits in peas, "
            "and for rare single-gene disorders the map still works that "
            "way. But most human traits - height, blood pressure, diabetes "
            "risk - are influenced by thousands of variants of tiny effect, "
            "plus environments, plus chance in development. Polygenic scores "
            "add up the small effects, and for height the best scores now "
            "explain around 40 percent of trait variance - impressive, yet "
            "still half of the heritable share and far from individual "
            "certainty. The deeper problem is that the map is not a list: "
            "variants interact with each other and with environments, their "
            "effects differ across ancestries, and development can amplify "
            "or erase small genetic nudges. Predicting a trait from a "
            "genome is therefore less like reading a blueprint and more "
            "like forecasting weather from a list of clouds."
        ),
        "why_it_matters": (
            "A working genotype-phenotype map would turn every genome "
            "sequence into a personalized risk forecast and a guide to "
            "which treatments fit which patient. Its current limits are "
            "also a guardrail: they are why responsible scientists warn "
            "against over-interpreting consumer DNA predictions."
        ),
        "sig_pointer": (
            "The Signature approach proposes a layered prediction stack - "
            "additive base, interaction layer, environment layer - with an "
            "honest uncertainty budget at each layer; the full treatment is "
            "in the Signature Edition record, labeled as a proposed "
            "solution."
        ),
        "sig_steps": [
            "Start from the additive polygenic base: sum of small effects gives the R^2 floor (~0.40 for height).",
            "Add an interaction layer: pairwise variant interactions estimated from family data.",
            "Add an environment layer: measured exposures that modify genetic effects.",
            "Attach an uncertainty budget to every prediction: report the interval, never just the point estimate.",
            "Predict that the ceiling of the stack converges to the twin heritability (~0.80 for height).",
        ],
        "sig_assumptions": {
            "twin_heritability": 0.80,
            "current_pgs_r2": 0.40,
            "unexplained_predictable": 0.40,
        },
        "sig_confirm": [
            "Stacked predictions beat additive-only scores on held-out cohorts across multiple traits.",
        ],
        "sig_refute": [
            "Interaction and environment layers add nothing beyond the additive base at large sample sizes.",
        ],
        "sig_scope": (
            "This does not claim individual traits can be predicted "
            "exactly; it proposes the layered stack and the uncertainty "
            "budget as the honest framing."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "Can a genome predict a person? This record covers the "
            "genotype-phenotype map: from Mendel's peas to polygenic scores "
            "that explain ~40% of height variance against an 80% heritable "
            "ceiling, why interactions and environments blur the map, and "
            "why its limits matter for responsible DNA interpretation. "
            "Includes a pointer to the Signature proposed solution."
        ),
        "key_points": [
            "Single-gene traits are predictable; most traits are influenced by thousands of tiny-effect variants.",
            "Best polygenic scores explain ~40% of height variance vs an ~80% heritability ceiling.",
            "Interactions, ancestry differences, and developmental chance all blur the map.",
            "The map is more like weather forecasting than blueprint reading.",
            "Current limits are a scientific guardrail against over-interpreting DNA predictions.",
        ],
        "requirements": [
            "The 0.40 vs 0.80 numbers with sources.",
            "Clear separation of what is predictable from what is not.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "Prediction figures attributed to the polygenic-score literature.",
            "No claim of individual-level trait prediction as established.",
        ],
        "citations": [CIT_YENGO, CIT_OMNI, CIT_MARTIN],
    },
    {
        "key": "gxe",
        "name": "Genes Meet Environment: Mapping Gene-Environment Interaction",
        "group": "Environment and Epigenetics",
        "ladder_rank": 7,
        "ladder_tier": "foundations",
        "problem": ("Genes do not act in a vacuum: the same genetic variant "
                    "can raise risk in one environment and be harmless in "
                    "another. Mapping these gene-environment interactions "
                    "systematically - which variants, which environments, "
                    "how large the effects - remains an unsolved measurement "
                    "problem."),
        "background": (
            "The idea is old: a seed's genes matter, but so do soil and "
            "rain. In human genetics the landmark was Caspi and "
            "colleagues' 2002 finding that a variant in the MAOA gene "
            "predicted antisocial outcomes mainly in maltreated children - "
            "genotype and environment interacting, neither sufficient "
            "alone. Since then, interaction studies have multiplied but "
            "also stumbled: environments are hard to measure with the "
            "precision of genotypes, people select and shape their own "
            "environments partly because of their genes, and early "
            "candidate-gene interactions often failed to replicate. Modern "
            "work uses polygenic scores crossed with measured exposures - "
            "for example, physical activity attenuating the obesity risk "
            "from FTO variants - and reaction-norm models borrowed from "
            "agriculture, where the same crop strain is planted across "
            "climates. The unsolved core is scale and causality: measuring "
            "environments as carefully as genomes, across a lifetime, in "
            "hundreds of thousands of people."
        ),
        "why_it_matters": (
            "If risk variants only bite in certain environments, then "
            "prevention can target the environment instead of the genome - "
            "no gene editing required. It also rescues heritability "
            "estimates from a false nature-versus-nurture framing: the "
            "action is in the interaction."
        ),
        "sig_pointer": (
            "The Signature approach proposes reaction-norm mapping at "
            "biobank scale with environment measured like a phenotype; the "
            "full treatment is in the Signature Edition record, labeled as "
            "a proposed solution."
        ),
        "sig_steps": [
            "Treat each environment as a measured phenotype with the same rigor as genotyping.",
            "Fit reaction norms: trait as a function of polygenic score crossed with environment.",
            "Rank interactions by the crossing statistic - where genotype ranks flip between environments.",
            "Validate top interactions in independent cohorts before any causal claim.",
        ],
        "sig_assumptions": {
            "genotype_A_env0": 100.0,
            "genotype_A_env1": 100.0,
            "genotype_B_env0": 95.0,
            "genotype_B_env1": 105.0,
            "interaction_effect": 10.0,
        },
        "sig_confirm": [
            "Top-ranked interactions replicate across independent biobanks.",
        ],
        "sig_refute": [
            "No interaction survives replication once environments are measured without bias.",
        ],
        "sig_scope": (
            "This does not claim any specific interaction is real; it "
            "proposes the measurement standard and the replication bar."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "The same variant can harm in one environment and sit quiet in "
            "another. This record covers gene-environment interaction from "
            "the 2002 MAOA landmark through replication struggles to modern "
            "biobank reaction-norm mapping, and why measuring environments "
            "as carefully as genomes is the unsolved core. Includes a "
            "pointer to the Signature proposed solution."
        ),
        "key_points": [
            "Caspi et al. (2002): MAOA variant predicted outcomes mainly in maltreated children - the classic interaction.",
            "Environments are measured far less precisely than genotypes, which biases every interaction study.",
            "People partly choose environments because of their genes, tangling cause and effect.",
            "Modern work crosses polygenic scores with measured exposures at biobank scale.",
            "Replication across independent cohorts is the bar an interaction must clear.",
        ],
        "requirements": [
            "The Caspi 2002 landmark described accurately.",
            "Honest account of replication failures in candidate-gene work.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "No specific gene-environment claim presented as established beyond the cited literature.",
            "Environments described as measurement-limited, not as solved.",
        ],
        "citations": [CIT_CASPI, CIT_FALCONER],
    },
    {
        "key": "siblings_differ",
        "name": "Why Siblings Differ: The Lottery Inside Families",
        "group": "Inheritance and Variation",
        "ladder_rank": 8,
        "ladder_tier": "foundations",
        "problem": ("Full siblings share the same parents, yet differ "
                    "markedly in looks, health, and temperament. How much "
                    "of that difference is the random shuffle of "
                    "inheritance itself - and can we quantify the lottery "
                    "each child draws?"),
        "background": (
            "Every child receives half of each parent's genome, but which "
            "half is a lottery: recombination shuffles parental chromosomes "
            "and independent assortment deals the segments, so full siblings "
            "share on average 50 percent of their DNA - with a standard "
            "deviation around 4 percent, meaning some pairs share notably "
            "more or less. On top of the shuffle, each child carries "
            "roughly 70 brand-new mutations that neither parent had in "
            "that form, most arriving in the father's sperm and increasing "
            "with his age. Quantitative geneticists have long partitioned "
            "sibling differences into the shared family environment, the "
            "non-shared environment, and this Mendelian sampling - the "
            "genetic lottery. The unsolved edge is prediction: given the "
            "parents' genomes, we can compute the distribution of possible "
            "children, but pinning down why a particular sibling pair "
            "diverged - which shuffle, which new mutation, which "
            "environment - remains beyond reach for complex traits."
        ),
        "why_it_matters": (
            "Understanding sibling differences is the cleanest window into "
            "how much of a life is chance: it separates the draw of the "
            "genetic lottery from upbringing. It also grounds debates "
            "about fairness - siblings start from the same family but never "
            "from the same genome."
        ),
        "sig_pointer": (
            "The Signature approach proposes a family lottery simulator "
            "that enumerates possible children from parental genomes; the "
            "full treatment is in the Signature Edition record, labeled as "
            "a proposed solution."
        ),
        "sig_steps": [
            "Model meiosis as a shuffle: recombination breakpoints drawn from the genetic map.",
            "Draw de novo mutations per child (~70, scaled by paternal age).",
            "Enumerate thousands of possible children from a parental pair and build the trait distribution.",
            "Compare real sibling pairs against the simulated distribution to partition luck from environment.",
        ],
        "sig_assumptions": {
            "mean_ibd_sharing": 0.50,
            "sd_ibd_sharing": 0.04,
            "denovo_per_child": 70,
            "shared_denovo_expected": 0,
        },
        "sig_confirm": [
            "Real sibling trait spreads match the simulated lottery distribution across many families.",
        ],
        "sig_refute": [
            "Sibling differences systematically exceed the lottery, implicating unmodeled systematic effects.",
        ],
        "sig_scope": (
            "This does not claim to explain any particular family's "
            "differences; it proposes the simulator and the comparison "
            "test."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "Siblings share parents but draw different genetic hands. This "
            "record quantifies the family lottery: ~50% DNA sharing with ~4% "
            "spread, ~70 new mutations per child, and why partitioning luck "
            "from upbringing remains unfinished for complex traits. Includes "
            "a pointer to the Signature proposed solution."
        ),
        "key_points": [
            "Full siblings share ~50% of DNA on average, with a standard deviation near 4%.",
            "Each child carries ~70 de novo mutations, mostly paternal in origin.",
            "Mendelian sampling - the shuffle - is distinct from family environment effects.",
            "The distribution of possible children is computable; the explanation of a specific pair is not.",
            "Sibling comparison is the cleanest natural experiment for separating chance from upbringing.",
        ],
        "requirements": [
            "The 50% / 4% / 70 numbers with sources.",
            "Clear distinction between the shuffle, new mutations, and environment.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "Sharing statistics attributed to the segregation literature.",
            "No claim of predicting individual sibling outcomes.",
        ],
        "citations": [CIT_KONG, CIT_FALCONER],
    },
    {
        "key": "harmful_persist",
        "name": "Why Harmful Mutations Persist",
        "group": "Inheritance and Variation",
        "ladder_rank": 9,
        "ladder_tier": "foundations",
        "problem": ("Natural selection should purge mutations that kill or "
                    "disable, yet severe disease alleles like the cystic "
                    "fibrosis mutation persist at carrier frequencies near 1 "
                    "in 25 in some populations. What keeps them around?"),
        "background": (
            "The textbook balance is mutation-selection equilibrium: new "
            "harmful mutations arise each generation while selection "
            "removes them, settling at a low frequency - for a lethal "
            "recessive, the equilibrium frequency is the square root of "
            "the mutation rate divided by the selection strength. But the "
            "numbers often refuse to cooperate. The delta-F508 variant in "
            "the CFTR gene reaches carrier frequencies around 1 in 25 in "
            "Northern European ancestry, implying an allele frequency near "
            "0.02; under simple balance with complete selection against "
            "homozygotes, that demands a mutation rate near 4 in 10,000 - "
            "roughly forty times the typical per-gene rate. Something else "
            "must be propping it up. Candidates include heterozygote "
            "advantage (carriers resisting some historical disease, as with "
            "sickle-cell and malaria), relaxed selection in recent history, "
            "population bottlenecks amplifying rare alleles by drift, and "
            "simply the slowness of purging recessives that hide in "
            "heterozygotes. Which force dominates for which disease allele "
            "is still debated case by case."
        ),
        "why_it_matters": (
            "Every persistent disease allele is a clue about human "
            "history: past epidemics, migrations, and bottlenecks are "
            "written in their frequencies. Understanding the forces also "
            "predicts how allele frequencies will shift as medicine relaxes "
            "selection further."
        ),
        "sig_pointer": (
            "The Signature approach proposes a force-decomposition test "
            "that pits balance, advantage, and drift against each allele's "
            "geography; the full treatment is in the Signature Edition "
            "record, labeled as a proposed solution."
        ),
        "sig_steps": [
            "Compute the mutation rate implied by simple mutation-selection balance for the allele.",
            "Compare it against the measured per-gene mutation rate; a large excess flags missing forces.",
            "Test heterozygote advantage via historical disease geography and carrier fitness data.",
            "Test drift via bottleneck signatures in the surrounding haplotype.",
            "Assign the allele a force profile: balance share, advantage share, drift share.",
        ],
        "sig_assumptions": {
            "carrier_frequency": 0.04,
            "allele_frequency": 0.02,
            "selection_against_homozygote": 1.0,
            "implied_mutation_rate": 0.0004,
            "typical_gene_mutation_rate": 1e-05,
        },
        "sig_confirm": [
            "Alleles with large balance excess show matching advantage or bottleneck signatures.",
        ],
        "sig_refute": [
            "Excess alleles show neither advantage nor drift signatures, demanding a new force.",
        ],
        "sig_scope": (
            "This does not claim to know why any specific allele persists; "
            "it proposes the decomposition test."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "Selection should erase lethal alleles, yet cystic fibrosis "
            "carriers number 1 in 25 in Northern Europe. This record walks "
            "through mutation-selection balance, shows the numbers demand "
            "forty times the normal mutation rate, and surveys the "
            "candidate rescue forces: heterozygote advantage, drift, and "
            "relaxed selection. Includes a pointer to the Signature "
            "proposed solution."
        ),
        "key_points": [
            "Cystic fibrosis delta-F508 carriers: ~1 in 25 in Northern European ancestry.",
            "Simple balance implies a mutation rate near 4e-4, ~40x the typical per-gene rate.",
            "Heterozygote advantage is proven for sickle-cell/malaria; unproven for most other alleles.",
            "Recessive alleles hide from selection in heterozygotes, slowing any purge.",
            "Bottlenecks and relaxed selection are live alternative explanations.",
        ],
        "requirements": [
            "The 1/25 and 4e-4 calculations shown explicitly.",
            "No claim that heterozygote advantage explains cystic fibrosis.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "Carrier frequency stated for the specific ancestry, not as a global figure.",
            "Advantage hypotheses labeled as hypotheses where unproven.",
        ],
        "citations": [CIT_ALLISON, CIT_FALCONER, CIT_HALDANE],
    },
    {
        "key": "paternal_age",
        "name": "Where New Mutations Come From: The Paternal Age Effect",
        "group": "Inheritance and Variation",
        "ladder_rank": 10,
        "ladder_tier": "foundations",
        "problem": ("Each child carries dozens of mutations neither parent "
                    "had, and the count rises with the father's age. What "
                    "sets the human mutation rate, why does it climb with "
                    "paternal age, and how much of disease risk does this "
                    "conveyor of new mutations explain?"),
        "background": (
            "Kong and colleagues' 2012 sequencing of Icelandic families "
            "established the modern numbers: roughly 70 de novo single-base "
            "mutations per child per generation, with about two additional "
            "mutations for each extra year of the father's age at "
            "conception. The mechanism is cell division: sperm stem cells "
            "divide continuously throughout a man's life, and every "
            "division risks a copying error, while eggs are formed before "
            "birth and divide far less. This paternal age effect links "
            "older fatherhood to modestly increased risks of conditions "
            "enriched for de novo mutations. The unsolved parts are the "
            "deeper controls: why the baseline rate is what it is, how "
            "much it varies between families and populations, what "
            "fraction of complex-disease risk flows through new mutations "
            "versus inherited ones, and whether the rate itself can evolve "
            "under selection."
        ),
        "why_it_matters": (
            "De novo mutations are evolution's raw material and a slice of "
            "disease risk that no family history can predict. Knowing the "
            "rate's controls would sharpen genetic counseling and reveal "
            "how fast the human genome is actually changing."
        ),
        "sig_pointer": (
            "The Signature approach proposes a division-counting model of "
            "the germline that predicts family-to-family rate variation; "
            "the full treatment is in the Signature Edition record, labeled "
            "as a proposed solution."
        ),
        "sig_steps": [
            "Model sperm stem-cell divisions as a function of paternal age from puberty onward.",
            "Assign a per-division error rate and predict each family's de novo count.",
            "Compare predictions against sequenced trios to find families that deviate.",
            "Investigate deviating families for genetic modifiers of the mutation rate itself.",
        ],
        "sig_assumptions": {
            "denovo_at_paternal_20": 70,
            "extra_per_paternal_year": 2.0,
            "denovo_at_paternal_40": 110.0,
        },
        "sig_confirm": [
            "Family deviations cluster by inherited modifiers of DNA repair genes.",
        ],
        "sig_refute": [
            "Deviations are pure noise with no heritable component.",
        ],
        "sig_scope": (
            "This does not claim the mutation rate is under simple genetic "
            "control; it proposes the search for modifiers."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "Every child carries ~70 new mutations, plus ~2 more for each "
            "year of the father's age. This record covers the paternal age "
            "effect from Kong 2012 through the stem-cell-division mechanism "
            "to the open questions: what sets the baseline rate, how it "
            "varies, and whether the rate itself can evolve. Includes a "
            "pointer to the Signature proposed solution."
        ),
        "key_points": [
            "~70 de novo single-base mutations per child per generation (Kong et al. 2012).",
            "About 2 additional mutations per extra year of paternal age.",
            "Mechanism: sperm stem cells divide lifelong; eggs do not.",
            "The baseline rate's controls and family-to-family variation are still open.",
            "De novo mutations are disease risk no family history can foresee.",
        ],
        "requirements": [
            "The 70 / 2-per-year numbers with the Kong 2012 source.",
            "Mechanism stated plainly without overstating disease-risk claims.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "Risk associations described as modest and probabilistic, never deterministic.",
            "No medical guidance implied.",
        ],
        "citations": [CIT_KONG],
    },
    {
        "key": "mutation_rate_var",
        "name": "Why Mutation Rates Vary Across the Genome",
        "group": "Inheritance and Variation",
        "ladder_rank": 11,
        "ladder_tier": "foundations",
        "problem": ("The mutation rate is not one number: CpG sites mutate "
                    "an order of magnitude faster than average, some regions "
                    "are hotspots, others are quiet. What sets the local "
                    "mutation rate, and can we predict it from sequence and "
                    "chromatin alone?"),
        "background": (
            "The textbook human mutation rate, about 1.2 in 100 million per "
            "base per generation, is an average that hides dramatic local "
            "variation. Cytosine-guanine dinucleotides - CpG sites - mutate "
            "roughly ten times faster than average because methylated "
            "cytosine spontaneously deaminates to thymine, a chemical "
            "accident no repair system fully prevents. Beyond CpGs, "
            "mutation rates track replication timing (late-replicating DNA "
            "mutates more), chromatin state, transcription, and proximity "
            "to recombination hotspots. Large trio-sequencing studies now "
            "map de novo mutations by the thousands, confirming the "
            "patterns but also showing residual unpredictability: models "
            "using sequence context plus chromatin features still leave "
            "much variance unexplained. The unsolved problem is a complete "
            "predictive model of the local rate - the mutational weather "
            "map of the genome - and an account of why evolution tolerates "
            "such unevenness."
        ),
        "why_it_matters": (
            "Disease-gene hunting depends on the null expectation: a "
            "mutation looks suspicious only against the local background "
            "rate. A true rate map would sharpen every rare-variant study "
            "and reveal which genomic neighborhoods evolution keeps under "
            "tight repair."
        ),
        "sig_pointer": (
            "The Signature approach proposes a feature-complete rate model "
            "with an explicit unexplained-variance ledger; the full "
            "treatment is in the Signature Edition record, labeled as a "
            "proposed solution."
        ),
        "sig_steps": [
            "Assemble features: sequence context, CpG status, replication timing, chromatin, transcription.",
            "Fit the local rate per megabase from trio de novo catalogs.",
            "Ledger the explained vs unexplained variance explicitly.",
            "Predict that the unexplained share shrinks as single-cell germline data arrives.",
        ],
        "sig_assumptions": {
            "genome_bp": 3200000000,
            "mu_per_bp": 1.2e-08,
            "expected_denovo": 38.4,
            "cpg_fraction": 0.01,
            "cpg_boost": 10.0,
            "cpg_expected_denovo": 3.5229,
        },
        "sig_confirm": [
            "The ledger's unexplained share falls below 20% with single-cell germline features.",
        ],
        "sig_refute": [
            "The unexplained share stays dominant, implying a stochastic floor to mutation.",
        ],
        "sig_scope": (
            "This does not claim the rate is fully predictable today; it "
            "proposes the ledger as the honest measure of progress."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "CpG sites mutate ~10x faster than average, and rates vary with "
            "replication timing and chromatin. This record covers the "
            "uneven mutation landscape from the deamination chemistry "
            "through trio-sequencing maps to the still-missing complete "
            "predictive model. Includes the rate arithmetic and a pointer "
            "to the Signature proposed solution."
        ),
        "key_points": [
            "Average rate ~1.2e-8 per base per generation hides order-of-magnitude local variation.",
            "CpG deamination drives ~10x hypermutability at ~1% of the genome.",
            "Late replication, open chromatin, and transcription all modulate the local rate.",
            "Feature models still leave much variance unexplained.",
            "The local rate map is the null model for all rare-variant disease studies.",
        ],
        "requirements": [
            "Rate numbers with sources.",
            "The CpG chemistry stated plainly.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "No claim of a complete predictive rate model as established.",
        ],
        "citations": [CIT_KONG, CIT_HGP],
    },
    {
        "key": "epigenetic_inheritance",
        "name": "How Much Inheritance Is Epigenetic",
        "group": "Environment and Epigenetics",
        "ladder_rank": 12,
        "ladder_tier": "compounded",
        "problem": ("Beyond the DNA sequence, chemical marks on DNA and "
                    "packaging proteins regulate genes - and some marks "
                    "appear to pass between generations. In mammals, how "
                    "much of what parents transmit is epigenetic rather "
                    "than genetic?"),
        "background": (
            "Epigenetics studies heritable changes in gene activity that do "
            "not alter the DNA sequence: methylation of cytosine, "
            "modifications of histone proteins, and the packaging of "
            "chromosomes. The controversy is transgenerational epigenetic "
            "inheritance - marks surviving from parent to grandchild and "
            "beyond. In plants and worms the evidence is strong; in mammals "
            "it is contested, because mammals run two waves of epigenetic "
            "reprogramming - one in the early embryo, one in developing "
            "germ cells - that erase most methylation marks. The famous "
            "exceptions are imprinted loci, roughly a hundred-plus regions "
            "where the parental origin of the mark is preserved and "
            "essential for development. Studies of famines and exposures "
            "claim multi-generational effects in humans, but separating "
            "true epigenetic inheritance from shared environments, "
            "behavioral transmission, and genetic confounding has proved "
            "extremely difficult. The honest position of the field: "
            "epigenetic inheritance is real in mammals at specific loci, "
            "and its genome-wide extent is unknown."
        ),
        "why_it_matters": (
            "If experiences can mark the genome for generations, it "
            "rewrites the boundary between nature and nurture and opens "
            "entirely new ideas about prevention. If the effect is tiny, "
            "that matters too - it stops the field chasing ghosts."
        ),
        "sig_pointer": (
            "The Signature approach proposes a reprogramming-survival "
            "budget that bounds the maximum epigenetic contribution; the "
            "full treatment is in the Signature Edition record, labeled as "
            "a proposed solution."
        ),
        "sig_steps": [
            "Model the two mammalian reprogramming waves as erasure filters with measured survival rates.",
            "Compute the upper bound on marks surviving both waves genome-wide.",
            "Subtract imprinted loci (the known exceptions) from the bound.",
            "Predict that any claimed transgenerational effect must fit inside the remaining budget.",
        ],
        "sig_assumptions": {
            "erasure_per_wave": 0.999,
            "survival_both_waves": 1e-06,
            "cpg_sites": 28000000,
            "illustrative_survivors": 28.0,
        },
        "sig_confirm": [
            "Claimed transgenerational marks concentrate in the predicted survivor set.",
        ],
        "sig_refute": [
            "Robust multi-generational effects map to fully erased regions, breaking the bound.",
        ],
        "sig_scope": (
            "This does not claim epigenetic inheritance is absent or "
            "present at any level; it proposes the budget as the bound "
            "that claims must respect."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "Can experiences mark the genome for generations? This record "
            "covers transgenerational epigenetic inheritance from plant and "
            "worm evidence through the mammalian reprogramming barrier to "
            "imprinted loci and the contested human studies. Includes the "
            "survival-budget arithmetic and a pointer to the Signature "
            "proposed solution."
        ),
        "key_points": [
            "Epigenetic marks regulate genes without changing DNA sequence.",
            "Mammals erase most marks in two reprogramming waves (embryo and germ cells).",
            "Imprinted loci (~100+) are the proven exceptions where parental marks persist.",
            "Plant and worm evidence is strong; mammalian evidence is contested.",
            "Human multi-generational claims struggle against environmental and genetic confounding.",
        ],
        "requirements": [
            "Fair treatment of both the strong (plants/worms/imprinting) and contested evidence.",
            "No claim that trauma or famine effects are proven epigenetic inheritance.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "Human transgenerational claims described as unproven, not dismissed.",
        ],
        "citations": [CIT_ENCODE, CIT_WADDINGTON],
    },
    {
        "key": "why_sex",
        "name": "Why Sex Exists: The Costliest Unsolved Problem in Genetics",
        "group": "Evolution",
        "ladder_rank": 13,
        "ladder_tier": "compounded",
        "problem": ("Asexual reproduction is twice as efficient: every "
                    "individual bears young, with no males. Yet sex "
                    "dominates the living world. What benefit pays the "
                    "twofold cost of sex?"),
        "background": (
            "Maynard Smith formalized the scandal in 1978: an asexual "
            "female passes all her genes to every offspring, while a "
            "sexual female passes half her genes to half her offspring "
            "(the daughters), because sons do not bear young - the twofold "
            "cost of sex. Any gene for asexuality should therefore sweep "
            "through a sexual population, yet sex is everywhere and "
            "ancient asexual lineages are rare curiosities. The leading "
            "explanations all invoke genetic mixing as the payoff. The Red "
            "Queen hypothesis (Van Valen) says sex helps hosts outrun "
            "parasites by constantly reshuffling defenses. Kondrashov's "
            "mutational deterministic hypothesis says sex purges harmful "
            "mutations more efficiently by bringing them together in the "
            "same unlucky offspring. Others point to faster adaptation in "
            "changing environments. Each has supporting evidence in "
            "particular systems - host-parasite experiments, mutation "
            "accumulation lines - but no single explanation commands "
            "consensus, and the honest answer may be that different "
            "payoffs dominate in different lineages."
        ),
        "why_it_matters": (
            "Sex shapes every genome: recombination rates, mutation "
            "purging, and the maintenance of variation all flow from it. "
            "Understanding its payoff would unify population genetics - "
            "and explain why the living world accepted such an expensive "
            "deal."
        ),
        "sig_pointer": (
            "The Signature approach proposes a payoff ledger that scores "
            "parasite, mutation, and adaptation benefits per lineage; the "
            "full treatment is in the Signature Edition record, labeled as "
            "a proposed solution."
        ),
        "sig_steps": [
            "Write the twofold cost as the baseline every benefit must beat: a 2x fitness hurdle.",
            "Score three payoff ledgers per lineage: parasite pressure, mutation load, environmental change.",
            "Predict that the dominant ledger varies by lineage ecology.",
            "Test by comparing asexuality's rarity against ledger scores across taxa.",
        ],
        "sig_assumptions": {
            "twofold_cost": 2.0,
            "generations": 10,
            "asexual_advantage_10gen": 1024.0,
        },
        "sig_confirm": [
            "Lineages with high parasite pressure and high mutation load retain sex most strictly.",
        ],
        "sig_refute": [
            "No ledger combination predicts sex's distribution better than chance.",
        ],
        "sig_scope": (
            "This does not claim to have solved why sex exists; it "
            "proposes the ledger framework and the cross-taxa test."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "Sex costs a twofold penalty, yet dominates life. This record "
            "covers the scandal from Maynard Smith's formalization through "
            "the Red Queen and mutation-purging hypotheses to the current "
            "no-consensus state. Includes the twofold-cost arithmetic and "
            "a pointer to the Signature proposed solution."
        ),
        "key_points": [
            "The twofold cost of sex: asexual lineages grow ~2x faster, all else equal.",
            "After 10 generations the asexual edge is 1024-fold in the simple model.",
            "Red Queen: sex outruns parasites via reshuffled defenses.",
            "Mutational deterministic: sex purges harmful mutations by concentrating them.",
            "Ancient asexual lineages are rare, but no single payoff explanation has won consensus.",
        ],
        "requirements": [
            "The twofold cost stated quantitatively.",
            "All three leading hypotheses presented without declaring a winner.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "Hypotheses attributed to their authors (Van Valen, Kondrashov, Maynard Smith).",
        ],
        "citations": [CIT_MAYNARD, CIT_KONDRASHOV],
    },
    {
        "key": "lewontin_paradox",
        "name": "Lewontin's Paradox: Too Little Variation for So Many Individuals",
        "group": "Inheritance and Variation",
        "ladder_rank": 14,
        "ladder_tier": "compounded",
        "problem": ("Neutral theory predicts genetic diversity should scale "
                    "with population size, yet humans - 8 billion strong - "
                    "carry barely more variation than far smaller species. "
                    "Why does diversity refuse to scale with census size?"),
        "background": (
            "Under the neutral theory, nucleotide diversity should equal "
            "four times the effective population size times the mutation "
            "rate. Humans show diversity around 0.1 percent - one differing "
            "base per thousand - which implies an effective population size "
            "near 20,000, a tiny fraction of the 8 billion census. Lewontin "
            "flagged the general version in 1974: across species, diversity "
            "varies by barely an order of magnitude while census sizes "
            "span many orders. Proposed resolutions include pervasive "
            "linked selection - selective sweeps and background selection "
            "constantly wiping out nearby neutral variation, capping "
            "diversity regardless of headcount - and demographic turbulence "
            "that keeps effective sizes small. Recent work argues linked "
            "selection can indeed cap diversity, but quantifying exactly "
            "how much of the paradox it explains, in which species, "
            "remains open."
        ),
        "why_it_matters": (
            "Diversity is the fuel of adaptation and the raw material of "
            "breeding and conservation. If linked selection caps it "
            "everywhere, then census size is a poor guide to a species' "
            "evolutionary potential - with direct consequences for "
            "endangered-species management."
        ),
        "sig_pointer": (
            "The Signature approach proposes a linked-selection cap model "
            "that predicts each species' diversity from its recombination "
            "map; the full treatment is in the Signature Edition record, "
            "labeled as a proposed solution."
        ),
        "sig_steps": [
            "Compute the neutral expectation for diversity from census size and mutation rate.",
            "Measure the observed shortfall (the paradox gap).",
            "Model linked selection as a function of the recombination map: low recombination, stronger cap.",
            "Predict each species' diversity from its map and test the prediction.",
        ],
        "sig_assumptions": {
            "nucleotide_diversity": 0.001,
            "mutation_rate": 1.2e-08,
            "implied_Ne": 20833.0,
            "census": 8000000000,
            "census_Ne_ratio": 384000.0,
        },
        "sig_confirm": [
            "Recombination-map predictions match observed diversity across species.",
        ],
        "sig_refute": [
            "High-recombination species still show the cap, implicating demography instead.",
        ],
        "sig_scope": (
            "This does not claim linked selection fully explains the "
            "paradox; it proposes the map-based test."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "Eight billion humans carry barely more genetic diversity than "
            "tiny species. This record covers Lewontin's paradox from the "
            "1974 flag through neutral expectations to the linked-selection "
            "cap hypothesis. Includes the Ne arithmetic (census/Ne ~384,000) "
            "and a pointer to the Signature proposed solution."
        ),
        "key_points": [
            "Human diversity ~0.001 implies effective size ~20,000 vs a census of 8 billion.",
            "Across species, diversity spans ~10x while census sizes span ~1,000,000x or more.",
            "Linked selection (sweeps + background selection) is the leading cap mechanism.",
            "Demographic turbulence is the leading alternative.",
            "How much each force explains, per species, is still unquantified.",
        ],
        "requirements": [
            "The neutral-theory arithmetic shown explicitly.",
            "Both linked selection and demography presented as live options.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "Paradox attributed to Lewontin 1974.",
        ],
        "citations": [CIT_LEWONTIN, CIT_FISHER],
    },
    {
        "key": "balancing_selection",
        "name": "How Much of the Genome Is Balanced on a Knife Edge",
        "group": "Inheritance and Variation",
        "ladder_rank": 15,
        "ladder_tier": "compounded",
        "problem": ("Some harmful alleles are actively maintained by "
                    "selection because heterozygotes gain an advantage - "
                    "the sickle-cell story. How widespread is balancing "
                    "selection across the genome, and how much variation "
                    "does it explain?"),
        "background": (
            "Allison's 1954 demonstration that sickle-cell trait protects "
            "against malaria is the textbook case: the heterozygote "
            "outperforms both homozygotes, so selection holds the harmful "
            "allele at a stable equilibrium - with textbook fitnesses the "
            "equilibrium sits near 15 percent. The immune system's HLA "
            "genes show even more dramatic balancing, with ancient "
            "polymorphisms shared across species. But beyond these "
            "showcases, the genome-wide extent of balancing selection is "
            "genuinely unknown. Genome scans find signatures - regions of "
            "elevated diversity, ancient allele ages - at perhaps hundreds "
            "of loci, yet distinguishing true balancing selection from "
            "relaxed constraint and demographic artifacts is hard, and "
            "estimates range from rare curiosity to a major maintainer of "
            "variation. The problem is measurement: balancing selection is "
            "easy to invoke and hard to prove locus by locus."
        ),
        "why_it_matters": (
            "Balanced polymorphisms are often the variants most relevant "
            "to disease - immune genes, blood groups, metabolic tradeoffs. "
            "A true map of them would highlight the parts of the genome "
            "where variation itself is the adaptation."
        ),
        "sig_pointer": (
            "The Signature approach proposes a triple-signature test "
            "(diversity, allele age, heterozygote fitness) for each "
            "candidate locus; the full treatment is in the Signature "
            "Edition record, labeled as a proposed solution."
        ),
        "sig_steps": [
            "Require three simultaneous signatures: elevated diversity, ancient allele age, and measured heterozygote advantage.",
            "Score every candidate locus on all three; no single signature suffices.",
            "Estimate the genome-wide count from loci passing the triple bar.",
            "Predict the count grows only with better fitness measurements, not with looser statistics.",
        ],
        "sig_assumptions": {
            "w_AA": 0.85,
            "w_AS": 1.0,
            "w_SS": 0.15,
            "equilibrium_q": 0.15,
        },
        "sig_confirm": [
            "Triple-bar loci replicate across populations and show consistent heterozygote fitness edges.",
        ],
        "sig_refute": [
            "Most candidates fail the fitness leg, collapsing the genome-wide count to the known showcases.",
        ],
        "sig_scope": (
            "This does not claim a new genome-wide count; it proposes the "
            "triple bar as the standard of proof."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "Sickle-cell trait versus malaria is the famous case of "
            "selection maintaining a harmful allele. This record covers "
            "balancing selection from Allison 1954 through HLA to the "
            "genuinely unknown genome-wide extent, and why the phenomenon "
            "is easy to invoke but hard to prove. Includes the equilibrium "
            "arithmetic and a pointer to the Signature proposed solution."
        ),
        "key_points": [
            "Heterozygote advantage holds the sickle allele near 15% equilibrium in the textbook model.",
            "HLA immune genes show the most dramatic balancing signatures.",
            "Genome scans suggest hundreds of candidates, but proof is thin beyond showcases.",
            "Elevated diversity alone does not prove balancing selection.",
            "The true genome-wide count remains unmeasured.",
        ],
        "requirements": [
            "The equilibrium calculation shown explicitly.",
            "Clear line between proven cases and scan candidates.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "Sickle-cell/malaria attributed to Allison 1954.",
        ],
        "citations": [CIT_ALLISON, CIT_FISHER],
    },
    {
        "key": "canalization",
        "name": "Canalization: How Development Buffers Genetic Chaos",
        "group": "Environment and Epigenetics",
        "ladder_rank": 16,
        "ladder_tier": "compounded",
        "problem": ("Development produces reliable bodies from noisy genes "
                    "and noisy environments - Waddington's canalization. "
                    "What are the molecular mechanisms of this buffering, "
                    "and how much genetic variation is hidden by it?"),
        "background": (
            "Waddington proposed in 1942 that development is canalized: "
            "like a ball rolling down a grooved landscape, the embryo "
            "returns to its track after perturbations, so genetic and "
            "environmental noise leave little mark on the final form. "
            "Modern biology has found pieces of the machinery: heat-shock "
            "chaperone proteins like Hsp90 that mask the effects of "
            "mutations until stress reveals them, redundant gene duplicates "
            "that cover for each other's failures, microRNAs that tune "
            "expression noise, and network motifs that filter fluctuations. "
            "Experiments show that disabling buffers releases hidden "
            "variation - the same genome suddenly produces diverse forms. "
            "The unsolved problem is the full inventory and the "
            "quantification: which buffers matter most, how much variation "
            "each hides, and whether buffering itself evolves - because a "
            "population storing hidden variation can adapt explosively "
            "when the environment shifts and the buffers drop."
        ),
        "why_it_matters": (
            "Hidden variation is evolution's savings account and medicine's "
            "blind spot: buffered mutations can surface as disease when "
            "buffers fail with age or stress. Mapping the buffers would "
            "reveal how much of the genome is silently loaded."
        ),
        "sig_pointer": (
            "The Signature approach proposes a buffer-knockout atlas that "
            "ranks buffers by released variation; the full treatment is in "
            "the Signature Edition record, labeled as a proposed solution."
        ),
        "sig_steps": [
            "List candidate buffers: chaperones, duplicates, microRNAs, network motifs.",
            "Disable each buffer in turn and measure the released phenotypic variance.",
            "Rank buffers by the variance they were hiding.",
            "Predict that top-ranked buffers are the most conserved across species.",
        ],
        "sig_assumptions": {
            "liability_threshold": 2.0,
            "unbuffered_variance": 1.0,
            "buffered_variance": 0.5,
            "p_unbuffered": 0.0228,
            "p_buffered": 0.00234,
        },
        "sig_confirm": [
            "Released-variance rankings replicate across tissues and species.",
        ],
        "sig_refute": [
            "No single buffer's removal releases more than noise-level variance.",
        ],
        "sig_scope": (
            "This does not claim a complete buffer inventory; it proposes "
            "the knockout-ranking method."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "Embryos build reliable bodies from noisy instructions. This "
            "record covers canalization from Waddington's 1942 landscape "
            "through Hsp90 and redundancy to the modern hunt for the full "
            "buffer inventory. Includes a threshold-model calculation of "
            "how buffering hides variation and a pointer to the Signature "
            "proposed solution."
        ),
        "key_points": [
            "Waddington (1942): development is canalized like a ball in a grooved landscape.",
            "Hsp90 chaperones mask mutations until stress reveals them.",
            "Gene duplicates, microRNAs, and network motifs add further buffering layers.",
            "Disabling buffers releases hidden, heritable variation.",
            "The full ranked inventory of buffers is still missing.",
        ],
        "requirements": [
            "The threshold arithmetic shown explicitly.",
            "Buffers described as partially mapped, not solved.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "Canalization attributed to Waddington 1942.",
        ],
        "citations": [CIT_WADDINGTON, CIT_FISHER],
    },
    {
        "key": "pleiotropy",
        "name": "Pleiotropy: Why One Gene Wears Many Hats",
        "group": "Regulation and Expression",
        "ladder_rank": 17,
        "ladder_tier": "compounded",
        "problem": ("Most genes affect multiple traits - pleiotropy is the "
                    "rule, not the exception. Why is it so universal, and "
                    "what does it imply for evolution and for treating "
                    "genetic disease without side effects?"),
        "background": (
            "Fisher's 1930 geometric model made the logic stark: as an "
            "organism's traits multiply, a random mutation is ever more "
            "likely to disturb something, because each gene's product "
            "participates in many processes. Modern data confirmed the "
            "ubiquity: genome-wide studies find most trait-associated "
            "variants touching multiple traits, and gene knockouts "
            "routinely produce syndromes of effects rather than single "
            "defects. The unsolved questions are quantitative and "
            "structural: what is the true distribution of pleiotropic "
            "effect sizes, how much pleiotropy is modular (one gene, "
            "separate jobs in separate tissues) versus genuinely entangled, "
            "and does pleiotropy mostly constrain adaptation - as Fisher "
            "argued - or mostly enable it by letting one mutation move "
            "many traits at once? For medicine the stakes are direct: a "
            "drug target with wide pleiotropy is a drug with side effects."
        ),
        "why_it_matters": (
            "Pleiotropy sets the side-effect profile of every genetic "
            "therapy: fixing one trait through a pleiotropic gene moves "
            "others. Understanding its structure would let us pick targets "
            "with narrow, modular effects."
        ),
        "sig_pointer": (
            "The Signature approach proposes a modularity map that scores "
            "each gene's pleiotropy as entangled or tissue-modular; the "
            "full treatment is in the Signature Edition record, labeled as "
            "a proposed solution."
        ),
        "sig_steps": [
            "For each gene, catalog its trait associations across studies.",
            "Score modularity: do the effects separate by tissue and timing, or co-occur inseparably?",
            "Predict that modular genes are safer therapeutic targets than entangled ones.",
            "Test the prediction against known drug side-effect profiles.",
        ],
        "sig_assumptions": {
            "n_traits": 10,
            "per_trait_probability": 0.10,
            "p_touches_any": 0.6513,
        },
        "sig_confirm": [
            "Modularity scores predict side-effect breadth in independent drug data.",
        ],
        "sig_refute": [
            "Side effects track expression breadth alone, with no added signal from modularity.",
        ],
        "sig_scope": (
            "This does not claim pleiotropy is fully mapped; it proposes "
            "the modularity score and its therapeutic test."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "One gene, many traits: pleiotropy is everywhere. This record "
            "covers the phenomenon from Fisher's 1930 geometric model "
            "through modern multi-trait GWAS hits to the open questions of "
            "modularity versus entanglement. Includes the probability "
            "arithmetic and a pointer to the Signature proposed solution."
        ),
        "key_points": [
            "Fisher (1930): more traits means random mutations more likely disturb something.",
            "Most trait-associated variants affect multiple traits.",
            "Knockouts typically yield syndromes of effects, not single defects.",
            "Modular pleiotropy (separate jobs per tissue) differs sharply from entangled pleiotropy.",
            "The distinction decides the side-effect profile of genetic therapies.",
        ],
        "requirements": [
            "Fisher's argument stated fairly.",
            "No claim that pleiotropy's structure is solved.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "Geometric model attributed to Fisher 1930.",
        ],
        "citations": [CIT_FISHER, CIT_OMNI],
    },
    {
        "key": "grn",
        "name": "Reconstructing the Gene Regulatory Network",
        "group": "Regulation and Expression",
        "ladder_rank": 18,
        "ladder_tier": "compounded",
        "problem": ("Every cell runs a program written in gene regulation: "
                    "which genes turn on which others, when, and how "
                    "strongly. Can we reconstruct the complete gene "
                    "regulatory network of even one cell type?"),
        "background": (
            "Kauffman's 1969 Boolean network models gave the field its "
            "founding abstraction: genes as on/off switches wired "
            "together, with the network's stable states corresponding to "
            "cell types. Half a century later we have the parts in "
            "unprecedented detail - transcription factor binding maps, "
            "chromatin accessibility, single-cell expression for millions "
            "of cells - yet the complete wiring diagram of any mammalian "
            "cell type remains out of reach. The obstacles are "
            "combinatorial and causal: a three-gene Boolean network already "
            "admits 8 states and over 16 million possible wirings, and "
            "real networks have thousands of genes; worse, correlation in "
            "expression data does not reveal who regulates whom, and "
            "perturbation experiments scale poorly. Inference algorithms "
            "proliferate, benchmarks disagree, and the field still lacks a "
            "gold-standard complete network to validate against."
        ),
        "why_it_matters": (
            "The regulatory network is the cell's operating system: "
            "reprogramming cells, directing stem cells, and understanding "
            "cancer all require the wiring diagram. A validated complete "
            "network for one cell type would be a landmark for all of "
            "biology."
        ),
        "sig_pointer": (
            "The Signature approach proposes a perturbation-first "
            "reconstruction protocol with a combinatorial budget; the full "
            "treatment is in the Signature Edition record, labeled as a "
            "proposed solution."
        ),
        "sig_steps": [
            "Budget the combinatorial space explicitly: states and wirings for the target gene set.",
            "Prioritize perturbations by expected information gain, not by convenience.",
            "Reconstruct iteratively: infer, perturb the most uncertain edges, re-infer.",
            "Validate against held-out perturbation outcomes, never against correlation alone.",
        ],
        "sig_assumptions": {
            "toy_genes": 3,
            "toy_states": 8,
            "toy_functions_per_gene": 256,
            "toy_networks": 16777216,
        },
        "sig_confirm": [
            "Iterative perturbation closes the edge-uncertainty budget for a small module.",
        ],
        "sig_refute": [
            "Perturbation outcomes stay unpredictable even for fully mapped small modules.",
        ],
        "sig_scope": (
            "This does not claim a complete network exists or is near; it "
            "proposes the budgeted protocol."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "The cell's operating system is its gene regulatory network, "
            "and no complete mammalian wiring diagram exists. This record "
            "covers the reconstruction problem from Kauffman's 1969 Boolean "
            "nets through single-cell data to the combinatorial and causal "
            "barriers. Includes the state-space arithmetic and a pointer to "
            "the Signature proposed solution."
        ),
        "key_points": [
            "Kauffman (1969) founded the field with Boolean network models of regulation.",
            "A 3-gene Boolean network has 8 states and 16,777,216 possible wirings.",
            "Correlation in expression data does not reveal regulatory causation.",
            "Perturbation experiments are the gold standard but scale poorly.",
            "No complete validated mammalian network exists for any cell type.",
        ],
        "requirements": [
            "The combinatorial arithmetic shown explicitly.",
            "Correlation-vs-causation stated as the core barrier.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "Boolean network origin attributed to Kauffman 1969.",
        ],
        "citations": [CIT_KAUFFMAN, CIT_ENCODE],
    },
    {
        "key": "splicing",
        "name": "Cracking the Splicing Code",
        "group": "Regulation and Expression",
        "ladder_rank": 19,
        "ladder_tier": "compounded",
        "problem": ("One gene can produce ten or more different proteins "
                    "through alternative splicing, and about 95 percent of "
                    "human multi-exon genes are spliced alternatively. Can "
                    "we predict the full set of a gene's messages from its "
                    "sequence?"),
        "background": (
            "Splicing edits the RNA message after transcription: introns "
            "are cut out, exons are joined, and alternative choices of "
            "exons multiply one gene into many proteins. Deep sequencing "
            "revealed the scale - around 95 percent of human multi-exon "
            "genes produce alternative isoforms, averaging roughly ten "
            "transcripts per gene. The regulatory code is written in "
            "splice-site sequences plus the binding sites of splicing "
            "factors, and it is tissue-specific: brain, muscle, and liver "
            "splice the same genes differently. Predictive models have "
            "improved enormously, some predicting splicing effects of "
            "variants with high accuracy, yet the full code - every "
            "isoform, every tissue, every developmental stage, from "
            "sequence alone - is not cracked. Splicing errors cause a "
            "large share of Mendelian disease, so the missing code has "
            "direct diagnostic stakes."
        ),
        "why_it_matters": (
            "A large fraction of disease-causing mutations act by breaking "
            "splicing, and current diagnostics miss many of them. A "
            "complete splicing code would turn every genome sequence into "
            "a readable set of protein messages."
        ),
        "sig_pointer": (
            "The Signature approach proposes a tissue-factored splicing "
            "model trained on the isoform census; the full treatment is in "
            "the Signature Edition record, labeled as a proposed solution."
        ),
        "sig_steps": [
            "Census the isoforms: ~200,000 transcripts from ~20,000 genes as the prediction target.",
            "Factor the model by tissue: sequence features times tissue-specific factor concentrations.",
            "Predict held-out tissues' splicing from sequence plus factor profiles.",
            "Score the code cracked only when cross-tissue predictions match observation.",
        ],
        "sig_assumptions": {
            "genes": 20000,
            "transcripts": 200000,
            "isoforms_per_gene": 10.0,
            "alt_spliced_fraction": 0.95,
        },
        "sig_confirm": [
            "Cross-tissue predictions reach diagnostic-grade accuracy.",
        ],
        "sig_refute": [
            "Accuracy plateaus far below diagnostic grade despite complete data.",
        ],
        "sig_scope": (
            "This does not claim the code is cracked; it proposes the "
            "census-factored test."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "One gene, ~10 messages: alternative splicing multiplies the "
            "genome's output. This record covers the splicing code from "
            "the 95%-of-genes discovery through tissue-specific regulation "
            "to the predictive models and their limits. Includes the "
            "isoform arithmetic and a pointer to the Signature proposed "
            "solution."
        ),
        "key_points": [
            "~95% of human multi-exon genes are alternatively spliced (Pan et al. 2008).",
            "~200,000 transcripts from ~20,000 genes: roughly 10 isoforms per gene.",
            "Splicing is tissue-specific: brain, muscle, and liver read the same genes differently.",
            "Predictive models are improving but the full code is not cracked.",
            "Splicing errors underlie many Mendelian disorders.",
        ],
        "requirements": [
            "The 95% / 10-per-gene numbers with sources.",
            "Tissue specificity stated as a core difficulty.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "Alternative-splicing prevalence attributed to the transcriptome sequencing literature.",
        ],
        "citations": [CIT_PAN, CIT_GENCODE],
    },
    {
        "key": "lncrna",
        "name": "The Long Non-Coding RNA Dark Matter",
        "group": "Regulation and Expression",
        "ladder_rank": 20,
        "ladder_tier": "compounded",
        "problem": ("The genome is transcribed into tens of thousands of "
                    "long non-coding RNAs, yet only a small fraction have "
                    "an established function. What are the rest doing - "
                    "and how do we tell functional lncRNAs from "
                    "transcriptional noise?"),
        "background": (
            "Long non-coding RNAs - transcripts longer than 200 bases that "
            "do not code for protein - went from curiosities to a crowd: "
            "GENCODE annotates roughly 19,000 lncRNA genes in human, "
            "comparable to the protein-coding count. A few are famous and "
            "functional: XIST silences an entire X chromosome, HOTAIR "
            "scaffolds chromatin complexes. But the vast majority have no "
            "assigned function, are expressed at low levels, evolve "
            "rapidly, and vanish in knockout experiments without obvious "
            "effect - the classic signature, skeptics say, of noise. "
            "Defenders reply that low expression and rapid evolution are "
            "expected for regulatory RNAs, and that subtle phenotypes need "
            "better assays. The field's unsolved problem is a decision "
            "procedure: a principled, scalable way to sort the functional "
            "minority from the transcriptional background, since testing "
            "19,000 candidates one by one is not feasible."
        ),
        "why_it_matters": (
            "If even a tenth of lncRNAs are functional regulators, they "
            "are a vast untapped layer of biology - and of drug targets. "
            "If most are noise, the field needs to know so it stops "
            "chasing shadows."
        ),
        "sig_pointer": (
            "The Signature approach proposes a functional-triage score "
            "combining structure, binding, and perturbation data; the full "
            "treatment is in the Signature Edition record, labeled as a "
            "proposed solution."
        ),
        "sig_steps": [
            "Score every annotated lncRNA on conserved structure, protein binding, and chromatin association.",
            "Rank candidates and perturb the top tier systematically.",
            "Define functional by reproducible molecular or organismal phenotype.",
            "Estimate the functional fraction from the top tier's hit rate, extrapolated honestly.",
        ],
        "sig_assumptions": {
            "lncrna_genes": 19000,
            "with_established_function": 500,
            "functional_fraction": 0.0263,
        },
        "sig_confirm": [
            "Top-tier perturbation hit rates extrapolate to a substantial functional minority.",
        ],
        "sig_refute": [
            "Even top-tier candidates mostly show no phenotype, shrinking the functional set toward zero.",
        ],
        "sig_scope": (
            "This does not claim any specific lncRNA is functional; it "
            "proposes the triage procedure."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "Some 19,000 long non-coding RNAs are annotated in human, but "
            "only hundreds have known functions. This record covers the "
            "lncRNA dark matter from XIST and HOTAIR through the noise "
            "debate to the missing decision procedure. Includes the "
            "fraction arithmetic and a pointer to the Signature proposed "
            "solution."
        ),
        "key_points": [
            "GENCODE annotates ~19,000 lncRNA genes in human.",
            "XIST and HOTAIR prove the class can be deeply functional.",
            "Most lncRNAs are lowly expressed, fast-evolving, and knockout-quiet.",
            "Low expression and rapid evolution are consistent with either regulation or noise.",
            "No scalable decision procedure yet separates the two.",
        ],
        "requirements": [
            "Both the functional examples and the noise evidence presented fairly.",
            "No claim about the true functional fraction as established.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "Annotation counts attributed to GENCODE.",
        ],
        "citations": [CIT_GENCODE, CIT_ENCODE],
    },
    {
        "key": "protein_function",
        "name": "From Structure to Function: The Post-AlphaFold Problem",
        "group": "Regulation and Expression",
        "ladder_rank": 21,
        "ladder_tier": "compounded",
        "problem": ("AlphaFold predicts protein structures with remarkable "
                    "accuracy, yet a structure is not a function. With "
                    "hundreds of millions of known protein sequences and a "
                    "tiny fraction experimentally characterized, how do we "
                    "predict what a protein actually does?"),
        "background": (
            "Jumper and colleagues' AlphaFold (2021) largely solved the "
            "fifty-year problem of predicting a protein's 3D shape from "
            "its amino-acid sequence, and structure databases now hold "
            "predicted shapes for essentially every known protein. But "
            "function - what the protein binds, what reaction it catalyzes, "
            "which pathway it serves - remains a separate, harder "
            "inference. The scale mismatch is stark: UniProt holds on the "
            "order of 250 million protein sequences while the Protein Data "
            "Bank holds roughly 200,000 experimental structures, a coverage "
            "near 0.08 percent, and experimentally verified functions cover "
            "an even smaller slice. Homology transfer (it looks like a "
            "kinase, so it is a kinase) works until it does not - "
            "moonlighting proteins and subtle active-site changes defeat "
            "it. The unsolved problem is function prediction at the scale "
            "of the sequence universe, with calibrated uncertainty."
        ),
        "why_it_matters": (
            "Every uncharacterized protein is a potential drug target, "
            "enzyme, or disease mechanism sitting in the dark. Closing the "
            "function gap would light up the majority of the protein "
            "universe at once."
        ),
        "sig_pointer": (
            "The Signature approach proposes a function-evidence graph "
            "that propagates annotations with uncertainty; the full "
            "treatment is in the Signature Edition record, labeled as a "
            "proposed solution."
        ),
        "sig_steps": [
            "Build a graph linking sequences by structure, genomic context, and interaction data.",
            "Propagate experimentally verified functions along graph edges with decay by distance.",
            "Attach a calibrated confidence to every propagated annotation.",
            "Validate by hiding known functions and measuring recovery.",
        ],
        "sig_assumptions": {
            "experimental_structures": 200000,
            "known_sequences": 250000000,
            "structural_coverage": 0.0008,
        },
        "sig_confirm": [
            "Hidden-function recovery beats homology-only baselines at matched confidence.",
        ],
        "sig_refute": [
            "Propagation adds nothing beyond nearest-homolog transfer.",
        ],
        "sig_scope": (
            "This does not claim functions can be predicted reliably "
            "today; it proposes the graph and the recovery benchmark."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "AlphaFold solved structure prediction, but structure is not "
            "function. This record covers the post-AlphaFold problem from "
            "the 2021 breakthrough through the 250M-sequence vs 200K-"
            "structure gap to the limits of homology transfer. Includes "
            "the coverage arithmetic and a pointer to the Signature "
            "proposed solution."
        ),
        "key_points": [
            "AlphaFold (2021) predicts protein structures from sequence with remarkable accuracy.",
            "~250 million known sequences vs ~200,000 experimental structures: ~0.08% coverage.",
            "Experimentally verified functions cover an even smaller fraction.",
            "Homology transfer fails for moonlighting proteins and subtle active-site changes.",
            "Function prediction needs calibrated uncertainty, not just best guesses.",
        ],
        "requirements": [
            "The coverage arithmetic shown explicitly.",
            "AlphaFold's achievement credited without overstating it.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "Structure prediction breakthrough attributed to Jumper et al. 2021.",
        ],
        "citations": [CIT_ALPHAFOLD, CIT_GENCODE],
    },
    {
        "key": "mitonuclear",
        "name": "Two Genomes, One Cell: The Mito-Nuclear Conversation",
        "group": "Regulation and Expression",
        "ladder_rank": 22,
        "ladder_tier": "compounded",
        "problem": ("Mitochondria carry their own tiny genome, but roughly "
                    "1,500 of their proteins are encoded in the nucleus. "
                    "How do two genomes with different mutation rates and "
                    "inheritance rules stay coordinated - and what happens "
                    "when they mismatch?"),
        "background": (
            "Mitochondria descend from an ancient bacterial endosymbiont, "
            "and most of its genes migrated to the nucleus long ago: human "
            "mitochondrial DNA encodes just 13 proteins, while about 1,500 "
            "nuclear-encoded proteins are imported into the organelle. The "
            "two genomes must cooperate intimately - respiratory complexes "
            "are built from subunits encoded on both sides - yet animal "
            "mitochondrial DNA mutates roughly ten times faster than "
            "nuclear DNA and is inherited maternally, so the partners "
            "evolve at different speeds under different rules. Experiments "
            "swapping mitochondrial genomes between strains reveal "
            "mito-nuclear incompatibilities: mismatched combinations show "
            "metabolic defects, fertility drops, and shortened lifespan. "
            "The unsolved problem is the full set of coordination rules: "
            "how the nucleus monitors and compensates for mitochondrial "
            "change, and where the mismatch boundaries lie between "
            "populations and species."
        ),
        "why_it_matters": (
            "Mitochondrial replacement techniques and the genetics of "
            "metabolic disease both hinge on mito-nuclear compatibility. "
            "Mapping the mismatch boundaries would define safe donor "
            "matching and explain a class of unexplained infertility."
        ),
        "sig_pointer": (
            "The Signature approach proposes a co-evolution compatibility "
            "score for any mito-nuclear pair; the full treatment is in the "
            "Signature Edition record, labeled as a proposed solution."
        ),
        "sig_steps": [
            "Catalog interacting mito-nuclear protein pairs (respiratory complexes first).",
            "Score co-evolution: correlated substitution rates across species.",
            "Predict incompatibility from divergence at high-score interfaces.",
            "Test predictions in cybrid cell lines carrying mismatched combinations.",
        ],
        "sig_assumptions": {
            "mtdna_proteins": 13,
            "nuclear_mito_proteins": 1500,
            "mtdna_rate_multiple": 10.0,
            "human_chimp_nuclear_divergence": 0.012,
            "naive_mtdna_divergence": 0.12,
        },
        "sig_confirm": [
            "Compatibility scores predict cybrid metabolic performance.",
        ],
        "sig_refute": [
            "Mismatched combinations perform identically, implying full nuclear compensation.",
        ],
        "sig_scope": (
            "This does not claim to predict clinical outcomes; it proposes "
            "the compatibility score and its cell-line test."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "Each cell runs on two genomes: 13 mitochondrial proteins plus "
            "~1,500 nuclear-encoded ones, evolving at different speeds. "
            "This record covers mito-nuclear coordination from the "
            "endosymbiont origin through incompatibility experiments to "
            "the missing compatibility map. Includes the divergence "
            "arithmetic and a pointer to the Signature proposed solution."
        ),
        "key_points": [
            "Human mtDNA encodes 13 proteins; ~1,500 mitochondrial proteins come from the nucleus.",
            "Animal mtDNA mutates ~10x faster than nuclear DNA and is maternally inherited.",
            "Swapped mito-nuclear combinations show metabolic and fertility defects.",
            "The nucleus must monitor and compensate for fast mitochondrial change.",
            "Mismatch boundaries between populations and species are unmapped.",
        ],
        "requirements": [
            "The 13 / 1,500 / 10x numbers stated.",
            "Incompatibility evidence described without clinical overreach.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "No medical claims about mitochondrial replacement outcomes.",
        ],
        "citations": [CIT_HGP, CIT_KONG],
    },
    {
        "key": "telomere",
        "name": "Telomeres: The Aging-Cancer Tradeoff Written in Chromosome Ends",
        "group": "Regulation and Expression",
        "ladder_rank": 23,
        "ladder_tier": "compounded",
        "problem": ("Chromosome ends shorten with each cell division, "
                    "limiting how many times a cell can divide - yet "
                    "lengthening them invites cancer. What sets the "
                    "telomere balance, and is the tradeoff escapable?"),
        "background": (
            "Hayflick and Moorhead showed in 1961 that normal human cells "
            "divide only about 40 to 60 times before stopping - the "
            "Hayflick limit - and telomeres, the protective caps on "
            "chromosome ends, are the counting mechanism: each division "
            "loses on the order of 50 to 200 base pairs. The enzyme "
            "telomerase can rebuild the caps and is active in stem cells "
            "and germ cells, but most adult cells keep it off. The reason "
            "looks like a bargain with cancer: unlimited division is "
            "exactly what a tumor needs, so short telomeres and silent "
            "telomerase act as a tumor-suppressor system, at the price of "
            "aging tissues that cannot renew forever. The unsolved problem "
            "is whether the tradeoff can be tuned - telomere biology "
            "disorders show what happens when the system breaks short, "
            "while most cancers reactivate telomerase to break it long - "
            "and what the optimal set point is for a long-lived mammal."
        ),
        "why_it_matters": (
            "The telomere tradeoff sits at the center of aging and cancer, "
            "the two great biological challenges of long life. Any "
            "intervention touching one side moves the other; understanding "
            "the set point is prerequisite to touching either safely."
        ),
        "sig_pointer": (
            "The Signature approach proposes a tradeoff-optimization model "
            "for telomere set points across mammals; the full treatment is "
            "in the Signature Edition record, labeled as a proposed "
            "solution."
        ),
        "sig_steps": [
            "Model telomere length as an optimizer balancing renewal capacity against cancer risk.",
            "Parameterize per species: body size, lifespan, and division demand.",
            "Predict each mammal's set point from its life-history parameters.",
            "Test against measured telomere lengths across species.",
        ],
        "sig_assumptions": {
            "hayflick_divisions": 60,
            "loss_per_division_bp": 100,
            "total_loss_bp": 6000,
            "start_bp": 10000,
            "end_bp": 4000,
        },
        "sig_confirm": [
            "Life-history parameters predict telomere set points across mammals.",
        ],
        "sig_refute": [
            "Set points scatter independently of lifespan and body size.",
        ],
        "sig_scope": (
            "This does not claim telomere extension is safe or desirable; "
            "it proposes the optimization model."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "Telomeres count cell divisions toward the Hayflick limit, "
            "trading renewal against cancer risk. This record covers the "
            "telomere tradeoff from 1961 through telomerase to the "
            "disorders of too-short and the cancers of too-long. Includes "
            "the shortening arithmetic and a pointer to the Signature "
            "proposed solution."
        ),
        "key_points": [
            "Hayflick limit: ~40-60 divisions for normal human cells.",
            "Each division costs ~50-200 bp of telomere.",
            "Telomerase rebuilds caps but is silenced in most adult cells.",
            "Short telomeres suppress tumors at the price of aging; cancers reactivate telomerase.",
            "The optimal set point for a long-lived mammal is unknown.",
        ],
        "requirements": [
            "The Hayflick and loss-per-division numbers with sources.",
            "No anti-aging or cancer-treatment claims.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "Tradeoff described as a hypothesis with evidence, not as proven optimality.",
        ],
        "citations": [CIT_HAYFLICK],
    },
    {
        "key": "karyotype",
        "name": "Why Chromosome Numbers Vary So Wildly",
        "group": "Genome Structure and Size",
        "ladder_rank": 24,
        "ladder_tier": "advanced",
        "problem": ("Humans have 46 chromosomes, chimpanzees 48, the Indian "
                    "muntjac deer as few as 6 or 7 - with similar gene "
                    "content. What drives chromosome number up and down, "
                    "and how much does the packaging matter?"),
        "background": (
            "Chromosome number is among the most variable traits in "
            "biology: ferns exceed a thousand, the muntjac deer manages "
            "with 6 or 7, and humans sit at 46 while our closest relatives "
            "carry 48 - the difference explained by the fusion of two "
            "ancestral ape chromosomes into human chromosome 2, confirmed "
            "by Ijdo and colleagues in 1991 via telomere sequences buried "
            "at the fusion site. Fusions and fissions reshuffle the "
            "packaging without much changing the gene list, yet chromosome "
            "rearrangements can drive speciation by scrambling meiosis in "
            "hybrids. The unsolved problem is the dynamics: what sets the "
            "rate of fusions and fissions, why some lineages are "
            "karyotypically frozen for tens of millions of years while "
            "others churn, and how much of adaptation versus accident "
            "each rearrangement represents."
        ),
        "why_it_matters": (
            "Chromosome rearrangements are engines of speciation and a "
            "frequent feature of cancers and infertility. Understanding "
            "their dynamics would clarify how new species form and why "
            "some genomes are structurally stable while others are not."
        ),
        "sig_pointer": (
            "The Signature approach proposes a fusion-fission rate model "
            "tied to centromere and telomere architecture; the full "
            "treatment is in the Signature Edition record, labeled as a "
            "proposed solution."
        ),
        "sig_steps": [
            "Catalog fusion and fission events across sequenced mammals with breakpoint architecture.",
            "Correlate event rates with centromere repeat content and telomere dynamics.",
            "Predict each lineage's karyotype volatility from its architecture.",
            "Test against lineages that froze versus lineages that churned.",
        ],
        "sig_assumptions": {
            "human_chromosomes": 46,
            "chimp_chromosomes": 48,
            "implied_fusions": 1,
            "muntjac_chromosomes": 7,
        },
        "sig_confirm": [
            "Architecture predicts volatility across independent lineages.",
        ],
        "sig_refute": [
            "Volatility shows no architectural correlate, implicating pure drift.",
        ],
        "sig_scope": (
            "This does not claim rearrangements are adaptive; it proposes "
            "the rate model."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "From 46 human chromosomes to a deer's 6, packaging varies "
            "wildly with similar gene content. This record covers karyotype "
            "evolution from the human chromosome 2 fusion through "
            "speciation effects to the unsolved dynamics of fusion and "
            "fission rates. Includes the fusion arithmetic and a pointer "
            "to the Signature proposed solution."
        ),
        "key_points": [
            "Human 46 vs chimpanzee 48: one telomere-telomere fusion (Ijdo et al. 1991).",
            "Indian muntjac: 6-7 chromosomes; some ferns: over 1,000.",
            "Rearrangements reshuffle packaging with little gene-content change.",
            "Rearrangements can drive speciation via hybrid meiosis failure.",
            "What sets fusion/fission rates per lineage is unknown.",
        ],
        "requirements": [
            "The chromosome-2 fusion evidence described accurately.",
            "Dynamics stated as the open question.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "Fusion claim attributed to the telomere-sequence evidence.",
        ],
        "citations": [CIT_CHR2, CIT_HGP],
    },
    {
        "key": "hgt",
        "name": "Horizontal Gene Transfer in Complex Organisms",
        "group": "Evolution",
        "ladder_rank": 25,
        "ladder_tier": "advanced",
        "problem": ("Bacteria swap genes freely, but how much horizontal "
                    "gene transfer shapes complex animals and plants - and "
                    "the human genome in particular?"),
        "background": (
            "Horizontal gene transfer - DNA moving between organisms "
            "outside parent-to-offspring inheritance - is routine in "
            "bacteria and a major force in their evolution. In complex "
            "eukaryotes the picture is murkier. The human genome's largest "
            "foreign contribution is viral: about 8 percent derives from "
            "endogenous retroviruses, ancient infections fossilized in "
            "our DNA (Lander et al. 2001). Claims of extensive "
            "bacterium-to-human transfers made headlines and then largely "
            "collapsed under scrutiny as contamination and annotation "
            "artifacts. Genuine cases exist - tardigrades, rotifers, and "
            "some insects carry confirmed foreign genes - but in "
            "vertebrates, well-supported transfers are rare. The unsolved "
            "problem is the true rate and significance: a complete, "
            "contamination-proof census of horizontal transfers in complex "
            "genomes, and whether any of them mattered functionally."
        ),
        "why_it_matters": (
            "If foreign genes contributed functional innovations to "
            "animals, textbooks on where our genes come from need "
            "rewriting. A clean census also sets the false-positive bar "
            "for every future claim."
        ),
        "sig_pointer": (
            "The Signature approach proposes a contamination-proof "
            "transfer census protocol; the full treatment is in the "
            "Signature Edition record, labeled as a proposed solution."
        ),
        "sig_steps": [
            "Require physical linkage: candidate foreign genes must sit on long native contigs.",
            "Require phylogenetic incongruence plus synteny evidence.",
            "Apply the protocol uniformly across sequenced vertebrates.",
            "Score survivors by functional evidence: expression, knockout phenotype.",
        ],
        "sig_assumptions": {
            "genome_bp": 3200000000,
            "erv_fraction": 0.08,
            "erv_bp": 256000000.0,
        },
        "sig_confirm": [
            "The protocol recovers known transfers and finds a stable, small set of new ones.",
        ],
        "sig_refute": [
            "Nearly all candidates fail the linkage bar, shrinking the census toward zero.",
        ],
        "sig_scope": (
            "This does not claim any particular transfer is real; it "
            "proposes the census standard."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "Bacteria trade genes freely; do we? This record covers "
            "horizontal transfer from bacterial ubiquity through the 8% "
            "viral fossil record in humans to the collapsed "
            "bacterium-to-human claims and the missing contamination-proof "
            "census. Includes the ERV arithmetic and a pointer to the "
            "Signature proposed solution."
        ),
        "key_points": [
            "~8% of the human genome derives from endogenous retroviruses.",
            "Early bacterium-to-human transfer claims largely collapsed as contamination.",
            "Confirmed transfers exist in tardigrades, rotifers, and some insects.",
            "Well-supported vertebrate transfers are rare.",
            "A uniform contamination-proof census is still missing.",
        ],
        "requirements": [
            "The 8% ERV figure with source.",
            "Collapsed claims described accurately, not mocked.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "Transfer claims held to the stated evidence bar.",
        ],
        "citations": [CIT_HGP],
    },
    {
        "key": "behavior_genetics",
        "name": "The Genetic Architecture of Behavior and Cognition",
        "group": "Health, Behavior, and Prediction",
        "ladder_rank": 26,
        "ladder_tier": "advanced",
        "problem": ("Twin studies find behavior and cognition substantially "
                    "heritable - yet the specific genetic architecture "
                    "behind traits like intelligence remains largely "
                    "unmapped. What is the true architecture, and what are "
                    "its limits?"),
        "background": (
            "Fifty years of twin studies, meta-analyzed by Polderman and "
            "colleagues in 2015, put the average heritability of human "
            "traits near 50 percent, with cognitive abilities among the "
            "most heritable - twin correlations for intelligence imply "
            "heritabilities around one-half by Falconer's formula, rising "
            "with age in the well-replicated Wilson effect. Yet the "
            "variant-level architecture is diffuse: thousands of tiny "
            "effects, no large single contributors, and prediction scores "
            "that capture only a slice of the twin-study share. The "
            "unsolved problems are the architecture's fine structure - how "
            "many variants, what effect-size distribution, what roles for "
            "rare variants and interactions - and the interpretation "
            "limits: heritability describes populations, not individuals, "
            "and says nothing about immutability. The field's hardest "
            "lesson is that high heritability coexists with high "
            "malleability."
        ),
        "why_it_matters": (
            "Misreading behavior genetics fuels both genetic determinism "
            "and blank-slate denial. A precise, honestly-bounded "
            "architecture would ground education and health policy in "
            "reality instead of ideology."
        ),
        "sig_pointer": (
            "The Signature approach proposes an architecture ledger that "
            "separates what twin studies prove from what variants explain; "
            "the full treatment is in the Signature Edition record, "
            "labeled as a proposed solution."
        ),
        "sig_steps": [
            "Ledger twin-study heritability as the total to explain (Falconer arithmetic).",
            "Partition it across variant classes: common, rare, structural, interactive.",
            "Track the explained share as sample sizes grow; project the asymptote.",
            "State the interpretation limits explicitly: population statistic, not individual destiny.",
        ],
        "sig_assumptions": {
            "r_MZ": 0.86,
            "r_DZ": 0.60,
            "falconer_h2": 0.52,
        },
        "sig_confirm": [
            "The explained share converges toward the twin-study total along the projected curve.",
        ],
        "sig_refute": [
            "The explained share plateaus far below the twin total, implicating non-additive architecture.",
        ],
        "sig_scope": (
            "This does not claim behavior is genetically determined; it "
            "proposes the ledger and its limits."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "Cognition is substantially heritable, yet its genetic "
            "architecture stays diffuse. This record covers behavior "
            "genetics from twin-study heritabilities through Falconer's "
            "formula to the variant-level gap and the interpretation "
            "limits that matter most. Includes the heritability arithmetic "
            "and a pointer to the Signature proposed solution."
        ),
        "key_points": [
            "Twin-study meta-analysis: average heritability of human traits ~50% (Polderman et al. 2015).",
            "Falconer's formula: h^2 = 2(rMZ - rDZ); example correlations give h^2 ~0.52.",
            "Cognitive heritability rises with age (the Wilson effect).",
            "Variant-level architecture: thousands of tiny effects, diffuse and incomplete.",
            "Heritability is a population statistic; it does not imply immutability.",
        ],
        "requirements": [
            "The Falconer arithmetic shown explicitly.",
            "Determinism explicitly rejected.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "Heritability figures attributed to the twin literature.",
            "No individual-level prediction claims.",
        ],
        "citations": [CIT_TWINMETA, CIT_FALCONER],
    },
    {
        "key": "omnigenic",
        "name": "The Omnigenic Model: Is Every Gene a Disease Gene",
        "group": "Health, Behavior, and Prediction",
        "ladder_rank": 27,
        "ladder_tier": "advanced",
        "problem": ("Boyle, Li, and Pritchard proposed in 2017 that for "
                    "complex traits, essentially every expressed gene "
                    "contributes - the omnigenic model. Is it true, and "
                    "what would prove or falsify it?"),
        "background": (
            "The omnigenic model grew from an embarrassment: genome-wide "
            "hits for traits like height and schizophrenia spread across "
            "the genome with no respect for biological plausibility, as if "
            "every gene expressed in the relevant tissue contributed a "
            "little. Boyle and colleagues formalized the intuition: a "
            "small set of core genes with direct effects, plus a vast "
            "periphery of genes whose tiny regulatory ripples propagate "
            "through networks into the core. The model elegantly explains "
            "the diffuse architecture and the missing heritability, but "
            "critics note it risks explaining everything and therefore "
            "nothing: if every gene contributes, the model makes few "
            "crisp, falsifiable predictions. Tests since 2017 have been "
            "mixed - some traits show the predicted network-mediated "
            "spread, others concentrate more than the model expects. The "
            "unsolved problem is turning the elegant idea into a "
            "quantitative, falsifiable theory with a measured core "
            "fraction per trait."
        ),
        "why_it_matters": (
            "If the model holds, the search for 'the gene for X' is "
            "fundamentally misguided for complex traits, and drug "
            "discovery must target network cores rather than peripheral "
            "hits. If it fails, the field needs a better story for the "
            "diffuse architecture."
        ),
        "sig_pointer": (
            "The Signature approach proposes a core-fraction measurement "
            "protocol per trait; the full treatment is in the Signature "
            "Edition record, labeled as a proposed solution."
        ),
        "sig_steps": [
            "Define core operationally: genes whose perturbation moves the trait directly.",
            "Measure each trait's heritability partition into core vs peripheral.",
            "Predict the core fraction is small but nonzero and trait-specific.",
            "Falsify by finding traits where no core/periphery split improves prediction.",
        ],
        "sig_assumptions": {
            "core_genes": 100,
            "peripheral_genes": 10000,
            "heritability": 0.80,
            "peripheral_share": 0.90,
            "h2_via_peripheral": 0.72,
        },
        "sig_confirm": [
            "Core/periphery partitions replicate across traits and predict perturbation outcomes.",
        ],
        "sig_refute": [
            "No stable core emerges; every gene looks equally peripheral.",
        ],
        "sig_scope": (
            "This does not claim the model is true; it proposes the "
            "measurement that would decide."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "Do all genes contribute to every complex trait? This record "
            "covers the 2017 omnigenic model from its motivation through "
            "the core-periphery picture to the falsifiability debate. "
            "Includes the heritability-partition arithmetic and a pointer "
            "to the Signature proposed solution."
        ),
        "key_points": [
            "Omnigenic model (Boyle, Li, Pritchard 2017): core genes plus a vast contributing periphery.",
            "Motivated by GWAS hits spreading implausibly across the genome.",
            "Explains diffuse architecture and part of missing heritability.",
            "Critics: the model risks being unfalsifiable.",
            "The measured core fraction per trait is still unknown.",
        ],
        "requirements": [
            "The model stated fairly with its motivation.",
            "Falsifiability concern presented honestly.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "Model attributed to Boyle, Li, Pritchard 2017.",
        ],
        "citations": [CIT_OMNI, CIT_YENGO],
    },
    {
        "key": "prs_portability",
        "name": "Polygenic Scores Across Ancestries: The Portability Gap",
        "group": "Health, Behavior, and Prediction",
        "ladder_rank": 28,
        "ladder_tier": "advanced",
        "problem": ("Polygenic scores predict best in the European "
                    "ancestries they were trained on and degrade sharply "
                    "elsewhere - Martin and colleagues showed drops of "
                    "several-fold. How do we close the portability gap?"),
        "background": (
            "Polygenic scores sum thousands of small variant effects into "
            "a single risk number, and they work - modestly - for traits "
            "from height to heart disease. But the training data is "
            "overwhelmingly European-ancestry, and scores do not travel: "
            "Martin et al. (2019) showed prediction accuracy falling by "
            "roughly two- to five-fold in African-ancestry cohorts, with "
            "intermediate drops elsewhere. The causes are understood in "
            "outline: variant frequencies differ, linkage patterns differ "
            "so tag variants misfire, and some causal effects genuinely "
            "differ across genetic backgrounds and environments. Proposed "
            "fixes include diverse training cohorts, cross-ancestry "
            "methods that model linkage differences, and causal-variant "
            "fine-mapping - but the gap persists, and deploying "
            "European-trained scores clinically would widen health "
            "disparities. The unsolved problem is a score that performs "
            "equitably everywhere, proven in prospective testing."
        ),
        "why_it_matters": (
            "A prediction tool that works only for one ancestry is a "
            "disparity engine. Closing the gap is prerequisite to any "
            "equitable clinical use of polygenic prediction."
        ),
        "sig_pointer": (
            "The Signature approach proposes an ancestry-factored score "
            "with a portability audit; the full treatment is in the "
            "Signature Edition record, labeled as a proposed solution."
        ),
        "sig_steps": [
            "Factor scores by ancestry-specific linkage and frequency, not by one global model.",
            "Audit every score: report accuracy per ancestry before any use.",
            "Require prospective validation in each target ancestry.",
            "Predict the gap closes only with diverse training data, not with statistical cleverness alone.",
        ],
        "sig_assumptions": {
            "r2_european": 0.10,
            "r2_african": 0.02,
            "portability_drop": 5.0,
        },
        "sig_confirm": [
            "Factored scores reach parity in prospective multi-ancestry trials.",
        ],
        "sig_refute": [
            "Parity remains unreachable even with fully diverse training data.",
        ],
        "sig_scope": (
            "This does not claim parity is achievable; it proposes the "
            "audit standard."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "Polygenic scores lose several-fold accuracy outside European "
            "ancestries. This record covers the portability gap from the "
            "2019 Martin findings through its causes to the proposed fixes "
            "and the equity stakes. Includes the drop arithmetic and a "
            "pointer to the Signature proposed solution."
        ),
        "key_points": [
            "European-trained scores drop ~2-5x in accuracy in African-ancestry cohorts (Martin et al. 2019).",
            "Causes: frequency differences, linkage differences, and background-dependent effects.",
            "Proposed fixes: diverse cohorts, cross-ancestry methods, fine-mapping.",
            "Clinical deployment of unported scores would widen disparities.",
            "Equitable performance, prospectively proven, is still missing.",
        ],
        "requirements": [
            "The drop figures with source.",
            "Equity stakes stated plainly.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "No claim that any current score is clinic-ready across ancestries.",
        ],
        "citations": [CIT_MARTIN, CIT_YENGO],
    },
    {
        "key": "genetic_nurture",
        "name": "Genetic Nurture: Genes That Work Without Being Inherited",
        "group": "Environment and Epigenetics",
        "ladder_rank": 29,
        "ladder_tier": "advanced",
        "problem": ("Parents influence children through genes they do not "
                    "transmit: Kong and colleagues showed non-transmitted "
                    "parental alleles affecting children's education. How "
                    "large is this genetic nurture, and how does it rewrite "
                    "heritability?"),
        "background": (
            "The classic model says parental genes matter only when "
            "transmitted. Kong et al. (2018) broke that model with a "
            "clever design: parental alleles NOT passed to the child "
            "nevertheless predicted the child's educational attainment, at "
            "about 30 percent of the strength of transmitted alleles. The "
            "mechanism is environmental but genetically caused: parents' "
            "genes shape the home, the neighborhood, the resources - the "
            "nurture the child grows in. The discovery tangles every "
            "heritability estimate, because part of what looks like "
            "direct genetic inheritance is really this indirect path, and "
            "it tangles polygenic prediction too. The unsolved problems "
            "are the full accounting - how much of each trait's "
            "heritability is nurture in disguise - and the mechanisms: "
            "which parental traits, built by which genes, shape which "
            "environments."
        ),
        "why_it_matters": (
            "Genetic nurture redraws the line between nature and nurture: "
            "genes matter partly by building environments. Getting the "
            "accounting right changes what heritability means and where "
            "interventions should aim."
        ),
        "sig_pointer": (
            "The Signature approach proposes a nurture-decomposition "
            "design for every heritability study; the full treatment is in "
            "the Signature Edition record, labeled as a proposed solution."
        ),
        "sig_steps": [
            "In every family study, genotype parents fully, not just children.",
            "Estimate transmitted vs non-transmitted allele effects separately.",
            "Report the nurture share of each heritability estimate.",
            "Predict the nurture share is largest for socially mediated traits like education.",
        ],
        "sig_assumptions": {
            "transmitted_effect": 1.0,
            "nurture_effect": 0.30,
            "nurture_share": 0.2308,
        },
        "sig_confirm": [
            "Nurture shares replicate across cohorts and track social mediation as predicted.",
        ],
        "sig_refute": [
            "Non-transmitted effects vanish with better socioeconomic controls.",
        ],
        "sig_scope": (
            "This does not claim a universal nurture fraction; it proposes "
            "the decomposition design."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "Genes parents do not pass on still shape their children - "
            "through the environments those genes build. This record "
            "covers genetic nurture from the 2018 Kong discovery through "
            "its threat to heritability estimates to the missing full "
            "accounting. Includes the effect-share arithmetic and a pointer "
            "to the Signature proposed solution."
        ),
        "key_points": [
            "Non-transmitted parental alleles predict child education at ~30% of transmitted strength (Kong et al. 2018).",
            "Mechanism: parental genes shape the rearing environment.",
            "Part of measured heritability is nurture in disguise.",
            "Polygenic prediction absorbs the nurture path silently.",
            "The full per-trait accounting is still missing.",
        ],
        "requirements": [
            "The 30% figure with source.",
            "Heritability implications stated carefully.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "Discovery attributed to Kong et al. 2018.",
        ],
        "citations": [CIT_NURTURE, CIT_FALCONER],
    },
    {
        "key": "domestication",
        "name": "The Genetics of Domestication",
        "group": "Evolution",
        "ladder_rank": 30,
        "ladder_tier": "advanced",
        "problem": ("Selecting foxes for tameness alone produced floppy "
                    "ears, spotted coats, and wagging tails - the "
                    "domestication syndrome. What genetic architecture "
                    "links behavior selection to such sweeping physical "
                    "change?"),
        "background": (
            "In 1959 Dmitry Belyaev began selecting silver foxes for a "
            "single trait - tameness toward humans - and within decades "
            "the foxes showed the full domestication syndrome: floppy "
            "ears, piebald coats, curly tails, shortened snouts, and "
            "altered reproductive timing, mirroring dogs, pigs, and other "
            "domesticates (Trut, Oskina, Kharlamova 2009). The leading "
            "explanation invokes neural crest cells: selection on behavior "
            "alters the development of these multipotent embryonic cells, "
            "which contribute to both the adrenal system (fight-or-flight) "
            "and to pigment, cartilage, and facial bone - one developmental "
            "lever moving many traits. Genomic studies of dogs, chickens, "
            "and foxes find selection signatures scattered across many "
            "loci, consistent with a polygenic, network-level response. "
            "The unsolved problem is the causal chain: from selected "
            "variants through developmental pathways to the syndrome, "
            "mapped completely in any one species."
        ),
        "why_it_matters": (
            "Domestication is evolution at human speed and the closest "
            "model for how selection on one trait remodels a whole "
            "organism. Its genetics illuminates both our past - the "
            "making of dogs and crops - and the developmental constraints "
            "on all rapid evolution."
        ),
        "sig_pointer": (
            "The Signature approach proposes a neural-crest lever test in "
            "the fox lines; the full treatment is in the Signature "
            "Edition record, labeled as a proposed solution."
        ),
        "sig_steps": [
            "Map selection signatures in tame vs aggressive fox lines completely.",
            "Test the neural-crest hypothesis: do top loci converge on crest development pathways?",
            "Perturb top candidate pathways in a model system and score syndrome traits.",
            "Quantify the response with the breeder's equation as the baseline expectation.",
        ],
        "sig_assumptions": {
            "heritability": 0.35,
            "selection_differential": 2.0,
            "response_per_generation": 0.70,
            "generations": 10,
            "total_response": 7.0,
        },
        "sig_confirm": [
            "Top loci converge on neural-crest pathways and perturbations reproduce syndrome traits.",
        ],
        "sig_refute": [
            "Selection signatures scatter with no developmental convergence.",
        ],
        "sig_scope": (
            "This does not claim the neural-crest hypothesis is proven; "
            "it proposes the test."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "Tameness selection remade the fox: ears, coat, tail, and "
            "temperament together. This record covers domestication "
            "genetics from Belyaev's 1959 fox experiment through the "
            "neural-crest hypothesis to the missing complete causal chain. "
            "Includes the breeder's-equation arithmetic and a pointer to "
            "the Signature proposed solution."
        ),
        "key_points": [
            "Belyaev's fox experiment (1959-): selecting for tameness alone produced the domestication syndrome.",
            "Syndrome traits mirror those of dogs, pigs, and other domesticates.",
            "Neural-crest hypothesis: one developmental lever moves behavior, pigment, cartilage, and bone.",
            "Genomic studies show polygenic, network-level selection responses.",
            "The complete causal chain is unmapped in any species.",
        ],
        "requirements": [
            "The fox experiment described accurately.",
            "Neural-crest hypothesis labeled as leading, not proven.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "Experiment attributed to Belyaev via Trut, Oskina, Kharlamova 2009.",
        ],
        "citations": [CIT_FOX, CIT_FALCONER],
    },
    {
        "key": "minimal_genome",
        "name": "The Minimal Genome: How Little DNA Can Run Life",
        "group": "Health, Behavior, and Prediction",
        "ladder_rank": 31,
        "ladder_tier": "advanced",
        "problem": ("The synthetic bacterium JCVI-syn3.0 runs on 473 genes "
                    "in 531,560 base pairs - yet a third of its genes have "
                    "unknown function. What is the true minimal gene set "
                    "for life, and what are the mystery genes doing?"),
        "background": (
            "Hutchison and colleagues reported JCVI-syn3.0 in 2016: a "
            "synthesized Mycoplasma genome stripped to 473 genes, the "
            "smallest genome of any self-replicating organism, running at "
            "531,560 base pairs - about 1,124 base pairs per gene. The "
            "stunning footnote was that 149 of those genes - nearly a "
            "third - had no known function; they were kept because the "
            "cell died without them. Follow-up work has assigned functions "
            "to some, but a residue of essential unknowns persists, a "
            "humbling reminder that we cannot fully account for even the "
            "simplest life we can build. The unsolved problems compound "
            "from here: is 473 near the true minimum or an artifact of "
            "one design path, how does the minimum change with environment "
            "richness, and what would a minimal genome for a different "
            "chemistry look like?"
        ),
        "why_it_matters": (
            "The minimal genome is the parts list of life itself: every "
            "mystery gene is a fundamental biological function we have "
            "not yet named. It is also the chassis for synthetic biology - "
            "the simplest platform on which to build."
        ),
        "sig_pointer": (
            "The Signature approach proposes a function-hunt protocol for "
            "the essential unknowns, ranked by conservation; the full "
            "treatment is in the Signature Edition record, labeled as a "
            "proposed solution."
        ),
        "sig_steps": [
            "Rank the essential unknowns by conservation across bacteria.",
            "Probe each with structural prediction and interaction screens.",
            "Assign provisional functions and test by targeted rescue experiments.",
            "Predict the most conserved unknowns encode core informational processes.",
        ],
        "sig_assumptions": {
            "genes": 473,
            "base_pairs": 531560,
            "bp_per_gene": 1123.81,
            "unknown_fraction": 0.315,
        },
        "sig_confirm": [
            "Top conserved unknowns resolve into core informational roles.",
        ],
        "sig_refute": [
            "Unknowns prove to be purely contextual - essential only in this exact design.",
        ],
        "sig_scope": (
            "This does not claim 473 is the universal minimum; it "
            "proposes the hunt protocol."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "The simplest synthetic cell runs on 473 genes - and a third "
            "are mysteries. This record covers the minimal genome from "
            "JCVI-syn3.0 (2016) through the essential unknowns to the "
            "open questions of true minimality. Includes the gene-density "
            "arithmetic and a pointer to the Signature proposed solution."
        ),
        "key_points": [
            "JCVI-syn3.0 (Hutchison et al. 2016): 473 genes, 531,560 bp - smallest self-replicating genome.",
            "~1,124 base pairs per gene.",
            "149 genes (~31%) were essential but of unknown function at publication.",
            "The minimum may depend on environment richness and design path.",
            "Every mystery gene is an unnamed fundamental function.",
        ],
        "requirements": [
            "The 473 / 531,560 numbers with source.",
            "Unknown-function fraction stated honestly.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "Minimal-genome claim attributed to Hutchison et al. 2016.",
        ],
        "citations": [CIT_SYN30],
    },
    {
        "key": "genetic_load",
        "name": "Genetic Load: How Much Harm Can a Genome Carry",
        "group": "Inheritance and Variation",
        "ladder_rank": 32,
        "ladder_tier": "advanced",
        "problem": ("Every genome carries deleterious mutations - the "
                    "genetic load. Haldane's arithmetic suggests the load "
                    "could be crushing, yet populations persist. How much "
                    "harm do we actually carry, and why does it not "
                    "destroy us?"),
        "background": (
            "Haldane showed in 1937 that each harmful mutation exacts a "
            "cost, and summing over the genome gives the genetic load - "
            "the reduction in fitness relative to a mutation-free ideal. "
            "With human deleterious mutation rates estimated near one to "
            "two per genome per generation, the naive load arithmetic "
            "gives startling numbers: a load of 1 - e^-U reaches about "
            "0.86 at U = 2, seemingly implying populations should collapse. "
            "They do not, and the resolutions are instructive: much of the "
            "load is carried silently in heterozygotes, selection acts on "
            "relative rather than absolute fitness, and synergistic "
            "interactions let selection clear multiple mutations at once. "
            "The modern unsolved problem is empirical: measuring the real "
            "distribution of fitness effects across the genome, tracking "
            "how the load shifts as medicine relaxes selection, and "
            "testing whether small populations face mutational meltdown - "
            "the feedback loop where load shrinks populations, which "
            "weakens selection, which raises load."
        ),
        "why_it_matters": (
            "The load sets the baseline burden of genetic disease and the "
            "viability floor for endangered species. As medicine relaxes "
            "selection, the load's trajectory becomes a question about "
            "humanity's genetic future."
        ),
        "sig_pointer": (
            "The Signature approach proposes a load-ledger tracked across "
            "generations in model populations; the full treatment is in "
            "the Signature Edition record, labeled as a proposed solution."
        ),
        "sig_steps": [
            "Estimate U, the deleterious rate per genome per generation, from trio data.",
            "Compute the naive load 1 - e^-U as the upper bound.",
            "Measure the realized load via fitness assays in model populations.",
            "Attribute the gap between naive and realized to dominance, synergy, and soft selection.",
        ],
        "sig_assumptions": {
            "U": 2.0,
            "naive_load": 0.8647,
        },
        "sig_confirm": [
            "Realized loads track the ledger's attributions across species.",
        ],
        "sig_refute": [
            "Realized loads exceed the naive bound, implying missing load sources.",
        ],
        "sig_scope": (
            "This does not claim to know humanity's true load; it proposes "
            "the ledger method."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "Haldane's arithmetic says our mutation burden should be "
            "crushing - yet we persist. This record covers genetic load "
            "from 1937 through the dominance and synergy resolutions to "
            "the modern empirical hunt for the true distribution of "
            "fitness effects. Includes the load arithmetic and a pointer "
            "to the Signature proposed solution."
        ),
        "key_points": [
            "Haldane (1937): each deleterious mutation exacts a fitness cost; the sum is the load.",
            "At U ~ 2 per genome per generation, naive load 1 - e^-U ~ 0.86.",
            "Heterozygote masking, relative fitness, and synergy resolve the paradox in principle.",
            "The empirical distribution of fitness effects is still being measured.",
            "Mutational meltdown threatens small populations in a feedback loop.",
        ],
        "requirements": [
            "The load arithmetic shown explicitly.",
            "Resolutions presented as understood mechanisms, measurements as open.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "Load concept attributed to Haldane 1937.",
        ],
        "citations": [CIT_HALDANE, CIT_KONG, CIT_FISHER],
    },
    {
        "key": "code_origin",
        "name": "The Origin of the Genetic Code",
        "group": "Evolution",
        "ladder_rank": 33,
        "ladder_tier": "advanced",
        "problem": ("Why do 64 codons encode 20 amino acids in exactly this "
                    "arrangement? Is the genetic code a frozen accident, a "
                    "stereochemical fit, or an optimized system - and could "
                    "it have been otherwise?"),
        "background": (
            "Crick's 1968 frozen-accident hypothesis held that the code's "
            "assignment of 61 sense codons to 20 amino acids (plus 3 stops) "
            "was arbitrary and then locked in, because any change would "
            "retarget every protein at once. But the code is not random: "
            "similar codons tend to encode similar amino acids, so point "
            "mutations often swap in a chemically similar replacement - a "
            "robustness that looks designed. Competing theories invoke "
            "stereochemistry (amino acids binding their codons directly), "
            "coevolution with amino-acid synthesis pathways, and "
            "error-minimization optimized by selection among competing "
            "early codes. Computational studies show the standard code is "
            "better than most random codes at buffering errors but not "
            "provably optimal. The problem is compounded by deep time: the "
            "code was fixed before the last universal common ancestor, "
            "leaving almost no direct evidence of the alternatives that "
            "lost."
        ),
        "why_it_matters": (
            "The code is the operating system of all known life; its "
            "origin story is the origin story of biological information. "
            "It also matters practically: synthetic biologists already "
            "rewire codons, testing whether the frozen accident can be "
            "thawed."
        ),
        "sig_pointer": (
            "The Signature approach proposes a code-competition tournament "
            "in simulation with explicit optimality scoring; the full "
            "treatment is in the Signature Edition record, labeled as a "
            "proposed solution."
        ),
        "sig_steps": [
            "Enumerate code variants under stereochemical and coevolutionary constraints.",
            "Score each on error robustness: mean chemical distance of single-base neighbors.",
            "Run competition tournaments: codes competing for translation machinery.",
            "Predict the winner resembles the standard code's robustness profile without matching it exactly.",
        ],
        "sig_assumptions": {
            "sense_codons": 61,
            "amino_acids": 20,
            "mean_degeneracy": 3.05,
        },
        "sig_confirm": [
            "Tournament winners cluster near the standard code's robustness.",
        ],
        "sig_refute": [
            "Winners scatter widely, supporting pure frozen accident.",
        ],
        "sig_scope": (
            "This does not claim to know how the code actually arose; it "
            "proposes the tournament as the decision procedure."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "Sixty-four codons, twenty amino acids, one arrangement used "
            "by nearly all life. This record covers the code's origin "
            "from Crick's 1968 frozen accident through stereochemical and "
            "optimization theories to the evidence limits of deep time. "
            "Includes the degeneracy arithmetic and a pointer to the "
            "Signature proposed solution."
        ),
        "key_points": [
            "61 sense codons encode 20 amino acids: mean degeneracy ~3.05.",
            "Similar codons encode similar amino acids - the code buffers point mutations.",
            "The standard code beats most random codes on robustness but is not provably optimal.",
            "The code fixed before LUCA, leaving almost no direct evidence of alternatives.",
            "Synthetic biologists now rewire codons, testing whether the accident can be thawed.",
        ],
        "requirements": [
            "The degeneracy arithmetic shown explicitly.",
            "All three theory families presented without declaring a winner.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "Frozen accident attributed to Crick 1968.",
        ],
        "citations": [CIT_CRICKCODE, CIT_WC],
    },
    {
        "key": "rna_world",
        "name": "The RNA World: Genetics Before Genes",
        "group": "Evolution",
        "ladder_rank": 34,
        "ladder_tier": "advanced",
        "problem": ("Before DNA and proteins, Gilbert proposed in 1986 "
                    "that RNA both stored information and catalyzed "
                    "reactions. Can an RNA-only system actually replicate "
                    "itself well enough to start evolution?"),
        "background": (
            "The RNA world hypothesis answers the chicken-and-egg problem "
            "of life's origin: DNA needs protein enzymes to copy it, "
            "proteins need DNA to encode them - but RNA can both carry "
            "information and catalyze reactions, as natural ribozymes "
            "prove. Gilbert's 1986 formulation launched a research program "
            "that has built impressive pieces: ribozymes that copy short "
            "templates, protocell models that grow and divide, and "
            "plausible prebiotic syntheses of RNA building blocks. The "
            "gap is replication fidelity and length: laboratory ribozymes "
            "copy only short stretches with errors, far from the accurate "
            "copying of a full ribozyme needed for sustained evolution. "
            "The sequence space is also daunting - a 40-base RNA has 4^40, "
            "about 1.2 x 10^24, possible sequences - raising the question "
            "of how the first functional replicator was ever found. The "
            "hypothesis remains the leading framework, but the "
            "demonstration of a self-sustaining RNA replicator system is "
            "still missing."
        ),
        "why_it_matters": (
            "The origin of genetics is the origin of heredity itself; "
            "solving it would complete the story from chemistry to "
            "biology. It also guides the search for life elsewhere: an "
            "RNA-first origin predicts what alien biochemistry might "
            "share with ours."
        ),
        "sig_pointer": (
            "The Signature approach proposes a fidelity-length threshold "
            "analysis for replicator takeoff; the full treatment is in the "
            "Signature Edition record, labeled as a proposed solution."
        ),
        "sig_steps": [
            "Define the takeoff threshold: replication fidelity times length must exceed the error catastrophe boundary.",
            "Map current ribozymes against the threshold: fidelity achieved vs length achieved.",
            "Predict the missing capability is processive copying of ~100+ bases above threshold fidelity.",
            "Test by directed evolution aimed explicitly at the threshold coordinates.",
        ],
        "sig_assumptions": {
            "ribozyme_length": 40,
            "sequence_space": 1.2089e24,
        },
        "sig_confirm": [
            "Directed evolution crosses the fidelity-length threshold and sustains replication.",
        ],
        "sig_refute": [
            "No ribozyme architecture approaches the threshold despite exhaustive search.",
        ],
        "sig_scope": (
            "This does not claim life began this way; it proposes the "
            "threshold as the missing demonstration's specification."
        ),
        "scenario": {"observed_confirm": [], "observed_refute": []},
        "description": (
            "Before DNA and proteins, RNA may have done both jobs. This "
            "record covers the RNA world from Gilbert's 1986 proposal "
            "through ribozyme engineering to the fidelity-length gap that "
            "keeps the hypothesis unproven. Includes the sequence-space "
            "arithmetic and a pointer to the Signature proposed solution."
        ),
        "key_points": [
            "RNA world (Gilbert 1986): RNA as both information store and catalyst.",
            "Natural ribozymes prove catalysis; lab ribozymes copy only short templates.",
            "A 40-base RNA has ~1.2e24 possible sequences - the search problem is immense.",
            "Self-sustained RNA replication above the error threshold is undemonstrated.",
            "The hypothesis leads the field but remains unproven.",
        ],
        "requirements": [
            "The sequence-space arithmetic shown explicitly.",
            "Hypothesis status stated as leading but unproven.",
            "Honesty label on the signature solution.",
        ],
        "standards": [
            "RNA world attributed to Gilbert 1986.",
        ],
        "citations": [CIT_RNAWORLD, CIT_WC],
    },
]
