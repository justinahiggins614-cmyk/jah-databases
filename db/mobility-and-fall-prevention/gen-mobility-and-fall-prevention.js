(function(){'use strict';
/* JAH The Mobility and Fall Prevention Database generator — jahdb-mobility-and-fall-prevention-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MFP-";
var FIELDS=["fall-risk-reduction","home-safety-modifications","strength-and-balance"];
var TOPICS={"fall-risk-reduction":["Fall Risk Self-Assessment \u2014 fall-risk-reduction","Stair Safety \u2014 fall-risk-reduction","Balance Exercises (Beginner) \u2014 fall-risk-reduction","Medication Fall Risks \u2014 fall-risk-reduction","Vitamin D and Bones \u2014 fall-risk-reduction","Getting Up After a Fall \u2014 fall-risk-reduction","Fear of Falling Cycle \u2014 fall-risk-reduction","Home Modification Planning \u2014 fall-risk-reduction","Community Fall Programs \u2014 fall-risk-reduction","Sleep and Fall Risk \u2014 fall-risk-reduction","Workplace Fall Prevention \u2014 fall-risk-reduction","Seasonal Fall Risks \u2014 fall-risk-reduction"],"home-safety-modifications":["Home Hazard Walkthrough \u2014 home-safety-modifications","Lighting for Fall Prevention \u2014 home-safety-modifications","Tai Chi for Fall Prevention \u2014 home-safety-modifications","Vision and Fall Risk \u2014 home-safety-modifications","Bone Density (DEXA) Testing \u2014 home-safety-modifications","Medical Alert Systems \u2014 home-safety-modifications","Outdoor Fall Prevention \u2014 home-safety-modifications","Caregiver Fall-Prevention Role \u2014 home-safety-modifications","Nutrition for Muscle \u2014 home-safety-modifications","The Annual Fall Review \u2014 home-safety-modifications","The Mobility Action Plan \u2014 home-safety-modifications"],"strength-and-balance":["Bathroom Safety Essentials \u2014 strength-and-balance","Footwear for Stability \u2014 strength-and-balance","Strength Training for Legs \u2014 strength-and-balance","Hearing and Balance \u2014 strength-and-balance","Assistive Devices Done Right \u2014 strength-and-balance","Post-Fall Medical Check \u2014 strength-and-balance","Exercise Class Selection \u2014 strength-and-balance","Hospital Fall Prevention \u2014 strength-and-balance","Hydration and Dizziness \u2014 strength-and-balance","Teaching Kids Fall Safety \u2014 strength-and-balance","Pet-Related Fall Hazards \u2014 strength-and-balance"]};
var KINDS="health-information record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Mobility and Fall Prevention Database — generated study\n"
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
   + "    print('kind: health-information record')\n"
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
    standards:['health-information record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Mobility and Fall Prevention Database.',
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
var gen={version:'jahdb-mobility-and-fall-prevention-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('mobility-and-fall-prevention',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
