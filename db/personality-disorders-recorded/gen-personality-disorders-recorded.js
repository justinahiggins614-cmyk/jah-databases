(function(){'use strict';
/* Personality Disorders Recorded Database generator — jahdb-personality-disorders-recorded-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. The generator recombines
   archive-derived topic material into new deep-dive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return s[(r()*s.length)|0];}
var PREFIX="JAH-PER-";
var SLUG="personality-disorders-recorded";
var FIELDS=["borderline", "narcissistic", "antisocial", "avoidant", "dependent", "ocpd", "schizotypal", "cluster-notes"];
var GEN_SRC="public-record";
var DATA={"borderline": [{"stem": "Borderline Personality Disorder (Documented)", "core": "Public documented information: Borderline Personality Disorder is classified in DSM-5-TR among personality disorders (Cluster B), documented around pervasive instability in relationships, self-image, and affect with impulsivity per documented criteria \u2014 summarized generally. ICD-11 takes a dimensional approach to personality disorder. Documented note: this diagnosis has carried heavy stigma; the documented clinical literature increasingly emphasizes treatability and the person beyond the label. Anyone affected deserves qualified professional care \u2014 never stigma.", "points": ["built to archive standard"]}, {"stem": "Treatability: The Documented Record", "core": "Public documented information: the documented literature increasingly emphasizes that personality disorders are treatable \u2014 specialized psychotherapies show documented effectiveness for several presentations (notably BPD). Stated generally as documented hope: the old \"untreatable\" narrative is documented as outdated.", "points": ["built to archive standard"]}], "narcissistic": [{"stem": "Narcissistic Personality Disorder (Documented)", "core": "Public documented information: Narcissistic Personality Disorder is classified in DSM-5-TR among personality disorders (Cluster B), documented around grandiosity, need for admiration, and empathy difficulties per documented criteria \u2014 summarized generally. A heavily memed label in popular culture; the documented clinical reality is more nuanced and deserves professional understanding, not internet diagnosis.", "points": ["built to archive standard"]}, {"stem": "The Label-Misuse Problem (Documented)", "core": "Public documented information: popular misuse of personality-disorder terms as insults \u2014 armchair diagnosis of public figures, ex-partners, colleagues \u2014 is documented as harmful by clinicians and advocates. The documented standard: these are clinical terms for professional use, not internet vocabulary. Stated firmly.", "points": ["built to archive standard"]}], "antisocial": [{"stem": "Antisocial Personality Disorder (Documented)", "core": "Public documented information: Antisocial Personality Disorder is classified in DSM-5-TR among personality disorders (Cluster B), documented around disregard for others\u2019 rights per documented criteria \u2014 summarized generally. The documented literature is nuanced; popular \"psychopath\" discourse is not the clinical reality. Professional territory; stated without sensationalism.", "points": ["built to archive standard"]}], "avoidant": [{"stem": "Avoidant Personality Disorder (Documented)", "core": "Public documented information: Avoidant Personality Disorder is classified in DSM-5-TR among personality disorders (Cluster C), documented around social inhibition and hypersensitivity to negative evaluation per documented criteria \u2014 summarized generally. Professional territory; stated with care.", "points": ["built to archive standard"]}], "dependent": [{"stem": "Dependent Personality Disorder (Documented)", "core": "Public documented information: Dependent Personality Disorder is classified in DSM-5-TR among personality disorders (Cluster C), documented around excessive need to be taken care of per documented criteria \u2014 summarized generally. Professional territory; stated with care.", "points": ["built to archive standard"]}], "ocpd": [{"stem": "Obsessive-Compulsive Personality Disorder (Documented)", "core": "Public documented information: Obsessive-Compulsive Personality Disorder is classified in DSM-5-TR among personality disorders (Cluster C), documented around preoccupation with orderliness and control per documented criteria \u2014 distinct from OCD, per the documented distinction. Professional territory.", "points": ["built to archive standard"]}], "schizotypal": [{"stem": "Schizotypal Personality Disorder (Documented)", "core": "Public documented information: Schizotypal Personality Disorder is classified in DSM-5-TR among personality disorders (Cluster A), documented around social/interpersonal deficits with cognitive-perceptual distortions per documented criteria \u2014 summarized generally with care. Professional territory.", "points": ["built to archive standard"]}], "cluster-notes": [{"stem": "The Cluster System (Documented Concept)", "core": "Public documented information: DSM-5-TR groups personality disorders into Clusters A (odd/eccentric), B (dramatic/emotional), C (anxious/fearful) \u2014 a documented organizing scheme with acknowledged limitations; ICD-11 moved dimensional. Stated generally as classification history.", "points": ["built to archive standard"]}, {"stem": "Personality Disorders: History", "core": "Documented history: from characterology and psychoanalytic character types through DSM-II\u2019s early categories, DSM-III\u2019s clusters (1980), to the dimensional turn (DSM-5 Section III alternative model; ICD-11). The documented arc: from types to traits to dimensions \u2014 still evolving.", "points": ["built to archive standard"]}, {"stem": "Stigma and Personality Labels (Documented)", "core": "Documented: personality-disorder labels are documented as carrying significant stigma \u2014 including within healthcare settings, per documented research \u2014 and popular misuse (especially Cluster B terms as insults) is documented harm. The record states this plainly: labels are clinical tools, not slurs; these databases\u2019 dignity rules exist for documented realities like this.", "points": ["built to archive standard"]}, {"stem": "Personality Disorders: Signature Overview", "core": "His Signature overview (conceptual framework \u2014 not medical fact): of the documented families, this one his frameworks approach most briefly \u2014 \"the documented here is deeply clinical; my dynamics stay in systems.\" His overview\u2019s contribution: the DIGNITY work \u2014 opposing label-misuse structurally, modeling feedback dynamics for teams and systems only. Kindness as method.", "points": ["built to archive standard"]}, {"stem": "Resources (Documented)", "core": "Public information: qualified professional care; crisis resources \u2014 US: call/text 988. Documented organizations: NIMH, WHO. Resource record; not guidance.", "points": ["built to archive standard"]}, {"stem": "Paranoid Personality Disorder (Documented)", "core": "Public documented information: Paranoid Personality Disorder is classified in DSM-5-TR among personality disorders (Cluster A), documented around pervasive distrust per documented criteria \u2014 summarized generally with care. Professional territory.", "points": ["built to archive standard"]}]};
var ANGLES=[
 ["Buyer's Deep Dive","When choosing one, work through this checklist in order: define the job first, then match the specification to the job, then compare build quality hands-on, then verify support and parts availability. The cheapest option that meets the real requirement usually beats the most expensive option that exceeds it. Buy once where the tool earns its keep daily; buy value where it is used occasionally."],
 ["Specification Breakdown","The specification sheet tells the real story. Read rated capacity, duty cycle, materials, tolerances, and warranty terms before the marketing copy. Compare like for like across brands: a specification measured under different test conditions is not comparable. Keep a short list of the three specifications that matter most for your use and ignore the rest."],
 ["Setup & Use Guide","Set up in a clean, well-lit space and read the manual cover to cover once. Do a first run at low intensity and check every adjustment point. Keep a simple log of settings that worked so the next session starts in seconds. Clean and inspect after each use; most failures announce themselves early to anyone who looks."],
 ["Maintenance & Longevity","Maintenance is what separates a ten-year tool from a two-year tool. Follow the maker's service intervals, keep moving parts clean and lubricated, store it dry and out of direct sun, and replace wear parts before they fail. A fifteen-minute routine after each use prevents most breakdowns."],
 ["History & Evolution","Every mature product category carries decades of lessons. Early versions solved the basic problem; later versions refined safety, ergonomics, and efficiency. Knowing what changed and why helps you judge whether the newest feature is a real improvement or marketing. Classics endure because their fundamentals were right."],
 ["Comparison Study","No single option wins every category, so compare on the criteria that matter to you: performance, durability, ease of use, support, and total cost over five years. Weight the criteria before you look at products to avoid being swayed by one flashy strength. The right choice is the one that fits your actual work."],
 ["Safety & Best Practice","Read every warning label and follow it; the rules exist because someone learned the hard way. Use the correct protective equipment every time, keep the work area clear, and never defeat a guard or interlock. If something feels wrong, stop and investigate before continuing."],
 ["Pro Tips & Workflow","Professionals get more from the same equipment by systematizing the workflow: standardize the setup, batch similar jobs, keep consumables stocked, and maintain a checklist for repeat tasks. Small process improvements compound into large time savings over a year."]
];
function words(s,n){var w=String(s||'').split(/\s+/);return w.slice(0,n).join(' ');}
function generate(seed,opts,rnd){
  opts=opts||{};
  var cats=Object.keys(DATA);
  var cat=(opts.category&&DATA[opts.category])?opts.category:pick(rnd,cats);
  var pool=DATA[cat];
  var t=pool[(rnd()*pool.length)|0];
  var ang=ANGLES[(rnd()*ANGLES.length)|0];
  var n=100000+((seed%900000+900000)%900000);
  var title=t.stem+' \u2014 '+ang[0];
  var desc=t.core+' '+ang[1]+' Key points: '+t.points.join('; ')+'.';
  while(desc.length<600){desc+=' '+ang[1];}
  var rec={
    id:PREFIX+String(n),
    title:title,
    t:title,
    g:cat,
    c:1,
    description:desc,
    key_points:t.points.slice(),
    angle:ang[0],
    src:GEN_SRC,
    ladder:1+(Math.abs(seed)%3),
    _seed:seed
  };
  rec.disclaimer="Signature-concept framework notice: this record presents Justin Addam Higgins's personal conceptual and philosophical framework. It is NOT medical fact, NOT medical advice, NOT a diagnosis, and NOT a treatment claim. Nothing here is presented as a cure for any condition. If you or someone you know is dealing with mental illness, please consult qualified medical or mental-health professionals, and in a crisis contact local emergency services (US: call or text 988).";
  return rec;
}
function validate(r){
  var e=[];
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.g)<0)e.push('group');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<200)e.push('description');
  if(!Array.isArray(r.key_points)||!r.key_points.length)e.push('key_points');
  if(['public-record','reference-authored','signature-line','signature-generated','signature-concept'].indexOf(r.src)<0)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var seen={};(sample||[]).forEach(function(s){if(s&&s.t)seen[s.t]=1;});
  if(rec&&seen[rec.title])return {ok:false,errors:['duplicate title in archive sample']};
  return {ok:true,errors:[]};
}
var gen={version:'jahdb-personality-disorders-recorded-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
