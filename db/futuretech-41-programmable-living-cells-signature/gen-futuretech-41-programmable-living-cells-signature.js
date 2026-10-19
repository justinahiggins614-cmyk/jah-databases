(function(){'use strict';
/* JAH The Programmable Living Cells Future Technology Database — Signature Edition generator — jahdb-"futuretech-41-programmable-living-cells-signature"-1.0.
   Property of Justin Addam Higgins (JAH).
   Signature Edition: every seeded archive record is a Signature original (src=signature).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT41-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
  "Foundations": [
    "Cells as machines: the cell theory (Signature Edition)",
    "The operon: nature's circuit (Signature Edition)",
    "Recombinant DNA: reprogramming cells (Signature Edition)",
    "The toggle switch in living cells (Signature Edition)",
    "The repressilator clock in cells (Signature Edition)",
    "Quorum sensing (Signature Edition)",
    "CAR-T: programmed immune cells (Signature Edition)",
    "SynNotch: custom cell receptors (Signature Edition)",
    "CRISPR circuits (Signature Edition)",
    "Bacterial biosensors (Signature Edition)",
    "Therapeutic bacteria (Signature Edition)",
    "Cellular recorders (Signature Edition)"
  ],
  "Compounded": [
    "Xenobots (Signature Edition)",
    "Anthrobots (Signature Edition)",
    "Organoid intelligence (Signature Edition)",
    "Pong-playing neurons (Signature Edition)",
    "DNA data storage in cells (Signature Edition)",
    "Kill switches (Signature Edition)",
    "Insulin from engineered bacteria (Signature Edition)",
    "Optogenetic cell control (Signature Edition)",
    "Bacterial photography (Signature Edition)",
    "Programmed cell death as a tool (Signature Edition)",
    "The transcriptor: cellular transistor (Signature Edition)"
  ],
  "Advanced": [
    "Mammalian cell classifiers (Signature Edition)",
    "T-cell exhaustion engineering (Signature Edition)",
    "Bacterial drug delivery (Signature Edition)",
    "Cellular therapeutics for diabetes (Signature Edition)",
    "The programmed stem cell (Signature Edition)",
    "Cells as sensors everywhere (Signature Edition)",
    "The sense-and-respond cancer cell (Signature Edition)",
    "Programmable microbiomes (Signature Edition)",
    "Cells that build materials (Signature Edition)",
    "The working programmable cell (Signature Edition)",
    "Life, programmed (Signature Edition)"
  ]
};
function demoProgram(topic,field,seed){
  return "# Signature programmable cell Study \u2014 "+topic+"\n"
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
    name:topic+' \u2014 Signature programmable cell record record (generated variant)',
    title:topic,
    description:'SIGNATURE GENERATED VARIANT (boundless generator). A Signature programmable cell record record study of "'+topic+'" in '+field+'. Clearly labeled: generated variants are never archive records.',
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
var api={generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,topics:TOPICS,slug:"futuretech-41-programmable-living-cells-signature",name:"The Programmable Living Cells Future Technology Database — Signature Edition"};
try{
  if(typeof JAHDB!=='undefined'&&JAHDB){JAHDB.generators=JAHDB.generators||{};JAHDB.generators["futuretech-41-programmable-living-cells-signature"]=api;JAHDB.registerGenerator&&JAHDB.registerGenerator("futuretech-41-programmable-living-cells-signature",api);}
}catch(e){}
try{if(typeof module!=='undefined'&&module.exports){module.exports=api;}}catch(e){}
})();
