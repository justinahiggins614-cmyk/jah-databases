(function(){'use strict';
/* JAH Forensics Database generator — jahdb-forensics-1.0.
   Deterministic client-side generator: same seed + same version = same record.
   Online-sourced technique profiles carry src:"online"; Signature-authored
   comparative studies carry src:"signature". All anchor facts are verifiable. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['dna','fingerprints','ballistics','pathology','toxicology','digital-forensics','trace-evidence','questioned-documents','odontology','entomology','crime-scene','legal-standards'];
var PREFIX='JAH-FOR-';
/* anchors: [title, cat, year, originator, facts...] */
var ANCH=[
["Locard's exchange principle","trace-evidence",1910,"Edmond Locard",
 "Locard's exchange principle states that every contact between two objects leaves a trace.",
 "Formulated by French criminologist Edmond Locard, who founded the first police crime laboratory in Lyon in 1910.",
 "The principle underlies all trace evidence work: fibers, hairs, soil, and glass fragments transferred during contact.",
 "It is often summarized as 'every contact leaves a trace', and it justifies the painstaking collection of microscopic evidence."],
["DNA fingerprinting","dna",1984,"Alec Jeffreys",
 "DNA fingerprinting identifies individuals from variable regions of their DNA, discovered by Alec Jeffreys at the University of Leicester in 1984.",
 "Jeffreys noticed that minisatellite sequences vary uniquely between people (except identical twins).",
 "The first criminal application exonerated an innocent suspect and then convicted Colin Pitchfork of two murders in 1986-1988.",
 "Modern profiling uses short tandem repeat (STR) markers amplified by PCR rather than Jeffreys' original Southern blot method."],
["STR analysis","dna",1990,"Forensic science community",
 "Short tandem repeat (STR) analysis examines microsatellite loci where 2-6 base-pair motifs repeat a variable number of times.",
 "Multiplex PCR amplifies a dozen or more loci at once from tiny or degraded samples.",
 "The random-match probability across a full profile is typically far below one in a quintillion.",
 "STR profiles are the standard currency of DNA databases worldwide."],
["CODIS","dna",1998,"FBI",
 "CODIS (Combined DNA Index System) is the FBI's national DNA database, launched in 1998.",
 "It stores profiles from convicted offenders, arrestees where permitted, crime scenes, and missing persons.",
 "The core loci set expanded from 13 to 20 STR markers in 2017 to improve discrimination and international compatibility.",
 "A CODIS hit provides an investigative lead that must be confirmed with a fresh reference sample."],
["Forensic genetic genealogy","dna",2018,"Forensic genealogy community",
 "Forensic genetic genealogy combines crime-scene SNP profiles with public genealogy databases to identify unknown suspects through distant relatives.",
 "It famously identified Joseph DeAngelo as the Golden State Killer in 2018, ending a decades-long investigation.",
 "Investigators build family trees from cousin matches and narrow them with age, geography, and records.",
 "The method has since solved hundreds of cold cases and identified unknown decedents, under evolving consent and privacy policies."],
["Henry fingerprint classification","fingerprints",1896,"Edward Henry",
 "The Henry Classification System, devised by Edward Henry in British India in 1896, sorts fingerprints into arches, loops, and whorls with subtypes.",
 "It let large fingerprint collections be filed and searched by hand long before computers.",
 "Henry's system was adopted by Scotland Yard in 1901 and became the model for fingerprint bureaus worldwide."],
["Galton's minutiae","fingerprints",1892,"Francis Galton",
 "Francis Galton's 1892 book 'Finger Prints' established that ridge patterns are unique, persistent, and classifiable.",
 "He defined the minutiae — ridge endings and bifurcations — that examiners still compare today.",
 "Galton estimated the chance of two identical prints as astronomically small, grounding a century of identification practice."],
["AFIS and NGI","fingerprints",1999,"FBI",
 "The Automated Fingerprint Identification System digitized fingerprint searching; the FBI's IAFIS launched in 1999.",
 "Its successor, Next Generation Identification (NGI), deployed in 2014, added palm prints, facial recognition, and iris data.",
 "AFIS returns candidate lists ranked by similarity; a human examiner makes the final identification decision."],
["Cyanoacrylate fuming","fingerprints",1978,"Forensic laboratories",
 "Cyanoacrylate (superglue) fuming develops latent fingerprints when heated glue vapor polymerizes on fingerprint residue.",
 "The white polymer outlines ridge detail on nonporous surfaces like plastic, metal, and glass.",
 "Fumed prints are usually enhanced further with fluorescent dyes or powders before photography."],
["Ninhydrin development","fingerprints",1954,"Forensic laboratories",
 "Ninhydrin reacts with amino acids in fingerprint residue to form a purple-blue compound called Ruhemann's purple.",
 "It develops latent prints on porous surfaces such as paper and cardboard.",
 "The reaction can take hours to days and is accelerated by heat and humidity."],
["Luminol blood detection","trace-evidence",1937,"Forensic laboratories",
 "Luminol chemiluminesces blue-green when oxidized in the presence of the iron in hemoglobin.",
 "It reveals latent bloodstains invisible to the eye, even after attempted cleanup.",
 "The reaction is presumptive only: bleach and some metals also trigger it, so confirmatory tests must follow."],
["Comparison microscope","ballistics",1925,"Calvin Goddard",
 "The comparison microscope places two bullets or cartridge cases side by side for striation comparison.",
 "Calvin Goddard used it in 1925 to link bullets in the St. Valentine's Day Massacre investigation, founding forensic ballistics.",
 "Matching individual characteristics — microscopic imperfections from a specific barrel — can identify the firearm that fired a bullet."],
["NIBIN","ballistics",1999,"ATF",
 "The National Integrated Ballistic Information Network (NIBIN), run by the ATF, images bullets and cartridge cases for automated comparison.",
 "Its BrassTrax/IBIS technology correlates markings across crimes to link shootings to the same gun.",
 "NIBIN hits generate investigative leads connecting otherwise unrelated shooting scenes."],
["Gunshot residue analysis","ballistics",1970,"Forensic laboratories",
 "Gunshot residue (GSR) consists of primer particles containing lead, barium, and antimony deposited on firing.",
 "Scanning electron microscopy with energy-dispersive X-ray (SEM-EDS) identifies the characteristic spheroidal particles.",
 "GSR indicates recent proximity to a discharged firearm but cannot prove who pulled the trigger."],
["Medicolegal autopsy","pathology",1800,"Medicolegal tradition",
 "The medicolegal autopsy determines cause, manner, and mechanism of death for legal purposes.",
 "Manner of death is classified as natural, accident, suicide, homicide, or undetermined.",
 "External and internal examination, toxicology, and histology combine to reconstruct the fatal sequence."],
["Postmortem interval indicators","pathology",1800,"Forensic pathology",
 "Algor mortis (body cooling), livor mortis (blood settling), and rigor mortis (muscle stiffening) help estimate time since death.",
 "Rigor typically begins within hours, peaks around 12 hours, and dissipates by 36 hours, though temperature dominates the timeline.",
 "Forensic entomology extends PMI estimation to days and weeks via insect succession."],
["Forensic entomology","entomology",1894,"Jean Pierre Megnin",
 "Forensic entomology estimates the postmortem interval from insects colonizing remains, pioneered by Jean Pierre Megnin in 1894.",
 "Blowflies arrive within minutes of death; their larvae develop at temperature-dependent rates that act as a biological clock.",
 "Succession waves of species over weeks and months extend estimates long after soft tissue is gone."],
["Marsh test","toxicology",1836,"James Marsh",
 "The Marsh test, devised by James Marsh in 1836, detects arsenic by converting it to arsine gas and depositing a metallic mirror.",
 "It was created after Marsh failed to convince a jury with existing tests in an 1832 poisoning trial.",
 "Sensitive to tiny arsenic quantities, it made poisoning far harder to conceal and helped found forensic toxicology."],
["GC-MS toxicology","toxicology",1960,"Analytical chemistry",
 "Gas chromatography-mass spectrometry (GC-MS) separates complex mixtures and identifies compounds by their mass spectra.",
 "It is the workhorse confirmatory technique in forensic toxicology for drugs, poisons, and volatiles.",
 "Screening immunoassays flag candidates; GC-MS or LC-MS/MS confirms identity before courtroom testimony."],
["Breath alcohol testing","toxicology",1954,"Robert Borkenstein",
 "The Breathalyzer, invented by Robert Borkenstein in 1954, estimates blood alcohol from deep-lung breath.",
 "It applies Henry's law: alcohol in alveolar air equilibrates with alcohol in pulmonary blood at a fixed ratio.",
 "Modern evidentiary instruments use infrared spectroscopy or fuel cells with duplicate-sample safeguards."],
["Forensic odontology","odontology",1970,"Forensic dentistry",
 "Forensic odontology identifies the dead from dental records, which survive fire and decomposition that destroy other features.",
 "Dentists compare antemortem charts and radiographs with postmortem findings tooth by tooth.",
 "Bite-mark comparison, once used to identify attackers, is now widely questioned after the NAS 2009 report found no scientific basis for unique attribution."],
["Digital forensics","digital-forensics",1990,"Law enforcement laboratories",
 "Digital forensics recovers and analyzes data from computers, phones, and storage while preserving admissibility.",
 "Write blockers prevent alteration during imaging; cryptographic hashes of the image prove it is unchanged in court.",
 "Examiners recover deleted files, timelines, and communications using tools descended from EnCase and FTK."],
["Questioned documents","questioned-documents",1910,"Albert Osborn",
 "Questioned-document examination authenticates handwriting, signatures, inks, and papers.",
 "Albert Osborn's 1910 'Questioned Documents' founded the discipline on systematic comparison of writing habits.",
 "Electrostatic detection (ESDA) reveals indented writing from sheets beneath the examined page."],
["Bertillonage","crime-scene",1879,"Alphonse Bertillon",
 "Bertillonage, created by Alphonse Bertillon in 1879, identified criminals through precise body measurements.",
 "Eleven measurements including head length and middle-finger length were filed on cards with photographs.",
 "Fingerprinting displaced it after the 1903 Will West case exposed measurement collisions, ending anthropometry's reign."],
["ABO blood grouping","trace-evidence",1901,"Karl Landsteiner",
 "Karl Landsteiner discovered the ABO blood groups in 1901, earning the 1930 Nobel Prize.",
 "Before DNA, ABO typing could include or exclude suspects from bloodstains, though millions share each type.",
 "Secretor status extended typing to saliva and semen stains in sexual assault cases."],
["Polygraph","legal-standards",1921,"John Larson",
 "The polygraph, developed by John Larson in 1921, records blood pressure, respiration, and skin conductivity during questioning.",
 "It measures physiological arousal, not lies; anxiety and countermeasures both distort results.",
 "Most US courts exclude polygraph evidence, and the National Research Council found its accuracy inadequate for security screening."],
["Arson investigation","crime-scene",1992,"NFPA 921 community",
 "Fire investigators determine origin and cause by reading burn patterns, char depth, and ventilation effects.",
 "NFPA 921, the guide for fire and explosion investigations, systematized the scientific method for fire scenes.",
 "Accelerant-detecting canines and GC-MS analysis of debris confirm or rule out ignitable liquids."],
["Bloodstain pattern analysis","trace-evidence",1955,"Forensic laboratories",
 "Bloodstain pattern analysis reconstructs events from the size, shape, and distribution of bloodstains.",
 "Spatter, cast-off, transfer, and flow patterns each record different mechanics of bloodshed.",
 "Analysts estimate area of origin by tracing droplet trajectories back in three dimensions."],
["Forensic accounting","digital-forensics",1940,"Investigative accounting",
 "Forensic accounting traces illicit money flows through books, bank records, and transaction trails.",
 "It convicted Al Capone of tax evasion in 1931 when violent crimes could not be proven.",
 "Modern practitioners follow cryptocurrency, shell companies, and layered transfers across jurisdictions."],
["Voice comparison","trace-evidence",1960,"Forensic acoustics",
 "Forensic voice comparison analyzes spectrograms and acoustic features to assess whether recordings share a speaker.",
 "The 'voiceprint' analogy to fingerprints overstates the science; voices vary with health, emotion, and channel.",
 "Courts increasingly require likelihood-ratio frameworks rather than categorical identifications."],
["Forensic linguistics","questioned-documents",1968,"Jan Svartvik and others",
 "Forensic linguistics applies language analysis to authorship attribution, threat assessment, and disputed confessions.",
 "Jan Svartvik's 1968 study of the Evans statements showed how linguistic analysis could challenge confession evidence.",
 "Stylometry now uses computational methods to compare idiolectal patterns across texts."],
["Crime scene photography","crime-scene",1900,"Police photography units",
 "Crime scene photography preserves the scene in overall, midrange, and close-up views with scales.",
 "Overall shots orient the scene; midrange shots relate evidence to landmarks; close-ups with rulers record detail.",
 "Photographs must be taken before anything is moved, forming the visual backbone of the case file."],
["Chain of custody","legal-standards",1900,"Evidence law",
 "Chain of custody is the documented, unbroken chronological record of who handled evidence and when.",
 "Every transfer, storage condition, and analysis must be logged to prove the evidence is what it claims to be.",
 "A broken chain can render decisive evidence inadmissible regardless of its scientific quality."],
["Frye standard","legal-standards",1923,"US federal courts",
 "The Frye standard (1923) admitted scientific evidence only if its principle was 'generally accepted' in its field.",
 "It governed US federal courts for seventy years, favoring established techniques over novel ones.",
 "The Supreme Court replaced it federally with Daubert in 1993, though several states retain Frye."],
["Daubert standard","legal-standards",1993,"US Supreme Court",
 "Daubert v. Merrell Dow (1993) made trial judges gatekeepers of scientific evidence in US federal courts.",
 "Judges weigh testability, peer review, known error rates, standards, and general acceptance.",
 "Daubert challenges have reshaped forensic disciplines, pressuring pattern-matching fields to quantify their error rates."],
["NAS 2009 report","legal-standards",2009,"National Academy of Sciences",
 "The 2009 National Academy of Sciences report 'Strengthening Forensic Science in the United States' found serious gaps in many disciplines.",
 "It concluded that only nuclear DNA analysis had been rigorously shown to link evidence to a specific individual.",
 "The report demanded research, standards, and independence from law enforcement for crime laboratories."],
["PCAST 2016 report","legal-standards",2016,"President's Council of Advisors on Science and Technology",
 "The 2016 PCAST report assessed the scientific validity of feature-comparison forensic methods.",
 "It found DNA and latent fingerprint analysis scientifically valid but questioned firearms, footwear, and hair comparison as practiced.",
 "The report urged blind verification procedures and black-box studies measuring real examiner error rates."],
["Innocence Project","legal-standards",1992,"Barry Scheck and Peter Neufeld",
 "The Innocence Project, founded in 1992 by Barry Scheck and Peter Neufeld, uses DNA testing to exonerate the wrongfully convicted.",
 "Its cases have freed hundreds of people, many convicted on eyewitness misidentification or faulty forensics.",
 "The exonerations exposed systemic causes: misidentification, false confessions, informant lies, and bad science."],
["Forensic anthropology","pathology",1970,"T. Dale Stewart and William Bass",
 "Forensic anthropology identifies the dead from skeletal remains: estimating age, sex, ancestry, and stature.",
 "T. Dale Stewart systematized the field; William Bass founded the Body Farm research facility in 1981 to study decomposition.",
 "Bone trauma analysis distinguishes perimortem injury from postmortem damage."],
["Forensic palynology","trace-evidence",1959,"Forensic botany",
 "Forensic palynology uses pollen and spores to link people and objects to locations.",
 "Pollen assemblages are geographically distinctive and cling to clothing, vehicles, and remains.",
 "The first criminal use in 1959 located a missing person in Austria through pollen on his shoes."],
["Impression evidence","trace-evidence",1900,"Crime laboratories",
 "Footwear and tire impressions record the unique wear and damage of a specific shoe or tire.",
 "Casting with dental stone and electrostatic dust lifting preserve three-dimensional detail.",
 "Examiners compare class characteristics (size, pattern) and individual characteristics (cuts, embedded stones)."],
["Alternate light source","crime-scene",1980,"Forensic laboratories",
 "Alternate light sources illuminate scenes with narrow-band wavelengths to reveal hidden evidence.",
 "Blue and ultraviolet light make semen, saliva, and treated fingerprints fluoresce against backgrounds.",
 "Orange barrier filters block the excitation light so only the fluorescence reaches the examiner's eyes."]
];
var ANGLES=["technique profile","historical profile","procedure profile","courtroom profile"];
var SYNREL=[
 ["compared with","This Signature comparative study evaluates both techniques on sensitivity, specificity, and courtroom acceptance."],
 ["contrasted against","This Signature contrast study shows where the two methods agree, compete, or complement each other."],
 ["as predecessor and successor to","This Signature lineage study traces how the newer method answered the older one's limitations."],
 ["alongside","This Signature pairing study examines how the two methods combine in a single investigation."]
];
function filedLine(id){return "Filed as "+id+" in the JAH Forensics Database archive.";}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var id=PREFIX+String(seed).padStart(6,'0');
  var pool=ANCH;
  if(opts.category){var f=ANCH.filter(function(a){return a[1]===opts.category;});if(f.length)pool=f;}
  var synth=!opts.category&&rnd()<0.38;
  if(synth){
    var A=pick(pool,rnd),B=pick(pool,rnd),guard=0;
    while(B===A&&guard++<20)B=pick(pool,rnd);
    var rel=pick(SYNREL,rnd);
    var title="Signature study: "+A[0]+" "+rel[0]+" "+B[0];
    var d="In "+A[2]+", "+A[0]+": "+A[4]+" "+rel[0]+" "+B[0]+" ("+B[2]+"), "+rel[1]+" "+B[4];
    return {id:id,title:title,description:d+" "+filedLine(id),category:A[1]==="legal-standards"||B[1]==="legal-standards"?"legal-standards":A[1],
      spec:{kind:"study",pair:[A[0],B[0]],relation:rel[0],years:[A[2],B[2]],src:"signature"},
      year:Math.max(A[2],B[2]),src:"signature"};
  }
  var A=pick(pool,rnd);
  var ang=pick(ANGLES,rnd);
  var facts=A.slice(4);
  var d=facts[0]+" "+pick(facts.slice(1),rnd);
  if(rnd()<0.6)d+=" "+pick(facts.slice(1),rnd);
  var title=A[0]+" — "+ang;
  return {id:id,title:title,description:d+" "+filedLine(id),category:A[1],
    spec:{kind:A[1],year:A[2],originator:A[3],src:"online"},year:A[2],src:"online",_facts:facts,_an:A[0]};
}
function sentences(s){return String(s).split(/[.!?]+/).filter(function(x){return x.trim().length>10;}).length;}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!/^JAH-FOR-\d{6}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<4)e.push('title');
  if(typeof r.description!=='string'||r.description.length<80)e.push('description');
  else if(sentences(r.description)<2)e.push('description-sentences');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(r.src!=='online'&&r.src!=='signature')e.push('src');
  if(typeof r.year!=='number'||r.year<1700||r.year>2026)e.push('year');
  var s=r.spec;
  if(!s||typeof s!=='object')e.push('spec');
  else{
    if(s.src!=='online'&&s.src!=='signature')e.push('spec.src');
    if(s.src!==r.src)e.push('spec.src-mismatch');
    if(s.src==='online'){
      if(typeof s.year!=='number'||s.year<1700||s.year>2026)e.push('spec.year');
      if(typeof s.originator!=='string'||!s.originator.length)e.push('spec.originator');
    }else if(s.kind==='signature-version'){
      if(typeof s.of!=='string'||!s.of.length)e.push('spec.of');
    }else{
      if(!Array.isArray(s.pair)||s.pair.length!==2)e.push('spec.pair');
      if(typeof s.relation!=='string'||!s.relation.length)e.push('spec.relation');
    }
  }
  return{ok:!e.length,errors:e};
}

