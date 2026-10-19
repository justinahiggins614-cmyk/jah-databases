(function(){'use strict';
/* JAH The Microenterprise Startup Essentials Signature Database generator — jahdb-microenterprise-startup-essentials-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MSE-";
var FIELDS=["lean-setup","first-customers","micro-operations"];
var TOPICS={"lean-setup":["Signature What Is a Microenterprise (Signature Edition) \u2014 lean-setup","Signature Business Licenses and Permits (Signature Edition) \u2014 lean-setup","Signature Pricing Your Work (Signature Edition) \u2014 lean-setup","Signature Tax Basics for Micro (Signature Edition) \u2014 lean-setup","Signature Online Presence Minimum (Signature Edition) \u2014 lean-setup","Signature Time Management Solo (Signature Edition) \u2014 lean-setup","Signature Farmers Market Selling (Signature Edition) \u2014 lean-setup","Signature Food Microbusiness Rules (Signature Edition) \u2014 lean-setup","Signature Failure-Proofing (Signature Edition) \u2014 lean-setup","Signature Work-Life Boundaries (Signature Edition) \u2014 lean-setup","Signature Free Help (SCORE/SBDC) (Signature Edition) \u2014 lean-setup","Signature Separating Personal and Business (Signature Edition) \u2014 lean-setup"],"first-customers":["Signature Sole Proprietorship Basics (Signature Edition) \u2014 first-customers","Signature EIN and Bank Account (Signature Edition) \u2014 first-customers","Signature First 10 Customers (Signature Edition) \u2014 first-customers","Signature Insurance on a Budget (Signature Edition) \u2014 first-customers","Signature Getting Paid (Signature Edition) \u2014 first-customers","Signature When to Hire Help (Signature Edition) \u2014 first-customers","Signature Online Selling Basics (Signature Edition) \u2014 first-customers","Signature Craft Business Basics (Signature Edition) \u2014 first-customers","Signature Knowing Your Numbers (Signature Edition) \u2014 first-customers","Signature Growing Beyond Micro (Signature Edition) \u2014 first-customers","Signature The Annual Micro Review (Signature Edition) \u2014 first-customers"],"micro-operations":["Signature LLC When It Makes Sense (Signature Edition) \u2014 micro-operations","Signature The One-Page Business Plan (Signature Edition) \u2014 micro-operations","Signature Simple Bookkeeping (Signature Edition) \u2014 micro-operations","Signature Home Business Setup (Signature Edition) \u2014 micro-operations","Signature Contracts for Micro Jobs (Signature Edition) \u2014 micro-operations","Signature Micro Funding Sources (Signature Edition) \u2014 micro-operations","Signature Service Business Systems (Signature Edition) \u2014 micro-operations","Signature Consulting Micro-Practice (Signature Edition) \u2014 micro-operations","Signature Customer Service Solo (Signature Edition) \u2014 micro-operations","Signature The Micro Launch Checklist (Signature Edition) \u2014 micro-operations","Signature Business Name and Branding (Signature Edition) \u2014 micro-operations"]};
var KINDS="small-business record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Microenterprise Startup Essentials Signature Database — generated study\n"
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
   + "    print('kind: small-business record')\n"
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
    standards:['small-business record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Microenterprise Startup Essentials Signature Database.',
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
var gen={version:'jahdb-microenterprise-startup-essentials-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('microenterprise-startup-essentials-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
