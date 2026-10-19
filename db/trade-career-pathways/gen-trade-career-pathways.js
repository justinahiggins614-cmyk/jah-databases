(function(){'use strict';
/* JAH The Trade Career Pathways Database generator — jahdb-trade-career-pathways-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TCP-";
var FIELDS=["trade-overviews","training-pathways","trade-business-skills"];
var TOPICS={"trade-overviews":["Electrician Pathway \u2014 trade-overviews","Welder Pathway \u2014 trade-overviews","Diesel Mechanic Pathway \u2014 trade-overviews","Roofer Pathway \u2014 trade-overviews","Apprenticeship Applications \u2014 trade-overviews","Licensing by State \u2014 trade-overviews","Estimating Jobs Profitably \u2014 trade-overviews","Women in Trades \u2014 trade-overviews","Physical Longevity in Trades \u2014 trade-overviews","Continuing Education Requirements \u2014 trade-overviews","Emerging Trade: Solar Installer \u2014 trade-overviews","Retirement for Tradespeople \u2014 trade-overviews"],"training-pathways":["Plumber Pathway \u2014 training-pathways","Carpenter Pathway \u2014 training-pathways","Lineman Pathway \u2014 training-pathways","Painter Pathway \u2014 training-pathways","Trade School Selection \u2014 training-pathways","From Journeyman to Master \u2014 training-pathways","Trade Math Refresher \u2014 training-pathways","Second-Career Trades Entry \u2014 training-pathways","Tools: Buy Once, Cry Once \u2014 training-pathways","The 10-Year Trade Career Map \u2014 training-pathways","Emerging Trade: EV Technician \u2014 training-pathways"],"trade-business-skills":["HVAC Technician Pathway \u2014 trade-business-skills","Auto Technician Pathway \u2014 trade-business-skills","Mason Pathway \u2014 trade-business-skills","Landscaper to Designer Path \u2014 trade-business-skills","Union vs Non-Union \u2014 trade-business-skills","Starting a Trade Business \u2014 trade-business-skills","Safety Certifications That Pay \u2014 trade-business-skills","Trade Specializations That Pay \u2014 trade-business-skills","Customer Skills for Tradespeople \u2014 trade-business-skills","Trade Career for Veterans \u2014 trade-business-skills","Trade Associations Worth Joining \u2014 trade-business-skills"]};
var KINDS="employment and workplace record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Trade Career Pathways Database — generated study\n"
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
   + "    print('kind: employment and workplace record')\n"
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
    standards:['employment and workplace record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Trade Career Pathways Database.',
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
var gen={version:'jahdb-trade-career-pathways-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('trade-career-pathways',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
