(function(){'use strict';
/* JAH The Earthquake-Resistant Construction Database generator — jahdb-earthquake-resistant-construction-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EQR-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Earthquake-Resistant Construction Is \u2014 Foundations",
  "Plate Tectonics: Why the Ground Moves \u2014 Foundations",
  "Seismic Waves: P, S, and Surface Waves \u2014 Foundations",
  "Measuring Earthquakes: Magnitude and Intensity \u2014 Foundations",
  "How Buildings Respond: The SDOF Idea \u2014 Foundations",
  "Resonance: When Buildings Amplify Shaking \u2014 Foundations",
  "Inertia Forces: F = ma in Buildings \u2014 Foundations",
  "Ductility: Bending Without Breaking \u2014 Foundations",
  "The Response Spectrum \u2014 Foundations",
  "Site Effects: Soil Matters \u2014 Foundations",
  "Liquefaction Basics \u2014 Foundations",
  "Nonstructural Components: The Forgotten Risk \u2014 Foundations"
 ],
 "Compounded": [
  "Equivalent Lateral Force Procedure \u2014 Compounded",
  "Base Shear Calculation \u2014 Compounded",
  "Story Drift Limits \u2014 Compounded",
  "Load Paths: Getting Forces to the Ground \u2014 Compounded",
  "Moment Frames \u2014 Compounded",
  "Shear Walls \u2014 Compounded",
  "Braced Frames \u2014 Compounded",
  "Diaphragms: Floors as Beams \u2014 Compounded",
  "Foundations for Seismic Loads \u2014 Compounded",
  "Detailing: Confinement and Hooks \u2014 Compounded",
  "Seismic Design Categories \u2014 Compounded",
  "Building Codes: ASCE 7 and IBC \u2014 Compounded"
 ],
 "Advanced": [
  "Response Spectrum Analysis \u2014 Advanced",
  "Base Isolation \u2014 Advanced",
  "Energy Dissipation: Dampers \u2014 Advanced",
  "Soil-Structure Interaction \u2014 Advanced",
  "Liquefaction Mitigation \u2014 Advanced",
  "Seismic Retrofit: Concrete Jacketing \u2014 Advanced",
  "Seismic Retrofit: FRP Wrapping \u2014 Advanced",
  "Retrofit: Steel Bracing Addition \u2014 Advanced",
  "3D-Printable Structural Models \u2014 Advanced",
  "Performance-Based Seismic Design \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Seismic Construction — "+safe+"\n"
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
    name:topic+' — seismic construction record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A seismic construction record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"seismic-construction-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-earthquake-resistant-construction-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('earthquake-resistant-construction',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
