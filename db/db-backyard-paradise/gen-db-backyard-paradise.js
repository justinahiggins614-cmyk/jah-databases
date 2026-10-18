(function(){'use strict';
/* The The Backyard Paradise Database generator — jahdb-db-backyard-paradise-pub-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-BACKYARD-PARADISE-PUB-";
var GENVER="jahdb-db-backyard-paradise-pub-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The Sun Map Weekend",
  "First Veggie Bed",
  "The $200 Patio Refresh",
  "Lawn to Meadow Patch",
  "Container Garden Starter",
  "The Fire Pit Corner",
  "Shade Sail Solution",
  "Pathway Rescue",
  "The Herb Spiral",
  "Bird and Pollinator Welcome",
  "Kids\u2019 Dig Patch",
  "The Hammock Spot"
 ],
 "Compounded": [
  "The Outdoor Kitchen Corner",
  "Rain Garden Magic",
  "The Play Zone",
  "Orchard Dreams: Five Fruit Trees",
  "The Evening Garden",
  "Deck Revival Project",
  "The Secret Garden Corner",
  "Chicken Coop Corner",
  "The Pond, Small and Alive",
  "Sports Court Strip",
  "The Herb Garden Wall",
  "The Wildlife Corridor"
 ],
 "Advanced": [
  "The Full Landscape Plan",
  "Outdoor Room with Roof",
  "The Food Forest",
  "Pool Surround Paradise",
  "The Night Garden Gala",
  "Orchard and Apiary Pairing",
  "The Grand Gathering Lawn",
  "Four-Season Interest Design",
  "The Legacy Garden",
  "Paradise on Autopilot"
 ]
};
var BLURBS={
 "The Sun Map Weekend": "Spend one weekend mapping sun and shade. Every future planting decision gets easier forever.",
 "First Veggie Bed": "One 4x8 raised bed, six easy crops. Fresh food steps from the door by midsummer.",
 "The $200 Patio Refresh": "Sweep, stain, string lights, and two chairs: a patio reborn for the price of dinner out.",
 "Lawn to Meadow Patch": "Replace a thirsty lawn square with native meadow. Less mowing, more butterflies.",
 "Container Garden Starter": "No beds? No problem. Pots on a sunny patio grow a shocking amount of food and flowers.",
 "The Fire Pit Corner": "A simple, safe fire circle with seating: the fastest way to make a yard feel like a destination.",
 "Shade Sail Solution": "One sail, four posts, instant cool. The cheapest real shade structure you can build.",
 "Pathway Rescue": "Define the walk from door to gate with stone, mulch, or pavers. Order appears immediately.",
 "The Herb Spiral": "A beautiful, space-efficient herb garden in a spiral of stone. Cook with fresh herbs daily.",
 "Bird and Pollinator Welcome": "Feeders, water, and native flowers turn any yard into a wildlife show.",
 "Kids\u2019 Dig Patch": "One corner where kids can dig freely. Childhood, contained and joyful.",
 "The Hammock Spot": "Two trees or two posts, one hammock: the highest relaxation-per-dollar in yard history.",
 "The Outdoor Kitchen Corner": "Grill station, prep counter, and seating: summer cooking moves outside where it belongs.",
 "Rain Garden Magic": "A shallow planted basin that drinks stormwater. Solves puddles and looks gorgeous doing it.",
 "The Play Zone": "Swings, sandbox, and climbing in one safe, visible zone. Kids outside, parents relaxed.",
 "Orchard Dreams: Five Fruit Trees": "Five well-chosen trees, years of fruit. The slowest, sweetest investment.",
 "The Evening Garden": "White flowers, fragrant blooms, and lighting for nights. The yard has a second shift.",
 "Deck Revival Project": "Clean, repair, stain, and furnish: a tired deck becomes the favorite room of the house.",
 "The Secret Garden Corner": "A hidden bench behind plantings. Every paradise needs one secret.",
 "Chicken Coop Corner": "Fresh eggs and endless entertainment: a small flock fits more yards than you think.",
 "The Pond, Small and Alive": "A half-barrel pond with a lily and a solar fountain. Water changes everything.",
 "Sports Court Strip": "A flat patch for hoops, badminton, or bocce. Active yards get used daily.",
 "The Herb Garden Wall": "Vertical herbs by the kitchen door: the cook\u2019s garden.",
 "The Wildlife Corridor": "Native plantings that invite birds and bees: the living fence.",
 "The Full Landscape Plan": "A professional-style master plan: zones, plant lists, phases, and budgets for the whole property.",
 "Outdoor Room with Roof": "A pergola or pavilion with curtains and heat: three-season living space.",
 "The Food Forest": "Layered edible landscaping: canopy, shrubs, herbs, groundcover. A grocery store that grows.",
 "Pool Surround Paradise": "Landscaping, shade, and seating that turn a pool into a resort.",
 "The Night Garden Gala": "Landscape lighting design: uplights, path lights, and moonlighting for after-dark magic.",
 "Orchard and Apiary Pairing": "Fruit trees plus two beehives: pollination and honey in one sweet system.",
 "The Grand Gathering Lawn": "Leveled, drained, and edged: a lawn built for weddings, games, and bare feet.",
 "Four-Season Interest Design": "Something beautiful every month: bark, berries, evergreens, and early bulbs.",
 "The Legacy Garden": "A garden planned for decades: specimen trees, stone paths, and a bench with your name on it.",
 "Paradise on Autopilot": "Irrigation, mulch, and plant choices that make the paradise nearly self-running."
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
    name:topic+' — backyard design record',
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

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-backyard-paradise',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();