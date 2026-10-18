(function(){'use strict';
/* The The Walking Discovery Database Signature generator — jahdb-db-walking-discovery-signature-sig-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-WALKING-DISCOVERY-SIG-";
var GENVER="jahdb-db-walking-discovery-signature-sig-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The New Block",
  "The Photo Five",
  "The History Hunt",
  "The Tree Census",
  "The Color Walk",
  "The Smell Tour",
  "The Bench Tour",
  "The Night Walk",
  "The Gratitude Walk",
  "The Dog-Spotting Walk",
  "The Architecture Glance",
  "The Silent Walk"
 ],
 "Compounded": [
  "The Themed Expedition",
  "The Foraging Walk",
  "The History Deep Dive",
  "The Photo Essay",
  "The Long Urban Hike",
  "The Dawn Walk",
  "The Market Walk",
  "The Water Walk",
  "The Stair Climb",
  "The Garden Tour",
  "The Music Walk",
  "The Sketch Walk"
 ],
 "Advanced": [
  "The Pilgrimage Walk",
  "The 100-Mile Month",
  "The City Circumnavigation",
  "The Night Expedition",
  "The Walking Interview",
  "The Solo Thru-Walk",
  "The Walking Club",
  "The Legacy Route",
  "Teaching Walking Discovery",
  "Masterclass: The Fl\u00e2neur"
 ]
};
var BLURBS={
 "The New Block": "Walk one block you\u2019ve never walked: the adjacent unknown.",
 "The Photo Five": "Five photos, one theme: the walk as art.",
 "The History Hunt": "Read one plaque: the street\u2019s story, found.",
 "The Tree Census": "Identify five trees: the urban forest, named.",
 "The Color Walk": "Find every color of the rainbow: the playful expedition.",
 "The Smell Tour": "Notice the bakery, the rain, the cut grass: the nose\u2019s walk.",
 "The Bench Tour": "Sit on three new benches: the city\u2019s living room.",
 "The Night Walk": "Your street after dark: the familiar, transformed.",
 "The Gratitude Walk": "Name a good thing per block: the mood, lifted.",
 "The Dog-Spotting Walk": "Count the dogs: the joyful census.",
 "The Architecture Glance": "Look up: the details above the storefronts.",
 "The Silent Walk": "No talking, just noticing: the meditation in motion.",
 "The Themed Expedition": "Murals, doors, gargoyles: the walk with a thesis.",
 "The Foraging Walk": "Edible plants, known safely: the wild pantry.",
 "The History Deep Dive": "Research, then walk the story: the past, present.",
 "The Photo Essay": "A walk that tells a story in twelve frames: the narrative stroll.",
 "The Long Urban Hike": "Ten miles through the city: the metropolis on foot.",
 "The Dawn Walk": "The city waking: the quietest hour, walked.",
 "The Market Walk": "Through markets and stalls: the delicious route.",
 "The Water Walk": "Follow the river or coast: the blue thread.",
 "The Stair Climb": "Find the city\u2019s stairs: the vertical walk.",
 "The Garden Tour": "Public and front gardens: the blooming route.",
 "The Music Walk": "A playlist scored to the streets: the cinematic stroll.",
 "The Sketch Walk": "Draw what you see: the artist\u2019s pace.",
 "The Pilgrimage Walk": "A multi-day walk with meaning: the ancient practice.",
 "The 100-Mile Month": "A hundred miles in thirty days: the walking quest.",
 "The City Circumnavigation": "Walk the city\u2019s edge: the grand loop.",
 "The Night Expedition": "A full moon walk: the wild night, safely.",
 "The Walking Interview": "Walk with an elder, record stories: the moving history.",
 "The Solo Thru-Walk": "Days alone on foot: the thinking pilgrimage.",
 "The Walking Club": "A weekly group walk: the community, in motion.",
 "The Legacy Route": "Walk the route yearly: the tradition on foot.",
 "Teaching Walking Discovery": "Lead others: the guide\u2019s joy.",
 "Masterclass: The Fl\u00e2neur": "The art of the urban wanderer: seeing as practice."
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
    name:topic+' — walking adventure record',
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

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-walking-discovery-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();