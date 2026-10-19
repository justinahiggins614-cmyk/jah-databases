(function(){'use strict';
/* JAH The Mobility and Fall Prevention Signature Database generator — jahdb-mobility-and-fall-prevention-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MFP-";
var FIELDS=["fall-risk-reduction","home-safety-modifications","strength-and-balance"];
var TOPICS={"fall-risk-reduction":["Signature Fall Risk Self-Assessment (Signature Edition) \u2014 fall-risk-reduction","Signature Stair Safety (Signature Edition) \u2014 fall-risk-reduction","Signature Balance Exercises (Beginner) (Signature Edition) \u2014 fall-risk-reduction","Signature Medication Fall Risks (Signature Edition) \u2014 fall-risk-reduction","Signature Vitamin D and Bones (Signature Edition) \u2014 fall-risk-reduction","Signature Getting Up After a Fall (Signature Edition) \u2014 fall-risk-reduction","Signature Fear of Falling Cycle (Signature Edition) \u2014 fall-risk-reduction","Signature Home Modification Planning (Signature Edition) \u2014 fall-risk-reduction","Signature Community Fall Programs (Signature Edition) \u2014 fall-risk-reduction","Signature Sleep and Fall Risk (Signature Edition) \u2014 fall-risk-reduction","Signature Workplace Fall Prevention (Signature Edition) \u2014 fall-risk-reduction","Signature Seasonal Fall Risks (Signature Edition) \u2014 fall-risk-reduction"],"home-safety-modifications":["Signature Home Hazard Walkthrough (Signature Edition) \u2014 home-safety-modifications","Signature Lighting for Fall Prevention (Signature Edition) \u2014 home-safety-modifications","Signature Tai Chi for Fall Prevention (Signature Edition) \u2014 home-safety-modifications","Signature Vision and Fall Risk (Signature Edition) \u2014 home-safety-modifications","Signature Bone Density (DEXA) Testing (Signature Edition) \u2014 home-safety-modifications","Signature Medical Alert Systems (Signature Edition) \u2014 home-safety-modifications","Signature Outdoor Fall Prevention (Signature Edition) \u2014 home-safety-modifications","Signature Caregiver Fall-Prevention Role (Signature Edition) \u2014 home-safety-modifications","Signature Nutrition for Muscle (Signature Edition) \u2014 home-safety-modifications","Signature The Annual Fall Review (Signature Edition) \u2014 home-safety-modifications","Signature The Mobility Action Plan (Signature Edition) \u2014 home-safety-modifications"],"strength-and-balance":["Signature Bathroom Safety Essentials (Signature Edition) \u2014 strength-and-balance","Signature Footwear for Stability (Signature Edition) \u2014 strength-and-balance","Signature Strength Training for Legs (Signature Edition) \u2014 strength-and-balance","Signature Hearing and Balance (Signature Edition) \u2014 strength-and-balance","Signature Assistive Devices Done Right (Signature Edition) \u2014 strength-and-balance","Signature Post-Fall Medical Check (Signature Edition) \u2014 strength-and-balance","Signature Exercise Class Selection (Signature Edition) \u2014 strength-and-balance","Signature Hospital Fall Prevention (Signature Edition) \u2014 strength-and-balance","Signature Hydration and Dizziness (Signature Edition) \u2014 strength-and-balance","Signature Teaching Kids Fall Safety (Signature Edition) \u2014 strength-and-balance","Signature Pet-Related Fall Hazards (Signature Edition) \u2014 strength-and-balance"]};
var KINDS="health-information record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Mobility and Fall Prevention Signature Database — generated study\n"
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
    name:topic+' — Signature generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural Signature sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['health-information record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Mobility and Fall Prevention Signature Database.',
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
var gen={version:'jahdb-mobility-and-fall-prevention-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('mobility-and-fall-prevention-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
