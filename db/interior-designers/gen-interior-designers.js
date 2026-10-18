(function(){'use strict';
/* JAH The Interior Designers Database generator — jahdb-interior-designers-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-INTDES-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Interior Designers Do",
  "The Elements of Design",
  "Principles: Balance, Rhythm, Harmony",
  "Space Planning Basics",
  "Color Theory for Interiors",
  "Lighting Design Fundamentals",
  "Materials and Finishes",
  "Furniture: Selection and Layout",
  "The Client Process",
  "Design Styles Through History",
  "Measuring and Drawing"
 ],
 "Compounded": [
  "Kitchens: The Hardest Room",
  "Bathrooms: Small Spaces, Big Demands",
  "Commercial Design: Offices and Retail",
  "Hospitality Design",
  "Sustainable and Healthy Design",
  "Textiles: Fabric, Rugs, and Upholstery",
  "Window Treatments",
  "Art and Accessories Styling",
  "Design Fees and Contracts",
  "Working with Contractors",
  "3D Visualization and Rendering",
  "Aging-in-Place and Universal Design"
 ],
 "Advanced": [
  "The Psychology of Space",
  "Historic Preservation Interiors",
  "Parametric and Computational Design",
  "Designing for Neurodiversity",
  "The Business of Design: Scaling Up",
  "Famous Interior Designers",
  "Future Spaces: What's Next",
  "Color Psychology in Depth",
  "Acoustics for Interiors",
  "Exhibition and Museum Interiors",
  "Biophilic Design Mastery"
 ]
};
var DEMOKIND="space planning";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Interior space planner — "+safe+"\n"
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
    name:topic+' — interior designers profession record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A interior designers profession record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-interior-designers-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('interior-designers',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
