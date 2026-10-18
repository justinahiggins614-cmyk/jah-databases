(function(){'use strict';
/* The The One-Hour Project Database generator — jahdb-db-one-hour-project-pub-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-ONE-HOUR-PROJECT-PUB-";
var GENVER="jahdb-db-one-hour-project-pub-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The Spice Rack Reset",
  "Photo Wall, Instant",
  "The Drawer Dividers",
  "Herb Pot Trio",
  "The 60-Minute Declutter",
  "Candle Making, Simple",
  "The Bookend Build",
  "Bathroom Refresh",
  "The Noticeboard",
  "Pillow Cover Swap",
  "The Key Hook Rail",
  "Pantry Labels"
 ],
 "Compounded": [
  "The Floating Shelf",
  "Paint One Wall",
  "The Terrarium",
  "Bread, No-Knead",
  "The Gallery Ledge",
  "Curtain Hemming",
  "The Boot Tray",
  "Chalkboard Wall, Small",
  "The Plant Propagation Station",
  "Furniture Touch-Up",
  "The Memory Jar",
  "Cable Box Build"
 ],
 "Advanced": [
  "The Hour-Long Mural",
  "Build a Stool",
  "The Capsule Wardrobe Edit",
  "The 60-Minute Website",
  "Preserve the Harvest",
  "The Furniture Flip",
  "The Emergency Kit",
  "The One-Hour Legacy Letter",
  "The Annual Hour",
  "Masterclass: The Finished Mindset"
 ]
};
var BLURBS={
 "The Spice Rack Reset": "Empty, wipe, label, refill: a kitchen upgrade in an hour.",
 "Photo Wall, Instant": "Print, tape, arrange: a gallery wall before lunch.",
 "The Drawer Dividers": "Cardboard and craft: custom organizers, zero cost.",
 "Herb Pot Trio": "Plant three herbs: the kitchen garden begins.",
 "The 60-Minute Declutter": "One zone, one hour, dramatic before-and-after.",
 "Candle Making, Simple": "Melt, scent, pour: homemade ambiance.",
 "The Bookend Build": "Two boards, some paint: a shelf upgrade.",
 "Bathroom Refresh": "Deep clean, new hand towel, one plant: spa in sixty.",
 "The Noticeboard": "Cork, frame, pins: command center, crafted.",
 "Pillow Cover Swap": "Sew or no-sew covers: the sofa\u2019s new outfit.",
 "The Key Hook Rail": "Mount a rail by the door: never lose keys again.",
 "Pantry Labels": "Label everything: the five-minute-cooking kitchen.",
 "The Floating Shelf": "Mount one shelf, style it well: instant architecture.",
 "Paint One Wall": "An accent wall in an hour (small room): the bold move.",
 "The Terrarium": "Glass, soil, plants: a world in a jar.",
 "Bread, No-Knead": "Mix, wait, bake: the hour (plus rising) miracle loaf.",
 "The Gallery Ledge": "A picture ledge styled and hung: art, flexible.",
 "Curtain Hemming": "Hem to puddle or sill: windows, tailored.",
 "The Boot Tray": "A tray, some stones: the mudroom solution.",
 "Chalkboard Wall, Small": "A framed chalkboard: menus, notes, art.",
 "The Plant Propagation Station": "Cuttings in jars on a sunny sill: free plants forever.",
 "Furniture Touch-Up": "Scratch markers and polish: the facelift.",
 "The Memory Jar": "Decorate a jar, fill with notes: the year\u2019s treasure.",
 "Cable Box Build": "Hide the router tangle: a box, a drill, peace.",
 "The Hour-Long Mural": "One wall, one design, sixty bold minutes: the statement.",
 "Build a Stool": "Simple joinery, real furniture: the maker milestone.",
 "The Capsule Wardrobe Edit": "A full closet curation in an hour: the ruthless, wonderful purge.",
 "The 60-Minute Website": "A personal page, live: the digital hour project.",
 "Preserve the Harvest": "Jam or pickles in an hour: summer, jarred.",
 "The Furniture Flip": "Sand, paint, stage: the thrift-to-treasure hour.",
 "The Emergency Kit": "Assemble the real one: prepared in sixty.",
 "The One-Hour Legacy Letter": "Write the letter that matters: the hour\u2019s deepest project.",
 "The Annual Hour": "One hour yearly on the same project: compound creation.",
 "Masterclass: The Finished Mindset": "Why finishers win: the psychology of done."
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
    name:topic+' — one-hour project record',
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

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-one-hour-project',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();