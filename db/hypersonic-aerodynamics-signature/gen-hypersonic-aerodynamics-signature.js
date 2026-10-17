(function(){'use strict';
/* JAH The Hypersonic Aerodynamics Signature Database generator — jahdb-hypersonic-aerodynamics-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HYS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Hypersonic Means: Speeds Past Mach 5 (Signature Edition) - Foundations",
  "Hypersonic Shocks: Thin, Close, and Hot (Signature Edition) - Foundations",
  "Mach-Number Independence: Why Hypersonics Stops Changing (Signature Edition) - Foundations",
  "Newtonian Impact Theory: Pressure From Particle Impacts (Signature Edition) - Foundations",
  "Hypersonic Similarity Parameters: Scaling the Heat (Signature Edition) - Foundations",
  "Strong and Weak Shocks at Hypersonic Speed (Signature Edition) - Foundations",
  "Stagnation Conditions: The Hot Point (Signature Edition) - Foundations",
  "The Perfect Gas Assumption and Where It Breaks (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Real-Gas Effects: Vibration, Dissociation, Ionization (Signature Edition) - Compounded",
  "The Blast-Wave Analogy: Shocks Like Explosions (Signature Edition) - Compounded",
  "Why Hypersonic Noses Are Blunt: The Standoff Trade (Signature Edition) - Compounded",
  "Stagnation-Point Heating: Sutton-Graves and Fay-Riddell (Signature Edition) - Compounded",
  "Where the Heat Lands: Heating Distribution Around the Body (Signature Edition) - Compounded",
  "Thermal Protection Systems: Rethinking the Skin (Signature Edition) - Compounded",
  "Ablation Physics: Sacrificing the Shield (Signature Edition) - Compounded",
  "Reentry Vehicle Dynamics: The Corridor and the Curve (Signature Edition) - Compounded",
  "Viscous Interaction: When the Boundary Layer Moves the Shock (Signature Edition) - Compounded",
  "Hypersonic Transition: Where Laminar Flow Ends (Signature Edition) - Compounded",
  "Shock/Boundary-Layer Interaction at Hypersonic Speed (Signature Edition) - Compounded",
  "The Entropy Layer: A Hot Blanket (Signature Edition) - Compounded",
  "Hypersonic Lift and Drag: The L/D Barrier (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "The Scramjet Cycle: Combustion in Supersonic Flow (Signature Edition) - Advanced",
  "Scramjet Inlets: Compressing Without Slowing (Signature Edition) - Advanced",
  "Waveriders: Riding Your Own Shock Wave (Signature Edition) - Advanced",
  "Rarefied Gas Effects: Slip Flow and Free Molecules (Signature Edition) - Advanced",
  "High-Temperature Air Chemistry: The Five-Species Model (Signature Edition) - Advanced",
  "Hypersonic Test Facilities: Shock Tunnels and Expansion Tubes (Signature Edition) - Advanced",
  "Flight Test: X-15, X-43, X-51 and the Proving Years (Signature Edition) - Advanced",
  "Stability and Control at Hypersonic Speed (Signature Edition) - Advanced",
  "Chemical Nonequilibrium: Damkohler and Relaxation (Signature Edition) - Advanced",
  "Radiative Heating: The Glow of Return (Signature Edition) - Advanced",
  "Designing for Hypersonics: The Full Stack (Signature Edition) - Advanced",
  "Boost-Glide Vehicles: Falling With Style (Signature Edition) - Advanced"
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
var gen={version:'jahdb-hypersonic-aerodynamics-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('hypersonic-aerodynamics-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
