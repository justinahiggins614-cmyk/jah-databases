(function(){'use strict';
/* JAH The Fabric Explorer generator — jahdb-db-fabric-explorer-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FBXES-";
var FIELDS=["Fabric Foundations", "The Fabric Library", "Fabric Mastery"];
var TOPICS={"Fabric Foundations": ["Natural Versus Synthetic", "The Touch Test", "Weave Basics", "Knit Versus Woven", "Fabric Weight", "Drape and Hand", "Reading Fabric Labels", "Fabric Care Symbols", "Shrinkage Science", "Pilling Causes and Cures", "Building a Swatch Library"], "The Fabric Library": ["Cotton: The Workhorse", "Linen: The Breezy Classic", "Wool: Nature's Performance Fiber", "Silk: The Luxury Standard", "Denim Deep Dive", "Leather and Suede", "Polyester: The Ubiquitous", "Nylon and Performance", "Velvet and Velour", "Lace and Embroidery", "Technical Fabrics", "Sustainable Textiles"], "Fabric Mastery": ["Sourcing Quality Fabric", "Fabric for Sewing Projects", "Textile Testing", "Fabric Storage", "Repairing Fabrics", "Teaching Textiles", "Curating a Fabric Stash", "Historical Textiles", "Future Fabrics", "The Master's Touch", "Fabric and Sustainability"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# minibot — "+safe+"\n"
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
    name:topic+' — fabric exploration record',
    title:topic,
    description:"SAMPLE RECORD (generated — structural Signature sample). A Signature-original fabric exploration record sample of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated Signature sample record — not an archive record. Seeded Signature records are the authoritative entries.',
    demo:{kind:"topic-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-db-fabric-explorer-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("db-fabric-explorer-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
