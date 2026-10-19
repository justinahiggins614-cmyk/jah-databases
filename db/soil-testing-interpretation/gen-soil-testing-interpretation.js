(function(){'use strict';
/* JAH The Soil Testing Interpretation Database generator — jahdb-soil-testing-interpretation-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-STI-";
var FIELDS=["test-reading","nutrient-management","amendment-planning"];
var TOPICS={"test-reading":["Why Test Soil \u2014 test-reading","NPK Basics \u2014 test-reading","Lowering pH (Sulfur) \u2014 test-reading","Potassium Management \u2014 test-reading","CEC Explained \u2014 test-reading","Drainage Assessment \u2014 test-reading","Manure Guidelines \u2014 test-reading","Fertilizer Labels \u2014 test-reading","Tissue Testing \u2014 test-reading","Testing Frequency \u2014 test-reading","Record Keeping \u2014 test-reading","The Fertile Ground Plan \u2014 test-reading"],"nutrient-management":["Taking a Good Sample \u2014 nutrient-management","The Amendment Playbook \u2014 nutrient-management","Nitrogen Management \u2014 nutrient-management","Micronutrients \u2014 nutrient-management","Soil Texture Triangle \u2014 nutrient-management","Salinity (EC) \u2014 nutrient-management","Cover Crops \u2014 nutrient-management","Slow-Release Fertilizers \u2014 nutrient-management","Soil Biology \u2014 nutrient-management","Lab vs Home Kits \u2014 nutrient-management","Problem Soils \u2014 nutrient-management"],"amendment-planning":["Understanding pH \u2014 amendment-planning","Raising pH (Lime) \u2014 amendment-planning","Phosphorus Management \u2014 amendment-planning","Organic Matter \u2014 amendment-planning","Compaction Testing \u2014 amendment-planning","Compost Application Rates \u2014 amendment-planning","Mulching \u2014 amendment-planning","Foliar Feeding \u2014 amendment-planning","Mycorrhizae \u2014 amendment-planning","Interpreting Recommendations \u2014 amendment-planning","Raised Bed Mixes \u2014 amendment-planning"]};
var KINDS="agriculture and environment record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Soil Testing Interpretation Database — generated study\n"
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
    name:topic+' — generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['agriculture and environment record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Soil Testing Interpretation Database.',
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
var gen={version:'jahdb-soil-testing-interpretation-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('soil-testing-interpretation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
