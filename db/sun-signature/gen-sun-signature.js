(function(){'use strict';
/* JAH Signature Sun Database generator — jahdb-sun-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SUNS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Fusion Core: The Signature Reading (Signature Edition)", "The Sunspot Cycle: The Signature Reading (Signature Edition)", "The Corona's Heat: The Signature Reading (Signature Edition)", "The Solar Wind: The Signature Reading (Signature Edition)", "The Photosphere: The Signature Reading (Signature Edition)", "The Chromosphere: The Signature Reading (Signature Edition)", "Solar Flares: The Signature Reading (Signature Edition)", "CMEs: The Signature Reading (Signature Edition)", "The Eclipse: The Signature Reading (Signature Edition)", "The Neutrinos: The Signature Reading (Signature Edition)", "The 99.8%: The Signature Reading (Signature Edition)"], "Compounded": ["The Differential Rotation: The Signature Reading (Signature Edition)", "The Sunspot's Anatomy: The Signature Reading (Signature Edition)", "The Maunder Minimum: The Signature Reading (Signature Edition)", "Helioseismology: The Signature Reading (Signature Edition)", "The Tachocline: The Signature Reading (Signature Edition)", "The Solar Probe: The Signature Reading (Signature Edition)", "Space Weather: The Signature Reading (Signature Edition)", "The Heliosphere's Edge: The Signature Reading (Signature Edition)", "The G2V: The Signature Reading (Signature Edition)", "The 8 Minutes: The Signature Reading (Signature Edition)", "The Sun's Habitable Zone: The Signature Reading (Signature Edition)", "The 4.6 Gyr: The Signature Reading (Signature Edition)"], "Advanced": ["The pp Chain Detail: The Signature Reading (Signature Edition)", "The CNO: The Signature Reading (Signature Edition)", "The Radiative Zone: The Signature Reading (Signature Edition)", "The Convective Zone: The Signature Reading (Signature Edition)", "The Coronal Heating Debate: The Signature Reading (Signature Edition)", "The Solar Dynamo Model: The Signature Reading (Signature Edition)", "The Red Giant Fate: The Signature Reading (Signature Edition)", "The White Dwarf After: The Signature Reading (Signature Edition)", "The Stellar Context: The Signature Reading (Signature Edition)", "Why the Sun Endures: The Signature Closing (Signature Edition)", "The 1 AU: The Signature Note (Signature Edition)"]};
var KIND="sun record";
var SRC="signature";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — sample demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
  var rec={
    id:id,
    name:topic+' — '+KIND,
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A '+KIND+' of "'+topic+'" in '+field+'. Generated sample records are clearly labeled and never presented as archive records.',
    field:field,
    src:SRC,
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"sample-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
  if(SRC==='signature')rec.signature_label='Signature original - created in the Signature system; not a public record.';
  return rec;
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
var gen={version:"jahdb-sun-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("sun-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
