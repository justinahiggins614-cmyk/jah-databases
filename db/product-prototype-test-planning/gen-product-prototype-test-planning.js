(function(){'use strict';
/* JAH The Product Prototype Test Planning Database generator — jahdb-product-prototype-test-planning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PPTP-";
var FIELDS=["test-strategy","prototype-levels","validation-systems"];
var TOPICS={"test-strategy":["Prototype Levels \u2014 test-strategy","The Prototype Test Playbook \u2014 test-strategy","Breadboard Prototypes \u2014 test-strategy","Usability Testing \u2014 test-strategy","Drop and Shock Testing \u2014 test-strategy","Safety Testing \u2014 test-strategy","Failure Analysis \u2014 test-strategy","Test Fixtures \u2014 test-strategy","User Acceptance Testing \u2014 test-strategy","Design of Experiments \u2014 test-strategy","Packaging Testing \u2014 test-strategy","The Test Master Plan \u2014 test-strategy"],"prototype-levels":["Test Planning Basics \u2014 prototype-levels","Paper Prototypes \u2014 prototype-levels","Wizard of Oz Testing \u2014 prototype-levels","Durability Testing \u2014 prototype-levels","Ingress Protection (IP) \u2014 prototype-levels","Beta Testing \u2014 prototype-levels","HALT Testing \u2014 prototype-levels","Test Automation \u2014 prototype-levels","Test Documentation \u2014 prototype-levels","Tolerance Testing \u2014 prototype-levels","Launch Readiness \u2014 prototype-levels"],"validation-systems":["Risk-Driven Testing \u2014 validation-systems","3D Printing for Prototypes \u2014 validation-systems","Functional Testing \u2014 validation-systems","Environmental Testing \u2014 validation-systems","EMC Testing \u2014 validation-systems","A/B Product Testing \u2014 validation-systems","Reliability Demonstration \u2014 validation-systems","Regression Testing \u2014 validation-systems","Bug Tracking \u2014 validation-systems","Human Factors Testing \u2014 validation-systems","Post-Launch Monitoring \u2014 validation-systems"]};
var KINDS="engineering record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Product Prototype Test Planning Database — generated study\n"
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
   + "    print('kind: engineering record')\n"
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
    standards:['engineering record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Product Prototype Test Planning Database.',
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
var gen={version:'jahdb-product-prototype-test-planning-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('product-prototype-test-planning',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
