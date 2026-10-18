(function(){'use strict';
/* JAH Signature Mammals Database generator — jahdb-mammals-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MAMMS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Signature Study: African Elephant (Loxodonta africana)", "Signature Study: Blue Whale (Balaenoptera musculus)", "Signature Study: Lion (Panthera leo)", "Signature Study: Tiger (Panthera tigris)", "Signature Study: Brown Bear (Ursus arctos)", "Signature Study: Gray Wolf (Canis lupus)", "Signature Study: Red Fox (Vulpes vulpes)", "Signature Study: White-tailed Deer (Odocoileus virginianus)", "Signature Study: Eastern Gray Squirrel (Sciurus carolinensis)", "Signature Study: House Mouse (Mus musculus)", "Signature Study: Brown Rat (Rattus norvegicus)", "Signature Study: Virginia Opossum (Didelphis virginiana)"], "Compounded": ["Signature Study: Giraffe (Giraffa camelopardalis)", "Signature Study: Hippopotamus (Hippopotamus amphibius)", "Signature Study: Black Rhinoceros (Diceros bicornis)", "Signature Study: Giant Panda (Ailuropoda melanoleuca)", "Signature Study: Koala (Phascolarctos cinereus)", "Signature Study: Red Kangaroo (Osphranter rufus)", "Signature Study: Polar Bear (Ursus maritimus)", "Signature Study: Sea Otter (Enhydra lutris)", "Signature Study: Bottlenose Dolphin (Tursiops truncatus)", "Signature Study: Orca (Orcinus orca)", "Signature Study: Humpback Whale (Megaptera novaeangliae)"], "Advanced": ["Signature Study: Platypus (Ornithorhynchus anatinus)", "Signature Study: Short-beaked Echidna (Tachyglossus aculeatus)", "Signature Study: Little Brown Bat (Myotis lucifugus)", "Signature Study: Large Flying Fox (Pteropus vampyrus)", "Signature Study: Aardvark (Orycteropus afer)", "Signature Study: Sunda Pangolin (Manis javanica)", "Signature Study: Nine-banded Armadillo (Dasypus novemcinctus)", "Signature Study: Brown-throated Sloth (Bradypus variegatus)", "Signature Study: North American Porcupine (Erethizon dorsatum)", "Signature Study: European Hedgehog (Erinaceus europaeus)", "Signature Study: Eastern Mole (Scalopus aquaticus)"]};
var DEMOKIND="species fact check";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Signature species demo: fact display with real size/habitat data. Educational illustration.\n# Topic: \""+safe+"\" | Field: "+field+"\n"
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
    description:'SAMPLE RECORD (generated — structural sample). A Signature mammal study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:"signature-generated",
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
var gen={version:"jahdb-mammals-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('mammals-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
