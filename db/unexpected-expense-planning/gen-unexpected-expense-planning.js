(function(){'use strict';
/* JAH The Unexpected Expense Planning Database generator — jahdb-unexpected-expense-planning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-UEP-";
var FIELDS=["emergency-fund-systems","expense-triage-methods","recovery-planning"];
var TOPICS={"emergency-fund-systems":["Emergency Fund Sizing \u2014 emergency-fund-systems","The Sinking Fund Method \u2014 emergency-fund-systems","Medical Bill Negotiation \u2014 emergency-fund-systems","Vet Emergency Planning \u2014 emergency-fund-systems","The 'What If' Budget Drill \u2014 emergency-fund-systems","Expense Shock Recovery Plan \u2014 emergency-fund-systems","Kid Emergency Cost Planning \u2014 emergency-fund-systems","The 'Pause Everything' Protocol \u2014 emergency-fund-systems","Funeral and Final Cost Awareness \u2014 emergency-fund-systems","Community Lending Circles \u2014 emergency-fund-systems","Expense Insurance Review \u2014 emergency-fund-systems","Insurance Claim Filing Speed \u2014 emergency-fund-systems"],"expense-triage-methods":["Starter Emergency Fund ($1,000) \u2014 expense-triage-methods","Insurance Deductible Planning \u2014 expense-triage-methods","Car Breakdown Response Plan \u2014 expense-triage-methods","Phone and Tech Failure Backup \u2014 expense-triage-methods","Borrowing Hierarchy in Emergencies \u2014 expense-triage-methods","The Two-Account Defense \u2014 expense-triage-methods","Legal Surprise Buffer \u2014 expense-triage-methods","Side Income Emergency Valve \u2014 expense-triage-methods","Identity Theft Expense Buffer \u2014 expense-triage-methods","The 'Good Enough' Repair Rule \u2014 expense-triage-methods","The Calm-Money Mindset \u2014 expense-triage-methods"],"recovery-planning":["Expense Triage: Needs vs Wants Freeze \u2014 recovery-planning","Job Loss Runway Calculation \u2014 recovery-planning","Home Emergency Repair Fund \u2014 recovery-planning","Travel Emergency Fund \u2014 recovery-planning","Assistance Program Speed-Apply \u2014 recovery-planning","Income Drop Early Warning \u2014 recovery-planning","Appliance Failure Playbook \u2014 recovery-planning","Tax Surprise Prevention \u2014 recovery-planning","The Annual Surprise Audit \u2014 recovery-planning","Rebuilding After Depletion \u2014 recovery-planning","Multi-Generational Safety Nets \u2014 recovery-planning"]};
var KINDS="everyday problem-solving record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Unexpected Expense Planning Database — generated study\n"
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
    provenance:'Generated structural sample for the The Unexpected Expense Planning Database.',
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
var gen={version:'jahdb-unexpected-expense-planning-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unexpected-expense-planning',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
