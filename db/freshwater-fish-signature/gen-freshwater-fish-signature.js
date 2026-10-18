(function(){'use strict';
/* JAH Signature Freshwater Fish Database generator — jahdb-freshwater-fish-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FRWFS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Signature Study: Largemouth Bass (Micropterus salmoides)", "Signature Study: Smallmouth Bass (Micropterus dolomieu)", "Signature Study: Rainbow Trout (Oncorhynchus mykiss)", "Signature Study: Brown Trout (Salmo trutta)", "Signature Study: Brook Trout (Salvelinus fontinalis)", "Signature Study: Lake Trout (Salvelinus namaycush)", "Signature Study: Arctic Char (Salvelinus alpinus)", "Signature Study: Atlantic Salmon (Salmo salar)", "Signature Study: Chinook Salmon (Oncorhynchus tshawytscha)", "Signature Study: Northern Pike (Esox lucius)", "Signature Study: Muskellunge (Esox masquinongy)"], "Compounded": ["Signature Study: Walleye (Sander vitreus)", "Signature Study: Channel Catfish (Ictalurus punctatus)", "Signature Study: Blue Catfish (Ictalurus furcatus)", "Signature Study: Flathead Catfish (Pylodictis olivaris)", "Signature Study: Common Carp (Cyprinus carpio)", "Signature Study: Grass Carp (Ctenopharyngodon idella)", "Signature Study: Goldfish (Carassius auratus)", "Signature Study: Crucian Carp (Carassius carassius)", "Signature Study: European Perch (Perca fluviatilis)", "Signature Study: Yellow Perch (Perca flavescens)", "Signature Study: Bluegill (Lepomis macrochirus)", "Signature Study: Black Crappie (Pomoxis nigromaculatus)"], "Advanced": ["Signature Study: White Crappie (Pomoxis annularis)", "Signature Study: Red-bellied Piranha (Pygocentrus nattereri)", "Signature Study: Electric Eel (Electrophorus electricus)", "Signature Study: Arapaima (Arapaima gigas)", "Signature Study: Alligator Gar (Atractosteus spatula)", "Signature Study: Bowfin (Amia calva)", "Signature Study: Beluga Sturgeon (Huso huso)", "Signature Study: White Sturgeon (Acipenser transmontanus)", "Signature Study: American Paddlefish (Polyodon spathula)", "Signature Study: Siamese Fighting Fish (Betta splendens)", "Signature Study: Neon Tetra (Paracheirodon innesi)"]};
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
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature freshwater fish species record of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-freshwater-fish-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("freshwater-fish-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
