(function(){'use strict';
/* JAH The Keyboard Accessibility Testing Database generator — jahdb-keyboard-accessibility-testing-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-KAT-";
var FIELDS=["keyboard-testing-methods","focus-management","wcag-compliance"];
var TOPICS={"keyboard-testing-methods":["Why Keyboard Testing \u2014 keyboard-testing-methods","Focus Visibility \u2014 keyboard-testing-methods","Shortcuts \u2014 keyboard-testing-methods","The Keyboard Test Playbook \u2014 keyboard-testing-methods","Focus on SPAs \u2014 keyboard-testing-methods","Forms Keyboard Testing \u2014 keyboard-testing-methods","Video Player Keyboard \u2014 keyboard-testing-methods","Motion Sensitivity \u2014 keyboard-testing-methods","User Testing (Disabled Users) \u2014 keyboard-testing-methods","Training Teams \u2014 keyboard-testing-methods","Gaming Keyboard A11y \u2014 keyboard-testing-methods","Annual Keyboard Audit \u2014 keyboard-testing-methods"],"focus-management":["Unplug the Mouse \u2014 focus-management","Keyboard Traps \u2014 focus-management","Modals and Focus \u2014 focus-management","ARIA for Keyboard \u2014 focus-management","Testing Tools \u2014 focus-management","Tables Keyboard \u2014 focus-management","Drag-and-Drop Alternatives \u2014 focus-management","Character Key Shortcuts \u2014 focus-management","Regression Testing \u2014 focus-management","Legal Risk (ADA) \u2014 focus-management","Documentation \u2014 focus-management"],"wcag-compliance":["Tab Order Logic \u2014 wcag-compliance","Skip Links \u2014 wcag-compliance","Dropdowns and Menus \u2014 wcag-compliance","Roving Tabindex \u2014 wcag-compliance","Screen Reader + Keyboard \u2014 wcag-compliance","Carousels Keyboard \u2014 wcag-compliance","Timeout Adjustments \u2014 wcag-compliance","Testing Checklists \u2014 wcag-compliance","Keyboard Testing Reports \u2014 wcag-compliance","Mobile Keyboard A11y \u2014 wcag-compliance","The Keyboard-First Manifesto \u2014 wcag-compliance"]};
var KINDS="accessibility record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Keyboard Accessibility Testing Database — generated study\n"
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
   + "    print('kind: accessibility record')\n"
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
    standards:['accessibility record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Keyboard Accessibility Testing Database.',
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
var gen={version:'jahdb-keyboard-accessibility-testing-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('keyboard-accessibility-testing',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
