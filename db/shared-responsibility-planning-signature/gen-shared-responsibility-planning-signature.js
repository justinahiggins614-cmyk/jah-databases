(function(){'use strict';
/* JAH The Shared Responsibility Planning Signature Database generator — jahdb-shared-responsibility-planning-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SRP-";
var FIELDS=["household-division-systems","shared-cost-methods","joint-decision-frameworks"];
var TOPICS={"household-division-systems":["Signature The Chore Audit (Signature Edition) \u2014 household-division-systems","Signature The 50/50 Money Split Alternatives (Signature Edition) \u2014 household-division-systems","Signature Mental Load Inventory (Signature Edition) \u2014 household-division-systems","Signature Elder Care Sharing Among Siblings (Signature Edition) \u2014 household-division-systems","Signature Holiday and Event Planning Split (Signature Edition) \u2014 household-division-systems","Signature The Check-In: 'What Do You Need?' (Signature Edition) \u2014 household-division-systems","Signature The Appreciation Ledger (Signature Edition) \u2014 household-division-systems","Signature The Grocery and Meal Split (Signature Edition) \u2014 household-division-systems","Signature Vacation Planning Partnership (Signature Edition) \u2014 household-division-systems","Signature The 'Done' Standard Agreement (Signature Edition) \u2014 household-division-systems","Signature Outsourcing Decisions Together (Signature Edition) \u2014 household-division-systems","Signature The 'Default Parent' Rebalance (Signature Edition) \u2014 household-division-systems"],"shared-cost-methods":["Signature Fair Play Deck Method (Signature Edition) \u2014 shared-cost-methods","Signature Shared Expense Tracking (Signature Edition) \u2014 shared-cost-methods","Signature Parenting Task Division (Signature Edition) \u2014 shared-cost-methods","Signature Car Sharing Between Partners (Signature Edition) \u2014 shared-cost-methods","Signature The 'Mine, Yours, Ours' Account System (Signature Edition) \u2014 shared-cost-methods","Signature Splitting the Mental Load of Kids' Schedules (Signature Edition) \u2014 shared-cost-methods","Signature Conflict Resolution Protocol (Signature Edition) \u2014 shared-cost-methods","Signature Financial Transparency Agreement (Signature Edition) \u2014 shared-cost-methods","Signature The Emergency Role Card (Signature Edition) \u2014 shared-cost-methods","Signature Renegotiation Triggers (Signature Edition) \u2014 shared-cost-methods","Signature The Annual Partnership Review (Signature Edition) \u2014 shared-cost-methods"],"joint-decision-frameworks":["Signature Chore Rotation Schedules (Signature Edition) \u2014 joint-decision-frameworks","Signature The Weekly Household Meeting (Signature Edition) \u2014 joint-decision-frameworks","Signature Roommate Agreement Template (Signature Edition) \u2014 joint-decision-frameworks","Signature Pet Care Division (Signature Edition) \u2014 joint-decision-frameworks","Signature Decision Rights Matrix (Signature Edition) \u2014 joint-decision-frameworks","Signature Fair Division of Unpleasant Tasks (Signature Edition) \u2014 joint-decision-frameworks","Signature Sharing a Home Office (Signature Edition) \u2014 joint-decision-frameworks","Signature The 'Second Shift' Conversation (Signature Edition) \u2014 joint-decision-frameworks","Signature Splitting Gift and Social Obligations (Signature Edition) \u2014 joint-decision-frameworks","Signature The Scoreboard (Without Scorekeeping) (Signature Edition) \u2014 joint-decision-frameworks","Signature Co-Habitation Exit Plan (Signature Edition) \u2014 joint-decision-frameworks"]};
var KINDS="everyday problem-solving record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Shared Responsibility Planning Signature Database — generated study\n"
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
   + "    print('kind: everyday problem-solving record')\n"
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
    standards:['everyday problem-solving record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Shared Responsibility Planning Signature Database.',
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
var gen={version:'jahdb-shared-responsibility-planning-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('shared-responsibility-planning-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
