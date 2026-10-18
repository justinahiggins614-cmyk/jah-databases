(function(){'use strict';
/* The The Digital Detox Adventure Signature generator — jahdb-db-digital-detox-adventure-signature-sig-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-DIGITAL-DETOX-ADVENTURE-SIG-";
var GENVER="jahdb-db-digital-detox-adventure-signature-sig-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The One-Hour Unplug",
  "Screen-Free Morning",
  "The Analog Evening",
  "Walk Without Podcasts",
  "Handwrite Letters",
  "The Cook-From-Memory Meal",
  "Puzzle Afternoon",
  "People-Watch at a Cafe",
  "The Sketch Walk",
  "Board Game Night",
  "Garden Hour",
  "The Library Trip"
 ],
 "Compounded": [
  "The 24-Hour Detox",
  "The Weekend Unplugged",
  "The Cabin Day",
  "Social Detox Party",
  "The Maker Weekend",
  "Analog Photography Day",
  "The Reading Marathon",
  "Volunteer Offline Day",
  "The Conversation Dinner",
  "Nature Immersion Day",
  "The Skill-Building Detox",
  "Hometown Exploration"
 ],
 "Advanced": [
  "The 7-Day Digital Detox",
  "The Detox Retreat",
  "The 30-Day Rebalance",
  "Family Detox Covenant",
  "The Attention Restoration Trip",
  "The Creative Residency",
  "The Relationship Reset",
  "The Annual Unplug",
  "Teaching Detox to Kids",
  "Masterclass: Attention Economics"
 ]
};
var BLURBS={
 "The One-Hour Unplug": "Phone in a drawer for one hour with a book ready. The gateway detox.",
 "Screen-Free Morning": "No phone until after breakfast. Mornings belong to you again.",
 "The Analog Evening": "Books, board games, conversation: an evening from 1995, on purpose.",
 "Walk Without Podcasts": "Just walk and think. The mind wanders to interesting places.",
 "Handwrite Letters": "Pen, paper, stamps: slow communication with real weight.",
 "The Cook-From-Memory Meal": "No recipe videos: cook what you know by heart. Taste and instinct lead.",
 "Puzzle Afternoon": "Jigsaw, crossword, or Sudoku: analog problem-solving joy.",
 "People-Watch at a Cafe": "No scrolling, just watching the world. Strangely fascinating.",
 "The Sketch Walk": "Bring a sketchbook, draw what you see. Bad drawings welcome.",
 "Board Game Night": "Dust off the box: laughter without a single notification.",
 "Garden Hour": "Hands in dirt, phone inside. The original mindfulness app.",
 "The Library Trip": "Browse spines, judge covers, leave with an armful. Free and glorious.",
 "The 24-Hour Detox": "A full day offline: the classic reset. Plan it like a mini-vacation.",
 "The Weekend Unplugged": "Friday night to Sunday night: two days of analog living.",
 "The Cabin Day": "Drive somewhere with no signal. Nature enforces the detox.",
 "Social Detox Party": "Friends all park phones at the door. Conversation, remembered.",
 "The Maker Weekend": "Build, sew, or craft all weekend: hands busy, mind quiet.",
 "Analog Photography Day": "Film camera, 36 shots, no previews. Deliberate seeing.",
 "The Reading Marathon": "One book, one day, no interruptions. Remember deep reading?",
 "Volunteer Offline Day": "Serve somewhere phones stay pocketed. Presence as service.",
 "The Conversation Dinner": "A long dinner with one rule: no devices at the table.",
 "Nature Immersion Day": "Trail, water, sky: a full day outside with the phone left behind.",
 "The Skill-Building Detox": "Learn juggling, knots, or whistling: silly skills need zero screens.",
 "Hometown Exploration": "Be a tourist with a paper map. Discovery, unplugged.",
 "The 7-Day Digital Detox": "A full week with a dumbphone: the deep reset. Planned carefully, transformative.",
 "The Detox Retreat": "A weekend retreat - solo or guided - built around disconnection.",
 "The 30-Day Rebalance": "A month of new tech rules: the permanent upgrade, not a stunt.",
 "Family Detox Covenant": "The whole household agrees to new norms: shared rules, shared freedom.",
 "The Attention Restoration Trip": "A week in nature with minimal tech: science-backed attention recovery.",
 "The Creative Residency": "A week offline devoted to one creative project. Output, uninterrupted.",
 "The Relationship Reset": "Couples or friends detox together: presence as the ultimate gift.",
 "The Annual Unplug": "One week a year, fully offline: the tradition that keeps tech in its place.",
 "Teaching Detox to Kids": "Help children build healthy tech relationships early: modeling over monitoring.",
 "Masterclass: Attention Economics": "How platforms harvest attention - and how to take it back for good."
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
    name:topic+' — digital detox record',
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

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-digital-detox-adventure-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();