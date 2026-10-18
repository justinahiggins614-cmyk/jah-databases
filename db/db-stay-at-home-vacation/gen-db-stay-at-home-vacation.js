(function(){'use strict';
/* The The Stay-at-Home Vacation Database generator — jahdb-db-stay-at-home-vacation-pub-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-STAY-AT-HOME-VACATION-PUB-";
var GENVER="jahdb-db-stay-at-home-vacation-pub-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "Paris Evening",
  "Tokyo Night",
  "Italian Sunday",
  "Beach Day Indoors",
  "Mexican Fiesta Night",
  "English Tea Time",
  "Greek Island Evening",
  "Movie Location Night",
  "Camping Indoors",
  "Spa Retreat Day",
  "New Orleans Jazz Night",
  "Swiss Chalet Evening"
 ],
 "Compounded": [
  "Japan Week",
  "Mediterranean Escape",
  "The Road Trip, Stationary",
  "Moroccan Nights",
  "Scandinavian Hygge Week",
  "New York Food Tour",
  "Hawaiian Luau Weekend",
  "The Safari Staycation",
  "French Countryside Days",
  "The Cruise, Docked",
  "Indian Festival of Flavor",
  "The Alpine Ski Lodge"
 ],
 "Advanced": [
  "Around the World in 7 Days",
  "The Honeymoon at Home",
  "The Cultural Deep Dive",
  "The Family Heritage Trip",
  "The Wellness Resort Week",
  "The Literary Tour",
  "The Music Pilgrimage",
  "The History Immersion",
  "Legacy: The Annual Staycation",
  "Masterclass: Cultural Appreciation"
 ]
};
var BLURBS={
 "Paris Evening": "Baguette, cheese, a French film, Edith Piaf: the City of Light, living room edition.",
 "Tokyo Night": "Sushi kits, neon vibes, anime marathon: electric Tokyo at home.",
 "Italian Sunday": "Pasta from scratch, red wine, loud conversation: la dolce vita.",
 "Beach Day Indoors": "Tropical drinks, beach sounds, swimsuit optional: the coast comes to you.",
 "Mexican Fiesta Night": "Tacos, mariachi, papel picado: fiesta energy, zero travel.",
 "English Tea Time": "Proper tea, scones, cucumber sandwiches: civilized and cozy.",
 "Greek Island Evening": "Grilled fare, bouzouki music, blue-and-white everything: the Aegean at home.",
 "Movie Location Night": "Watch a film, then cook its cuisine: double-feature travel.",
 "Camping Indoors": "Tent, sleeping bags, campfire snacks: wilderness, weatherproof.",
 "Spa Retreat Day": "Robes, masks, cucumber water: the resort, minus the bill.",
 "New Orleans Jazz Night": "Gumbo, jazz playlist, second-line parade in the hallway: laissez les bons temps rouler.",
 "Swiss Chalet Evening": "Fondue, snow films, chunky knits: alpine cozy.",
 "Japan Week": "Seven days: sushi-making, origami, garden contemplation, Studio Ghibli. Deep dive.",
 "Mediterranean Escape": "Three days of coastal food, slow lunches, and siesta culture.",
 "The Road Trip, Stationary": "Route 66 in the driveway: diner food, road movies, car camping in the garage.",
 "Moroccan Nights": "Tagine, mint tea, lanterns, low seating: the souk at home.",
 "Scandinavian Hygge Week": "Candles, baking, wool socks, slow living: the art of cozy, studied.",
 "New York Food Tour": "A borough a day: pizza, bagels, dumplings, cheesecake. The city that never sleeps, on plates.",
 "Hawaiian Luau Weekend": "Poke, ukulele, flower leis: aloha spirit, mainland edition.",
 "The Safari Staycation": "Nature documentaries, binocular birding, campfire stories: the wild, channeled.",
 "French Countryside Days": "Rustic bread, market cheese, long walks: la vie simple.",
 "The Cruise, Docked": "Formal night, buffet lunches, deck games on the patio: all aboard (the house).",
 "Indian Festival of Flavor": "Curries, colors, music: a sensory celebration.",
 "The Alpine Ski Lodge": "Fondue, hot chocolate, fireplace films: winter sports, spectator edition.",
 "Around the World in 7 Days": "A different country daily: the ultimate staycation marathon.",
 "The Honeymoon at Home": "Romance, fine dining, no phones: the trip of a lifetime, address unchanged.",
 "The Cultural Deep Dive": "One culture, one month: language, food, film, history. Travel as education.",
 "The Family Heritage Trip": "Cook ancestors\u2019 food, tell their stories, visit virtually: roots, honored.",
 "The Wellness Resort Week": "Yoga, smoothies, meditation, early beds: the retreat, at home.",
 "The Literary Tour": "Visit (virtually) the settings of beloved books, then feast on their food.",
 "The Music Pilgrimage": "A genre\u2019s homeland explored through sound, food, and film: Nashville, Havana, Lagos.",
 "The History Immersion": "One era, fully inhabited: costumes, food, music, and manners. Time travel, themed.",
 "Legacy: The Annual Staycation": "One themed week yearly: the family tradition of armchair travel.",
 "Masterclass: Cultural Appreciation": "Celebrating cultures deeply and respectfully: research, care, and joy."
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
    name:topic+' — staycation plan record',
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

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-stay-at-home-vacation',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();