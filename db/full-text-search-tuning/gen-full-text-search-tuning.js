(function(){'use strict';
/* JAH The Full-Text Search Tuning Database generator — jahdb-full-text-search-tuning-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FTST-";
var FIELDS=["relevance-tuning","analyzer-configuration","search-operations"];
var TOPICS={"relevance-tuning":["How Full-Text Search Works \u2014 relevance-tuning","Stemming vs Lemmatization \u2014 relevance-tuning","Relevance Feedback Loop \u2014 relevance-tuning","Faceted Search \u2014 relevance-tuning","Multi-language Search \u2014 relevance-tuning","Postgres Full-Text \u2014 relevance-tuning","Search at Scale \u2014 relevance-tuning","Phrase Matching \u2014 relevance-tuning","Learning to Rank \u2014 relevance-tuning","Zero-Result Handling \u2014 relevance-tuning","Index Lifecycle \u2014 relevance-tuning","Search Ops Runbook \u2014 relevance-tuning"],"analyzer-configuration":["BM25 Ranking \u2014 analyzer-configuration","Stop Words \u2014 analyzer-configuration","Measuring Relevance \u2014 analyzer-configuration","Autocomplete/Suggest \u2014 analyzer-configuration","Elasticsearch Basics \u2014 analyzer-configuration","Vector/Hybrid Search \u2014 analyzer-configuration","The Search Tuning Playbook \u2014 analyzer-configuration","Boolean Queries \u2014 analyzer-configuration","Personalization \u2014 analyzer-configuration","Search Analytics \u2014 analyzer-configuration","Security for Search \u2014 analyzer-configuration"],"search-operations":["Analyzers and Tokenizers \u2014 search-operations","Synonyms \u2014 search-operations","Query Understanding \u2014 search-operations","Typo Tolerance \u2014 search-operations","OpenSearch Alternative \u2014 search-operations","Indexing Performance \u2014 search-operations","Field Boosting \u2014 search-operations","Function Score \u2014 search-operations","Search UI Patterns \u2014 search-operations","A/B Testing Search \u2014 search-operations","Multitenant Search \u2014 search-operations"]};
var KINDS="data-engineering record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Full-Text Search Tuning Database — generated study\n"
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
   + "    print('kind: data-engineering record')\n"
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
    standards:['data-engineering record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Full-Text Search Tuning Database.',
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
var gen={version:'jahdb-full-text-search-tuning-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('full-text-search-tuning',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
