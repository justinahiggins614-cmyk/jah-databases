(function(){'use strict';
/* JAH The Microenterprise Startup Essentials Database generator — jahdb-microenterprise-startup-essentials-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MSE-";
var FIELDS=["lean-setup","first-customers","micro-operations"];
var TOPICS={"lean-setup":["What Is a Microenterprise \u2014 lean-setup","Business Licenses and Permits \u2014 lean-setup","Pricing Your Work \u2014 lean-setup","Tax Basics for Micro \u2014 lean-setup","Online Presence Minimum \u2014 lean-setup","Time Management Solo \u2014 lean-setup","Farmers Market Selling \u2014 lean-setup","Food Microbusiness Rules \u2014 lean-setup","Failure-Proofing \u2014 lean-setup","Work-Life Boundaries \u2014 lean-setup","Free Help (SCORE/SBDC) \u2014 lean-setup","Separating Personal and Business \u2014 lean-setup"],"first-customers":["Sole Proprietorship Basics \u2014 first-customers","EIN and Bank Account \u2014 first-customers","First 10 Customers \u2014 first-customers","Insurance on a Budget \u2014 first-customers","Getting Paid \u2014 first-customers","When to Hire Help \u2014 first-customers","Online Selling Basics \u2014 first-customers","Craft Business Basics \u2014 first-customers","Knowing Your Numbers \u2014 first-customers","Growing Beyond Micro \u2014 first-customers","The Annual Micro Review \u2014 first-customers"],"micro-operations":["LLC When It Makes Sense \u2014 micro-operations","The One-Page Business Plan \u2014 micro-operations","Simple Bookkeeping \u2014 micro-operations","Home Business Setup \u2014 micro-operations","Contracts for Micro Jobs \u2014 micro-operations","Micro Funding Sources \u2014 micro-operations","Service Business Systems \u2014 micro-operations","Consulting Micro-Practice \u2014 micro-operations","Customer Service Solo \u2014 micro-operations","The Micro Launch Checklist \u2014 micro-operations","Business Name and Branding \u2014 micro-operations"]};
var KINDS="small-business record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Microenterprise Startup Essentials Database — generated study\n"
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
    name:topic+' — generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['small-business record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Microenterprise Startup Essentials Database.',
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
var gen={version:'jahdb-microenterprise-startup-essentials-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('microenterprise-startup-essentials',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
