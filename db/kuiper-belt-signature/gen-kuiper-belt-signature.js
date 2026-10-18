(function(){'use strict';
/* JAH Signature Kuiper Belt Database generator — jahdb-kuiper-belt-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-KB2S-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["The Kuiper Belt: The Signature Reading (Signature Edition)", "Pluto, King of the Belt: The Signature Reading (Signature Edition)", "Charon, Pluto's Partner: The Signature Reading (Signature Edition)", "Arrokoth: The Signature Reading (Signature Edition)", "Eris, the Troublemaker: The Signature Reading (Signature Edition)", "Makemake, the Bright One: The Signature Reading (Signature Edition)", "Haumea, the Football: The Signature Reading (Signature Edition)", "Quaoar: The Signature Reading (Signature Edition)", "Orcus: The Signature Reading (Signature Edition)", "Sedna: The Signature Reading (Signature Edition)", "Gonggong: The Signature Reading (Signature Edition)"], "Compounded": ["The Classical Belt: The Signature Reading (Signature Edition)", "The Plutinos: The Signature Reading (Signature Edition)", "The Scattered Disk: The Signature Reading (Signature Edition)", "The Detached: The Signature Reading (Signature Edition)", "The Kuiper Cliff: The Signature Reading (Signature Edition)", "The Nice Model: The Signature Reading (Signature Edition)", "Neptune's Migration: The Signature Reading (Signature Edition)", "The Cold Classicals: The Signature Reading (Signature Edition)", "KBO Binaries: The Signature Reading (Signature Edition)", "KBO Colors: The Signature Reading (Signature Edition)", "Cryovolcanism: The Signature Reading (Signature Edition)", "Pluto's Nitrogen Seasons: The Signature Reading (Signature Edition)"], "Advanced": ["New Horizons: The Signature Reading (Signature Edition)", "Tholins: The Signature Reading (Signature Edition)", "Occultations: The Signature Reading (Signature Edition)", "The Mass Problem: The Signature Reading (Signature Edition)", "The Late Heavy Bombardment: The Signature Reading (Signature Edition)", "Planet Nine: The Signature Reading (Signature Edition)", "Jewitt and Luu: The Signature Reading (Signature Edition)", "LSST: The Signature Reading (Signature Edition)", "The Twotinos: The Signature Reading (Signature Edition)", "Triton: The Signature Reading (Signature Edition)", "Why the Belt Endures: The Signature Closing (Signature Edition)"]};
var KIND="kuiper-belt record";
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
var gen={version:"jahdb-kuiper-belt-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("kuiper-belt-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
