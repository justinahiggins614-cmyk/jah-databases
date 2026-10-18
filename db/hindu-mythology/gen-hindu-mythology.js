(function(){'use strict';
/* JAH The Hindu Mythology Database generator — jahdb-hindu-mythology-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HIMY-";
var FIELDS=["Devas & the Trimurti", "Epics & Avatars", "Cosmos & Philosophy"];
var TOPICS={
 "Devas & the Trimurti": [
  "Brahma — The Creator \u2014 Devas & the Trimurti",
  "Vishnu — The Preserver \u2014 Devas & the Trimurti",
  "Shiva — The Transformer \u2014 Devas & the Trimurti",
  "Lakshmi — Goddess of Fortune \u2014 Devas & the Trimurti",
  "Saraswati — Goddess of Learning \u2014 Devas & the Trimurti",
  "Ganesha — Remover of Obstacles \u2014 Devas & the Trimurti",
  "Durga — The Invincible \u2014 Devas & the Trimurti",
  "Kali — The Fierce Mother \u2014 Devas & the Trimurti",
  "Hanuman — The Devoted Servant \u2014 Devas & the Trimurti",
  "The Trimurti — Three in One \u2014 Devas & the Trimurti",
  "Parvati — The Mountain Goddess \u2014 Devas & the Trimurti",
  "The Devi Mahatmya — Glory of the Goddess \u2014 Devas & the Trimurti"
 ],
 "Epics & Avatars": [
  "Rama — The Ideal King \u2014 Epics & Avatars",
  "Sita — The Earth's Daughter \u2014 Epics & Avatars",
  "Krishna — The Divine Cowherd \u2014 Epics & Avatars",
  "The Ramayana — Rama's Journey \u2014 Epics & Avatars",
  "The Mahabharata — The Great War \u2014 Epics & Avatars",
  "Arjuna — The Peerless Archer \u2014 Epics & Avatars",
  "Draupadi — The Fire-Born Queen \u2014 Epics & Avatars",
  "Ravana — The Demon King \u2014 Epics & Avatars",
  "The Bhagavad Gita — The Song \u2014 Epics & Avatars",
  "The Avatars — Vishnu's Descents \u2014 Epics & Avatars",
  "Ayodhya — The Ideal City \u2014 Epics & Avatars",
  "Kurukshetra — The Field of Dharma \u2014 Epics & Avatars"
 ],
 "Cosmos & Philosophy": [
  "The Churning of the Ocean \u2014 Cosmos & Philosophy",
  "Yugas — The Four Ages \u2014 Cosmos & Philosophy",
  "Karma and Dharma — The Moral Cosmos \u2014 Cosmos & Philosophy",
  "Moksha — Liberation \u2014 Cosmos & Philosophy",
  "The Vedas — The Oldest Songs \u2014 Cosmos & Philosophy",
  "The Upanishads — The Forest Teachings \u2014 Cosmos & Philosophy",
  "The Puranas — The Old Tales \u2014 Cosmos & Philosophy",
  "Samsara — The Wheel \u2014 Cosmos & Philosophy",
  "Nachiketa — The Boy Who Questioned Death \u2014 Cosmos & Philosophy",
  "The Bhakti Saints — Love's Poets \u2014 Cosmos & Philosophy"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Hindu Mythology — "+safe+"\n"
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
var gen={version:'jahdb-hindu-mythology-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('hindu-mythology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
