(function(){'use strict';
/* JAH The Family Game Generator Database — REAL generator — "jahdb-gen-family-game-generator-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same output. Every run produces a genuine,
   fully-formed new item — never a structural sample. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,s){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(s()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}
function fill(t,slots,s){var out=t;Object.keys(slots).forEach(function(k){out=out.split('{'+k+'}').join(pick(slots[k],s));});return out;}
function pyDemo(title,text){
  var t=String(text).replace(/\\/g,'\\\\').replace(/"""/g,'\\"\\"\\"');
  var h=String(title).replace(/[\r\n]+/g,' ').slice(0,120);
  return '# '+h+'\n# Property of Justin Addam Higgins (JAH).\n'
    + 'ITEM = """'+t+'"""\n'
    + 'print(ITEM)\n'
    + 'assert len(ITEM) > 40, "empty generated item"\n'
    + 'assert "{" not in ITEM, "unfilled slot in generated item"\n'
    + 'print("generated_chars=%d" % len(ITEM))\n'
    + 'print("DEMO OK")\n';
}
var PREFIX="JAH-FAMGAMGEN-";
var SRC="public-harvest";
var RECORD_KIND="family game record";

var FIELDS=["Quiz Round","Scavenger Hunt","Charades Deck","Story Builder"];
var QUIZ=[{"q": "How many legs does a spider have?", "a": "Eight."}, {"q": "What planet is known as the Red Planet?", "a": "Mars."}, {"q": "How many days are in a leap year?", "a": "366."}, {"q": "What is the largest ocean on Earth?", "a": "The Pacific Ocean."}, {"q": "Which animal is the tallest in the world?", "a": "The giraffe."}, {"q": "How many colors are in a rainbow?", "a": "Seven."}, {"q": "What do you call a baby frog?", "a": "A tadpole."}, {"q": "Which planet has beautiful rings around it?", "a": "Saturn."}, {"q": "How many sides does a triangle have?", "a": "Three."}, {"q": "What is the fastest land animal?", "a": "The cheetah."}, {"q": "What gas do plants absorb from the air?", "a": "Carbon dioxide."}, {"q": "How many minutes are in an hour?", "a": "Sixty."}, {"q": "Which ocean is the Bermuda Triangle in?", "a": "The Atlantic Ocean."}, {"q": "What is a group of wolves called?", "a": "A pack."}, {"q": "How many strings does a violin have?", "a": "Four."}, {"q": "What is the hardest natural substance on Earth?", "a": "Diamond."}, {"q": "Which bird cannot fly but swims well?", "a": "The penguin."}, {"q": "How many players are on a soccer team on the field?", "a": "Eleven."}, {"q": "What is the capital of France?", "a": "Paris."}, {"q": "What do caterpillars turn into?", "a": "Butterflies (or moths)."}, {"q": "How many teeth does an adult human usually have?", "a": "Thirty-two."}, {"q": "What is H2O commonly known as?", "a": "Water."}, {"q": "Which continent is the Sahara Desert on?", "a": "Africa."}, {"q": "What shape has five sides?", "a": "A pentagon."}, {"q": "How many wheels does a tricycle have?", "a": "Three."}, {"q": "What is the largest mammal in the world?", "a": "The blue whale."}, {"q": "Which month has the fewest days?", "a": "February."}, {"q": "What do you call frozen water?", "a": "Ice."}, {"q": "How many cents are in a dollar?", "a": "One hundred."}, {"q": "What animal says 'moo'?", "a": "A cow."}, {"q": "What is the sun?", "a": "A star."}, {"q": "How many seasons are there in a year?", "a": "Four."}, {"q": "What color do you get mixing blue and yellow?", "a": "Green."}, {"q": "Which animal is known as the king of the jungle?", "a": "The lion."}, {"q": "How many hours are in a day?", "a": "Twenty-four."}, {"q": "What do bees make?", "a": "Honey."}, {"q": "What is the opposite of hot?", "a": "Cold."}, {"q": "How many letters are in the English alphabet?", "a": "Twenty-six."}, {"q": "What fruit keeps the doctor away, according to the saying?", "a": "An apple."}, {"q": "Which animal hops and carries babies in a pouch?", "a": "A kangaroo."}];
var HUNT=["something red", "something that makes noise", "something soft", "something older than you", "something that smells good", "something with wheels", "something you can wear", "something that grows", "something square", "something that reflects", "something with a button", "something that opens and closes", "something tiny", "something that floats", "something with stripes", "something you read", "something musical", "something from nature", "something blue", "something that keeps you warm", "something funny", "something with a handle", "something shiny", "something round"];
var CHARADES=[{"w": "brushing teeth", "d": "Easy"}, {"w": "walking a dog", "d": "Easy"}, {"w": "eating spaghetti", "d": "Easy"}, {"w": "playing basketball", "d": "Easy"}, {"w": "a penguin waddling", "d": "Medium"}, {"w": "building a sandcastle", "d": "Medium"}, {"w": "a robot dancing", "d": "Medium"}, {"w": "flying a kite", "d": "Medium"}, {"w": "a popcorn kernel popping", "d": "Hard"}, {"w": "defusing a bomb (gently!)", "d": "Hard"}, {"w": "a sloth crossing the road", "d": "Hard"}, {"w": "baking a cake in fast-forward", "d": "Hard"}, {"w": "a cat chasing a laser pointer", "d": "Easy"}, {"w": "swimming upstream", "d": "Medium"}, {"w": "a statue coming to life", "d": "Hard"}, {"w": "wrapping a present", "d": "Easy"}];
var STARTERS=["On the morning of the big picnic, the family discovered the car would not start — and something was glowing in the garage.", "Grandma's old recipe box had one card nobody had ever dared to cook — until today.", "The power went out during the storm, and that is when the knocking started — three knocks, then giggling.", "A mysterious package arrived with no return address, labeled: OPEN TOGETHER AFTER DINNER.", "The new puppy dug up something shiny in the backyard that hummed when you held it."];
var TWISTS=["A talking parrot lands on the windowsill with urgent news.", "Someone's phone starts playing music nobody recognizes — and it is coming from inside the walls.", "A long-lost relative knocks on the door holding a pie.", "Everything suddenly goes silent — even the birds.", "A map falls out of a book, marked with an X in your own neighborhood.", "The youngest person present suddenly knows exactly what to do.", "It starts raining — indoors. Just a little."];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var title,body;
  if(field==="Quiz Round"){
    var qs=shuffle(QUIZ,rnd).slice(0,5);
    title='Family quiz round ('+qs.length+' questions)';
    body='FAMILY QUIZ ROUND — read each question aloud; players write answers secretly. Answers are at the bottom, no peeking.\n\n'
      +qs.map(function(q,i){return 'Q'+(i+1)+': '+q.q;}).join('\n')
      +'\n\nScoring: 1 point per correct answer, bonus point for the funniest wrong answer (family vote).\n\nANSWERS (no peeking):\n'
      +qs.map(function(q,i){return 'A'+(i+1)+': '+q.a;}).join('\n');
  }else if(field==="Scavenger Hunt"){
    var items=shuffle(HUNT,rnd).slice(0,8);
    title='Family scavenger hunt ('+items.length+' items)';
    body='FAMILY SCAVENGER HUNT — 20 minutes on the clock. Find each item and bring it (or photograph it) back to base.\n\n'
      +items.map(function(it,i){return (i+1)+'. '+it;}).join('\n')
      +'\n\nScoring: 1 point per item, 2 points if the whole family agrees it was the most creative find. Grown-ups play too — no sidelines in this family.';
  }else if(field==="Charades Deck"){
    var cards=shuffle(CHARADES,rnd).slice(0,8);
    title='Family charades deck ('+cards.length+' cards)';
    body='FAMILY CHARADES — no talking, no pointing at objects, sounds and gestures only. 60 seconds per card.\n\n'
      +cards.map(function(c,i){return 'Card '+(i+1)+' ['+c.d+']: '+c.w;}).join('\n')
      +'\n\nLittle kids get the Easy cards first; let them deal. The actor may not speak — the guessers may shout all they want.';
  }else{
    var st=pick(STARTERS,rnd);
    var tw=shuffle(TWISTS,rnd).slice(0,3);
    title='Family story builder';
    body='FAMILY STORY BUILDER — one person reads the starter, then players take turns adding one sentence each. When a twist card appears, the next player MUST work it in.\n\nStarter: '+st
      +'\n\nTwist cards (in order):\n'+tw.map(function(t,i){return (i+1)+'. '+t;}).join('\n')
      +'\n\nKeep going until someone says "the end" and everyone agrees. Write down the best lines — family lore starts here.';
  }
  var desc='NEW FAMILY GAME (generated). '+body;
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — '+RECORD_KIND,
    title:title,
    description:desc,
    field:field,
    src:SRC,
    sample:true,
    disclaimer:'Generated family game — answers included where needed. Seeded archive records are the authoritative entries.',
    demo:{kind:'family-game',language:'python',program:pyDemo(title,desc),note:'Demo prints the generated game.'},
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
  if(!r.description||r.description.length<40)e.push('description');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:"jahdb-gen-family-game-generator-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("gen-family-game-generator",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
