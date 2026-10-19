(function(){'use strict';
/* JAH The Blindness Navigation Resources Signature Database generator — jahdb-blindness-navigation-resources-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BNR-";
var FIELDS=["orientation-and-mobility","assistive-navigation-tech","independent-travel"];
var TOPICS={"orientation-and-mobility":["Signature Orientation and Mobility (Signature Edition) \u2014 orientation-and-mobility","Signature The Navigation Playbook (Signature Edition) \u2014 orientation-and-mobility","Signature Public Transit (Signature Edition) \u2014 orientation-and-mobility","Signature Street Crossing (Signature Edition) \u2014 orientation-and-mobility","Signature Braille Signage (Signature Edition) \u2014 orientation-and-mobility","Signature Traveling Alone (Signature Edition) \u2014 orientation-and-mobility","Signature Shopping Independently (Signature Edition) \u2014 orientation-and-mobility","Signature Self-Defense (Signature Edition) \u2014 orientation-and-mobility","Signature Hiking and Outdoors (Signature Edition) \u2014 orientation-and-mobility","Signature Peer Mentoring (Signature Edition) \u2014 orientation-and-mobility","Signature Children's Mobility (Signature Edition) \u2014 orientation-and-mobility","Signature The Independent Traveler (Signature Edition) \u2014 orientation-and-mobility"],"assistive-navigation-tech":["Signature Guide Dogs (Signature Edition) \u2014 assistive-navigation-tech","Signature Cane Techniques (Signature Edition) \u2014 assistive-navigation-tech","Signature Rideshare Access (Signature Edition) \u2014 assistive-navigation-tech","Signature Indoor Navigation (Signature Edition) \u2014 assistive-navigation-tech","Signature Tactile Maps (Signature Edition) \u2014 assistive-navigation-tech","Signature Hotel Navigation (Signature Edition) \u2014 assistive-navigation-tech","Signature Currency Identification (Signature Edition) \u2014 assistive-navigation-tech","Signature Guide Dog Travel (Signature Edition) \u2014 assistive-navigation-tech","Signature Sports and Fitness (Signature Edition) \u2014 assistive-navigation-tech","Signature Advocacy (NFB/ACB) (Signature Edition) \u2014 assistive-navigation-tech","Signature College Campus Nav (Signature Edition) \u2014 assistive-navigation-tech"],"independent-travel":["Signature Smartphone Navigation (Signature Edition) \u2014 independent-travel","Signature GPS Apps (Blind) (Signature Edition) \u2014 independent-travel","Signature Airport Navigation (Blind) (Signature Edition) \u2014 independent-travel","Signature Aira and Be My Eyes (Signature Edition) \u2014 independent-travel","Signature Echolocation Basics (Signature Edition) \u2014 independent-travel","Signature Restaurant Navigation (Signature Edition) \u2014 independent-travel","Signature Emergency Preparedness (Signature Edition) \u2014 independent-travel","Signature International Travel (Signature Edition) \u2014 independent-travel","Signature Tech Training Centers (Signature Edition) \u2014 independent-travel","Signature Newly Blind Adjustment (Signature Edition) \u2014 independent-travel","Signature Workplace Navigation (Signature Edition) \u2014 independent-travel"]};
var KINDS="accessibility record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Blindness Navigation Resources Signature Database — generated study\n"
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
    name:topic+' — Signature generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural Signature sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['accessibility record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Blindness Navigation Resources Signature Database.',
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
var gen={version:'jahdb-blindness-navigation-resources-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('blindness-navigation-resources-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
