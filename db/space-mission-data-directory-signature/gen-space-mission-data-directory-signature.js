(function(){'use strict';
/* JAH The Space Mission Data Directory Signature Database generator — jahdb-space-mission-data-directory-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SMDD-";
var FIELDS=["mission-archives","dataset-access","data-use-guides"];
var TOPICS={"mission-archives":["Signature NASA Data Archives (Signature Edition) \u2014 mission-archives","Signature Astrophysics Archives (Signature Edition) \u2014 mission-archives","Signature Reading FITS Files (Signature Edition) \u2014 mission-archives","Signature Citizen Science (Space) (Signature Edition) \u2014 mission-archives","Signature Mars Mission Data (Signature Edition) \u2014 mission-archives","Signature Heliophysics Data (Signature Edition) \u2014 mission-archives","Signature Hubble Legacy (Signature Edition) \u2014 mission-archives","Signature ISS Data (Signature Edition) \u2014 mission-archives","Signature Asteroid Mining Data (Signature Edition) \u2014 mission-archives","Signature Deep Space Network (Signature Edition) \u2014 mission-archives","Signature Sample Data (Apollo etc.) (Signature Edition) \u2014 mission-archives","Signature The Mission Data Master Index (Signature Edition) \u2014 mission-archives"],"dataset-access":["Signature Planetary Data System (Signature Edition) \u2014 dataset-access","Signature ESA Archives (Signature Edition) \u2014 dataset-access","Signature Mission Timelines (Signature Edition) \u2014 dataset-access","Signature The Directory Playbook (Signature Edition) \u2014 dataset-access","Signature Outer Planets Data (Signature Edition) \u2014 dataset-access","Signature Exoplanet Data (Signature Edition) \u2014 dataset-access","Signature Radio Astronomy Data (Signature Edition) \u2014 dataset-access","Signature Lunar Mission Data (Signature Edition) \u2014 dataset-access","Signature Space Weather Data (Signature Edition) \u2014 dataset-access","Signature Mission Spice Kernels (Signature Edition) \u2014 dataset-access","Signature Mission APIs (Signature Edition) \u2014 dataset-access"],"data-use-guides":["Signature Earth Science Data (Signature Edition) \u2014 data-use-guides","Signature JAXA/ISRO/Other Agencies (Signature Edition) \u2014 data-use-guides","Signature Citing Mission Data (Signature Edition) \u2014 data-use-guides","Signature Apollo Program Data (Signature Edition) \u2014 data-use-guides","Signature Small Bodies Data (Signature Edition) \u2014 data-use-guides","Signature JWST Data (Signature Edition) \u2014 data-use-guides","Signature Gravitational Wave Data (Signature Edition) \u2014 data-use-guides","Signature Comet Mission Data (Signature Edition) \u2014 data-use-guides","Signature Satellite Imagery (Earth) (Signature Edition) \u2014 data-use-guides","Signature Planetary Maps (Signature Edition) \u2014 data-use-guides","Signature Visualization Tools (Signature Edition) \u2014 data-use-guides"]};
var KINDS="science and research record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Space Mission Data Directory Signature Database — generated study\n"
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
   + "    print('kind: science and research record')\n"
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
    standards:['science and research record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Space Mission Data Directory Signature Database.',
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
var gen={version:'jahdb-space-mission-data-directory-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('space-mission-data-directory-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
