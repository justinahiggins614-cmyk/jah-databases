(function(){'use strict';
/* JAH The Package Tracking Troubleshooting Database generator — jahdb-package-tracking-troubleshooting-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PTT-";
var FIELDS=["tracking-basics","problem-resolution","claims-and-prevention"];
var TOPICS={"tracking-basics":["Reading Tracking Statuses \u2014 tracking-basics","Filing Claims \u2014 tracking-basics","FedEx Delivery Manager \u2014 tracking-basics","Porch Pirate Defense \u2014 tracking-basics","Address Errors \u2014 tracking-basics","Lost Package Protocol \u2014 tracking-basics","Third-Party Insurance \u2014 tracking-basics","Apartment Deliveries \u2014 tracking-basics","Vacation Holds \u2014 tracking-basics","Weather Delay Handling \u2014 tracking-basics","The Package Playbook \u2014 tracking-basics","Prohibited Items \u2014 tracking-basics"],"problem-resolution":["Tracking Number Formats \u2014 problem-resolution","USPS Tracking Quirks \u2014 problem-resolution","Amazon Logistics Tracking \u2014 problem-resolution","Signature Requirements \u2014 problem-resolution","International Tracking \u2014 problem-resolution","Damaged Package Claims \u2014 problem-resolution","Chargebacks for Lost Goods \u2014 problem-resolution","PO Box Shipping \u2014 problem-resolution","Tracking Apps \u2014 problem-resolution","Peak Season Shipping \u2014 problem-resolution","Shipping Cost Comparison \u2014 problem-resolution"],"claims-and-prevention":["The Stuck Package Playbook \u2014 claims-and-prevention","UPS My Choice \u2014 claims-and-prevention","'Delivered' But Missing \u2014 claims-and-prevention","Hold at Location \u2014 claims-and-prevention","Customs Delays \u2014 claims-and-prevention","Insurance: Worth It? \u2014 claims-and-prevention","Seller Communication \u2014 claims-and-prevention","Forwarding Packages \u2014 claims-and-prevention","Delivery Instructions \u2014 claims-and-prevention","Returns Tracking \u2014 claims-and-prevention","Packaging for Safety \u2014 claims-and-prevention"]};
var KINDS="transportation record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Package Tracking Troubleshooting Database — generated study\n"
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
   + "    print('kind: transportation record')\n"
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
    standards:['transportation record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Package Tracking Troubleshooting Database.',
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
var gen={version:'jahdb-package-tracking-troubleshooting-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('package-tracking-troubleshooting',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
