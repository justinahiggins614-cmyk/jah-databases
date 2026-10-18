(function(){'use strict';
/* JAH The Mammals Database generator — jahdb-mammals-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MAMM-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["African Elephant (Loxodonta africana)", "Blue Whale (Balaenoptera musculus)", "Lion (Panthera leo)", "Tiger (Panthera tigris)", "Brown Bear (Ursus arctos)", "Gray Wolf (Canis lupus)", "Red Fox (Vulpes vulpes)", "White-tailed Deer (Odocoileus virginianus)", "Eastern Gray Squirrel (Sciurus carolinensis)", "House Mouse (Mus musculus)", "Brown Rat (Rattus norvegicus)", "Virginia Opossum (Didelphis virginiana)"], "Compounded": ["Giraffe (Giraffa camelopardalis)", "Hippopotamus (Hippopotamus amphibius)", "Black Rhinoceros (Diceros bicornis)", "Giant Panda (Ailuropoda melanoleuca)", "Koala (Phascolarctos cinereus)", "Red Kangaroo (Osphranter rufus)", "Polar Bear (Ursus maritimus)", "Sea Otter (Enhydra lutris)", "Bottlenose Dolphin (Tursiops truncatus)", "Orca (Orcinus orca)", "Humpback Whale (Megaptera novaeangliae)"], "Advanced": ["Platypus (Ornithorhynchus anatinus)", "Short-beaked Echidna (Tachyglossus aculeatus)", "Little Brown Bat (Myotis lucifugus)", "Large Flying Fox (Pteropus vampyrus)", "Aardvark (Orycteropus afer)", "Sunda Pangolin (Manis javanica)", "Nine-banded Armadillo (Dasypus novemcinctus)", "Brown-throated Sloth (Bradypus variegatus)", "North American Porcupine (Erethizon dorsatum)", "European Hedgehog (Erinaceus europaeus)", "Eastern Mole (Scalopus aquaticus)"]};
var DEMOKIND="species fact check";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Species demo: fact display with real size/habitat data. Educational illustration.\n# Topic: \""+safe+"\" | Field: "+field+"\n"
   + "record = {'topic': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "print('Sample record — structural sample, not an archive entry.')\n"
   + "print(record['topic'] + ' [' + record['field'] + ']')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic,
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A mammal species record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:"public-harvest",
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-mammals-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('mammals',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
