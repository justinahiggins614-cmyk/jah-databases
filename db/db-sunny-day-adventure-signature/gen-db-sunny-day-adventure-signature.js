(function(){'use strict';
/* The The Sunny Day Adventure Database Signature generator — jahdb-db-sunny-day-adventure-signature-sig-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-SUNNY-DAY-ADVENTURE-SIG-";
var GENVER="jahdb-db-sunny-day-adventure-signature-sig-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The Golden Hour Walk",
  "Park Picnic Basics",
  "The Splash Pad Hit",
  "Bike the Greenway",
  "Sidewalk Cafe Morning",
  "The Kite Afternoon",
  "Outdoor Reading Hour",
  "The Sprinkler Run",
  "Sunset Watch Party",
  "The Garden Wander",
  "Frisbee Golf, DIY",
  "The Lemonade Stand"
 ],
 "Compounded": [
  "The Day Hike",
  "Beach Day Done Right",
  "The River Float",
  "Outdoor Climbing Intro",
  "The Cycling Tour",
  "Paddleboard Morning",
  "The Wildlife Safari",
  "Farmers Market + Park",
  "The Outdoor Festival",
  "Geocaching Adventure",
  "The Sunset Sail",
  "Stargazing Prep Night"
 ],
 "Advanced": [
  "The Summit Sunrise",
  "The Coastal Expedition",
  "The Multi-Sport Day",
  "The Wilderness Day Trip",
  "The Island Day",
  "The Photography Expedition",
  "The Outdoor Feast",
  "The Charity Ride/Walk",
  "Legacy: The Annual Sun Day",
  "Masterclass: Reading the Sky"
 ]
};
var BLURBS={
 "The Golden Hour Walk": "An evening stroll as the light turns gold. The day\u2019s free finale.",
 "Park Picnic Basics": "Blanket, snacks, frisbee: the timeless formula.",
 "The Splash Pad Hit": "Water, kids, joy: summer\u2019s simplest perfect afternoon.",
 "Bike the Greenway": "An easy ride on a safe path: wind, views, freedom.",
 "Sidewalk Cafe Morning": "Coffee outside, world watching: the slow luxury.",
 "The Kite Afternoon": "Wind + kite + open field = timeless physics fun.",
 "Outdoor Reading Hour": "A book, a bench, a breeze: the perfect chapter.",
 "The Sprinkler Run": "Kids, hose, squeals: the backyard water park.",
 "Sunset Watch Party": "Find the view, bring snacks, watch the show. Nightly and free.",
 "The Garden Wander": "Botanical garden or park blooms: beauty, curated.",
 "Frisbee Golf, DIY": "Targets around the park: instant sport, zero cost.",
 "The Lemonade Stand": "Classic entrepreneurship: kids learn business, neighbors get lemonade.",
 "The Day Hike": "Trail, summit, lunch with a view: the full outdoor meal.",
 "Beach Day Done Right": "Shade, cooler, games, and the golden-hour swim: the complete beach.",
 "The River Float": "Tubes, current, sunshine: the laziest adventure.",
 "Outdoor Climbing Intro": "A guided first climb: vertical sunny thrill.",
 "The Cycling Tour": "A 30-mile loop with food stops: the day as journey.",
 "Paddleboard Morning": "Glass water, core workout, total calm.",
 "The Wildlife Safari": "Binoculars and patience: the park\u2019s secret residents.",
 "Farmers Market + Park": "Morning market, afternoon park feast: the delicious day.",
 "The Outdoor Festival": "Music, food, crowds: summer\u2019s big communal joy.",
 "Geocaching Adventure": "Treasure hunts with GPS: the world as game board.",
 "The Sunset Sail": "An evening on the water: wind, waves, and gold light.",
 "Stargazing Prep Night": "Dark-sky spot, blankets, constellations: the day that becomes night.",
 "The Summit Sunrise": "A dawn summit: the most earned view there is.",
 "The Coastal Expedition": "Cliffs, tide pools, and hidden coves: a full coastal day.",
 "The Multi-Sport Day": "Hike, swim, bike: the triathlon of fun.",
 "The Wilderness Day Trip": "Deep trail, real remoteness, total reset.",
 "The Island Day": "Ferry out, explore, ferry back: the mini-vacation.",
 "The Photography Expedition": "Chase light all day: golden hour to blue hour, camera ready.",
 "The Outdoor Feast": "A full meal cooked and eaten outside: fire, food, friends.",
 "The Charity Ride/Walk": "Miles for a cause: sweat with purpose.",
 "Legacy: The Annual Sun Day": "One perfect sunny day, repeated yearly: the tradition of light.",
 "Masterclass: Reading the Sky": "Clouds, wind, and light: the adventurer\u2019s weather literacy."
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
    name:topic+' — sunny day activity record',
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

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-sunny-day-adventure-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();