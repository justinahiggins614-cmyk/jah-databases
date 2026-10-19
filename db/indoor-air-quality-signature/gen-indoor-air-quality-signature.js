(function(){'use strict';
/* JAH The Indoor Air Quality Signature Database generator — jahdb-indoor-air-quality-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-IAQ-";
var FIELDS=["pollutant-identification","ventilation-and-filtration","air-testing-methods"];
var TOPICS={"pollutant-identification":["Signature Common Indoor Pollutants (Signature Edition) \u2014 pollutant-identification","Signature HEPA Filtration Basics (Signature Edition) \u2014 pollutant-identification","Signature VOCs and Off-Gassing (Signature Edition) \u2014 pollutant-identification","Signature Pet Dander Management (Signature Edition) \u2014 pollutant-identification","Signature CO2 as Ventilation Proxy (Signature Edition) \u2014 pollutant-identification","Signature Air Fresheners: The Truth (Signature Edition) \u2014 pollutant-identification","Signature New Renovation Ventilation (Signature Edition) \u2014 pollutant-identification","Signature Plants and Air Quality Reality (Signature Edition) \u2014 pollutant-identification","Signature Lead Paint Dust (Signature Edition) \u2014 pollutant-identification","Signature Ventilation While Away (Signature Edition) \u2014 pollutant-identification","Signature Sick Building Clues (Signature Edition) \u2014 pollutant-identification","Signature Secondhand Smoke Infiltration (Signature Edition) \u2014 pollutant-identification"],"ventilation-and-filtration":["Signature Radon Testing and Mitigation (Signature Edition) \u2014 ventilation-and-filtration","Signature HVAC Filter Upgrades (Signature Edition) \u2014 ventilation-and-filtration","Signature Cleaning Product Air Impact (Signature Edition) \u2014 ventilation-and-filtration","Signature Dust Control Systems (Signature Edition) \u2014 ventilation-and-filtration","Signature Mold Spore Air Testing (Signature Edition) \u2014 ventilation-and-filtration","Signature Fireplace and Wood Stove Air (Signature Edition) \u2014 ventilation-and-filtration","Signature Bedroom Air Optimization (Signature Edition) \u2014 ventilation-and-filtration","Signature Wildfire Smoke Response (Signature Edition) \u2014 ventilation-and-filtration","Signature Asbestos Awareness (Signature Edition) \u2014 ventilation-and-filtration","Signature IAQ for Newborns (Signature Edition) \u2014 ventilation-and-filtration","Signature Air Purifier Placement (Signature Edition) \u2014 ventilation-and-filtration"],"air-testing-methods":["Signature Carbon Monoxide Safety (Signature Edition) \u2014 air-testing-methods","Signature Cooking Pollution Control (Signature Edition) \u2014 air-testing-methods","Signature Candle and Incense Particles (Signature Edition) \u2014 air-testing-methods","Signature Air Quality Monitors (Signature Edition) \u2014 air-testing-methods","Signature Formaldehyde Sources (Signature Edition) \u2014 air-testing-methods","Signature Garage-to-House Air Sealing (Signature Edition) \u2014 air-testing-methods","Signature Basement Air Quality (Signature Edition) \u2014 air-testing-methods","Signature Humidity and Respiratory Health (Signature Edition) \u2014 air-testing-methods","Signature Ozone Generators: Avoid (Signature Edition) \u2014 air-testing-methods","Signature The Annual IAQ Checkup (Signature Edition) \u2014 air-testing-methods","Signature Whole-House IAQ Plan (Signature Edition) \u2014 air-testing-methods"]};
var KINDS="home and household-systems record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Indoor Air Quality Signature Database — generated study\n"
   + "# Topic: "+safe+"\n"
   + "# Field: "+field+" | seed "+seed+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\", 'seed': "+seed+"}\n"
   + "CHECKS = ['topic_set','field_set','seed_set']\n"
   + "def validate(r):\n"
   + "    missing = [c for c in CHECKS if not r.get(c.replace('_set','')) and c!='seed_set']\n"
   + "    assert r['title'] and r['field'], 'record incomplete'\n"
   + "    return True\n"
   + "def main():\n"
   + "    assert validate(record)\n"
   + "    print('study: '+record['title'])\n"
   + "    print('field: '+record['field'])\n"
   + "    print('kind: home and household-systems record')\n"
   + "    print('Sample record — structural sample, not an archive entry.')\n"
   + "if __name__ == '__main__':\n"
   + "    main()\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — Signature generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural Signature sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['home and household-systems record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Indoor Air Quality Signature Database.',
    last_verified:'2026-10-18',
    ladder_rank:1, ladder_tier:'Foundations',
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field,seed),note:'Structural sample demo.'},
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
var gen={version:'jahdb-indoor-air-quality-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('indoor-air-quality-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
