(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['genes','variants','pathways','inheritance','testing'];
var PREFIX='JAH-GEN-';
var CHROMS=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','X','Y','MT'];
var GENES=[['SIGA1','kinase signaling'],['SIGB2','transcription regulation'],['SIGC3','membrane transport'],['SIGD4','DNA repair'],['SIGE5','metabolic enzyme'],['SIGF6','cell adhesion'],['SIGG7','immune response'],['SIGH8','chromatin remodeling']];
var VARTYPES=[['missense','single amino acid substitution'],['nonsense','premature stop codon'],['frameshift','insertion or deletion shifting the reading frame'],['splice-site','disruption of exon-intron boundary'],['synonymous','no amino acid change'],['copy-number','deletion or duplication of a segment']];
var PATHS=[['Signature MAPK-like cascade','signal transduction'],['Signature p53-like checkpoint','cell cycle control'],['Signature Wnt-like patterning','developmental signaling'],['Signature insulin-like metabolic axis','metabolism'],['Signature apoptosis module','programmed cell death']];
var INHER=[['autosomal dominant','one altered copy is enough for the trait to appear'],['autosomal recessive','two altered copies are needed for the trait to appear'],['X-linked','the gene resides on the X chromosome'],['mitochondrial','transmitted through maternal cytoplasm'],['multifactorial','many genes plus environment contribute']];
var TESTS=[['karyotype','chromosome count and large rearrangements'],['FISH','targeted chromosomal regions'],['Sanger sequencing','single-gene variant confirmation'],['gene panel NGS','many genes at once'],['whole exome sequencing','protein-coding regions'],['microarray','copy-number variants']];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var id=PREFIX+String(seed).padStart(7,'0');
  var rec={id:id,category:cat,source:'signature',source_ref:'JAH Signature Generator',creation_mode:'SIGNATURE-GENERATED',_seed:seed,
    privacy_note:'Educational model only. Contains no real patient data.'};
  if(cat==='genes'){
    var g=pick(GENES,rnd),n=ri(rnd,1,99);
    rec.title='Signature gene model '+g[0]+'-'+n;
    rec.description='A Signature-generated gene study model named '+g[0]+'-'+n+' involved in '+g[1]+'. It is a teaching construct for practicing gene-record workflows, not a verified human gene.';
    rec.symbol=g[0]+'-'+n;rec.chromosome=pick(CHROMS,rnd);rec.location=rec.chromosome+'q'+ri(rnd,1,4)+'.'+ri(rnd,1,3);
    rec.gene_type='protein-coding (model)';rec.function_summary='Modeled role in '+g[1]+'.';
    rec.associated_conditions=['none - teaching model'];
  }else if(cat==='variants'){
    var v=pick(VARTYPES,rnd),g2=pick(GENES,rnd);
    rec.title='Signature variant model: '+v[0]+' in '+g2[0];
    rec.description='A teaching example of a '+v[0]+' variant ('+v[1]+') in the model gene '+g2[0]+'. Illustrative nomenclature practice only; not a real clinical variant.';
    rec.symbol=g2[0];rec.chromosome=pick(CHROMS,rnd);rec.location='model locus';
    rec.variant_type=v[0];rec.clinical_significance='illustrative only - not a real finding';
    rec.associated_conditions=['none - teaching model'];
  }else if(cat==='pathways'){
    var p=pick(PATHS,rnd);
    rec.title='Signature pathway model: '+p[0];
    rec.description='A teaching model of a '+p[1]+' pathway ('+p[0]+'). Members and interactions are illustrative constructs for practicing pathway-record workflows.';
    rec.pathway_class=p[1];rec.member_genes=[pick(GENES,rnd)[0],pick(GENES,rnd)[0],pick(GENES,rnd)[0]];
    rec.summary='Illustrative '+p[1]+' cascade with modeled members.';
  }else if(cat==='inheritance'){
    var ih=pick(INHER,rnd);
    rec.title='Inheritance pattern study: '+ih[0];
    rec.description='An educational record describing '+ih[0]+' inheritance: '+ih[1]+'. Includes a practice pedigree sketch and recurrence-risk arithmetic for teaching.';
    rec.pattern=ih[0];rec.recurrence_note=ih[1]+'.';
    rec.example_genes=['teaching example only'];
  }else{
    var t=pick(TESTS,rnd);
    rec.title='Genetic testing method: '+t[0];
    rec.description='An educational record for the '+t[0]+' method, used to detect '+t[1]+'. Covers indications, sample type, and limitations in general teaching terms.';
    rec.method=t[0];rec.detects=t[1];rec.sample_types=['blood','saliva'];
  }
  return rec;
}
function validChrom(c){return CHROMS.indexOf(String(c))>=0;}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-GEN-\d{7}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(r.category==='genes'){
    if(!/^[A-Z0-9-]+$/.test(r.symbol||''))e.push('symbol');
    if(!validChrom(r.chromosome))e.push('chromosome');
    if(typeof r.location!=='string'||!r.location.length)e.push('location');
  }
  if(r.category==='variants'){
    if(typeof r.variant_type!=='string'||!r.variant_type.length)e.push('variant_type');
    if(typeof r.clinical_significance!=='string'||!/illustrative|teaching|educational/i.test(r.clinical_significance))e.push('clinical_significance');
  }
  if(r.category==='pathways'){
    if(!Array.isArray(r.member_genes)||!r.member_genes.length)e.push('member_genes');
  }
  if(r.category==='inheritance'){
    if(typeof r.pattern!=='string'||!r.pattern.length)e.push('pattern');
  }
  if(r.category==='testing'){
    if(typeof r.method!=='string'||!r.method.length)e.push('method');
  }
  if(typeof r.privacy_note!=='string'||!/no real patient data/i.test(r.privacy_note))e.push('privacy_note');
  if(r.source!=='signature'&&r.source!=='online')e.push('source');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-genetics-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('genetics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
