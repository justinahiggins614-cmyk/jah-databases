(function(){'use strict';
/* JAH The Signature Microfluidic Lab-on-a-Chip Diagnostic Kits Database generator — jahdb-tech-130-microfluidic-lab-on-a-chip-diagnostic-kits-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET130S-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The Signature Approach to Microfluidic Lab-on-a-Chip Diagnostic Kits (Signature)","Signature Research and Development Program (Signature)","Signature Design Specifications (Signature)","Signature Development Roadmap (Signature)","Signature Design Challenges (Signature)"],"Compounded": ["Signature Microfluidic Cartridge (Signature)","Signature CRISPR Detection (Signature)","Signature Phone Reader (Signature)","Signature Multiplex Panel (Signature)","Signature Sample Prep Module (Signature)","Signature Home Test Kit (Signature)","Signature Cancer Screening Chip (Signature)"],"Advanced": ["Signature Antimicrobial Stewardship (Signature)","Signature Global Health Kit (Signature)","Signature Regulatory Path (Signature)","Signature Data Integration (Signature)","Signature Manufacturing Scale (Signature)","Signature Veterinary Use (Signature)","Signature Pandemic Preparedness (Signature)","Signature Education Kit (Signature)"]};
var DEMOKIND="signature microfluidic lab-on-a-chip diagnostic kit record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# signature microfluidic lab-on-a-chip diagnostic kit record planner — "+safe+"\n"
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
    name:topic+' — signature microfluidic lab-on-a-chip diagnostic kit record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A signature microfluidic lab-on-a-chip diagnostic kit record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-130-microfluidic-lab-on-a-chip-diagnostic-kits-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-130-microfluidic-lab-on-a-chip-diagnostic-kits-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
