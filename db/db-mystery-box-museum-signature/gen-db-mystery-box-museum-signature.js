(function(){'use strict';
/* JAH The Mystery Box Museum Signature Database generator — jahdb-db-mystery-box-museum-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MMBMS-";
var FIELDS=["Instruments","Containers","Relics"];
var TOPICS={
 "Instruments": [
  "The Singing Bowl (Signature Edition) \u2014 Instruments",
  "The Signature Method for The Singing Bowl \u2014 Instruments",
  "The Brass Astrolabe (Signature Edition) \u2014 Instruments",
  "The Signature Method for The Brass Astrolabe \u2014 Instruments",
  "The Silent Music Box (Signature Edition) \u2014 Instruments",
  "The Signature Method for The Silent Music Box \u2014 Instruments",
  "The Compass That Points South (Signature Edition) \u2014 Instruments",
  "The Signature Method for The Compass That Points South \u2014 Instruments",
  "The Sextant With Two Scales (Signature Edition) \u2014 Instruments",
  "The Signature Method for The Sextant With Two Scales \u2014 Instruments",
  "The Typewriter With One Key (Signature Edition) \u2014 Instruments",
  "The Signature Method for The Typewriter With One Key \u2014 Instruments",
  "The Globe With an Extra Continent (Signature Edition) \u2014 Instruments",
  "The Signature Method for The Globe With an Extra Continent \u2014 Instruments",
  "The Hourglass That Runs Up (Signature Edition) \u2014 Instruments",
  "The Signature Method for The Hourglass That Runs Up \u2014 Instruments",
  "The Lantern That Burns Cold (Signature Edition) \u2014 Instruments",
  "The Signature Method for The Lantern That Burns Cold \u2014 Instruments"
 ],
 "Containers": [
  "The Locked Diary (Signature Edition) \u2014 Containers",
  "The Signature Method for The Locked Diary \u2014 Containers",
  "The Locket With No Portrait (Signature Edition) \u2014 Containers",
  "The Signature Method for The Locket With No Portrait \u2014 Containers",
  "The Key That Opens Nothing (Signature Edition) \u2014 Containers",
  "The Signature Method for The Key That Opens Nothing \u2014 Containers"
 ],
 "Relics": [
  "The Scrimshaw Tooth (Signature Edition) \u2014 Relics",
  "The Signature Method for The Scrimshaw Tooth \u2014 Relics",
  "The Coded Quilt (Signature Edition) \u2014 Relics",
  "The Signature Method for The Coded Quilt \u2014 Relics",
  "The Festival Mask (Signature Edition) \u2014 Relics",
  "The Signature Method for The Festival Mask \u2014 Relics",
  "The Chess Set With 33 Pieces (Signature Edition) \u2014 Relics",
  "The Signature Method for The Chess Set With 33 Pieces \u2014 Relics",
  "The Doll With Real Tears (Signature Edition) \u2014 Relics",
  "The Signature Method for The Doll With Real Tears \u2014 Relics"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Mystery Box Study — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
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
    name:topic+' — mystery box exhibit record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A mystery box exhibit record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
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
var gen={version:'jahdb-db-mystery-box-museum-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-mystery-box-museum-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
