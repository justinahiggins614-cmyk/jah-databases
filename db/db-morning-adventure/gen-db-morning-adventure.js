(function(){'use strict';
/* The The Morning Adventure Database generator — jahdb-db-morning-adventure-pub-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-MORNING-ADVENTURE-PUB-";
var GENVER="jahdb-db-morning-adventure-pub-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The Sunrise Walk",
  "Breakfast Experiment Day",
  "New Route to Work",
  "Morning Pages",
  "The 10-Minute Tidy Sprint",
  "Coffee Shop Morning",
  "Stretch in the Sun",
  "The Gratitude Porch Sit",
  "Learn-One-Thing Breakfast",
  "The Early Errand Win",
  "Birdsong Listening",
  "Make Something Before Work"
 ],
 "Compounded": [
  "Sunrise Hike Mission",
  "The Breakfast Club",
  "Morning Market Run",
  "Photo Walk Challenge",
  "The Swim Start",
  "Volunteer Morning",
  "The Long Breakfast Cook",
  "Sunrise Paddle",
  "The Museum Early Hour",
  "Neighborhood History Walk",
  "The 5K Before Breakfast",
  "Sunrise Picnic"
 ],
 "Advanced": [
  "The Dawn Patrol Club",
  "Sunrise Summit Series",
  "The Morning Sabbatical",
  "City Sunrise Tour",
  "The 4AM Club, Done Right",
  "Morning Adventure Streak",
  "The Sunrise Proposal Plan",
  "Legacy Mornings",
  "Masterclass: Chronotype Design",
  "The Year of Mornings"
 ]
};
var BLURBS={
 "The Sunrise Walk": "Fifteen minutes outside as the sun comes up. Light, air, and a day that starts with wonder.",
 "Breakfast Experiment Day": "Try one new breakfast a week: overnight oats, shakshuka, smoothie bowls. Mornings get delicious.",
 "New Route to Work": "Take the long way once. New streets, new thoughts, same arrival time.",
 "Morning Pages": "Three pages of longhand before screens. The mind empties and the day clarifies.",
 "The 10-Minute Tidy Sprint": "Reset one room before leaving. Come home to calm.",
 "Coffee Shop Morning": "Work or read somewhere new for an hour. Scenery changes thinking.",
 "Stretch in the Sun": "Ten minutes of stretching in direct morning light. Body and clock both reset.",
 "The Gratitude Porch Sit": "Coffee outside, three gratitudes. Five minutes that reframe everything.",
 "Learn-One-Thing Breakfast": "One short video or article with breakfast. Compounding curiosity, daily.",
 "The Early Errand Win": "Do the dreaded errand at 7am. The rest of the day feels downhill.",
 "Birdsong Listening": "Sit still and count the birds you hear. Mindfulness with feathers.",
 "Make Something Before Work": "Sketch, write, or build for twenty minutes. Creativity before obligation.",
 "Sunrise Hike Mission": "A real trail at dawn: headlamp start, summit sunrise. The best alarm clock is a view.",
 "The Breakfast Club": "A standing weekly breakfast with friends. Rituals beat resolutions.",
 "Morning Market Run": "Farmers market at opening: the freshest picks and the liveliest hour.",
 "Photo Walk Challenge": "Twenty photos, one theme, before 9am. See your neighborhood like a tourist.",
 "The Swim Start": "A morning swim, pool or open water. Nothing wakes you like water.",
 "Volunteer Morning": "Two hours helping before the day starts. Perspective, guaranteed.",
 "The Long Breakfast Cook": "Weekend project breakfast: pancakes from scratch, slow coffee. Worth waking for.",
 "Sunrise Paddle": "Kayak or paddleboard at dawn. Glass water, empty world.",
 "The Museum Early Hour": "First entry, empty galleries. Art without crowds.",
 "Neighborhood History Walk": "Research one street\u2019s story, then walk it. Your block becomes a museum.",
 "The 5K Before Breakfast": "Run it, walk it, own it. Breakfast tastes like victory.",
 "Sunrise Picnic": "Blanket, thermos, pastries at a viewpoint. Romance with the day itself.",
 "The Dawn Patrol Club": "A crew that meets for sunrise adventures weekly. Community built on early light.",
 "Sunrise Summit Series": "Twelve peaks, twelve sunrises, one year. A quest with a view.",
 "The Morning Sabbatical": "One full week of designed mornings: the ultimate reset experiment.",
 "City Sunrise Tour": "Watch dawn from a different landmark each month. Know your city by its mornings.",
 "The 4AM Club, Done Right": "Extreme early rising with real sleep science: protecting rest while owning the dark hours.",
 "Morning Adventure Streak": "Thirty different mornings in thirty days. Documented, photographed, unforgettable.",
 "The Sunrise Proposal Plan": "For the big question: timing, location, and light, planned to perfection.",
 "Legacy Mornings": "Design a morning ritual worth passing down: the family\u2019s dawn tradition.",
 "Masterclass: Chronotype Design": "Build mornings around your real biology, not hustle mythology.",
 "The Year of Mornings": "A full year of intentional mornings, logged and reviewed. A life, redesigned dawn by dawn."
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
    name:topic+' — morning adventure record',
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

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-morning-adventure',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();