(function(){'use strict';
/* JAH The Fastener and Joint Reference Database generator — jahdb-fastener-and-joint-reference-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FJR-";
var FIELDS=["fastener-selection","joint-design","assembly-practice"];
var TOPICS={"fastener-selection":["Bolt Grades Explained \u2014 fastener-selection","Torque Specs \u2014 fastener-selection","Welding Basics \u2014 fastener-selection","The Fastener Playbook \u2014 fastener-selection","Set Screws \u2014 fastener-selection","Wood Screws \u2014 fastener-selection","Pins and Retaining \u2014 fastener-selection","Keyways and Keys \u2014 fastener-selection","Rivet Nuts \u2014 fastener-selection","Weld Symbols \u2014 fastener-selection","Corrosion and Fasteners \u2014 fastener-selection","The Joint Design Checklist \u2014 fastener-selection"],"joint-design":["Metric Bolt Classes \u2014 joint-design","Locking Methods \u2014 joint-design","Adhesive Bonding \u2014 joint-design","Washers: When and Why \u2014 joint-design","Self-Tapping Screws \u2014 joint-design","Anchors (Concrete/Masonry) \u2014 joint-design","Snap Fits \u2014 joint-design","Splines \u2014 joint-design","Clevis and Pins \u2014 joint-design","Bolted Joint Design \u2014 joint-design","Stainless Fasteners \u2014 joint-design"],"assembly-practice":["Thread Types \u2014 assembly-practice","Rivets \u2014 assembly-practice","Screws vs Bolts \u2014 assembly-practice","Nuts: Types \u2014 assembly-practice","Machine Screws \u2014 assembly-practice","Drywall Anchors \u2014 assembly-practice","Press Fits \u2014 assembly-practice","Threaded Inserts \u2014 assembly-practice","Ball Joints \u2014 assembly-practice","Fatigue in Fasteners \u2014 assembly-practice","Fastener Inspection \u2014 assembly-practice"]};
var KINDS="engineering record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Fastener and Joint Reference Database — generated study\n"
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
   + "    print('kind: engineering record')\n"
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
    standards:['engineering record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Fastener and Joint Reference Database.',
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
var gen={version:'jahdb-fastener-and-joint-reference-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('fastener-and-joint-reference',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
