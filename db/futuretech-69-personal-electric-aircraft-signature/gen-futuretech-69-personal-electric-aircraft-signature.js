(function(){'use strict';
/* JAH The Personal Electric Aircraft Future Technology Database — Signature Edition generator — jahdb-futuretech-69-personal-electric-aircraft-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT69-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Personal Electric Aircraft — the Flying Flea - Build Your Own Plane (Signature Edition)", "Personal Electric Aircraft — the Piper Cub - Everyman's Airplane (Signature Edition)", "Personal Electric Aircraft — the Ercoupe - Anyone Can Fly (Signature Edition)", "Personal Electric Aircraft — Homebuilders Organize (Signature Edition)", "Personal Electric Aircraft — Ultralights - Cheap Flight (Signature Edition)", "Personal Electric Aircraft — Part 103 - Ultralights Legal (Signature Edition)", "Personal Electric Aircraft — Powered Paragliders (Signature Edition)", "Personal Electric Aircraft — ICON A5 - the Jet-Ski Plane (Signature Edition)", "Personal Electric Aircraft — the GoFly Prize (Signature Edition)", "Personal Electric Aircraft — BlackFly - the Personal eVTOL (Signature Edition)", "Personal Electric Aircraft — AirCar Flies Between Cities (Signature Edition)"], "Compounded": ["Personal Electric Aircraft — Jetson ONE - the $92k Flyer (Signature Edition)", "Personal Electric Aircraft — Xpeng X2 (Signature Edition)", "Personal Electric Aircraft — Personal eVTOLs Sell Out (Signature Edition)", "Personal Electric Aircraft — Dubai Sees the X2 (Signature Edition)", "Personal Electric Aircraft — Pivotal Helix (Signature Edition)", "Personal Electric Aircraft — MOSAIC Modernizes (Signature Edition)", "Personal Electric Aircraft — Driveway Aircraft Sell (Signature Edition)", "Personal Electric Aircraft — the Land Aircraft Carrier (Signature Edition)", "Personal Electric Aircraft — Learning to Fly Electric (Signature Edition)", "Personal Electric Aircraft — Deliveries to Driveways (Signature Edition)", "Personal Electric Aircraft — the Rules Clarify (Signature Edition)", "Personal Electric Aircraft — the Safety Record (Signature Edition)"], "Advanced": ["Personal Electric Aircraft — Flying Car Meets (Signature Edition)", "Personal Electric Aircraft — Prices Fall (Signature Edition)", "Personal Electric Aircraft — Certified Personal eVTOL (Signature Edition)", "Personal Electric Aircraft — Driveway Aircraft (Signature Edition)", "Personal Electric Aircraft — Personal Air Commuting (Signature Edition)", "Personal Electric Aircraft — Autonomous Personal Flight (Signature Edition)", "Personal Electric Aircraft — Shared Personal Aircraft (Signature Edition)", "Personal Electric Aircraft — Rural Air Mobility (Signature Edition)", "Personal Electric Aircraft — The Flying Car in Every Garage (Signature Edition)", "Personal Electric Aircraft — The Managed Personal Sky (Signature Edition)", "Personal Electric Aircraft — Everyday Personal Flight - Working Version (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Personal Electric Aircraft study \u2014 "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record \u2014 structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — technology study record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A technology study record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-futuretech-69-personal-electric-aircraft-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-69-personal-electric-aircraft-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
