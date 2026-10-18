(function(){'use strict';
/* JAH Mesopotamia Database generator — jahdb-mesopotamia-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MESOP-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Mesopotamia: An Overview", "Sumer and the First Cities", "Cuneiform: The First Writing", "Uruk: The First Great City", "Ziggurats: Mountains of the Gods", "The Code of Hammurabi", "Sargon of Akkad: The First Empire", "Babylon: The Great City", "Assyria: The Empire of Iron", "Irrigation: Farming the Desert", "The Wheel and the Sail"], "Compounded": ["Ur of the Chaldees", "Lagash and Umma: The First Border War", "Ebla: The Archive City", "Mari: The Crossroads Kingdom", "The Epic of Gilgamesh", "The Sexagesimal System: Why 60?", "Mesopotamian Astronomy", "Mesopotamian Medicine", "Trade Networks of the Bronze Age", "Cylinder Seals: The First Signatures", "Scribal Schools: The First Education", "The Amarna Diplomacy"], "Advanced": ["The Neo-Babylonian Empire", "The Fall of Babylon to Persia", "Babylonian Mathematics", "Water Management and Canals", "The Library of Ashurbanipal", "Assyrian Siege Warfare", "The Hanging Gardens Debate", "Mesopotamian Religion and Gods", "Daily Life in Babylon", "The Kassites and the Middle Period", "Mesopotamia's Legacy: What We Kept"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — mesopotamia demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — mesopotamia record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A mesopotamia record of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"mesopotamia-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-mesopotamia-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("mesopotamia",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
