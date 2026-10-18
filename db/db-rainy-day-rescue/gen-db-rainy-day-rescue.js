(function(){'use strict';
/* The The Rainy Day Rescue Database generator — jahdb-db-rainy-day-rescue-pub-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-RAINY-DAY-RESCUE-PUB-";
var GENVER="jahdb-db-rainy-day-rescue-pub-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "Blanket Fort Cinema",
  "Baking Rescue",
  "Puzzle Marathon",
  "Indoor Scavenger Hunt",
  "Art Attack Afternoon",
  "Board Game Tournament",
  "Story Chain Writing",
  "Indoor Picnic",
  "Spa Day at Home",
  "The Great Sort",
  "Karaoke Rain Party",
  "Letter Writing Hour"
 ],
 "Compounded": [
  "The Science Lab Day",
  "Cook-Off Challenge",
  "Indoor Camping",
  "The Craft Fair Prep",
  "Movie Marathon, Themed",
  "The Escape Room, DIY",
  "Learn-a-Skill Day",
  "The Photo Project",
  "Indoor Garden Planting",
  "The Music Session",
  "Furniture Rearrange",
  "The Book Sprint"
 ],
 "Advanced": [
  "The Rainy Weekend Project",
  "The Film Festival",
  "The Cookbook Weekend",
  "The Home Museum",
  "The Game Design Lab",
  "The Deep Clean Delight",
  "The Talent Show",
  "The Time Capsule",
  "Legacy: The Rainy Day Box",
  "Masterclass: Designing Cozy"
 ]
};
var BLURBS={
 "Blanket Fort Cinema": "Build the fort, pick the film, pop the corn. The classic never fails.",
 "Baking Rescue": "Cookies or bread: the house smells amazing and time flies deliciously.",
 "Puzzle Marathon": "A 1000-piece puzzle and a whole rainy afternoon. Meditative teamwork.",
 "Indoor Scavenger Hunt": "A list, a timer, hidden clues: the house becomes an adventure.",
 "Art Attack Afternoon": "Paper, paints, total freedom: make a mess, make a masterpiece.",
 "Board Game Tournament": "Bracket, snacks, glory: settle who is truly the champion.",
 "Story Chain Writing": "Each person adds a paragraph: the silliest story ever, collaboratively.",
 "Indoor Picnic": "Blanket on the living room floor: the picnic, minus the mud.",
 "Spa Day at Home": "Face masks, foot soaks, calm music: the rain as ambiance.",
 "The Great Sort": "Tackle one messy zone together: productive AND satisfying.",
 "Karaoke Rain Party": "Hairbrush microphones, full commitment. The neighbors will understand.",
 "Letter Writing Hour": "Real letters to real people: slow, thoughtful, delightful.",
 "The Science Lab Day": "Kitchen experiments: volcanoes, slime, rockets (safe ones). Learning, fizzing.",
 "Cook-Off Challenge": "Same ingredients, competing dishes, family judges. May the best chef win.",
 "Indoor Camping": "Tent in the living room, flashlights, s\u2019mores from the oven. Wilderness, dry.",
 "The Craft Fair Prep": "Make things to gift or sell: rainy days become productive studios.",
 "Movie Marathon, Themed": "A trilogy, matching snacks, intermission stretches: cinema at home.",
 "The Escape Room, DIY": "Design puzzles for each other: the house as mystery.",
 "Learn-a-Skill Day": "Origami, juggling, magic tricks: emerge with a party trick.",
 "The Photo Project": "Sort, print, and frame the backlog: memories, curated.",
 "Indoor Garden Planting": "Start seeds and repot plants: green therapy while it pours.",
 "The Music Session": "Instruments out, jam or learn: rainy days have rhythm.",
 "Furniture Rearrange": "A free room makeover: the space feels brand new.",
 "The Book Sprint": "Everyone reads, then shares: a silent party of stories.",
 "The Rainy Weekend Project": "A two-day build: furniture, mural, or garden beds between showers.",
 "The Film Festival": "Make short films all weekend: write, shoot, premiere. Hollywood, homemade.",
 "The Cookbook Weekend": "Cook through a whole chapter: skills and feasts, compounded.",
 "The Home Museum": "Curate family artifacts with labels and stories: your own exhibition.",
 "The Game Design Lab": "Invent a board game, playtest, refine: designers are made on rainy days.",
 "The Deep Clean Delight": "A systematic whole-home reset: strangely euphoric.",
 "The Talent Show": "Rehearse all day, perform at night: the household\u2019s big stage.",
 "The Time Capsule": "Pack today\u2019s treasures for a future rainy day: a gift to yourselves.",
 "Legacy: The Rainy Day Box": "A curated kit - games, crafts, recipes - ready for every future storm.",
 "Masterclass: Designing Cozy": "The architecture of indoor joy: light, texture, and ritual."
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
    name:topic+' — rainy day activity record',
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

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-rainy-day-rescue',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();