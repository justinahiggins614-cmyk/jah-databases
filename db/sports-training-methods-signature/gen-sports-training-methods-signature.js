(function(){'use strict';
/* JAH Sports Training Methods Signature Database generator — jahdb-sports-training-methods-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SPORTTRNS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The FITT Principle (Signature Edition)", "Warm-Up Science (Signature Edition)", "Cool-Down and Recovery Basics (Signature Edition)", "Aerobic Base Building (Signature Edition)", "Strength Training Basics for Athletes (Signature Edition)", "Flexibility and Mobility (Signature Edition)", "Rest Days and Sleep (Signature Edition)", "Training Logs (Signature Edition)", "Progressive Overload (Signature Edition)", "Specificity Principle (Signature Edition)", "Youth Training Guidelines (Signature Edition)"], "Compounded": ["Interval Training (HIIT) (Signature Edition)", "Periodization (Macrocycles) (Signature Edition)", "Plyometrics (Signature Edition)", "Olympic Lifts for Power (Signature Edition)", "Speed and Agility Drills (Signature Edition)", "Core Training for Sport (Signature Edition)", "Cross-Training Benefits (Signature Edition)", "Altitude Training (Signature Edition)", "Heart-Rate Zone Training (Signature Edition)", "Strength-to-Weight Optimization (Signature Edition)", "Deload Weeks (Signature Edition)", "Testing and Benchmarking (Signature Edition)"], "Advanced": ["Block Periodization (Signature Edition)", "Velocity-Based Training (Signature Edition)", "GPS Load Monitoring (Signature Edition)", "Tapering for Peak Performance (Signature Edition)", "Concurrent Training Interference (Signature Edition)", "Heat Acclimation Protocols (Signature Edition)", "Nutritional Periodization (Signature Edition)", "Travel and Jet-Lag Management (Signature Edition)", "Return After Layoff (Signature Edition)", "Individual Response Variation (Signature Edition)", "Long-Term Athlete Development Models (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# training-load-demo \u2014 "+safe+"\n"
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
    name:topic+' \u2014 training method record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A training method record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"training-load-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-sports-training-methods-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('sports-training-methods-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
