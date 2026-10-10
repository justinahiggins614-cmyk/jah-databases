(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['trials','evidence','methods','findings','reviews'];
var PREFIX='JAH-MED-';
var DESIGNS=[['randomized controlled trial','participants are randomly assigned to intervention or control arms'],['cohort study','a defined group is followed over time to compare outcomes'],['case-control study','cases with an outcome are compared with controls without it'],['cross-sectional study','exposure and outcome are measured at one time point'],['crossover trial','each participant receives each intervention in sequence'],['non-inferiority trial','tests that a new intervention is not worse than standard by a margin']];
var POPS=[['adults with a chronic condition','primary-care clinics'],['older adults in community settings','community centers'],['hospital inpatients','tertiary hospitals'],['healthy volunteers','research units'],['children in school settings','schools']];
var OUTC=['a symptom score','a functional measure','a laboratory marker','a quality-of-life scale','an event rate'];
var EVL=[['Level 1','systematic reviews of randomized trials'],['Level 2','individual randomized trials'],['Level 3','cohort and case-control studies'],['Level 4','case series and expert opinion']];
var METH=[['randomization','balances known and unknown confounders across arms'],['blinding','reduces bias in outcome assessment'],['intention-to-treat analysis','preserves the benefit of randomization'],['sample-size calculation','ensures adequate power for the primary outcome'],['allocation concealment','prevents selection bias at enrollment']];
var REV=[['systematic review','identifies, appraises, and synthesizes all eligible studies'],['meta-analysis','pools quantitative results across studies'],['scoping review','maps the breadth of evidence on a topic'],['narrative review','expert synthesis without a formal protocol']];
var DISC='Educational template with illustrative example values; not a real study. Never presented as real trial outcomes.';
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var id=PREFIX+String(seed).padStart(7,'0');
  var rec={id:id,category:cat,source:'signature',source_ref:'JAH Signature Generator',creation_mode:'SIGNATURE-GENERATED',_seed:seed};
  if(cat==='trials'){
    var d=pick(DESIGNS,rnd),p=pick(POPS,rnd),o=pick(OUTC,rnd),n=ri(rnd,1,90);
    rec.title='Signature trial template '+n+': '+d[0];
    rec.description='A teaching template for a '+d[0]+' ('+d[1]+'). Population: '+p[0]+' recruited from '+p[1]+'. Primary outcome: '+o+'. '+DISC;
    rec.study_design=d[0];rec.design_definition=d[1];rec.population=p[0];rec.setting=p[1];
    rec.methods_summary='Define eligibility, randomize or allocate per design, measure '+o+' with a validated instrument, and analyze by a pre-specified plan.';
    rec.findings_summary='Illustrative example values only, generated for teaching; no real outcomes are reported.';
    rec.illustrative_example=true;rec.disclaimer=DISC;
  }else if(cat==='evidence'){
    var ev=pick(EVL,rnd);
    rec.title='Evidence level study: '+ev[0];
    rec.description='A teaching record for '+ev[0]+' in an evidence hierarchy: '+ev[1]+'. Explains what designs sit at this level and how to appraise them.';
    rec.evidence_level=ev[0];rec.includes=ev[1];
    rec.appraisal_notes='Check design fit, bias risk, precision, and applicability before acting on any result.';
  }else if(cat==='methods'){
    var m=pick(METH,rnd);
    rec.title='Research method: '+m[0];
    rec.description='A teaching record for the method "'+m[0]+'": '+m[1]+'. Covers purpose, basic steps, and common pitfalls in general terms.';
    rec.method=m[0];rec.purpose=m[1];
    rec.steps=['State the research question','Apply the method per protocol','Report what was done transparently'];
  }else if(cat==='findings'){
    var f1=ri(rnd,5,40),f2=ri(rnd,1,20);
    rec.title='Signature findings template '+ri(rnd,1,90);
    rec.description='A teaching template showing how findings are structured: illustrative counts ('+f1+' events in group A, '+f2+' in group B) with a plain-language reading. '+DISC;
    rec.findings_summary='Illustrative example: '+f1+' vs '+f2+' events. Example numbers for teaching only; no real outcomes.';
    rec.reading_guide='Report absolute counts first, then relative comparisons, then uncertainty.';
    rec.illustrative_example=true;rec.disclaimer=DISC;
  }else{
    var rv=pick(REV,rnd);
    rec.title='Review template: '+rv[0];
    rec.description='A teaching template for a '+rv[0]+' ('+rv[1]+'). Covers protocol registration, search, selection, appraisal, and synthesis steps.';
    rec.review_type=rv[0];rec.definition=rv[1];
    rec.steps=['Register a protocol','Search systematically','Select and appraise studies','Synthesize transparently'];
  }
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-MED-\d{7}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(r.illustrative_example===true){
    if(typeof r.disclaimer!=='string'||!/not a real study/i.test(r.disclaimer))e.push('disclaimer');
    if(typeof r.findings_summary!=='string'||!/illustrative/i.test(r.findings_summary))e.push('findings_summary');
  }
  if(r.category==='trials'&&typeof r.study_design!=='string')e.push('study_design');
  if(r.category==='evidence'&&typeof r.evidence_level!=='string')e.push('evidence_level');
  if(r.category==='methods'&&typeof r.method!=='string')e.push('method');
  if(r.category==='reviews'&&typeof r.review_type!=='string')e.push('review_type');
  if(r.source!=='signature'&&r.source!=='online')e.push('source');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-medical-research-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('medical-research',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
