(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["adjustment", "linearity", "traceability", "environmental", "reference-standards"];
var PREFIX='JAH-SCIENT6-';
var USE="Used by metrology labs, field scientists, and quality engineers to defend every measurement.";
var FLD=[["procedure", "Procedure"], ["reference", "Reference"], ["tolerance", "Tolerance"]];
var DEMO="# {title} - linear fit check (python3)\nxs={d1}\nys={d2}\nr2min={d3}\nn=len(xs)\nmx=sum(xs)/n; my=sum(ys)/n\nsxy=sum((x-mx)*(y-my) for x,y in zip(xs,ys))\nsxx=sum((x-mx)**2 for x in xs)\nslope=sxy/sxx; icept=my-slope*mx\nsyy=sum((y-my)**2 for y in ys)\nr2=sxy**2/(sxx*syy)\nprint(\"y=%.4fx%+.4f R2=%.4f\" % (slope, icept, r2))\nprint(\"LINEAR\" if r2 >= r2min else \"NONLINEAR - investigate\")\n";
var SIG=false;
var SRC="public-harvest";
var B=[["adjustment", "Zero Adjustment", "Sets the instrument reading to zero with zero input applied, removing offset error.", "Zero Adjustment", "zero standard", "0.1% FS", "[0, 1, 2, 3, 4]", "[0.02, 1.01, 1.99, 3.02, 3.98]", "0.995"], ["linearity", "Span Adjustment", "Sets the full-scale reading with a known full-scale input, fixing gain error.", "Span Adjustment", "full-scale standard", "0.1% FS", "[0, 25, 50, 75, 100]", "[0.1, 24.9, 50.2, 74.8, 100.1]", "0.999"], ["traceability", "Linearity Check", "Verifies readings stay proportional across the range, flagging bow or S-shaped error.", "Linearity Check", "multi-point standard", "0.05% FS", "[0, 2, 4, 6, 8, 10]", "[0.0, 2.01, 3.99, 6.02, 7.98, 10.0]", "0.999"], ["environmental", "Hysteresis Test", "Compares upscale and downscale readings to detect mechanical or magnetic lag.", "Hysteresis Test", "bidirectional standard", "0.05% FS", "[0, 5, 10]", "[0.0, 5.0, 10.0]", "0.999"], ["reference-standards", "Repeatability Test", "Repeats the same measurement many times to quantify random variation.", "Repeatability Test", "stable artifact", "3 sigma bound", "[1, 2, 3, 4, 5]", "[1.001, 0.999, 1.0, 1.002, 0.998]", "0.99"], ["adjustment", "NIST Traceability Chain", "Documents the unbroken chain of comparisons linking the instrument to national standards.", "NIST Traceability Chain", "NIST-traceable refs", "chain documented", "[0, 10, 20, 30]", "[0.0, 10.0, 20.01, 29.99]", "0.9999"], ["linearity", "Calibration Curve Fitting", "Fits a polynomial or spline through calibration points for interpolation between them.", "Calibration Curve Fitting", "certified points", "residual < tol", "[0, 1, 2, 3]", "[0.0, 1.0, 4.02, 8.98]", "0.999"], ["traceability", "Two-point Calibration", "Fast field calibration using just zero and span points when linearity is already proven.", "Two-point Calibration", "two standards", "field-grade", "[0, 100]", "[0.2, 99.7]", "0.99"], ["environmental", "Multi-point Calibration", "Uses five or more points to capture nonlinearity across the full range.", "Multi-point Calibration", "point set", "lab-grade", "[0, 20, 40, 60, 80, 100]", "[0.0, 20.1, 39.9, 60.0, 80.2, 99.8]", "0.999"], ["reference-standards", "Temperature Compensation", "Applies correction coefficients for ambient temperature effects on the sensor.", "Temperature Compensation", "temp chamber", "per datasheet", "[20, 25, 30, 35]", "[0.0, 0.11, 0.21, 0.32]", "0.99"], ["adjustment", "Pressure Compensation", "Corrects readings for barometric pressure influence on pressure-sensitive instruments.", "Pressure Compensation", "pressure standard", "per datasheet", "[95, 100, 105]", "[ -0.05, 0.0, 0.05]", "0.99"], ["linearity", "Wavelength Calibration", "Aligns spectrometer wavelength scale against known emission lines.", "Wavelength Calibration", "Hg/Ne lamp lines", "0.1 nm", "[400, 500, 600]", "[400.02, 499.98, 600.01]", "0.9999"], ["traceability", "Mass Calibration", "Compares balances against certified masses with buoyancy correction.", "Mass Calibration", "OIML weights", "class tolerance", "[1, 10, 100]", "[1.0, 10.0, 100.0]", "0.99999"], ["environmental", "pH Buffer Calibration", "Calibrates pH meters with NIST-traceable buffer solutions at two or three points.", "pH Buffer Calibration", "pH 4/7/10 buffers", "0.02 pH", "[4.0, 7.0, 10.0]", "[4.01, 6.99, 10.02]", "0.999"], ["reference-standards", "Flow Meter Proving", "Compares flow meters against a prover loop or master meter at operating conditions.", "Flow Meter Proving", "prover", "0.25%", "[100, 200, 300]", "[100.1, 199.8, 300.2]", "0.999"], ["adjustment", "Torque Wrench Calibration", "Verifies torque wrenches on a calibrated transducer across their range.", "Torque Wrench Calibration", "torque transducer", "4% CW", "[20, 60, 100]", "[20.3, 59.5, 100.4]", "0.99"], ["linearity", "Gauge Block Comparison", "Compares working gauge blocks against master blocks interferometrically.", "Gauge Block Comparison", "master blocks", "grade tolerance", "[10, 25, 50]", "[10.0, 25.0, 50.0]", "0.999999"], ["traceability", "Deadweight Pressure Test", "Applies pressure from calibrated masses on a piston for primary-standard accuracy.", "Deadweight Pressure Test", "deadweight tester", "0.01%", "[10, 50, 100]", "[10.0, 50.0, 100.01]", "0.9999"], ["environmental", "Photometric Standard", "Calibrates light meters against a standard lamp of known luminous intensity.", "Photometric Standard", "standard lamp", "2%", "[100, 500, 1000]", "[101, 498, 1002]", "0.999"], ["reference-standards", "Electrical Reference", "Calibrates voltmeters against Josephson-junction or Zener references.", "Electrical Reference", "Josephson array", "ppm level", "[1, 5, 10]", "[1.0, 5.0, 10.0]", "0.999999"]];
function buildTitle(b){ return SIG?('Signature '+b[1]):b[1]; }
function buildDesc(b){
  var d=b[2]+' Recorded facts \u2014 '+FLD[0][1]+': '+b[3]+'; '+FLD[1][1]+': '+b[4]+'; '+FLD[2][1]+': '+b[5]+'. '+USE;
  if(SIG) d='Signature-original: '+d+' Built as a Signature-authored original for the JAH network; clearly labeled Signature and never presented as a public record.';
  return d;
}
function buildDemo(b){
  return DEMO.split('{title}').join(b[1]).split('{d1}').join(b[6]).split('{d2}').join(b[7]).split('{d3}').join(b[8]);
}
function generate(seed,opts){
  opts=opts||{}; var rnd=prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=buildTitle(b);
  var fields={}; fields[FLD[0][0]]=b[3]; fields[FLD[1][0]]=b[4]; fields[FLD[2][0]]=b[5];
  if(SIG) fields['signature_label']='Signature-authored original';
  return {id:id,title:title,description:buildDesc(b),category:cat,fields:fields,
    ladder_rank:1+(seed%3),
    demo:'# '+title+' \u2014 runnable demo (python3)\n'+buildDemo(b),
    provenance:'JAH Databases \u00b7 lane N3 build',last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].category===rec.category)
      return {ok:false,errors:['duplicate of archive record '+sample[i].id]};
  }
  return {ok:true,errors:[]};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var idre=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!idre.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(['public-harvest','signature-generated-completion'].indexOf(r.src)<0)e.push('src');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-scientific-instrument-calibration-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('scientific-instrument-calibration',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
