(function(){'use strict';
/* JAH The Scientific Datasets Signature Database generator — jahdb-scientific-datasets-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SCIDS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What a Scientific Dataset Is: Observations, Not Conclusions (Signature Edition) \u2014 Foundations",
  "Measurement Basics: Variables, Units, and Instruments (Signature Edition) \u2014 Foundations",
  "Experimental Conditions: Recording the Context of Every Reading (Signature Edition) \u2014 Foundations",
  "Sampling: How Often, How Many, How Representative (Signature Edition) \u2014 Foundations",
  "Data Formats: CSV, NetCDF, HDF5, and Plain Text (Signature Edition) \u2014 Foundations",
  "Metadata: Describing Data So Others Can Use It (Signature Edition) \u2014 Foundations",
  "The Lab Notebook: The Original Processing History (Signature Edition) \u2014 Foundations",
  "Calibration Records: Tying Measurements to Standards (Signature Edition) \u2014 Foundations",
  "Uncertainty and Error Bars: Honest Measurements (Signature Edition) \u2014 Foundations",
  "Time Series: Ordering Observations in Time (Signature Edition) \u2014 Foundations",
  "Replication: Repeating Measurements, Recording Repeats (Signature Edition) \u2014 Foundations",
  "Data Cleaning: Documenting What Was Removed and Why (Signature Edition) \u2014 Foundations"
 ],
 "Compounded": [
  "Controlled Experiments: Treatment, Control, Randomization (Signature Edition) \u2014 Compounded",
  "Field Observations: Messy Real-World Data Collection (Signature Edition) \u2014 Compounded",
  "Sensor Networks: Streaming Observations at Scale (Signature Edition) \u2014 Compounded",
  "Survey Data: Questions, Respondents, Response Rates (Signature Edition) \u2014 Compounded",
  "Imaging Datasets: Pixels as Measurements (Signature Edition) \u2014 Compounded",
  "Spectral Data: Wavelength-Resolved Observations (Signature Edition) \u2014 Compounded",
  "Genomic Sequence Reads: Base Calls and Quality Scores (Signature Edition) \u2014 Compounded",
  "Climate Station Records: Long Baselines, Homogenization (Signature Edition) \u2014 Compounded",
  "Astronomical Catalogs: Positions, Magnitudes, Redshifts (Signature Edition) \u2014 Compounded",
  "Particle Detector Event Data: Triggers and Reconstructions (Signature Edition) \u2014 Compounded",
  "Processing Pipelines: From Raw to Analysis-Ready (Signature Edition) \u2014 Compounded",
  "Versioning Datasets: DOIs and Immutable Snapshots (Signature Edition) \u2014 Compounded"
 ],
 "Advanced": [
  "Provenance Graphs: Every Transformation Traced (Signature Edition) \u2014 Advanced",
  "FAIR Data: Findable, Accessible, Interoperable, Reusable (Signature Edition) \u2014 Advanced",
  "Statistical Power and Design of Experiments (Signature Edition) \u2014 Advanced",
  "Missing Data: Mechanisms and Principled Handling (Signature Edition) \u2014 Advanced",
  "Data Fusion: Combining Heterogeneous Observations (Signature Edition) \u2014 Advanced",
  "Uncertainty Propagation Through Pipelines (Signature Edition) \u2014 Advanced",
  "Reproducibility Audits: Re-running the Analysis (Signature Edition) \u2014 Advanced",
  "Long-Term Archiving: Bit Preservation of Datasets (Signature Edition) \u2014 Advanced",
  "Synthetic and Simulated Datasets: Labeled as Such (Signature Edition) \u2014 Advanced",
  "Dataset Publication: Data Papers and Citations (Signature Edition) \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Scientific Dataset — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — scientific dataset record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A scientific dataset record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"scientific-dataset-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-scientific-datasets-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('scientific-datasets-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
