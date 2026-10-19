(function(){'use strict';
/* JAH The College Application Planning Database generator — jahdb-college-application-planning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CAP-";
var FIELDS=["application-timeline","essays-and-materials","affordability-strategy"];
var TOPICS={"application-timeline":["The Junior Year Timeline \u2014 application-timeline","Early Decision vs Early Action \u2014 application-timeline","Supplemental Essays \u2014 application-timeline","Counselor Relationship \u2014 application-timeline","Demonstrated Interest \u2014 application-timeline","Merit Aid Hunting \u2014 application-timeline","Comparing Aid Offers \u2014 application-timeline","Gap Year Planning \u2014 application-timeline","Arts Portfolio Applications \u2014 application-timeline","Decision Day: Choosing \u2014 application-timeline","Parent Role in Applications \u2014 application-timeline","Reapplying After Rejection \u2014 application-timeline"],"essays-and-materials":["Building the College List \u2014 essays-and-materials","The Common App Master \u2014 essays-and-materials","Activities List Optimization \u2014 essays-and-materials","SAT/ACT Strategy \u2014 essays-and-materials","College Interviews \u2014 essays-and-materials","Need-Based Aid Maximization \u2014 essays-and-materials","Appealing Aid Decisions \u2014 essays-and-materials","Transfer Applications \u2014 essays-and-materials","First-Generation Applicants \u2014 essays-and-materials","Deferring Admission \u2014 essays-and-materials","Senior Year Spring Checklist \u2014 essays-and-materials"],"affordability-strategy":["Safety Schools Done Right \u2014 affordability-strategy","Personal Statement Architecture \u2014 affordability-strategy","Recommendation Letters \u2014 affordability-strategy","Test-Optional Decisions \u2014 affordability-strategy","Net Price Calculators \u2014 affordability-strategy","The CSS Profile \u2014 affordability-strategy","Waitlist Strategy \u2014 affordability-strategy","Athletic Recruiting \u2014 affordability-strategy","Application Fee Waivers \u2014 affordability-strategy","The Application Tracker \u2014 affordability-strategy","Summer Before College \u2014 affordability-strategy"]};
var KINDS="education and learning record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The College Application Planning Database — generated study\n"
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
    name:topic+' — generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['education and learning record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The College Application Planning Database.',
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
var gen={version:'jahdb-college-application-planning-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('college-application-planning',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
