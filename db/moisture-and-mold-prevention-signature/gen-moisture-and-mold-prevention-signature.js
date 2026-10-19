(function(){'use strict';
/* JAH The Moisture and Mold Prevention Signature Database generator — jahdb-moisture-and-mold-prevention-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MMP-";
var FIELDS=["moisture-detection","humidity-control","mold-remediation"];
var TOPICS={"moisture-detection":["Signature Indoor Humidity Targets (Signature Edition) \u2014 moisture-detection","Signature Dehumidifier Sizing and Use (Signature Edition) \u2014 moisture-detection","Signature Small Mold Cleanup (Under 10 sq ft) (Signature Edition) \u2014 moisture-detection","Signature Grading and Drainage Basics (Signature Edition) \u2014 moisture-detection","Signature Vapor Barriers: Where They Go (Signature Edition) \u2014 moisture-detection","Signature Flood Cleanup First 48 Hours (Signature Edition) \u2014 moisture-detection","Signature Humidity and Wood Floors (Signature Edition) \u2014 moisture-detection","Signature Roof Leak Triage (Signature Edition) \u2014 moisture-detection","Signature Houseplant Humidity Balance (Signature Edition) \u2014 moisture-detection","Signature Whole-House Ventilation Strategy (Signature Edition) \u2014 moisture-detection","Signature The Dry-Home Annual Plan (Signature Edition) \u2014 moisture-detection","Signature Plumbing Condensation (Sweating Pipes) (Signature Edition) \u2014 moisture-detection"],"humidity-control":["Signature Bathroom Ventilation Rules (Signature Edition) \u2014 humidity-control","Signature Condensation on Windows (Signature Edition) \u2014 humidity-control","Signature When to Call a Mold Professional (Signature Edition) \u2014 humidity-control","Signature Plumbing Leak Detection (Signature Edition) \u2014 humidity-control","Signature Musty Smell Investigation (Signature Edition) \u2014 humidity-control","Signature Mold-Resistant Building Materials (Signature Edition) \u2014 humidity-control","Signature Dust Mite Control (Signature Edition) \u2014 humidity-control","Signature Ice Dam Prevention (Signature Edition) \u2014 humidity-control","Signature New Construction Drying (Signature Edition) \u2014 humidity-control","Signature Mold and Health: Sensible View (Signature Edition) \u2014 humidity-control","Signature Dehumidifier vs Air Conditioner (Signature Edition) \u2014 humidity-control"],"mold-remediation":["Signature Basement Moisture Sources (Signature Edition) \u2014 mold-remediation","Signature Mold Test Kits: What They Tell You (Signature Edition) \u2014 mold-remediation","Signature Crawl Space Encapsulation (Signature Edition) \u2014 mold-remediation","Signature Attic Moisture and Venting (Signature Edition) \u2014 mold-remediation","Signature HVAC Condensate Management (Signature Edition) \u2014 mold-remediation","Signature Seasonal Moisture Checklist (Signature Edition) \u2014 mold-remediation","Signature Sump Pump Reliability (Signature Edition) \u2014 mold-remediation","Signature Laundry Moisture Management (Signature Edition) \u2014 mold-remediation","Signature Moisture Meter Use (Signature Edition) \u2014 mold-remediation","Signature Rental Moisture Rights (Signature Edition) \u2014 mold-remediation","Signature When Moisture Means Structure (Signature Edition) \u2014 mold-remediation"]};
var KINDS="home and household-systems record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Moisture and Mold Prevention Signature Database — generated study\n"
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
   + "    print('kind: home and household-systems record')\n"
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
    standards:['home and household-systems record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Moisture and Mold Prevention Signature Database.',
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
var gen={version:'jahdb-moisture-and-mold-prevention-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('moisture-and-mold-prevention-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
