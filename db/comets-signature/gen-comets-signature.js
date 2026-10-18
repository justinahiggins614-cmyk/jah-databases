(function(){'use strict';
/* JAH Signature Comets Database generator — jahdb-comets-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-COMS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Dirty Snowballs: The Signature Reading (Signature Edition)", "Halley: The Signature Reading (Signature Edition)", "Hale-Bopp: The Signature Reading (Signature Edition)", "NEOWISE: The Signature Reading (Signature Edition)", "Two Tails: The Signature Reading (Signature Edition)", "Short vs. Long Period: The Signature Reading (Signature Edition)", "The Oort Cloud: The Signature Reading (Signature Edition)", "Rosetta: The Signature Reading (Signature Edition)", "Deep Impact: The Signature Reading (Signature Edition)", "Sungrazers: The Signature Reading (Signature Edition)", "Borisov: The Signature Reading (Signature Edition)"], "Compounded": ["'Oumuamua: The Signature Reading (Signature Edition)", "Outgassing: The Signature Reading (Signature Edition)", "Encke: The Signature Reading (Signature Edition)", "Tempel-Tuttle: The Signature Reading (Signature Edition)", "Swift-Tuttle: The Signature Reading (Signature Edition)", "The Water Debate: The Signature Reading (Signature Edition)", "Stardust: The Signature Reading (Signature Edition)", "Giotto: The Signature Reading (Signature Edition)", "Nucleus Fluff: The Signature Reading (Signature Edition)", "The Dirty Snowball at 75: The Signature Note (Signature Edition)", "Comet Showers: The Signature Reading (Signature Edition)", "Lovejoy: The Signature Reading (Signature Edition)"], "Advanced": ["Orbital Elements: The Signature Reading (Signature Edition)", "Kepler's Law: The Signature Reading (Signature Edition)", "The Oort Spike: The Signature Reading (Signature Edition)", "Dynamically New: The Signature Reading (Signature Edition)", "Disintegration: The Signature Reading (Signature Edition)", "Coma Spectroscopy: The Signature Reading (Signature Edition)", "Comet Interceptor: The Signature Reading (Signature Edition)", "Designations: The Signature Reading (Signature Edition)", "The Census: The Signature Reading (Signature Edition)", "The Great Comets: The Signature Closing (Signature Edition)", "The Snow Line: The Signature Note (Signature Edition)"]};
var KIND="comet record";
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
var gen={version:"jahdb-comets-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("comets-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
