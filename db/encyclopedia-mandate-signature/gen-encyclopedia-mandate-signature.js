(function(){'use strict';
/* JAH The Mandate Encyclopedia Database (Signature Edition) generator — jahdb-encyclopedia-mandate-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EMANS-";
var FIELDS=["Physics Laws", "Astronomy & Cosmology", "Earth Systems", "Cell & Molecular Biology", "Life Systems & Immunity", "Environment & Remediation", "Signature Technology", "Signature Genetics", "Signature Cosmology"];
var TOPICS={"Physics Laws": ["The Mandate Encyclopedia: structural study 1 \u2014 Physics Laws", "The Mandate Encyclopedia: structural study 2 \u2014 Physics Laws", "The Mandate Encyclopedia: structural study 3 \u2014 Physics Laws", "The Mandate Encyclopedia: structural study 4 \u2014 Physics Laws", "The Mandate Encyclopedia: structural study 5 \u2014 Physics Laws", "The Mandate Encyclopedia: structural study 6 \u2014 Physics Laws"], "Astronomy & Cosmology": ["The Mandate Encyclopedia: structural study 1 \u2014 Astronomy & Cosmology", "The Mandate Encyclopedia: structural study 2 \u2014 Astronomy & Cosmology", "The Mandate Encyclopedia: structural study 3 \u2014 Astronomy & Cosmology", "The Mandate Encyclopedia: structural study 4 \u2014 Astronomy & Cosmology", "The Mandate Encyclopedia: structural study 5 \u2014 Astronomy & Cosmology", "The Mandate Encyclopedia: structural study 6 \u2014 Astronomy & Cosmology"], "Earth Systems": ["The Mandate Encyclopedia: structural study 1 \u2014 Earth Systems", "The Mandate Encyclopedia: structural study 2 \u2014 Earth Systems", "The Mandate Encyclopedia: structural study 3 \u2014 Earth Systems", "The Mandate Encyclopedia: structural study 4 \u2014 Earth Systems", "The Mandate Encyclopedia: structural study 5 \u2014 Earth Systems", "The Mandate Encyclopedia: structural study 6 \u2014 Earth Systems"], "Cell & Molecular Biology": ["The Mandate Encyclopedia: structural study 1 \u2014 Cell & Molecular Biology", "The Mandate Encyclopedia: structural study 2 \u2014 Cell & Molecular Biology", "The Mandate Encyclopedia: structural study 3 \u2014 Cell & Molecular Biology", "The Mandate Encyclopedia: structural study 4 \u2014 Cell & Molecular Biology", "The Mandate Encyclopedia: structural study 5 \u2014 Cell & Molecular Biology", "The Mandate Encyclopedia: structural study 6 \u2014 Cell & Molecular Biology"], "Life Systems & Immunity": ["The Mandate Encyclopedia: structural study 1 \u2014 Life Systems & Immunity", "The Mandate Encyclopedia: structural study 2 \u2014 Life Systems & Immunity", "The Mandate Encyclopedia: structural study 3 \u2014 Life Systems & Immunity", "The Mandate Encyclopedia: structural study 4 \u2014 Life Systems & Immunity", "The Mandate Encyclopedia: structural study 5 \u2014 Life Systems & Immunity", "The Mandate Encyclopedia: structural study 6 \u2014 Life Systems & Immunity"], "Environment & Remediation": ["The Mandate Encyclopedia: structural study 1 \u2014 Environment & Remediation", "The Mandate Encyclopedia: structural study 2 \u2014 Environment & Remediation", "The Mandate Encyclopedia: structural study 3 \u2014 Environment & Remediation", "The Mandate Encyclopedia: structural study 4 \u2014 Environment & Remediation", "The Mandate Encyclopedia: structural study 5 \u2014 Environment & Remediation", "The Mandate Encyclopedia: structural study 6 \u2014 Environment & Remediation"], "Signature Technology": ["The Mandate Encyclopedia: structural study 1 \u2014 Signature Technology", "The Mandate Encyclopedia: structural study 2 \u2014 Signature Technology", "The Mandate Encyclopedia: structural study 3 \u2014 Signature Technology", "The Mandate Encyclopedia: structural study 4 \u2014 Signature Technology", "The Mandate Encyclopedia: structural study 5 \u2014 Signature Technology", "The Mandate Encyclopedia: structural study 6 \u2014 Signature Technology"], "Signature Genetics": ["The Mandate Encyclopedia: structural study 1 \u2014 Signature Genetics", "The Mandate Encyclopedia: structural study 2 \u2014 Signature Genetics", "The Mandate Encyclopedia: structural study 3 \u2014 Signature Genetics", "The Mandate Encyclopedia: structural study 4 \u2014 Signature Genetics", "The Mandate Encyclopedia: structural study 5 \u2014 Signature Genetics", "The Mandate Encyclopedia: structural study 6 \u2014 Signature Genetics"], "Signature Cosmology": ["The Mandate Encyclopedia: structural study 1 \u2014 Signature Cosmology", "The Mandate Encyclopedia: structural study 2 \u2014 Signature Cosmology", "The Mandate Encyclopedia: structural study 3 \u2014 Signature Cosmology", "The Mandate Encyclopedia: structural study 4 \u2014 Signature Cosmology", "The Mandate Encyclopedia: structural study 5 \u2014 Signature Cosmology", "The Mandate Encyclopedia: structural study 6 \u2014 Signature Cosmology"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Mandate Encyclopedia — structural study\n"
   + "# Track: "+field+"\n"
   + "record = {'entry': \""+safe+"\", 'track': \""+field+"\"}\n"
   + "print(record['entry'] + ' — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — structural study record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-encyclopedia-mandate-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('encyclopedia-mandate-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
