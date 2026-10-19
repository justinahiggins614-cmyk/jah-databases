(function(){'use strict';
/* JAH The Shared Responsibility Planning Database generator — jahdb-shared-responsibility-planning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SRP-";
var FIELDS=["household-division-systems","shared-cost-methods","joint-decision-frameworks"];
var TOPICS={"household-division-systems":["The Chore Audit \u2014 household-division-systems","The 50/50 Money Split Alternatives \u2014 household-division-systems","Mental Load Inventory \u2014 household-division-systems","Elder Care Sharing Among Siblings \u2014 household-division-systems","Holiday and Event Planning Split \u2014 household-division-systems","The Check-In: 'What Do You Need?' \u2014 household-division-systems","The Appreciation Ledger \u2014 household-division-systems","The Grocery and Meal Split \u2014 household-division-systems","Vacation Planning Partnership \u2014 household-division-systems","The 'Done' Standard Agreement \u2014 household-division-systems","Outsourcing Decisions Together \u2014 household-division-systems","The 'Default Parent' Rebalance \u2014 household-division-systems"],"shared-cost-methods":["Fair Play Deck Method \u2014 shared-cost-methods","Shared Expense Tracking \u2014 shared-cost-methods","Parenting Task Division \u2014 shared-cost-methods","Car Sharing Between Partners \u2014 shared-cost-methods","The 'Mine, Yours, Ours' Account System \u2014 shared-cost-methods","Splitting the Mental Load of Kids' Schedules \u2014 shared-cost-methods","Conflict Resolution Protocol \u2014 shared-cost-methods","Financial Transparency Agreement \u2014 shared-cost-methods","The Emergency Role Card \u2014 shared-cost-methods","Renegotiation Triggers \u2014 shared-cost-methods","The Annual Partnership Review \u2014 shared-cost-methods"],"joint-decision-frameworks":["Chore Rotation Schedules \u2014 joint-decision-frameworks","The Weekly Household Meeting \u2014 joint-decision-frameworks","Roommate Agreement Template \u2014 joint-decision-frameworks","Pet Care Division \u2014 joint-decision-frameworks","Decision Rights Matrix \u2014 joint-decision-frameworks","Fair Division of Unpleasant Tasks \u2014 joint-decision-frameworks","Sharing a Home Office \u2014 joint-decision-frameworks","The 'Second Shift' Conversation \u2014 joint-decision-frameworks","Splitting Gift and Social Obligations \u2014 joint-decision-frameworks","The Scoreboard (Without Scorekeeping) \u2014 joint-decision-frameworks","Co-Habitation Exit Plan \u2014 joint-decision-frameworks"]};
var KINDS="everyday problem-solving record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Shared Responsibility Planning Database — generated study\n"
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
    name:topic+' — generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['everyday problem-solving record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Shared Responsibility Planning Database.',
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
var gen={version:'jahdb-shared-responsibility-planning-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('shared-responsibility-planning',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
