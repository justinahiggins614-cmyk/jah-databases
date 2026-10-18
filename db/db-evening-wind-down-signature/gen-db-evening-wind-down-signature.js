(function(){'use strict';
/* The The Evening Wind-Down Database Signature generator — jahdb-db-evening-wind-down-signature-sig-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-EVENING-WIND-DOWN-SIG-";
var GENVER="jahdb-db-evening-wind-down-signature-sig-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The 20-Minute Unwind",
  "Gentle Stretch Flow",
  "The No-Screen Hour",
  "Tea Ritual",
  "Evening Walk Loop",
  "Journal Dump",
  "Warm Shower Sequence",
  "Candlelight Dinner for One",
  "The Gratitude Three",
  "Puzzle Wind-Down",
  "Scent Switch",
  "The Tomorrow List"
 ],
 "Compounded": [
  "The Bath Ritual",
  "Yin Yoga Evening",
  "Cooking as Meditation",
  "The Listening Session",
  "Stargazing Wind-Down",
  "The Couple\u2019s Debrief",
  "Evening Sketch Session",
  "The Digital Sunset",
  "Read-Aloud Ritual",
  "Garden Evening Rounds",
  "The Slow Dinner Party",
  "Meditation Progression"
 ],
 "Advanced": [
  "The Full Sleep Sanctuary",
  "The Weekly Sabbath Evening",
  "The Seasonal Wind-Down",
  "The Stress-Detox Evening",
  "The Artist\u2019s Evening",
  "The Family Wind-Down",
  "Travel Wind-Down Kit",
  "The Decade Review Evening",
  "Legacy: The Evening Tradition",
  "Masterclass: Sleep Science at Home"
 ]
};
var BLURBS={
 "The 20-Minute Unwind": "A simple sequence: change clothes, dim lights, herbal tea. The day officially ends.",
 "Gentle Stretch Flow": "Ten minutes of easy stretches release the day\u2019s tension from shoulders and back.",
 "The No-Screen Hour": "One hour before bed with zero screens. Rediscover books, baths, and boredom.",
 "Tea Ritual": "Brew, sip slowly, notice the warmth. A tiny ceremony with outsized calm.",
 "Evening Walk Loop": "A slow walk around the block as the light fades. The day gets a proper goodbye.",
 "Journal Dump": "Empty the mind onto paper: tomorrow\u2019s worries become tonight\u2019s list, then rest.",
 "Warm Shower Sequence": "Warm water, slow breathing. The post-shower cool-down invites sleep.",
 "Candlelight Dinner for One": "Eat by candlelight, no phone. Ordinary dinner becomes occasion.",
 "The Gratitude Three": "Name three good things from today. The brain files the day as good.",
 "Puzzle Wind-Down": "A jigsaw or crossword: engaging enough to distract, calm enough to soothe.",
 "Scent Switch": "An evening scent - lavender, cedar - signals the brain that day mode is over.",
 "The Tomorrow List": "Write tomorrow\u2019s top three tonight. The mind stops rehearsing and rests.",
 "The Bath Ritual": "Epsom salts, low light, no phone: the full reset button for hard days.",
 "Yin Yoga Evening": "Long-held gentle poses melt deep tension. Forty minutes of profound unwinding.",
 "Cooking as Meditation": "A slow, simple recipe made mindfully. Chopping becomes calming.",
 "The Listening Session": "One album, start to finish, eyes closed. Music as the whole evening.",
 "Stargazing Wind-Down": "A blanket and the night sky. Perspective is the ultimate relaxant.",
 "The Couple\u2019s Debrief": "Fifteen minutes sharing the day\u2019s highs and lows. Connection is calming.",
 "Evening Sketch Session": "Draw the day: a scene, a feeling, a doodle. Creative unwinding.",
 "The Digital Sunset": "All screens docked and dimmed at a set hour. The house exhales.",
 "Read-Aloud Ritual": "Read to each other or listen to an audiobook together. Stories soothe all ages.",
 "Garden Evening Rounds": "Water, weed, and wander the garden at dusk. Nature\u2019s own wind-down.",
 "The Slow Dinner Party": "Friends, simple food, long table, no rush. The evening as event.",
 "Meditation Progression": "Ten minutes building to twenty over a month. The mind learns stillness gradually.",
 "The Full Sleep Sanctuary": "Bedroom, routine, and environment engineered together for legendary sleep.",
 "The Weekly Sabbath Evening": "One evening a week with zero obligations: the deep recharge ritual.",
 "The Seasonal Wind-Down": "Evening rituals that shift with the seasons: fire pits, porches, and blankets.",
 "The Stress-Detox Evening": "A protocol for brutal days: movement, heat, journaling, and early bed. Recovery, designed.",
 "The Artist\u2019s Evening": "Creative wind-down for makers: sketchbooks, instruments, and gentle making.",
 "The Family Wind-Down": "A whole-household routine: kids, adults, and pets all descending together.",
 "Travel Wind-Down Kit": "Hotel-room rituals that make any bed feel like home. Sleep anywhere.",
 "The Decade Review Evening": "Once a year, review the year by candlelight: what mattered, what\u2019s next.",
 "Legacy: The Evening Tradition": "A wind-down ritual worth handing down: the family\u2019s way of ending days well.",
 "Masterclass: Sleep Science at Home": "The full evidence-based sleep protocol, translated into a livable evening."
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
    name:topic+' — evening wind-down record',
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

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-evening-wind-down-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();