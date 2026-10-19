(function(){'use strict';
/* JAH The Child Support Navigation Signature Database generator — jahdb-child-support-navigation-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CSUP-";
var FIELDS=["establishing-orders","payments-and-enforcement","modifications"];
var TOPICS={"establishing-orders":["Signature How Child Support Is Calculated (Signature Edition) \u2014 establishing-orders","Signature Income Withholding Orders (Signature Edition) \u2014 establishing-orders","Signature Enforcement Tools (Signature Edition) \u2014 establishing-orders","Signature Self-Employment Income (Signature Edition) \u2014 establishing-orders","Signature College Expense Provisions (Signature Edition) \u2014 establishing-orders","Signature Military Parent Support (Signature Edition) \u2014 establishing-orders","Signature Tax and Support (Signature Edition) \u2014 establishing-orders","Signature When the Other Parent Won't Pay (Signature Edition) \u2014 establishing-orders","Signature Emancipation and Termination (Signature Edition) \u2014 establishing-orders","Signature Mediation for Support Disputes (Signature Edition) \u2014 establishing-orders","Signature The Annual Support Review (Signature Edition) \u2014 establishing-orders","Signature Support Order Portability (Signature Edition) \u2014 establishing-orders"],"payments-and-enforcement":["Signature Establishing an Order (Signature Edition) \u2014 payments-and-enforcement","Signature Paying on Time Systems (Signature Edition) \u2014 payments-and-enforcement","Signature Modifying an Order (Signature Edition) \u2014 payments-and-enforcement","Signature Health Insurance Requirements (Signature Edition) \u2014 payments-and-enforcement","Signature Custody Time and Support (Signature Edition) \u2014 payments-and-enforcement","Signature Incarcerated Parents (Signature Edition) \u2014 payments-and-enforcement","Signature Keeping Records (Signature Edition) \u2014 payments-and-enforcement","Signature When You Can't Afford to Pay (Signature Edition) \u2014 payments-and-enforcement","Signature Grandparent and Third-Party Cases (Signature Edition) \u2014 payments-and-enforcement","Signature Free Help Resources (Signature Edition) \u2014 payments-and-enforcement","Signature Explaining Support to Kids (Signature Edition) \u2014 payments-and-enforcement"],"modifications":["Signature Paternity Establishment (Signature Edition) \u2014 modifications","Signature Receiving: Tracking Payments (Signature Edition) \u2014 modifications","Signature Job Loss and Support (Signature Edition) \u2014 modifications","Signature Childcare Cost Sharing (Signature Edition) \u2014 modifications","Signature Interstate Orders (UIFSA) (Signature Edition) \u2014 modifications","Signature Arrears Management (Signature Edition) \u2014 modifications","Signature Communication Between Parents (Signature Edition) \u2014 modifications","Signature Support and New Families (Signature Edition) \u2014 modifications","Signature Domestic Violence Safeguards (Signature Edition) \u2014 modifications","Signature Common Mistakes to Avoid (Signature Edition) \u2014 modifications","Signature Building a Co-Parenting Plan (Signature Edition) \u2014 modifications"]};
var KINDS="law and rights record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Child Support Navigation Signature Database — generated study\n"
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
    name:topic+' — Signature generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural Signature sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['law and rights record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Child Support Navigation Signature Database.',
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
var gen={version:'jahdb-child-support-navigation-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('child-support-navigation-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
