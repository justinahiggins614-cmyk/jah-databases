(function(){'use strict';
/* JAH The Autonomous Ocean Explorers Future Technology Database — Signature Edition generator — jahdb-"futuretech-24-autonomous-ocean-explorers-signature"-1.0.
   Property of Justin Addam Higgins (JAH).
   Signature Edition: every seeded archive record is a Signature original (src=signature).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT24-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
  "Foundations": [
    "The bathysphere: first deep views (Signature Edition)",
    "The Trieste reaches Challenger Deep (Signature Edition)",
    "Alvin: the workhorse submersible (Signature Edition)",
    "Hydrothermal vents discovered (Signature Edition)",
    "Titanic found by robot (Signature Edition)",
    "ROVs: remotely operated vehicles (Signature Edition)",
    "ABE: the first autonomous explorer (Signature Edition)",
    "Gliders: months at sea (Signature Edition)",
    "Argo floats: the global array (Signature Edition)",
    "Wave Glider crosses the Pacific (Signature Edition)",
    "Saildrone's hurricane missions (Signature Edition)",
    "Mapping the seafloor: Seabed 2030 (Signature Edition)"
  ],
  "Compounded": [
    "Hadal landers (Signature Edition)",
    "Environmental DNA sampling (Signature Edition)",
    "Deep-sea mining prospectors (Signature Edition)",
    "Ocean cleanup robots (Signature Edition)",
    "Bioluminescence hunters (Signature Edition)",
    "Coral reef guardians (Signature Edition)",
    "Under-ice explorers (Signature Edition)",
    "Jason and Hercules: the workhorse ROVs (Signature Edition)",
    "The Ocean Census: 100,000 species (Signature Edition)",
    "The hadal swarm (projection) (Signature Edition)",
    "Living ocean digital twin (Signature Edition)"
  ],
  "Advanced": [
    "New species by the thousand (Signature Edition)",
    "Deep-sea vents as pharmacies (Signature Edition)",
    "Mineral mapping for the green transition (Signature Edition)",
    "Tsunami and quake warning fleets (Signature Edition)",
    "The ocean internet (Signature Edition)",
    "Autonomous research vessels (Signature Edition)",
    "Protecting the deep from ourselves (Signature Edition)",
    "The working ocean explorer fleet (Signature Edition)",
    "The fully known ocean (Signature Edition)",
    "What the deep teaches (Signature Edition)",
    "The ocean's memory (Signature Edition)"
  ]
};
function demoProgram(topic,field,seed){
  return "# Signature ocean explorer Study \u2014 "+topic+"\n"
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
    name:topic+' \u2014 Signature ocean explorer record record (generated variant)',
    title:topic,
    description:'SIGNATURE GENERATED VARIANT (boundless generator). A Signature ocean explorer record record study of "'+topic+'" in '+field+'. Clearly labeled: generated variants are never archive records.',
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
var api={generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,topics:TOPICS,slug:"futuretech-24-autonomous-ocean-explorers-signature",name:"The Autonomous Ocean Explorers Future Technology Database — Signature Edition"};
try{
  if(typeof JAHDB!=='undefined'&&JAHDB){JAHDB.generators=JAHDB.generators||{};JAHDB.generators["futuretech-24-autonomous-ocean-explorers-signature"]=api;JAHDB.registerGenerator&&JAHDB.registerGenerator("futuretech-24-autonomous-ocean-explorers-signature",api);}
}catch(e){}
try{if(typeof module!=='undefined'&&module.exports){module.exports=api;}}catch(e){}
})();
