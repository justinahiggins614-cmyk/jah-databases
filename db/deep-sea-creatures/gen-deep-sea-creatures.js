(function(){'use strict';
/* JAH The Deep-Sea Creatures Database generator — jahdb-deep-sea-creatures-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DEEP-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Humpback Anglerfish (Melanocetus johnsonii)", "Gulper Eel (Eurypharynx pelecanoides)", "Giant Isopod (Bathynomus giganteus)", "Black-eyed Squid (Gonatus onyx)", "Colossal Squid (Mesonychoteuthis hamiltoni)", "Bigfin Squid (Magnapinna pacifica)", "Dumbo Octopus (Grimpoteuthis bathynecta)", "Barreleye (Macropinna microstoma)", "Marine Hatchetfish (Argyropelecus hemigymnus)", "Viperfish (Chauliodus sloani)", "Fangtooth (Anoplogaster cornuta)"], "Compounded": ["Stoplight Loosejaw (Malacosteus niger)", "Glacier Lanternfish (Benthosema glaciale)", "Tripod Fish (Bathypterois grallator)", "Abyssal Cusk-eel (Abyssobrotula galatheae)", "Mariana Snailfish (Pseudoliparis swirei)", "Giant Grenadier (Coryphaenoides pectoralis)", "Black Swallower (Chiasmodon niger)", "Snipe Eel (Nemichthys scolopaceus)", "Yeti Crab (Kiwa hirsuta)", "Giant Tube Worm (Riftia pachyptila)", "Pompeii Worm (Alvinella pompejana)", "Flapjack Octopus (Opisthoteuthis californiana)"], "Advanced": ["Venus Flower Basket (Euplectella aspergillum)", "Giant Sea Spider (Colossendeis australis)", "Pacific Blackdragon (Idiacanthus antrostomus)", "Atolla Jellyfish (Atolla wyvillei)", "Giant Siphonophore (Praya dubia)", "Headless Chicken Monster (Enypniastes eximia)", "Basket Star (Gorgonocephalus eucnemis)", "Feather Star (Florometra serratissima)", "Supergiant Amphipod (Alicella gigantea)", "Rabbit Fish (Chimaera monstrosa)", "Coelacanth (Latimeria chalumnae)"]};
var DEMOKIND="species fact check";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Species demo\n# Topic: \""+safe+"\" | Field: "+field+"\n"
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
    description:"SAMPLE RECORD (generated \u2014 structural sample). A deep-sea creature species record of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"public-harvest",
    sample:true,
    disclaimer:"Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.",
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
var gen={version:"jahdb-deep-sea-creatures-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("deep-sea-creatures",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
