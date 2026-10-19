(function(){'use strict';
/* JAH The Blindness Navigation Resources Database generator — jahdb-blindness-navigation-resources-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BNR-";
var FIELDS=["orientation-and-mobility","assistive-navigation-tech","independent-travel"];
var TOPICS={"orientation-and-mobility":["Orientation and Mobility \u2014 orientation-and-mobility","The Navigation Playbook \u2014 orientation-and-mobility","Public Transit \u2014 orientation-and-mobility","Street Crossing \u2014 orientation-and-mobility","Braille Signage \u2014 orientation-and-mobility","Traveling Alone \u2014 orientation-and-mobility","Shopping Independently \u2014 orientation-and-mobility","Self-Defense \u2014 orientation-and-mobility","Hiking and Outdoors \u2014 orientation-and-mobility","Peer Mentoring \u2014 orientation-and-mobility","Children's Mobility \u2014 orientation-and-mobility","The Independent Traveler \u2014 orientation-and-mobility"],"assistive-navigation-tech":["Guide Dogs \u2014 assistive-navigation-tech","Cane Techniques \u2014 assistive-navigation-tech","Rideshare Access \u2014 assistive-navigation-tech","Indoor Navigation \u2014 assistive-navigation-tech","Tactile Maps \u2014 assistive-navigation-tech","Hotel Navigation \u2014 assistive-navigation-tech","Currency Identification \u2014 assistive-navigation-tech","Guide Dog Travel \u2014 assistive-navigation-tech","Sports and Fitness \u2014 assistive-navigation-tech","Advocacy (NFB/ACB) \u2014 assistive-navigation-tech","College Campus Nav \u2014 assistive-navigation-tech"],"independent-travel":["Smartphone Navigation \u2014 independent-travel","GPS Apps (Blind) \u2014 independent-travel","Airport Navigation (Blind) \u2014 independent-travel","Aira and Be My Eyes \u2014 independent-travel","Echolocation Basics \u2014 independent-travel","Restaurant Navigation \u2014 independent-travel","Emergency Preparedness \u2014 independent-travel","International Travel \u2014 independent-travel","Tech Training Centers \u2014 independent-travel","Newly Blind Adjustment \u2014 independent-travel","Workplace Navigation \u2014 independent-travel"]};
var KINDS="accessibility record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Blindness Navigation Resources Database — generated study\n"
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
   + "    print('kind: accessibility record')\n"
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
    standards:['accessibility record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Blindness Navigation Resources Database.',
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
var gen={version:'jahdb-blindness-navigation-resources-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('blindness-navigation-resources',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
