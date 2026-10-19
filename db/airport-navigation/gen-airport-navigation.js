(function(){'use strict';
/* JAH The Airport Navigation Database generator — jahdb-airport-navigation-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AN-";
var FIELDS=["terminal-navigation","connection-management","airport-services"];
var TOPICS={"terminal-navigation":["Reading Airport Signs \u2014 terminal-navigation","The Connection Playbook \u2014 terminal-navigation","Customs and Immigration \u2014 terminal-navigation","Airport Lounges \u2014 terminal-navigation","Airport Food Strategy \u2014 terminal-navigation","Flight Delay Rights \u2014 terminal-navigation","International Terminals \u2014 terminal-navigation","Pet Travel in Airports \u2014 terminal-navigation","SIM Cards at Airports \u2014 terminal-navigation","Rideshare Pickup Zones \u2014 terminal-navigation","The Airport Cheat Sheet \u2014 terminal-navigation","Enjoying the Airport \u2014 terminal-navigation"],"connection-management":["Arrival Time Rules \u2014 connection-management","Terminal Maps \u2014 connection-management","Baggage Claim \u2014 connection-management","Layover City Tours \u2014 connection-management","Wi-Fi and Power \u2014 connection-management","TSA PreCheck/Global Entry \u2014 connection-management","Airport Accessibility \u2014 connection-management","Duty-Free: Deals? \u2014 connection-management","Airport Hotels \u2014 connection-management","Parking at Airports \u2014 connection-management","New Airport Recon \u2014 connection-management"],"airport-services":["Security Line Strategy \u2014 airport-services","Gate Changes \u2014 airport-services","Ground Transport \u2014 airport-services","Sleeping in Airports \u2014 airport-services","Missed Connection Recovery \u2014 airport-services","CLEAR: Worth It? \u2014 airport-services","Traveling with Kids \u2014 airport-services","Currency Exchange \u2014 airport-services","Rental Cars at Airports \u2014 airport-services","Drop-Off Strategy \u2014 airport-services","Airport Emergency Contacts \u2014 airport-services"]};
var KINDS="transportation record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Airport Navigation Database — generated study\n"
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
    provenance:'Generated structural sample for the The Airport Navigation Database.',
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
var gen={version:'jahdb-airport-navigation-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('airport-navigation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
