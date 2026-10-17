(function(){'use strict';
/* JAH The Tunneling Database generator — jahdb-tunneling-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TUN-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Tunneling: The Art of Building Underground - Foundations",
  "Why Tunnels: Rivers, Ridges, and Congested Cities - Foundations",
  "Tunnel Types: Road, Rail, Water, and Mining Access - Foundations",
  "The Ground Is the Structure: Load, Behaviour, and Stand-Up Time - Foundations",
  "Excavation Methods at a Glance: Drill-and-Blast, Mechanical, and Cut-and-Cover - Foundations",
  "Cut-and-Cover: The Simplest Way Under - Foundations",
  "Portals: Where the Tunnel Meets the Daylight - Foundations"
 ],
 "Compounded": [
  "Drill-and-Blast: The Cycle That Built the Tunnels - Compounded",
  "Blast Design: Powder Factor, Patterns, and the Burn Cut - Compounded",
  "RMR: The Rock Mass Rating, Bieniawski's Field Scorecard - Compounded",
  "Q-System: Barton's Tunneling Quality Index, the Support Designer - Compounded",
  "GSI: The Geological Strength Index, Reading the Rock's Character - Compounded",
  "Rock Bolts: Stitching the Ground to Itself - Compounded",
  "Shotcrete: Concrete Sprayed Like Paint, Working Like Structure - Compounded",
  "Steel Sets and Lattice Girders: Arches for Ground That Cannot Arch - Compounded",
  "NATM / SEM: Building With the Ground, Not Against It - Compounded",
  "Roadheaders: The Milling Machines That Carve Rock - Compounded",
  "Tunnel Boring Machines: Open Gripper, Shielded, EPB, and Slurry - Compounded",
  "TBM Advance: Penetration, Utilization, and Metres per Day - Compounded",
  "Mucking and Haulage: Moving the Mountain Out - Compounded"
 ],
 "Advanced": [
  "Ground Support Pressure: Terzaghi, Bieniawski, and Barton - Advanced",
  "Tunnel Lining Design: Segmental Rings and Cast Concrete - Advanced",
  "Tunnel Ventilation: Fresh Air In, Fumes and Fire Out - Advanced",
  "Dewatering and Groundwater Control: Drying the Underground - Advanced",
  "Monitoring and Instrumentation: Listening to the Ground - Advanced",
  "Tunnel Safety and Rescue: Engineering for the Worst Day - Advanced",
  "Shaft Sinking: Building the Vertical Tunnel - Advanced",
  "Compressed Air and Pressurized-Face Working: Holding Back the Water - Advanced",
  "Raise Boring: Drilling Up from Below - Advanced",
  "Cutterhead Design and Cutter Wear: The Teeth of the Machine - Advanced",
  "Immersed Tunnels: Sinking the Tunnel Like a Ship - Advanced",
  "Tunnel Refurbishment: Giving Old Tunnels Their Second Century - Advanced",
  "Fault Zones and Squeezing Ground: Tunneling's Hardest Fight - Advanced",
  "The Economics of Tunneling: Cost per Metre and the Learning Curve - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Tunneling Study — "+safe+"\n"
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
    name:topic+' — tunneling record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A tunneling record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"tunneling-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-tunneling-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('tunneling',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
