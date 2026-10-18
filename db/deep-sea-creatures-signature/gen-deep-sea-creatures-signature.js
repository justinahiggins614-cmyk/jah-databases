(function(){'use strict';
/* JAH Signature Deep-Sea Creatures Database generator — jahdb-deep-sea-creatures-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DEEPS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Signature Study: Humpback Anglerfish (Melanocetus johnsonii)", "Signature Study: Gulper Eel (Eurypharynx pelecanoides)", "Signature Study: Giant Isopod (Bathynomus giganteus)", "Signature Study: Black-eyed Squid (Gonatus onyx)", "Signature Study: Colossal Squid (Mesonychoteuthis hamiltoni)", "Signature Study: Bigfin Squid (Magnapinna pacifica)", "Signature Study: Dumbo Octopus (Grimpoteuthis bathynecta)", "Signature Study: Barreleye (Macropinna microstoma)", "Signature Study: Marine Hatchetfish (Argyropelecus hemigymnus)", "Signature Study: Viperfish (Chauliodus sloani)", "Signature Study: Fangtooth (Anoplogaster cornuta)"], "Compounded": ["Signature Study: Stoplight Loosejaw (Malacosteus niger)", "Signature Study: Glacier Lanternfish (Benthosema glaciale)", "Signature Study: Tripod Fish (Bathypterois grallator)", "Signature Study: Abyssal Cusk-eel (Abyssobrotula galatheae)", "Signature Study: Mariana Snailfish (Pseudoliparis swirei)", "Signature Study: Giant Grenadier (Coryphaenoides pectoralis)", "Signature Study: Black Swallower (Chiasmodon niger)", "Signature Study: Snipe Eel (Nemichthys scolopaceus)", "Signature Study: Yeti Crab (Kiwa hirsuta)", "Signature Study: Giant Tube Worm (Riftia pachyptila)", "Signature Study: Pompeii Worm (Alvinella pompejana)", "Signature Study: Flapjack Octopus (Opisthoteuthis californiana)"], "Advanced": ["Signature Study: Venus Flower Basket (Euplectella aspergillum)", "Signature Study: Giant Sea Spider (Colossendeis australis)", "Signature Study: Pacific Blackdragon (Idiacanthus antrostomus)", "Signature Study: Atolla Jellyfish (Atolla wyvillei)", "Signature Study: Giant Siphonophore (Praya dubia)", "Signature Study: Headless Chicken Monster (Enypniastes eximia)", "Signature Study: Basket Star (Gorgonocephalus eucnemis)", "Signature Study: Feather Star (Florometra serratissima)", "Signature Study: Supergiant Amphipod (Alicella gigantea)", "Signature Study: Rabbit Fish (Chimaera monstrosa)", "Signature Study: Coelacanth (Latimeria chalumnae)"]};
var DEMOKIND="species fact check";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Signature species demo\n# Topic: \""+safe+"\" | Field: "+field+"\n"
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
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature deep-sea creature species record of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"signature-generated",
    sample:true,
    disclaimer:"Generated Signature sample record \u2014 not an archive record. Seeded Signature records are the authoritative entries.",
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
var gen={version:"jahdb-deep-sea-creatures-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("deep-sea-creatures-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
