(function(){'use strict';
/* JAH The Indoor Air Quality Database generator — jahdb-indoor-air-quality-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-IAQ-";
var FIELDS=["pollutant-identification","ventilation-and-filtration","air-testing-methods"];
var TOPICS={"pollutant-identification":["Common Indoor Pollutants \u2014 pollutant-identification","HEPA Filtration Basics \u2014 pollutant-identification","VOCs and Off-Gassing \u2014 pollutant-identification","Pet Dander Management \u2014 pollutant-identification","CO2 as Ventilation Proxy \u2014 pollutant-identification","Air Fresheners: The Truth \u2014 pollutant-identification","New Renovation Ventilation \u2014 pollutant-identification","Plants and Air Quality Reality \u2014 pollutant-identification","Lead Paint Dust \u2014 pollutant-identification","Ventilation While Away \u2014 pollutant-identification","Sick Building Clues \u2014 pollutant-identification","Secondhand Smoke Infiltration \u2014 pollutant-identification"],"ventilation-and-filtration":["Radon Testing and Mitigation \u2014 ventilation-and-filtration","HVAC Filter Upgrades \u2014 ventilation-and-filtration","Cleaning Product Air Impact \u2014 ventilation-and-filtration","Dust Control Systems \u2014 ventilation-and-filtration","Mold Spore Air Testing \u2014 ventilation-and-filtration","Fireplace and Wood Stove Air \u2014 ventilation-and-filtration","Bedroom Air Optimization \u2014 ventilation-and-filtration","Wildfire Smoke Response \u2014 ventilation-and-filtration","Asbestos Awareness \u2014 ventilation-and-filtration","IAQ for Newborns \u2014 ventilation-and-filtration","Air Purifier Placement \u2014 ventilation-and-filtration"],"air-testing-methods":["Carbon Monoxide Safety \u2014 air-testing-methods","Cooking Pollution Control \u2014 air-testing-methods","Candle and Incense Particles \u2014 air-testing-methods","Air Quality Monitors \u2014 air-testing-methods","Formaldehyde Sources \u2014 air-testing-methods","Garage-to-House Air Sealing \u2014 air-testing-methods","Basement Air Quality \u2014 air-testing-methods","Humidity and Respiratory Health \u2014 air-testing-methods","Ozone Generators: Avoid \u2014 air-testing-methods","The Annual IAQ Checkup \u2014 air-testing-methods","Whole-House IAQ Plan \u2014 air-testing-methods"]};
var KINDS="home and household-systems record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Indoor Air Quality Database — generated study\n"
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
    name:topic+' — generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['home and household-systems record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Indoor Air Quality Database.',
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
var gen={version:'jahdb-indoor-air-quality-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('indoor-air-quality',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
