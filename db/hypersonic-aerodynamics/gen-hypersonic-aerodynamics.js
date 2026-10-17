(function(){'use strict';
/* JAH The Hypersonic Aerodynamics Database generator — jahdb-hypersonic-aerodynamics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HYP-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Hypersonic Means: Speeds Past Mach 5 - Foundations",
  "Hypersonic Shocks: Thin, Close, and Hot - Foundations",
  "Mach-Number Independence: Why Hypersonics Stops Changing - Foundations",
  "Newtonian Impact Theory: Pressure From Particle Impacts - Foundations",
  "Hypersonic Similarity Parameters: Scaling the Heat - Foundations",
  "Strong and Weak Shocks at Hypersonic Speed - Foundations",
  "Stagnation Conditions: The Hot Point - Foundations",
  "The Perfect Gas Assumption and Where It Breaks - Foundations"
 ],
 "Compounded": [
  "Real-Gas Effects: Vibration, Dissociation, Ionization - Compounded",
  "The Blast-Wave Analogy: Shocks Like Explosions - Compounded",
  "Why Hypersonic Noses Are Blunt: The Standoff Trade - Compounded",
  "Stagnation-Point Heating: Sutton-Graves and Fay-Riddell - Compounded",
  "Where the Heat Lands: Heating Distribution Around the Body - Compounded",
  "Thermal Protection Systems: Rethinking the Skin - Compounded",
  "Ablation Physics: Sacrificing the Shield - Compounded",
  "Reentry Vehicle Dynamics: The Corridor and the Curve - Compounded",
  "Viscous Interaction: When the Boundary Layer Moves the Shock - Compounded",
  "Hypersonic Transition: Where Laminar Flow Ends - Compounded",
  "Shock/Boundary-Layer Interaction at Hypersonic Speed - Compounded",
  "The Entropy Layer: A Hot Blanket - Compounded",
  "Hypersonic Lift and Drag: The L/D Barrier - Compounded"
 ],
 "Advanced": [
  "The Scramjet Cycle: Combustion in Supersonic Flow - Advanced",
  "Scramjet Inlets: Compressing Without Slowing - Advanced",
  "Waveriders: Riding Your Own Shock Wave - Advanced",
  "Rarefied Gas Effects: Slip Flow and Free Molecules - Advanced",
  "High-Temperature Air Chemistry: The Five-Species Model - Advanced",
  "Hypersonic Test Facilities: Shock Tunnels and Expansion Tubes - Advanced",
  "Flight Test: X-15, X-43, X-51 and the Proving Years - Advanced",
  "Stability and Control at Hypersonic Speed - Advanced",
  "Chemical Nonequilibrium: Damkohler and Relaxation - Advanced",
  "Radiative Heating: The Glow of Return - Advanced",
  "Designing for Hypersonics: The Full Stack - Advanced",
  "Boost-Glide Vehicles: Falling With Style - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Hypersonic Study — "+safe+"\n"
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
    name:topic+' — hypersonic aerodynamics record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A hypersonic aerodynamics record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"hypersonic-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-hypersonic-aerodynamics-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('hypersonic-aerodynamics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
