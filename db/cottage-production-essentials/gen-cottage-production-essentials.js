(function(){'use strict';
/* JAH The Cottage Production Essentials Database generator — jahdb-cottage-production-essentials-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CPE-";
var FIELDS=["cottage-food-law","home-production-systems","selling-channels"];
var TOPICS={"cottage-food-law":["Cottage Food Laws Explained \u2014 cottage-food-law","Food Handler Certification \u2014 cottage-food-law","Costing Homemade Goods \u2014 cottage-food-law","Online Cottage Sales \u2014 cottage-food-law","Allergen Management \u2014 cottage-food-law","Seasonal Production Planning \u2014 cottage-food-law","Photography for Food \u2014 cottage-food-law","Sales Caps and Growth \u2014 cottage-food-law","Year Two: What's Next \u2014 cottage-food-law","Holiday Gift Sets \u2014 cottage-food-law","Story Branding \u2014 cottage-food-law","The Cottage Annual Review \u2014 cottage-food-law"],"home-production-systems":["What's Allowed vs Not \u2014 home-production-systems","Home Kitchen Setup \u2014 home-production-systems","Packaging on a Budget \u2014 home-production-systems","Wholesale: When Ready \u2014 home-production-systems","Scaling to Commercial Kitchen \u2014 home-production-systems","Non-Food Cottage Products \u2014 home-production-systems","Customer Feedback Loops \u2014 home-production-systems","Hiring Help at Home \u2014 home-production-systems","Pricing Psychology at Markets \u2014 home-production-systems","Subscription Boxes (Cottage) \u2014 home-production-systems","Collaborating with Farms \u2014 home-production-systems"],"selling-channels":["Labeling Requirements \u2014 selling-channels","Recipe Standardization \u2014 selling-channels","Farmers Markets (Food) \u2014 selling-channels","Shelf-Life Basics \u2014 selling-channels","Cottage Business Insurance \u2014 selling-channels","Craft Show Selling \u2014 selling-channels","Record-Keeping (Food Biz) \u2014 selling-channels","The Cottage Launch Plan \u2014 selling-channels","Sampling Strategy \u2014 selling-channels","Dietary Niche Products \u2014 selling-channels","Teaching What You Make \u2014 selling-channels"]};
var KINDS="small-business record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Cottage Production Essentials Database — generated study\n"
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
   + "    print('kind: small-business record')\n"
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
    standards:['small-business record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Cottage Production Essentials Database.',
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
var gen={version:'jahdb-cottage-production-essentials-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('cottage-production-essentials',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
