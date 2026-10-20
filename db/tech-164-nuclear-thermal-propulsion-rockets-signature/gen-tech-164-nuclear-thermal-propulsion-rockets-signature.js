(function(){'use strict';
/* JAH The Signature Nuclear Thermal Propulsion Rockets Database generator — jahdb-tech-164-nuclear-thermal-propulsion-rockets-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET164S-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The Signature Approach to Nuclear Thermal Propulsion Rockets (Signature)","Signature Research and Development Program (Signature)","Signature Design Specifications (Signature)","Signature Development Roadmap (Signature)","Signature Design Challenges (Signature)"],"Compounded": ["Signature NTP Reactor (Signature)","Signature HALEU Fuel (Signature)","Signature Hydrogen Tank (Signature)","Signature Radiation Shield (Signature)","Signature Ground Test (Signature)","Signature Flight Demo (Signature)","Signature Mars Transit (Signature)"],"Advanced": ["Signature Safety Framework (Signature)","Signature Public Engagement (Signature)","Signature Cargo Missions (Signature)","Signature Outer Planets (Signature)","Signature Bimodal Power (Signature)","Signature Regulatory Path (Signature)","Signature International Program (Signature)","Signature Next Gen (Signature)"]};
var DEMOKIND="signature nuclear thermal propulsion rocket record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# signature nuclear thermal propulsion rocket record planner — "+safe+"\n"
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
    name:topic+' — signature nuclear thermal propulsion rocket record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A signature nuclear thermal propulsion rocket record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-164-nuclear-thermal-propulsion-rockets-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-164-nuclear-thermal-propulsion-rockets-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
