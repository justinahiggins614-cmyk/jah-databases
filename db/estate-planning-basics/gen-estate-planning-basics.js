(function(){'use strict';
/* JAH The Estate Planning Basics Database generator — jahdb-estate-planning-basics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EPB-";
var FIELDS=["core-documents","beneficiary-planning","estate-administration"];
var TOPICS={"core-documents":["The Will: Core Document \u2014 core-documents","Healthcare Proxy / Medical POA \u2014 core-documents","Choosing an Executor \u2014 core-documents","Estate Tax Thresholds \u2014 core-documents","Life Insurance Sizing \u2014 core-documents","Updating After Life Changes \u2014 core-documents","Business Succession Basics \u2014 core-documents","Pet Provisions in Wills \u2014 core-documents","Incapacity Planning Beyond Documents \u2014 core-documents","Estate Planning Attorney vs DIY \u2014 core-documents","Estate Planning Myths \u2014 core-documents","Annual Estate Review Ritual \u2014 core-documents"],"beneficiary-planning":["Beneficiary Designations Beat Wills \u2014 beneficiary-planning","Living Will Essentials \u2014 beneficiary-planning","Trusts: Revocable Living Trust \u2014 beneficiary-planning","Digital Asset Planning \u2014 beneficiary-planning","Funeral Wishes Documentation \u2014 beneficiary-planning","Blended Family Planning \u2014 beneficiary-planning","Charitable Giving in Estates \u2014 beneficiary-planning","Debt After Death \u2014 beneficiary-planning","Gifting While Alive \u2014 beneficiary-planning","Storing Documents Safely \u2014 beneficiary-planning","The 90-Minute Estate Starter \u2014 beneficiary-planning"],"estate-administration":["Power of Attorney (Financial) \u2014 estate-administration","Choosing Guardians for Minor Children \u2014 estate-administration","Probate: What It Really Is \u2014 estate-administration","The 'Death Binder' \u2014 estate-administration","Letters to Loved Ones \u2014 estate-administration","Special Needs Trusts \u2014 estate-administration","Estate Planning for Singles \u2014 estate-administration","Executor's First 30 Days \u2014 estate-administration","Reviewing Insurance Beneficiaries \u2014 estate-administration","Communicating the Plan \u2014 estate-administration","Estate Planning for New Parents \u2014 estate-administration"]};
var KINDS="money and financial-decision record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Estate Planning Basics Database — generated study\n"
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
    name:topic+' — generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['money and financial-decision record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Estate Planning Basics Database.',
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
var gen={version:'jahdb-estate-planning-basics-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('estate-planning-basics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
