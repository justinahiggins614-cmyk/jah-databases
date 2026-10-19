(function(){'use strict';
/* JAH The Inclusive Communication Templates Database generator — jahdb-inclusive-communication-templates-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ICT-";
var FIELDS=["plain-language-templates","accessible-formats","respectful-language-guides"];
var TOPICS={"plain-language-templates":["Plain Language Basics \u2014 plain-language-templates","The Template Library \u2014 plain-language-templates","Announcement Templates \u2014 plain-language-templates","Person-First Language \u2014 plain-language-templates","Gender-Inclusive Language \u2014 plain-language-templates","Avoiding Ableist Language \u2014 plain-language-templates","Audio Description Scripts \u2014 plain-language-templates","Braille Requests \u2014 plain-language-templates","Document Structure \u2014 plain-language-templates","Event Access Statements \u2014 plain-language-templates","Training Teams \u2014 plain-language-templates","Template Maintenance \u2014 plain-language-templates"],"accessible-formats":["Reading Level Targets \u2014 accessible-formats","Email Templates \u2014 accessible-formats","Apology Templates \u2014 accessible-formats","Identity-First Language \u2014 accessible-formats","Race-Conscious Language \u2014 accessible-formats","Caption Templates \u2014 accessible-formats","Easy-Read Formats \u2014 accessible-formats","Color Contrast \u2014 accessible-formats","Social Media Access \u2014 accessible-formats","Feedback on Language \u2014 accessible-formats","Review Process \u2014 accessible-formats"],"respectful-language-guides":["Alt Text Templates \u2014 respectful-language-guides","Meeting Invite Templates \u2014 respectful-language-guides","Feedback Templates \u2014 respectful-language-guides","Asking Preferences \u2014 respectful-language-guides","Age-Inclusive Language \u2014 respectful-language-guides","Transcript Templates \u2014 respectful-language-guides","Large Print Guidelines \u2014 respectful-language-guides","Font Choices \u2014 respectful-language-guides","Presentation Access \u2014 respectful-language-guides","Style Guide Creation \u2014 respectful-language-guides","The Inclusive Comms Audit \u2014 respectful-language-guides"]};
var KINDS="accessibility record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Inclusive Communication Templates Database — generated study\n"
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
    provenance:'Generated structural sample for the The Inclusive Communication Templates Database.',
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
var gen={version:'jahdb-inclusive-communication-templates-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('inclusive-communication-templates',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
