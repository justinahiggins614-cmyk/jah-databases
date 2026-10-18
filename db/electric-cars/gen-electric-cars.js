(function(){'use strict';
/* JAH Electric Cars Database generator — "jahdb-electric-cars-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EVCAR-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={"foundations": ["How Electric Cars Work", "Lithium-Ion Batteries: The Enabler", "The First Electric Cars: 1890s", "GM EV1: The Pioneer", "Tesla Model S: The Game Changer", "Nissan Leaf: The Mass EV", "Tesla Model 3: The Volume", "Charging: Levels 1, 2, and DC Fast", "Range Anxiety and Its Cure", "Total Cost of Ownership", "EV Motors: AC Induction to Permanent Magnet"], "compounded": ["BYD: China's EV Giant", "Volkswagen ID: The Legacy Pivot", "Hyundai-Kia E-GMP: The 800V", "Ford Mach-E and F-150 Lightning", "Rivian: The Adventure EV", "Lucid Air: The Efficiency King", "Solid-State Batteries: The Promise", "Battery Swapping: NIO's Answer", "Vehicle-to-Grid: The Car as Power Plant", "Electric Trucks and Semis", "Electric Buses: The Transit Workhorse", "Charging Networks: The Electron Highways"], "advanced": ["EV Fires: The Safety Record", "Battery Recycling: The Circular Pack", "Mining Ethics: Lithium and Cobalt", "Winter Range: The Cold Truth", "Formula E: Electric Racing", "Electric Motorcycles: The Silent Ride", "E-Bikes: The Micromobility Revolution", "Autonomous EVs: The Self-Driving Electric", "Wireless Charging: The Cut Cord", "Aptera and Solar EVs", "The Electric Decade: Capstone"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# "+safe+" — structural sample demo\n"
    + "RECORD = "+JSON.stringify({topic:safe,field:field})+"\n"
    + "def main():\n"
    + "    print('Record:', RECORD['topic'])\n"
    + "    print('Field:', RECORD['field'])\n"
    + "    vals = [3, 7, 11]\n"
    + "    print('Sample values:', vals)\n"
    + "    print('Total:', sum(vals))\n"
    + "    print('Demo complete.')\n"
    + "if __name__ == '__main__':\n"
    + "    main()\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — structural sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A '+field+' sample on "'+topic+'". Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"sample-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-electric-cars-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("electric-cars",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
