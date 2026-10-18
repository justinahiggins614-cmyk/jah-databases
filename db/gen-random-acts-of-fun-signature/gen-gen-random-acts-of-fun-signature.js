(function(){'use strict';
/* The The Random Acts of Fun Database Signature generator — jahdb-gen-random-acts-of-fun-signature-sig-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-RANDOM-ACTS-OF-FUN-SIG-";
var GENVER="jahdb-gen-random-acts-of-fun-signature-sig-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The 15-Minute Spark",
  "Free Fun Friday",
  "The Compliment Mission",
  "Sidewalk Chalk Art",
  "The $5 Thrill",
  "Kitchen Experiment",
  "The Memory Lane Drive",
  "Cloud Shape Championship",
  "The Library Lucky Dip",
  "Dance Break Protocol",
  "The Penny Wish",
  "Speed-Friend Challenge"
 ],
 "Compounded": [
  "The Mystery Outing",
  "Thrift Store Challenge",
  "The Food Truck Crawl",
  "Sunset Spot Hunt",
  "The Mini Road Trip",
  "Arcade Afternoon",
  "The Potluck Picnic",
  "Night Swim (Where Allowed)",
  "The Comedy Night Out",
  "Bookstore Wander",
  "The Photo Scavenger Hunt",
  "Karaoke Courage"
 ],
 "Advanced": [
  "The 24-Hour Adventure",
  "The Yes Day",
  "The Flash Mob Picnic",
  "The Skill Swap Party",
  "The Midnight Expedition",
  "The Generosity Spree",
  "The Time Capsule Day",
  "The Festival Crash",
  "The Legacy Fun Day",
  "Masterclass: The Science of Play"
 ]
};
var BLURBS={
 "The 15-Minute Spark": "One tiny burst of fun: a silly walk, a kitchen dance party, a speed-sketch. Small, done, delightful.",
 "Free Fun Friday": "An evening of zero-cost fun: library haul, park sunset, living-room campout.",
 "The Compliment Mission": "Give five genuine compliments today. Watch faces change - including yours.",
 "Sidewalk Chalk Art": "Draw something big and temporary. The neighborhood gets a gallery.",
 "The $5 Thrill": "What is the most fun five dollars can buy? Find out today.",
 "Kitchen Experiment": "Combine three random ingredients into something edible-ish. Science, delicious.",
 "The Memory Lane Drive": "Drive past your old haunts with the windows down. Nostalgia, free.",
 "Cloud Shape Championship": "Lie down, name shapes, keep score. The oldest game still works.",
 "The Library Lucky Dip": "Grab five random books by cover. Judge away.",
 "Dance Break Protocol": "One song, full commitment, wherever you are. Endorphins on demand.",
 "The Penny Wish": "Find a fountain, make a wish, flip the coin. Tiny ritual, real smile.",
 "Speed-Friend Challenge": "Learn one stranger\u2019s story today (safely, kindly). People are plots.",
 "The Mystery Outing": "One person plans, the other just shows up. Surprise is the whole activity.",
 "Thrift Store Challenge": "Ten dollars, best find wins. Creativity under constraint.",
 "The Food Truck Crawl": "Hit three trucks, share everything. A tasting menu on wheels.",
 "Sunset Spot Hunt": "Find the best sunset view within 20 minutes. Chase the light.",
 "The Mini Road Trip": "One town over, no plan, full tank of curiosity.",
 "Arcade Afternoon": "A roll of quarters and zero dignity. High scores and higher laughs.",
 "The Potluck Picnic": "Everyone brings one dish to the park. Feast, cheap.",
 "Night Swim (Where Allowed)": "Moonlight water, safely and legally. Magic is real.",
 "The Comedy Night Out": "Local standup, cheap tickets, big laughs. Support live funny.",
 "Bookstore Wander": "Two hours, no buying required (good luck with that).",
 "The Photo Scavenger Hunt": "A list, a camera, a time limit. Your town becomes a game board.",
 "Karaoke Courage": "One song, full heart. The crowd loves the brave, not the good.",
 "The 24-Hour Adventure": "Dawn to dawn: a full day of planned spontaneity. Legendary.",
 "The Yes Day": "Say yes to every reasonable suggestion for one day. Watch life expand.",
 "The Flash Mob Picnic": "Text friends a park and a time, two hours out. Instant community.",
 "The Skill Swap Party": "Everyone teaches something in 15 minutes. A festival of each other.",
 "The Midnight Expedition": "A safe, legal late-night adventure: diners, overlooks, empty streets.",
 "The Generosity Spree": "A day of small kindnesses with a set budget. Joy, multiplied.",
 "The Time Capsule Day": "Bury or box today\u2019s treasures for future-you. Fun with a sequel.",
 "The Festival Crash": "Find the nearest festival, fair, or market and dive in fully.",
 "The Legacy Fun Day": "Design a perfect fun day and repeat it yearly. Traditions start as experiments.",
 "Masterclass: The Science of Play": "Why adults need play - and how to engineer more of it into real life."
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
    name:topic+' — fun activity record',
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

var BUILD_RANDOM_FUN=(function(){
var BANK={low:[['Living-room blanket fort + a film you have never seen','0-30 min, $0'],['Speed-clean one drawer while music plays','15 min, $0'],['Write a 6-word story about your day','5 min, $0'],['Video-call someone you miss','20 min, $0'],['Cook with only what is already open','30-45 min, $0']],mid:[['Thrift-store challenge: best find under $10','1-2 h, $10'],['Picnic in the nearest green space','1 h, $15'],['Try a free class or workshop nearby','1 h, $0-10'],['Photo walk: 20 shots, one theme','1 h, $0']],high:[['Day-trip to the next town over','half day, $40'],['Mini golf + ice cream run','2 h, $30'],['Sunset spot hunt with snacks','2 h, $20']]};
return function(inp){
  var r=prng(inp.seed||3);
  var budget=inp.budget||'low';
  var pool=BANK[budget]||BANK.low;
  var main=pick(pool,r);
  var others=shuffle(pool,r).filter(function(x){return x[0]!==main[0];}).slice(0,3);
  return {title:'Your random act of fun',intro:'Spontaneous, low-pressure, picked for a '+budget+' budget and about '+(inp.time||'an hour')+' of time.',
    sections:[{h:'Do this',items:[main[0]+' — '+main[1]]},{h:'Backups if the mood shifts',items:others.map(function(x){return x[0]+' — '+x[1];})},{h:'Make it stick',text:'Do it within 24 hours or it was just a nice idea. Send one photo to a friend.'}]};
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
gen.builderId="random-fun";
gen.builderFields=[["time", "Time available", "select", ["15 minutes", "an hour", "half a day", "a full day"]], ["budget", "Budget", "select", ["low", "mid", "high"]], ["seed", "Seed (optional)", "number", "3"]];
gen.build=BUILD_RANDOM_FUN;

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-random-acts-of-fun-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();