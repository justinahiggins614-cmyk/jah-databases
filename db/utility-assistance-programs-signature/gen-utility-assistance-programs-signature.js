(function(){'use strict';
/* JAH The Utility Assistance Programs Signature Database generator — jahdb-utility-assistance-programs-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-UAP-";
var FIELDS=["bill-assistance-programs","shutoff-protection","energy-efficiency-help"];
var TOPICS={"bill-assistance-programs":["Signature LIHEAP Essentials (Signature Edition) \u2014 bill-assistance-programs","Signature What To Do at Shutoff Notice (Signature Edition) \u2014 bill-assistance-programs","Signature Energy Audit Basics (Signature Edition) \u2014 bill-assistance-programs","Signature Senior Utility Discounts (Signature Edition) \u2014 bill-assistance-programs","Signature Cooling Assistance (Signature Edition) \u2014 bill-assistance-programs","Signature Reading Your Meter (Signature Edition) \u2014 bill-assistance-programs","Signature Nonprofit Utility Help (Signature Edition) \u2014 bill-assistance-programs","Signature Moving: Utility Transfers (Signature Edition) \u2014 bill-assistance-programs","Signature Energy-Efficient Appliances Aid (Signature Edition) \u2014 bill-assistance-programs","Signature Generator Safety (Signature Edition) \u2014 bill-assistance-programs","Signature Documenting Everything (Signature Edition) \u2014 bill-assistance-programs","Signature Utility Deposit Help (Signature Edition) \u2014 bill-assistance-programs"],"shutoff-protection":["Signature Utility Company Hardship Programs (Signature Edition) \u2014 shutoff-protection","Signature Payment Plan Negotiation (Signature Edition) \u2014 shutoff-protection","Signature Reducing the Bill Now (Signature Edition) \u2014 shutoff-protection","Signature Water Bill Assistance (Signature Edition) \u2014 shutoff-protection","Signature Heating Oil Assistance (Signature Edition) \u2014 shutoff-protection","Signature Disputing High Bills (Signature Edition) \u2014 shutoff-protection","Signature Disability Utility Protections (Signature Edition) \u2014 shutoff-protection","Signature Solar for Low-Income (Signature Edition) \u2014 shutoff-protection","Signature The Annual Utility Review (Signature Edition) \u2014 shutoff-protection","Signature Preparing for Rate Hikes (Signature Edition) \u2014 shutoff-protection","Signature The Utility Aid Calendar (Signature Edition) \u2014 shutoff-protection"],"energy-efficiency-help":["Signature Shutoff Protection Rules (Signature Edition) \u2014 energy-efficiency-help","Signature Weatherization Assistance (WAP) (Signature Edition) \u2014 energy-efficiency-help","Signature Medical Baseline Programs (Signature Edition) \u2014 energy-efficiency-help","Signature Phone/Internet (Lifeline/ACP) (Signature Edition) \u2014 energy-efficiency-help","Signature Budget Billing Explained (Signature Edition) \u2014 energy-efficiency-help","Signature 211: The Starting Point (Signature Edition) \u2014 energy-efficiency-help","Signature Landlord vs Tenant Utilities (Signature Edition) \u2014 energy-efficiency-help","Signature Time-of-Use Rates (Signature Edition) \u2014 energy-efficiency-help","Signature Crisis: No Heat in Winter (Signature Edition) \u2014 energy-efficiency-help","Signature Utility Scam Defense (Signature Edition) \u2014 energy-efficiency-help","Signature Advocating for Yourself (Signature Edition) \u2014 energy-efficiency-help"]};
var KINDS="government-assistance record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Utility Assistance Programs Signature Database — generated study\n"
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
    name:topic+' — Signature generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural Signature sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['government-assistance record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Utility Assistance Programs Signature Database.',
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
var gen={version:'jahdb-utility-assistance-programs-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('utility-assistance-programs-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
