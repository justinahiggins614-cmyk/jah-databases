(function(){'use strict';
/* JAH The Food Assistance Access Signature Database generator — jahdb-food-assistance-access-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FTA-";
var FIELDS=["federal-nutrition-programs","community-food-resources","application-help"];
var TOPICS={"federal-nutrition-programs":["Signature SNAP Essentials (Signature Edition) \u2014 federal-nutrition-programs","Signature WIC Program (Signature Edition) \u2014 federal-nutrition-programs","Signature Community Fridges (Signature Edition) \u2014 federal-nutrition-programs","Signature College Food Pantries (Signature Edition) \u2014 federal-nutrition-programs","Signature Gleaning Programs (Signature Edition) \u2014 federal-nutrition-programs","Signature Dietary Restrictions (Signature Edition) \u2014 federal-nutrition-programs","Signature Appealing Denials (Signature Edition) \u2014 federal-nutrition-programs","Signature Nutrition on a Budget (Signature Edition) \u2014 federal-nutrition-programs","Signature Mutual Aid Networks (Signature Edition) \u2014 federal-nutrition-programs","Signature Commodity Programs (TEFAP/CSFP) (Signature Edition) \u2014 federal-nutrition-programs","Signature Rural Food Access (Signature Edition) \u2014 federal-nutrition-programs","Signature SNAP Recertification (Signature Edition) \u2014 federal-nutrition-programs"],"community-food-resources":["Signature SNAP Application Tips (Signature Edition) \u2014 community-food-resources","Signature School Meals (Signature Edition) \u2014 community-food-resources","Signature Senior Nutrition Programs (Signature Edition) \u2014 community-food-resources","Signature Farmers Market Benefits (Signature Edition) \u2014 community-food-resources","Signature Community Gardens (Signature Edition) \u2014 community-food-resources","Signature SNAP Work Requirements (Signature Edition) \u2014 community-food-resources","Signature EBT Security (Signature Edition) \u2014 community-food-resources","Signature Cooking Skills Basics (Signature Edition) \u2014 community-food-resources","Signature Faith Community Meals (Signature Edition) \u2014 community-food-resources","Signature Breastfeeding Support (WIC) (Signature Edition) \u2014 community-food-resources","Signature The Food Resource Map (Signature Edition) \u2014 community-food-resources"],"application-help":["Signature What SNAP Covers (Signature Edition) \u2014 application-help","Signature Food Banks and Pantries (Signature Edition) \u2014 application-help","Signature Summer Food Service (Signature Edition) \u2014 application-help","Signature Food Recovery Apps (Signature Edition) \u2014 application-help","Signature Culturally Appropriate Food (Signature Edition) \u2014 application-help","Signature Reporting Changes (Signature Edition) \u2014 application-help","Signature Stretching Food Dollars (Signature Edition) \u2014 application-help","Signature Food Safety at Home (Signature Edition) \u2014 application-help","Signature Disaster Food Aid (D-SNAP) (Signature Edition) \u2014 application-help","Signature Foster Youth Food Access (Signature Edition) \u2014 application-help","Signature Volunteering at Food Programs (Signature Edition) \u2014 application-help"]};
var KINDS="government-assistance record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Food Assistance Access Signature Database — generated study\n"
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
    name:topic+' — Signature generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural Signature sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['government-assistance record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Food Assistance Access Signature Database.',
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
var gen={version:'jahdb-food-assistance-access-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('food-assistance-access-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
