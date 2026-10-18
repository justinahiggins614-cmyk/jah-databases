(function(){'use strict';
/* The The Random Skill of the Day Database Signature generator — jahdb-gen-random-skill-of-the-day-signature-sig-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-RANDOM-SKILL-OF-THE-DAY-SIG-";
var GENVER="jahdb-gen-random-skill-of-the-day-signature-sig-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The Bowline Knot",
  "Speed Reading Basics",
  "The Memory Palace",
  "Whistling Loud",
  "Home-Row Typing",
  "The Paper Crane Fold",
  "Two-Ball Juggling",
  "Beatbox Basics",
  "The Pocket Fold",
  "Mental Math Tricks",
  "Proportional Faces",
  "Pen Spinning Start"
 ],
 "Compounded": [
  "Morse Code SOS",
  "The Riffle Shuffle",
  "Speed Cube First Layer",
  "Calligraphy Initial",
  "The Bird Call",
  "One-Foot Balance",
  "The Gratitude Letter",
  "Speed Sketching",
  "The Coin Roll",
  "Lock Basics (Practice Lock)",
  "The Yoyo Sleeper",
  "Napkin Ring Math"
 ],
 "Advanced": [
  "The 30-Day Skill Sprint",
  "Teaching a Skill",
  "The Skill Chain",
  "Performance Ready",
  "The Skill Journal",
  "Skill Swap Meet",
  "The Impossible Skill",
  "Legacy: The Skill Collection",
  "Masterclass: How Skills Compound",
  "The Renaissance Year"
 ]
};
var BLURBS={
 "The Bowline Knot": "The king of knots in fifteen minutes: the rabbit, the tree, the hole.",
 "Speed Reading Basics": "Time a page, re-read for meaning: the first step to faster reading.",
 "The Memory Palace": "Ten groceries along your hallway: walk it twice, remember forever.",
 "Whistling Loud": "Fingers, breath, practice: the playground superpower.",
 "Home-Row Typing": "asdf jkl;, ten minutes, no peeking: the foundation of speed.",
 "The Paper Crane Fold": "Sixteen folds, one beautiful bird: origami\u2019s hello.",
 "Two-Ball Juggling": "The cascade foundation: throws that land steady.",
 "Beatbox Basics": "Boots and cats: the three sounds that start everything.",
 "The Pocket Fold": "Napkin elegance in six folds: dinner-table upgrade.",
 "Mental Math Tricks": "Two-digit multiplication, broken down: the party trick with uses.",
 "Proportional Faces": "Oval, thirds, features: drawing people, demystified.",
 "Pen Spinning Start": "The thumb-around: fifty tries, one smooth spin.",
 "Morse Code SOS": "Dots, dashes, and your initials: the timeless signal skill.",
 "The Riffle Shuffle": "Split, bridge, square: cards like a dealer.",
 "Speed Cube First Layer": "White cross then corners: the cube surrenders in stages.",
 "Calligraphy Initial": "Your letter, twenty slow reps: the beautiful hand.",
 "The Bird Call": "One species, learned well: try it outside today.",
 "One-Foot Balance": "Sixty seconds, eyes open then closed: the wobble workout.",
 "The Gratitude Letter": "150 words to someone specific: the skill of saying thanks.",
 "Speed Sketching": "Thirty-second gestures: drawing fast and loose.",
 "The Coin Roll": "Across the knuckles: the classic fidget, mastered.",
 "Lock Basics (Practice Lock)": "How pin tumblers work, on your own practice lock: the honest skill.",
 "The Yoyo Sleeper": "Throw, sleep, return: the foundation trick.",
 "Napkin Ring Math": "Fold the perfect ring: geometry you can wear.",
 "The 30-Day Skill Sprint": "One skill, thirty days, real competence: the deep version.",
 "Teaching a Skill": "Turn any learned skill into a 5-minute lesson: mastery\u2019s final test.",
 "The Skill Chain": "Link daily skills into combos: juggling + unicycling = legend.",
 "Performance Ready": "Polish one skill for an audience: the stage version.",
 "The Skill Journal": "Log every skill with notes: the compounding record.",
 "Skill Swap Meet": "Trade skills with friends: the community university.",
 "The Impossible Skill": "Pick the one you swore you couldn\u2019t: the 90-day quest.",
 "Legacy: The Skill Collection": "A lifetime of tiny skills: the most fun resume ever.",
 "Masterclass: How Skills Compound": "The science of micro-learning: why daily tiny wins.",
 "The Renaissance Year": "365 skills, one year: the ultimate challenge."
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
    name:topic+' — daily skill record',
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

var BUILD_DAILY_SKILL=(function(){
var SKILLS=[['Speed reading','Time one page, then re-read for comprehension; track words per minute.'],['Knot tying','Learn the bowline today: rabbit, tree, hole. Ten reps each hand.'],['Memory palace','Place 10 grocery items along your hallway; walk it twice.'],['Whistling with fingers','Position, breath, adjust — 15 minutes of loud trial.'],['Touch typing home row','10 minutes on asdf jkl; no peeking, accuracy over speed.'],['Origami crane','One square of paper, 16 folds, follow along slowly.'],['Juggling 3 balls','Two-ball cascade first; add the third when throws land steady.'],['Basic beatboxing','Boots-n-cats: B-T-K-T sounds, loop them slow.'],['Napkin folding','The pocket fold: 6 folds, instant dinner-table upgrade.'],['Mental math: 2-digit multiply','Break into tens and ones; 5 problems, time yourself.'],['Drawing a face in proportion','Oval, eye-line halfway, thirds for nose and mouth.'],['Pen spinning (thumb-around)','Push, catch, repeat — 50 tries minimum.'],['Morse code basics','SOS first, then your initials; tap it on the table.'],['Card shuffle (riffle)','Split, bridge, square — practice over a table.'],['Lock picking (your own lock)','Tension wrench + pick on a practice lock only.'],['Speed cubing: first layer','White cross, then corners — one algorithm at a time.'],['Calligraphy: one letterform','Pick your initial; 20 slow reps with any pen.'],['Bird call: one species','Learn the robin or crow call; try it outside.'],['Balance: 60-second one-foot stand','Eyes open, then closed; switch feet.'],['Gratitude letter','Write 150 words to someone specific; send it.']];
return function(inp){
  var seed=parseInt(inp.seed,10)||((new Date().getFullYear()*1000)+(new Date().getMonth()*40)+(new Date().getDate()));
  var r=prng(seed);
  var pool=SKILLS.filter(function(s){return !inp.interest||s[1].toLowerCase().indexOf(inp.interest.toLowerCase())>=0;});
  if(!pool.length)pool=SKILLS;
  var s=pick(pool,r);
  return {title:'Skill of the day: '+s[0],intro:'One small skill, one 15-minute lesson. Do it today; the streak is the skill.',
    sections:[{h:'Your 15-minute lesson',items:['Minutes 0–3: watch or read how it is done once.', 'Minutes 3–10: '+s[1], 'Minutes 10–15: repeat the hardest part three times.']},{h:'Prove it',text:'Record a 30-second clip or write one sentence about what clicked. Tomorrow builds on today.'}]};
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
gen.builderId="daily-skill";
gen.builderFields=[["interest", "Interest (optional)", "text", ""], ["seed", "Seed: use today\u2019s date number, or pick", "number", "20261017"]];
gen.build=BUILD_DAILY_SKILL;

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-random-skill-of-the-day-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();