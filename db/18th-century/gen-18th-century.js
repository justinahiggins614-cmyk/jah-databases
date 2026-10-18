(function(){'use strict';
/* JAH 18th Century Database generator — jahdb-18th-century-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-18THC-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The 18th Century: An Overview", "The Enlightenment", "The American Revolution", "The French Revolution", "The Early Industrial Revolution", "James Watt and the Steam Engine", "The Seven Years' War", "Captain James Cook's Voyages", "The United States Constitution", "The Haitian Revolution Begins", "The Gregorian Calendar Spreads"], "Compounded": ["The War of the Spanish Succession", "The South Sea Bubble", "Peter the Great's Legacy and the Russian Empire", "The Rise of Prussia", "Diderot's Encyclopedia", "Mozart and the Classical Age", "Adam Smith: The Wealth of Nations", "The Partitions of Poland", "The Cotton Gin", "Edward Jenner and Vaccination", "Napoleon's Rise", "The Qing Dynasty at Its Height"], "Advanced": ["The Diplomatic Revolution of 1756", "Solving the Longitude Problem", "Linnaeus and the System of Nature", "The Steam Engine's Economics", "Kant and the Late Enlightenment", "The Abolition Movement Begins", "The Scientific Institution", "The Agricultural Revolution of the 1700s", "The Global Slave Trade at Its Peak", "The First Factories", "The Century Turns: 1800 in Review"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — 18th-century demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — century record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A century record of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"18th-century-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-18th-century-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("18th-century",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
