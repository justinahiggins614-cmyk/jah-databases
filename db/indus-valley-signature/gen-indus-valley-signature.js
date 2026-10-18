(function(){'use strict';
/* JAH Signature Indus Valley Database generator — jahdb-indus-valley-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-INDUSS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Indus Valley: An Overview (Signature Edition)", "Mohenjo-daro: The Mound of the Dead (Signature Edition)", "Harappa: The Type Site (Signature Edition)", "The Great Bath (Signature Edition)", "The Undeciphered Script (Signature Edition)", "Urban Planning: Streets and Drains (Signature Edition)", "Lothal: The Dockyard (Signature Edition)", "Dholavira: The Desert City (Signature Edition)", "Standardized Weights (Signature Edition)", "Cotton: The Harappan Crop (Signature Edition)", "Mehrgarh: The Beginning (Signature Edition)"], "Compounded": ["Trade with Mesopotamia: Meluhha (Signature Edition)", "The Seals: Art and Administration (Signature Edition)", "Bead-Making: The Harappan Industry (Signature Edition)", "Bronze and Copper Working (Signature Edition)", "The Priest-King Statue (Signature Edition)", "Rakhigarhi: The Largest Site (Signature Edition)", "Harappan Religion (Signature Edition)", "The Cemetery H Culture (Signature Edition)", "Climate and the Rivers (Signature Edition)", "The Vedic Transition (Signature Edition)", "Harappan Toys and Games (Signature Edition)", "What the Harappans Teach (Signature Edition)"], "Advanced": ["The Dockyard Debate (Signature Edition)", "Cracking the Script: The Statistical Attack (Signature Edition)", "The Sarasvati River Question (Signature Edition)", "Harappan Health and Medicine (Signature Edition)", "Textiles: What the Harappans Wore (Signature Edition)", "Pottery: The Black-on-Red Ware (Signature Edition)", "The Late Harappan Regional Cultures (Signature Edition)", "Did the Harappans Do Astronomy? (Signature Edition)", "Women in Harappan Society (Signature Edition)", "Floods at Mohenjo-daro (Signature Edition)", "Legacy: Crops, Crafts, and Genes (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — indus-valley-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — indus valley record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A indus valley record of "'+topic+'" in '+field+'. Signature original sample are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:false,
    signature_label:'Signature original - created in the Signature system; not a public record.',
    disclaimer:'Signature original sample — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"indus-valley-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-indus-valley-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("indus-valley-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
