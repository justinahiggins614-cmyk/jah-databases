(function(){'use strict';
/* JAH The Research Funding Directory Signature Database generator — jahdb-research-funding-directory-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RFD-";
var FIELDS=["funding-sources","proposal-craft","grant-management"];
var TOPICS={"funding-sources":["Signature Federal Grant Landscape (Signature Edition) \u2014 funding-sources","Signature Foundation Funding (Signature Edition) \u2014 funding-sources","Signature Writing Winning Proposals (Signature Edition) \u2014 funding-sources","Signature Broader Impacts (NSF) (Signature Edition) \u2014 funding-sources","Signature The Funding Playbook (Signature Edition) \u2014 funding-sources","Signature USDA/NIFA Funding (Signature Edition) \u2014 funding-sources","Signature Crowdfunding Science (Signature Edition) \u2014 funding-sources","Signature Graduate Funding (Signature Edition) \u2014 funding-sources","Signature Conference/Travel Grants (Signature Edition) \u2014 funding-sources","Signature LOI and Pre-proposals (Signature Edition) \u2014 funding-sources","Signature Collaboration Plans (Signature Edition) \u2014 funding-sources","Signature Funding Ethics (Signature Edition) \u2014 funding-sources"],"proposal-craft":["Signature NIH Grant Types (Signature Edition) \u2014 proposal-craft","Signature Fellowships (Signature Edition) \u2014 proposal-craft","Signature Specific Aims Page (Signature Edition) \u2014 proposal-craft","Signature Resubmission Strategy (Signature Edition) \u2014 proposal-craft","Signature DOE Office of Science (Signature Edition) \u2014 proposal-craft","Signature International Funding (Signature Edition) \u2014 proposal-craft","Signature Early-Career Awards (Signature Edition) \u2014 proposal-craft","Signature Undergraduate Research (Signature Edition) \u2014 proposal-craft","Signature Finding Calls (Signature Edition) \u2014 proposal-craft","Signature Review Process Demystified (Signature Edition) \u2014 proposal-craft","Signature Data Management Plans (Signature Edition) \u2014 proposal-craft"],"grant-management":["Signature NSF Programs (Signature Edition) \u2014 grant-management","Signature Small Business (SBIR/STTR) (Signature Edition) \u2014 grant-management","Signature Budget Building (Signature Edition) \u2014 grant-management","Signature Grant Management (Signature Edition) \u2014 grant-management","Signature DOD Research (DARPA etc.) (Signature Edition) \u2014 grant-management","Signature Corporate Research Funding (Signature Edition) \u2014 grant-management","Signature Postdoc Fellowships (Signature Edition) \u2014 grant-management","Signature Equipment Grants (Signature Edition) \u2014 grant-management","Signature Eligibility Checks (Signature Edition) \u2014 grant-management","Signature Responding to Reviews (Signature Edition) \u2014 grant-management","Signature Compliance (IRB/IACUC) (Signature Edition) \u2014 grant-management"]};
var KINDS="science and research record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Research Funding Directory Signature Database — generated study\n"
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
   + "    print('kind: science and research record')\n"
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
    standards:['science and research record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Research Funding Directory Signature Database.',
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
var gen={version:'jahdb-research-funding-directory-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('research-funding-directory-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
