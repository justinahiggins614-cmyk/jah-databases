(function(){'use strict';
/* JAH The Darkroom Developing Image-Making Database generator — jahdb-image-making-darkroom-developing-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-IMDD-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["What Happens in the Darkroom", "Darkroom Safety: Chemicals and Ventilation", "The Enlarger: Your Darkroom Camera", "Developers: What They Do", "Stop Bath and Fixer", "Loading Film onto Reels Blind", "Developing Your First Black-and-White Roll", "Reading a Negative", "Making Your First Contact Sheet", "Paper: RC vs Fiber, Grades and Surfaces", "Your First Enlarged Print"], "Compounded": ["Test Strips: Nailing Exposure", "Contrast Control with Multigrade Filters", "Dodging and Burning", "Push Processing in the Darkroom", "Toning Prints: Selenium and Sepia", "Washing and Archival Processing", "Spotting and Retouching Prints", "Cropping and the Easel", "Split-Filter Printing", "Pre-Flashing Paper", "Lith Printing", "Sabattier Effect (Solarization)"], "Advanced": ["Fiber-Base Fine Printing", "Editioning Darkroom Prints", "Mounting and Matting for Exhibition", "The Archival Wash: Museum Standards", "Troubleshooting: Fog, Stains, Spots", "Building a Home Darkroom", "Ventilation and Plumbing for Darkrooms", "Teaching Darkroom Practice", "The Darkroom Printer's Business", "Alternative Processes Overview", "From Darkroom to Digital Archive"]};
var DEMOKIND="darkroom chemistry planning";
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
    name:topic+' — darkroom developing image-making record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A darkroom developing image-making record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
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
var gen={version:'jahdb-image-making-darkroom-developing-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('image-making-darkroom-developing-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
