(function(){'use strict';
/* JAH The Soil Testing Interpretation Signature Database generator — jahdb-soil-testing-interpretation-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-STI-";
var FIELDS=["test-reading","nutrient-management","amendment-planning"];
var TOPICS={"test-reading":["Signature Why Test Soil (Signature Edition) \u2014 test-reading","Signature NPK Basics (Signature Edition) \u2014 test-reading","Signature Lowering pH (Sulfur) (Signature Edition) \u2014 test-reading","Signature Potassium Management (Signature Edition) \u2014 test-reading","Signature CEC Explained (Signature Edition) \u2014 test-reading","Signature Drainage Assessment (Signature Edition) \u2014 test-reading","Signature Manure Guidelines (Signature Edition) \u2014 test-reading","Signature Fertilizer Labels (Signature Edition) \u2014 test-reading","Signature Tissue Testing (Signature Edition) \u2014 test-reading","Signature Testing Frequency (Signature Edition) \u2014 test-reading","Signature Record Keeping (Signature Edition) \u2014 test-reading","Signature The Fertile Ground Plan (Signature Edition) \u2014 test-reading"],"nutrient-management":["Signature Taking a Good Sample (Signature Edition) \u2014 nutrient-management","Signature The Amendment Playbook (Signature Edition) \u2014 nutrient-management","Signature Nitrogen Management (Signature Edition) \u2014 nutrient-management","Signature Micronutrients (Signature Edition) \u2014 nutrient-management","Signature Soil Texture Triangle (Signature Edition) \u2014 nutrient-management","Signature Salinity (EC) (Signature Edition) \u2014 nutrient-management","Signature Cover Crops (Signature Edition) \u2014 nutrient-management","Signature Slow-Release Fertilizers (Signature Edition) \u2014 nutrient-management","Signature Soil Biology (Signature Edition) \u2014 nutrient-management","Signature Lab vs Home Kits (Signature Edition) \u2014 nutrient-management","Signature Problem Soils (Signature Edition) \u2014 nutrient-management"],"amendment-planning":["Signature Understanding pH (Signature Edition) \u2014 amendment-planning","Signature Raising pH (Lime) (Signature Edition) \u2014 amendment-planning","Signature Phosphorus Management (Signature Edition) \u2014 amendment-planning","Signature Organic Matter (Signature Edition) \u2014 amendment-planning","Signature Compaction Testing (Signature Edition) \u2014 amendment-planning","Signature Compost Application Rates (Signature Edition) \u2014 amendment-planning","Signature Mulching (Signature Edition) \u2014 amendment-planning","Signature Foliar Feeding (Signature Edition) \u2014 amendment-planning","Signature Mycorrhizae (Signature Edition) \u2014 amendment-planning","Signature Interpreting Recommendations (Signature Edition) \u2014 amendment-planning","Signature Raised Bed Mixes (Signature Edition) \u2014 amendment-planning"]};
var KINDS="agriculture and environment record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Soil Testing Interpretation Signature Database — generated study\n"
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
   + "    print('kind: agriculture and environment record')\n"
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
    standards:['agriculture and environment record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Soil Testing Interpretation Signature Database.',
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
var gen={version:'jahdb-soil-testing-interpretation-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('soil-testing-interpretation-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
