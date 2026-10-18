(function(){'use strict';
/* JAH The World Culture Explorer generator — jahdb-db-world-culture-explorer-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WCE-";
var FIELDS=["Greetings & Customs","Food & Festivals","Arts & Daily Life"];
var TOPICS={
 "Greetings & Customs": [
  "Greetings Around the World - Greetings & Customs",
  "Gift-Giving Customs - Greetings & Customs",
  "Dining Etiquette Basics - Greetings & Customs",
  "Shoes: On or Off? - Greetings & Customs",
  "Personal Space and Touch - Greetings & Customs",
  "Time: Strict or Flowing? - Greetings & Customs",
  "Names and Titles - Greetings & Customs",
  "Photography Etiquette - Greetings & Customs",
  "Bargaining Cultures - Greetings & Customs",
  "Sacred Spaces: Visiting Respectfully - Greetings & Customs",
  "Festivals of Light - Greetings & Customs",
  "Tipping Around the World - Greetings & Customs"
 ],
 "Food & Festivals": [
  "Street Food Cultures - Food & Festivals",
  "Tea Cultures - Food & Festivals",
  "Bread: The Universal Food - Food & Festivals",
  "Harvest Festivals - Food & Festivals",
  "Carnival and Mardi Gras - Food & Festivals",
  "New Year Celebrations - Food & Festivals",
  "Wedding Traditions - Food & Festivals",
  "Music and Dance Traditions - Food & Festivals",
  "Textile Arts - Food & Festivals",
  "Calligraphy and Writing Arts - Food & Festivals",
  "Masks and Performance - Food & Festivals"
 ],
 "Arts & Daily Life": [
  "Pottery Traditions - Arts & Daily Life",
  "Architecture as Culture - Arts & Daily Life",
  "Markets: The Heart of Cities - Arts & Daily Life",
  "Sports That Define Nations - Arts & Daily Life",
  "Storytelling Traditions - Arts & Daily Life",
  "Rites of Passage - Arts & Daily Life",
  "Elders and Ancestors - Arts & Daily Life",
  "Craftsmanship and Apprenticeship - Arts & Daily Life",
  "Gardens as Philosophy - Arts & Daily Life",
  "Water Cultures - Arts & Daily Life",
  "Your Culture, Seen Fresh - Arts & Daily Life"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Culture Explorer Study — "+safe+"\n"
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
    name:topic+' — culture lesson record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A culture lesson record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"culture-explorer-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-world-culture-explorer-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-world-culture-explorer',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
