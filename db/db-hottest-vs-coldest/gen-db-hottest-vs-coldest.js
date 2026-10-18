(function(){'use strict';
/* JAH The Hottest vs. Coldest Database generator — jahdb-db-hottest-vs-coldest-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HVC-";
var FIELDS=["Temperature Foundations","Heat Extremes","Cold Extremes"];
var TOPICS={
 "Temperature Foundations": [
  "Sun's Core vs Absolute Zero: Thermal Limits - Temperature Foundations",
  "Lava vs Dry Ice: Touchable Extremes - Temperature Foundations",
  "Death Valley vs Antarctica: Earth Extremes - Temperature Foundations",
  "Sauna vs Cryochamber: Human Extremes - Temperature Foundations",
  "Forge vs Freezer: Workshop Extremes - Temperature Foundations",
  "CPU vs Heatsink: Chip Thermal Battle - Temperature Foundations",
  "Lightning vs Lava: Hotter? - Temperature Foundations",
  "Oven vs Stovetop: Kitchen Heat - Temperature Foundations",
  "Desert Day vs Desert Night: Daily Swing - Temperature Foundations",
  "Fever vs Hypothermia: Body Extremes - Temperature Foundations",
  "Match vs Lighter: Pocket Fire - Temperature Foundations",
  "Tropical Sea vs Polar Sea: Ocean Heat - Temperature Foundations"
 ],
 "Heat Extremes": [
  "Blast Furnace vs Crematorium: Industrial Fire - Heat Extremes",
  "Nuclear Core vs Sun's Surface: Human vs Star - Heat Extremes",
  "Reentry vs Meteor: Falling Fire - Heat Extremes",
  "Wildfire vs Volcano: Natural Infernos - Heat Extremes",
  "Glass Furnace vs Kiln: Maker's Heat - Heat Extremes",
  "Jet Exhaust vs Rocket Exhaust: Propulsion Heat - Heat Extremes",
  "Pizza Oven vs Home Oven: Food Fire - Heat Extremes",
  "Thermite vs Welding Torch: Cutting Heat - Heat Extremes",
  "Desert Surface vs Sauna Rocks: Hottest Touch - Heat Extremes",
  "Magma Chamber vs Earth's Core: Deep Heat - Heat Extremes"
 ],
 "Cold Extremes": [
  "Liquid Nitrogen vs Dry Ice: Cold Lab - Cold Extremes",
  "Antarctic Winter vs Arctic Winter: Pole Cold - Cold Extremes",
  "Cryosleep (Sci-Fi) vs Hibernation: Cold Rest - Cold Extremes",
  "Ice Age vs Nuclear Winter: Cold Worlds - Cold Extremes",
  "Frozen Lake vs Glacier: Ice Water - Cold Extremes",
  "Cold Brew vs Iced Coffee: Chill Drinks - Cold Extremes",
  "Snow vs Hail: Frozen Sky - Cold Extremes",
  "Permafrost vs Season Frost: Ground Cold - Cold Extremes",
  "Ice Bath vs Cold Shower: Bracing Rituals - Cold Extremes",
  "Comet vs Snowball: Dirty Ice - Cold Extremes",
  "Deep Ocean vs Surface Ocean: Cold Depths - Cold Extremes",
  "Winter Night vs Summer Night: Sky Cold - Cold Extremes"
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
var gen={version:'jahdb-db-hottest-vs-coldest-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-hottest-vs-coldest',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
