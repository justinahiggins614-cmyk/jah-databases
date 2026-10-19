(function(){'use strict';
/* JAH The Food Assistance Access Database generator — jahdb-food-assistance-access-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FTA-";
var FIELDS=["federal-nutrition-programs","community-food-resources","application-help"];
var TOPICS={"federal-nutrition-programs":["SNAP Essentials \u2014 federal-nutrition-programs","WIC Program \u2014 federal-nutrition-programs","Community Fridges \u2014 federal-nutrition-programs","College Food Pantries \u2014 federal-nutrition-programs","Gleaning Programs \u2014 federal-nutrition-programs","Dietary Restrictions \u2014 federal-nutrition-programs","Appealing Denials \u2014 federal-nutrition-programs","Nutrition on a Budget \u2014 federal-nutrition-programs","Mutual Aid Networks \u2014 federal-nutrition-programs","Commodity Programs (TEFAP/CSFP) \u2014 federal-nutrition-programs","Rural Food Access \u2014 federal-nutrition-programs","SNAP Recertification \u2014 federal-nutrition-programs"],"community-food-resources":["SNAP Application Tips \u2014 community-food-resources","School Meals \u2014 community-food-resources","Senior Nutrition Programs \u2014 community-food-resources","Farmers Market Benefits \u2014 community-food-resources","Community Gardens \u2014 community-food-resources","SNAP Work Requirements \u2014 community-food-resources","EBT Security \u2014 community-food-resources","Cooking Skills Basics \u2014 community-food-resources","Faith Community Meals \u2014 community-food-resources","Breastfeeding Support (WIC) \u2014 community-food-resources","The Food Resource Map \u2014 community-food-resources"],"application-help":["What SNAP Covers \u2014 application-help","Food Banks and Pantries \u2014 application-help","Summer Food Service \u2014 application-help","Food Recovery Apps \u2014 application-help","Culturally Appropriate Food \u2014 application-help","Reporting Changes \u2014 application-help","Stretching Food Dollars \u2014 application-help","Food Safety at Home \u2014 application-help","Disaster Food Aid (D-SNAP) \u2014 application-help","Foster Youth Food Access \u2014 application-help","Volunteering at Food Programs \u2014 application-help"]};
var KINDS="government-assistance record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Food Assistance Access Database — generated study\n"
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
   + "    print('kind: government-assistance record')\n"
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
    standards:['government-assistance record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Food Assistance Access Database.',
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
var gen={version:'jahdb-food-assistance-access-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('food-assistance-access',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
