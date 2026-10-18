(function(){'use strict';
/* JAH The Houseplants Signature Database generator — jahdb-houseplants-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HPLS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Houseplants 101: Why We Grow Indoors (Signature Edition) \u2014 Foundations",
  "Reading Light: Foot-Candles to Windows (Signature Edition) \u2014 Foundations",
  "Watering: The Soak-and-Dry Rule (Signature Edition) \u2014 Foundations",
  "Potting Mix and Drainage (Signature Edition) \u2014 Foundations",
  "Humidity and Temperature (Signature Edition) \u2014 Foundations",
  "Fertilizing Houseplants (Signature Edition) \u2014 Foundations",
  "The Pothos (Epipremnum aureum) (Signature Edition) \u2014 Foundations",
  "The Snake Plant (Sansevieria trifasciata) (Signature Edition) \u2014 Foundations",
  "The Spider Plant (Chlorophytum comosum) (Signature Edition) \u2014 Foundations",
  "The ZZ Plant (Zamioculcas zamiifolia) (Signature Edition) \u2014 Foundations",
  "The Peace Lily (Spathiphyllum) (Signature Edition) \u2014 Foundations"
 ],
 "Compounded": [
  "The Monstera (Monstera deliciosa) (Signature Edition) \u2014 Compounded",
  "The Fiddle-Leaf Fig (Ficus lyrata) (Signature Edition) \u2014 Compounded",
  "The Rubber Plant (Ficus elastica) (Signature Edition) \u2014 Compounded",
  "The Heartleaf Philodendron (Philodendron hederaceum) (Signature Edition) \u2014 Compounded",
  "The Boston Fern (Nephrolepis exaltata) (Signature Edition) \u2014 Compounded",
  "The African Violet (Saintpaulia) (Signature Edition) \u2014 Compounded",
  "The Aloe Vera (Aloe barbadensis) (Signature Edition) \u2014 Compounded",
  "The Jade Plant (Crassula ovata) (Signature Edition) \u2014 Compounded",
  "The Corn Plant Dracaena (Dracaena fragrans) (Signature Edition) \u2014 Compounded",
  "The Chinese Evergreen (Aglaonema) (Signature Edition) \u2014 Compounded",
  "The Prayer Plant (Maranta leuconeura) (Signature Edition) \u2014 Compounded",
  "The Bird of Paradise (Strelitzia nicolai) (Signature Edition) \u2014 Compounded"
 ],
 "Advanced": [
  "Propagating Houseplants (Signature Edition) \u2014 Advanced",
  "Repotting Without Shock (Signature Edition) \u2014 Advanced",
  "Houseplant Pests: Mealybugs to Fungus Gnats (Signature Edition) \u2014 Advanced",
  "Pruning and Training Houseplants (Signature Edition) \u2014 Advanced",
  "The Calathea (Goeppertia) (Signature Edition) \u2014 Advanced",
  "The Flamingo Flower (Anthurium andraeanum) (Signature Edition) \u2014 Advanced",
  "The Money Tree (Pachira aquatica) (Signature Edition) \u2014 Advanced",
  "The Norfolk Island Pine (Araucaria heterophylla) (Signature Edition) \u2014 Advanced",
  "Air Plants (Tillandsia) (Signature Edition) \u2014 Advanced",
  "Toxic Houseplants: Pets and Kids (Signature Edition) \u2014 Advanced",
  "The Indoor Jungle: Design and Grouping (Signature Edition) \u2014 Advanced"
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
var gen={version:'jahdb-houseplants-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('houseplants-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
