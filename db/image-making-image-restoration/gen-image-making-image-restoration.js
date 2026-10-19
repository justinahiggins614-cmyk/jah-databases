(function(){'use strict';
/* JAH The Image Restoration Image-Making Database generator — jahdb-image-making-image-restoration-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-IMRS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["What Image Restoration Is", "Assessing Damage First", "Dust, Scratches, and Spots", "Denoising Old Scans", "Deblurring: Focus and Motion", "Fading and Color Correction", "Torn and Missing Pieces", "Face Restoration (GFPGAN/CodeFormer)", "Stains, Mold, and Water Damage", "Digitizing Before Restoring", "Historical Photo Restoration"], "Compounded": ["The Restoration Business", "Teaching Restoration", "Crease Removal Techniques", "Tape Stain Treatment", "Silver Mirroring on Old Prints", "Vinegar Syndrome: Film Base Decay", "Color Cast Removal Masterclass", "Rebuilding Missing Corners", "Album Page Restoration", "Slide Film Restoration", "Negative Scratch Repair (Digital ICE)", "Print Surface Texture Matching"], "Advanced": ["Museum Conservation Standards", "Working with Archivists", "Disaster Recovery for Collections", "Mass Digitization Projects", "Grant Writing for Preservation", "The Restoration Studio Business", "Expert Witness: Photo Authentication", "Dating Photographs Forensically", "Teaching Conservation Ethics", "AI's Limits in Restoration", "The Master Restorer's Legacy"]};
var DEMOKIND="restoration planning";
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
    name:topic+' — image restoration image-making record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A image restoration image-making record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-image-making-image-restoration-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('image-making-image-restoration',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
