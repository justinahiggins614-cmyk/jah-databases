(function(){'use strict';
/* JAH The Signature Supersonic Commercial Passenger Jets Database generator — jahdb-tech-155-supersonic-commercial-passenger-jets-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-ET155S-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The Signature Approach to Supersonic Commercial Passenger Jets (Signature)","Signature Research and Development Program (Signature)","Signature Design Specifications (Signature)","Signature Development Roadmap (Signature)","Signature Design Challenges (Signature)"],"Compounded": ["Signature Low-Boom Airframe (Signature)","Signature Supersonic Engine (Signature)","Signature Thermal Structure (Signature)","Signature Cabin (Signature)","Signature SAF Fuel System (Signature)","Signature Boom Regulation (Signature)","Signature Route Network (Signature)"],"Advanced": ["Signature Ticket Economics (Signature)","Signature Airport Integration (Signature)","Signature Maintenance (Signature)","Signature Cargo Variant (Signature)","Signature Military Derivative (Signature)","Signature Certification (Signature)","Signature Next Generation (Signature)","Signature Passenger Experience (Signature)"]};
var DEMOKIND="signature supersonic commercial passenger jet record planner";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# signature supersonic commercial passenger jet record planner — "+safe+"\n"
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
    name:topic+' — signature supersonic commercial passenger jet record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A signature supersonic commercial passenger jet record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-tech-155-supersonic-commercial-passenger-jets-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tech-155-supersonic-commercial-passenger-jets-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
