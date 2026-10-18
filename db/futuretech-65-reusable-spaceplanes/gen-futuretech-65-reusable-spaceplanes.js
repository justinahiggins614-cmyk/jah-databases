(function(){'use strict';
/* JAH The Reusable Spaceplanes Future Technology Database generator — jahdb-futuretech-65-reusable-spaceplanes-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FT65-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "1930s: Silbervogel - the First Spaceplane Dream - Foundations",
  "1959: the X-15 - Wings to Space - Foundations",
  "1963: Dyna-Soar Canceled - Foundations",
  "1963: Wings Above 100 km - Foundations",
  "1972: the Shuttle Approved - Foundations",
  "1981: STS-1 - the Orbiter Flies - Foundations",
  "1986: Challenger - Foundations",
  "1988: Buran - the Robot Shuttle - Foundations",
  "2003: Columbia - Foundations",
  "2004: SpaceShipOne Wins the X Prize - Foundations",
  "2010: X-37B - the Robot Spaceplane - Foundations"
 ],
 "Compounded": [
  "2011: the Shuttle Retires - Compounded",
  "2012: Dream Chaser Takes Shape - Compounded",
  "2015: SABRE - Breathing to Orbit - Compounded",
  "2018: SpaceShipTwo Tests On - Compounded",
  "2020: the Enduring Robot - Compounded",
  "2021: Branson Flies - Compounded",
  "2022: Tenacity Takes Form - Compounded",
  "2023: Sierra Space Advances - Compounded",
  "2024: Tenacity Ready - Compounded",
  "2024: Stoke - the Reusable Upper Stage - Compounded",
  "2025: Spaceplanes Near Flight - Compounded",
  "2025: Radian - the SSTO Dream - Compounded"
 ],
 "Advanced": [
  "Dream Chaser Cargo Service - Advanced",
  "Crewed Dream Chaser - Advanced",
  "Point-to-Point Suborbital - Advanced",
  "Rapid-Turnaround Spaceplanes - Advanced",
  "Single-Stage-to-Orbit - Advanced",
  "Orbital Spaceplane Fleets - Advanced",
  "Routine Spaceplane Tourism - Advanced",
  "Spaceplane Satellite Servicing - Advanced",
  "90-Minute Intercontinental - Advanced",
  "Spaceplanes at Scale - Advanced",
  "The Everyday Spaceplane - Working Version - Advanced"
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
    name:topic+' — reusable spaceplane record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A reusable spaceplane record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"futuretech-65-reusable-spaceplanes-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-futuretech-65-reusable-spaceplanes-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('futuretech-65-reusable-spaceplanes',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
