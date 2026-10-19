(function(){'use strict';
/* JAH The Airport Navigation Signature Database generator — jahdb-airport-navigation-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AN-";
var FIELDS=["terminal-navigation","connection-management","airport-services"];
var TOPICS={"terminal-navigation":["Signature Reading Airport Signs (Signature Edition) \u2014 terminal-navigation","Signature The Connection Playbook (Signature Edition) \u2014 terminal-navigation","Signature Customs and Immigration (Signature Edition) \u2014 terminal-navigation","Signature Airport Lounges (Signature Edition) \u2014 terminal-navigation","Signature Airport Food Strategy (Signature Edition) \u2014 terminal-navigation","Signature Flight Delay Rights (Signature Edition) \u2014 terminal-navigation","Signature International Terminals (Signature Edition) \u2014 terminal-navigation","Signature Pet Travel in Airports (Signature Edition) \u2014 terminal-navigation","Signature SIM Cards at Airports (Signature Edition) \u2014 terminal-navigation","Signature Rideshare Pickup Zones (Signature Edition) \u2014 terminal-navigation","Signature The Airport Cheat Sheet (Signature Edition) \u2014 terminal-navigation","Signature Enjoying the Airport (Signature Edition) \u2014 terminal-navigation"],"connection-management":["Signature Arrival Time Rules (Signature Edition) \u2014 connection-management","Signature Terminal Maps (Signature Edition) \u2014 connection-management","Signature Baggage Claim (Signature Edition) \u2014 connection-management","Signature Layover City Tours (Signature Edition) \u2014 connection-management","Signature Wi-Fi and Power (Signature Edition) \u2014 connection-management","Signature TSA PreCheck/Global Entry (Signature Edition) \u2014 connection-management","Signature Airport Accessibility (Signature Edition) \u2014 connection-management","Signature Duty-Free: Deals? (Signature Edition) \u2014 connection-management","Signature Airport Hotels (Signature Edition) \u2014 connection-management","Signature Parking at Airports (Signature Edition) \u2014 connection-management","Signature New Airport Recon (Signature Edition) \u2014 connection-management"],"airport-services":["Signature Security Line Strategy (Signature Edition) \u2014 airport-services","Signature Gate Changes (Signature Edition) \u2014 airport-services","Signature Ground Transport (Signature Edition) \u2014 airport-services","Signature Sleeping in Airports (Signature Edition) \u2014 airport-services","Signature Missed Connection Recovery (Signature Edition) \u2014 airport-services","Signature CLEAR: Worth It? (Signature Edition) \u2014 airport-services","Signature Traveling with Kids (Signature Edition) \u2014 airport-services","Signature Currency Exchange (Signature Edition) \u2014 airport-services","Signature Rental Cars at Airports (Signature Edition) \u2014 airport-services","Signature Drop-Off Strategy (Signature Edition) \u2014 airport-services","Signature Airport Emergency Contacts (Signature Edition) \u2014 airport-services"]};
var KINDS="transportation record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Airport Navigation Signature Database — generated study\n"
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
    provenance:'Generated structural sample for the The Airport Navigation Signature Database.',
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
var gen={version:'jahdb-airport-navigation-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('airport-navigation-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
