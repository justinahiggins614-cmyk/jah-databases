(function(){'use strict';
/* JAH The Crisis Support Navigation Database generator — jahdb-crisis-support-navigation-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CSN-";
var FIELDS=["crisis-helplines","support-navigation","safety-planning"];
var TOPICS={"crisis-helplines":["988 Suicide and Crisis Lifeline \u2014 crisis-helplines","Helping Someone in Crisis \u2014 crisis-helplines","Warning Signs to Know \u2014 crisis-helplines","Veterans Crisis Line \u2014 crisis-helplines","Eating Disorder Support \u2014 crisis-helplines","Grief Crisis Support \u2014 crisis-helplines","School Crisis Teams \u2014 crisis-helplines","Supporting a Friend Long-Term \u2014 crisis-helplines","What to Say (and Not Say) \u2014 crisis-helplines","Recovering After Crisis \u2014 crisis-helplines","The Hope Kit \u2014 crisis-helplines","Crisis De-escalation Basics \u2014 crisis-helplines"],"support-navigation":["Crisis Text Line (741741) \u2014 support-navigation","Safety Planning \u2014 support-navigation","After a Suicide Loss \u2014 support-navigation","Domestic Violence Hotline \u2014 support-navigation","LGBTQ+ Crisis Support \u2014 support-navigation","Financial Crisis and Suicide Risk \u2014 support-navigation","Faith Community Support \u2014 support-navigation","Crisis Support for Men \u2014 support-navigation","Creating a Support Network Map \u2014 support-navigation","Becoming a Crisis Volunteer \u2014 support-navigation","Checking In On Strong Friends \u2014 support-navigation"],"safety-planning":["When to Call 911 vs 988 \u2014 safety-planning","Means Restriction \u2014 safety-planning","Teen Crisis Resources \u2014 safety-planning","Substance Crisis Help \u2014 safety-planning","Postpartum Crisis Help \u2014 safety-planning","Workplace Crisis Resources \u2014 safety-planning","Crisis After Natural Disaster \u2014 safety-planning","Crisis Support for Seniors \u2014 safety-planning","Crisis Planning for Families \u2014 safety-planning","Workplace Postvention \u2014 safety-planning","Crisis Resource Wallet Card \u2014 safety-planning"]};
var KINDS="health-information record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Crisis Support Navigation Database — generated study\n"
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
   + "    print('kind: health-information record')\n"
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
    standards:['health-information record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Crisis Support Navigation Database.',
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
var gen={version:'jahdb-crisis-support-navigation-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('crisis-support-navigation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
