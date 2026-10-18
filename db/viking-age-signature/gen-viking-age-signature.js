(function(){'use strict';
/* JAH Signature Viking Age Database generator — jahdb-viking-age-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-VIKINGS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Viking Age: An Overview (Signature Edition)", "Lindisfarne 793 (Signature Edition)", "The Longship (Signature Edition)", "Norse Mythology: Odin and Thor (Signature Edition)", "Runes: The Norse Alphabet (Signature Edition)", "Leif Erikson and Vinland (Signature Edition)", "The Danelaw (Signature Edition)", "Harald Hardrada and Stamford Bridge (Signature Edition)", "The Thing: Norse Democracy (Signature Edition)", "Norse Mythology: The Nine Worlds (Signature Edition)", "Viking Ships: Burials (Signature Edition)"], "Compounded": ["Raiders vs. Traders (Signature Edition)", "Dublin: The Norse City (Signature Edition)", "York: Jorvik (Signature Edition)", "The Rus: Vikings in the East (Signature Edition)", "Normandy: Rollo's Grant (Signature Edition)", "Iceland: The Commonwealth (Signature Edition)", "Greenland: The Norse Colony (Signature Edition)", "The Varangian Guard (Signature Edition)", "Norse Women (Signature Edition)", "The Berserkers (Signature Edition)", "Norse Law and Feud (Signature Edition)", "Skaldic Poetry (Signature Edition)"], "Advanced": ["Sunstones and Norse Navigation (Signature Edition)", "The Ulfberht Swords (Signature Edition)", "The Jelling Stones (Signature Edition)", "Harald Bluetooth and Denmark (Signature Edition)", "Cnut the Great's North Sea Empire (Signature Edition)", "The Conversion to Christianity (Signature Edition)", "Norse Shipbuilding (Signature Edition)", "The Oseberg Ship (Signature Edition)", "The Shield Wall (Signature Edition)", "The Norse Road to Baghdad (Signature Edition)", "The Viking Legacy (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — viking-age-signature demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — viking age record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A viking age record of "'+topic+'" in '+field+'. Signature original sample are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:false,
    signature_label:'Signature original - created in the Signature system; not a public record.',
    disclaimer:'Signature original sample — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"viking-age-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-viking-age-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("viking-age-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
