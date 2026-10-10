(function(){'use strict';
/* JAH Research Discovery Database generator — deterministic, every record validated.
   Signature records are ILLUSTRATIVE HYPOTHETICAL MODELS for teaching —
   never presented as real discoveries. Compact JSON. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['findings','hypotheses','methods','measurements','references'];
var PREFIX='JAH-RD-';
var FIELDS=['physics','chemistry','biology','medicine','astronomy','geology','computer-science','psychology'];
var NOTICE='ILLUSTRATIVE HYPOTHETICAL MODEL — a teaching illustration, not a real scientific discovery.';
var TOPICS=[
 ['Resonant algae blooms','biology','light cycles shifting algal pigment ratios'],
 ['Granular flow sorting','physics','vibration separating mixed grains by size'],
 ['Mycorrhizal message timing','biology','fungi relaying stress signals between seedlings'],
 ['Urban heat pockets','geology','city blocks trapping warmth overnight'],
 ['Checklist item order','psychology','item order changing error rates'],
 ['Aerosol settling','chemistry','droplet size setting fall time'],
 ['Tide-pool temperature swings','geology','shallow pools buffering heat'],
 ['Sleep spindle density','psychology','nap length shifting memory scores'],
 ['Fermentation gas curves','chemistry','sugar level shaping CO2 release'],
 ['Corvid tool preferences','biology','crow groups choosing stick lengths'],
 ['River pebble rounding','geology','distance downstream smoothing stones'],
 ['Screen flicker perception','psychology','refresh rate shifting reported strain'],
 ['Soil moisture memory','geology','clay recording wet spells'],
 ['Protein folding chaperones','biology','helper molecules cutting misfold time'],
 ['Exoplanet transit dips','astronomy','light curves revealing planet size'],
 ['Meteor shower rates','astronomy','radiant position predicting counts'],
 ['Dosage timing windows','medicine','dose hour shifting absorption'],
 ['Wound dressing airflow','medicine','ventilation changing healing time'],
 ['Cache eviction patterns','computer-science','access order shaping hit rates'],
 ['Sorting network depth','computer-science','comparator count scaling with input size'],
 ['Crystal growth seeding','chemistry','seed size setting final crystal mass'],
 ['Birdsong dialect drift','biology','isolated flocks shifting call pitch'],
 ['Glacier melt channels','geology','slope steering summer rivulets'],
 ['Reaction time under noise','psychology','background sound slowing responses'],
 ['Vaccine cold-chain breaks','medicine','temperature excursions cutting potency']
];
var DESIGNS=['randomized controlled trial','longitudinal cohort study','double-blind experiment','field observation survey','laboratory bench study','computational simulation','meta-analysis','cross-sectional survey'];
var UNITS=['mg','ml','mm','cm','s','min','Hz','kPa','lux','dB','ppm','percent'];
function fmt(n){return Math.round(n*100)/100;}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var tp=pick(TOPICS,rnd),topic=tp[0],field=tp[1],about=tp[2];
  var id=PREFIX+String(seed).padStart(7,'0');
  var design=pick(DESIGNS,rnd);
  var steps=['Record baselines for '+about+'.','Apply the intervention per the '+design+' protocol.','Collect readings across '+ri(rnd,2,6)+' sessions and log confounds.'];
  var nM=2,meas=[],i;
  for(i=0;i<nM;i++){
    var val=fmt(rnd()*100+1),unc=fmt(val*(0.01+rnd()*0.09));
    meas.push({quantity:pick(['peak response','mean shift','settling time','yield rate'],rnd)+' '+(i+1),value:val,unit:pick(UNITS,rnd),uncertainty:unc});
  }
  var refs=[];
  for(i=0;i<2;i++)refs.push({title:'Illustrative prior work: '+topic.toLowerCase()+' ('+(i+1)+')',authors:pick(['A. Rivera','J. Okafor','M. Lindqvist','S. Patel','K. Novak'],rnd)+' et al.',year:ri(rnd,1995,2025)});
  return {
    id:id,record_id:id,
    title:'Illustrative: '+topic+' — hypothetical '+cat.slice(0,-1)+' study',
    category:cat,field:field,
    summary:'A hypothetical '+design+' exploring '+about+' — a teaching illustration of how '+field+' research is structured.',
    hypothesis:{statement:'Varying the driver behind '+about+' shifts the measured outcome predictably.',iv:'driver level',dv:'outcome for '+topic.toLowerCase(),falsifiable:true},
    method:{design:design,steps:steps,controls:pick([['matched control group'],['blinded measurement','randomized order']],rnd)},
    measurements:meas,
    key_finding:'Under the model assumptions the outcome tracks the driver repeatably.',
    references:refs,confidence:fmt(0.4+rnd()*0.5),
    is_real:false,notice:NOTICE,
    source:'signature',creation_mode:'SIGNATURE-GENERATED',_seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-RD-\d{7}$/.test(r.id||''))e.push('id');
  if(r.record_id!==r.id)e.push('record_id');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.summary!=='string'||r.summary.length<40)e.push('summary');
  if(r.source!=='online'&&r.source!=='signature')e.push('source');
  if(r.source==='signature'){
    if(r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
    if(r.is_real!==false)e.push('is_real');
    if(typeof r.notice!=='string'||r.notice.indexOf('not a real scientific discovery')<0)e.push('notice');
    if(r.title.indexOf('Illustrative:')!==0)e.push('title-prefix');
    var h=r.hypothesis;
    if(!h||typeof h.statement!=='string'||!h.statement.length)e.push('hypothesis-statement');
    else if(typeof h.falsifiable!=='boolean')e.push('hypothesis-falsifiable');
    if(!h||typeof h.iv!=='string'||!h.iv.length)e.push('hypothesis-iv');
    if(!h||typeof h.dv!=='string'||!h.dv.length)e.push('hypothesis-dv');
    var m=r.method;
    if(!m||typeof m.design!=='string'||!m.design.length)e.push('method-design');
    else if(!Array.isArray(m.steps)||m.steps.length<3)e.push('method-steps');
    if(!Array.isArray(r.measurements)||r.measurements.length<2)e.push('measurements');
    else r.measurements.forEach(function(x){
      if(typeof x.value!=='number'||typeof x.uncertainty!=='number')e.push('measurement-numbers');
      else if(x.uncertainty<0||x.uncertainty>Math.abs(x.value))e.push('measurement-uncertainty-range');
      if(typeof x.unit!=='string'||!x.unit.length)e.push('measurement-unit');
      if(typeof x.quantity!=='string'||!x.quantity.length)e.push('measurement-quantity');
    });
    if(!Array.isArray(r.references)||r.references.length<2)e.push('references');
    else r.references.forEach(function(x){
      if(typeof x.title!=='string'||!x.title.length)e.push('ref-title');
      if(typeof x.year!=='number'||x.year<1800||x.year>2026)e.push('ref-year');
    });
    if(typeof r.confidence!=='number'||r.confidence<0||r.confidence>1)e.push('confidence');
    if(typeof r.key_finding!=='string'||!r.key_finding.length)e.push('key_finding');
  }else{
    if(r.is_real!==true)e.push('is_real');
    if(typeof r.source_ref!=='string'||!/^https?:\/\//.test(r.source_ref))e.push('source_ref');
    if(typeof r.discovery!=='string'||!r.discovery.length)e.push('discovery');
    if(typeof r.year!=='number'||r.year<1500||r.year>2026)e.push('year');
    if(typeof r.discoverers!=='string'||!r.discoverers.length)e.push('discoverers');
    if(typeof r.significance!=='string'||r.significance.length<20)e.push('significance');
  }
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-research-discovery-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('research-discovery',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