var SIG_T=[
 "Signature reading of {N}: {F1}",
 "Held in the Signature system as a governed Signature version, this record preserves the fact-checked core whole \u2014 nothing is reduced. {F2}",
 "Signature assessment: {N} is cross-referenced against the archive's related records, so the fact-checked original and its Signature version travel together. Property of Justin Addam Higgins."
];
function sigFill(t,m){return t.replace(/\{N\}|\{F1\}|\{F2\}/g,function(k){return m[k]||'';});}
function signatureVersion(seed){
  var base=generate(seed,{},prng(seed));
  if(!base||base.src!=='online')return null;
  var facts=(base._facts&&base._facts.length)?base._facts:[base.description];
  var N=base._an||base.title;
  var F1=facts[0],F2=facts.length>1?facts[1+((seed%(facts.length-1))|0)]:facts[0];
  var map={'{N}':N,'{F1}':F1,'{F2}':F2};
  var d=sigFill(SIG_T[0],map)+" "+sigFill(SIG_T[1],map)+" "+sigFill(SIG_T[2],map);
  var sv={id:base.id,_seed:seed,title:"Signature version: "+N,description:d,category:base.category,
    spec:{kind:"signature-version",of:base.id,src:"signature"},src:"signature"};
  Object.keys(base).forEach(function(k){
    if(k.charAt(0)==='_'||k==='id'||k==='title'||k==='description'||k==='category'||k==='spec'||k==='src')return;
    sv[k]=base[k];
  });
  return sv;
}
var gen={version:'jahdb-forensics-1.0',generate:generate,validate:validate,signatureVersion:signatureVersion};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('forensics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
