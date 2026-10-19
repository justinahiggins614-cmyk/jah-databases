(function(){'use strict';
/* JAH The Estate Planning Basics Signature Database generator — jahdb-estate-planning-basics-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EPB-";
var FIELDS=["core-documents","beneficiary-planning","estate-administration"];
var TOPICS={"core-documents":["Signature The Will: Core Document (Signature Edition) \u2014 core-documents","Signature Healthcare Proxy / Medical POA (Signature Edition) \u2014 core-documents","Signature Choosing an Executor (Signature Edition) \u2014 core-documents","Signature Estate Tax Thresholds (Signature Edition) \u2014 core-documents","Signature Life Insurance Sizing (Signature Edition) \u2014 core-documents","Signature Updating After Life Changes (Signature Edition) \u2014 core-documents","Signature Business Succession Basics (Signature Edition) \u2014 core-documents","Signature Pet Provisions in Wills (Signature Edition) \u2014 core-documents","Signature Incapacity Planning Beyond Documents (Signature Edition) \u2014 core-documents","Signature Estate Planning Attorney vs DIY (Signature Edition) \u2014 core-documents","Signature Estate Planning Myths (Signature Edition) \u2014 core-documents","Signature Annual Estate Review Ritual (Signature Edition) \u2014 core-documents"],"beneficiary-planning":["Signature Beneficiary Designations Beat Wills (Signature Edition) \u2014 beneficiary-planning","Signature Living Will Essentials (Signature Edition) \u2014 beneficiary-planning","Signature Trusts: Revocable Living Trust (Signature Edition) \u2014 beneficiary-planning","Signature Digital Asset Planning (Signature Edition) \u2014 beneficiary-planning","Signature Funeral Wishes Documentation (Signature Edition) \u2014 beneficiary-planning","Signature Blended Family Planning (Signature Edition) \u2014 beneficiary-planning","Signature Charitable Giving in Estates (Signature Edition) \u2014 beneficiary-planning","Signature Debt After Death (Signature Edition) \u2014 beneficiary-planning","Signature Gifting While Alive (Signature Edition) \u2014 beneficiary-planning","Signature Storing Documents Safely (Signature Edition) \u2014 beneficiary-planning","Signature The 90-Minute Estate Starter (Signature Edition) \u2014 beneficiary-planning"],"estate-administration":["Signature Power of Attorney (Financial) (Signature Edition) \u2014 estate-administration","Signature Choosing Guardians for Minor Children (Signature Edition) \u2014 estate-administration","Signature Probate: What It Really Is (Signature Edition) \u2014 estate-administration","Signature The 'Death Binder' (Signature Edition) \u2014 estate-administration","Signature Letters to Loved Ones (Signature Edition) \u2014 estate-administration","Signature Special Needs Trusts (Signature Edition) \u2014 estate-administration","Signature Estate Planning for Singles (Signature Edition) \u2014 estate-administration","Signature Executor's First 30 Days (Signature Edition) \u2014 estate-administration","Signature Reviewing Insurance Beneficiaries (Signature Edition) \u2014 estate-administration","Signature Communicating the Plan (Signature Edition) \u2014 estate-administration","Signature Estate Planning for New Parents (Signature Edition) \u2014 estate-administration"]};
var KINDS="money and financial-decision record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Estate Planning Basics Signature Database — generated study\n"
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
   + "    print('kind: money and financial-decision record')\n"
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
    standards:['money and financial-decision record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Estate Planning Basics Signature Database.',
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
var gen={version:'jahdb-estate-planning-basics-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('estate-planning-basics-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
