(function(){'use strict';
/* JAH The Keyboard Accessibility Testing Signature Database generator — jahdb-keyboard-accessibility-testing-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-KAT-";
var FIELDS=["keyboard-testing-methods","focus-management","wcag-compliance"];
var TOPICS={"keyboard-testing-methods":["Signature Why Keyboard Testing (Signature Edition) \u2014 keyboard-testing-methods","Signature Focus Visibility (Signature Edition) \u2014 keyboard-testing-methods","Signature Shortcuts (Signature Edition) \u2014 keyboard-testing-methods","Signature The Keyboard Test Playbook (Signature Edition) \u2014 keyboard-testing-methods","Signature Focus on SPAs (Signature Edition) \u2014 keyboard-testing-methods","Signature Forms Keyboard Testing (Signature Edition) \u2014 keyboard-testing-methods","Signature Video Player Keyboard (Signature Edition) \u2014 keyboard-testing-methods","Signature Motion Sensitivity (Signature Edition) \u2014 keyboard-testing-methods","Signature User Testing (Disabled Users) (Signature Edition) \u2014 keyboard-testing-methods","Signature Training Teams (Signature Edition) \u2014 keyboard-testing-methods","Signature Gaming Keyboard A11y (Signature Edition) \u2014 keyboard-testing-methods","Signature Annual Keyboard Audit (Signature Edition) \u2014 keyboard-testing-methods"],"focus-management":["Signature Unplug the Mouse (Signature Edition) \u2014 focus-management","Signature Keyboard Traps (Signature Edition) \u2014 focus-management","Signature Modals and Focus (Signature Edition) \u2014 focus-management","Signature ARIA for Keyboard (Signature Edition) \u2014 focus-management","Signature Testing Tools (Signature Edition) \u2014 focus-management","Signature Tables Keyboard (Signature Edition) \u2014 focus-management","Signature Drag-and-Drop Alternatives (Signature Edition) \u2014 focus-management","Signature Character Key Shortcuts (Signature Edition) \u2014 focus-management","Signature Regression Testing (Signature Edition) \u2014 focus-management","Signature Legal Risk (ADA) (Signature Edition) \u2014 focus-management","Signature Documentation (Signature Edition) \u2014 focus-management"],"wcag-compliance":["Signature Tab Order Logic (Signature Edition) \u2014 wcag-compliance","Signature Skip Links (Signature Edition) \u2014 wcag-compliance","Signature Dropdowns and Menus (Signature Edition) \u2014 wcag-compliance","Signature Roving Tabindex (Signature Edition) \u2014 wcag-compliance","Signature Screen Reader + Keyboard (Signature Edition) \u2014 wcag-compliance","Signature Carousels Keyboard (Signature Edition) \u2014 wcag-compliance","Signature Timeout Adjustments (Signature Edition) \u2014 wcag-compliance","Signature Testing Checklists (Signature Edition) \u2014 wcag-compliance","Signature Keyboard Testing Reports (Signature Edition) \u2014 wcag-compliance","Signature Mobile Keyboard A11y (Signature Edition) \u2014 wcag-compliance","Signature The Keyboard-First Manifesto (Signature Edition) \u2014 wcag-compliance"]};
var KINDS="accessibility record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Keyboard Accessibility Testing Signature Database — generated study\n"
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
    name:topic+' — Signature generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural Signature sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['accessibility record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Keyboard Accessibility Testing Signature Database.',
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
var gen={version:'jahdb-keyboard-accessibility-testing-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('keyboard-accessibility-testing-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
