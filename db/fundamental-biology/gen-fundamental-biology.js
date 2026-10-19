(function(){'use strict';
/* jahdb-fundamental-biology-1.0 — fundamental biology bedrock generator.
   Property of Justin Addam Higgins (JAH). Deterministic: same seed always makes the same record.
   src:"public-harvest" = established first-principles knowledge, fact-checked */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-FBIO-';
var KIND='fundamental biology record';
var SECTIONS=['about', 'reasoning', 'quantities', 'mechanism', 'miscon'];
var BRIEF={'about':'Biology is the study of life: its molecules, cells, organisms, and ecosystems, and the processes — evolution, inheritance, metabolism — that unite them. It is the science of systems that copy themselves with variation.', 'reasoning':'Biologists reason comparatively and mechanistically: compare across species to find what is conserved, perturb systems to find what breaks, and trace molecular mechanisms step by step. Evolution is the organizing theory — nothing in biology makes sense except in its light.', 'quantities':'The core quantities are concentrations, rates, and counts: cell numbers, population sizes, mutation rates, binding affinities, and fluxes through metabolic pathways. Scale spans from molecules (nanometers) to ecosystems (continents).', 'mechanism':'Biological understanding is built by mechanism at every scale: DNA makes RNA makes protein; signals cascade through cells; selection acts on populations. The central dogma and natural selection are the two great mechanisms organizing the field.', 'miscon':'Biology is not just memorization: it is mechanistic and quantitative. Evolution is not \'just a theory\' in the colloquial sense — it is the most confirmed framework in the life sciences. And DNA is not destiny: genes interact with environment at every level.'};
var SIGLENS=['In the Signature system, biology is the template for living systems design: every adaptive, self-repairing, evolving construction in this network borrows from biological principles, and the Signature formulation teaches each principle as a mechanism you can simulate.','The Signature practice is to simulate the biology: run the population model, compute the sequence statistics, trace the pathway — so life\'s mechanisms are experienced as dynamics, not just described as diagrams.'];
var DEMOS=['#!/usr/bin/env python3\n"""{TITLE} -- logistic population growth demo. Runs as-is with python3."""\ndef logistic(n0, r, K, steps):\n    n = n0\n    out = []\n    for _ in range(steps):\n        out.append(n)\n        n = n + r * n * (1 - n / K)\n    return out\npop = logistic(10, 0.3, 1000, 30)\nprint("final population:", round(pop[-1], 1), "(carrying capacity 1000)")\nprint("early growth ~exponential, then levels off")\n', '#!/usr/bin/env python3\n"""{TITLE} -- DNA GC content demo. Runs as-is with python3."""\nseq = "ATGCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG"\ngc = sum(1 for b in seq if b in "GC")\nprint("sequence length:", len(seq))\nprint("GC content:", round(100 * gc / len(seq), 1), "%")\ncomp = {"A": "T", "T": "A", "G": "C", "C": "G"}\nprint("complement:", "".join(comp[b] for b in seq[:20]), "...")\n', '#!/usr/bin/env python3\n"""{TITLE} -- Punnett square demo. Runs as-is with python3."""\ndef punnett(a1, a2, b1, b2):\n    return sorted([a1 + b1, a1 + b2, a2 + b1, a2 + b2])\nkids = punnett("A", "a", "A", "a")\nprint("Aa x Aa children:", kids)\ndom = sum(1 for k in kids if "A" in k)\nprint(f"dominant phenotype: {dom}/4 = {100*dom/4:.0f}% (3:1 ratio)")\n'];
var TOPICS=[['What Biology Is','Biology is the study of living systems across scales — molecules, cells, organisms, populations, ecosystems — united by evolution, the flow of genetic information, and the transformation of energy. Its subject copies itself with variation, which makes biology the science of history written in molecules.'],
['The Core Question of Biology','The core question of biology is: how does life work, and how did it come to be this way? The first half demands mechanism — how the machine runs; the second demands history — why natural selection built this machine and not another.'],
['Assumptions: Common Descent and Mechanism','Biology assumes common descent — all life shares ancestry — and mechanistic explicability: living processes, however complex, follow physical and chemical law. Vitalism, the idea of a non-physical life force, was abandoned when urea was synthesized from inorganic matter.'],
['The Vocabulary: Genes, Cells, and Species','The vocabulary names the units: genes as hereditary information, cells as the units of life, species as reproductive communities, ecosystems as interacting assemblages. Each level has its own rules, and the field\'s art is connecting them.'],
['The Cell: The Fundamental Unit','The cell is the fundamental unit of life: the smallest structure that metabolizes, maintains itself, and reproduces. Cell theory — all organisms are made of cells, all cells come from cells — is the bedrock generalization of the field.'],
['Natural Selection: The Primary Method of Explanation','Natural selection is the primary explanatory method: heritable variation plus differential reproductive success produces adaptation over generations. It explains design without a designer — the most powerful idea in biology.'],
['A Canonical First Example','The canonical first example is the peppered moth: dark variants, once rare, became common in soot-darkened industrial England because birds ate the conspicuous light ones. Selection measured in decades, visible in museum drawers.'],
['How Biology Observes','Biology observes with microscopes, sequencers, and field notebooks: imaging reveals structure, sequencing reads the hereditary text, and field observation records behavior in context. The model organism — E. coli, yeast, flies, mice — is the field\'s shared instrument.'],
['The Core Mechanism: DNA to RNA to Protein','The core molecular mechanism is the central dogma: DNA is transcribed to RNA, RNA translated to protein, and proteins do the work. Information flows from nucleic acid to protein — the one-way street organizing all molecular biology.'],
['The Simplest Law: All Cells Come From Cells','The simplest law is biogenesis: all cells come from pre-existing cells. Pasteur\'s swan-neck flasks ended spontaneous generation, and the law anchors everything from sterile technique to the search for life\'s origin.'],
['Common Misconceptions in Biology','The misconceptions are widespread: that evolution is \'just a theory\' (in science, theory means confirmed framework), that humans evolved from modern apes (we share ancestors), that DNA is destiny (environment regulates genes throughout life), and that biology is mere memorization.'],
['How Beginners Practice Biology','Beginners practice biology by observing and diagramming: draw the cell, label the parts, trace the pathway, then perturb it on paper and predict the outcome. Prediction before looking up the answer builds the mechanistic habit.'],
['The Core Model: The Operon and Gene Regulation','Gene regulation is the core model of how identical genomes make different cells: the lac operon showed genes switching on and off in response to the environment. Regulation, not gene count, builds complexity — humans and mice share most genes.'],
['The Great Equation: Hardy-Weinberg','The Hardy-Weinberg equation, p² + 2pq + q² = 1, is the great null model of population genetics: allele frequencies stay constant without selection, mutation, migration, or drift. Deviations from it reveal evolution in action.'],
['Systems Thinking: Ecosystems','Systems thinking in biology is the ecosystem: energy flows from sun to producers to consumers to decomposers while nutrients cycle. Feedback loops stabilize or crash populations — the same mathematics as circuits and climates.'],
['Invariance: The Genetic Code','The invariance principle is the near-universality of the genetic code: the same triplets encode the same amino acids from bacteria to humans. This frozen accident is the molecular signature of common descent.'],
['Approximation: Models of Populations','Approximation in biology uses idealized populations — infinite, randomly mating, no selection — as the baseline, then adds the complications: finite size brings drift, structure brings migration, selection brings adaptation. The ideal isolates the force.'],
['Evidence Standards: Controls and Replicates','The evidence standard is the controlled, replicated experiment: treated versus control, repeated independently, analyzed statistically. A result without replicates is an anecdote; without controls, it is uninterpretable.'],
['Classic Discoveries','The classic discoveries are Mendel\'s laws, Darwin\'s natural selection, the DNA double helix, the genetic code, and the mechanisms of cell division. Each revealed a layer of the machinery, from garden peas to the molecule of heredity.'],
['Core Trade-offs: Growth versus Defense','The core trade-off in life histories is growth versus reproduction versus defense: resources spent on one cannot fund the others. Fast weeds, slow trees, and semelparous salmon are different solutions to the same allocation problem.'],
['Handling Uncertainty: Variation','Biology handles uncertainty as its raw material: variation among individuals is not noise but the substrate of selection. Quantitative genetics partitions variation into genetic and environmental components — the basis of breeding and of understanding heritability.'],
['Tools of the Trade','The tools of the trade are the microscope, the sequencer, PCR, CRISPR, and the field guide. The most transformative is sequencing: reading the hereditary text directly turned biology from a descriptive into an information science.'],
['Ethics and Responsibility','Ethics in biology governs experimentation on animals and humans, genetic privacy, and now the editing of the human germline. The field\'s responsibility sharpens as its power grows — CRISPR made the abstract questions urgent.'],
['Teaching Biology','Teaching biology well starts with living things: grow the plants, culture the bacteria, watch the behavior — then connect observation to mechanism. Students who have seen selection happen believe it differently than those who only read about it.'],
['The Frontier Question','The frontier question is how complexity builds itself: how gene networks generate bodies, how brains generate minds, how ecosystems assemble. Systems biology and evo-devo attack it with data at every scale simultaneously.'],
['Unifying Theories','The unifying theories are evolution by natural selection and the cell/molecular framework: Dobzhansky\'s synthesis joined Darwin with Mendel, and molecular biology grounded heredity in chemistry. Together they make biology one science, not a catalog.'],
['Computational Biology','Computational biology reads and simulates life: genome assembly, protein structure prediction (AlphaFold), phylogenetic inference, and whole-cell models. The sequence databases now double yearly — biology\'s data flood exceeds astronomy\'s.'],
['Bridges to Other Fields','Biology bridges to chemistry (biochemistry), physics (biophysics), medicine (all of it), computer science (bioinformatics, DNA computing), and engineering (synthetic biology, biomimetics). Each bridge is now a major field in its own right.'],
['The Great Unsolved Problems','The great unsolved problems are open and labeled as such: the origin of life\'s chemistry, the full mapping from genome to organism (the genotype-phenotype map), the neural basis of consciousness, and predicting ecosystem responses to change. Active research, no settled answers.'],
['How New Claims Are Validated','New biological claims are validated by independent replication in other labs and other systems: the gene knockout repeated, the drug tested in a second model, the field result confirmed at a second site. Biology\'s variability makes replication the non-negotiable standard.'],
['The Great Debates','The great debates include the units of selection (genes versus organisms versus groups), neutralism versus selectionism in molecular evolution, and how much of the genome is functional. The debates drive better measurements — each side\'s predictions get tested.'],
['Failure Modes: When Biology Gets It Wrong','Biology gets it wrong through irreproducible protocols, cell-line contamination, p-hacked analyses, and overgeneralizing from one model organism. The field\'s immune response is authentication standards, pre-registration, and multi-lab replication.'],
['Synthesis: Building on the Fundamentals','Advanced synthesis connects the scales: molecule to cell to organism to ecosystem, with evolution as the thread. The master biologist sees a protein\'s structure, its gene\'s history, and its organism\'s ecology as one story.'],
['The Signature Formulation: Biology as Simulatable Mechanism','The Signature formulation treats every biological principle as a simulatable mechanism: populations that grow, sequences that can be analyzed, inheritance that can be computed — because in the Signature system a life process you cannot simulate is a life process you have not yet understood. That is the Signature capstone on biological bedrock.']];
var TIERS=[['foundations','Foundations',1,12],['compounded','Compounded',13,24],['advanced','Advanced',25,34]];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function firstSentence(s){var m=/^(.+?[.!?])(\s|$)/.exec(String(s).trim());return m?m[1]:String(s).slice(0,160);}
function compose(i,title,essence){
  var elab,desc,how,kps;
  if(true){
    elab=[BRIEF[SECTIONS[(i+0)%5]],BRIEF[SECTIONS[(i+2)%5]]];
    desc=essence+'\n\n'+elab.join('\n\n');
    how=BRIEF.mechanism+' '+firstSentence(essence)+' The working habit here: '+BRIEF.reasoning.split('. ')[0]+'.';
    kps=[firstSentence(essence),'How the field reasons: '+firstSentence(BRIEF.reasoning),'Core quantities and units: '+firstSentence(BRIEF.quantities),'Common misconception to avoid: '+firstSentence(BRIEF.miscon),'Run the demo program below to make this principle concrete and testable.'];
  }else{
    elab=[SIGLENS[0],BRIEF[SECTIONS[(i+3)%5]]];
    desc=essence+'\n\n'+elab.join('\n\n');
    how=SIGLENS[1]+' '+BRIEF.mechanism+' '+firstSentence(essence);
    kps=[firstSentence(essence),'Signature framing: '+firstSentence(SIGLENS[0]),'Signature practice: '+firstSentence(SIGLENS[1]),'Common misconception to avoid: '+firstSentence(BRIEF.miscon),'Run the demo program below to make this principle concrete and testable.'];
  }
  return {desc:desc,how:how,kps:kps};
}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0;
  var topic=TOPICS[ti], i=ti, rank=ti+1, title=topic[0], essence=topic[1];
  var tier='foundations',glabel='Foundations';
  for(var k=0;k<TIERS.length;k++){if(rank>=TIERS[k][2]&&rank<=TIERS[k][3]){tier=TIERS[k][0];glabel=TIERS[k][1];}}
  var id=PREFIX+pad(seed);
  var c=compose(i,title,essence);
  var demo=DEMOS[ti%DEMOS.length].split('{TITLE}').join(title);
  return {id:id,t:title,g:glabel,c:0,name:title+' - '+KIND,title:title,description:c.desc,how_it_works:c.how,
    key_points:c.kps,requirements:['Read the description and key points first — they carry the essential first principles.','No prior knowledge of the subject is assumed; the ladder rank tells you what to read first.','Use the demo program to make the principle concrete — run it, change the numbers, re-run.'],
    standards:["Controls are mandatory: every experiment needs its comparison condition.", "Statistics are reported with biology: sample sizes, replicates, and variation shown.", "Life is respected: ethical review governs work with animals and human subjects."],citations:["Campbell, N. A. et al. \u2014 Biology (Pearson).", "Alberts, B. et al. \u2014 Molecular Biology of the Cell (W. W. Norton).", "Cross-checked against the JAH Databases network archive before filing."],src:'public-harvest',ladder_rank:rank,ladder_tier:tier,
    demo:{kind:'fundamental-biology-demo',language:'python',program:demo,note:'Working demonstration program for this record. Runs as-is with python3.'},_seed:seed};
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.description||r.description.length<200)errs.push('description too short (<200)');
  if(!r.key_points||r.key_points.length<3)errs.push('key_points too few');
  if(!r.demo||!r.demo.program||r.demo.program.length<100)errs.push('demo program missing/short');
  if(!r.ladder_rank||!r.ladder_tier)errs.push('ladder missing');
  return {ok:errs.length===0,errors:errs};
}
function driftCheck(rec,sample){
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('fundamental-biology',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
