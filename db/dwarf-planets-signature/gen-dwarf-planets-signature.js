(function(){'use strict';
/* JAH Signature Dwarf Planets Database generator — jahdb-dwarf-planets-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DPLS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Pluto: The Signature Reading (Signature Edition)", "The Roundness Doctrine: A Signature Framework (Signature Edition)", "Ceres: The Signature Reading (Signature Edition)", "Eris: The Signature Reading (Signature Edition)", "The Clearing Test: A Signature Analysis (Signature Edition)", "Haumea: The Signature Reading (Signature Edition)", "Makemake: The Signature Reading (Signature Edition)", "The Candidate List: A Signature Forecast (Signature Edition)", "Sputnik Planitia: The Signature Reading (Signature Edition)", "The Binary Rule: A Signature Observation (Signature Edition)", "Cryovolcanoes: The Signature Reading (Signature Edition)"], "Compounded": ["Dawn's Legacy: The Signature Reading (Signature Edition)", "New Horizons' Legacy: The Signature Reading (Signature Edition)", "The Stern Dissent: A Signature Assessment (Signature Edition)", "Occator's Salts: The Signature Reading (Signature Edition)", "Charon: The Signature Reading (Signature Edition)", "The Tombaugh Legacy: A Signature Tribute (Signature Edition)", "Nitrogen Glaciers: The Signature Reading (Signature Edition)", "The Dysnomia Key: A Signature Note (Signature Edition)", "Sedna's Message: The Signature Reading (Signature Edition)", "The Naming Game: A Signature Commentary (Signature Edition)", "Quaoar's Rings: The Signature Reading (Signature Edition)", "The Hundred-Dwarf Future: A Signature Forecast (Signature Edition)"], "Advanced": ["Equilibrium Mathematics: The Signature Treatment (Signature Edition)", "The Prague Vote: A Signature History (Signature Edition)", "Nitrogen Seasons: The Signature Reading (Signature Edition)", "The Mass Census: A Signature Projection (Signature Edition)", "Worldhood: The Signature Definition (Signature Edition)", "The Long Census: A Signature Meditation (Signature Edition)", "The IAU's Next Move: A Signature Recommendation (Signature Edition)", "Pluto's Heart: The Signature Reading (Signature Edition)", "The In-Between: A Signature Philosophy (Signature Edition)", "The Plutino Census: A Signature Projection (Signature Edition)", "Why the Dwarfs Endure: The Signature Closing (Signature Edition)"]};
var KIND="dwarf planet record";
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
var gen={version:"jahdb-dwarf-planets-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("dwarf-planets-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
