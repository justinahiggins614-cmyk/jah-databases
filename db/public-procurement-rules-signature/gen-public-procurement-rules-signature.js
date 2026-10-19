(function(){'use strict';
/* JAH The Public Procurement Rules Signature Database generator — jahdb-public-procurement-rules-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PPR-";
var FIELDS=["bidding-basics","contract-compliance","selling-to-government"];
var TOPICS={"bidding-basics":["Signature How Government Buying Works (Signature Edition) \u2014 bidding-basics","Signature Reading Solicitations (Signature Edition) \u2014 bidding-basics","Signature Set-Asides (Small Business) (Signature Edition) \u2014 bidding-basics","Signature Proposal Writing Basics (Signature Edition) \u2014 bidding-basics","Signature Performance and Delivery (Signature Edition) \u2014 bidding-basics","Signature Protests (Signature Edition) \u2014 bidding-basics","Signature Cooperative Purchasing (Signature Edition) \u2014 bidding-basics","Signature Teaming Agreements (Signature Edition) \u2014 bidding-basics","Signature Invoicing Disputes (Signature Edition) \u2014 bidding-basics","Signature The Capture Process (Signature Edition) \u2014 bidding-basics","Signature Post-Award Debriefs (Signature Edition) \u2014 bidding-basics","Signature Bid/No-Bid Decision Framework (Signature Edition) \u2014 bidding-basics"],"contract-compliance":["Signature SAM.gov Registration (Signature Edition) \u2014 contract-compliance","Signature Responsive vs Responsible (Signature Edition) \u2014 contract-compliance","Signature Subcontracting to Primes (Signature Edition) \u2014 contract-compliance","Signature Invoicing the Government (Signature Edition) \u2014 contract-compliance","Signature Change Orders (Government) (Signature Edition) \u2014 contract-compliance","Signature Ethics and Gifts Rules (Signature Edition) \u2014 contract-compliance","Signature GSA Schedule Contracts (Signature Edition) \u2014 contract-compliance","Signature Compliance: Labor Standards (Signature Edition) \u2014 contract-compliance","Signature Debarment Avoidance (Signature Edition) \u2014 contract-compliance","Signature Proposal Compliance Matrix (Signature Edition) \u2014 contract-compliance","Signature Growing Past Small Business (Signature Edition) \u2014 contract-compliance"],"selling-to-government":["Signature Finding Bid Opportunities (Signature Edition) \u2014 selling-to-government","Signature Bid Pricing Strategy (Signature Edition) \u2014 selling-to-government","Signature Past Performance (Signature Edition) \u2014 selling-to-government","Signature Contract Types (Signature Edition) \u2014 selling-to-government","Signature Terminations (Signature Edition) \u2014 selling-to-government","Signature State and Local Procurement (Signature Edition) \u2014 selling-to-government","Signature Certifications That Help (Signature Edition) \u2014 selling-to-government","Signature Cybersecurity (CMMC/NIST) (Signature Edition) \u2014 selling-to-government","Signature Selling to Schools/Hospitals (Signature Edition) \u2014 selling-to-government","Signature Oral Presentations (Signature Edition) \u2014 selling-to-government","Signature The Annual GovCon Review (Signature Edition) \u2014 selling-to-government"]};
var KINDS="law and rights record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Public Procurement Rules Signature Database — generated study\n"
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
    provenance:'Generated structural sample for the The Public Procurement Rules Signature Database.',
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
var gen={version:'jahdb-public-procurement-rules-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-procurement-rules-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
