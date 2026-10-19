(function(){'use strict';
/* JAH The Utility Assistance Programs Database generator — jahdb-utility-assistance-programs-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-UAP-";
var FIELDS=["bill-assistance-programs","shutoff-protection","energy-efficiency-help"];
var TOPICS={"bill-assistance-programs":["LIHEAP Essentials \u2014 bill-assistance-programs","What To Do at Shutoff Notice \u2014 bill-assistance-programs","Energy Audit Basics \u2014 bill-assistance-programs","Senior Utility Discounts \u2014 bill-assistance-programs","Cooling Assistance \u2014 bill-assistance-programs","Reading Your Meter \u2014 bill-assistance-programs","Nonprofit Utility Help \u2014 bill-assistance-programs","Moving: Utility Transfers \u2014 bill-assistance-programs","Energy-Efficient Appliances Aid \u2014 bill-assistance-programs","Generator Safety \u2014 bill-assistance-programs","Documenting Everything \u2014 bill-assistance-programs","Utility Deposit Help \u2014 bill-assistance-programs"],"shutoff-protection":["Utility Company Hardship Programs \u2014 shutoff-protection","Payment Plan Negotiation \u2014 shutoff-protection","Reducing the Bill Now \u2014 shutoff-protection","Water Bill Assistance \u2014 shutoff-protection","Heating Oil Assistance \u2014 shutoff-protection","Disputing High Bills \u2014 shutoff-protection","Disability Utility Protections \u2014 shutoff-protection","Solar for Low-Income \u2014 shutoff-protection","The Annual Utility Review \u2014 shutoff-protection","Preparing for Rate Hikes \u2014 shutoff-protection","The Utility Aid Calendar \u2014 shutoff-protection"],"energy-efficiency-help":["Shutoff Protection Rules \u2014 energy-efficiency-help","Weatherization Assistance (WAP) \u2014 energy-efficiency-help","Medical Baseline Programs \u2014 energy-efficiency-help","Phone/Internet (Lifeline/ACP) \u2014 energy-efficiency-help","Budget Billing Explained \u2014 energy-efficiency-help","211: The Starting Point \u2014 energy-efficiency-help","Landlord vs Tenant Utilities \u2014 energy-efficiency-help","Time-of-Use Rates \u2014 energy-efficiency-help","Crisis: No Heat in Winter \u2014 energy-efficiency-help","Utility Scam Defense \u2014 energy-efficiency-help","Advocating for Yourself \u2014 energy-efficiency-help"]};
var KINDS="government-assistance record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Utility Assistance Programs Database — generated study\n"
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
   + "    print('kind: government-assistance record')\n"
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
    standards:['government-assistance record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Utility Assistance Programs Database.',
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
var gen={version:'jahdb-utility-assistance-programs-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('utility-assistance-programs',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
