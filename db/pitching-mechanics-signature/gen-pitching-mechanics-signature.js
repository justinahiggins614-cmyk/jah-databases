(function(){'use strict';
/* JAH Pitching Mechanics Signature Database generator — jahdb-pitching-mechanics-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PITCHMS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Four-Seam Fastball Grip (Signature Edition)", "The Windup (Signature Edition)", "The Stretch (Signature Edition)", "Balance Point (Signature Edition)", "Stride and Landing (Signature Edition)", "Arm Action and Release (Signature Edition)", "Follow-Through (Signature Edition)", "Throwing to Bases (Pickoff Move) (Signature Edition)", "Fielding the Position (PFP) (Signature Edition)", "Pitch Count Basics (Signature Edition)", "Warm-Up and Arm Care (Signature Edition)"], "Compounded": ["Two-Seam Fastball (Sinker) (Signature Edition)", "Changeup Grip and Arm Speed (Signature Edition)", "Curveball (12-6) (Signature Edition)", "Slider Grip (Signature Edition)", "Cutter (Signature Edition)", "Pitch Sequencing Basics (Signature Edition)", "Holding Runners (Signature Edition)", "Pitching from Behind in Count (Signature Edition)", "Attacking Hitter Weaknesses (Signature Edition)", "The Slide Step (Signature Edition)", "Bunting Defense (Signature Edition)", "Covering First (Signature Edition)"], "Advanced": ["Spin Rate and Spin Efficiency (Signature Edition)", "Tunneling Pitches (Signature Edition)", "Biomechanical Load Management (Signature Edition)", "Reading Swings Mid-At-Bat (Signature Edition)", "Pitching with Runners in Scoring Position (Signature Edition)", "Playoff and High-Leverage Approach (Signature Edition)", "Developing a New Pitch (Signature Edition)", "High-Speed Video Analysis (Signature Edition)", "Catcher-Pitcher Game Calling (Signature Edition)", "Elite Running-Game Control (Signature Edition)", "Comeback Mechanics After Injury (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# pitch-arsenal-demo \u2014 "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record \u2014 structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' \u2014 pitching mechanics record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A pitching mechanics record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"pitch-arsenal-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-pitching-mechanics-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('pitching-mechanics-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
