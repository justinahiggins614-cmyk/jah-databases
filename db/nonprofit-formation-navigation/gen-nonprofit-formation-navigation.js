(function(){'use strict';
/* JAH The Nonprofit Formation Navigation Database generator — jahdb-nonprofit-formation-navigation-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NFN-";
var FIELDS=["formation-steps","tax-exemption","compliant-operations"];
var TOPICS={"formation-steps":["Is Nonprofit Right? \u2014 formation-steps","EIN Application \u2014 formation-steps","Form 1023 (Tax Exemption) \u2014 formation-steps","Conflict of Interest Policy \u2014 formation-steps","Donation Receipting \u2014 formation-steps","Lobbying Limits (c3) \u2014 formation-steps","Dissolution Planning \u2014 formation-steps","Mission Statement Craft \u2014 formation-steps","Donor Stewardship Basics \u2014 formation-steps","Executive Director Hiring \u2014 formation-steps","The First-Year Checklist \u2014 formation-steps","Record Retention Schedule \u2014 formation-steps"],"tax-exemption":["Choosing a Legal Structure \u2014 tax-exemption","Bylaws Drafting \u2014 tax-exemption","State Tax Exemptions \u2014 tax-exemption","Financial Controls \u2014 tax-exemption","Fundraising Compliance \u2014 tax-exemption","Employment Law for Nonprofits \u2014 tax-exemption","Insurance for Nonprofits \u2014 tax-exemption","Strategic Planning Lite \u2014 tax-exemption","Program Evaluation \u2014 tax-exemption","Board Meetings That Work \u2014 tax-exemption","Pro Bono Legal Help \u2014 tax-exemption"],"compliant-operations":["State Incorporation \u2014 compliant-operations","Board Recruitment \u2014 compliant-operations","Charitable Solicitation Registration \u2014 compliant-operations","Form 990 Filing \u2014 compliant-operations","Unrelated Business Income (UBI) \u2014 compliant-operations","Fiscal Sponsorship Alternative \u2014 compliant-operations","Grant Readiness \u2014 compliant-operations","Volunteer Management \u2014 compliant-operations","Financial Transparency \u2014 compliant-operations","Avoiding Common Pitfalls \u2014 compliant-operations","Merging or Partnering \u2014 compliant-operations"]};
var KINDS="law and rights record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Nonprofit Formation Navigation Database — generated study\n"
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
    provenance:'Generated structural sample for the The Nonprofit Formation Navigation Database.',
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
var gen={version:'jahdb-nonprofit-formation-navigation-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('nonprofit-formation-navigation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
