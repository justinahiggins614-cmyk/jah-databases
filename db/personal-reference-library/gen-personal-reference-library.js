(function(){'use strict';
/* JAH The Personal Reference Library Database generator — jahdb-personal-reference-library-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PRL-";
var FIELDS=["capture-systems","organization-methods","retrieval-practices"];
var TOPICS={"capture-systems":["The Commonplace Book \u2014 capture-systems","The PARA Method \u2014 capture-systems","Medical History File \u2014 capture-systems","Recipe and Meal Database \u2014 capture-systems","Numbers You Should Memorize \u2014 capture-systems","Gift Idea Bank \u2014 capture-systems","The 'How I Fixed It' Log \u2014 capture-systems","Network Map \u2014 capture-systems","Reference Capture Inbox \u2014 capture-systems","The Family Knowledge Transfer \u2014 capture-systems","Emergency Quick-Reference Card \u2014 capture-systems","The Annual Learning Plan \u2014 capture-systems"],"organization-methods":["Zettelkasten Note Method \u2014 organization-methods","Household Document Binder \u2014 organization-methods","Vehicle Maintenance Log \u2014 organization-methods","Contact Relationship Notes \u2014 organization-methods","The Decision Archive \u2014 organization-methods","Travel Reference File \u2014 organization-methods","Annual Review Document \u2014 organization-methods","Learning Resource Index \u2014 organization-methods","The 60-Second Retrieval Test \u2014 organization-methods","Subscription and Renewal Tracker \u2014 organization-methods","The Library Audit \u2014 organization-methods"],"retrieval-practices":["Personal Wiki Setup \u2014 retrieval-practices","Password and Account Ledger \u2014 retrieval-practices","Home Inventory for Insurance \u2014 retrieval-practices","Book Notes System \u2014 retrieval-practices","Skill Learning Log \u2014 retrieval-practices","Wisdom File (Quotes That Earned It) \u2014 retrieval-practices","Values and Principles Sheet \u2014 retrieval-practices","The 'Teach It' File \u2014 retrieval-practices","Digital Declutter Protocol \u2014 retrieval-practices","The 'Someday' List (Curated) \u2014 retrieval-practices","Backup and Legacy Plan \u2014 retrieval-practices"]};
var KINDS="everyday problem-solving record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Personal Reference Library Database — generated study\n"
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
    provenance:'Generated structural sample for the The Personal Reference Library Database.',
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
var gen={version:'jahdb-personal-reference-library-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('personal-reference-library',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
