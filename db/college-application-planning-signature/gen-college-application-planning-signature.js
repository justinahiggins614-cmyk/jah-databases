(function(){'use strict';
/* JAH The College Application Planning Signature Database generator — jahdb-college-application-planning-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CAP-";
var FIELDS=["application-timeline","essays-and-materials","affordability-strategy"];
var TOPICS={"application-timeline":["Signature The Junior Year Timeline (Signature Edition) \u2014 application-timeline","Signature Early Decision vs Early Action (Signature Edition) \u2014 application-timeline","Signature Supplemental Essays (Signature Edition) \u2014 application-timeline","Signature Counselor Relationship (Signature Edition) \u2014 application-timeline","Signature Demonstrated Interest (Signature Edition) \u2014 application-timeline","Signature Merit Aid Hunting (Signature Edition) \u2014 application-timeline","Signature Comparing Aid Offers (Signature Edition) \u2014 application-timeline","Signature Gap Year Planning (Signature Edition) \u2014 application-timeline","Signature Arts Portfolio Applications (Signature Edition) \u2014 application-timeline","Signature Decision Day: Choosing (Signature Edition) \u2014 application-timeline","Signature Parent Role in Applications (Signature Edition) \u2014 application-timeline","Signature Reapplying After Rejection (Signature Edition) \u2014 application-timeline"],"essays-and-materials":["Signature Building the College List (Signature Edition) \u2014 essays-and-materials","Signature The Common App Master (Signature Edition) \u2014 essays-and-materials","Signature Activities List Optimization (Signature Edition) \u2014 essays-and-materials","Signature SAT/ACT Strategy (Signature Edition) \u2014 essays-and-materials","Signature College Interviews (Signature Edition) \u2014 essays-and-materials","Signature Need-Based Aid Maximization (Signature Edition) \u2014 essays-and-materials","Signature Appealing Aid Decisions (Signature Edition) \u2014 essays-and-materials","Signature Transfer Applications (Signature Edition) \u2014 essays-and-materials","Signature First-Generation Applicants (Signature Edition) \u2014 essays-and-materials","Signature Deferring Admission (Signature Edition) \u2014 essays-and-materials","Signature Senior Year Spring Checklist (Signature Edition) \u2014 essays-and-materials"],"affordability-strategy":["Signature Safety Schools Done Right (Signature Edition) \u2014 affordability-strategy","Signature Personal Statement Architecture (Signature Edition) \u2014 affordability-strategy","Signature Recommendation Letters (Signature Edition) \u2014 affordability-strategy","Signature Test-Optional Decisions (Signature Edition) \u2014 affordability-strategy","Signature Net Price Calculators (Signature Edition) \u2014 affordability-strategy","Signature The CSS Profile (Signature Edition) \u2014 affordability-strategy","Signature Waitlist Strategy (Signature Edition) \u2014 affordability-strategy","Signature Athletic Recruiting (Signature Edition) \u2014 affordability-strategy","Signature Application Fee Waivers (Signature Edition) \u2014 affordability-strategy","Signature The Application Tracker (Signature Edition) \u2014 affordability-strategy","Signature Summer Before College (Signature Edition) \u2014 affordability-strategy"]};
var KINDS="education and learning record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The College Application Planning Signature Database — generated study\n"
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
   + "    print('kind: education and learning record')\n"
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
    standards:['education and learning record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The College Application Planning Signature Database.',
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
var gen={version:'jahdb-college-application-planning-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('college-application-planning-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
