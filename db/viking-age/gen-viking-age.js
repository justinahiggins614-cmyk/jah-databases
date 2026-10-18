(function(){'use strict';
/* JAH Viking Age Database generator — jahdb-viking-age-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-VIKING-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Viking Age: An Overview", "Lindisfarne 793", "The Longship", "Norse Mythology: Odin and Thor", "Runes: The Norse Alphabet", "Leif Erikson and Vinland", "The Danelaw", "Harald Hardrada and Stamford Bridge", "The Thing: Norse Democracy", "Norse Mythology: The Nine Worlds", "Viking Ships: Burials"], "Compounded": ["Raiders vs. Traders", "Dublin: The Norse City", "York: Jorvik", "The Rus: Vikings in the East", "Normandy: Rollo's Grant", "Iceland: The Commonwealth", "Greenland: The Norse Colony", "The Varangian Guard", "Norse Women", "The Berserkers", "Norse Law and Feud", "Skaldic Poetry"], "Advanced": ["Sunstones and Norse Navigation", "The Ulfberht Swords", "The Jelling Stones", "Harald Bluetooth and Denmark", "Cnut the Great's North Sea Empire", "The Conversion to Christianity", "Norse Shipbuilding", "The Oseberg Ship", "The Shield Wall", "The Norse Road to Baghdad", "The Viking Legacy"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — viking-age demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    description:'SAMPLE RECORD (generated — structural sample). A viking age record of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"viking-age-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-viking-age-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("viking-age",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
