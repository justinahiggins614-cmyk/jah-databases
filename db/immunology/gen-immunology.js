/* ✳ SIGNATURE — JAH Immunology Database generator. Property of Justin Addam Higgins (JAH).
   Deterministic client-side generator: same seed + same version => same record.
   Anchor facts verified from published immunology sources; application studies
   are Signature-generated and labeled as such. Educational content only. */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['immune-cells','antibodies','vaccines','innate-immunity','adaptive-immunity','complement-system','cytokines','autoimmunity','allergies','transplantation'];
var PREFIX='JAH-IMM-';
/* [subject, category, type, role/function, key fact, [associated x3], year (0 = none)] */
var ANCH=[
['Helper T cells','immune-cells','cell','CD4 T cells coordinate the immune response by activating B cells, killer T cells, and macrophages','the cells targeted and depleted by HIV',['B cell activation','cytokines','HIV'],0],
['Cytotoxic T cells','immune-cells','cell','CD8 killer T cells destroy virus-infected and cancerous cells directly','recognize antigens presented on MHC class I molecules',['cell killing','viruses','cancer surveillance'],0],
['B cells','immune-cells','cell','produce antibodies; activated B cells differentiate into plasma cells that secrete them','antibodies are Y-shaped H2L2 proteins',['antibodies','plasma cells','memory B cells'],0],
['Natural killer cells','immune-cells','cell','innate lymphocytes that kill stressed or infected cells without prior sensitization','a first line against tumors and viruses',['innate immunity','tumor surveillance','viruses'],0],
['Macrophages','immune-cells','cell','large phagocytes that engulf pathogens and present antigens to T cells','tissue-resident sentinels of the immune system',['phagocytosis','antigen presentation','inflammation'],0],
['Dendritic cells','immune-cells','cell','professional antigen-presenting cells that prime naive T cells in the lymph nodes','the bridge between innate and adaptive immunity',['antigen presentation','T cell priming','lymph nodes'],0],
['Neutrophils','immune-cells','cell','the most abundant white blood cells; first responders that engulf bacteria','form pus at infection sites',['bacterial killing','inflammation','first responders'],0],
['Mast cells','immune-cells','cell','release histamine and other mediators that drive allergic reactions','IgE bound to mast cells triggers degranulation',['histamine','allergy','anaphylaxis'],0],
['Immunoglobulin G (IgG)','antibodies','antibody','the most abundant antibody in blood, about 75-80% of immunoglobulin; the main antibody of the secondary response','the only antibody class that crosses the placenta',['long-term immunity','placenta','opsonization'],0],
['Immunoglobulin M (IgM)','antibodies','antibody','the first antibody produced in a primary immune response; the largest antibody, a pentamer','does not cross the placenta',['primary response','complement activation','pentamer'],0],
['Immunoglobulin A (IgA)','antibodies','antibody','the secretory antibody of mucous membranes, saliva, tears, and breast milk; blocks pathogen attachment','does not fix complement',['mucosal immunity','breast milk','secretions'],0],
['Immunoglobulin E (IgE)','antibodies','antibody','mediates immediate hypersensitivity: it binds mast cells and basophils, triggering histamine release','the main host defense against helminth parasites',['allergy','asthma','parasites'],0],
['Immunoglobulin D (IgD)','antibodies','antibody','found on the surface of naive B cells, where it acts as an antigen receptor','present in small amounts in blood',['B cell receptor','activation','naive B cells'],0],
['Antibody structure','antibodies','molecule','Y-shaped proteins of two heavy and two light chains (H2L2); the tips bind antigen while the stem recruits immune functions','the variable regions determine specificity',['heavy chains','light chains','antigen binding'],0],
['Smallpox vaccine (Jenner)','vaccines','vaccine','in 1796 Edward Jenner inoculated cowpox matter to protect against smallpox, founding the science of vaccinology','smallpox was eradicated by vaccination, declared in 1980',['cowpox','eradication','variolation'],1796],
['Rabies vaccine (Pasteur)','vaccines','vaccine','in 1885 Louis Pasteur vaccinated Joseph Meister against rabies with dried spinal cord preparations','Pasteur coined the word vaccination in honor of Jenner',['rabies','post-exposure','Pasteur'],1885],
['Polio vaccine (Salk)','vaccines','vaccine','Jonas Salk\u2019s formalin-inactivated polio vaccine, licensed in 1955 after field trials in over 1.3 million children','dramatically reduced polio in the United States',['IPV','1954 field trial','inactivated'],1955],
['Oral polio vaccine (Sabin)','vaccines','vaccine','Albert Sabin\u2019s live-attenuated oral polio vaccine, given as drops, approved around 1960','easier to administer in mass campaigns',['OPV','live-attenuated','mass campaigns'],1960],
['Yellow fever vaccine (17D)','vaccines','vaccine','Max Theiler\u2019s 17D strain, developed in 1937, remains one of the most effective vaccines ever made','Theiler was awarded the Nobel Prize',['17D strain','single dose','lifelong immunity'],1937],
['MMR vaccine','vaccines','vaccine','the combined live-attenuated vaccine against measles, mumps, and rubella','two doses give long-lasting protection',['measles','mumps','rubella'],0],
['Phagocytosis','innate-immunity','process','the engulfment and digestion of pathogens by phagocytes such as neutrophils and macrophages','a cornerstone of innate defense',['neutrophils','macrophages','engulfment'],0],
['Inflammation','innate-immunity','process','redness, heat, swelling, and pain from increased blood flow and immune-cell recruitment','the cardinal signs described since antiquity',['redness','swelling','recruitment'],0],
['Skin and mucosal barriers','innate-immunity','barrier','the physical and chemical first lines: skin, mucus, stomach acid, and antimicrobial peptides','block most pathogens before immunity engages',['skin','mucus','stomach acid'],0],
['Clonal selection','adaptive-immunity','process','lymphocytes with matching receptors are selected and expanded when they meet their antigen','explains the specificity and memory of immunity',['lymphocytes','expansion','specificity'],0],
['Immunological memory','adaptive-immunity','process','memory B and T cells persist after infection, responding faster and stronger on re-exposure','the principle behind every vaccine',['memory cells','booster doses','faster response'],0],
['MHC antigen presentation','adaptive-immunity','molecule','MHC molecules display peptide fragments to T cells: class I to killer T cells, class II to helper T cells','discovered through transplant genetics',['MHC class I','MHC class II','T cell recognition'],0],
['The complement system','complement-system','system','a cascade of blood proteins that punch holes in pathogens, opsonize them, and recruit inflammation','three activation pathways converge on the same outcome',['opsonization','membrane attack','inflammation'],0],
['Interferons','cytokines','molecule','signaling proteins that warn neighboring cells of viral infection and activate defenses','among the first cytokines used as medicines',['antiviral state','signaling','therapy'],0],
['Interleukins','cytokines','molecule','messenger proteins coordinating white blood cell communication and growth','dozens identified, numbered IL-1 upward',['communication','inflammation','growth'],0],
['Rheumatoid arthritis','autoimmunity','disorder','an autoimmune attack on joint linings causing chronic inflammation and damage','treated with immunosuppressive biologics',['joints','autoantibodies','biologics'],0],
['Type 1 diabetes','autoimmunity','disorder','autoimmune destruction of the insulin-producing beta cells of the pancreas','requires lifelong insulin replacement',['beta cells','insulin','autoimmunity'],0],
['Systemic lupus erythematosus','autoimmunity','disorder','a systemic autoimmune disease producing antibodies against the body\u2019s own nuclear components','can affect skin, joints, kidneys, and brain',['autoantibodies','systemic','flares'],0],
['Hay fever','allergies','disorder','an IgE-mediated allergy to pollen causing sneezing, itchy eyes, and runny nose','mast-cell histamine release drives the symptoms',['pollen','IgE','histamine'],0],
['Anaphylaxis','allergies','disorder','a severe systemic allergic reaction that can close airways within minutes','epinephrine is the emergency treatment',['epinephrine','emergency','systemic'],0],
['Transplant rejection','transplantation','process','the recipient\u2019s immune system attacks donor tissue recognized as foreign through MHC differences','controlled with immunosuppressive drugs',['MHC matching','immunosuppression','graft'],0],
['Graft-versus-host disease','transplantation','disorder','transplanted immune cells attack the recipient\u2019s tissues after bone-marrow transplant','a major complication of allogeneic transplant',['bone marrow','donor T cells','complication'],0]
];
var ASPECTS=['overview','function deep-dive','clinical relevance','historical timeline','research frontiers','comparative analysis'];
var CONTEXTS=['clinical case review','laboratory study','immunization program','educational module','research survey','therapeutic program'];
var TYPELBL={'cell':'immune cell','antibody':'antibody class','vaccine':'vaccine','process':'immune process','molecule':'immune molecule','system':'immune system','barrier':'immune barrier','disorder':'immune disorder'};
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=ANCH.filter(function(a){return a[1]===cat;});
  if(!pool.length)pool=ANCH;
  var a=pick(pool,rnd);
  var mode=rnd()<0.45?'profile':'study';
  var aspect=pick(ASPECTS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var serial='R-'+(10000+seed);
  var title,desc,src,code=null,assoc=a[5].slice();
  if(mode==='profile'){
    code=serial;
    title=a[0]+': '+aspect+' ('+serial+')';
    var s1=a[0]+' is a '+(TYPELBL[a[2]]||a[2])+' of the immune system. '+(a[6]>0?'Dated to '+a[6]+'. ':'')+'Its role: '+a[3]+'.';
    var s2='Key fact: '+a[4]+'.';
    var s3='Closely associated with '+a[5][0]+', '+a[5][1]+', and '+a[5][2]+'.';
    if(aspect==='function deep-dive')desc=s1+' '+s2+' This function explains why '+a[0]+' is central to '+a[1].replace(/-/g,' ')+'. '+s3;
    else if(aspect==='clinical relevance')desc=s1+' '+s3+' Clinicians monitor '+a[0]+' because immune health depends on it. '+s2;
    else if(aspect==='historical timeline')desc=(a[6]>0?'In '+a[6]+', ':'In the history of immunology, ')+a[0]+' entered the record. '+s1+' '+s2;
    else if(aspect==='research frontiers')desc=s1+' '+s2+' Researchers now probe '+a[0]+' with single-cell sequencing and spatial imaging. '+s3;
    else if(aspect==='comparative analysis')desc=s1+' Compared with related immune components, '+a[0]+' is distinguished by this: '+a[3]+' '+s2;
    else desc=s1+' '+s2+' '+s3;
    src='online';
  }else{
    code='CS-'+(1000+((seed*7919)%9000))+'/'+serial;
    var ctx=pick(CONTEXTS,rnd);
    var n=ri(rnd,30,4000),yr=ri(rnd,2016,2026);
    title=a[0]+' \u2014 '+ctx+' '+code;
    desc='This generated study ('+code+', compiled '+yr+') reviews '+n.toLocaleString('en-US')+' documented observations of '+a[0]+' in a '+ctx+' setting. '+
      'The established facts remain: '+a[3]+' '+
      'Observers in this illustrative study focused on '+a[5][0]+' and '+a[5][1]+', reporting patterns consistent with the published literature. '+
      'As a Signature-generated study record, the scenario is illustrative and educational; the core facts about '+a[0]+' come from published immunology. This content is educational only, not medical advice.';
    src='signature';assoc=[a[5][0],a[5][1],ctx+' (generated study)'];
  }
  return {id:id,title:title,description:desc,category:a[1],
    spec:{subject:a[0],subject_type:a[2],category:a[1],role:a[3],key_fact:a[4],associated:assoc,year:a[6]||null,aspect:aspect,study_code:code,educational:'Educational reference only; not medical advice.'},
    src:src,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-IMM-\d{6}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<8||r.title.length>160)e.push('title');
  if(typeof r.description!=='string'||r.description.length<120||r.description.length>1600)e.push('description');
  else{var parts=r.description.split('. ');if(parts.length<2)e.push('description-sentences');if(!/\.$/.test(r.description.trim()))e.push('description-period');}
  if(CATS.indexOf(r.category)<0)e.push('category');
  var s=r.spec;
  if(!s||typeof s!=='object')e.push('spec');
  else{
    if(!s.subject||typeof s.subject!=='string')e.push('spec.subject');
    if(!s.subject_type||typeof s.subject_type!=='string')e.push('spec.subject_type');
    if(!s.role||typeof s.role!=='string')e.push('spec.role');
    if(!s.key_fact||typeof s.key_fact!=='string')e.push('spec.key_fact');
    if(!Array.isArray(s.associated)||s.associated.length<2||s.associated.some(function(x){return typeof x!=='string'||!x.length;}))e.push('spec.associated');
    if(!(s.year===null||(Number.isInteger(s.year)&&s.year>=1500&&s.year<=2026)))e.push('spec.year');
    if(s.educational!=='Educational reference only; not medical advice.')e.push('spec.educational');
  }
  if(r.src!=='online'&&r.src!=='signature')e.push('src');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-immunology-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('immunology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
