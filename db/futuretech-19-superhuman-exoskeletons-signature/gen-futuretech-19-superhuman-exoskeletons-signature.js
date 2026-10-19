(function(){'use strict';
/* JAH The Superhuman Exoskeletons Future Technology Database — Signature Edition generator — jahdb-"futuretech-19-superhuman-exoskeletons-signature"-1.0.
   Property of Justin Addam Higgins (JAH).
   Signature Edition: every seeded archive record is a Signature original (src=signature).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT19-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
  "Foundations": [
    "Armor: the original exoskeleton (Signature Edition)",
    "Hardiman: the first powered exoskeleton (Signature Edition)",
    "Mihajlo Pupin's early ideas (Signature Edition)",
    "The Berkeley BLEEX (Signature Edition)",
    "Ekso and the medical turn (Signature Edition)",
    "ReWalk: walking after paralysis (Signature Edition)",
    "Lockheed ONYX for soldiers (Signature Edition)",
    "SuitX and industrial exoskeletons (Signature Edition)",
    "Soft exosuits: Harvard's breakthrough (Signature Edition)",
    "Sarcos Guardian XO (Signature Edition)",
    "German Bionic and warehouse suits (Signature Edition)",
    "Exoskeletons for stroke rehab (Signature Edition)"
  ],
  "Compounded": [
    "Hero Arm: affordable bionics (Signature Edition)",
    "Powered knees and ankles (Signature Edition)",
    "Exoskeletons for the elderly (Signature Edition)",
    "The running exoskeleton (Signature Edition)",
    "Brain-controlled exoskeletons (Signature Edition)",
    "Exoskeletons in construction (Signature Edition)",
    "Superhuman strength (projection) (Signature Edition)",
    "All-day wearable power (Signature Edition)",
    "The invisible exosuit (Signature Edition)",
    "Exoskeletons for every worker (Signature Edition)",
    "Athletic exoskeletons: the debate (Signature Edition)"
  ],
  "Advanced": [
    "Military exoskeletons at scale (Signature Edition)",
    "Child-sized exoskeletons (Signature Edition)",
    "Neural-integrated exosuits (Signature Edition)",
    "Exoskeleton swarms for rescue (Signature Edition)",
    "The cost curve: exosuits for all (Signature Edition)",
    "Regulating the enhanced worker (Signature Edition)",
    "NASA X1 and the Robo-Glove (Signature Edition)",
    "Exoskeletons for caregivers and farmers (Signature Edition)",
    "The working superhuman exoskeleton (Signature Edition)",
    "Beyond human: the next body (Signature Edition)",
    "A world without heavy lifting (Signature Edition)"
  ]
};
function demoProgram(topic,field,seed){
  return "# Signature exoskeleton Study \u2014 "+topic+"\n"
   + "# Field: "+field+" | seed "+seed+"\n"
   + "record = {'title': "+JSON.stringify(topic)+", 'field': "+JSON.stringify(field)+", 'seed': "+seed+", 'src': 'signature'}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + '] (seed ' + str(r['seed']) + ')'\n"
   + "print(summarize(record))\n"
   + "print('Signature-generated variant \u2014 not an archive record.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' \u2014 Signature exoskeleton record record (generated variant)',
    title:topic,
    description:'SIGNATURE GENERATED VARIANT (boundless generator). A Signature exoskeleton record record study of "'+topic+'" in '+field+'. Clearly labeled: generated variants are never archive records.',
    field:field,
    src:'signature',
    generated:true,
    disclaimer:'Signature-generated variant \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field,seed),note:'Generated variant demo.'},
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
var api={generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,topics:TOPICS,slug:"futuretech-19-superhuman-exoskeletons-signature",name:"The Superhuman Exoskeletons Future Technology Database — Signature Edition"};
try{
  if(typeof JAHDB!=='undefined'&&JAHDB){JAHDB.generators=JAHDB.generators||{};JAHDB.generators["futuretech-19-superhuman-exoskeletons-signature"]=api;JAHDB.registerGenerator&&JAHDB.registerGenerator("futuretech-19-superhuman-exoskeletons-signature",api);}
}catch(e){}
try{if(typeof module!=='undefined'&&module.exports){module.exports=api;}}catch(e){}
})();
