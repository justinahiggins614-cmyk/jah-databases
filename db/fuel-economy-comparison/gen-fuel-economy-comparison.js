(function(){'use strict';
/* JAH The Fuel Economy Comparison Database generator — jahdb-fuel-economy-comparison-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FEC-";
var FIELDS=["economy-measurement","vehicle-comparison","efficiency-improvement"];
var TOPICS={"economy-measurement":["MPG vs L/100km \u2014 economy-measurement","The Comparison Playbook \u2014 economy-measurement","Hybrid vs Gas Math \u2014 economy-measurement","Tire Pressure Impact \u2014 economy-measurement","Speed and Economy \u2014 economy-measurement","Cruise Control \u2014 economy-measurement","Trip Planning \u2014 economy-measurement","Winter MPG Drop \u2014 economy-measurement","Fuel Apps and Cards \u2014 economy-measurement","Plug-In Hybrid Math \u2014 economy-measurement","Fleet Fuel Management \u2014 economy-measurement","Annual Fuel Review \u2014 economy-measurement"],"vehicle-comparison":["EPA Ratings Explained \u2014 vehicle-comparison","Calculating Your MPG \u2014 vehicle-comparison","EV vs Gas Math \u2014 vehicle-comparison","Weight Impact \u2014 vehicle-comparison","Idling Costs \u2014 vehicle-comparison","Maintenance and MPG \u2014 vehicle-comparison","Fuel Grades \u2014 vehicle-comparison","Comparing Two Cars \u2014 vehicle-comparison","EV Charging Costs \u2014 vehicle-comparison","Motorcycle Economy \u2014 vehicle-comparison","Carbon Per Mile \u2014 vehicle-comparison"],"efficiency-improvement":["Real-World vs Rated \u2014 efficiency-improvement","Fuel Cost Per Mile \u2014 efficiency-improvement","Diesel vs Gas \u2014 efficiency-improvement","Aerodynamics \u2014 efficiency-improvement","AC vs Windows \u2014 efficiency-improvement","Driving Style (Hypermiling) \u2014 efficiency-improvement","Ethanol Blends \u2014 efficiency-improvement","Total Cost of Ownership \u2014 efficiency-improvement","EV Range Reality \u2014 efficiency-improvement","Truck Economy Tips \u2014 efficiency-improvement","The Economy Logbook \u2014 efficiency-improvement"]};
var KINDS="transportation record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Fuel Economy Comparison Database — generated study\n"
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
    name:topic+' — generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['transportation record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Fuel Economy Comparison Database.',
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
var gen={version:'jahdb-fuel-economy-comparison-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('fuel-economy-comparison',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
