(function(){'use strict';
/* JAH The Accessible Kitchen Planning Signature Database generator — jahdb-accessible-kitchen-planning-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AKP-";
var FIELDS=["accessible-layouts","adaptive-tools","safety-systems"];
var TOPICS={"accessible-layouts":["Signature Universal Kitchen Principles (Signature Edition) \u2014 accessible-layouts","Signature The Accessible Playbook (Signature Edition) \u2014 accessible-layouts","Signature Oven Access (Signature Edition) \u2014 accessible-layouts","Signature Pull-Down Shelving (Signature Edition) \u2014 accessible-layouts","Signature One-Handed Tools (Signature Edition) \u2014 accessible-layouts","Signature Talking Appliances (Signature Edition) \u2014 accessible-layouts","Signature Non-Slip Flooring (Signature Edition) \u2014 accessible-layouts","Signature Galley Layouts (Signature Edition) \u2014 accessible-layouts","Signature Remodel Planning (Signature Edition) \u2014 accessible-layouts","Signature Meal Prep Systems (Signature Edition) \u2014 accessible-layouts","Signature Small Kitchen Access (Signature Edition) \u2014 accessible-layouts","Signature Inspiration Gallery Notes (Signature Edition) \u2014 accessible-layouts"],"adaptive-tools":["Signature Wheelchair Clearances (Signature Edition) \u2014 adaptive-tools","Signature Sink and Faucet Access (Signature Edition) \u2014 adaptive-tools","Signature Refrigerator Layout (Signature Edition) \u2014 adaptive-tools","Signature Lazy Susans and Pull-Outs (Signature Edition) \u2014 adaptive-tools","Signature Seated Cooking Setup (Signature Edition) \u2014 adaptive-tools","Signature Fire Safety Adapted (Signature Edition) \u2014 adaptive-tools","Signature Task Lighting (Signature Edition) \u2014 adaptive-tools","Signature L-Shape Access (Signature Edition) \u2014 adaptive-tools","Signature OT Consultations (Signature Edition) \u2014 adaptive-tools","Signature Caregiver Kitchen Design (Signature Edition) \u2014 adaptive-tools","Signature Outdoor Cooking Access (Signature Edition) \u2014 adaptive-tools"],"safety-systems":["Signature Counter Height Options (Signature Edition) \u2014 safety-systems","Signature Cooktop Safety (Signature Edition) \u2014 safety-systems","Signature Storage Reach Zones (Signature Edition) \u2014 safety-systems","Signature D-Handles and Levers (Signature Edition) \u2014 safety-systems","Signature Visual Contrasts (Signature Edition) \u2014 safety-systems","Signature Anti-Scald Devices (Signature Edition) \u2014 safety-systems","Signature Cart Workstations (Signature Edition) \u2014 safety-systems","Signature Budget Adaptations (Signature Edition) \u2014 safety-systems","Signature Cooking Techniques Adapted (Signature Edition) \u2014 safety-systems","Signature Aging-in-Place Kitchens (Signature Edition) \u2014 safety-systems","Signature The Kitchen Checklist (Signature Edition) \u2014 safety-systems"]};
var KINDS="accessibility record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Accessible Kitchen Planning Signature Database — generated study\n"
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
   + "    print('kind: accessibility record')\n"
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
    standards:['accessibility record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Accessible Kitchen Planning Signature Database.',
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
var gen={version:'jahdb-accessible-kitchen-planning-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('accessible-kitchen-planning-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
