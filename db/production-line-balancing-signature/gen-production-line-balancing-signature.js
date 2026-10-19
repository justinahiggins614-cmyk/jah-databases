(function(){'use strict';
/* JAH The Production Line Balancing Signature Database generator — jahdb-production-line-balancing-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PLB-";
var FIELDS=["line-analysis","balancing-methods","flow-optimization"];
var TOPICS={"line-analysis":["Signature Takt Time (Signature Edition) \u2014 line-analysis","Signature Line Balancing Basics (Signature Edition) \u2014 line-analysis","Signature Precedence Diagrams (Signature Edition) \u2014 line-analysis","Signature Efficiency Metrics (Signature Edition) \u2014 line-analysis","Signature U-Shaped Lines (Signature Edition) \u2014 line-analysis","Signature WIP Limits (Signature Edition) \u2014 line-analysis","Signature SMED (Quick Changeover) (Signature Edition) \u2014 line-analysis","Signature Yamazumi Charts (Signature Edition) \u2014 line-analysis","Signature Ergonomics on Lines (Signature Edition) \u2014 line-analysis","Signature Simulation for Lines (Signature Edition) \u2014 line-analysis","Signature Heijunka (Leveling) (Signature Edition) \u2014 line-analysis","Signature Line Balancing Software (Signature Edition) \u2014 line-analysis"],"balancing-methods":["Signature Cycle Time vs Takt (Signature Edition) \u2014 balancing-methods","Signature The Balancing Playbook (Signature Edition) \u2014 balancing-methods","Signature Largest Candidate Rule (Signature Edition) \u2014 balancing-methods","Signature Smoothness Index (Signature Edition) \u2014 balancing-methods","Signature One-Piece Flow (Signature Edition) \u2014 balancing-methods","Signature Andon Systems (Signature Edition) \u2014 balancing-methods","Signature Standard Work (Signature Edition) \u2014 balancing-methods","Signature Operator Flexibility (Signature Edition) \u2014 balancing-methods","Signature Quality at the Source (Signature Edition) \u2014 balancing-methods","Signature OEE (Overall Equipment Effectiveness) (Signature Edition) \u2014 balancing-methods","Signature The Flow Audit (Signature Edition) \u2014 balancing-methods"],"flow-optimization":["Signature Bottleneck Identification (Signature Edition) \u2014 flow-optimization","Signature Workstation Design (Signature Edition) \u2014 flow-optimization","Signature Ranked Positional Weight (Signature Edition) \u2014 flow-optimization","Signature Mixed-Model Lines (Signature Edition) \u2014 flow-optimization","Signature Pull Systems (Kanban) (Signature Edition) \u2014 flow-optimization","Signature Poka-Yoke (Signature Edition) \u2014 flow-optimization","Signature Time Studies (Signature Edition) \u2014 flow-optimization","Signature Line-Side Inventory (Signature Edition) \u2014 flow-optimization","Signature Rebalancing Triggers (Signature Edition) \u2014 flow-optimization","Signature Continuous Flow Cells (Signature Edition) \u2014 flow-optimization","Signature Kaizen for Lines (Signature Edition) \u2014 flow-optimization"]};
var KINDS="engineering record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Production Line Balancing Signature Database — generated study\n"
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
   + "    print('kind: engineering record')\n"
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
    standards:['engineering record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Production Line Balancing Signature Database.',
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
var gen={version:'jahdb-production-line-balancing-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('production-line-balancing-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
