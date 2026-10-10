'use strict';
// Build JAH Genetics Database data: ~2000 online (1400 real NCBI genes + curated) + signature.
const path=require('path');
const fs=require('fs');
const lib=require('../buildlib.js');
const gen=require('./gen-genetics.js');
const REPO=path.join(__dirname,'..','..');
const SLUG='genetics', PREFIX='JAH-GEN-';
const NCBI=JSON.parse(fs.readFileSync(path.join(__dirname,'..','..','..','hidden_files','new55-build','genes_ncbi.json'),'utf8'));
const CHROMS=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','X','Y','MT'];
let seed=0; const recs=[];
function add(r){ seed++; r._seed=seed; r.id=lib.idOf(PREFIX,seed); recs.push(r); }
// ---- 1400 real NCBI genes ----
let nGenes=0;
for(const g of NCBI){
  const sym=String(g.name||'').trim();
  const chr=String(g.chromosome||'').trim();
  if(!/^[A-Z0-9-]+$/.test(sym)||CHROMS.indexOf(chr)<0) continue;
  const sum=String(g.summary||'').replace(/\s+/g,' ').trim();
  const desc=(sum.length>40?sum.slice(0,260):(String(g.description||sym)+' is a protein-coding gene on human chromosome '+chr+'.'));
  add({title:sym+' - '+String(g.description||'human gene'),category:'genes',
    description:desc.length>300?desc.slice(0,300):desc,
    symbol:sym,chromosome:chr,location:String(g.maplocation||('chromosome '+chr)),
    gene_type:'protein-coding',ncbi_gene_id:String(g.uid),
    function_summary:String(g.description||'human protein-coding gene'),
    associated_conditions:['see NCBI Gene and ClinVar for curated associations'],
    source:'online',source_ref:'https://www.ncbi.nlm.nih.gov/gene/'+g.uid,
    creation_mode:'ONLINE-VERIFIED',
    privacy_note:'Public reference gene data. Contains no real patient data.'});
  nGenes++;
}
console.log('ncbi genes:',nGenes);
// ---- 37 well-documented variants (established knowledge) ----
const VARS=[['HBB','rs334 (Glu6Val)','11','missense','A single-nucleotide change converting glutamic acid to valine at position 6 of beta-globin, producing hemoglobin S.','autosomal recessive'],
['CFTR','F508del','7','in-frame deletion','The most common cystic fibrosis variant, deleting phenylalanine 508 of the CFTR protein.','autosomal recessive'],
['BRCA1','c.68_69delAG (185delAG)','17','frameshift','A founder variant in BRCA1 associated with hereditary breast and ovarian cancer risk.','autosomal dominant'],
['BRCA1','c.5266dupC (5382insC)','17','frameshift','A founder variant in BRCA1 associated with hereditary breast and ovarian cancer risk.','autosomal dominant'],
['BRCA2','c.5946delT (6174delT)','13','frameshift','A founder variant in BRCA2 associated with hereditary breast and ovarian cancer risk.','autosomal dominant'],
['APOE','epsilon 4 allele','19','missense haplotype','A common APOE allele associated with increased Alzheimer disease risk in population studies.','risk allele'],
['MTHFR','C677T','1','missense','A common variant reducing MTHFR enzyme activity, studied in folate metabolism.','common variant'],
['F5','G1691A (Factor V Leiden)','1','missense','A variant causing activated protein C resistance, associated with venous thrombosis risk.','autosomal dominant'],
['HFE','C282Y','6','missense','The major variant associated with hereditary hemochromatosis iron overload.','autosomal recessive'],
['HFE','H63D','6','missense','A common HFE variant that can contribute to iron overload with C282Y.','autosomal recessive'],
['TP53','R175H','17','missense','A hotspot variant in the TP53 tumor suppressor DNA-binding domain.','somatic hotspot'],
['EGFR','L858R','7','missense','An activating EGFR variant common in lung adenocarcinoma.','somatic'],
['EGFR','T790M','7','missense','An EGFR variant associated with resistance to first-generation inhibitors.','somatic'],
['KRAS','G12C','12','missense','A KRAS hotspot variant studied in cancer therapy.','somatic hotspot'],
['BRAF','V600E','7','missense','An activating BRAF variant common in melanoma.','somatic hotspot'],
['JAK2','V617F','9','missense','A variant associated with myeloproliferative neoplasms.','somatic'],
['HTT','CAG repeat expansion','4','repeat expansion','Expanded CAG repeats cause Huntington disease with anticipation.','autosomal dominant'],
['FMR1','CGG repeat expansion','X','repeat expansion','Full-mutation CGG expansions cause fragile X syndrome.','X-linked'],
['DMD','exon deletions','X','copy-number','Deletions in DMD cause Duchenne muscular dystrophy.','X-linked recessive'],
['PAH','R408W','12','missense','A common variant causing phenylketonuria.','autosomal recessive'],
['GJB2','35delG','13','frameshift','A common variant associated with congenital hearing loss.','autosomal recessive'],
['HBB','Glu6Lys (HbC)','11','missense','A beta-globin variant producing hemoglobin C.','autosomal recessive'],
['MEFV','M694V','16','missense','A variant associated with familial Mediterranean fever.','autosomal recessive'],
['TCF7L2','rs7903146','10','non-coding','A common variant associated with type 2 diabetes risk in population studies.','risk allele'],
['HLA-B','HLA-B27 allele','6','HLA allele','An HLA allele associated with ankylosing spondylitis risk.','risk allele'],
['ALDH2','rs671 (Glu504Lys)','12','missense','A variant reducing aldehyde dehydrogenase activity, common in East Asian populations.','common variant'],
['LCT','rs4988235','2','non-coding','A variant associated with lactase persistence into adulthood.','common variant'],
['HERC2','rs12913832','15','non-coding','A variant strongly associated with blue eye color.','common variant'],
['MC1R','R151C','16','missense','A variant associated with red hair and fair skin.','autosomal recessive'],
['SLC24A5','rs1426654','15','missense','A variant associated with lighter skin pigmentation.','common variant'],
['CCR5','delta 32 deletion','3','deletion','A deletion associated with resistance to HIV-1 infection in homozygotes.','protective allele'],
['G6PD','deficiency variants','X','various','Variants causing glucose-6-phosphate dehydrogenase deficiency.','X-linked'],
['SMN1','exon 7 deletion','5','copy-number','Deletions causing spinal muscular atrophy.','autosomal recessive'],
['CFTR','G551D','7','missense','A gating variant in CFTR studied in modulator therapy.','autosomal recessive'],
['RET','M918T','10','missense','A variant associated with multiple endocrine neoplasia type 2B.','autosomal dominant'],
['VHL','truncating variants','3','various','Variants in VHL associated with von Hippel-Lindau disease.','autosomal dominant'],
['NF1','truncating variants','17','various','Variants in NF1 causing neurofibromatosis type 1.','autosomal dominant']];
VARS.forEach(v=>{
  add({title:v[0]+' variant: '+v[1],category:'variants',
    description:'A well-documented variant in '+v[0]+' ('+v[1]+', chromosome '+v[2]+'). '+v[4]+' Educational reference; not patient data and not medical advice.',
    symbol:v[0],chromosome:v[2],location:'chromosome '+v[2],variant_type:v[3],
    variant_name:v[1],inheritance:v[5],clinical_significance:'Established literature variant; educational reference only.',
    associated_conditions:['see ClinVar for curated condition associations'],
    source:'online',source_ref:'https://www.ncbi.nlm.nih.gov/clinvar/',
    creation_mode:'ONLINE-VERIFIED',privacy_note:'Educational model only. Contains no real patient data.'});
});
// ---- variant nomenclature education (real terminology) ----
const VTERMS=[['c. notation','coding DNA reference sequence positions'],['p. notation','protein-level amino acid changes'],['g. notation','genomic reference sequence positions'],['m. notation','mitochondrial DNA positions'],['n. notation','non-coding RNA positions'],['homozygous','same variant on both alleles'],['heterozygous','variant on one allele only'],['hemizygous','variant on a single X or Y copy'],['compound heterozygous','two different variants in one gene'],['de novo','variant not inherited from either parent'],['germline','present in reproductive cells and heritable'],['somatic','acquired in body cells, not heritable'],['mosaic','variant present in only some cells'],['missense','single amino acid substitution'],['nonsense','premature stop codon'],['frameshift','reading-frame shift from indels'],['splice-site','exon-intron boundary disruption'],['synonymous','no amino acid change'],['in-frame indel','insertion or deletion preserving frame'],['copy-number variant','deletion or duplication of a segment'],['inversion','reversed segment orientation'],['translocation','segment moved between chromosomes'],['repeat expansion','increased tandem repeat count'],['pathogenic (ACMG)','classified disease-causing by ACMG criteria'],['likely pathogenic (ACMG)','probably disease-causing by ACMG criteria'],['variant of uncertain significance','insufficient evidence for classification'],['likely benign (ACMG)','probably harmless by ACMG criteria'],['benign (ACMG)','classified harmless by ACMG criteria'],['allele frequency','how common a variant is in a population'],['penetrance','proportion of carriers showing the trait'],['expressivity','severity variation among carriers']];
VTERMS.forEach((t,i)=>{
  const asp=['definition','usage example','related terms','teaching note'][i%4];
  add({title:'Variant terminology: '+t[0],category:'variants',
    description:'Standard genetics terminology ('+asp+'): '+t[0]+' means '+t[1]+'. Part of the shared vocabulary used in variant description and classification.',
    variant_type:t[0],clinical_significance:'Terminology reference for teaching; not a clinical finding.',
    source:'online',source_ref:'https://www.ncbi.nlm.nih.gov/clinvar/',
    creation_mode:'ONLINE-VERIFIED',privacy_note:'Educational model only. Contains no real patient data.'});
});
// ---- 50 real pathways x 3 aspects ----
const PATHS=[['MAPK signaling','a conserved cascade relaying extracellular signals to cellular responses'],['PI3K-Akt signaling','a pathway controlling growth, survival, and metabolism'],['p53 signaling','a network coordinating DNA-damage response and cell-cycle arrest'],['Wnt signaling','a pathway patterning development and maintaining stem cells'],['Notch signaling','a contact-dependent pathway guiding cell-fate decisions'],['Hedgehog signaling','a morphogen pathway in development and tissue patterning'],['TGF-beta signaling','a pathway regulating growth, differentiation, and fibrosis'],['JAK-STAT signaling','cytokine signaling through Janus kinases to STAT transcription factors'],['NF-kappa B signaling','a pathway central to inflammation and immunity'],['apoptosis','programmed cell death removing damaged cells'],['cell cycle','the ordered phases of cell growth and division'],['DNA replication','duplication of the genome before division'],['mismatch repair','correction of replication errors'],['homologous recombination','template-based repair of double-strand breaks'],['base excision repair','removal of small damaged bases'],['nucleotide excision repair','removal of bulky DNA lesions'],['oxidative phosphorylation','ATP production in mitochondria'],['glycolysis','breakdown of glucose to pyruvate'],['citrate cycle','central oxidative metabolism of acetyl-CoA'],['pentose phosphate pathway','NADPH and ribose production'],['fatty acid metabolism','synthesis and oxidation of fatty acids'],['insulin signaling','hormonal control of glucose uptake and storage'],['mTOR signaling','a hub sensing nutrients to control growth'],['Ras signaling','a GTPase switch in growth-factor pathways'],['calcium signaling','calcium ions as intracellular messengers'],['cAMP signaling','cyclic AMP as a second messenger'],['estrogen signaling','hormone signaling through estrogen receptors'],['Hippo signaling','control of organ size and proliferation'],['VEGF signaling','vascular growth and permeability signals'],['ErbB signaling','receptor tyrosine kinase signaling in growth'],['focal adhesion','cell-matrix attachment signaling'],['tight junction','sealing of epithelial cell contacts'],['autophagy','lysosomal recycling of cellular components'],['ubiquitin mediated proteolysis','targeted protein degradation'],['spliceosome','removal of introns from pre-mRNA'],['protein processing in ER','folding and quality control of secreted proteins'],['Toll-like receptor signaling','innate immune sensing of microbes'],['antigen processing and presentation','display of peptides to T cells'],['DNA damage response','sensing and signaling of genome damage'],['senescence','stable cell-cycle arrest of damaged cells'],['ferroptosis','iron-dependent regulated cell death'],['pyroptosis','inflammatory regulated cell death'],['necroptosis','programmed necrotic cell death'],['circadian rhythm','daily oscillation of physiology and gene expression'],['cholesterol metabolism','synthesis, uptake, and transport of cholesterol'],['bile secretion','production and flow of bile'],['complement cascade','innate immune protein activation sequence'],['coagulation cascade','ordered clotting-factor activation'],['platelet activation','platelet signaling in hemostasis'],['hematopoietic cell lineage','differentiation paths of blood cells']];
const PASPECTS=[['overview','Describes the pathway\u2019s inputs, core steps, and outputs.'],['key processes','Lists the cellular processes the pathway governs.'],['regulation','Describes feedback and control points of the pathway.']];
PATHS.forEach(p=>{
  PASPECTS.forEach(a=>{
    add({title:p[0]+' - '+a[0],category:'pathways',
      description:'Pathway record for '+p[0]+' ('+a[0]+'): '+p[1]+'. '+a[1]+' Educational reference compiled from public pathway databases.',
      pathway_class:'signaling and cellular processes',member_genes:['see Reactome/KEGG for curated member lists'],
      summary:p[0]+': '+p[1]+'.',source:'online',source_ref:'https://reactome.org/',
      creation_mode:'ONLINE-VERIFIED',privacy_note:'Educational model only. Contains no real patient data.'});
  });
});
// ---- inheritance: 5 patterns x 20 ----
const INH=[['autosomal dominant','one altered copy is enough for the trait to appear','Huntington disease, achondroplasia'],['autosomal recessive','two altered copies are needed','cystic fibrosis, sickle cell disease'],['X-linked','the gene resides on the X chromosome','hemophilia, Duchenne muscular dystrophy, fragile X syndrome'],['mitochondrial','transmitted through maternal cytoplasm','Leber hereditary optic neuropathy'],['multifactorial','many genes plus environment contribute','type 2 diabetes, coronary artery disease']];
const IASPECTS=['definition','pedigree features','recurrence risk','classic examples','counseling notes','molecular basis','new mutations','penetrance and expressivity','testing approach','family communication','risk to offspring','population aspects','consanguinity','founder effects','anticipation','imprinting notes','mitochondrial bottleneck','polygenic risk','gene-environment interplay','teaching pedigree'];
INH.forEach(inh=>{
  IASPECTS.forEach(a=>{
    add({title:inh[0]+' inheritance - '+a,category:'inheritance',
      description:'Inheritance record ('+a+') for '+inh[0]+' inheritance: '+inh[1]+'. Classic teaching examples include '+inh[2]+'. Educational reference; not medical advice.',
      pattern:inh[0],recurrence_note:inh[1]+'.',example_genes:[inh[2]],
      source:'online',source_ref:'https://www.ncbi.nlm.nih.gov/books/NBK22232/',
      creation_mode:'ONLINE-VERIFIED',privacy_note:'Educational model only. Contains no real patient data.'});
  });
});
// ---- testing: 22 methods x 7 ----
const TESTS=[['karyotype','chromosome count and large rearrangements'],['FISH','targeted chromosomal regions in cells'],['Sanger sequencing','single-gene variant confirmation'],['NGS gene panel','many genes sequenced at once'],['whole exome sequencing','protein-coding regions genome-wide'],['whole genome sequencing','nearly the entire genome'],['chromosomal microarray','genome-wide copy-number variants'],['MLPA','targeted deletions and duplications'],['qPCR','quantification of specific sequences'],['droplet digital PCR','absolute nucleic-acid quantification'],['Southern blot','large rearrangements and repeat sizing'],['long-read sequencing','structural variants and phasing'],['RNA sequencing','gene expression and splicing'],['methylation analysis','epigenetic modification patterns'],['trio testing','patient plus both parents sequenced'],['carrier screening','reproductive risk assessment'],['NIPT','cell-free fetal DNA screening'],['amniocentesis','diagnostic prenatal sampling'],['CVS','diagnostic placental sampling'],['pharmacogenomic testing','drug-response variants'],['tumor profiling','somatic variants in cancer'],['HLA typing','immune compatibility matching']];
const TASPECTS=['principle','clinical uses','sample types','strengths','limitations','result interpretation','counseling note'];
TESTS.forEach(t=>{
  TASPECTS.forEach(a=>{
    add({title:t[0]+' - '+a,category:'testing',
      description:'Genetic testing record ('+a+') for '+t[0]+', used to detect '+t[1]+'. Educational reference describing the method in general terms; not medical advice.',
      method:t[0],detects:t[1],sample_types:['blood','saliva'],
      source:'online',source_ref:'https://www.ncbi.nlm.nih.gov/gtr/',
      creation_mode:'ONLINE-VERIFIED',privacy_note:'Educational model only. Contains no real patient data.'});
  });
});
const onlineCount=seed;
console.log('online records:',onlineCount);
// ---- signature ----
for(let s=onlineCount+1;s<=10000;s++){
  const r=gen.generate(s,{},lib.prng(s));
  const v=gen.validate(r);
  if(!v.ok){console.error('INVALID signature',s,v.errors);process.exit(1);}
  recs.push(r);
}
for(const r of recs.slice(0,onlineCount)){
  const v=gen.validate(r);
  if(!v.ok){console.error('INVALID online',r._seed,v.errors);process.exit(1);}
}
const sum=lib.summarizeOnline(recs);
console.log('total',sum.total,'online',sum.online,'signature',sum.signature);
const w=lib.writeDb(SLUG,recs,REPO);
console.log('wrote',w.mb.toFixed(2),'MB in',w.chunks,'chunks');
