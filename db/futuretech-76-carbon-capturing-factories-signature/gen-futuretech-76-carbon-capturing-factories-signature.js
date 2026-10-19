(function(){'use strict';
/* JAH The Carbon-Capturing Factories Future Technology Database — Signature Edition generator — jahdb-futuretech-76-carbon-capturing-factories-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT76-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Carbon Capturing Factories — Amine Catches Carbon (Signature Edition)", "Carbon Capturing Factories — Carbon Goes Underground (Signature Edition)", "Carbon Capturing Factories — Sleipner - First CCS (Signature Edition)", "Carbon Capturing Factories — Weyburn Monitored (Signature Edition)", "Carbon Capturing Factories — Catching Sky Carbon (Signature Edition)", "Carbon Capturing Factories — Boundary Dam (Signature Edition)", "Carbon Capturing Factories — Climeworks Founded (Signature Edition)", "Carbon Capturing Factories — Petra Nova (Signature Edition)", "Carbon Capturing Factories — First Commercial DAC (Signature Edition)", "Carbon Capturing Factories — Air to Fuel (Signature Edition)", "Carbon Capturing Factories — Orca (Signature Edition)"], "Compounded": ["Carbon Capturing Factories — $85 a Ton (Signature Edition)", "Carbon Capturing Factories — DAC Hubs Funded (Signature Edition)", "Carbon Capturing Factories — Stratos Rises (Signature Edition)", "Carbon Capturing Factories — Mammoth (Signature Edition)", "Carbon Capturing Factories — Heirloom's Limestone (Signature Edition)", "Carbon Capturing Factories — the Megaton Era (Signature Edition)", "Carbon Capturing Factories — Carbon Has a Price (Signature Edition)", "Carbon Capturing Factories — Direct Air Capture Scales (Signature Edition)", "Carbon Capturing Factories — Gigaton Capture (Signature Edition)", "Carbon Capturing Factories — $50-a-Ton Air Capture (Signature Edition)", "Carbon Capturing Factories — Carbon to Products (Signature Edition)", "Carbon Capturing Factories — The Home Carbon Unit (Signature Edition)"], "Advanced": ["Carbon Capturing Factories — The Carbon-Negative Industry (Signature Edition)", "Carbon Capturing Factories — Ocean Carbon Capture (Signature Edition)", "Carbon Capturing Factories — CO2 to Rock (Signature Edition)", "Carbon Capturing Factories — The Carbon Refinery (Signature Edition)", "Carbon Capturing Factories — Atmospheric Restoration (Signature Edition)", "Carbon Capturing Factories — Carbon-Negative Concrete (Signature Edition)", "Carbon Capturing Factories — The Drawdown Economy (Signature Edition)", "Carbon Capturing Factories — Factory Forests (Signature Edition)", "Carbon Capturing Factories — The Global Capture Grid (Signature Edition)", "Carbon Capturing Factories — The Carbon-Negative Civilization (Signature Edition)", "Carbon Capturing Factories — Everyday Capture - Working Version (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Carbon Capturing Factories study \u2014 "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record \u2014 structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — technology study record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A technology study record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-futuretech-76-carbon-capturing-factories-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-76-carbon-capturing-factories-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
