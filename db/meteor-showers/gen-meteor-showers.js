(function(){'use strict';
/* JAH Meteor Showers Database generator — jahdb-meteor-showers-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MSHR-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Meteor Showers: An Overview", "What a Meteor Is: Dust Becoming Light", "The Perseids: August's Great Shower", "The Geminids: December's Finest", "The Leonids: Storms of History", "The Quadrantids: January's Sharp Peak", "The Orionids: Halley's Debris", "The Eta Aquariids: Halley's Other Shower", "The Lyrids: April's Oldest Shower", "The Radiant: Perspective in the Sky", "ZHR Explained: Counting Meteors Right"], "Compounded": ["Parent Bodies: Comets and Rock Comets", "The Draconids: The Sleeping Dragon", "The Taurids: Fireball Season", "The Ursids: The Solstice Shower", "The Alpha Capricornids: Slow Fireballs", "Meteor Storms: When the Sky Falls", "The 1833 Leonid Storm: The Night the Stars Fell", "Fireballs and Bolides: The Bright Ones", "Observing Basics: How to Watch", "Moonlight and Showers: The Great Spoiler", "The American Meteor Society: The Observers' Network", "Meteor vs. Meteorite: What's the Difference"], "Advanced": ["Dust-Trail Modeling: Predicting Storms", "Outburst Prediction: The Forecasters", "The 1999-2002 Leonid Storms: Predicted and Delivered", "Radar Meteor Science: Seeing the Invisible", "Infrasound Detection: Hearing Meteors", "Meteorite-Dropping Fireballs: From Sky to Lab", "The IMO Shower Calendar: The Year's Almanac", "The Global Meteor Network: Cameras Everywhere", "Spectroscopy of Meteors: Reading the Flash", "The Year's Shower Calendar: Never Miss One", "Meteor Science by the Numbers"]};
var KIND="meteor shower record";
var SRC="public-harvest";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — sample demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "def summarize():\n"
   + "    return TOPIC + ' [' + FIELD + ']'\n"
   + "print(summarize())\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={
    id:id,
    name:topic+' — '+KIND,
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A '+KIND+' of "'+topic+'" in '+field+'. Generated sample records are clearly labeled and never presented as archive records.',
    field:field,
    src:SRC,
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"sample-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
  if(SRC==='signature')rec.signature_label='Signature original - created in the Signature system; not a public record.';
  return rec;
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
var gen={version:"jahdb-meteor-showers-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("meteor-showers",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
