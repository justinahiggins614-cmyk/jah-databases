(function(){'use strict';
/* The The Dream Bedroom Studio Signature generator — jahdb-gen-dream-bedroom-studio-signature-sig-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-DREAM-BEDROOM-STUDIO-SIG-";
var GENVER="jahdb-gen-dream-bedroom-studio-signature-sig-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "Calm Minimal: The Quiet Room",
  "Warm Cozy: The Nest",
  "Tiny Room, Big Calm",
  "The $100 Refresh",
  "Dark and Moody Sleep Cave",
  "Bright Morning Person Room",
  "The Renter-Friendly Makeover",
  "Shared Room Harmony",
  "First Apartment Bedroom",
  "The Guest Room Glow-Up",
  "Kids\u2019 Cozy Corner",
  "Teen Retreat Studio"
 ],
 "Compounded": [
  "Bold Modern: The Statement Room",
  "Forest Retreat Bedroom",
  "The Reader\u2019s Bedroom",
  "Gamer Loft Bedroom",
  "Artist Studio Bedroom",
  "The Vintage Collector Room",
  "Japandi Calm Bedroom",
  "Boho Layered Bedroom",
  "The Plant Parent Bedroom",
  "Work-From-Bedroom Zones",
  "The Cozy Reading Loft",
  "The Minimalist\u2019s Capsule Room"
 ],
 "Advanced": [
  "The Suite: Hotel at Home",
  "Acoustic Sleep Sanctuary",
  "The Collector\u2019s Gallery Bedroom",
  "Smart Bedroom Automation",
  "The Forever Bedroom",
  "Bedroom Plus Dressing Room",
  "The Writer\u2019s Garret",
  "Masterclass: Light Like a Designer",
  "The Sensory Sleep Lab",
  "Legacy: The Room That Grows Up"
 ]
};
var BLURBS={
 "Calm Minimal: The Quiet Room": "A serene, clutter-free bedroom in soft neutrals. Fewer things, better sleep, calmer mornings.",
 "Warm Cozy: The Nest": "Layered textiles and warm light turn any bedroom into a nest you never want to leave.",
 "Tiny Room, Big Calm": "Dorm-sized bedroom, full-sized comfort: vertical storage and a strict color diet.",
 "The $100 Refresh": "No renovation, no new furniture: textiles, light, and layout tricks that transform a room for a hundred dollars.",
 "Dark and Moody Sleep Cave": "Deep colors, blackout curtains, zero glow. Built for people who sleep best in total dark.",
 "Bright Morning Person Room": "Light colors, sheer curtains, sunrise-friendly layout. Wake up with the sun, on purpose.",
 "The Renter-Friendly Makeover": "Zero holes, zero paint: removable everything that still looks intentional and chic.",
 "Shared Room Harmony": "Two sleepers, one room, no friction: zones, sound, and light discipline.",
 "First Apartment Bedroom": "Starting from an empty room: the buy-in-order list that gets you sleeping well on night one.",
 "The Guest Room Glow-Up": "A guest bedroom that feels like a boutique hotel: crisp, warm, and thoughtfully stocked.",
 "Kids\u2019 Cozy Corner": "A child\u2019s bedroom that invites sleep and morning play alike, with storage they can actually use.",
 "Teen Retreat Studio": "A teenager\u2019s room that respects their taste and your budget, with study space that gets used.",
 "Bold Modern: The Statement Room": "One dramatic color, clean lines, gallery attitude. For people whose bedroom should have opinions.",
 "Forest Retreat Bedroom": "Greens, woods, and leafy textures bring the outdoors in. Sleep like you are camping, minus the bugs.",
 "The Reader\u2019s Bedroom": "A proper reading chair, perfect lamp, and books within arm\u2019s reach of the pillow.",
 "Gamer Loft Bedroom": "Sleep space by night, battlestation by day: lighting scenes that switch the room\u2019s whole job.",
 "Artist Studio Bedroom": "A bedroom with a real creative corner: daylight lamp, washable surfaces, inspiration wall.",
 "The Vintage Collector Room": "Thrifted finds with a unified palette look curated, not cluttered. Patina is a design choice.",
 "Japandi Calm Bedroom": "Japanese minimalism meets Scandinavian warmth: low, natural, profoundly restful.",
 "Boho Layered Bedroom": "Pattern on pattern, done right: the secret is one shared undertone across every textile.",
 "The Plant Parent Bedroom": "Twenty plants, zero chaos: how to jungle a bedroom while keeping it sleepable.",
 "Work-From-Bedroom Zones": "A real office corner inside the bedroom that disappears after hours. Boundaries you can see.",
 "The Cozy Reading Loft": "A lofted corner for books and blankets: vertical comfort.",
 "The Minimalist\u2019s Capsule Room": "Twelve items, total calm: the edited bedroom.",
 "The Suite: Hotel at Home": "Turn the primary bedroom into a suite: sitting corner, layered lighting, linens worth the hype.",
 "Acoustic Sleep Sanctuary": "Sound-treated, blackout, temperature-tuned: the bedroom engineered for the deepest sleep of your life.",
 "The Collector\u2019s Gallery Bedroom": "Display a real collection - vinyl, art, sneakers - as the room\u2019s designed centerpiece.",
 "Smart Bedroom Automation": "Lights, blinds, and white noise on schedule. The room prepares itself for sleep and waking.",
 "The Forever Bedroom": "A timeless design built to last fifteen years: quality bones, swappable textiles, zero trends.",
 "Bedroom Plus Dressing Room": "Carve a dressing zone from a large bedroom: open wardrobe, full mirror, boutique energy.",
 "The Writer\u2019s Garret": "A bedroom built around a writing desk with a view: romantic, focused, and a little dramatic.",
 "Masterclass: Light Like a Designer": "The full lighting-layer method professionals use, adapted for real bedrooms and real budgets.",
 "The Sensory Sleep Lab": "Every sense tuned for rest: scent, sound, touch, temperature, and light in one protocol.",
 "Legacy: The Room That Grows Up": "A bedroom designed to evolve from teen to adult to guest room with only textile swaps."
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
    name:topic+' — bedroom design record',
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

var BUILD_ROOM_THEME=(function(){
var PALETTES={calm:[['#2b3a55','deep slate'],['#7fa6a3','sea mist'],['#e8e0d0','warm linen']],warm:[['#5b3a29','cocoa'],['#c98a5e','terracotta'],['#f2e3c6','sand']],bold:[['#1d1d2f','midnight'],['#e63946','signal red'],['#f1fa8c','neon lime']],forest:[['#22331f','pine'],['#5c7a4d','moss'],['#d9c9a3','straw']]};
var LAYOUTS=['Bed against the longest wall, desk by the window for daylight.','Bed in the corner nook, open floor kept clear for movement.','Bed centered as the anchor, zones split by a rug, not walls.'];
var LIGHT=['Warm 2700K bedside lamp for wind-down.','String lights along the headboard for soft glow.','One bright daylight bulb at the desk for focus work.'];
return function(inp){
  var r=prng(inp.seed||7);
  var pal=pick(Object.keys(PALETTES),r);
  var cols=PALETTES[pal];
  var budget=parseInt(inp.budget,10)||300;
  var parts=[['Bedding + textiles',0.35],['Lighting',0.2],['Wall decor + art',0.2],['Storage + organizers',0.15],['Plants + finishing',0.1]];
  var sections=[
    {h:'Palette — '+pal+' theme',items:cols.map(function(c){return c[1]+' ('+c[0]+')';})},
    {h:'Layout for a '+inp.size+' room',text:pick(LAYOUTS,r)+' Keep walkways at least 60cm wide so the room breathes.'},
    {h:'Lighting plan',items:shuffle(LIGHT,r).slice(0,2)},
    {h:'Budget split — $'+budget,items:parts.map(function(p){return p[0]+': $'+Math.round(budget*p[1]);})},
    {h:'First three buys',items:['A textile that sets the mood (throw, rug, or curtains).','The one light you will use every night.','Storage that hides the mess you actually make.']}
  ];
  return {title:'Dream bedroom studio: '+inp.style+' theme',intro:'A complete '+inp.style+' bedroom plan for a '+inp.size+' space on about $'+budget+'.',sections:sections};
};})();

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
gen.builderId="room-theme";
gen.builderFields=[["size", "Room size", "select", ["tiny (dorm)", "small", "medium", "large"]], ["budget", "Budget ($)", "number", "300"], ["style", "Style", "select", ["calm minimal", "warm cozy", "bold modern", "forest retreat"]], ["seed", "Seed (optional)", "number", "7"]];
gen.build=BUILD_ROOM_THEME;

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-dream-bedroom-studio-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();