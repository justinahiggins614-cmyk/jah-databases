(function(){'use strict';
/* JAH The Digital Telepathy Future Technology Database — Signature Edition generator — jahdb-"futuretech-31-digital-telepathy-signature"-1.0.
   Property of Justin Addam Higgins (JAH).
   Signature Edition: every seeded archive record is a Signature original (src=signature).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT31-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
  "Foundations": [
    "Telepathy in folklore (Signature Edition)",
    "Myers coins 'telepathy' (Signature Edition)",
    "Rhine's ESP experiments (Signature Edition)",
    "The Ganzfeld debates (Signature Edition)",
    "Brain-to-brain in rats (Signature Edition)",
    "Human brain-to-brain: the game (Signature Edition)",
    "The 2014 conscious transmission (Signature Edition)",
    "BCI text relays (Signature Edition)",
    "TMS: writing to the brain (Signature Edition)",
    "Ultrasound neuromodulation (Signature Edition)",
    "Bidirectional BTBI (Signature Edition)",
    "The ethics of brain-to-brain (Signature Edition)"
  ],
  "Compounded": [
    "Mesmer and animal magnetism (Signature Edition)",
    "The telegraph: thought at a distance (Signature Edition)",
    "The telephone: voices across wires (Signature Edition)",
    "Radio: broadcasting thought (Signature Edition)",
    "The internet: minds linked by text (Signature Edition)",
    "Multi-person brain networks (Signature Edition)",
    "Neural dust and write-in futures (Signature Edition)",
    "The shared dream experiment (Signature Edition)",
    "Telepathic gaming (Signature Edition)",
    "The consent firewall (Signature Edition)",
    "Group minds for science (Signature Edition)"
  ],
  "Advanced": [
    "Telepathy and power (Signature Edition)",
    "High-bandwidth neural write-in (projection) (Signature Edition)",
    "Shared sensorimotor experience (Signature Edition)",
    "The hive mind question (Signature Edition)",
    "Telepathic consent protocols (Signature Edition)",
    "Brain-to-brain language (Signature Edition)",
    "The end of misunderstanding (Signature Edition)",
    "Telepathy and warfare (the refusal) (Signature Edition)",
    "The locked-in bridge: telepathy's first users (Signature Edition)",
    "The working digital telepathy (Signature Edition)",
    "A world that thinks together (Signature Edition)"
  ]
};
function demoProgram(topic,field,seed){
  return "# Signature digital telepathy Study \u2014 "+topic+"\n"
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
    name:topic+' \u2014 Signature digital telepathy record record (generated variant)',
    title:topic,
    description:'SIGNATURE GENERATED VARIANT (boundless generator). A Signature digital telepathy record record study of "'+topic+'" in '+field+'. Clearly labeled: generated variants are never archive records.',
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
var api={generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,topics:TOPICS,slug:"futuretech-31-digital-telepathy-signature",name:"The Digital Telepathy Future Technology Database — Signature Edition"};
try{
  if(typeof JAHDB!=='undefined'&&JAHDB){JAHDB.generators=JAHDB.generators||{};JAHDB.generators["futuretech-31-digital-telepathy-signature"]=api;JAHDB.registerGenerator&&JAHDB.registerGenerator("futuretech-31-digital-telepathy-signature",api);}
}catch(e){}
try{if(typeof module!=='undefined'&&module.exports){module.exports=api;}}catch(e){}
})();
