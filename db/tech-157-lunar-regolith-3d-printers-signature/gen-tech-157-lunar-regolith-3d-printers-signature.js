(function(){'use strict';
/* JAH The Signature Lunar Regolith 3D Printers Database generator — jahdb-tech-157-lunar-regolith-3d-printers-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET157S-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The Signature Approach to Lunar Regolith 3D Printers (Signature)","Signature Research and Development Program (Signature)","Signature Design Specifications (Signature)","Signature Development Roadmap (Signature)","Signature Design Challenges (Signature)"],"Compounded": ["Signature Regolith Sinterer (Signature)","Signature Mobile Printer (Signature)","Signature Habitat Shell (Signature)","Signature Landing Pad (Signature)","Signature Binder System (Signature)","Signature Excavator (Signature)","Signature Power System (Signature)"],"Advanced": ["Signature Dust Mitigation (Signature)","Signature Autonomy Stack (Signature)","Signature Test Campaign (Signature)","Signature Flight Demo (Signature)","Signature Base Architecture (Signature)","Signature Road Builder (Signature)","Signature Mars Adaptation (Signature)","Signature Commercial Model (Signature)"]};
var DEMOKIND="signature lunar regolith 3d printer record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# signature lunar regolith 3d printer record planner — "+safe+"\n"
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
    name:topic+' — signature lunar regolith 3d printer record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A signature lunar regolith 3d printer record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-157-lunar-regolith-3d-printers-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-157-lunar-regolith-3d-printers-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
