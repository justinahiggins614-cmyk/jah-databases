(function(){'use strict';
/* JAH The Corrosion and Degradation Science Database generator — jahdb-corrosion-degradation-science-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CDS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Corrosion Is: Metal Returning to Ore \u2014 Foundations",
  "The Electrochemical Cell: Anode, Cathode, Electrolyte \u2014 Foundations",
  "Uniform Corrosion: The Even Attack \u2014 Foundations",
  "The Galvanic Series: Who Sacrifices for Whom \u2014 Foundations",
  "Rust: Iron's Familiar Failure \u2014 Foundations",
  "Corrosion Rate: Mils Per Year \u2014 Foundations",
  "Environment Matters: What Surrounds the Metal \u2014 Foundations",
  "Passivity: The Protective Film \u2014 Foundations",
  "Corrosion Measurement: Coupons and Probes \u2014 Foundations",
  "Faraday's Law and Metal Loss \u2014 Foundations",
  "Degradation Beyond Metals: Polymers, Concrete \u2014 Foundations",
  "Cost of Corrosion: The Trillion-Dollar Problem \u2014 Foundations"
 ],
 "Compounded": [
  "Galvanic Corrosion: Dissimilar Metals \u2014 Compounded",
  "Pitting Corrosion: The Hidden Killer \u2014 Compounded",
  "Crevice Corrosion \u2014 Compounded",
  "Intergranular Corrosion and Sensitization \u2014 Compounded",
  "Stress Corrosion Cracking (SCC) \u2014 Compounded",
  "Corrosion Fatigue \u2014 Compounded",
  "Erosion-Corrosion \u2014 Compounded",
  "Microbiologically Influenced Corrosion (MIC) \u2014 Compounded",
  "Pourbaix Diagrams: Maps of Stability \u2014 Compounded",
  "Polarization Curves and Tafel \u2014 Compounded",
  "PREN: Pitting Resistance Equivalent \u2014 Compounded",
  "Atmospheric Corrosion and Weathering \u2014 Compounded"
 ],
 "Advanced": [
  "Cathodic Protection: Sacrificial and Impressed \u2014 Advanced",
  "Coatings: Barriers Between Metal and World \u2014 Advanced",
  "Inhibitors: Chemistry Against Corrosion \u2014 Advanced",
  "Material Selection Against Corrosion \u2014 Advanced",
  "Corrosion Monitoring Systems \u2014 Advanced",
  "Service Life Modeling \u2014 Advanced",
  "Concrete Degradation: Rebar Corrosion \u2014 Advanced",
  "High-Temperature Oxidation \u2014 Advanced",
  "Corrosion Test Racks: Printable Exposure Fixtures \u2014 Advanced",
  "Designing Against Corrosion: The Systems View \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Corrosion Science — "+safe+"\n"
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
    name:topic+' — corrosion science record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A corrosion science record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"corrosion-science-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-corrosion-degradation-science-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('corrosion-degradation-science',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
