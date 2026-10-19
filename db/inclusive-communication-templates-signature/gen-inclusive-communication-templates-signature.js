(function(){'use strict';
/* JAH The Inclusive Communication Templates Signature Database generator — jahdb-inclusive-communication-templates-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ICT-";
var FIELDS=["plain-language-templates","accessible-formats","respectful-language-guides"];
var TOPICS={"plain-language-templates":["Signature Plain Language Basics (Signature Edition) \u2014 plain-language-templates","Signature The Template Library (Signature Edition) \u2014 plain-language-templates","Signature Announcement Templates (Signature Edition) \u2014 plain-language-templates","Signature Person-First Language (Signature Edition) \u2014 plain-language-templates","Signature Gender-Inclusive Language (Signature Edition) \u2014 plain-language-templates","Signature Avoiding Ableist Language (Signature Edition) \u2014 plain-language-templates","Signature Audio Description Scripts (Signature Edition) \u2014 plain-language-templates","Signature Braille Requests (Signature Edition) \u2014 plain-language-templates","Signature Document Structure (Signature Edition) \u2014 plain-language-templates","Signature Event Access Statements (Signature Edition) \u2014 plain-language-templates","Signature Training Teams (Signature Edition) \u2014 plain-language-templates","Signature Template Maintenance (Signature Edition) \u2014 plain-language-templates"],"accessible-formats":["Signature Reading Level Targets (Signature Edition) \u2014 accessible-formats","Signature Email Templates (Signature Edition) \u2014 accessible-formats","Signature Apology Templates (Signature Edition) \u2014 accessible-formats","Signature Identity-First Language (Signature Edition) \u2014 accessible-formats","Signature Race-Conscious Language (Signature Edition) \u2014 accessible-formats","Signature Caption Templates (Signature Edition) \u2014 accessible-formats","Signature Easy-Read Formats (Signature Edition) \u2014 accessible-formats","Signature Color Contrast (Signature Edition) \u2014 accessible-formats","Signature Social Media Access (Signature Edition) \u2014 accessible-formats","Signature Feedback on Language (Signature Edition) \u2014 accessible-formats","Signature Review Process (Signature Edition) \u2014 accessible-formats"],"respectful-language-guides":["Signature Alt Text Templates (Signature Edition) \u2014 respectful-language-guides","Signature Meeting Invite Templates (Signature Edition) \u2014 respectful-language-guides","Signature Feedback Templates (Signature Edition) \u2014 respectful-language-guides","Signature Asking Preferences (Signature Edition) \u2014 respectful-language-guides","Signature Age-Inclusive Language (Signature Edition) \u2014 respectful-language-guides","Signature Transcript Templates (Signature Edition) \u2014 respectful-language-guides","Signature Large Print Guidelines (Signature Edition) \u2014 respectful-language-guides","Signature Font Choices (Signature Edition) \u2014 respectful-language-guides","Signature Presentation Access (Signature Edition) \u2014 respectful-language-guides","Signature Style Guide Creation (Signature Edition) \u2014 respectful-language-guides","Signature The Inclusive Comms Audit (Signature Edition) \u2014 respectful-language-guides"]};
var KINDS="accessibility record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Inclusive Communication Templates Signature Database — generated study\n"
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
    provenance:'Generated structural sample for the The Inclusive Communication Templates Signature Database.',
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
var gen={version:'jahdb-inclusive-communication-templates-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('inclusive-communication-templates-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
