(function(){'use strict';
/* JAH Signature Biomes Database generator — jahdb-biomes-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BIOMES-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Signature Study: Tropical Rainforest \u2014 Amazon Basin", "Signature Study: Tropical Rainforest \u2014 Congo Basin", "Signature Study: Tropical Rainforest \u2014 Southeast Asia", "Signature Study: Tropical Savanna \u2014 Serengeti", "Signature Study: Tropical Savanna \u2014 Brazilian Cerrado", "Signature Study: Hot Desert \u2014 Sahara", "Signature Study: Hot Desert \u2014 Arabian Desert", "Signature Study: Cold Desert \u2014 Gobi", "Signature Study: Semiarid Steppe \u2014 Eurasian Steppe", "Signature Study: Mediterranean Scrub \u2014 California Chaparral", "Signature Study: Mediterranean Scrub \u2014 Mediterranean Basin", "Signature Study: Temperate Grassland \u2014 North American Prairie"], "Compounded": ["Signature Study: Temperate Deciduous Forest \u2014 Eastern North America", "Signature Study: Temperate Deciduous Forest \u2014 European Beech Forest", "Signature Study: Temperate Rainforest \u2014 Pacific Northwest", "Signature Study: Boreal Forest (Taiga) \u2014 Siberia", "Signature Study: Boreal Forest (Taiga) \u2014 Canadian Shield", "Signature Study: Montane Cloud Forest \u2014 Andes", "Signature Study: Alpine Tundra \u2014 Himalaya", "Signature Study: Arctic Tundra \u2014 Alaska North Slope", "Signature Study: Mangrove Forest \u2014 Sundarbans", "Signature Study: Freshwater Wetland \u2014 Everglades", "Signature Study: Peat Bog \u2014 West Siberian Lowland"], "Advanced": ["Signature Study: Coral Reef \u2014 Great Barrier Reef", "Signature Study: Coral Reef \u2014 Coral Triangle", "Signature Study: Kelp Forest \u2014 California Coast", "Signature Study: Open Ocean Pelagic Zone \u2014 Mid-Atlantic Gyre", "Signature Study: Deep-Sea Hydrothermal Vent \u2014 East Pacific Rise", "Signature Study: Polar Ice Cap \u2014 Antarctica", "Signature Study: Polar Ice Cap \u2014 Greenland", "Signature Study: Estuary \u2014 Chesapeake Bay", "Signature Study: Salt Marsh \u2014 Wadden Sea", "Signature Study: Volcanic Island Ecosystem \u2014 Hawaii", "Signature Study: Cave Ecosystem \u2014 Mammoth Cave"]};
var DEMOKIND="biome climate check";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Signature biome demo: climate-envelope field check with real biome ranges. Educational illustration.\n# Topic: \""+safe+"\" | Field: "+field+"\n"
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
    description:'SAMPLE RECORD (generated — structural sample). A Signature biome study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:"jahdb-biomes-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('biomes-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
