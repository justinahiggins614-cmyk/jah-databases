(function(){'use strict';
/* JAH The Accessible Employment Services Database generator — jahdb-accessible-employment-services-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-AES-";
var FIELDS=["accommodation-rights","employment-services","career-advancement"];
var TOPICS={"accommodation-rights":["ADA Employment Rights \u2014 accommodation-rights","The Employment Playbook \u2014 accommodation-rights","Disclosure at Work \u2014 accommodation-rights","Ticket to Work \u2014 accommodation-rights","Benefits Counseling \u2014 accommodation-rights","Self-Employment (Disability) \u2014 accommodation-rights","Remote Work Access \u2014 accommodation-rights","Paratransit Commutes \u2014 accommodation-rights","Career Ladders \u2014 accommodation-rights","Gig Work Access \u2014 accommodation-rights","Emergency Evacuation \u2014 accommodation-rights","The Access Employment Map \u2014 accommodation-rights"],"employment-services":["Requesting Accommodations \u2014 employment-services","Reasonable Accommodation Examples \u2014 employment-services","Interview Rights \u2014 employment-services","PASS Plans \u2014 employment-services","Customized Employment \u2014 employment-services","Federal Hiring (Schedule A) \u2014 employment-services","Assistive Tech at Work \u2014 employment-services","Dealing with Denials \u2014 employment-services","Mentorship \u2014 employment-services","Financial Literacy \u2014 employment-services","Annual Career Review \u2014 employment-services"],"career-advancement":["Vocational Rehabilitation \u2014 career-advancement","JAN (Job Accommodation Network) \u2014 career-advancement","American Job Centers (Disability) \u2014 career-advancement","IRWE \u2014 career-advancement","Supported Employment \u2014 career-advancement","Disability:IN \u2014 career-advancement","Service Animals at Work \u2014 career-advancement","EEOC Process \u2014 career-advancement","Entrepreneurship \u2014 career-advancement","Workplace Culture \u2014 career-advancement","Success Stories \u2014 career-advancement"]};
var KINDS="accessibility record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Accessible Employment Services Database — generated study\n"
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
    provenance:'Generated structural sample for the The Accessible Employment Services Database.',
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
var gen={version:'jahdb-accessible-employment-services-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('accessible-employment-services',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
