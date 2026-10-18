(function(){'use strict';
/* JAH Helicopters Database generator — "jahdb-helicopters-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HELI-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={"foundations": ["How a Helicopter Flies: Lift from Rotors", "Cyclic, Collective, and Anti-Torque: The Controls", "Autorotation: Flying Without Engine Power", "The Autogyro: Rotorcraft Ancestor", "Sikorsky VS-300: First Practical Helicopter", "Sikorsky R-4: First Mass-Produced Helicopter", "Bell 47: The Bubble-Canopy Classic", "Alouette II: First Turbine Helicopter", "Robinson R22: The Training Standard", "Ground Effect and Translating Tendency", "Retreating Blade Stall and Rotor Limits"], "compounded": ["Bell UH-1 Iroquois ‘Huey’", "Bell 206 JetRanger", "Hughes OH-6 Cayuse", "Sikorsky CH-47 Chinook: Tandem Rotor", "Mil Mi-8: The World's Most-Produced Helicopter", "Sikorsky S-61 Sea King", "Aérospatiale SA 330 Puma", "Bölkow Bo 105: Rigid Rotor", "MD 500 Series: Light-Utility Legend", "Bell 212 and 412: Twin Huey", "Sikorsky UH-60 Black Hawk", "Boeing AH-64 Apache"], "advanced": ["Mil Mi-24 Hind: Gunship Transport", "Kamov Ka-50 and Ka-52: Coaxial Rotors", "Airbus H135: Light-Twin Standard", "Leonardo AW139: Medium-Twin Workhorse", "Sikorsky S-92: Medium-Lift Standard", "Bell 525 Relentless: Fly-by-Wire Helicopter", "NOTAR: No Tail Rotor", "Bell-Boeing V-22 Osprey: Tiltrotor", "Leonardo AW609 Tiltrotor", "Electric and eVTOL Rotorcraft", "Helicopter Safety and Maintenance Essentials"]};
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
var gen={version:"jahdb-helicopters-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("helicopters",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
