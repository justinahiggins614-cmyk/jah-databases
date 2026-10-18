(function(){'use strict';
/* JAH The Hottest vs. Coldest Signature Database generator — jahdb-db-hottest-vs-coldest-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HVCS-";
var FIELDS=["Temperature Foundations","Heat Extremes","Cold Extremes"];
var TOPICS={
 "Temperature Foundations": [
  "Sun's Core vs Absolute Zero: Thermal Limits (Signature Edition) - Temperature Foundations",
  "Lava vs Dry Ice: Touchable Extremes (Signature Edition) - Temperature Foundations",
  "Death Valley vs Antarctica: Earth Extremes (Signature Edition) - Temperature Foundations",
  "Sauna vs Cryochamber: Human Extremes (Signature Edition) - Temperature Foundations",
  "Forge vs Freezer: Workshop Extremes (Signature Edition) - Temperature Foundations",
  "CPU vs Heatsink: Chip Thermal Battle (Signature Edition) - Temperature Foundations",
  "Lightning vs Lava: Hotter? (Signature Edition) - Temperature Foundations",
  "Oven vs Stovetop: Kitchen Heat (Signature Edition) - Temperature Foundations",
  "Desert Day vs Desert Night: Daily Swing (Signature Edition) - Temperature Foundations",
  "Fever vs Hypothermia: Body Extremes (Signature Edition) - Temperature Foundations",
  "Match vs Lighter: Pocket Fire (Signature Edition) - Temperature Foundations",
  "Tropical Sea vs Polar Sea: Ocean Heat (Signature Edition) - Temperature Foundations"
 ],
 "Heat Extremes": [
  "Blast Furnace vs Crematorium: Industrial Fire (Signature Edition) - Heat Extremes",
  "Nuclear Core vs Sun's Surface: Human vs Star (Signature Edition) - Heat Extremes",
  "Reentry vs Meteor: Falling Fire (Signature Edition) - Heat Extremes",
  "Wildfire vs Volcano: Natural Infernos (Signature Edition) - Heat Extremes",
  "Glass Furnace vs Kiln: Maker's Heat (Signature Edition) - Heat Extremes",
  "Jet Exhaust vs Rocket Exhaust: Propulsion Heat (Signature Edition) - Heat Extremes",
  "Pizza Oven vs Home Oven: Food Fire (Signature Edition) - Heat Extremes",
  "Thermite vs Welding Torch: Cutting Heat (Signature Edition) - Heat Extremes",
  "Desert Surface vs Sauna Rocks: Hottest Touch (Signature Edition) - Heat Extremes",
  "Magma Chamber vs Earth's Core: Deep Heat (Signature Edition) - Heat Extremes"
 ],
 "Cold Extremes": [
  "Liquid Nitrogen vs Dry Ice: Cold Lab (Signature Edition) - Cold Extremes",
  "Antarctic Winter vs Arctic Winter: Pole Cold (Signature Edition) - Cold Extremes",
  "Cryosleep (Sci-Fi) vs Hibernation: Cold Rest (Signature Edition) - Cold Extremes",
  "Ice Age vs Nuclear Winter: Cold Worlds (Signature Edition) - Cold Extremes",
  "Frozen Lake vs Glacier: Ice Water (Signature Edition) - Cold Extremes",
  "Cold Brew vs Iced Coffee: Chill Drinks (Signature Edition) - Cold Extremes",
  "Snow vs Hail: Frozen Sky (Signature Edition) - Cold Extremes",
  "Permafrost vs Season Frost: Ground Cold (Signature Edition) - Cold Extremes",
  "Ice Bath vs Cold Shower: Bracing Rituals (Signature Edition) - Cold Extremes",
  "Comet vs Snowball: Dirty Ice (Signature Edition) - Cold Extremes",
  "Deep Ocean vs Surface Ocean: Cold Depths (Signature Edition) - Cold Extremes",
  "Winter Night vs Summer Night: Sky Cold (Signature Edition) - Cold Extremes"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Hottest Vs Coldest Study — "+safe+"\n"
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
    name:topic+' — temperature comparison record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A temperature comparison record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"hottest-vs-coldest-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-hottest-vs-coldest-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-hottest-vs-coldest-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
