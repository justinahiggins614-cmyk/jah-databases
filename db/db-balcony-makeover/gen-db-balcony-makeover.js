(function(){'use strict';
/* The The Balcony Makeover Database generator — jahdb-db-balcony-makeover-pub-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-BALCONY-MAKEOVER-PUB-";
var GENVER="jahdb-db-balcony-makeover-pub-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The Railing Herb Garden",
  "Bistro Corner for Two",
  "String Light Magic",
  "The Outdoor Rug Trick",
  "First Three Pots",
  "Privacy Screen in a Weekend",
  "The Reading Ledge",
  "Windbreak Basics",
  "Drainage Done Right",
  "The Sunrise Coffee Spot",
  "Folding Everything",
  "The $75 Makeover"
 ],
 "Compounded": [
  "Container Veggie Patch",
  "The Balcony Office",
  "Vertical Garden Wall",
  "Dining Al Fresco Setup",
  "The Pollinator Balcony",
  "Evening Lounge Build",
  "The Balcony Bar",
  "Seasonal Color Rotation",
  "Cat-Safe Balcony Garden",
  "The Workout Ledge",
  "The Morning Sun Trap",
  "The Herb Rail, Extended"
 ],
 "Advanced": [
  "The Outdoor Living Room",
  "Edible Balcony Abundance",
  "The Balcony Greenhouse",
  "Water Feature, Pint-Sized",
  "The Entertainer\u2019s Balcony",
  "Four-Season Balcony",
  "The Artist\u2019s Balcony Studio",
  "Balcony Cinema Nights",
  "The Legacy Balcony Garden",
  "Masterclass: Small-Space Design"
 ]
};
var BLURBS={
 "The Railing Herb Garden": "Rail-mounted planters with kitchen herbs. Cook with fresh basil steps from the stove.",
 "Bistro Corner for Two": "A folding table and two chairs: coffee, dinner, and conversation in four square feet.",
 "String Light Magic": "One strand of warm lights turns any concrete slab into an evening destination.",
 "The Outdoor Rug Trick": "An outdoor rug visually doubles a tiny balcony and hides ugly flooring instantly.",
 "First Three Pots": "Start with three forgiving plants matched to your sun. Success builds the garden.",
 "Privacy Screen in a Weekend": "Bamboo screening or tall planters block the sightlines. Instant outdoor room.",
 "The Reading Ledge": "One great chair, one side table, one lamp: a library with fresh air.",
 "Windbreak Basics": "A simple screen or dense planter row tames the wind that kills balcony comfort.",
 "Drainage Done Right": "Trays, feet, and soil mix that keep water where it belongs. Neighbor-friendly gardening.",
 "The Sunrise Coffee Spot": "Face the morning sun with a chair and a tiny table. The best minutes of the day.",
 "Folding Everything": "Folding furniture for balconies that must also dry laundry or store bikes. Flexibility wins.",
 "The $75 Makeover": "Rug, lights, and one plant: proof that tiny budgets make real transformations.",
 "Container Veggie Patch": "Tomatoes, peppers, and greens in pots: a real harvest from a railing and a corner.",
 "The Balcony Office": "A weather-savvy work corner for laptop days outside. Fresh air improves everything.",
 "Vertical Garden Wall": "Pocket planters or a trellis panel turn one wall into a living tapestry.",
 "Dining Al Fresco Setup": "A proper little dining set for outdoor meals: the balcony earns its keep nightly.",
 "The Pollinator Balcony": "Native flowers in pots feed bees and butterflies floors above the street.",
 "Evening Lounge Build": "Floor cushions, low table, lanterns: a lounge that rivals any living room.",
 "The Balcony Bar": "A rail-mounted bar shelf for drinks at sunset. Happy hour with a view.",
 "Seasonal Color Rotation": "Swap annuals four times a year: the balcony never looks tired.",
 "Cat-Safe Balcony Garden": "Netting and non-toxic plants make a balcony paradise cats can enjoy safely.",
 "The Workout Ledge": "A mat, a band, and a plan: the smallest gym with the best ventilation.",
 "The Morning Sun Trap": "Orient seating to catch sunrise: the bright start.",
 "The Herb Rail, Extended": "A full culinary rail: the chef\u2019s balcony.",
 "The Outdoor Living Room": "Full lounge set, rug, lighting, and plants: a second living room under the sky.",
 "Edible Balcony Abundance": "Dwarf fruit, berries, and intensive veg: serious food from small square footage.",
 "The Balcony Greenhouse": "A mini greenhouse or cold frame extends the season by months.",
 "Water Feature, Pint-Sized": "A tabletop fountain brings the sound of water to the smallest space.",
 "The Entertainer\u2019s Balcony": "Seating for six, serving station, and lighting zones: parties, elevated.",
 "Four-Season Balcony": "Evergreens, winter interest, and a heat source: usable 365 days.",
 "The Artist\u2019s Balcony Studio": "An easel, good light, and a view: plein air without leaving home.",
 "Balcony Cinema Nights": "A sheet, a projector, and floor seating: movies under the stars.",
 "The Legacy Balcony Garden": "Perennial plantings and quality pieces that mature beautifully year after year.",
 "Masterclass: Small-Space Design": "Professional small-space principles applied to balconies: sightlines, scale, and restraint."
};

function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  var h=0;for(var i=0;i<safe.length;i++){h=(h*31+safe.charCodeAt(i))>>>0;}
  var steps=['Prepare the space','Gather the essentials','Do the core work','Review the result','Lock in the win'];
  var out='# '+safe+' — working demo\n# Field: '+field+'\n';
  out+='steps = '+JSON.stringify(steps)+'\n';
  out+='for i, s in enumerate(steps, 1):\n    print(f"{i}. {s}")\n';
  out+='print("Seed '+h+': repeat the steps in order and the result compounds.")\n';
  return out;
}

function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||['General Study'];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — balcony design record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). '+ (BLURBS[topic]||('A '+field+' study of "'+topic+'".')) +' Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'sample-demo',language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:GENVER,generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-balcony-makeover',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();