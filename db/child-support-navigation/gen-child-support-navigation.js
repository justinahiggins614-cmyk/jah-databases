(function(){'use strict';
/* JAH The Child Support Navigation Database generator — jahdb-child-support-navigation-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CSUP-";
var FIELDS=["establishing-orders","payments-and-enforcement","modifications"];
var TOPICS={"establishing-orders":["How Child Support Is Calculated \u2014 establishing-orders","Income Withholding Orders \u2014 establishing-orders","Enforcement Tools \u2014 establishing-orders","Self-Employment Income \u2014 establishing-orders","College Expense Provisions \u2014 establishing-orders","Military Parent Support \u2014 establishing-orders","Tax and Support \u2014 establishing-orders","When the Other Parent Won't Pay \u2014 establishing-orders","Emancipation and Termination \u2014 establishing-orders","Mediation for Support Disputes \u2014 establishing-orders","The Annual Support Review \u2014 establishing-orders","Support Order Portability \u2014 establishing-orders"],"payments-and-enforcement":["Establishing an Order \u2014 payments-and-enforcement","Paying on Time Systems \u2014 payments-and-enforcement","Modifying an Order \u2014 payments-and-enforcement","Health Insurance Requirements \u2014 payments-and-enforcement","Custody Time and Support \u2014 payments-and-enforcement","Incarcerated Parents \u2014 payments-and-enforcement","Keeping Records \u2014 payments-and-enforcement","When You Can't Afford to Pay \u2014 payments-and-enforcement","Grandparent and Third-Party Cases \u2014 payments-and-enforcement","Free Help Resources \u2014 payments-and-enforcement","Explaining Support to Kids \u2014 payments-and-enforcement"],"modifications":["Paternity Establishment \u2014 modifications","Receiving: Tracking Payments \u2014 modifications","Job Loss and Support \u2014 modifications","Childcare Cost Sharing \u2014 modifications","Interstate Orders (UIFSA) \u2014 modifications","Arrears Management \u2014 modifications","Communication Between Parents \u2014 modifications","Support and New Families \u2014 modifications","Domestic Violence Safeguards \u2014 modifications","Common Mistakes to Avoid \u2014 modifications","Building a Co-Parenting Plan \u2014 modifications"]};
var KINDS="law and rights record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Child Support Navigation Database — generated study\n"
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
   + "    print('kind: law and rights record')\n"
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
    standards:['law and rights record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Child Support Navigation Database.',
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
var gen={version:'jahdb-child-support-navigation-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('child-support-navigation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
