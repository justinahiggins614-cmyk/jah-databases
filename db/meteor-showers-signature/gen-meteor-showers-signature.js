(function(){'use strict';
/* JAH Signature Meteor Showers Database generator — jahdb-meteor-showers-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MSHRS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Perseids: The Signature Reading (Signature Edition)", "The Geminids: The Signature Reading (Signature Edition)", "The Leonids: The Signature Reading (Signature Edition)", "The Quadrantids: The Signature Reading (Signature Edition)", "The Orionids: The Signature Reading (Signature Edition)", "The Lyrids: The Signature Reading (Signature Edition)", "The Eta Aquariids: The Signature Reading (Signature Edition)", "The Taurids: The Signature Reading (Signature Edition)", "The Draconids: The Signature Reading (Signature Edition)", "The Ursids: The Signature Reading (Signature Edition)", "The Radiant: The Signature Reading (Signature Edition)"], "Compounded": ["3200 Phaethon: The Signature Reading (Signature Edition)", "The 1833 Storm: The Signature Reading (Signature Edition)", "The 1966 Storm: The Signature Reading (Signature Edition)", "Meteor Storms: The Signature Reading (Signature Edition)", "Fireballs: The Signature Reading (Signature Edition)", "Ablation: The Signature Reading (Signature Edition)", "Dust Trails: The Signature Reading (Signature Edition)", "The ZHR: The Signature Reading (Signature Edition)", "Sporadics: The Signature Reading (Signature Edition)", "Radio Meteors: The Signature Reading (Signature Edition)", "Meteor Photography: The Signature Reading (Signature Edition)", "Outbursts: The Signature Reading (Signature Edition)"], "Advanced": ["Jenniskens's Models: The Signature Reading (Signature Edition)", "The Taurid Swarm: The Signature Reading (Signature Edition)", "Daytime Showers: The Signature Reading (Signature Edition)", "Lunar Impacts: The Signature Reading (Signature Edition)", "Meteors vs. Meteorites: The Signature Reading (Signature Edition)", "The CAMS Network: The Signature Reading (Signature Edition)", "Spacecraft Risk: The Signature Reading (Signature Edition)", "The Apex: The Signature Reading (Signature Edition)", "Mars Meteors: The Signature Note (Signature Edition)", "The 2022 Tau Herculids: The Signature Note (Signature Edition)", "Why Showers Endure: The Signature Closing (Signature Edition)"]};
var KIND="meteor-shower record";
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
var gen={version:"jahdb-meteor-showers-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("meteor-showers-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
