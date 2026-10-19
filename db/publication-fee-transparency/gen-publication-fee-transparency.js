(function(){'use strict';
/* JAH The Publication Fee Transparency Database generator — jahdb-publication-fee-transparency-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PFT-";
var FIELDS=["fee-landscapes","waiver-systems","publishing-alternatives"];
var TOPICS={"fee-landscapes":["APC Landscape \u2014 fee-landscapes","Institutional Deals \u2014 fee-landscapes","Preprint Servers \u2014 fee-landscapes","Fee Comparison Tools \u2014 fee-landscapes","The Transparency Playbook \u2014 fee-landscapes","Hybrid Journals \u2014 fee-landscapes","Society Journals \u2014 fee-landscapes","Review Commons \u2014 fee-landscapes","Global South Access \u2014 fee-landscapes","Retraction Watch \u2014 fee-landscapes","Choosing Where to Publish \u2014 fee-landscapes","The Fee-Free Publishing Guide \u2014 fee-landscapes"],"waiver-systems":["What APCs Buy \u2014 waiver-systems","Predatory Journals \u2014 waiver-systems","Green OA (Self-Archiving) \u2014 waiver-systems","Funder Mandates \u2014 waiver-systems","APC by Discipline \u2014 waiver-systems","Subscribe to Open \u2014 waiver-systems","Mega-Journals \u2014 waiver-systems","Preprint Review \u2014 waiver-systems","Sci-Hub Debate \u2014 waiver-systems","Paper Mills \u2014 waiver-systems","Open Peer Review \u2014 waiver-systems"],"publishing-alternatives":["Waiver Programs \u2014 publishing-alternatives","Diamond Open Access \u2014 publishing-alternatives","Page/Color Charges \u2014 publishing-alternatives","Negotiating Fees \u2014 publishing-alternatives","APC Inflation \u2014 publishing-alternatives","Library Publishing \u2014 publishing-alternatives","Overlay Journals \u2014 publishing-alternatives","Fee Assistance Funds \u2014 publishing-alternatives","Unpaywall Tools \u2014 publishing-alternatives","Authorship Ethics \u2014 publishing-alternatives","Publishing Timeline \u2014 publishing-alternatives"]};
var KINDS="science and research record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Publication Fee Transparency Database — generated study\n"
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
    name:topic+' — generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['science and research record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Publication Fee Transparency Database.',
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
var gen={version:'jahdb-publication-fee-transparency-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('publication-fee-transparency',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
