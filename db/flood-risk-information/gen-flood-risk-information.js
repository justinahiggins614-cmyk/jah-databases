(function(){'use strict';
/* JAH The Flood Risk Information Database generator — jahdb-flood-risk-information-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FRI-";
var FIELDS=["risk-assessment","flood-insurance","preparation-and-recovery"];
var TOPICS={"risk-assessment":["Flood Maps (FEMA) \u2014 risk-assessment","100-Year Flood Myth \u2014 risk-assessment","Elevation Certificates \u2014 risk-assessment","Private Flood Insurance \u2014 risk-assessment","Waiting Periods \u2014 risk-assessment","Floodproofing Homes \u2014 risk-assessment","Elevation (Raising Homes) \u2014 risk-assessment","Backflow Valves \u2014 risk-assessment","Turn Around Don't Drown \u2014 risk-assessment","Mold After Floods \u2014 risk-assessment","Documenting Damage \u2014 risk-assessment","The Flood-Ready Household \u2014 risk-assessment"],"flood-insurance":["Flood Zones Explained \u2014 flood-insurance","Checking Your Address \u2014 flood-insurance","NFIP Basics \u2014 flood-insurance","Mandatory Purchase \u2014 flood-insurance","Filing Flood Claims \u2014 flood-insurance","Wet Floodproofing \u2014 flood-insurance","Sandbags Done Right \u2014 flood-insurance","Flood Emergency Kit \u2014 flood-insurance","Flood Watches vs Warnings \u2014 flood-insurance","FEMA Assistance \u2014 flood-insurance","Community Rating System \u2014 flood-insurance"],"preparation-and-recovery":["The Flood Playbook \u2014 preparation-and-recovery","Map Changes \u2014 preparation-and-recovery","NFIP Costs \u2014 preparation-and-recovery","Contents Coverage \u2014 preparation-and-recovery","Increased Cost of Compliance \u2014 preparation-and-recovery","Dry Floodproofing \u2014 preparation-and-recovery","Sump Pumps \u2014 preparation-and-recovery","Evacuation Planning \u2014 preparation-and-recovery","Post-Flood Cleanup \u2014 preparation-and-recovery","SBA Disaster Loans \u2014 preparation-and-recovery","Floodplain Regulations \u2014 preparation-and-recovery"]};
var KINDS="agriculture and environment record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Flood Risk Information Database — generated study\n"
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
    provenance:'Generated structural sample for the The Flood Risk Information Database.',
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
var gen={version:'jahdb-flood-risk-information-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('flood-risk-information',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
