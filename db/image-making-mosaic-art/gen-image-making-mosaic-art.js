(function(){'use strict';
/* JAH The Mosaic Art Image-Making Database generator — jahdb-image-making-mosaic-art-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-IMMA-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["What Mosaic Art Is", "Tesserae: Stone, Glass, Smalti", "Cutting Tesserae: Hammer, Hardy, Nippers", "Andamento: The Flow of Rows", "Designing for Mosaic: Cartoons", "Direct Method on Mesh and Board", "Indirect Method: Paper Face Down", "Grout: The Lines Between", "Gold Smalti and Byzantine Light", "Portraits in Mosaic", "Mosaic Murals for Public Space"], "Compounded": ["Pebble and Found-Object Mosaic", "Mosaic on Sculptural Forms", "Color Theory for Tesserae", "Restoring Ancient Mosaics", "Modern Abstract Mosaic", "Mosaic Jewelry and Small Forms", "Installing Mosaic: Mortar Beds", "Sealing Outdoor Mosaic", "Teaching Mosaic", "The Mosaic Business", "Digital Design Tools for Mosaic", "Lighting Mosaic for Display"], "Advanced": ["Mosaic History: Rome to Ravenna", "Troubleshooting Mosaic Failures", "Smalti Portraits: Byzantine Technique", "Mosaic Vaults and Domes", "Terrazzo: Mosaic's Cousin", "Glass Fusing for Mosaic Tesserae", "Mosaic Conservation Science", "Large Public Commissions: Bidding", "Mosaic in Landscape Architecture", "Teaching Master-Level Mosaic", "The Mosaic Artist's Legacy: Documentation"]};
var DEMOKIND="mosaic material planning";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# "+DEMOKIND+" — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — mosaic art image-making record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A mosaic art image-making record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
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
var gen={version:'jahdb-image-making-mosaic-art-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('image-making-mosaic-art',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
