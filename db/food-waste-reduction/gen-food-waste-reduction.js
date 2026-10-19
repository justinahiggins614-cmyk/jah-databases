(function(){'use strict';
/* JAH The Food Waste Reduction Database generator — jahdb-food-waste-reduction-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FWR-";
var FIELDS=["waste-prevention","food-recovery","composting-systems"];
var TOPICS={"waste-prevention":["Where Food Is Wasted \u2014 waste-prevention","Home: Meal Planning \u2014 waste-prevention","Home: Use-It-Up Meals \u2014 waste-prevention","Farm: Harvest Efficiency \u2014 waste-prevention","Retail: Markdown Systems \u2014 waste-prevention","Restaurant: Inventory FIFO \u2014 waste-prevention","Composting Basics \u2014 waste-prevention","Municipal Composting \u2014 waste-prevention","Measuring Waste \u2014 waste-prevention","Donation Logistics \u2014 waste-prevention","Zero-Waste Kitchens \u2014 waste-prevention","Annual Waste Review \u2014 waste-prevention"],"food-recovery":["Prevention Hierarchy \u2014 food-recovery","Home: Smart Shopping \u2014 food-recovery","Home: Freezing Guide \u2014 food-recovery","Farm: Cosmetic Standards \u2014 food-recovery","Retail: Donation Programs \u2014 food-recovery","Food Recovery Apps \u2014 food-recovery","Vermicomposting \u2014 food-recovery","Animal Feed \u2014 food-recovery","Waste Tracking Apps \u2014 food-recovery","Liability Protection \u2014 food-recovery","The Waste-Free Plan \u2014 food-recovery"],"composting-systems":["The Reduction Playbook \u2014 composting-systems","Home: Proper Storage \u2014 composting-systems","Date Labels Decoded \u2014 composting-systems","Gleaning \u2014 composting-systems","Restaurant: Portion Control \u2014 composting-systems","Food Banks \u2014 composting-systems","Bokashi \u2014 composting-systems","Anaerobic Digestion \u2014 composting-systems","Staff Training \u2014 composting-systems","School Waste Programs \u2014 composting-systems","Community Fridges \u2014 composting-systems"]};
var KINDS="agriculture and environment record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Food Waste Reduction Database — generated study\n"
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
    provenance:'Generated structural sample for the The Food Waste Reduction Database.',
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
var gen={version:'jahdb-food-waste-reduction-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('food-waste-reduction',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
