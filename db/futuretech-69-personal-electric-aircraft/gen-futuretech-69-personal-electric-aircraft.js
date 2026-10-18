(function(){'use strict';
/* JAH The Personal Electric Aircraft Future Technology Database generator — jahdb-futuretech-69-personal-electric-aircraft-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT69-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "1933: the Flying Flea - Build Your Own Plane - Foundations",
  "1938: the Piper Cub - Everyman's Airplane - Foundations",
  "1940: the Ercoupe - Anyone Can Fly - Foundations",
  "1953: Homebuilders Organize - Foundations",
  "1970s: Ultralights - Cheap Flight - Foundations",
  "1982: Part 103 - Ultralights Legal - Foundations",
  "1990s: Powered Paragliders - Foundations",
  "2008: ICON A5 - the Jet-Ski Plane - Foundations",
  "2017: the GoFly Prize - Foundations",
  "2018: BlackFly - the Personal eVTOL - Foundations",
  "2021: AirCar Flies Between Cities - Foundations"
 ],
 "Compounded": [
  "2021: Jetson ONE - the $92k Flyer - Compounded",
  "2021: Xpeng X2 - Compounded",
  "2022: Personal eVTOLs Sell Out - Compounded",
  "2022: Dubai Sees the X2 - Compounded",
  "2023: Pivotal Helix - Compounded",
  "2023: MOSAIC Modernizes - Compounded",
  "2024: Driveway Aircraft Sell - Compounded",
  "2024: the Land Aircraft Carrier - Compounded",
  "2024: Learning to Fly Electric - Compounded",
  "2025: Deliveries to Driveways - Compounded",
  "2025: the Rules Clarify - Compounded",
  "2025: the Safety Record - Compounded"
 ],
 "Advanced": [
  "2025: Flying Car Meets - Advanced",
  "2025: Prices Fall - Advanced",
  "Certified Personal eVTOL - Advanced",
  "Driveway Aircraft - Advanced",
  "Personal Air Commuting - Advanced",
  "Autonomous Personal Flight - Advanced",
  "Shared Personal Aircraft - Advanced",
  "Rural Air Mobility - Advanced",
  "The Flying Car in Every Garage - Advanced",
  "The Managed Personal Sky - Advanced",
  "Everyday Personal Flight - Working Version - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Future Technology Study — "+safe+"\n"
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
  var id=PREFIX+String(seed).padStart(4,'0');
  return {
    id:id,
    name:topic+' — personal electric aircraft record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A personal electric aircraft record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-69-personal-electric-aircraft-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{4}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-futuretech-69-personal-electric-aircraft-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-69-personal-electric-aircraft',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
