(function(){'use strict';
/* JAH The Space Mission Data Directory Database generator — jahdb-space-mission-data-directory-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SMDD-";
var FIELDS=["mission-archives","dataset-access","data-use-guides"];
var TOPICS={"mission-archives":["NASA Data Archives \u2014 mission-archives","Astrophysics Archives \u2014 mission-archives","Reading FITS Files \u2014 mission-archives","Citizen Science (Space) \u2014 mission-archives","Mars Mission Data \u2014 mission-archives","Heliophysics Data \u2014 mission-archives","Hubble Legacy \u2014 mission-archives","ISS Data \u2014 mission-archives","Asteroid Mining Data \u2014 mission-archives","Deep Space Network \u2014 mission-archives","Sample Data (Apollo etc.) \u2014 mission-archives","The Mission Data Master Index \u2014 mission-archives"],"dataset-access":["Planetary Data System \u2014 dataset-access","ESA Archives \u2014 dataset-access","Mission Timelines \u2014 dataset-access","The Directory Playbook \u2014 dataset-access","Outer Planets Data \u2014 dataset-access","Exoplanet Data \u2014 dataset-access","Radio Astronomy Data \u2014 dataset-access","Lunar Mission Data \u2014 dataset-access","Space Weather Data \u2014 dataset-access","Mission Spice Kernels \u2014 dataset-access","Mission APIs \u2014 dataset-access"],"data-use-guides":["Earth Science Data \u2014 data-use-guides","JAXA/ISRO/Other Agencies \u2014 data-use-guides","Citing Mission Data \u2014 data-use-guides","Apollo Program Data \u2014 data-use-guides","Small Bodies Data \u2014 data-use-guides","JWST Data \u2014 data-use-guides","Gravitational Wave Data \u2014 data-use-guides","Comet Mission Data \u2014 data-use-guides","Satellite Imagery (Earth) \u2014 data-use-guides","Planetary Maps \u2014 data-use-guides","Visualization Tools \u2014 data-use-guides"]};
var KINDS="science and research record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Space Mission Data Directory Database — generated study\n"
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
    name:topic+' — generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['science and research record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Space Mission Data Directory Database.',
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
var gen={version:'jahdb-space-mission-data-directory-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('space-mission-data-directory',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
