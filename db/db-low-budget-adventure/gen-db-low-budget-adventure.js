(function(){'use strict';
/* The The Low-Budget Adventure Database generator — jahdb-db-low-budget-adventure-pub-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-LOW-BUDGET-ADVENTURE-PUB-";
var GENVER="jahdb-db-low-budget-adventure-pub-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The $10 Day",
  "The $20 Date",
  "Lunch Adventure",
  "The Thrift Flip",
  "Park + Food Truck",
  "The Matinee Hack",
  "Bike + Picnic",
  "The Free-Plus-One",
  "Coffee Shop Workation",
  "The Sunset Drive",
  "Library + Lunch",
  "The $5 Challenge"
 ],
 "Compounded": [
  "The $50 Day Trip",
  "The Food Crawl",
  "The $75 Weekend",
  "Camping on $30",
  "The City Pass Day",
  "The $40 Adventure Race",
  "Beach Day, Budgeted",
  "The Antique Hunt",
  "Concert on a Budget",
  "The $60 Couple\u2019s Day",
  "Sports Day Cheap",
  "The Photography Day"
 ],
 "Advanced": [
  "The $100 Weekend",
  "The $200 Mini-Vacation",
  "The Budget Road Trip",
  "The $150 City Break",
  "Adventure Racing, Cheap",
  "The Seasonal Pass Play",
  "The Group Trip Split",
  "The Annual Budget Quest",
  "Teaching Budget Adventure",
  "Masterclass: Joy Per Dollar"
 ]
};
var BLURBS={
 "The $10 Day": "A full fun day on ten dollars: the classic constraint challenge.",
 "The $20 Date": "Romance on twenty: proof that thought beats spending.",
 "Lunch Adventure": "A midday food crawl on pocket change: delicious reconnaissance.",
 "The Thrift Flip": "Ten dollars to find and transform: treasure hunting, budget edition.",
 "Park + Food Truck": "One great food truck meal in a great park: the $15 perfect afternoon.",
 "The Matinee Hack": "Cheap seats, packed snacks: cinema for less.",
 "Bike + Picnic": "Wheels and homemade food: the $5 expedition.",
 "The Free-Plus-One": "A free activity plus one small splurge: the formula.",
 "Coffee Shop Workation": "One good coffee, hours of productive ambiance.",
 "The Sunset Drive": "Gas money and a viewpoint: the cheapest romance.",
 "Library + Lunch": "Morning among books, afternoon picnic: the $8 cultural day.",
 "The $5 Challenge": "What is the best $5 adventure? Competitive frugality.",
 "The $50 Day Trip": "A real getaway on fifty: gas, food, and one attraction.",
 "The Food Crawl": "Five cheap eats, one neighborhood: the delicious tour.",
 "The $75 Weekend": "Two days, seventy-five: the budget weekend blueprint.",
 "Camping on $30": "A night out for thirty: nature\u2019s hotel, economy class.",
 "The City Pass Day": "Bundle deals and free hours: the metropolis, discounted.",
 "The $40 Adventure Race": "Teams, clues, cheap prizes: the amazing race, local.",
 "Beach Day, Budgeted": "Sun, sand, packed cooler: the $25 seaside.",
 "The Antique Hunt": "Small towns, small prices: the treasure road trip.",
 "Concert on a Budget": "Lawn seats and tailgate: live music, affordable.",
 "The $60 Couple\u2019s Day": "A full date day, itemized: romance with receipts.",
 "Sports Day Cheap": "Minor league magic: affordable, fun, close.",
 "The Photography Day": "A tank of gas and a camera: the $30 art expedition.",
 "The $100 Weekend": "Two full days on a hundred: the flagship budget adventure.",
 "The $200 Mini-Vacation": "Three days, two hundred: the long weekend, unlocked.",
 "The Budget Road Trip": "500 miles on a shoestring: the classic American art.",
 "The $150 City Break": "A new city in 48 hours, budgeted to the dollar.",
 "Adventure Racing, Cheap": "Enter the local race: the finish line feeling, affordable.",
 "The Seasonal Pass Play": "One pass, a season of adventures: the math that wins.",
 "The Group Trip Split": "Costs divided, fun multiplied: the economics of together.",
 "The Annual Budget Quest": "One big yearly adventure, saved for monthly: the goal that organizes spending.",
 "Teaching Budget Adventure": "Show others the low-cost life: the generous skill.",
 "Masterclass: Joy Per Dollar": "The economics of happiness: maximizing memories per dollar."
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
    name:topic+' — budget adventure record',
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

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-low-budget-adventure',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();