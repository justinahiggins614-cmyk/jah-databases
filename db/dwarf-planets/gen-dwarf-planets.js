(function(){'use strict';
/* JAH Dwarf Planets Database generator — jahdb-dwarf-planets-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DPL-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Dwarf Planets: An Overview", "What Is a Dwarf Planet: The IAU Definition", "The 2006 Decision: Pluto's Reclassification", "Ceres: The Dwarf Planet of the Asteroid Belt", "Pluto: The Heart of the Kuiper Belt", "Eris: The World That Changed the Rules", "Makemake: The Bright Kuiper World", "Haumea: The Spinning Football World", "Hydrostatic Equilibrium: Round by Gravity", "Clearing the Neighborhood: The Third Rule", "Dwarf Planet Candidates: The Waiting List"], "Compounded": ["Dawn at Ceres: Bright Spots and Ahuna Mons", "Pluto's Moons: Charon, Nix, Hydra, Kerberos, Styx", "New Horizons: The 2015 Pluto Flyby", "Sputnik Planitia: Pluto's Nitrogen Heart", "Eris and Dysnomia: The Heavyweight Pair", "Haumea's Ring and Record Spin", "Makemake's Moon MK2", "Orcus and Vanth: The Anti-Pluto", "Sedna: Gateway to the Inner Oort Cloud", "Quaoar: Rings Beyond the Limit", "Gonggong: The Red Dwarf World", "Dwarf Planet Atmospheres: Thin and Seasonal"], "Advanced": ["The Math of Roundness: Hydrostatic Equilibrium", "IAU Resolutions 5A and 6A: Reading the Text", "The Planet Debate: Stern vs. the IAU", "Pluto's Geology in Depth: Glaciers of Nitrogen", "Cryovolcanism on Dwarf Worlds", "Binary Dwarf Systems: Formation and Fate", "Finding New Dwarfs: Survey Methods", "Naming the Dwarf Planets: IAU Conventions", "Future Missions: The Road Ahead", "The Outer System Inventory: Counting Dwarfs", "Why Dwarf Planets Matter"]};
var KIND="dwarf planet record";
var SRC="public-harvest";
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
var gen={version:"jahdb-dwarf-planets-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("dwarf-planets",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
