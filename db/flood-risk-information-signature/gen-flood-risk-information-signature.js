(function(){'use strict';
/* JAH The Flood Risk Information Signature Database generator — jahdb-flood-risk-information-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FRI-";
var FIELDS=["risk-assessment","flood-insurance","preparation-and-recovery"];
var TOPICS={"risk-assessment":["Signature Flood Maps (FEMA) (Signature Edition) \u2014 risk-assessment","Signature 100-Year Flood Myth (Signature Edition) \u2014 risk-assessment","Signature Elevation Certificates (Signature Edition) \u2014 risk-assessment","Signature Private Flood Insurance (Signature Edition) \u2014 risk-assessment","Signature Waiting Periods (Signature Edition) \u2014 risk-assessment","Signature Floodproofing Homes (Signature Edition) \u2014 risk-assessment","Signature Elevation (Raising Homes) (Signature Edition) \u2014 risk-assessment","Signature Backflow Valves (Signature Edition) \u2014 risk-assessment","Signature Turn Around Don't Drown (Signature Edition) \u2014 risk-assessment","Signature Mold After Floods (Signature Edition) \u2014 risk-assessment","Signature Documenting Damage (Signature Edition) \u2014 risk-assessment","Signature The Flood-Ready Household (Signature Edition) \u2014 risk-assessment"],"flood-insurance":["Signature Flood Zones Explained (Signature Edition) \u2014 flood-insurance","Signature Checking Your Address (Signature Edition) \u2014 flood-insurance","Signature NFIP Basics (Signature Edition) \u2014 flood-insurance","Signature Mandatory Purchase (Signature Edition) \u2014 flood-insurance","Signature Filing Flood Claims (Signature Edition) \u2014 flood-insurance","Signature Wet Floodproofing (Signature Edition) \u2014 flood-insurance","Signature Sandbags Done Right (Signature Edition) \u2014 flood-insurance","Signature Flood Emergency Kit (Signature Edition) \u2014 flood-insurance","Signature Flood Watches vs Warnings (Signature Edition) \u2014 flood-insurance","Signature FEMA Assistance (Signature Edition) \u2014 flood-insurance","Signature Community Rating System (Signature Edition) \u2014 flood-insurance"],"preparation-and-recovery":["Signature The Flood Playbook (Signature Edition) \u2014 preparation-and-recovery","Signature Map Changes (Signature Edition) \u2014 preparation-and-recovery","Signature NFIP Costs (Signature Edition) \u2014 preparation-and-recovery","Signature Contents Coverage (Signature Edition) \u2014 preparation-and-recovery","Signature Increased Cost of Compliance (Signature Edition) \u2014 preparation-and-recovery","Signature Dry Floodproofing (Signature Edition) \u2014 preparation-and-recovery","Signature Sump Pumps (Signature Edition) \u2014 preparation-and-recovery","Signature Evacuation Planning (Signature Edition) \u2014 preparation-and-recovery","Signature Post-Flood Cleanup (Signature Edition) \u2014 preparation-and-recovery","Signature SBA Disaster Loans (Signature Edition) \u2014 preparation-and-recovery","Signature Floodplain Regulations (Signature Edition) \u2014 preparation-and-recovery"]};
var KINDS="agriculture and environment record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Flood Risk Information Signature Database — generated study\n"
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
    provenance:'Generated structural sample for the The Flood Risk Information Signature Database.',
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
var gen={version:'jahdb-flood-risk-information-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('flood-risk-information-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
