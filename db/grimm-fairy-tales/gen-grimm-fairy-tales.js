(function(){'use strict';
/* JAH The Grimm Fairy Tales Database generator — jahdb-grimm-fairy-tales-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GRFT-";
var FIELDS=["Tales of Enchantment", "Tales of Trial", "Tales of Wonder"];
var TOPICS={
 "Tales of Enchantment": [
  "Cinderella — Aschenputtel \u2014 Tales of Enchantment",
  "Snow White — Schneewittchen \u2014 Tales of Enchantment",
  "Rapunzel \u2014 Tales of Enchantment",
  "The Frog Prince — Der Froschkönig \u2014 Tales of Enchantment",
  "Sleeping Beauty — Dornröschen \u2014 Tales of Enchantment",
  "The Six Swans \u2014 Tales of Enchantment",
  "The Seven Ravens \u2014 Tales of Enchantment",
  "Briar-Rose's Kin — The Variants \u2014 Tales of Enchantment",
  "Snow White and Rose Red \u2014 Tales of Enchantment"
 ],
 "Tales of Trial": [
  "Hansel and Gretel — Hänsel und Gretel \u2014 Tales of Trial",
  "Rumpelstiltskin \u2014 Tales of Trial",
  "Little Red Cap — Rotkäppchen \u2014 Tales of Trial",
  "The Fisherman and His Wife \u2014 Tales of Trial",
  "The Juniper Tree — Von dem Machandelboom \u2014 Tales of Trial",
  "The Wolf and the Seven Young Goats \u2014 Tales of Trial",
  "The Three Spinners \u2014 Tales of Trial",
  "The Devil's Three Golden Hairs \u2014 Tales of Trial",
  "Faithful John — Der treue Johannes \u2014 Tales of Trial",
  "The Goose Girl \u2014 Tales of Trial"
 ],
 "Tales of Wonder": [
  "The Bremen Town Musicians \u2014 Tales of Wonder",
  "The Twelve Dancing Princesses \u2014 Tales of Wonder",
  "The Golden Goose \u2014 Tales of Wonder",
  "The Elves and the Shoemaker \u2014 Tales of Wonder",
  "The Star Money — Sterntaler \u2014 Tales of Wonder",
  "Thumbling — Daumesdick \u2014 Tales of Wonder",
  "The Two Brothers \u2014 Tales of Wonder",
  "The Water of Life — Das Wasser des Lebens \u2014 Tales of Wonder",
  "The White Snake \u2014 Tales of Wonder",
  "The Knapsack, the Hat, and the Horn \u2014 Tales of Wonder",
  "The Grimm Method — Collecting \u2014 Tales of Wonder",
  "The Tales' Afterlife — Influence \u2014 Tales of Wonder",
  "Why the Grimms Matter \u2014 Tales of Wonder",
  "The Golden Bird \u2014 Tales of Wonder",
  "Iron John — Eisenhans \u2014 Tales of Wonder"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Grimm Fairy Tales — "+safe+"\n"
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
    name:topic+' — fairy tale record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A fairy tale record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-grimm-fairy-tales-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('grimm-fairy-tales',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
