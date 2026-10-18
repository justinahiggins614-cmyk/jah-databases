(function(){'use strict';
/* JAH Indus Valley Database generator — jahdb-indus-valley-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-INDUS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Indus Valley: An Overview", "Mohenjo-daro: The Mound of the Dead", "Harappa: The Type Site", "The Great Bath", "The Undeciphered Script", "Urban Planning: Streets and Drains", "Lothal: The Dockyard", "Dholavira: The Desert City", "Standardized Weights", "Cotton: The Harappan Crop", "Mehrgarh: The Beginning"], "Compounded": ["Trade with Mesopotamia: Meluhha", "The Seals: Art and Administration", "Bead-Making: The Harappan Industry", "Bronze and Copper Working", "The Priest-King Statue", "Rakhigarhi: The Largest Site", "Harappan Religion", "The Cemetery H Culture", "Climate and the Rivers", "The Vedic Transition", "Harappan Toys and Games", "What the Harappans Teach"], "Advanced": ["The Dockyard Debate", "Cracking the Script: The Statistical Attack", "The Sarasvati River Question", "Harappan Health and Medicine", "Textiles: What the Harappans Wore", "Pottery: The Black-on-Red Ware", "The Late Harappan Regional Cultures", "Did the Harappans Do Astronomy?", "Women in Harappan Society", "Floods at Mohenjo-daro", "Legacy: Crops, Crafts, and Genes"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — indus-valley demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    description:'SAMPLE RECORD (generated — structural sample). A indus valley record of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"indus-valley-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-indus-valley-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("indus-valley",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
