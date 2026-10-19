#!/usr/bin/env python3
"""Entries for The Unsolved Bioinformatics Database (unsolved-bioinformatics) and its
Signature half (unsolved-bioinformatics-signature).

34 famous unsolved problems in bioinformatics, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex/compounded).
Public half: real, fact-checked problems. Signature half: the same 34
through the Signature lens, ALWAYS labeled as proposals, never established
science.

ID prefixes JAH-USBF- / JAH-USBFS- verified free in manifest id_prefix
values (exact + substring, both directions).
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

FIELD = {
 "tag": "bioinformatics",
 "disp": "bioinformatics",
 "name": "The Unsolved Bioinformatics Database",
 "sig_name": "The Unsolved Bioinformatics Signature Database",
 "prefix": "JAH-USBF-",
 "sig_prefix": "JAH-USBFS-",
 "ai": "JAH Unsolved Bioinformatics Archivist",
 "tagline": ("Thirty-four famous open problems in bioinformatics, from sequence alignment to the unified "
             "computational biology: real, fact-checked, each with its full story and a clearly labeled Signature "
             "proposed solution."),
 "sig_tagline": ("His original Signature solution method applied to all 34 great open problems of bioinformatics: "
                 "Signature-generated proposed solutions with assumptions declared, confirm and refute conditions "
                 "stated, and limits honestly marked. Clearly labeled Signature-made, never established science."),
 "pub_line": ("Public records - 34 famous open problems in bioinformatics, real and fact-checked: sequence "
              "alignment, multiple alignment, genome assembly, gene prediction, variant calling, read mapping, "
              "phylogenetics, orthology, motif discovery, RNA structure, and protein function prediction - every "
              "record carrying the problem statement, background, why it matters, key points, requirements, "
              "standards, citations, and a working solution-explorer demonstration, organized in the Signature "
              "system."),
 "sig_line": ("Signature originals - his original Signature solution method: the same 34 famous unsolved "
              "bioinformatics problems approached as a covenant between the known and the unknown, each carrying "
              "the full Signature-generated proposed solution with its assumptions declared, its confirm and "
              "refute conditions stated, and its limits honestly marked. Clearly labeled Signature-made, never "
              "presented as established science or authentic public record."),
 "ladder_text": (" Records are ordered by the teaching ladder: Foundations (sequence alignment, multiple "
                 "alignment, genome assembly, gene prediction, variant calling, read mapping, phylogenetics, "
                 "orthology, motif discovery, RNA structure, protein function prediction) -> Compounded "
                 "(metagenomic binning, single-cell integration, spatial transcriptomics, long-read assembly, "
                 "structural variants, epigenomic integration, network inference, pathway enrichment, biomarker "
                 "discovery, drug-target prediction, CRISPR off-target, base-editing prediction) -> Advanced "
                 "(pangenome, graph genomes, telomere-to-telomere, dark genome, microbiome causality, multi-omics "
                 "integration, digital twin cell, AI interpretability, genomic privacy, reproducibility, unified "
                 "bioinformatics)."),
 "search_ph": ("Search alignment, assembly, variant calling, phylogenetics, single-cell, pangenome, multi-omics..."),
 "chat_ph": "Ask about the great open problems of bioinformatics...",
 "greet_pub": ("I am the JAH Unsolved Bioinformatics Archivist. Ask me about the great open problems of "
               "bioinformatics - from sequence alignment, assembly, and variant calling through single-cell and "
               "epigenomics, to pangenomes, multi-omics, and unified computational biology."),
 "greet_sig": ("I am the JAH Unsolved Bioinformatics Archivist (Signature). Ask me about the Signature proposed "
               "solutions to the great open problems of bioinformatics - every approach labeled as a proposal, "
               "never established science."),
 "role_pub": ("unsolved bioinformatics archivist - the great open problems of bioinformatics, from sequence "
              "alignment, assembly, and variant calling through single-cell and epigenomics, to pangenomes, "
              "multi-omics, and unified computational biology; teaches progressively along the ladder from "
              "foundations through compounded to advanced; answers from many angles - definition, example, "
              "analogy, application, history, math - using only archive data from this system"),
 "role_sig": ("unsolved bioinformatics archivist - Signature editions: his original Signature solution method "
              "applied to the 34 great open problems of bioinformatics, each carrying the full "
              "Signature-generated proposed solution, clearly labeled Signature-made and never presented as "
              "established science; teaches progressively along the ladder from foundations through compounded "
              "to advanced; answers from many angles - definition, example, analogy, application, history, "
              "math - using only archive data from this system"),
 "gen_desc": "Generate clearly-labeled unsolved bioinformatics studies. Seeded archive records are the authoritative entries.",
 "standards": [
  "Problem statements verified against the published literature; open status confirmed as of 2026.",
  "Quantitative claims cross-checked against standard references (Durbin et al., Biological Sequence Analysis; Pevzner, Computational Molecular Biology).",
  "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
 ],
 "sig_tail": ("Signature editions carry the Signature system's proposed solution approaches to famous "
              "unsolved problems. Every solution is labeled a Signature-generated proposal, never "
              "established science, never peer-accepted, never proof."),
}

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "bf-alignment",
 "name": "The Sequence Alignment Problem",
 "group": "Sequences",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "Comparing two DNA sequences sounds simple - but what is the biologically correct alignment when gaps, repeats, and rearrangements confuse the algorithms?",
 "background": "The sequence-alignment problem - optimal pairwise alignment - is solved algorithmically (Needleman-Wunsch, Smith-Waterman) but not biologically: the scoring matrices and gap penalties are heuristic, and the 'optimal' alignment is optimal only under those choices. For divergent sequences, different parameters give different alignments - and different biological conclusions. The algorithm is exact; the biology is parameterized. The alignment is the foundation every comparative analysis stands on - and its correctness is assumed, not known.",
 "why_it_matters": "Every homology inference, phylogeny, and variant call starts from an alignment. The parameterized foundation's errors propagate everywhere.",
 "sig_lens": "The Signature lens reads alignment as the text comparison: the protocol must choose the scoring honestly - and report where the text admits multiple readings.",
 "sig_solution": LABEL + " Assumptions: (1) optimality is parameter-relative; (2) divergent alignments vary with parameters. Reasoning path: report alignment uncertainty - suboptimal alignments and parameter-sensitivity - instead of a single answer. Proposed mechanism: a text protocol with alignment-uncertainty reporting (suboptimal ensembles), parameter-robustness checks, and downstream analyses carrying the uncertainty. Confirm: uncertainty-aware analyses are more reliable. Kill: the uncertainty proves unquantifiable. Does NOT claim: the true alignment - it reports the readings.",
 "pointer": "The Signature system's proposed approach reports sequence-alignment uncertainty explicitly; the companion Signature Edition record specifies the text protocol.",
 "key_points": [
  "Needleman-Wunsch/Smith-Waterman solve the algorithmic problem.",
  "Scoring matrices and gap penalties are heuristic.",
  "Divergent sequences align differently under parameters.",
  "Alignment errors propagate to all comparative analyses.",
 ],
 "requirements": [
  "Suboptimal-alignment ensemble reporting.",
  "Parameter-robustness checks.",
  "Uncertainty carried into downstream analyses.",
 ],
 "citations": [
  "Needleman SB, Wunsch CD (1970) A general method applicable to the search for similarities. J. Molecular Biology 48.",
 ],
 "demo": {"seed": 1, "length": 60},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "bf-msa",
 "name": "The Multiple Sequence Alignment Problem",
 "group": "Sequences",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "Aligning many sequences at once is NP-hard - but how close do the heuristic aligners get, and does it matter for the biology?",
 "background": "The MSA problem - optimal multiple alignment is NP-hard; the heuristics (progressive: Clustal, MUSCLE; iterative; consistency-based: T-Coffee; phylogeny-aware: PRANK) each have failure modes: progressive alignment's once-a-gap errors propagate, and the benchmarks (BAliBASE, SABmark) are small and possibly unrepresentative. For phylogenetics, alignment error is the dominant error source - worse than the tree method. The heuristics are good; their errors are the phylogeny's errors.",
 "why_it_matters": "MSA errors dominate phylogenetic error. The heuristic's mistakes become the tree of life's mistakes.",
 "sig_lens": "The Signature lens reads MSA as the committee alignment: the protocol must know each member's biases (heuristics) and vote with uncertainty.",
 "sig_solution": LABEL + " Assumptions: (1) optimal MSA NP-hard; (2) alignment error dominates phylogeny error. Reasoning path: align with uncertainty - ensemble aligners and alignment-masked phylogenetics. Proposed mechanism: a committee protocol with multi-aligner ensembles, reliability-scored columns, and phylogenetics on the reliable subset with uncertainty. Confirm: ensemble-masked trees are more accurate. Kill: the ensembles disagree too widely. Does NOT claim: the true MSA - it votes with uncertainty.",
 "pointer": "The Signature system's proposed approach builds MSA ensembles with reliability-scored phylogenetics; the companion Signature Edition record specifies the committee protocol.",
 "key_points": [
  "Optimal MSA is NP-hard; heuristics rule.",
  "Progressive errors propagate once made.",
  "Benchmarks are small and possibly unrepresentative.",
  "Alignment error dominates phylogenetic error.",
 ],
 "requirements": [
  "Multi-aligner ensemble approaches.",
  "Column-reliability scoring.",
  "Uncertainty-aware phylogenetics.",
 ],
 "citations": [
  "Notredame C et al. (2000) T-Coffee: a novel method for fast and accurate multiple sequence alignment. J. Molecular Biology 302.",
 ],
 "demo": {"seed": 2, "length": 80},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "bf-assembly",
 "name": "The Genome Assembly Problem",
 "group": "Sequences",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "Reconstructing a genome from fragments is a giant jigsaw - but how can repeats be resolved, and how is an assembly's correctness verified?",
 "background": "The assembly problem - reconstructing genomes from reads - is challenged by repeats: short reads cannot span long repeats, producing fragmented assemblies; the overlap-layout-consensus and de Bruijn paradigms each have repeat-resolution limits. Assembly validation is itself hard: N50 measures contiguity, not correctness; misassemblies (chimeric joins) are common. Long reads (PacBio HiFi, Oxford Nanopore) transformed the field - yet telomere-to-telomere remains the exception. The jigsaw's box cover (the true genome) is unknown.",
 "why_it_matters": "Every genomic analysis starts from an assembly. Misassembled genomes corrupt everything downstream.",
 "sig_lens": "The Signature lens reads assembly as the jigsaw without the box cover: the protocol must verify each join independently - and admit the unverifiable regions.",
 "sig_solution": LABEL + " Assumptions: (1) repeats defeat short reads; (2) contiguity metrics mislead. Reasoning path: assemble with long reads and verify joins independently (Hi-C, optical maps, trio data). Proposed mechanism: a jigsaw protocol with long-read-first assembly, independent join verification, and correctness (not just contiguity) reporting. Confirm: verified assemblies have fewer downstream errors. Kill: the repeats stay unresolvable. Does NOT claim: perfect assemblies - it verifies each join.",
 "pointer": "The Signature system's proposed approach verifies genome assemblies join-by-join independently; the companion Signature Edition record specifies the jigsaw protocol.",
 "key_points": [
  "Repeats defeat short-read assembly.",
  "N50 measures contiguity, not correctness.",
  "Misassembled chimeric joins are common.",
  "Long reads transformed but did not finish the problem.",
 ],
 "requirements": [
  "Long-read-first assembly strategies.",
  "Independent join verification (Hi-C, optical maps).",
  "Correctness reporting beyond contiguity.",
 ],
 "citations": [
  "Nagarajan N, Pop M (2013) Sequence assembly demystified. Nature Reviews Genetics 14.",
 ],
 "demo": {"seed": 3, "length": 100},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "bf-gene-pred",
 "name": "The Gene Prediction Problem",
 "group": "Annotation",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "Finding genes in raw DNA - but how can the predictions be accurate when the signals are weak and the biology is complex?",
 "background": "The gene-prediction problem - ab initio finders (Genscan, Augustus) plus evidence-based annotation - is largely solved for human protein-coding genes (the count converged ~19,000-20,000) but open for: non-model organisms, alternative splicing isoforms, small ORFs, lncRNAs, and the exact exon boundaries. The predictions' errors (false exons, missed genes) propagate to every functional analysis. Annotation is never finished: each genome's gene set is a working draft.",
 "why_it_matters": "Gene catalogs are the genome's table of contents. The draft's errors misdirect all functional genomics.",
 "sig_lens": "The Signature lens reads gene prediction as the table of contents: the protocol must verify each entry with evidence - and keep the draft open.",
 "sig_solution": LABEL + " Assumptions: (1) human coding count converged; (2) isoforms, small ORFs, non-models open. Reasoning path: annotate with evidence integration - RNA-seq, proteomics, conservation - and version the drafts. Proposed mechanism: a contents protocol with evidence-integrated annotation pipelines, draft versioning with change logs, and targeted validation of uncertain genes. Confirm: evidence-integrated catalogs have fewer errors. Kill: the uncertain genes stay uncertain. Does NOT claim: the final gene catalog - it keeps the draft open.",
 "pointer": "The Signature system's proposed approach annotates genes with integrated evidence and versioned drafts; the companion Signature Edition record specifies the contents protocol.",
 "key_points": [
  "Human protein-coding count converged ~19,000-20,000.",
  "Isoforms, small ORFs, lncRNAs remain hard.",
  "Non-model organisms poorly annotated.",
  "Every genome's catalog is a working draft.",
 ],
 "requirements": [
  "Evidence-integrated annotation (RNA-seq, proteomics).",
  "Versioned annotation drafts.",
  "Targeted validation of uncertain genes.",
 ],
 "citations": [
  "Brent MR (2008) Steady progress and recent breakthroughs in the accuracy of automated genome annotation. Nature Reviews Genetics 9.",
 ],
 "demo": {"seed": 4, "length": 70},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "bf-variant",
 "name": "The Variant Calling Problem",
 "group": "Variation",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "Finding DNA differences from sequencing reads - but how can true variants be separated from errors when the data is noisy?",
 "background": "The variant-calling problem - SNPs and indels from read alignments - is mature for SNPs (GATK best practices, deep-learning callers) but open for: indels in repeats, low-frequency somatic variants, and the reference-bias problem (reads from divergent haplotypes map poorly). The truth sets (Genome in a Bottle) cover only parts of the genome - the hard regions (segmental duplications) lack truth. Clinical variant calling needs accuracies the benchmarks cannot verify in hard regions.",
 "why_it_matters": "Clinical genomics decides treatments from variant calls. The hard regions' unverified accuracy is the diagnostic risk.",
 "sig_lens": "The Signature lens reads variant calling as the proofreading: the protocol must proofread the hard passages (repeats, low-frequency) with extra care - and mark the illegible ones.",
 "sig_solution": LABEL + " Assumptions: (1) SNP calling mature; indels/somatic/reference-bias open; (2) truth sets avoid hard regions. Reasoning path: extend truth to hard regions (long-read-based truth sets) and call with uncertainty. Proposed mechanism: a proofreading protocol with hard-region truth sets, uncertainty-quantified variant calls, and clinical reporting with region-aware confidence. Confirm: hard-region calls validated. Kill: the hard regions stay illegible. Does NOT claim: perfect variant calls - it marks the illegible passages.",
 "pointer": "The Signature system's proposed approach extends variant-calling truth to hard regions with uncertainty; the companion Signature Edition record specifies the proofreading protocol.",
 "key_points": [
  "SNP calling mature; indel/somatic calling open.",
  "Reference bias against divergent haplotypes.",
  "Truth sets avoid segmental duplications.",
  "Clinical accuracy unverified in hard regions.",
 ],
 "requirements": [
  "Long-read-based hard-region truth sets.",
  "Uncertainty-quantified variant calls.",
  "Region-aware clinical confidence reporting.",
 ],
 "citations": [
  "Zook JM et al. (2016) Extensive sequencing of seven human genomes (Genome in a Bottle). Scientific Data 3.",
 ],
 "demo": {"seed": 5, "length": 90},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "bf-mapping",
 "name": "The Read Mapping Problem",
 "group": "Sequences",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "Placing billions of reads on a reference - but how can multi-mapping reads be placed correctly, and what does reference bias cost?",
 "background": "The read-mapping problem - aligning billions of short reads - is solved for speed (BWA, Bowtie) but not for correctness: multi-mapping reads (repeats, gene families) are placed ambiguously or randomly; reference bias systematically undercounts non-reference alleles; and the linear reference itself is being superseded by graph genomes. The mappers are fast; their placements in hard regions are approximate. Every count (expression, variants) inherits the placement errors.",
 "why_it_matters": "Read placement errors corrupt expression and variant analyses. The fast mappers' approximations are the counts' errors.",
 "sig_lens": "The Signature lens reads mapping as the shelving: the protocol must shelve ambiguous books (multi-mappers) honestly - and fix the shelf (reference) bias.",
 "sig_solution": LABEL + " Assumptions: (1) multi-mappers placed ambiguously; (2) reference bias systematic. Reasoning path: place probabilistically and debias - multi-mapper-aware quantification, graph-genome references. Proposed mechanism: a shelving protocol with probabilistic multi-mapper handling, graph-genome mapping, and bias-corrected quantification. Confirm: debiased counts match ground truth better. Kill: the ambiguity proves irreducible. Does NOT claim: correct placements - it shelves honestly.",
 "pointer": "The Signature system's proposed approach handles multi-mappers probabilistically on graph genomes; the companion Signature Edition record specifies the shelving protocol.",
 "key_points": [
  "BWA/Bowtie fast; hard-region placements approximate.",
  "Multi-mapping reads placed ambiguously.",
  "Reference bias undercounts non-reference alleles.",
  "Linear references being superseded by graphs.",
 ],
 "requirements": [
  "Probabilistic multi-mapper quantification.",
  "Graph-genome mapping adoption.",
  "Bias-corrected count reporting.",
 ],
 "citations": [
  "Li H, Durbin R (2009) Fast and accurate short read alignment with Burrows-Wheeler transform. Bioinformatics 25.",
 ],
 "demo": {"seed": 6, "length": 60},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "bf-phylogeny",
 "name": "The Phylogenetic Tree Problem",
 "group": "Evolution",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "Reconstructing the tree of life - but how can the true tree be found when the data conflicts and the models are approximate?",
 "background": "The phylogeny problem - the true evolutionary tree - faces gene-tree/species-tree conflict (incomplete lineage sorting, hybridization), model misspecification (the substitution models are approximate), and the deep-time signal erosion. Methods (maximum likelihood: RAxML/IQ-TREE; Bayesian: MrBayes; coalescent: ASTRAL) each handle part; the total-evidence tree is debated at deep nodes. The tree of life's trunk is the hardest part - where the signal is oldest and weakest.",
 "why_it_matters": "The tree of life organizes all biology. Its deep trunk - the oldest relationships - is the least certain.",
 "sig_lens": "The Signature lens reads phylogeny as the family tree with disputed ancestors: the protocol must weigh each witness (gene) and mark the disputed branches.",
 "sig_solution": LABEL + " Assumptions: (1) gene trees conflict; (2) deep signal eroded. Reasoning path: model the conflict - coalescent methods with model-adequacy checks - and report branch support honestly. Proposed mechanism: a family protocol with gene-tree/species-tree reconciliation, model-adequacy testing, and disputed branches marked with the conflict shown. Confirm: reconciled trees stabilize deep nodes. Kill: the deep nodes stay unresolvable. Does NOT claim: the true tree - it marks the disputed ancestors.",
 "pointer": "The Signature system's proposed approach reconciles gene trees with model-adequacy checks; the companion Signature Edition record specifies the family protocol.",
 "key_points": [
  "Gene-tree/species-tree conflict from ILS and hybridization.",
  "Substitution models are approximate.",
  "Deep-time signal eroded.",
  "Deep nodes most debated.",
 ],
 "requirements": [
  "Coalescent gene-tree reconciliation.",
  "Model-adequacy testing.",
  "Honest conflict reporting on branches.",
 ],
 "citations": [
  "Kapli P et al. (2020) Phylogenetic tree building in the genomic age. Nature Reviews Genetics 21.",
 ],
 "demo": {"seed": 7, "length": 80},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "bf-orthology",
 "name": "The Orthology Problem",
 "group": "Evolution",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "Finding the 'same' gene across species - but how can orthologs be distinguished from paralogs when duplications tangle the history?",
 "background": "The orthology problem - orthologs (speciation-separated) vs paralogs (duplication-separated) - underlies all functional transfer: the ortholog conjecture (orthologs more functionally similar) is debated, and the inference methods (reciprocal best hits, tree-based: OrthoFinder, OMA) disagree on hard cases. Whole-genome duplications and rampant microbial HGT tangle the histories. The functional annotation transferred across species rests on orthology calls that are method-dependent.",
 "why_it_matters": "Function prediction across species assumes orthology. The method-dependent calls are the transferred annotation's risk.",
 "sig_lens": "The Signature lens reads orthology as the identity check: the protocol must verify identity (tree-based) before transferring the reputation (function).",
 "sig_solution": LABEL + " Assumptions: (1) methods disagree on hard cases; (2) ortholog conjecture debated. Reasoning path: call orthology tree-aware and transfer function cautiously with confidence. Proposed mechanism: an identity protocol with tree-based orthology inference, function-transfer confidence scores, and conjecture testing per family. Confirm: tree-aware calls improve transfer accuracy. Kill: the histories stay untangleable. Does NOT claim: perfect orthology - it verifies before transferring.",
 "pointer": "The Signature system's proposed approach infers orthology tree-aware with scored function transfer; the companion Signature Edition record specifies the identity protocol.",
 "key_points": [
  "Orthologs vs paralogs: speciation vs duplication.",
  "Methods (RBH, tree-based) disagree on hard cases.",
  "Ortholog conjecture (function similarity) debated.",
  "WGD and HGT tangle histories.",
 ],
 "requirements": [
  "Tree-based orthology inference.",
  "Confidence-scored function transfer.",
  "Per-family conjecture testing.",
 ],
 "citations": [
  "Emms DM, Kelly S (2019) OrthoFinder: phylogenetic orthology inference. Genome Biology 20.",
 ],
 "demo": {"seed": 8, "length": 70},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "bf-motif",
 "name": "The Motif Discovery Problem",
 "group": "Regulation",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "Transcription factors bind short, degenerate motifs - but how can the true binding sites be found among the genomic noise?",
 "background": "The motif-discovery problem - finding TF binding motifs in sequences - is challenged by degeneracy (the motif occurs by chance everywhere), the in-vivo context (chromatin, cofactors decide binding, not sequence alone), and the motif's inadequacy (PWMs miss dependencies). ChIP-seq finds bound regions; the motif within is still inferred. The sequence-to-binding map is probabilistic; the predictions' false-positive rates are high. The regulatory code's words are found; their meanings are contextual.",
 "why_it_matters": "Gene regulation is motif-driven. The noisy motif predictions are the regulatory network's false edges.",
 "sig_lens": "The Signature lens reads motifs as the words: the protocol must learn the grammar (context) that decides which word occurrences are real sentences.",
 "sig_solution": LABEL + " Assumptions: (1) motifs degenerate; chance occurrences everywhere; (2) context decides binding. Reasoning path: predict binding with context - chromatin, cofactors, and motif syntax jointly. Proposed mechanism: a words protocol with context-aware binding prediction, in-vivo validation (ChIP, MPRA), and false-positive-controlled motif scans. Confirm: context-aware predictions validate better. Kill: the context proves too complex. Does NOT claim: the regulatory code - it learns the grammar.",
 "pointer": "The Signature system's proposed approach predicts TF binding with genomic context; the companion Signature Edition record specifies the words protocol.",
 "key_points": [
  "TF motifs short and degenerate.",
  "Chromatin and cofactors decide in-vivo binding.",
  "PWMs miss positional dependencies.",
  "Motif scans have high false-positive rates.",
 ],
 "requirements": [
  "Context-aware binding prediction.",
  "In-vivo validation of predictions.",
  "False-positive-controlled motif scanning.",
 ],
 "citations": [
  "Stormo GD (2000) DNA binding sites: representation and discovery. Bioinformatics 16.",
 ],
 "demo": {"seed": 9, "length": 60},
},
# ----------------------------------------------------------------- rank 10
{
 "key": "bf-rna-structure",
 "name": "The RNA Structure Prediction Problem",
 "group": "Sequences",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "RNA folds into functional shapes - but how can the structure be predicted when pseudoknots and dynamics defeat the algorithms?",
 "background": "The RNA-structure problem - secondary and tertiary prediction - is harder than proteins': the energy models are less accurate, pseudoknots break the dynamic programming, and the functional structure is often the ensemble, not one fold. Deep learning (like protein's AlphaFold moment) is arriving but the data (structures) is sparser. RNA therapeutics (mRNA vaccines) need the structure-function map. The folded RNA's shape is predicted approximately.",
 "why_it_matters": "RNA drugs and vaccines need the structure-function map. The approximate predictions are the design gap.",
 "sig_lens": "The Signature lens reads RNA as the origami: the protocol must predict the folds - including the hard creases (pseudoknots) - and the moving paper (dynamics).",
 "sig_solution": LABEL + " Assumptions: (1) energy models less accurate; (2) pseudoknots break algorithms. Reasoning path: learn from data - deep-learning structure prediction trained on the growing structure set, with ensemble outputs. Proposed mechanism: an origami protocol with data-driven RNA structure prediction, pseudoknot-capable methods, and ensemble (not single-fold) outputs. Confirm: predictions match experimental structures. Kill: the data stays too sparse. Does NOT claim: the RNA fold solved - it learns the origami.",
 "pointer": "The Signature system's proposed approach predicts RNA structures with data-driven ensemble methods; the companion Signature Edition record specifies the origami protocol.",
 "key_points": [
  "RNA energy models less accurate than proteins'.",
  "Pseudoknots defeat dynamic programming.",
  "Functional structure often the ensemble.",
  "Structure data sparser than proteins.",
 ],
 "requirements": [
  "Data-driven RNA structure prediction.",
  "Pseudoknot-capable algorithms.",
  "Ensemble structure outputs.",
 ],
 "citations": [
  "Seetin MG, Mathews DH (2012) RNA structure prediction: an overview of methods. Methods Molecular Biology 905.",
 ],
 "demo": {"seed": 10, "length": 90},
},
# ----------------------------------------------------------------- rank 11
{
 "key": "bf-function-pred",
 "name": "The Protein Function Prediction Problem",
 "group": "Annotation",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "Most proteins lack experimental functional annotation - but how can function be predicted reliably for the uncharacterized majority?",
 "background": "The function-prediction problem - the annotation gap (most proteins uncharacterized) - is attacked by homology transfer (unreliable at distance), genomic context, and deep learning (CAFA challenge): the best methods achieve useful but imperfect accuracy, and the evaluation (CAFA) shows slow progress on the hard cases. The moonlighting proteins (multiple functions) and the condition-dependent functions defeat simple labels. The uncharacterized majority grows faster than the characterized minority.",
 "why_it_matters": "Functional annotation is the genome's meaning. The uncharacterized majority is biology's unread majority.",
 "sig_lens": "The Signature lens reads function prediction as the job interview: the protocol must check references (homology), skills tests (assays), and never hire on the resume alone.",
 "sig_solution": LABEL + " Assumptions: (1) homology transfer unreliable at distance; (2) CAFA shows slow hard-case progress. Reasoning path: predict with uncertainty and verify - probabilistic function assignments with targeted experimental validation. Proposed mechanism: an interview protocol with uncertainty-quantified function prediction, validation prioritized by uncertainty and importance, and moonlighting-aware multi-label outputs. Confirm: validated predictions accumulate. Kill: the hard cases stay unpredictable. Does NOT claim: functions predicted - it interviews carefully.",
 "pointer": "The Signature system's proposed approach predicts protein function with uncertainty and validation; the companion Signature Edition record specifies the interview protocol.",
 "key_points": [
  "Most proteins lack experimental annotation.",
  "Homology transfer unreliable at distance.",
  "CAFA shows slow progress on hard cases.",
  "Moonlighting and condition-dependence defeat labels.",
 ],
 "requirements": [
  "Uncertainty-quantified function prediction.",
  "Validation prioritized by uncertainty.",
  "Multi-label moonlighting-aware outputs.",
 ],
 "citations": [
  "Radivojac P et al. (2013) A large-scale evaluation of computational protein function prediction (CAFA1). Nature Methods 10.",
 ],
 "demo": {"seed": 11, "length": 80},
},
# ----------------------------------------------------------------- rank 12
{
 "key": "bf-binning",
 "name": "The Metagenomic Binning Problem",
 "group": "Metagenomics",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "Environmental DNA mixes thousands of species - but how can the fragments be sorted into genomes (bins) when most species are unknown?",
 "background": "The binning problem - clustering metagenomic contigs into metagenome-assembled genomes (MAGs) - uses composition and coverage signals, but the bins are imperfect: contamination (mixed species), incompleteness (missing parts), and the strain-level confusion. The quality standards (MIMAG) define high-quality drafts, but most MAGs are medium-quality. The unknown species (microbial dark matter) bin worst - the method needs references it lacks. The sorted genomes are drafts with known flaws.",
 "why_it_matters": "MAGs are the genomes of the uncultured majority. Their flaws are microbiology's knowledge gaps.",
 "sig_lens": "The Signature lens reads binning as the sorting: the protocol must sort honestly - reporting contamination and completeness - and improve the sort with long reads.",
 "sig_solution": LABEL + " Assumptions: (1) bins imperfect: contamination, incompleteness; (2) unknown species bin worst. Reasoning path: sort better - long-read metagenomics, Hi-C linkage, and honest quality reporting. Proposed mechanism: a sorting protocol with long-read-first metagenomics, Hi-C-binning integration, and MIMAG-strict quality reporting. Confirm: high-quality MAG counts rise. Kill: the strains stay unresolvable. Does NOT claim: perfect bins - it sorts honestly.",
 "pointer": "The Signature system's proposed approach improves metagenomic binning with long reads and Hi-C; the companion Signature Edition record specifies the sorting protocol.",
 "key_points": [
  "Binning uses composition and coverage signals.",
  "Bins suffer contamination and incompleteness.",
  "MIMAG defines quality tiers; most MAGs medium.",
  "Unknown species bin worst.",
 ],
 "requirements": [
  "Long-read metagenomic assembly.",
  "Hi-C linkage binning.",
  "MIMAG-strict quality reporting.",
 ],
 "citations": [
  "Bowers RM et al. (2017) Minimum information about a single amplified genome (MISAG) and MAG (MIMAG). Nature Biotechnology 35.",
 ],
 "demo": {"seed": 12, "length": 100},
},
# ----------------------------------------------------------------- rank 13
{
 "key": "bf-single-cell",
 "name": "The Single Cell Data Integration Problem",
 "group": "Single Cell",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "Single-cell experiments each capture one modality - but how can RNA, chromatin, and protein measurements from different cells be integrated?",
 "background": "The single-cell integration problem - combining scRNA-seq, scATAC-seq, CITE-seq across batches and modalities - is the atlas challenge: batch effects confound biology, the modalities measure different cells (requiring diagonal integration), and the integration methods (Seurat, Harmony, scVI) each distort differently. The Human Cell Atlas needs the integrated map; the methods' distortions are the map's errors. The cells are measured; their joint portrait is assembled approximately.",
 "why_it_matters": "Cell atlases organize all single-cell biology. The integration distortions are the atlas's misdrawn borders.",
 "sig_lens": "The Signature lens reads integration as the portrait assembly: the protocol must align the sketches (modalities) without distorting the faces (biology).",
 "sig_solution": LABEL + " Assumptions: (1) batch effects confound; (2) methods distort differently. Reasoning path: integrate with distortion checks - benchmark on ground-truth (multiome same-cell) data. Proposed mechanism: a portrait protocol with same-cell multiome ground truth, distortion-benchmarked integration methods, and batch-effect reporting. Confirm: benchmarked integration preserves biology. Kill: the distortions prove unavoidable. Does NOT claim: perfect integration - it assembles without distorting.",
 "pointer": "The Signature system's proposed approach benchmarks single-cell integration on same-cell ground truth; the companion Signature Edition record specifies the portrait protocol.",
 "key_points": [
  "Modalities often measure different cells.",
  "Batch effects confound biological signal.",
  "Integration methods distort differently.",
  "Multiome same-cell data is the ground truth.",
 ],
 "requirements": [
  "Same-cell multiome benchmarking.",
  "Distortion-checked integration methods.",
  "Batch-effect reporting.",
 ],
 "citations": [
  "Stuart T et al. (2019) Comprehensive integration of single-cell data. Cell 177.",
 ],
 "demo": {"seed": 13, "length": 70},
},
# ----------------------------------------------------------------- rank 14
{
 "key": "bf-spatial",
 "name": "The Spatial Transcriptomics Problem",
 "group": "Single Cell",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "Tissues organize gene expression in space - but how can the spatial patterns be resolved at single-cell resolution across whole tissues?",
 "background": "The spatial problem - mapping transcripts in tissue space - trades resolution for area: Visium (55-micron spots, multi-cell), MERFISH/seqFISH (single-molecule, limited genes/area), Slide-seq (10-micron, limited sensitivity). The computational challenges (cell segmentation, spot deconvolution) are unsolved at scale; the 3D tissue reconstruction is nascent. The tissue's geography is mapped at mismatched scales.",
 "why_it_matters": "Tissue function is spatial. The mismatched-scale maps are the histology's missing molecular layer.",
 "sig_lens": "The Signature lens reads spatial transcriptomics as the map: the protocol must draw it at the right scale - single cells across whole tissues - and verify the borders.",
 "sig_solution": LABEL + " Assumptions: (1) resolution-area tradeoff; (2) segmentation/deconvolution unsolved at scale. Reasoning path: combine scales - pair high-resolution targeted with broad unbiased, and deconvolve with single-cell references. Proposed mechanism: a map protocol with multi-scale spatial integration, reference-based deconvolution, and 3D tissue reconstruction. Confirm: the maps validate histologically. Kill: the tradeoff proves fundamental. Does NOT claim: the full spatial map - it draws at the right scale.",
 "pointer": "The Signature system's proposed approach integrates spatial transcriptomics across scales; the companion Signature Edition record specifies the map protocol.",
 "key_points": [
  "Visium: broad but multi-cell spots.",
  "MERFISH: single-molecule but limited genes/area.",
  "Cell segmentation unsolved at scale.",
  "3D tissue reconstruction nascent.",
 ],
 "requirements": [
  "Multi-scale spatial integration.",
  "Reference-based spot deconvolution.",
  "3D tissue reconstruction methods.",
 ],
 "citations": [
  "Marx V (2021) Method of the year: spatially resolved transcriptomics. Nature Methods 18.",
 ],
 "demo": {"seed": 14, "length": 80},
},
# ----------------------------------------------------------------- rank 15
{
 "key": "bf-long-read",
 "name": "The Long Read Assembly Problem",
 "group": "Sequences",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "Long reads span repeats - but how can their higher error rates be handled, and what is the best assembly strategy?",
 "background": "The long-read problem - PacBio/Nanopore error profiles (random vs systematic) - is easing (HiFi: long and accurate) but the assembly strategies (overlap-based: hifiasm, Flye) still face: diploid phasing (haplotype-resolved assembly), the remaining hard repeats (centromeres, rDNA), and the compute costs. The telomere-to-telomere human genome (T2T-CHM13) proved it possible; the routine diploid T2T is the goal. The reads are long; the phasing is hard.",
 "why_it_matters": "Haplotype-resolved genomes are the diploid truth. The unphased assemblies are the collapsed diploid.",
 "sig_lens": "The Signature lens reads long-read assembly as the diploid jigsaw: the protocol must separate the two pictures (haplotypes) while assembling.",
 "sig_solution": LABEL + " Assumptions: (1) HiFi eased errors; (2) phasing and hard repeats remain. Reasoning path: phase while assembling - trio/Hi-C-phased long-read assembly to diploid T2T. Proposed mechanism: a diploid protocol with phased assembly pipelines, hard-repeat resolution methods, and diploid-completeness reporting. Confirm: routine diploid T2T achieved. Kill: the hard repeats stay unresolvable. Does NOT claim: routine diploid T2T - it separates the pictures.",
 "pointer": "The Signature system's proposed approach phases diploid genome assembly with long reads; the companion Signature Edition record specifies the diploid protocol.",
 "key_points": [
  "HiFi reads: long and accurate.",
  "Diploid phasing remains hard.",
  "Centromeres and rDNA resist assembly.",
  "T2T-CHM13 proved haploid T2T possible.",
 ],
 "requirements": [
  "Trio/Hi-C-phased assembly pipelines.",
  "Hard-repeat resolution methods.",
  "Diploid-completeness reporting.",
 ],
 "citations": [
  "Nurk S et al. (2022) The complete sequence of a human genome (T2T-CHM13). Science 376.",
 ],
 "demo": {"seed": 15, "length": 110},
},
# ----------------------------------------------------------------- rank 16
{
 "key": "bf-sv",
 "name": "The Structural Variant Problem",
 "group": "Variation",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "Large DNA rearrangements cause disease - but how can structural variants be detected reliably when short reads miss them?",
 "background": "The SV problem - deletions, duplications, inversions, translocations - is the variant caller's blind spot: short reads infer SVs indirectly (split reads, read pairs) with high false rates; long reads see them directly but the callers (Sniffles, pbsv) are young. The population SV catalogs are incomplete; the clinical interpretation lags SNPs by years. The large variants - the most consequential - are the least reliably called.",
 "why_it_matters": "SVs cause genomic disorders and cancer. The unreliable calls are the missed diagnoses.",
 "sig_lens": "The Signature lens reads SVs as the large print: the protocol must read it directly (long reads) - and build the population catalog the clinics need.",
 "sig_solution": LABEL + " Assumptions: (1) short reads infer SVs unreliably; (2) catalogs incomplete. Reasoning path: detect directly - long-read SV calling with population catalogs. Proposed mechanism: a print protocol with long-read SV detection, population SV reference catalogs, and clinical SV interpretation guidelines. Confirm: the catalogs enable diagnoses. Kill: the callers stay unreliable. Does NOT claim: all SVs found - it reads the large print directly.",
 "pointer": "The Signature system's proposed approach detects structural variants with long reads and population catalogs; the companion Signature Edition record specifies the print protocol.",
 "key_points": [
  "Short-read SV inference has high false rates.",
  "Long-read callers are young but direct.",
  "Population SV catalogs incomplete.",
  "Clinical SV interpretation lags SNPs.",
 ],
 "requirements": [
  "Long-read SV detection pipelines.",
  "Population SV reference catalogs.",
  "Clinical interpretation guidelines.",
 ],
 "citations": [
  "Mahmoud M et al. (2019) Structural variant calling: the long and the short of it. Genome Biology 20.",
 ],
 "demo": {"seed": 16, "length": 90},
},
# ----------------------------------------------------------------- rank 17
{
 "key": "bf-epigenome",
 "name": "The Epigenomic Data Integration Problem",
 "group": "Regulation",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "Chromatin marks, accessibility, and methylation each describe regulation - but how can the epigenomic layers be integrated into a coherent model?",
 "background": "The epigenomic-integration problem - ChromHMM/Segway segmentations combine marks, but the layers' joint logic (which mark combinations mean what, causally) is unmapped: the Roadmap/ENCODE segmentations are descriptive; the predictive models (Basenji, Enformer) learn sequence-to-epigenome but opaquely. The single-cell epigenome adds the cell-type dimension. The layers are measured; their joint grammar is unlearned.",
 "why_it_matters": "Disease variants act through the epigenome. The unlearned joint grammar is the variant-interpretation gap.",
 "sig_lens": "The Signature lens reads the epigenome as the multi-track recording: the protocol must mix the tracks (layers) into the song (regulatory logic) - and test the mix.",
 "sig_solution": LABEL + " Assumptions: (1) segmentations descriptive; (2) predictive models opaque. Reasoning path: integrate interpretably - joint models with causal testing via epigenome editing. Proposed mechanism: a tracks protocol with interpretable multi-layer models, causal validation (dCas9 epigenome editing), and variant-effect prediction on the integrated model. Confirm: the integrated models predict variant effects. Kill: the layers prove unintegrable interpretably. Does NOT claim: the epigenomic grammar - it mixes the tracks.",
 "pointer": "The Signature system's proposed approach integrates epigenomic layers with causal validation; the companion Signature Edition record specifies the tracks protocol.",
 "key_points": [
  "ChromHMM/Segway segmentations are descriptive.",
  "Sequence-to-epigenome models (Enformer) are opaque.",
  "Joint causal logic of mark combinations unmapped.",
  "Single-cell adds the cell-type dimension.",
 ],
 "requirements": [
  "Interpretable multi-layer integration models.",
  "Causal epigenome-editing validation.",
  "Variant-effect prediction on integrated models.",
 ],
 "citations": [
  "Ernst J, Kellis M (2012) ChromHMM: automating chromatin-state discovery. Nature Methods 9.",
 ],
 "demo": {"seed": 17, "length": 80},
},
# ----------------------------------------------------------------- rank 18
{
 "key": "bf-network",
 "name": "The Network Inference Problem",
 "group": "Systems",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "Gene regulatory networks control the cell - but how can the true network be inferred from expression data when correlation is not causation?",
 "background": "The network-inference problem - GRNs from expression (DREAM challenge) - is humbling: the best methods achieve modest accuracy on benchmarks, correlation confounds causation, and the ground truth (the true network) is unknown for real cells. Single-cell data adds resolution and dropout noise; perturbation screens (Perturb-seq) provide causal ground truth partially. The inferred networks are hypotheses; their validation rate is low.",
 "why_it_matters": "GRNs are the cell's wiring diagram. The low-validation inferences are the miswired diagrams.",
 "sig_lens": "The Signature lens reads network inference as the wiring guess: the protocol must test each wire (perturbation) - and report the guess's accuracy honestly.",
 "sig_solution": LABEL + " Assumptions: (1) DREAM shows modest accuracy; (2) ground truth unknown. Reasoning path: infer causally - perturbation-based (Perturb-seq) networks with benchmarked accuracy. Proposed mechanism: a wiring protocol with perturbation-grounded network inference, accuracy benchmarking on interventional data, and hypothesis-graded network edges. Confirm: the inferred networks validate. Kill: the accuracy stays modest. Does NOT claim: the true network - it tests each wire.",
 "pointer": "The Signature system's proposed approach infers regulatory networks from perturbation data; the companion Signature Edition record specifies the wiring protocol.",
 "key_points": [
  "DREAM challenge: modest inference accuracy.",
  "Correlation confounds causation.",
  "True networks unknown for real cells.",
  "Perturb-seq provides partial causal truth.",
 ],
 "requirements": [
  "Perturbation-grounded network inference.",
  "Interventional accuracy benchmarking.",
  "Hypothesis-graded network edges.",
 ],
 "citations": [
  "Marbach D et al. (2012) Wisdom of crowds for robust gene network inference (DREAM5). Nature Methods 9.",
 ],
 "demo": {"seed": 18, "length": 70},
},
# ----------------------------------------------------------------- rank 19
{
 "key": "bf-enrichment",
 "name": "The Pathway Enrichment Problem",
 "group": "Systems",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "Gene lists need biological meaning - but how can pathway enrichment be done when the pathways overlap, the databases disagree, and the statistics are fragile?",
 "background": "The enrichment problem - GSEA, over-representation analysis - is the most-run and most-misused bioinformatics: pathway databases (GO, KEGG, Reactome) disagree on membership; overlapping pathways double-count; the gene-set statistics assume independence that genes violate. The results guide the biology - and the fragility is underappreciated. The most-used analysis is the least-robust.",
 "why_it_matters": "Enrichment results steer biological interpretation. The fragile statistics are the misled interpretations.",
 "sig_lens": "The Signature lens reads enrichment as the library search: the protocol must know the catalogs disagree (databases) - and report the search's uncertainty.",
 "sig_solution": LABEL + " Assumptions: (1) databases disagree; pathways overlap; (2) independence assumptions violated. Reasoning path: enrich robustly - multi-database consensus with redundancy-aware statistics. Proposed mechanism: a library protocol with consensus pathway annotations, redundancy-aware enrichment statistics, and uncertainty-reported results. Confirm: robust enrichments replicate better. Kill: the databases never agree. Does NOT claim: the true pathways - it searches honestly.",
 "pointer": "The Signature system's proposed approach makes pathway enrichment redundancy-aware and consensus-based; the companion Signature Edition record specifies the library protocol.",
 "key_points": [
  "GO, KEGG, Reactome disagree on membership.",
  "Overlapping pathways double-count signals.",
  "Independence assumptions violated by genes.",
  "Most-run analysis; least-robust.",
 ],
 "requirements": [
  "Consensus pathway annotations.",
  "Redundancy-aware enrichment statistics.",
  "Uncertainty-reported enrichment results.",
 ],
 "citations": [
  "Subramanian A et al. (2005) Gene set enrichment analysis. PNAS 102.",
 ],
 "demo": {"seed": 19, "length": 60},
},
# ----------------------------------------------------------------- rank 20
{
 "key": "bf-biomarker",
 "name": "The Biomarker Discovery Problem",
 "group": "Medicine",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "Omics promises disease biomarkers - but why do so few discovered biomarkers validate, and how can the pipeline be fixed?",
 "background": "The biomarker problem - the discovery-to-clinic attrition - is the omics reproducibility crisis in miniature: overfit signatures, batch-confounded discoveries, and the validation gap (few biomarkers survive independent cohorts). The FDA-approved omics biomarkers are few. The fixes (pre-registration, independent validation, prospective trials) are known but underused. The discovered markers are mostly false; the pipeline leaks.",
 "why_it_matters": "Biomarkers guide treatment. The false discoveries are the misled treatments.",
 "sig_lens": "The Signature lens reads biomarkers as the diagnostic claim: the protocol must prove the claim - in independent cohorts, prospectively - before the clinic.",
 "sig_solution": LABEL + " Assumptions: (1) overfit, batch-confounded discoveries dominate; (2) validation fixes known, underused. Reasoning path: validate before claiming - locked signatures, independent cohorts, prospective trials. Proposed mechanism: a claim protocol with pre-registered biomarker signatures, mandatory independent validation, and prospective-trial gating for clinical use. Confirm: validated biomarkers reach the clinic. Kill: the pipeline stays leaky. Does NOT claim: the biomarkers - it proves the claims.",
 "pointer": "The Signature system's proposed approach gates biomarkers on independent prospective validation; the companion Signature Edition record specifies the claim protocol.",
 "key_points": [
  "Most discovered biomarkers fail validation.",
  "Overfitting and batch confounding dominate.",
  "FDA-approved omics biomarkers few.",
  "Pre-registration and prospective trials underused.",
 ],
 "requirements": [
  "Pre-registered biomarker signatures.",
  "Mandatory independent-cohort validation.",
  "Prospective-trial gating for clinical use.",
 ],
 "citations": [
  "Ioannidis JPA, Panagiotou OA (2011) Comparison of effect sizes in omics biomarkers. JAMA 305.",
 ],
 "demo": {"seed": 20, "length": 80},
},
# ----------------------------------------------------------------- rank 21
{
 "key": "bf-drug-target",
 "name": "The Drug Target Prediction Problem",
 "group": "Medicine",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "Genomics nominates drug targets - but how can the truly druggable, disease-causing targets be picked from the genomic noise?",
 "background": "The target problem - from GWAS/omics to validated drug targets - has a translation gap: most GWAS hits are noncoding with unclear genes; the druggability (pocket, chemistry) is predictable only roughly; and the causal inference (Mendelian randomization) is assumption-laden. The successes (PCSK9 from genetics) are the template; the failures are the norm. The nominated targets are mostly noise.",
 "why_it_matters": "Drug targets decide pipelines worth billions. The noisy nominations are the failed pipelines.",
 "sig_lens": "The Signature lens reads target prediction as the prospecting: the protocol must assay the ore (causality, druggability) - not just pan the stream (GWAS).",
 "sig_solution": LABEL + " Assumptions: (1) GWAS hits mostly noncoding, unclear genes; (2) druggability roughly predictable. Reasoning path: prospect rigorously - causal inference plus druggability plus genetic validation (human knockouts). Proposed mechanism: a prospecting protocol with causal target prioritization, druggability assessment, and human-genetic validation. Confirm: the prioritized targets succeed more. Kill: the translation gap persists. Does NOT claim: the drug targets - it assays the ore.",
 "pointer": "The Signature system's proposed approach prioritizes drug targets with causal and druggability evidence; the companion Signature Edition record specifies the prospecting protocol.",
 "key_points": [
  "GWAS hits mostly noncoding; causal genes unclear.",
  "Druggability predictable only roughly.",
  "Mendelian randomization assumption-laden.",
  "PCSK9 is the template success.",
 ],
 "requirements": [
  "Causal target prioritization.",
  "Druggability assessment.",
  "Human-genetic validation.",
 ],
 "citations": [
  "Nelson MR et al. (2015) The support of human genetic evidence for approved drug indications. Nature Genetics 47.",
 ],
 "demo": {"seed": 21, "length": 70},
},
# ----------------------------------------------------------------- rank 22
{
 "key": "bf-crispr-off",
 "name": "The CRISPR Off Target Problem",
 "group": "Genome Editing",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "CRISPR edits the target - but how can all off-target edits be found, and how can the editors be made specific enough for therapy?",
 "background": "The off-target problem - Cas9's unintended edits - is the therapeutic gate: detection methods (GUIDE-seq, CIRCLE-seq, CHANGE-seq) each miss classes; the in-vivo off-target landscape differs from in-vitro; and the high-fidelity editors (SpCas9-HF, base/prime editors) trade efficiency for specificity. The therapeutic bar (no consequential off-targets) needs assays the field is still building. The editor is powerful; its precision is half-measured.",
 "why_it_matters": "Therapeutic editing needs proven specificity. The half-measured precision is the safety gap.",
 "sig_lens": "The Signature lens reads off-target as the stray cuts: the protocol must find every cut (unbiased detection) - and sharpen the blade (fidelity) - before therapy.",
 "sig_solution": LABEL + " Assumptions: (1) detection methods each miss classes; (2) in-vivo differs from in-vitro. Reasoning path: detect comprehensively - multi-method off-target profiling in the therapeutic context. Proposed mechanism: a cuts protocol with multi-assay off-target detection, therapeutic-context profiling, and fidelity-efficiency co-optimization. Confirm: the editors pass comprehensive profiling. Kill: the off-targets stay unfindable. Does NOT claim: the editors safe - it finds every cut.",
 "pointer": "The Signature system's proposed approach profiles CRISPR off-targets comprehensively in therapeutic context; the companion Signature Edition record specifies the cuts protocol.",
 "key_points": [
  "Detection methods (GUIDE/CIRCLE/CHANGE-seq) each miss classes.",
  "In-vivo off-targets differ from in-vitro.",
  "High-fidelity editors trade efficiency.",
  "Therapeutic bar needs better assays.",
 ],
 "requirements": [
  "Multi-assay off-target detection.",
  "Therapeutic-context profiling.",
  "Fidelity-efficiency co-optimization.",
 ],
 "citations": [
  "Tsai SQ, Joung JK (2016) Defining and improving the genome-wide specificities of CRISPR-Cas nucleases. Nature Reviews Genetics 17.",
 ],
 "demo": {"seed": 22, "length": 60},
},
# ----------------------------------------------------------------- rank 23
{
 "key": "bf-base-edit",
 "name": "The Base Editing Prediction Problem",
 "group": "Genome Editing",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "Base editors rewrite single letters - but how can the editing outcomes (bystanders, efficiency) be predicted for any target?",
 "background": "The base-editing problem - predicting ABE/CBE outcomes - is the precision-editing frontier: the editing window's bystander edits, the sequence-context dependence, and the off-target deamination are predictable only roughly (BE-Hive, DeepBaseEditor models). The therapeutic edits need exact predictions; the models are approximate. The prime-editing outcomes are even harder. The letter-rewriters' accuracy is half-predicted.",
 "why_it_matters": "Therapeutic base editing needs exact outcome predictions. The approximate models are the dosing uncertainty.",
 "sig_lens": "The Signature lens reads base editing as the letter rewrite: the protocol must predict every letter changed (bystanders included) - exactly.",
 "sig_solution": LABEL + " Assumptions: (1) bystander edits context-dependent; (2) models approximate. Reasoning path: predict exactly - train on comprehensive outcome libraries with the therapeutic context. Proposed mechanism: a letters protocol with outcome-library-trained predictors, bystander-inclusive predictions, and therapeutic-context validation. Confirm: the predictions match therapeutic outcomes. Kill: the context-dependence defeats prediction. Does NOT claim: exact predictions - it learns every letter.",
 "pointer": "The Signature system's proposed approach predicts base-editing outcomes including bystanders; the companion Signature Edition record specifies the letters protocol.",
 "key_points": [
  "Bystander edits within the window.",
  "Sequence-context dependence strong.",
  "BE-Hive/DeepBaseEditor models approximate.",
  "Prime-editing outcomes harder still.",
 ],
 "requirements": [
  "Outcome-library-trained predictors.",
  "Bystander-inclusive predictions.",
  "Therapeutic-context validation.",
 ],
 "citations": [
  "Arbab M et al. (2020) Determinants of base editing outcomes. Cell 182.",
 ],
 "demo": {"seed": 23, "length": 70},
},
# ----------------------------------------------------------------- rank 24
{
 "key": "bf-pangenome",
 "name": "The Pangenome Problem",
 "group": "Variation",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "One reference genome cannot represent a species - but how can the pangenome (all genes of all strains) be built and used?",
 "background": "The pangenome problem - the species' full gene set (core + accessory) - is solved conceptually but open practically: the pangenome's size estimation (open vs closed), the accessory genome's function, and the reference-structure (how to represent and map to a pangenome) are active. Microbial pangenomes are vast; the human pangenome (HPRC) is being built. The single reference is obsolete; the pangenome's use is young.",
 "why_it_matters": "The pangenome is the species' true genome. The single reference's bias is the missed variation.",
 "sig_lens": "The Signature lens reads the pangenome as the species' library: the protocol must shelve every book (strain) - and make the catalog searchable.",
 "sig_solution": LABEL + " Assumptions: (1) single reference obsolete; (2) pangenome use young. Reasoning path: build and use - complete pangenome references with graph-based mapping. Proposed mechanism: a library protocol with pangenome reference construction, graph-genome mapping tools, and accessory-genome functional studies. Confirm: the pangenomes improve mapping and discovery. Kill: the pangenomes prove unusable at scale. Does NOT claim: the complete pangenome - it shelves every book.",
 "pointer": "The Signature system's proposed approach builds usable pangenome references with graph mapping; the companion Signature Edition record specifies the library protocol.",
 "key_points": [
  "Pangenome: core + accessory genes.",
  "Open vs closed pangenome estimation open.",
  "Human Pangenome Reference Consortium building.",
  "Graph mapping needed for pangenome use.",
 ],
 "requirements": [
  "Pangenome reference construction.",
  "Graph-genome mapping tools.",
  "Accessory-genome functional studies.",
 ],
 "citations": [
  "Liao WW et al. (2023) A draft human pangenome reference. Nature 617.",
 ],
 "demo": {"seed": 24, "length": 90},
},
# ----------------------------------------------------------------- rank 25
{
 "key": "bf-graph-genome",
 "name": "The Graph Genome Problem",
 "group": "Variation",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "Genomes vary - but how can the linear reference be replaced by a graph that represents all variation?",
 "background": "The graph-genome problem - replacing the linear reference with variation graphs - is the infrastructure challenge: the graph construction (which variants, which populations), the mapping algorithms (vg, GraphAligner), and the ecosystem migration (all tools assume linear coordinates) are each hard. The benefits (no reference bias, SV representation) are proven in principle; the adoption is slow. The linear reference's retirement is scheduled but not executed.",
 "why_it_matters": "Graph genomes end reference bias. The slow migration is the field's infrastructure debt.",
 "sig_lens": "The Signature lens reads graph genomes as the new shelving: the protocol must rebuild the library (tools) on the new shelves - without losing the books.",
 "sig_solution": LABEL + " Assumptions: (1) benefits proven in principle; (2) ecosystem migration slow. Reasoning path: migrate the ecosystem - graph-native tools with linear-coordinate bridges. Proposed mechanism: a shelves protocol with graph-genome tool development, coordinate-translation bridges, and population-representative graph construction. Confirm: the graph ecosystem matures. Kill: the migration stalls. Does NOT claim: the linear reference retired - it rebuilds the shelves.",
 "pointer": "The Signature system's proposed approach migrates genomics to graph-genome infrastructure; the companion Signature Edition record specifies the shelves protocol.",
 "key_points": [
  "Variation graphs end reference bias.",
  "Graph construction choices (variants, populations) hard.",
  "Mapping algorithms (vg) developing.",
  "Tool ecosystem assumes linear coordinates.",
 ],
 "requirements": [
  "Graph-native tool development.",
  "Linear-graph coordinate bridges.",
  "Population-representative graphs.",
 ],
 "citations": [
  "Garrison E et al. (2018) Variation graph toolkit (vg). Nature Biotechnology 36.",
 ],
 "demo": {"seed": 25, "length": 80},
},
# ----------------------------------------------------------------- rank 26
{
 "key": "bf-t2t",
 "name": "The Telomere to Telomere Problem",
 "group": "Sequences",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "The first complete human genome (T2T-CHM13) is done - but how can every genome be finished telomere-to-telomere, including diploid human genomes?",
 "background": "The T2T problem - complete genomes gaplessly - was solved for one haploid genome (CHM13) but the generalization is open: diploid T2T (both haplotypes complete), the remaining hard repeats' biology (centromere function, rDNA), and the T2T-for-all cost. The complete genome revealed millions of new variants in the former gaps. The finished genome is the exception; the draft is the rule.",
 "why_it_matters": "The gaps held millions of variants. The unfinished genomes are the missing variation.",
 "sig_lens": "The Signature lens reads T2T as the finished book: the protocol must finish every copy (diploid) - and read the former blank pages (gaps).",
 "sig_solution": LABEL + " Assumptions: (1) CHM13 proved haploid T2T; (2) diploid T2T the goal. Reasoning path: finish diploid - phased long-read T2T pipelines with gap-biology studies. Proposed mechanism: a book protocol with diploid-T2T pipelines, former-gap variant catalogs, and centromere/rDNA functional studies. Confirm: diploid T2T routine. Kill: the diploid gaps resist. Does NOT claim: every genome finished - it finishes the copies.",
 "pointer": "The Signature system's proposed approach finishes diploid telomere-to-telomere genomes; the companion Signature Edition record specifies the book protocol.",
 "key_points": [
  "T2T-CHM13: first complete human genome.",
  "Diploid T2T (both haplotypes) the goal.",
  "Former gaps held millions of variants.",
  "Centromere/rDNA biology newly accessible.",
 ],
 "requirements": [
  "Phased diploid-T2T pipelines.",
  "Former-gap variant catalogs.",
  "Gap-region functional studies.",
 ],
 "citations": [
  "Nurk S et al. (2022) The complete sequence of a human genome. Science 376.",
 ],
 "demo": {"seed": 26, "length": 100},
},
# ----------------------------------------------------------------- rank 27
{
 "key": "bf-dark-genome",
 "name": "The Dark Genome Problem",
 "group": "Annotation",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "Half the genome is annotated as repeats and 'junk' - but how much of the dark genome is functional?",
 "background": "The dark-genome problem - the function fraction of repeats, transposons, and unannotated regions - is the annotation's shadow: ENCODE's biochemical activity vs evolutionary conservation debate; transposons' regulatory roles (emerging); the satellite DNA's function (centromeres excepted, unknown). The 'junk' label is retired; the function map is not drawn. The dark genome is half the genome.",
 "why_it_matters": "Half the genome's function is unmapped. The dark half may run regulation.",
 "sig_lens": "The Signature lens reads the dark genome as the unmapped half: the protocol must survey it - functionally, not just biochemically.",
 "sig_solution": LABEL + " Assumptions: (1) biochemical activity vs conservation debated; (2) transposon roles emerging. Reasoning path: map functionally - systematic perturbation of dark regions with phenotypic readouts. Proposed mechanism: a survey protocol with dark-region perturbation screens, transposon-function studies, and conservation-informed prioritization. Confirm: the functional dark elements identified. Kill: most proves nonfunctional. Does NOT claim: the dark genome mapped - it surveys the half.",
 "pointer": "The Signature system's proposed approach functionally surveys the genome's dark regions; the companion Signature Edition record specifies the survey protocol.",
 "key_points": [
  "Half the genome: repeats, transposons, unannotated.",
  "ENCODE activity vs conservation debate.",
  "Transposon regulatory roles emerging.",
  "Satellite DNA function (beyond centromeres) unknown.",
 ],
 "requirements": [
  "Dark-region perturbation screens.",
  "Transposon-function studies.",
  "Conservation-informed prioritization.",
 ],
 "citations": [
  "de Koning APJ et al. (2011) Repetitive elements may comprise over two-thirds of the human genome. PLoS Genetics 7.",
 ],
 "demo": {"seed": 27, "length": 70},
},
# ----------------------------------------------------------------- rank 28
{
 "key": "bf-microbiome-cause",
 "name": "The Microbiome Causality Problem",
 "group": "Metagenomics",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "Microbiomes correlate with disease - but which microbes cause disease, and how can causality be proven?",
 "background": "The causality problem - correlation vs causation in microbiome studies - is the field's reckoning: the associations (obesity, IBD, autism) are legion; the causal proofs (gnotobiotic transfer, interventional trials) are few. The confounders (diet, drugs, geography) are strong; the effect sizes small. FMT's success (C. difficile) is the causal template; most associations lack it. The correlated microbes are mostly passengers.",
 "why_it_matters": "Microbiome therapies need causal microbes. The passenger associations are the failed trials.",
 "sig_lens": "The Signature lens reads microbiome causality as the suspect lineup: the protocol must prove guilt (gnotobiotics, trials) - not just presence at the scene (association).",
 "sig_solution": LABEL + " Assumptions: (1) associations legion; causal proofs few; (2) confounders strong. Reasoning path: prove causality - gnotobiotic transfer, Mendelian randomization, interventional trials. Proposed mechanism: a lineup protocol with causal-proof standards, confounder-controlled designs, and FMT-template interventional trials. Confirm: the causal microbes identified. Kill: most associations prove confounded. Does NOT claim: the causal microbes - it proves guilt.",
 "pointer": "The Signature system's proposed approach proves microbiome causality with interventional standards; the companion Signature Edition record specifies the lineup protocol.",
 "key_points": [
  "Microbiome-disease associations legion.",
  "Causal proofs (gnotobiotics, trials) few.",
  "Confounders (diet, drugs) strong.",
  "FMT for C. difficile is the causal template.",
 ],
 "requirements": [
  "Causal-proof standards (gnotobiotics, MR, trials).",
  "Confounder-controlled study designs.",
  "Interventional microbiome trials.",
 ],
 "citations": [
  "Fischbach MA (2018) Microbiome: focus on causation and mechanism. Cell 174.",
 ],
 "demo": {"seed": 28, "length": 80},
},
# ----------------------------------------------------------------- rank 29
{
 "key": "bf-multiomics",
 "name": "The Multi Omics Integration Problem",
 "group": "Systems",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "Genomes, transcriptomes, proteomes, metabolomes each describe the cell - but how can the omics layers be integrated into one model?",
 "background": "The multi-omics problem - joint modeling of omics layers - is the systems-biology integration: the layers have different scales, noise, and missingness; the integration methods (MOFA, DIABLO, totalVI) find joint factors but the biological interpretation is hard; and the temporal dynamics (layers change at different speeds) are rarely modeled. The single-cell multiome is the data; the integrated model is the goal. The layers are measured; the cell is not yet modeled.",
 "why_it_matters": "Disease mechanisms span omics layers. The unintegrated layers are the partial mechanisms.",
 "sig_lens": "The Signature lens reads multi-omics as the orchestra: the protocol must hear the sections together - and score the symphony (the joint model).",
 "sig_solution": LABEL + " Assumptions: (1) layers differ in scale, noise, missingness; (2) joint factors hard to interpret. Reasoning path: integrate interpretably - joint models with pathway-anchored factors and temporal dynamics. Proposed mechanism: an orchestra protocol with interpretable multi-omics integration, temporal layer-dynamics modeling, and mechanism validation. Confirm: the integrated models reveal mechanisms. Kill: the layers resist joint modeling. Does NOT claim: the cell modeled - it scores the symphony.",
 "pointer": "The Signature system's proposed approach integrates multi-omics interpretably with dynamics; the companion Signature Edition record specifies the orchestra protocol.",
 "key_points": [
  "Omics layers differ in scale, noise, missingness.",
  "Joint-factor methods (MOFA) hard to interpret.",
  "Temporal layer dynamics rarely modeled.",
  "Single-cell multiome is the data frontier.",
 ],
 "requirements": [
  "Interpretable joint omics models.",
  "Temporal dynamics integration.",
  "Mechanism validation of joint factors.",
 ],
 "citations": [
  "Argelaguet R et al. (2018) Multi-Omics Factor Analysis (MOFA). Molecular Systems Biology 14.",
 ],
 "demo": {"seed": 29, "length": 90},
},
# ----------------------------------------------------------------- rank 30
{
 "key": "bf-digital-twin",
 "name": "The Digital Twin Cell Problem",
 "group": "Systems",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "Can a cell's omics be modeled as a digital twin - predicting its responses - and what would the twin need?",
 "background": "The digital-twin problem - predictive cell models from omics - is the systems-biology moonshot: the whole-cell models (Mycoplasma) are the proof of concept; the human cell's complexity (compartments, stochasticity, unknown parameters) is the barrier. The twin would predict drug responses and perturbations; the parameter gaps and the validation standards are open. The moonshot is named; the rocket is unbuilt.",
 "why_it_matters": "Digital twin cells would predict drug responses in silico. The unbuilt twin is the trial-and-error medicine.",
 "sig_lens": "The Signature lens reads the digital twin as the flight simulator: the protocol must build it module by module - and certify it on predicted flights (perturbations).",
 "sig_solution": LABEL + " Assumptions: (1) Mycoplasma proof of concept; (2) human-cell barriers: parameters, stochasticity. Reasoning path: build modularly - validated module twins integrated with perturbation benchmarks. Proposed mechanism: a simulator protocol with module-twin validation, integration milestones, and perturbation-prediction certification. Confirm: the twin predicts perturbations. Kill: the complexity defeats integration. Does NOT claim: the digital twin - it builds the simulator.",
 "pointer": "The Signature system's proposed approach builds digital-twin cells by validated module integration; the companion Signature Edition record specifies the simulator protocol.",
 "key_points": [
  "Whole-cell Mycoplasma model: proof of concept.",
  "Human cell: compartments, stochasticity, parameter gaps.",
  "Twin would predict drug/perturbation responses.",
  "Validation standards open.",
 ],
 "requirements": [
  "Validated module-twin models.",
  "Integration milestones.",
  "Perturbation-prediction certification.",
 ],
 "citations": [
  "Karr JR et al. (2012) A whole-cell computational model predicts phenotype from genotype. Cell 150.",
 ],
 "demo": {"seed": 30, "length": 100},
},
# ----------------------------------------------------------------- rank 31
{
 "key": "bf-interpretability",
 "name": "The AI Interpretability Problem",
 "group": "Methods",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "Deep learning predicts biology opaquely - but how can the models' reasoning be interpreted so the biology trusts the predictions?",
 "background": "The interpretability problem - black-box bioinformatics AI (AlphaFold, Enformer, scVI) - is the trust gap: the predictions work but the reasoning is hidden; the attribution methods (saliency, attention) are approximate; and the scientific value needs the mechanism, not just the prediction. The field wants both accuracy and insight; the models give the first. The oracle speaks; its reasoning is sealed.",
 "why_it_matters": "Biology needs mechanisms, not just predictions. The sealed reasoning is the insight gap.",
 "sig_lens": "The Signature lens reads AI as the oracle: the protocol must demand the oracle show its work - attribution, counterfactuals, mechanism tests.",
 "sig_solution": LABEL + " Assumptions: (1) predictions accurate; reasoning hidden; (2) attribution approximate. Reasoning path: interpret rigorously - attribution validated on known biology, counterfactual testing, mechanism extraction. Proposed mechanism: an oracle protocol with validated attribution methods, counterfactual model probing, and mechanism-hypothesis generation. Confirm: the interpretations yield verified biology. Kill: the models stay inscrutable. Does NOT claim: the models interpreted - it demands the work shown.",
 "pointer": "The Signature system's proposed approach interprets bioinformatics AI with validated attribution; the companion Signature Edition record specifies the oracle protocol.",
 "key_points": [
  "Bioinformatics AI accurate but opaque.",
  "Attribution methods (saliency, attention) approximate.",
  "Biology needs mechanisms, not predictions.",
  "Interpretability is the trust gap.",
 ],
 "requirements": [
  "Validated attribution methods.",
  "Counterfactual model probing.",
  "Mechanism-hypothesis generation.",
 ],
 "citations": [
  "Ching T et al. (2018) Opportunities and obstacles for deep learning in biology and medicine. JR Soc Interface 15.",
 ],
 "demo": {"seed": 31, "length": 70},
},
# ----------------------------------------------------------------- rank 32
{
 "key": "bf-privacy",
 "name": "The Genomic Privacy Problem",
 "group": "Methods",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "Genomes identify people - but how can genomic data be shared for research while protecting privacy?",
 "background": "The privacy problem - genomic re-identification (Homer's attack, surname inference from Y-STRs) - ended open data sharing: the identifiability is inherent (the genome is the ultimate identifier); the protections (dbGaP controlled access, differential privacy, federated analysis, homomorphic encryption) each cost utility or practicality. The research needs sharing; the participants need privacy. The balance is technical and ethical - and unresolved.",
 "why_it_matters": "Genomic research needs data sharing; participants need privacy. The unresolved balance slows both.",
 "sig_lens": "The Signature lens reads genomic privacy as the sealed envelope: the protocol must let researchers read the letter (the science) without opening the envelope (the identity).",
 "sig_solution": LABEL + " Assumptions: (1) genomes inherently identifying; (2) protections cost utility. Reasoning path: share safely - federated analysis, differential privacy, and cryptographic methods with utility measured. Proposed mechanism: an envelope protocol with privacy-preserving analysis infrastructure, utility-privacy tradeoff quantification, and participant-centered governance. Confirm: the methods enable research with protection. Kill: the tradeoff proves unacceptable. Does NOT claim: the privacy solved - it seals the envelope.",
 "pointer": "The Signature system's proposed approach enables privacy-preserving genomic sharing; the companion Signature Edition record specifies the envelope protocol.",
 "key_points": [
  "Genomes are inherently identifying.",
  "Re-identification attacks ended open sharing.",
  "dbGaP, differential privacy, federated analysis each cost.",
  "Balance technical and ethical, unresolved.",
 ],
 "requirements": [
  "Privacy-preserving analysis infrastructure.",
  "Utility-privacy tradeoff quantification.",
  "Participant-centered data governance.",
 ],
 "citations": [
  "Homer N et al. (2008) Resolving individuals contributing trace amounts of DNA. PLoS Genetics 4.",
 ],
 "demo": {"seed": 32, "length": 80},
},
# ----------------------------------------------------------------- rank 33
{
 "key": "bf-reproducibility",
 "name": "The Reproducibility Problem",
 "group": "Methods",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "Bioinformatics analyses are hard to reproduce - but how can the field ensure results replicate when pipelines, data, and environments vary?",
 "background": "The reproducibility problem - the bioinformatics replication crisis - has known causes: unversioned tools, undocumented parameters, unavailable data, environment drift. The fixes (workflow managers: Nextflow/Snakemake; containers; FAIR data) are known but unevenly adopted. The published analysis that cannot be rerun is the field's credibility gap. The science that cannot be repeated is not yet science.",
 "why_it_matters": "Irreproducible analyses waste resources and mislead. The credibility gap is the field's foundation crack.",
 "sig_lens": "The Signature lens reads reproducibility as the repeat performance: the protocol must make every analysis re-runnable - by anyone, anywhere.",
 "sig_solution": LABEL + " Assumptions: (1) causes known: tools, parameters, data, environments; (2) fixes known, unevenly adopted. Reasoning path: require re-runnability - workflow-managed, containerized, FAIR analyses as the publication standard. Proposed mechanism: a performance protocol with reproducibility checklists for publication, containerized workflow requirements, and reproducibility auditing. Confirm: the audited analyses rerun. Kill: adoption stays uneven. Does NOT claim: the crisis solved - it makes the performance repeatable.",
 "pointer": "The Signature system's proposed approach makes bioinformatics analyses re-runnable by standard; the companion Signature Edition record specifies the performance protocol.",
 "key_points": [
  "Causes: unversioned tools, undocumented parameters, unavailable data.",
  "Fixes known: Nextflow/Snakemake, containers, FAIR.",
  "Adoption uneven across the field.",
  "Irreproducible analyses mislead.",
 ],
 "requirements": [
  "Publication reproducibility checklists.",
  "Containerized workflow requirements.",
  "Reproducibility auditing.",
 ],
 "citations": [
  "Sandve GK et al. (2013) Ten simple rules for reproducible computational research. PLoS Comp Bio 9.",
 ],
 "demo": {"seed": 33, "length": 90},
},
# ----------------------------------------------------------------- rank 34
{
 "key": "bf-unified",
 "name": "The Unified Bioinformatics Problem",
 "group": "Methods",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "Bioinformatics is fragmented into sequence, structure, systems, and AI silos - but can the computational biology be unified as one science?",
 "background": "The unified-bioinformatics problem - one framework from sequence to systems - is the field's synthesis: the silos (aligners, structurers, networkers, learners) each have methods and cultures; the integrations (AlphaFold's learned potentials, Enformer's sequence-to-function) hint at unification via learned models. The foundation models (scGPT, ESM) promise a unified representation. The fragmented tools are unifying - through learning, not through theory.",
 "why_it_matters": "The biology is one; the tools are many. The unification - via learning - is the field's convergence.",
 "sig_lens": "The Signature lens reads bioinformatics as the many instruments: the protocol must tune them to the same score - the unified representation - and keep each instrument's voice.",
 "sig_solution": LABEL + " Assumptions: (1) silos fragment; (2) foundation models hint unification via learning. Reasoning path: unify representationally - foundation models with task-specific heads, benchmarked across silos. Proposed mechanism: a score protocol with unified representation learning, cross-silo benchmarking, and silo-expertise preservation. Confirm: the unified models beat siloed ones. Kill: the silos resist unification. Does NOT claim: bioinformatics unified - it tunes the instruments.",
 "pointer": "The Signature system's proposed approach unifies bioinformatics via foundation representations; the companion Signature Edition record specifies the score protocol.",
 "key_points": [
  "Silos: sequence, structure, systems, AI.",
  "AlphaFold/Enformer hint learned unification.",
  "Foundation models (ESM, scGPT) promise unified representation.",
  "Unification via learning, not theory.",
 ],
 "requirements": [
  "Unified representation learning.",
  "Cross-silo benchmarking.",
  "Silo-expertise preservation.",
 ],
 "citations": [
  "Rives A et al. (2021) Biological structure and function emerge from scaling unsupervised learning (ESM). PNAS 118.",
 ],
 "demo": {"seed": 34, "length": 100},
},
]
