(function(){'use strict';
/* JAH The Fuel Economy Comparison Signature Database generator — jahdb-fuel-economy-comparison-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FEC-";
var FIELDS=["economy-measurement","vehicle-comparison","efficiency-improvement"];
var TOPICS={"economy-measurement":["Signature MPG vs L/100km (Signature Edition) \u2014 economy-measurement","Signature The Comparison Playbook (Signature Edition) \u2014 economy-measurement","Signature Hybrid vs Gas Math (Signature Edition) \u2014 economy-measurement","Signature Tire Pressure Impact (Signature Edition) \u2014 economy-measurement","Signature Speed and Economy (Signature Edition) \u2014 economy-measurement","Signature Cruise Control (Signature Edition) \u2014 economy-measurement","Signature Trip Planning (Signature Edition) \u2014 economy-measurement","Signature Winter MPG Drop (Signature Edition) \u2014 economy-measurement","Signature Fuel Apps and Cards (Signature Edition) \u2014 economy-measurement","Signature Plug-In Hybrid Math (Signature Edition) \u2014 economy-measurement","Signature Fleet Fuel Management (Signature Edition) \u2014 economy-measurement","Signature Annual Fuel Review (Signature Edition) \u2014 economy-measurement"],"vehicle-comparison":["Signature EPA Ratings Explained (Signature Edition) \u2014 vehicle-comparison","Signature Calculating Your MPG (Signature Edition) \u2014 vehicle-comparison","Signature EV vs Gas Math (Signature Edition) \u2014 vehicle-comparison","Signature Weight Impact (Signature Edition) \u2014 vehicle-comparison","Signature Idling Costs (Signature Edition) \u2014 vehicle-comparison","Signature Maintenance and MPG (Signature Edition) \u2014 vehicle-comparison","Signature Fuel Grades (Signature Edition) \u2014 vehicle-comparison","Signature Comparing Two Cars (Signature Edition) \u2014 vehicle-comparison","Signature EV Charging Costs (Signature Edition) \u2014 vehicle-comparison","Signature Motorcycle Economy (Signature Edition) \u2014 vehicle-comparison","Signature Carbon Per Mile (Signature Edition) \u2014 vehicle-comparison"],"efficiency-improvement":["Signature Real-World vs Rated (Signature Edition) \u2014 efficiency-improvement","Signature Fuel Cost Per Mile (Signature Edition) \u2014 efficiency-improvement","Signature Diesel vs Gas (Signature Edition) \u2014 efficiency-improvement","Signature Aerodynamics (Signature Edition) \u2014 efficiency-improvement","Signature AC vs Windows (Signature Edition) \u2014 efficiency-improvement","Signature Driving Style (Hypermiling) (Signature Edition) \u2014 efficiency-improvement","Signature Ethanol Blends (Signature Edition) \u2014 efficiency-improvement","Signature Total Cost of Ownership (Signature Edition) \u2014 efficiency-improvement","Signature EV Range Reality (Signature Edition) \u2014 efficiency-improvement","Signature Truck Economy Tips (Signature Edition) \u2014 efficiency-improvement","Signature The Economy Logbook (Signature Edition) \u2014 efficiency-improvement"]};
var KINDS="transportation record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Fuel Economy Comparison Signature Database — generated study\n"
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
   + "    print('kind: transportation record')\n"
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
    standards:['transportation record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Fuel Economy Comparison Signature Database.',
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
var gen={version:'jahdb-fuel-economy-comparison-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('fuel-economy-comparison-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
