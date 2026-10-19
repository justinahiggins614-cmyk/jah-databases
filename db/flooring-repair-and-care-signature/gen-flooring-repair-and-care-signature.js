(function(){'use strict';
/* JAH Flooring Repair and Care Database generator — jahdb-flooring-repair-and-care-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FLOORACS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Identifying Your Flooring (Signature Edition)", "Hardwood Scratch Repair (Signature Edition)", "Silencing Squeaky Floors (Signature Edition)", "Replacing Damaged Boards (Signature Edition)", "Refinishing Hardwood (Signature Edition)", "Screen and Recoat (Signature Edition)", "Laminate Floor Repairs (Signature Edition)", "Vinyl Plank Fixes (Signature Edition)", "Tile Crack Repair (Signature Edition)", "Regrouting Tile (Signature Edition)", "Carpet Stain Removal (Signature Edition)"], "Compounded": ["Carpet Patch Repair (Signature Edition)", "Stretching Loose Carpet (Signature Edition)", "Subfloor Assessment (Signature Edition)", "Moisture Testing (Signature Edition)", "Transition Strips (Signature Edition)", "Baseboards and Trim (Signature Edition)", "Furniture Protection (Signature Edition)", "Cleaning by Floor Type (Signature Edition)", "Pet Damage Prevention (Signature Edition)", "Sun Fading Management (Signature Edition)", "Water Damage Response (Signature Edition)", "Stair Treads and Risers (Signature Edition)"], "Advanced": ["Entryway Flooring Strategy (Signature Edition)", "Radiant Heat and Flooring (Signature Edition)", "Soundproofing Between Floors (Signature Edition)", "Eco-Friendly Flooring Options (Signature Edition)", "Budget Planning for Floors (Signature Edition)", "Hiring Flooring Contractors (Signature Edition)", "Seasonal Floor Care (Signature Edition)", "The Floor Maintenance Calendar (Signature Edition)", "Documenting Floor History (Signature Edition)", "Accessibility and Floors (Signature Edition)", "Teaching Floor Care (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — flooring guide demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
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
    name:topic+' — flooring guide',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A flooring guide of "'+topic+'" in '+field+'. Generated sample record are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"flooring-repair-and-care-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-flooring-repair-and-care-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("flooring-repair-and-care-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
