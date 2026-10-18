(function(){'use strict';
/* JAH The Conifers Signature Database generator — jahdb-conifers-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CNFS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Conifers 101 (Signature Edition) \u2014 Foundations",
  "How Conifers Reproduce: The Cone (Signature Edition) \u2014 Foundations",
  "Pine (Pinus) (Signature Edition) \u2014 Foundations",
  "Spruce (Picea) (Signature Edition) \u2014 Foundations",
  "Fir (Abies) (Signature Edition) \u2014 Foundations",
  "Cedar: True Cedars and Impostors (Signature Edition) \u2014 Foundations",
  "Coast Redwood (Sequoia sempervirens) (Signature Edition) \u2014 Foundations",
  "Giant Sequoia (Sequoiadendron giganteum) (Signature Edition) \u2014 Foundations",
  "Juniper (Juniperus) (Signature Edition) \u2014 Foundations",
  "Yew (Taxus): The Toxic Conifer (Signature Edition) \u2014 Foundations",
  "Larch (Larix): The Deciduous Conifer (Signature Edition) \u2014 Foundations"
 ],
 "Compounded": [
  "Douglas-Fir (Pseudotsuga menziesii) (Signature Edition) \u2014 Compounded",
  "Hemlock (Tsuga) (Signature Edition) \u2014 Compounded",
  "Cypress (Cupressus) (Signature Edition) \u2014 Compounded",
  "Bald Cypress (Taxodium distichum) (Signature Edition) \u2014 Compounded",
  "Dawn Redwood (Metasequoia glyptostroboides) (Signature Edition) \u2014 Compounded",
  "Monkey Puzzle (Araucaria araucana) (Signature Edition) \u2014 Compounded",
  "Norfolk Island Pine (Araucaria heterophylla) (Signature Edition) \u2014 Compounded",
  "Bristlecone Pine (Pinus longaeva) (Signature Edition) \u2014 Compounded",
  "Conifer Leaves: Needles, Scales, and Awls (Signature Edition) \u2014 Compounded",
  "Conifer Wood (Signature Edition) \u2014 Compounded",
  "Christmas Trees (Signature Edition) \u2014 Compounded",
  "Conifer Resin and Pitch (Signature Edition) \u2014 Compounded"
 ],
 "Advanced": [
  "Identifying Conifers by Cone (Signature Edition) \u2014 Advanced",
  "Identifying Conifers by Needle (Signature Edition) \u2014 Advanced",
  "Landscaping Conifers (Signature Edition) \u2014 Advanced",
  "Bonsai Conifers (Signature Edition) \u2014 Advanced",
  "Conifer Diseases and Pests (Signature Edition) \u2014 Advanced",
  "Fire Ecology of Conifers (Signature Edition) \u2014 Advanced",
  "Conifers and Climate (Signature Edition) \u2014 Advanced",
  "The Tallest: How Trees Reach the Sky (Signature Edition) \u2014 Advanced",
  "Growing Conifers from Seed (Signature Edition) \u2014 Advanced",
  "Conifer Essential Oils (Signature Edition) \u2014 Advanced",
  "The Conifer Collection: A Capstone (Signature Edition) \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Conifer Study — "+safe+"\n"
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
    name:topic+' — conifer record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A conifer record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"conifer-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-conifers-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('conifers-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
