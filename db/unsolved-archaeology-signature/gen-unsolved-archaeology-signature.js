(function(){'use strict';
/* JAH The Unsolved Archaeology Signature Database generator — jahdb-unsolved-archaeology-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-USARS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Indus Script (Signature Edition) - Decipherment",
  "Linear A (Signature Edition) - Decipherment",
  "Rongorongo (Signature Edition) - Decipherment",
  "The Phaistos Disc (Signature Edition) - Decipherment",
  "The Tartaria Tablets (Signature Edition) - Decipherment",
  "The Purpose of the Nazca Lines (Signature Edition) - Monuments",
  "The Plain of Jars (Signature Edition) - Monuments",
  "Stonehenge: The Full Purpose (Signature Edition) - Monuments",
  "The Olmec Colossal Heads (Signature Edition) - Monuments",
  "Who Built the Pyramids: The Organization (Signature Edition) - Monuments",
  "The Copper Scroll Treasure (Signature Edition) - Lost Treasures"
 ],
 "Compounded": [
  "The Amber Room (Signature Edition) - Lost Treasures",
  "The Sea Peoples (Signature Edition) - Lost Peoples",
  "The Etruscan Origins (Signature Edition) - Lost Peoples",
  "The Tomb of Genghis Khan (Signature Edition) - Lost Tombs",
  "The Sutton Hoo Ship Burial (Signature Edition) - Burials",
  "The Tarim Basin Mummies (Signature Edition) - Burials",
  "The Minoan Eruption Date (Signature Edition) - Dating",
  "The Antikythera Mechanism (Signature Edition) - Technology",
  "The Baghdad Battery (Signature Edition) - Technology",
  "Roman Concrete: The Full Recipe (Signature Edition) - Technology",
  "Greek Fire (Signature Edition) - Technology",
  "The Shugborough Inscription (Signature Edition) - Decipherment"
 ],
 "Advanced": [
  "The Piri Reis Map Sources (Signature Edition) - Cartography",
  "Yonaguni: Natural or Artificial (Signature Edition) - Contested Sites",
  "The Lost Library of Alexandria (Signature Edition) - Lost Knowledge",
  "The Bronze Age Collapse (Signature Edition) - Collapses",
  "The Maya Collapse (Signature Edition) - Collapses",
  "The Rapa Nui Revision (Signature Edition) - Collapses",
  "The Lost City of Ubar (Signature Edition) - Lost Cities",
  "Doggerland: The Drowned Mesolithic (Signature Edition) - Deep History",
  "The Terracotta Army Workshops (Signature Edition) - Monuments",
  "The Vinland Map: Genuine or Forgery (Signature Edition) - Contested Sites",
  "The Theory Wars: Can Archaeology Unify (Signature Edition) - Methods"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unsolved Archaeology Study — "+safe+"\n"
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
    name:topic+' — unsolved problem record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A unsolved problem record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"unsolved-archaeology-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-unsolved-archaeology-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('unsolved-archaeology-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
