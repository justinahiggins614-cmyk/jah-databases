(function(){'use strict';
/* JAH The Egyptian Mythology Database generator — jahdb-egyptian-mythology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EGMY-";
var FIELDS=["Gods of the Nile", "Pharaohs & the Afterlife", "Creation & Cosmos"];
var TOPICS={
 "Gods of the Nile": [
  "Ra — The Sun God \u2014 Gods of the Nile",
  "Isis — The Great Magician \u2014 Gods of the Nile",
  "Osiris — The Risen King \u2014 Gods of the Nile",
  "Horus — The Falcon King \u2014 Gods of the Nile",
  "Set — God of Chaos \u2014 Gods of the Nile",
  "Thoth — God of Wisdom \u2014 Gods of the Nile",
  "Anubis — Guardian of the Dead \u2014 Gods of the Nile",
  "Bastet — The Cat Goddess \u2014 Gods of the Nile",
  "Sekhmet — The Lioness of War \u2014 Gods of the Nile",
  "Ptah — The Craftsman Creator \u2014 Gods of the Nile",
  "Sobek — The Crocodile God \u2014 Gods of the Nile",
  "Hathor — Goddess of Joy \u2014 Gods of the Nile",
  "The Contendings of Horus and Set \u2014 Gods of the Nile",
  "The Destruction of Mankind \u2014 Gods of the Nile",
  "Nephthys — The Mourning Sister \u2014 Gods of the Nile"
 ],
 "Pharaohs & the Afterlife": [
  "The Weighing of the Heart \u2014 Pharaohs & the Afterlife",
  "The Book of the Dead \u2014 Pharaohs & the Afterlife",
  "The Pyramid Texts \u2014 Pharaohs & the Afterlife",
  "Mummification — The Making Eternal \u2014 Pharaohs & the Afterlife",
  "The Pharaoh — Living God \u2014 Pharaohs & the Afterlife",
  "Tutankhamun — The Boy King \u2014 Pharaohs & the Afterlife",
  "Cleopatra — The Last Pharaoh \u2014 Pharaohs & the Afterlife",
  "Imhotep — The First Genius \u2014 Pharaohs & the Afterlife",
  "The Sphinx — Guardian of Giza \u2014 Pharaohs & the Afterlife",
  "The Field of Reeds \u2014 Pharaohs & the Afterlife",
  "Ammit — Devourer of the Dead \u2014 Pharaohs & the Afterlife"
 ],
 "Creation & Cosmos": [
  "Maat — Truth and Order \u2014 Creation & Cosmos",
  "The Heliopolitan Creation \u2014 Creation & Cosmos",
  "The Memphite Creation \u2014 Creation & Cosmos",
  "Nun — The Primeval Waters \u2014 Creation & Cosmos",
  "The Solar Barque — Journey of the Night \u2014 Creation & Cosmos",
  "Apophis — Serpent of Chaos \u2014 Creation & Cosmos",
  "The Ogdoad — The Eight of Hermopolis \u2014 Creation & Cosmos",
  "Khepri — The Dawn Scarab \u2014 Creation & Cosmos"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Egyptian Mythology — "+safe+"\n"
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
    name:topic+' — mythology record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A mythology record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-egyptian-mythology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('egyptian-mythology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
