(function(){'use strict';
/* JAH The Delta-V Spaceflight Database generator — jahdb-delta-v-spaceflight-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DV-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Delta-V: The Currency of Spaceflight \u2014 Foundations",
  "The Tsiolkovsky Rocket Equation \u2014 Foundations",
  "Exhaust Velocity and Specific Impulse \u2014 Foundations",
  "Propellant Mass Fraction \u2014 Foundations",
  "The Mass Ratio and the Exponential Penalty \u2014 Foundations",
  "Staging: Shedding Dead Weight \u2014 Foundations",
  "Units: Meters per Second and Kilometers per Second \u2014 Foundations",
  "Circular Orbit Velocity and Escape Velocity \u2014 Foundations",
  "Reading a Delta-V Map \u2014 Foundations",
  "Gravity Losses and Drag Losses \u2014 Foundations",
  "The Tyranny of the Rocket Equation \u2014 Foundations"
 ],
 "Compounded": [
  "Hohmann Transfer: The Minimum-Energy Orbit Change \u2014 Compounded",
  "Bi-Elliptic Transfer \u2014 Compounded",
  "Plane-Change Maneuver \u2014 Compounded",
  "The Oberth Effect \u2014 Compounded",
  "Gravity Assist: Stealing Energy from Planets \u2014 Compounded",
  "Aerocapture vs. Aerobraking \u2014 Compounded",
  "Ion Propulsion and Low-Thrust Spirals \u2014 Compounded",
  "Engine Specific Impulse Table \u2014 Compounded",
  "Apollo Mission Delta-V Budget \u2014 Compounded",
  "Mars Hohmann Transfer Budget \u2014 Compounded",
  "C3 and Hyperbolic Excess Velocity \u2014 Compounded",
  "Stationkeeping and ISS Reboost \u2014 Compounded"
 ],
 "Advanced": [
  "Patched Conics \u2014 Advanced",
  "Lambert's Problem and Porkchop Plots \u2014 Advanced",
  "Bi-Elliptic vs. Hohmann Tradeoff Analysis \u2014 Advanced",
  "Combined Plane-Change and Circularization \u2014 Advanced",
  "Cryogenic vs. Storable vs. Solid Propellants \u2014 Advanced",
  "Earth-Surface to Mars-Surface Budget \u2014 Advanced",
  "Cassini Tour: A Delta-V Case Study \u2014 Advanced",
  "Interstellar Delta-V Scale \u2014 Advanced",
  "Launch Vehicle Delta-V Comparison \u2014 Advanced",
  "The Rocket Equation's Hard Limits \u2014 Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  var body;
  if(field==="Compounded"){
    body="# Compounded study: Hohmann-style transfer leg calculator\n"
     + "import math\n"
     + "MU=398600.4418\n"
     + "def hohmann(r1,r2):\n"
     + "    a=(r1+r2)/2.0\n"
     + "    dv1=math.sqrt(MU*(2.0/r1-1.0/a))-math.sqrt(MU/r1)\n"
     + "    dv2=math.sqrt(MU/r2)-math.sqrt(MU*(2.0/r2-1.0/a))\n"
     + "    return dv1,dv2,dv1+dv2\n"
     + "dv1,dv2,tot=hohmann(6578.0,42164.0)\n"
     + "print('LEO->GEO: burn1 %.2f km/s, burn2 %.2f km/s, total %.2f km/s' % (dv1,dv2,tot))\n";
  }else if(field==="Advanced"){
    body="# Advanced study: single-stack delta-v ceiling vs propellant fraction\n"
     + "import math\n"
     + "VE=465.5*9.80665\n"
     + "for f in (0.90,0.95,0.99):\n"
     + "    print('fraction %.2f -> ceiling %.1f km/s' % (f, VE*math.log(1.0/(1.0-f))/1000.0))\n";
  }else{
    body="# Foundations study: the Tsiolkovsky rocket equation\n"
     + "import math\n"
     + "G0=9.80665\n"
     + "def rocket_dv(isp,m0,mf):\n"
     + "    return isp*G0*math.log(m0/mf)\n"
     + "print('dv = %.0f m/s' % rocket_dv(450.0,10000.0,2500.0))\n";
  }
  return "# Delta-V Study \u2014 "+safe+"\n"
   + "# Tier: "+field+"\n"
   + body
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
    name:topic+' \u2014 delta-v spaceflight record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A delta-v spaceflight record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"delta-v-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-delta-v-spaceflight-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('delta-v-spaceflight',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
