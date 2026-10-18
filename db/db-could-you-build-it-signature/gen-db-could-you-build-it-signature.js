(function(){'use strict';
/* JAH The Could You Build It? Signature Database generator — jahdb-db-could-you-build-it-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CYBIS-";
var FIELDS=["Everyday Inventions","Ambitious Builds","Moonshots"];
var TOPICS={
 "Everyday Inventions": [
  "Backyard Treehouse vs Physics: Could You Build It? (Signature Edition) - Everyday Inventions",
  "Home Solar vs Grid: Could You Power It? (Signature Edition) - Everyday Inventions",
  "DIY Robot vs Kit Reality: Could You Build It? (Signature Edition) - Everyday Inventions",
  "Backyard Forge vs Safety: Could You Build It? (Signature Edition) - Everyday Inventions",
  "Rain Barrel vs Plumbing: Could You Build It? (Signature Edition) - Everyday Inventions",
  "Chicken Coop vs Zoning: Could You Build It? (Signature Edition) - Everyday Inventions",
  "Workshop Shed vs Permits: Could You Build It? (Signature Edition) - Everyday Inventions",
  "Pizza Oven vs Backyard: Could You Build It? (Signature Edition) - Everyday Inventions",
  "Greenhouse vs Climate: Could You Build It? (Signature Edition) - Everyday Inventions",
  "Home Battery vs Blackout: Could You Build It? (Signature Edition) - Everyday Inventions",
  "Aquaponics vs Garden: Could You Build It? (Signature Edition) - Everyday Inventions",
  "Tiny House vs Code: Could You Build It? (Signature Edition) - Everyday Inventions"
 ],
 "Ambitious Builds": [
  "Jetpack vs Physics: Could You Build It? (Signature Edition) - Ambitious Builds",
  "Submarine vs Pressure: Could You Build It? (Signature Edition) - Ambitious Builds",
  "Hovercraft vs Water: Could You Build It? (Signature Edition) - Ambitious Builds",
  "Wind Turbine (Home) vs Wind: Could You Build It? (Signature Edition) - Ambitious Builds",
  "Electric Car Conversion vs New EV: Could You Build It? (Signature Edition) - Ambitious Builds",
  "Cabin vs Wilderness: Could You Build It? (Signature Edition) - Ambitious Builds",
  "Boat vs Ocean: Could You Build It? (Signature Edition) - Ambitious Builds",
  "Airplane (Kit) vs Sky: Could You Build It? (Signature Edition) - Ambitious Builds",
  "Castle vs Budget: Could You Build It? (Signature Edition) - Ambitious Builds",
  "Bunker vs Fear: Could You Build It? (Signature Edition) - Ambitious Builds"
 ],
 "Moonshots": [
  "Space Elevator vs Materials: Could You Build It? (Signature Edition) - Moonshots",
  "Underwater City vs Pressure: Could You Build It? (Signature Edition) - Moonshots",
  "Mars Colony vs Everything: Could You Build It? (Signature Edition) - Moonshots",
  "Dyson Swarm vs Energy: Could You Build It? (Signature Edition) - Moonshots",
  "Floating City vs Ocean: Could You Build It? (Signature Edition) - Moonshots",
  "Weather Control vs Atmosphere: Could You Build It? (Signature Edition) - Moonshots",
  "Asteroid Mining vs Distance: Could You Build It? (Signature Edition) - Moonshots",
  "Fusion Reactor (Home) vs Physics: Could You Build It? (Signature Edition) - Moonshots",
  "Teleportation vs Quantum: Could You Build It? (Signature Edition) - Moonshots",
  "Time Machine vs Causality: Could You Build It? (Signature Edition) - Moonshots",
  "Perpetual Motion vs Thermodynamics: Could You Build It? (Signature Edition) - Moonshots",
  "Antimatter Engine vs Production: Could You Build It? (Signature Edition) - Moonshots"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Could You Build It Study — "+safe+"\n"
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
    name:topic+' — build feasibility record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A build feasibility record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"could-you-build-it-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-could-you-build-it-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-could-you-build-it-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
