(function(){'use strict';
/* JAH The De-Extinction Technologies Future Technology Database — Signature Edition generator — jahdb-"futuretech-43-de-extinction-technologies-signature"-1.0.
   Property of Justin Addam Higgins (JAH).
   Signature Edition: every seeded archive record is a Signature original (src=signature).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT43-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
  "Foundations": [
    "Fossils: reading extinction (Signature Edition)",
    "The dodo: the icon of loss (Signature Edition)",
    "The great auk (Signature Edition)",
    "Passenger pigeons (Signature Edition)",
    "DNA's structure (Signature Edition)",
    "Cloning: Dolly (Signature Edition)",
    "Mammoth DNA sequenced (Signature Edition)",
    "Ancient DNA: Pääbo's Nobel (Signature Edition)",
    "The bucardo: de-extinction's first attempt (Signature Edition)",
    "Church's mammoth project (Signature Edition)",
    "Colossal Biosciences (Signature Edition)",
    "The dire wolf pups (Signature Edition)"
  ],
  "Compounded": [
    "Thylacine project (Signature Edition)",
    "Dodo project (Signature Edition)",
    "Passenger pigeon: Revive & Restore (Signature Edition)",
    "Coral and seed banks (Signature Edition)",
    "The mammoth steppe hypothesis (Signature Edition)",
    "De-extinction ethics (Signature Edition)",
    "The quagga project (Signature Edition)",
    "Aurochs back-breeding (Signature Edition)",
    "Frozen zoos (Signature Edition)",
    "The Carolina parakeet (Signature Edition)",
    "Moa: New Zealand's giants (Signature Edition)"
  ],
  "Advanced": [
    "The Woolly Rhino in De-Extinction Science (Signature Edition)",
    "Rewilding: Oostvaardersplassen (Signature Edition)",
    "The thylacine's genome (Signature Edition)",
    "Mammoth cloning in Korea (Signature Edition)",
    "The ivory-billed woodpecker debate (Signature Edition)",
    "The ethics of proxies (Signature Edition)",
    "Saber-Toothed Cats in De-Extinction Science (Signature Edition)",
    "The first true de-extinction (Signature Edition)",
    "Ecosystem restoration with proxies (Signature Edition)",
    "The working de-extinction (Signature Edition)",
    "What extinction teaches (Signature Edition)"
  ]
};
function demoProgram(topic,field,seed){
  return "# Signature de-extinction Study \u2014 "+topic+"\n"
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
    name:topic+' \u2014 Signature de-extinction record record (generated variant)',
    title:topic,
    description:'SIGNATURE GENERATED VARIANT (boundless generator). A Signature de-extinction record record study of "'+topic+'" in '+field+'. Clearly labeled: generated variants are never archive records.',
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
var api={generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,topics:TOPICS,slug:"futuretech-43-de-extinction-technologies-signature",name:"The De-Extinction Technologies Future Technology Database — Signature Edition"};
try{
  if(typeof JAHDB!=='undefined'&&JAHDB){JAHDB.generators=JAHDB.generators||{};JAHDB.generators["futuretech-43-de-extinction-technologies-signature"]=api;JAHDB.registerGenerator&&JAHDB.registerGenerator("futuretech-43-de-extinction-technologies-signature",api);}
}catch(e){}
try{if(typeof module!=='undefined'&&module.exports){module.exports=api;}}catch(e){}
})();
