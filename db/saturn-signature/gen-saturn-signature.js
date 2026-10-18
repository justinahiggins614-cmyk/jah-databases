(function(){'use strict';
/* JAH Signature Saturn Database generator — jahdb-saturn-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SATS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Rings: The Signature Reading (Signature Edition)", "Titan: The Signature Reading (Signature Edition)", "Enceladus: The Signature Reading (Signature Edition)", "Cassini: The Signature Reading (Signature Edition)", "The Hexagon: The Signature Reading (Signature Edition)", "Rhea, Dione, Tethys: The Signature Reading (Signature Edition)", "Mimas: The Signature Reading (Signature Edition)", "Iapetus: The Signature Reading (Signature Edition)", "Hyperion: The Signature Reading (Signature Edition)", "Phoebe: The Signature Reading (Signature Edition)", "The Seasons: The Signature Reading (Signature Edition)"], "Compounded": ["The Rings' Age: The Signature Reading (Signature Edition)", "The Rings' Origin: The Signature Reading (Signature Edition)", "The Shepherds: The Signature Reading (Signature Edition)", "The Spokes: The Signature Reading (Signature Edition)", "The E Ring: The Signature Reading (Signature Edition)", "Titan's Lakes: The Signature Reading (Signature Edition)", "Titan's Dunes: The Signature Reading (Signature Edition)", "Enceladus's Ocean: The Signature Reading (Signature Edition)", "The Plumes' Chemistry: The Signature Reading (Signature Edition)", "The 29-Year Year: The Signature Reading (Signature Edition)", "The Low Density: The Signature Reading (Signature Edition)", "The Storms: The Signature Reading (Signature Edition)"], "Advanced": ["Saturn's Interior: The Signature Reading (Signature Edition)", "The Magnetic Field: The Signature Reading (Signature Edition)", "The Ring Rain: The Signature Reading (Signature Edition)", "The Propellers: The Signature Reading (Signature Edition)", "The F Ring: The Signature Reading (Signature Edition)", "Titan's Future: The Signature Reading (Signature Edition)", "The Moon Formation: The Signature Reading (Signature Edition)", "The Grand Finale Science: The Signature Reading (Signature Edition)", "The Night Sky: The Signature Reading (Signature Edition)", "Why Saturn Endures: The Signature Closing (Signature Edition)", "The 29.4-Year Year: The Signature Note (Signature Edition)"]};
var KIND="saturn record";
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
var gen={version:"jahdb-saturn-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("saturn-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
