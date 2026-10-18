(function(){'use strict';
/* JAH The Giant vs. Tiny Database generator — jahdb-db-giant-vs-tiny-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GVT-";
var FIELDS=["Giants of Nature","Giants of Engineering","The Tiny Mighty"];
var TOPICS={
 "Giants of Nature": [
  "Blue Whale vs Krill: Ocean Extremes - Giants of Nature",
  "Coast Redwood vs Bonsai: Tree Extremes - Giants of Nature",
  "African Elephant vs Etruscan Shrew: Mammal Extremes - Giants of Nature",
  "Whale Shark vs Seahorse: Fish Extremes - Giants of Nature",
  "Giant Tortoise vs Dart Frog: Slow Giants vs Tiny Jewels - Giants of Nature",
  "Ostrich vs Bee Hummingbird: Bird Extremes - Giants of Nature",
  "Giant Sequoia vs Grass Blade: Plant Scale - Giants of Nature",
  "Colossal Squid vs Plankton: Deep Extremes - Giants of Nature",
  "Komodo Dragon vs Gecko: Lizard Extremes - Giants of Nature",
  "Polar Bear vs Lemming: Arctic Extremes - Giants of Nature",
  "Anaconda vs Thread Snake: Snake Extremes - Giants of Nature",
  "Goliath Beetle vs Ant: Insect Heavyweight vs Workhorse - Giants of Nature"
 ],
 "Giants of Engineering": [
  "Burj Khalifa vs Tiny House: Dwelling Extremes - Giants of Engineering",
  "Aircraft Carrier vs Kayak: Vessel Extremes - Giants of Engineering",
  "Saturn V vs Model Rocket: Rocket Extremes - Giants of Engineering",
  "Hoover Dam vs Beaver Dam: Dam Builders - Giants of Engineering",
  "Cargo Ship vs Canoe: Hauling Extremes - Giants of Engineering",
  "Wind Turbine vs Desk Fan: Air Movers - Giants of Engineering",
  "Great Pyramid vs Sandcastle: Built to Last? - Giants of Engineering",
  "Stadium vs Phone Booth: Crowd Extremes - Giants of Engineering",
  "Jumbo Jet vs Paper Plane: Flight Extremes - Giants of Engineering",
  "Suspension Bridge vs Toothpick Bridge: Span Extremes - Giants of Engineering",
  "Freight Train vs Toy Train: Rail Extremes - Giants of Engineering",
  "Supertanker vs Toy Boat: Float Extremes - Giants of Engineering"
 ],
 "The Tiny Mighty": [
  "Library vs Single Book: Knowledge Scale - The Tiny Mighty",
  "Ocean vs Droplet: Water Extremes - The Tiny Mighty",
  "City vs Village: Human Scale - The Tiny Mighty",
  "Stadium Screen vs Smartwatch: Display Extremes - The Tiny Mighty",
  "Old-Growth Forest vs Meadow: Ecosystem Scale - The Tiny Mighty",
  "Skyscraper vs Doghouse: Shelter Extremes - The Tiny Mighty",
  "Highway vs Garden Path: Road Extremes - The Tiny Mighty",
  "Symphony Orchestra vs Solo Whistle: Music Scale - The Tiny Mighty",
  "Waterfall vs Dripping Faucet: Flow Extremes - The Tiny Mighty",
  "Galaxy vs Snowflake: Cosmic vs Tiny Patterns - The Tiny Mighty"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Giant Vs Tiny Study — "+safe+"\n"
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
    name:topic+' — size comparison record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A size comparison record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"giant-vs-tiny-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-giant-vs-tiny-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-giant-vs-tiny',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
