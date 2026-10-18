(function(){'use strict';
/* JAH The Orchids Signature Database generator — jahdb-orchids-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ORQS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Orchids 101: The World's Largest Plant Family (Signature Edition) \u2014 Foundations",
  "Orchid Anatomy: Pseudobulbs, Velamen, and Lips (Signature Edition) \u2014 Foundations",
  "Light and Water for Orchids (Signature Edition) \u2014 Foundations",
  "Orchid Potting Media: Bark and Moss (Signature Edition) \u2014 Foundations",
  "The Moth Orchid (Phalaenopsis) (Signature Edition) \u2014 Foundations",
  "The Cattleya: Queen of Orchids (Signature Edition) \u2014 Foundations",
  "The Dendrobium (Signature Edition) \u2014 Foundations",
  "The Lady's Slipper (Paphiopedilum) (Signature Edition) \u2014 Foundations",
  "The Cymbidium (Signature Edition) \u2014 Foundations",
  "The Oncidium: Dancing Ladies (Signature Edition) \u2014 Foundations",
  "Repotting Orchids (Signature Edition) \u2014 Foundations"
 ],
 "Compounded": [
  "The Vanda (Signature Edition) \u2014 Compounded",
  "The Pansy Orchid (Miltoniopsis) (Signature Edition) \u2014 Compounded",
  "The Zygopetalum (Signature Edition) \u2014 Compounded",
  "The Epidendrum: Reed-Stem Orchids (Signature Edition) \u2014 Compounded",
  "The Spider Orchid (Brassia) (Signature Edition) \u2014 Compounded",
  "The Vanilla Orchid (Vanilla planifolia) (Signature Edition) \u2014 Compounded",
  "The Ghost Orchid (Dendrophylax lindenii) (Signature Edition) \u2014 Compounded",
  "The Bee Orchid (Ophrys apifera) (Signature Edition) \u2014 Compounded",
  "Orchid Pollination Tricks (Signature Edition) \u2014 Compounded",
  "Fertilizing Orchids: Weakly Weekly (Signature Edition) \u2014 Compounded",
  "Keikis: Baby Orchids (Signature Edition) \u2014 Compounded",
  "Orchid Pests and Diseases (Signature Edition) \u2014 Compounded"
 ],
 "Advanced": [
  "Hardy Lady's Slippers (Cypripedium) (Signature Edition) \u2014 Advanced",
  "Jewel Orchids (Ludisia discolor) (Signature Edition) \u2014 Advanced",
  "Miniature Orchids (Signature Edition) \u2014 Advanced",
  "Orchid Conservation and CITES (Signature Edition) \u2014 Advanced",
  "Hybridizing Orchids (Signature Edition) \u2014 Advanced",
  "Mounting Orchids on Bark and Cork (Signature Edition) \u2014 Advanced",
  "Terrarium and Wardian Orchids (Signature Edition) \u2014 Advanced",
  "Judging Orchids: The AOS Awards System (Signature Edition) \u2014 Advanced",
  "Summer Outdoors: The Vacation Method (Signature Edition) \u2014 Advanced",
  "The Corsage Era: Orchids in Culture (Signature Edition) \u2014 Advanced",
  "The Lifelong Orchid Collection (Signature Edition) \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Orchid Study — "+safe+"\n"
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
    name:topic+' — orchid record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A orchid record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"orchid-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-orchids-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('orchids-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
