(function(){'use strict';
/* JAH The Houseplants Database generator — jahdb-houseplants-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HPL-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Houseplants 101: Why We Grow Indoors \u2014 Foundations",
  "Reading Light: Foot-Candles to Windows \u2014 Foundations",
  "Watering: The Soak-and-Dry Rule \u2014 Foundations",
  "Potting Mix and Drainage \u2014 Foundations",
  "Humidity and Temperature \u2014 Foundations",
  "Fertilizing Houseplants \u2014 Foundations",
  "The Pothos (Epipremnum aureum) \u2014 Foundations",
  "The Snake Plant (Sansevieria trifasciata) \u2014 Foundations",
  "The Spider Plant (Chlorophytum comosum) \u2014 Foundations",
  "The ZZ Plant (Zamioculcas zamiifolia) \u2014 Foundations",
  "The Peace Lily (Spathiphyllum) \u2014 Foundations"
 ],
 "Compounded": [
  "The Monstera (Monstera deliciosa) \u2014 Compounded",
  "The Fiddle-Leaf Fig (Ficus lyrata) \u2014 Compounded",
  "The Rubber Plant (Ficus elastica) \u2014 Compounded",
  "The Heartleaf Philodendron (Philodendron hederaceum) \u2014 Compounded",
  "The Boston Fern (Nephrolepis exaltata) \u2014 Compounded",
  "The African Violet (Saintpaulia) \u2014 Compounded",
  "The Aloe Vera (Aloe barbadensis) \u2014 Compounded",
  "The Jade Plant (Crassula ovata) \u2014 Compounded",
  "The Corn Plant Dracaena (Dracaena fragrans) \u2014 Compounded",
  "The Chinese Evergreen (Aglaonema) \u2014 Compounded",
  "The Prayer Plant (Maranta leuconeura) \u2014 Compounded",
  "The Bird of Paradise (Strelitzia nicolai) \u2014 Compounded"
 ],
 "Advanced": [
  "Propagating Houseplants \u2014 Advanced",
  "Repotting Without Shock \u2014 Advanced",
  "Houseplant Pests: Mealybugs to Fungus Gnats \u2014 Advanced",
  "Pruning and Training Houseplants \u2014 Advanced",
  "The Calathea (Goeppertia) \u2014 Advanced",
  "The Flamingo Flower (Anthurium andraeanum) \u2014 Advanced",
  "The Money Tree (Pachira aquatica) \u2014 Advanced",
  "The Norfolk Island Pine (Araucaria heterophylla) \u2014 Advanced",
  "Air Plants (Tillandsia) \u2014 Advanced",
  "Toxic Houseplants: Pets and Kids \u2014 Advanced",
  "The Indoor Jungle: Design and Grouping \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Houseplant Study — "+safe+"\n"
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
    name:topic+' — houseplant record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A houseplant record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"houseplant-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-houseplants-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('houseplants',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
