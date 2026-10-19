(function(){'use strict';
/* JAH The Public Procurement Rules Database generator — jahdb-public-procurement-rules-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PPR-";
var FIELDS=["bidding-basics","contract-compliance","selling-to-government"];
var TOPICS={"bidding-basics":["How Government Buying Works \u2014 bidding-basics","Reading Solicitations \u2014 bidding-basics","Set-Asides (Small Business) \u2014 bidding-basics","Proposal Writing Basics \u2014 bidding-basics","Performance and Delivery \u2014 bidding-basics","Protests \u2014 bidding-basics","Cooperative Purchasing \u2014 bidding-basics","Teaming Agreements \u2014 bidding-basics","Invoicing Disputes \u2014 bidding-basics","The Capture Process \u2014 bidding-basics","Post-Award Debriefs \u2014 bidding-basics","Bid/No-Bid Decision Framework \u2014 bidding-basics"],"contract-compliance":["SAM.gov Registration \u2014 contract-compliance","Responsive vs Responsible \u2014 contract-compliance","Subcontracting to Primes \u2014 contract-compliance","Invoicing the Government \u2014 contract-compliance","Change Orders (Government) \u2014 contract-compliance","Ethics and Gifts Rules \u2014 contract-compliance","GSA Schedule Contracts \u2014 contract-compliance","Compliance: Labor Standards \u2014 contract-compliance","Debarment Avoidance \u2014 contract-compliance","Proposal Compliance Matrix \u2014 contract-compliance","Growing Past Small Business \u2014 contract-compliance"],"selling-to-government":["Finding Bid Opportunities \u2014 selling-to-government","Bid Pricing Strategy \u2014 selling-to-government","Past Performance \u2014 selling-to-government","Contract Types \u2014 selling-to-government","Terminations \u2014 selling-to-government","State and Local Procurement \u2014 selling-to-government","Certifications That Help \u2014 selling-to-government","Cybersecurity (CMMC/NIST) \u2014 selling-to-government","Selling to Schools/Hospitals \u2014 selling-to-government","Oral Presentations \u2014 selling-to-government","The Annual GovCon Review \u2014 selling-to-government"]};
var KINDS="law and rights record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Public Procurement Rules Database — generated study\n"
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
    provenance:'Generated structural sample for the The Public Procurement Rules Database.',
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
var gen={version:'jahdb-public-procurement-rules-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-procurement-rules',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
