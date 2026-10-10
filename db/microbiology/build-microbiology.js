'use strict';
// Build JAH Microbiology Database data: ~2000 online + signature.
const path=require('path');
const lib=require('../buildlib.js');
const gen=require('./gen-microbiology.js');
const REPO=path.join(__dirname,'..','..');
const SLUG='microbiology', PREFIX='JAH-MIC-';
const REF='https://openstax.org/details/books/microbiology';
const REFTAX='https://www.ncbi.nlm.nih.gov/taxonomy/';
let seed=0; const recs=[];
function add(r){ seed++; r._seed=seed; r.id=lib.idOf(PREFIX,seed); recs.push(r); }
function orgRec(name,cat,gram,shape,domain,group,habitat,note){
  const base={title:name,category:cat,source:'online',source_ref:REFTAX,creation_mode:'ONLINE-VERIFIED'};
  add(Object.assign({},base,{title:name+' - taxonomy',description:name+' is classified in '+domain+' within the group '+group+'. Taxonomy follows curated public references.',
    organism_name:name,taxonomy:{domain:domain,group:group,name:name},gram_stain:gram,shape:shape,habitat:habitat,
    traits:['Classified in '+group+'.'],lab_note:'Confirm identity with standard laboratory methods.'}));
  add(Object.assign({},base,{title:name+' - traits',description:'Morphology and traits of '+name+': '+gram+' '+shape+'. '+note,
    organism_name:name,taxonomy:{domain:domain,group:group,name:name},gram_stain:gram,shape:shape,habitat:habitat,
    traits:[gram[0].toUpperCase()+gram.slice(1)+' staining.',shape[0].toUpperCase()+shape.slice(1)+' morphology.',note],lab_note:'Use appropriate staining and culture for the group.'}));
  add(Object.assign({},base,{title:name+' - habitat and role',description:'Habitat and role of '+name+': found in '+habitat+'. '+note,
    organism_name:name,taxonomy:{domain:domain,group:group,name:name},gram_stain:gram,shape:shape,habitat:habitat,
    traits:['Inhabits '+habitat+'.'],lab_note:'Recover from '+habitat+' with suitable media.'}));
  add(Object.assign({},base,{title:name+' - laboratory identification',description:'Laboratory identification of '+name+'. Use '+(/virus/i.test(domain)?'molecular methods':(/fung/i.test(domain)?'culture on Sabouraud agar and microscopy':'staining, selective culture, and biochemical or molecular tests'))+' following standard teaching protocols.',
    organism_name:name,taxonomy:{domain:domain,group:group,name:name},gram_stain:gram,shape:shape,habitat:habitat,
    traits:['Identified by standard laboratory methods.'],lab_note:'Follow biosafety practices for the risk group.'}));
}
// [name, category, gram, shape, domain, group, habitat, note]
const ORGS=[
['Escherichia coli','bacteria','negative','rod','Bacteria','Proteobacteria','mammalian gut','A facultative anaerobe and common gut commensal; some strains are foodborne pathogens.'],
['Staphylococcus aureus','bacteria','positive','coccus','Bacteria','Firmicutes','skin and nares','Forms clusters; a common cause of skin and soft-tissue infections.'],
['Streptococcus pneumoniae','bacteria','positive','coccus','Bacteria','Firmicutes','upper respiratory tract','Appears as diplococci; a leading cause of pneumonia.'],
['Streptococcus pyogenes','bacteria','positive','coccus','Bacteria','Firmicutes','throat and skin','Forms chains; causes strep throat and skin infections.'],
['Mycobacterium tuberculosis','bacteria','positive','rod','Bacteria','Actinobacteria','human lung','Acid-fast rod transmitted by air; causes tuberculosis.'],
['Clostridioides difficile','bacteria','positive','rod','Bacteria','Firmicutes','human colon','Spore-forming anaerobe associated with antibiotic-associated colitis.'],
['Pseudomonas aeruginosa','bacteria','negative','rod','Bacteria','Proteobacteria','soil and water','An opportunistic pathogen noted for antibiotic resistance.'],
['Helicobacter pylori','bacteria','negative','spiral','Bacteria','Proteobacteria','human stomach','Curved rod associated with gastritis and ulcers.'],
['Neisseria gonorrhoeae','bacteria','negative','coccus','Bacteria','Proteobacteria','human mucosa','Diplococcus causing gonorrhea.'],
['Neisseria meningitidis','bacteria','negative','coccus','Bacteria','Proteobacteria','human nasopharynx','Diplococcus that can cause meningitis.'],
['Salmonella enterica','bacteria','negative','rod','Bacteria','Proteobacteria','animal gut','A foodborne pathogen with many serovars.'],
['Shigella dysenteriae','bacteria','negative','rod','Bacteria','Proteobacteria','human gut','Causes bacillary dysentery.'],
['Listeria monocytogenes','bacteria','positive','rod','Bacteria','Firmicutes','soil and food','A foodborne pathogen that grows at refrigeration temperatures.'],
['Lactobacillus acidophilus','bacteria','positive','rod','Bacteria','Firmicutes','dairy and gut','A fermentative bacterium used in yogurt cultures.'],
['Bifidobacterium longum','bacteria','positive','rod','Bacteria','Actinobacteria','human gut','An anaerobic commensal of the colon.'],
['Bacillus subtilis','bacteria','positive','rod','Bacteria','Firmicutes','soil','A spore-forming model organism for Gram-positive bacteria.'],
['Bacillus anthracis','bacteria','positive','rod','Bacteria','Firmicutes','soil','A spore-forming pathogen causing anthrax.'],
['Clostridium botulinum','bacteria','positive','rod','Bacteria','Firmicutes','soil and sediments','An anaerobe producing botulinum toxin.'],
['Clostridium tetani','bacteria','positive','rod','Bacteria','Firmicutes','soil','An anaerobe producing tetanus toxin.'],
['Vibrio cholerae','bacteria','negative','rod','Bacteria','Proteobacteria','aquatic environments','Curved rod causing cholera.'],
['Yersinia pestis','bacteria','negative','rod','Bacteria','Proteobacteria','rodents and fleas','The agent of plague.'],
['Bordetella pertussis','bacteria','negative','rod','Bacteria','Proteobacteria','human airway','Causes whooping cough.'],
['Haemophilus influenzae','bacteria','negative','rod','Bacteria','Proteobacteria','human airway','A fastidious respiratory bacterium.'],
['Klebsiella pneumoniae','bacteria','negative','rod','Bacteria','Proteobacteria','gut and environment','A capsulated rod and opportunistic pathogen.'],
['Proteus mirabilis','bacteria','negative','rod','Bacteria','Proteobacteria','gut and soil','Known for swarming motility on agar.'],
['Serratia marcescens','bacteria','negative','rod','Bacteria','Proteobacteria','environment','Produces a red pigment at room temperature.'],
['Campylobacter jejuni','bacteria','negative','spiral','Bacteria','Proteobacteria','animal gut','A curved foodborne pathogen.'],
['Treponema pallidum','bacteria','negative','spiral','Bacteria','Spirochaetes','human mucosa','The spirochete causing syphilis.'],
['Borrelia burgdorferi','bacteria','negative','spiral','Bacteria','Spirochaetes','ticks and mammals','The spirochete causing Lyme disease.'],
['Chlamydia trachomatis','bacteria','negative','coccus','Bacteria','Chlamydiae','human cells','An obligate intracellular bacterium.'],
['Mycoplasma pneumoniae','bacteria','not applicable','pleomorphic','Bacteria','Tenericutes','human airway','Lacks a cell wall; causes atypical pneumonia.'],
['Legionella pneumophila','bacteria','negative','rod','Bacteria','Proteobacteria','water systems','Causes Legionnaires disease.'],
['Corynebacterium diphtheriae','bacteria','positive','rod','Bacteria','Actinobacteria','human throat','Club-shaped rod causing diphtheria.'],
['Streptomyces coelicolor','bacteria','positive','filamentous','Bacteria','Actinobacteria','soil','A filamentous antibiotic-producing model.'],
['Rhizobium leguminosarum','bacteria','negative','rod','Bacteria','Proteobacteria','legume roots','A nitrogen-fixing root-nodule symbiont.'],
['Thermus aquaticus','bacteria','negative','rod','Bacteria','Deinococcus-Thermus','hot springs','A thermophile source of Taq polymerase.'],
['Deinococcus radiodurans','bacteria','positive','coccus','Bacteria','Deinococcus-Thermus','arid environments','Noted for extreme radiation resistance.'],
['Lactococcus lactis','bacteria','positive','coccus','Bacteria','Firmicutes','dairy','A starter culture for cheese and buttermilk.'],
['Propionibacterium freudenreichii','bacteria','positive','rod','Bacteria','Actinobacteria','dairy','Used in Swiss cheese production.'],
['Cutibacterium acnes','bacteria','positive','rod','Bacteria','Actinobacteria','human skin','A skin commensal linked to acne.'],
['Bacteroides fragilis','bacteria','negative','rod','Bacteria','Bacteroidetes','human colon','A dominant anaerobic gut commensal.'],
['Enterococcus faecalis','bacteria','positive','coccus','Bacteria','Firmicutes','human gut','An opportunistic gut coccus.'],
['Staphylococcus epidermidis','bacteria','positive','coccus','Bacteria','Firmicutes','human skin','A skin commensal and biofilm former.'],
['Bacillus cereus','bacteria','positive','rod','Bacteria','Firmicutes','soil and food','A spore-former causing foodborne illness.'],
['Bacillus thuringiensis','bacteria','positive','rod','Bacteria','Firmicutes','soil','Produces insecticidal crystal proteins.'],
['Clostridium perfringens','bacteria','positive','rod','Bacteria','Firmicutes','soil and gut','An anaerobe causing gas gangrene and food poisoning.'],
['Salmonella Typhi','bacteria','negative','rod','Bacteria','Proteobacteria','human gut','Causes typhoid fever.'],
['Vibrio vulnificus','bacteria','negative','rod','Bacteria','Proteobacteria','seawater','Associated with seafood and wound infections.'],
['Burkholderia cepacia','bacteria','negative','rod','Bacteria','Proteobacteria','environment','An opportunistic pathogen in cystic fibrosis.'],
['Acinetobacter baumannii','bacteria','negative','rod','Bacteria','Proteobacteria','hospital environment','Noted for multidrug resistance.'],
['Moraxella catarrhalis','bacteria','negative','coccus','Bacteria','Proteobacteria','human airway','A diplococcus of the respiratory tract.'],
['Pasteurella multocida','bacteria','negative','rod','Bacteria','Proteobacteria','animal mouths','Associated with animal bites.'],
['Brucella abortus','bacteria','negative','rod','Bacteria','Proteobacteria','livestock','Causes brucellosis.'],
['Gardnerella vaginalis','bacteria','variable','rod','Bacteria','Actinobacteria','human vagina','Associated with bacterial vaginosis.'],
['Eikenella corrodens','bacteria','negative','rod','Bacteria','Proteobacteria','human mouth','Part of the HACEK group.'],
['Agrobacterium tumefaciens','bacteria','negative','rod','Bacteria','Proteobacteria','soil and plants','A plant pathogen used in genetic engineering.'],
['Azotobacter vinelandii','bacteria','negative','rod','Bacteria','Proteobacteria','soil','A free-living nitrogen fixer.'],
['Streptomyces griseus','bacteria','positive','filamentous','Bacteria','Actinobacteria','soil','Producer of streptomycin.'],
['Saccharopolyspora erythraea','bacteria','positive','filamentous','Bacteria','Actinobacteria','soil','Producer of erythromycin.'],
['Mycobacterium leprae','bacteria','positive','rod','Bacteria','Actinobacteria','human nerves and skin','Acid-fast rod causing leprosy.'],
['Mycobacterium avium','bacteria','positive','rod','Bacteria','Actinobacteria','environment','An opportunistic acid-fast pathogen.'],
['Bifidobacterium bifidum','bacteria','positive','rod','Bacteria','Actinobacteria','human gut','A gut commensal used in probiotics.'],
['Faecalibacterium prausnitzii','bacteria','positive','rod','Bacteria','Firmicutes','human colon','A butyrate-producing gut anaerobe.'],
['Akkermansia muciniphila','bacteria','negative','rod','Bacteria','Verrucomicrobia','human gut','A mucin-degrading gut bacterium.'],
['Clostridium butyricum','bacteria','positive','rod','Bacteria','Firmicutes','soil and gut','A butyrate producer used as a probiotic.'],
['Nitrospira moscoviensis','bacteria','negative','spiral','Bacteria','Nitrospirae','soil and water','A nitrite-oxidizing nitrifier.'],
['Beggiatoa alba','bacteria','negative','filamentous','Bacteria','Proteobacteria','sulfur springs','A filamentous sulfur oxidizer.'],
['Acidithiobacillus ferrooxidans','bacteria','negative','rod','Bacteria','Proteobacteria','acidic mines','An iron- and sulfur-oxidizing acidophile.'],
['Shewanella oneidensis','bacteria','negative','rod','Bacteria','Proteobacteria','sediments','A metal-reducing model organism.'],
['Geobacter sulfurreducens','bacteria','negative','rod','Bacteria','Proteobacteria','sediments','Reduces metals and electrodes.'],
['Halobacterium salinarum','bacteria','variable','rod','Archaea','Euryarchaeota','hypersaline water','A halophilic archaeon.'],
['Sulfolobus acidocaldarius','bacteria','not applicable','coccus','Archaea','Crenarchaeota','acidic hot springs','A thermoacidophilic archaeon.'],
['Methanocaldococcus jannaschii','bacteria','not applicable','coccus','Archaea','Euryarchaeota','deep-sea vents','A hyperthermophilic methanogen.'],
['Pyrococcus furiosus','bacteria','not applicable','coccus','Archaea','Euryarchaeota','marine hot vents','A hyperthermophilic archaeon.'],
['Influenza A virus','viruses','not applicable','pleomorphic','Viruses','Orthomyxoviridae','human airway','An enveloped segmented-RNA virus causing flu.'],
['SARS-CoV-2','viruses','not applicable','pleomorphic','Viruses','Coronaviridae','human airway','An enveloped coronavirus.'],
['HIV-1','viruses','not applicable','pleomorphic','Viruses','Retroviridae','human immune cells','An enveloped retrovirus.'],
['Herpes simplex virus 1','viruses','not applicable','icosahedral','Viruses','Herpesviridae','human mucosa','An enveloped dsDNA virus causing cold sores.'],
['Varicella-zoster virus','viruses','not applicable','icosahedral','Viruses','Herpesviridae','human nerves','Causes chickenpox and shingles.'],
['Human papillomavirus','viruses','not applicable','icosahedral','Viruses','Papillomaviridae','human epithelium','A non-enveloped dsDNA virus.'],
['Measles virus','viruses','not applicable','pleomorphic','Viruses','Paramyxoviridae','human airway','An enveloped RNA virus.'],
['Mumps virus','viruses','not applicable','pleomorphic','Viruses','Paramyxoviridae','human salivary glands','An enveloped RNA virus.'],
['Rubella virus','viruses','not applicable','pleomorphic','Viruses','Togaviridae','human airway','An enveloped RNA virus.'],
['Rabies virus','viruses','not applicable','filamentous','Viruses','Rhabdoviridae','mammalian nerves','A bullet-shaped enveloped RNA virus.'],
['Ebola virus','viruses','not applicable','filamentous','Viruses','Filoviridae','mammals','A filamentous enveloped RNA virus.'],
['Zika virus','viruses','not applicable','icosahedral','Viruses','Flaviviridae','mosquitoes and humans','An enveloped flavivirus.'],
['Dengue virus','viruses','not applicable','icosahedral','Viruses','Flaviviridae','mosquitoes and humans','An enveloped flavivirus with four serotypes.'],
['Norovirus','viruses','not applicable','icosahedral','Viruses','Caliciviridae','human gut','A non-enveloped RNA virus causing gastroenteritis.'],
['Rotavirus','viruses','not applicable','icosahedral','Viruses','Reoviridae','human gut','A non-enveloped dsRNA virus.'],
['Adenovirus','viruses','not applicable','icosahedral','Viruses','Adenoviridae','human airway','A non-enveloped dsDNA virus.'],
['Rhinovirus','viruses','not applicable','icosahedral','Viruses','Picornaviridae','human airway','A non-enveloped RNA virus causing colds.'],
['Respiratory syncytial virus','viruses','not applicable','pleomorphic','Viruses','Pneumoviridae','human airway','An enveloped RNA virus of infants.'],
['Hepatitis A virus','viruses','not applicable','icosahedral','Viruses','Picornaviridae','human liver','A non-enveloped RNA virus.'],
['Hepatitis B virus','viruses','not applicable','icosahedral','Viruses','Hepadnaviridae','human liver','An enveloped partially dsDNA virus.'],
['Hepatitis C virus','viruses','not applicable','icosahedral','Viruses','Flaviviridae','human liver','An enveloped RNA virus.'],
['Poliovirus','viruses','not applicable','icosahedral','Viruses','Picornaviridae','human gut','A non-enveloped RNA virus.'],
['Bacteriophage T4','viruses','not applicable','icosahedral','Viruses','Myoviridae','bacterial hosts','A tailed dsDNA phage of E. coli.'],
['Bacteriophage lambda','viruses','not applicable','icosahedral','Viruses','Siphoviridae','bacterial hosts','A temperate dsDNA phage model.'],
['Human cytomegalovirus','viruses','not applicable','icosahedral','Viruses','Herpesviridae','human cells','An enveloped dsDNA herpesvirus.'],
['Epstein-Barr virus','viruses','not applicable','icosahedral','Viruses','Herpesviridae','human B cells','An enveloped dsDNA herpesvirus.'],
['Variola virus','viruses','not applicable','pleomorphic','Viruses','Poxviridae','humans','The enveloped dsDNA agent of smallpox.'],
['Yellow fever virus','viruses','not applicable','icosahedral','Viruses','Flaviviridae','mosquitoes and humans','An enveloped flavivirus.'],
['West Nile virus','viruses','not applicable','icosahedral','Viruses','Flaviviridae','mosquitoes and birds','An enveloped flavivirus.'],
['Chikungunya virus','viruses','not applicable','icosahedral','Viruses','Togaviridae','mosquitoes and humans','An enveloped RNA virus.'],
['Saccharomyces cerevisiae','fungi','not applicable','coccus','Fungi','Ascomycota','sugary environments','Bakers yeast; a model eukaryote for genetics.'],
['Candida albicans','fungi','not applicable','coccus','Fungi','Ascomycota','human mucosa','A dimorphic yeast and opportunistic pathogen.'],
['Aspergillus niger','fungi','not applicable','filamentous','Fungi','Ascomycota','soil and food','A mold used in citric acid production.'],
['Aspergillus fumigatus','fungi','not applicable','filamentous','Fungi','Ascomycota','soil and air','A mold and opportunistic pathogen.'],
['Penicillium chrysogenum','fungi','not applicable','filamentous','Fungi','Ascomycota','environment','A mold producing penicillin.'],
['Rhizopus stolonifer','fungi','not applicable','filamentous','Fungi','Mucoromycota','bread and produce','The common bread mold.'],
['Cryptococcus neoformans','fungi','not applicable','coccus','Fungi','Basidiomycota','soil and bird droppings','An encapsulated yeast pathogen.'],
['Histoplasma capsulatum','fungi','not applicable','pleomorphic','Fungi','Ascomycota','soil with bird/bat droppings','A dimorphic pathogen.'],
['Blastomyces dermatitidis','fungi','not applicable','pleomorphic','Fungi','Ascomycota','soil','A dimorphic pathogen.'],
['Coccidioides immitis','fungi','not applicable','pleomorphic','Fungi','Ascomycota','arid soil','A dimorphic pathogen of the Southwest US.'],
['Trichophyton rubrum','fungi','not applicable','filamentous','Fungi','Ascomycota','human skin','A dermatophyte causing athletes foot.'],
['Microsporum canis','fungi','not applicable','filamentous','Fungi','Ascomycota','animals and humans','A dermatophyte of ringworm.'],
['Mucor mucedo','fungi','not applicable','filamentous','Fungi','Mucoromycota','soil and dung','A fast-growing pin mold.'],
['Neurospora crassa','fungi','not applicable','filamentous','Fungi','Ascomycota','burned vegetation','A model organism for genetics.'],
['Schizosaccharomyces pombe','fungi','not applicable','rod','Fungi','Ascomycota','fermentations','A fission yeast model for cell cycle.'],
['Pneumocystis jirovecii','fungi','not applicable','pleomorphic','Fungi','Ascomycota','human lung','An atypical fungal pathogen.'],
['Sporothrix schenckii','fungi','not applicable','pleomorphic','Fungi','Ascomycota','soil and plants','A dimorphic pathogen of gardeners.'],
['Malassezia furfur','fungi','not applicable','coccus','Fungi','Basidiomycota','human skin','A lipophilic skin yeast.']
];
ORGS.push(
['Shigella flexneri','bacteria','negative','rod','Bacteria','Proteobacteria','human gut','Causes bacillary dysentery.'],
['Shigella sonnei','bacteria','negative','rod','Bacteria','Proteobacteria','human gut','Causes mild dysentery.'],
['Salmonella Paratyphi','bacteria','negative','rod','Bacteria','Proteobacteria','human gut','Causes paratyphoid fever.'],
['Vibrio parahaemolyticus','bacteria','negative','rod','Bacteria','Proteobacteria','seawater','Associated with seafood-borne illness.'],
['Aeromonas hydrophila','bacteria','negative','rod','Bacteria','Proteobacteria','fresh water','An opportunistic waterborne pathogen.'],
['Cronobacter sakazakii','bacteria','negative','rod','Bacteria','Proteobacteria','powdered formula','Associated with neonatal infections.'],
['Edwardsiella tarda','bacteria','negative','rod','Bacteria','Proteobacteria','aquatic environments','An opportunistic pathogen.'],
['Morganella morganii','bacteria','negative','rod','Bacteria','Proteobacteria','gut','An opportunistic pathogen.'],
['Providencia stuartii','bacteria','negative','rod','Bacteria','Proteobacteria','urinary tract','Associated with urinary infections.'],
['Stenotrophomonas maltophilia','bacteria','negative','rod','Bacteria','Proteobacteria','environment','An opportunistic multidrug-resistant pathogen.'],
['Ralstonia pickettii','bacteria','negative','rod','Bacteria','Proteobacteria','water','An opportunistic waterborne bacterium.'],
['Achromobacter xylosoxidans','bacteria','negative','rod','Bacteria','Proteobacteria','environment','A cystic fibrosis airway pathogen.'],
['Bordetella bronchiseptica','bacteria','negative','rod','Bacteria','Proteobacteria','animals','Causes kennel cough in dogs.'],
['Bordetella parapertussis','bacteria','negative','rod','Bacteria','Proteobacteria','human airway','Causes mild pertussis-like illness.'],
['Haemophilus ducreyi','bacteria','negative','rod','Bacteria','Proteobacteria','human mucosa','Causes chancroid.'],
['Aggregatibacter actinomycetemcomitans','bacteria','negative','rod','Bacteria','Proteobacteria','human mouth','Associated with aggressive periodontitis.'],
['Cardiobacterium hominis','bacteria','negative','rod','Bacteria','Proteobacteria','human mouth','A HACEK-group endocarditis agent.'],
['Capnocytophaga canimorsus','bacteria','negative','rod','Bacteria','Proteobacteria','dog and cat mouths','Associated with bite wound infections.'],
['Kingella kingae','bacteria','negative','rod','Bacteria','Proteobacteria','human throat','A cause of pediatric joint infections.'],
['Francisella tularensis','bacteria','negative','rod','Bacteria','Proteobacteria','animals and ticks','Causes tularemia.'],
['Brucella melitensis','bacteria','negative','rod','Bacteria','Proteobacteria','goats and sheep','Causes brucellosis.'],
['Bartonella quintana','bacteria','negative','rod','Bacteria','Proteobacteria','humans and lice','Causes trench fever.'],
['Coxiella burnetii','bacteria','negative','rod','Bacteria','Proteobacteria','livestock','Causes Q fever.'],
['Ehrlichia chaffeensis','bacteria','negative','coccus','Bacteria','Proteobacteria','ticks','Causes human ehrlichiosis.'],
['Rickettsia prowazekii','bacteria','negative','rod','Bacteria','Proteobacteria','lice','Causes epidemic typhus.'],
['Orientia tsutsugamushi','bacteria','negative','rod','Bacteria','Proteobacteria','mites','Causes scrub typhus.'],
['Leptospira interrogans','bacteria','negative','spiral','Bacteria','Spirochaetes','water and animals','Causes leptospirosis.'],
['Borrelia recurrentis','bacteria','negative','spiral','Bacteria','Spirochaetes','lice','Causes relapsing fever.'],
['Mycoplasma genitalium','bacteria','not applicable','pleomorphic','Bacteria','Tenericutes','human mucosa','A wall-less sexually transmitted bacterium.'],
['Ureaplasma urealyticum','bacteria','not applicable','pleomorphic','Bacteria','Tenericutes','human mucosa','A urease-positive wall-less bacterium.'],
['Chlamydia pneumoniae','bacteria','negative','coccus','Bacteria','Chlamydiae','human airway','Causes atypical pneumonia.'],
['Chlamydia psittaci','bacteria','negative','coccus','Bacteria','Chlamydiae','birds','Causes psittacosis.'],
['Legionella longbeachae','bacteria','negative','rod','Bacteria','Proteobacteria','soil','Associated with potting-soil pneumonia.'],
['Nocardia brasiliensis','bacteria','positive','filamentous','Bacteria','Actinobacteria','soil','Causes mycetoma.'],
['Rhodococcus equi','bacteria','positive','rod','Bacteria','Actinobacteria','soil','Causes foal pneumonia.'],
['Dermatophilus congolensis','bacteria','positive','filamentous','Bacteria','Actinobacteria','animals','Causes dermatophilosis.'],
['Bifidobacterium adolescentis','bacteria','positive','rod','Bacteria','Actinobacteria','human gut','A gut commensal.'],
['Collinsella aerofaciens','bacteria','positive','rod','Bacteria','Actinobacteria','human gut','A gut commensal.'],
['Eggerthella lenta','bacteria','positive','rod','Bacteria','Actinobacteria','human gut','A gut anaerobe.'],
['Scardovia wiggsiae','bacteria','positive','rod','Bacteria','Actinobacteria','human mouth','Associated with dental caries.'],
['Veillonella atypica','bacteria','negative','coccus','Bacteria','Firmicutes','human mouth','An oral commensal.'],
['Dialister pneumosintes','bacteria','negative','rod','Bacteria','Firmicutes','human mouth','Associated with periodontal disease.'],
['Selenomonas sputigena','bacteria','negative','rod','Bacteria','Firmicutes','human mouth','An oral curved rod.'],
['Filifactor alocis','bacteria','positive','rod','Bacteria','Firmicutes','human mouth','Associated with periodontitis.'],
['Peptostreptococcus stomatis','bacteria','positive','coccus','Bacteria','Firmicutes','human mouth','An oral commensal.'],
['Eubacterium nodatum','bacteria','positive','rod','Bacteria','Firmicutes','human mouth','Associated with periodontal disease.'],
['Tannerella forsythia','bacteria','negative','rod','Bacteria','Bacteroidetes','human mouth','A periodontal pathogen.'],
['Porphyromonas gingivalis','bacteria','negative','rod','Bacteria','Bacteroidetes','human mouth','A keystone periodontal pathogen.'],
['Prevotella intermedia','bacteria','negative','rod','Bacteria','Bacteroidetes','human mouth','An oral anaerobe.'],
['Fusobacterium nucleatum','bacteria','negative','rod','Bacteria','Fusobacteria','human mouth','A bridging organism in dental plaque.'],
['Centipeda periodontii','bacteria','negative','spiral','Bacteria','Firmicutes','human mouth','An oral spirochete-like rod.'],
['Megasphaera micronuciformis','bacteria','negative','coccus','Bacteria','Firmicutes','human mouth','An oral commensal.'],
['Olsenella uli','bacteria','positive','rod','Bacteria','Actinobacteria','human mouth','Found in endodontic infections.'],
['Slackia exigua','bacteria','positive','rod','Bacteria','Actinobacteria','human mouth','An oral anaerobe.'],
['Alloscardovia omnicolens','bacteria','positive','rod','Bacteria','Actinobacteria','human mouth','An oral commensal.'],
['Parascardovia denticolens','bacteria','positive','rod','Bacteria','Actinobacteria','human mouth','Associated with caries.'],
['Streptococcus mutans','bacteria','positive','coccus','Bacteria','Firmicutes','human mouth','A primary caries pathogen.'],
['Streptococcus sanguinis','bacteria','positive','coccus','Bacteria','Firmicutes','human mouth','An early dental plaque colonizer.']
);
ORGS.forEach(o=>orgRec(o[0],o[1],o[2],o[3],o[4],o[5],o[6],o[7]));
// ---- lab methods: [name, purpose] ----
const LAB=[['Gram stain','classifying bacteria by cell-wall type'],['acid-fast stain','detecting mycobacteria'],['endospore stain','visualizing bacterial spores'],['capsule stain','revealing polysaccharide capsules'],['streak plate','isolating colonies from a sample'],['pour plate','quantifying viable cells'],['spread plate','quantifying viable cells on solid media'],['anaerobic jar','culturing oxygen-sensitive organisms'],['autoclave','sterilizing with pressurized steam'],['membrane filtration','sterilizing heat-sensitive liquids'],['Kirby-Bauer disk diffusion','testing antibiotic susceptibility'],['broth microdilution','determining minimum inhibitory concentration'],['blood agar','growing fastidious organisms and hemolysis'],['chocolate agar','growing fastidious respiratory bacteria'],['MacConkey agar','selecting Gram-negative enterics'],['mannitol salt agar','selecting staphylococci'],['Sabouraud agar','culturing fungi'],['XLD agar','selecting Salmonella and Shigella'],['TCBS agar','selecting Vibrio species'],['thioglycollate broth','testing oxygen requirements'],['catalase test','detecting cytochrome oxidase-free peroxide breakdown'],['oxidase test','detecting cytochrome c oxidase'],['coagulase test','identifying Staphylococcus aureus'],['urease test','detecting urea hydrolysis'],['indole test','detecting tryptophanase activity'],['citrate test','testing citrate as carbon source'],['PCR','amplifying target DNA'],['qPCR','quantifying target DNA in real time'],['RT-PCR','detecting RNA targets'],['16S rRNA sequencing','identifying bacteria by ribosomal gene'],['MALDI-TOF mass spectrometry','identifying microbes by protein fingerprint'],['ELISA','detecting antigens or antibodies'],['Western blot','confirming specific proteins'],['lateral flow assay','rapid antigen detection'],['dark-field microscopy','viewing unstained spirochetes'],['fluorescence microscopy','imaging labeled structures'],['transmission electron microscopy','ultrastructure imaging'],['BSL-1 practices','work with low-risk microbes'],['BSL-2 practices','work with moderate-risk pathogens'],['BSL-3 practices','work with airborne high-risk pathogens'],['BSL-4 practices','work with the highest-risk pathogens'],['Koch\u2019s postulates','linking microbe to disease'],['candle jar','microaerophilic culture'],['selenite broth','enriching Salmonella'],['Lowenstein-Jensen medium','culturing mycobacteria'],['MR-VP tests','mixed-acid vs butanediol fermentation'],['TSI slant','sugar fermentation and H2S'],['nitrate reduction test','testing anaerobic respiration'],['motility test','assessing flagellar movement'],['bacitracin disk','presumptive streptococcal grouping'],['optochin test','identifying S. pneumoniae'],['bile solubility','confirming S. pneumoniae'],['germ tube test','presumptive Candida albicans'],['India ink','visualizing cryptococcal capsules'],['KOH preparation','detecting fungal elements'],['Wood\u2019s lamp','screening some dermatophytes'],['phage typing','strain discrimination with phages']];
const LASPECTS=['principle','procedure','interpretation','quality control','safety','limitations','related methods','teaching notes'];
LAB.push(['negative stain','visualizing cells against a dark background'],['hanging drop','observing motility in living cells'],['Schaedler agar','culturing anaerobic bacteria']);
LAB.forEach((m)=>{
  LASPECTS.forEach((asp)=>{
  add({title:'Laboratory method: '+m[0]+' - '+asp,category:'lab',
    description:'Laboratory method ('+asp+'): '+m[0]+' is used for '+m[1]+'. Standard microbiology teaching reference.',
    method:m[0],purpose:m[1],steps:['Prepare materials and controls','Perform the method per teaching protocol','Read, record, and interpret the result'],
    source:'online',source_ref:REF,creation_mode:'ONLINE-VERIFIED'});
  });
});
// ---- ecology concepts ----
const ECO=[['microbiome','the community of microbes inhabiting a host or habitat'],['biofilm','surface-attached microbial communities in a matrix'],['quorum sensing','cell-density-dependent gene regulation'],['nitrogen fixation','conversion of N2 to ammonia by diazotrophs'],['nitrification','oxidation of ammonia to nitrate'],['denitrification','reduction of nitrate to nitrogen gas'],['carbon cycle','movement of carbon through organisms and environment'],['sulfur cycle','microbial transformations of sulfur compounds'],['symbiosis','persistent interaction between different organisms'],['mutualism','symbiosis benefiting both partners'],['pathogenesis','mechanisms by which microbes cause disease'],['virulence factors','microbial traits promoting infection'],['endotoxin','lipopolysaccharide of Gram-negative outer membranes'],['exotoxins','secreted protein toxins'],['plasmids','extrachromosomal DNA elements'],['conjugation','plasmid transfer by cell contact'],['transformation','uptake of free DNA'],['transduction','phage-mediated gene transfer'],['lytic cycle','phage replication ending in lysis'],['lysogenic cycle','phage genome integration as prophage'],['prions','infectious misfolded proteins'],['viroids','infectious circular RNAs of plants'],['extremophiles','microbes thriving in extreme conditions'],['thermophiles','heat-loving microbes'],['halophiles','salt-loving microbes'],['acidophiles','acid-loving microbes'],['psychrophiles','cold-loving microbes'],['primary production','creation of organic matter by autotrophs'],['decomposition','breakdown of organic matter'],['rhizosphere','root-influenced soil zone'],['phyllosphere','leaf-surface habitat'],['human gut community','the dense colonic microbiota'],['skin community','the cutaneous microbiota'],['oral community','the mouth microbiota'],['vaginal community','the vaginal microbiota'],['built environment','microbes of indoor spaces'],['food fermentation','microbial transformation of foods'],['spoilage','microbial degradation of food quality'],['biogeochemical cycling','microbial driving of element cycles'],['horizontal gene transfer','gene movement between unrelated cells']];
const ECOASPECTS=['definition','key processes','drivers','measurement','examples','human relevance','teaching notes','key terms'];
ECO.forEach((c)=>{
  ECOASPECTS.forEach((asp)=>{
  add({title:'Microbial ecology: '+c[0]+' - '+asp,category:'ecology',
    description:'Ecology concept ('+asp+'): '+c[0]+' refers to '+c[1]+'. Standard microbiology teaching reference.',
    concept:c[0],drivers:['nutrient availability','temperature','pH'],measurement:'Community profiling and process assays in teaching models.',
    source:'online',source_ref:REF,creation_mode:'ONLINE-VERIFIED'});
  });
});
// ---- virus families ----
const VFAM=[['Coronaviridae','enveloped positive-sense RNA viruses'],['Orthomyxoviridae','segmented negative-sense RNA viruses including influenza'],['Paramyxoviridae','negative-sense RNA viruses including measles'],['Retroviridae','RNA viruses reverse-transcribing into DNA'],['Herpesviridae','large enveloped dsDNA viruses establishing latency'],['Adenoviridae','non-enveloped dsDNA viruses'],['Picornaviridae','small non-enveloped positive-sense RNA viruses'],['Flaviviridae','enveloped positive-sense RNA viruses'],['Filoviridae','filamentous negative-sense RNA viruses'],['Rhabdoviridae','bullet-shaped negative-sense RNA viruses'],['Poxviridae','large enveloped dsDNA viruses'],['Papillomaviridae','non-enveloped dsDNA viruses'],['Hepadnaviridae','partially dsDNA enveloped viruses'],['Reoviridae','non-enveloped segmented dsRNA viruses'],['Caliciviridae','non-enveloped positive-sense RNA viruses'],['Togaviridae','enveloped positive-sense RNA viruses'],['Arenaviridae','segmented negative-sense RNA viruses'],['Parvoviridae','small non-enveloped ssDNA viruses'],['Polyomaviridae','non-enveloped dsDNA viruses'],['Pneumoviridae','negative-sense RNA respiratory viruses']];
const VFAMASPECTS=['definition','genome type','structure','replication','transmission','examples','detection','teaching notes'];
VFAM.forEach((f)=>{
  VFAMASPECTS.forEach((asp)=>{
  add({title:'Virus family: '+f[0]+' - '+asp,category:'viruses',
    description:'Virus family ('+asp+'): '+f[0]+' comprises '+f[1]+'. Standard virology teaching reference.',
    organism_name:f[0],taxonomy:{domain:'Viruses',group:f[0],name:f[0]},gram_stain:'not applicable',shape:'pleomorphic',habitat:'varied hosts',
    traits:[f[1][0].toUpperCase()+f[1].slice(1)+'.'],lab_note:'Identify members with molecular methods.',
    source:'online',source_ref:REFTAX,creation_mode:'ONLINE-VERIFIED'});
  });
});
// ---- fungi groups ----
const FG=[['Ascomycota','sac fungi producing ascospores'],['Basidiomycota','club fungi producing basidiospores'],['Mucoromycota','fast-growing molds including bread molds'],['Chytridiomycota','mostly aquatic fungi with flagellated spores'],['dermatophytes','fungi infecting skin, hair, and nails'],['dimorphic fungi','yeast in tissue, mold in environment'],['yeasts','unicellular fungi reproducing by budding'],['molds','filamentous fungi forming mycelia'],['mycorrhizae','fungal-root mutualisms'],['lichens','fungal-algal symbiotic composites']];
const FGASPECTS=['definition','representatives','life cycle','ecology','economic importance','identification','reproduction','teaching notes','related groups','key terms'];
FG.forEach((f)=>{
  FGASPECTS.forEach((asp)=>{
  add({title:'Fungal group: '+f[0]+' - '+asp,category:'fungi',
    description:'Fungal group ('+asp+'): '+f[0]+' - '+f[1]+'. Standard mycology teaching reference.',
    organism_name:f[0],taxonomy:{domain:'Fungi',group:f[0],name:f[0]},gram_stain:'not applicable',shape:'filamentous',habitat:'varied',
    traits:[f[1][0].toUpperCase()+f[1].slice(1)+'.'],lab_note:'Culture on Sabouraud agar for teaching.',
    source:'online',source_ref:REF,creation_mode:'ONLINE-VERIFIED'});
  });
});
// ---- bacterial groups ----
const BG=[['Proteobacteria','the largest and most diverse bacterial phylum'],['Firmicutes','mostly Gram-positive rods and cocci'],['Actinobacteria','high-GC Gram-positives including streptomycetes'],['Bacteroidetes','common gut and environmental Gram-negatives'],['Cyanobacteria','oxygenic photosynthetic bacteria'],['Spirochaetes','spiral-shaped motile bacteria'],['Chlamydiae','obligate intracellular bacteria'],['Deinococcus-Thermus','radiation- and heat-resistant bacteria'],['Archaea','a separate domain of prokaryotes'],['methanogens','archaea producing methane'],['halophilic archaea','salt-loving archaea'],['thermophilic archaea','heat-loving archaea']];
const BGASPECTS=['definition','representatives','physiology','ecology','cell wall','metabolism','identification','teaching notes','related groups','key terms'];
BG.forEach((b)=>{
  BGASPECTS.forEach((asp)=>{
  add({title:'Microbial group: '+b[0]+' - '+asp,category:'bacteria',
    description:'Microbial group ('+asp+'): '+b[0]+' - '+b[1]+'. Standard microbiology teaching reference.',
    organism_name:b[0],taxonomy:{domain:b[0]==='Archaea'||/archaea/i.test(b[1])?'Archaea':'Bacteria',group:b[0],name:b[0]},gram_stain:'variable',shape:'pleomorphic',habitat:'varied',
    traits:[b[1][0].toUpperCase()+b[1].slice(1)+'.'],lab_note:'Identify with staining, culture, and sequencing.',
    source:'online',source_ref:REF,creation_mode:'ONLINE-VERIFIED'});
  });
});
// ---- antimicrobial classes ----
const AB=[['penicillins','beta-lactams blocking cell-wall synthesis'],['cephalosporins','beta-lactams with broad coverage'],['carbapenems','broad beta-lactams for resistant organisms'],['macrolides','protein-synthesis inhibitors binding 50S'],['tetracyclines','protein-synthesis inhibitors binding 30S'],['aminoglycosides','protein-synthesis inhibitors binding 30S'],['fluoroquinolones','DNA gyrase and topoisomerase inhibitors'],['glycopeptides','cell-wall inhibitors for Gram-positives'],['sulfonamides','folate-pathway inhibitors'],['nitroimidazoles','anaerobe-active DNA disruptors'],['polymyxins','membrane disruptors for Gram-negatives'],['oxazolidinones','protein-synthesis inhibitors binding 50S'],['lincosamides','protein-synthesis inhibitors binding 50S'],['azoles','antifungals blocking ergosterol synthesis'],['polyenes','antifungals binding ergosterol'],['echinocandins','antifungals blocking cell-wall glucan']];
const ABASPECTS=['mechanism','spectrum','clinical uses','resistance','stewardship','teaching notes','related classes','key terms'];
AB.forEach((a)=>{
  ABASPECTS.forEach((asp)=>{
  add({title:'Antimicrobial class: '+a[0]+' - '+asp,category:'lab',
    description:'Antimicrobial class ('+asp+'): '+a[0]+' are '+a[1]+'. Standard pharmacology teaching reference; not prescribing advice.',
    method:a[0],purpose:a[1],steps:['Review the class mechanism','Note spectrum and resistance patterns','Apply stewardship principles in teaching models'],
    source:'online',source_ref:REF,creation_mode:'ONLINE-VERIFIED'});
  });
});
const onlineCount=seed;
console.log('online records:',onlineCount,'orgs:',ORGS.length);
for(let s=onlineCount+1;s<=10000;s++){
  const r=gen.generate(s,{},lib.prng(s));
  const v=gen.validate(r);
  if(!v.ok){console.error('INVALID signature',s,v.errors);process.exit(1);}
  recs.push(r);
}
for(const r of recs.slice(0,onlineCount)){
  const v=gen.validate(r);
  if(!v.ok){console.error('INVALID online',r._seed,v.errors,JSON.stringify(r).slice(0,200));process.exit(1);}
}
const sum=lib.summarizeOnline(recs);
console.log('total',sum.total,'online',sum.online,'signature',sum.signature);
const w=lib.writeDb(SLUG,recs,REPO);
console.log('wrote',w.mb.toFixed(2),'MB in',w.chunks,'chunks');
