(function(){'use strict';
/* JAH Infinite Curiosity Generator - jahdb-gen-infinite-curiosity-1.0.
   Property of Justin Addam Higgins (JAH).
   REAL client-side generator: walks a bank of 72 verified curiosity nodes
   with a seeded, non-repeating walk. Same seed, same chain - every time.
   public edition. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function perm(n,rnd){var p=[];for(var i=0;i<n;i++)p.push(i);for(var i=n-1;i>0;i--){var j=(rnd()*(i+1))|0;var t=p[i];p[i]=p[j];p[j]=t;}return p;}
var PREFIX="JAH-WICG-";
var TOPICS=["Space", "Human Body", "Earth & Nature", "Animals", "History", "Physics", "Technology", "Numbers"];
var NODES=[{"t": "Space", "f": "The Moon is drifting away from Earth at about 3.8 cm per year.", "w": "What happens when it drifts too far to cause total solar eclipses?"}, {"t": "Space", "f": "A day on Venus lasts longer than its year - it rotates once every 243 Earth days but orbits in 225.", "w": "Why does Venus spin backwards compared to most planets?"}, {"t": "Space", "f": "Venus is the hottest planet at 465 C - hotter than Mercury, though it is farther from the Sun.", "w": "What runaway process made the second planet hotter than the first?"}, {"t": "Space", "f": "Saturn would float in water: it is the least dense planet, at 0.69 g per cubic cm.", "w": "What is Saturn actually made of, if it is lighter than water?"}, {"t": "Space", "f": "There are more stars in the universe than grains of sand on all of Earth's beaches.", "w": "With that many stars, where is everybody?"}, {"t": "Space", "f": "Light from the Sun takes 8 minutes 20 seconds to reach Earth.", "w": "What does that delay mean for how we see the universe's past?"}, {"t": "Space", "f": "Olympus Mons on Mars is nearly three times the height of Everest.", "w": "Why can Mars grow volcanoes so much bigger than Earth's?"}, {"t": "Space", "f": "A year on Neptune lasts 165 Earth years - it has completed just one orbit since its discovery.", "w": "What was happening on Earth when Neptune was last in this position?"}, {"t": "Space", "f": "The Great Red Spot is a storm wider than Earth that has raged for centuries.", "w": "What fuels a storm that never stops?"}, {"t": "Human Body", "f": "Your stomach gets a new lining every few days so it does not digest itself.", "w": "What happens when that renewal process fails?"}, {"t": "Human Body", "f": "You cannot tickle yourself because your brain predicts the sensation and cancels it.", "w": "What does that prediction system reveal about consciousness?"}, {"t": "Human Body", "f": "Humans share about 60 percent of their DNA with bananas.", "w": "What does 'shared DNA' actually mean for such different organisms?"}, {"t": "Human Body", "f": "Your bones are stronger than concrete, ounce for ounce.", "w": "What material in bone gives it that strength-to-weight ratio?"}, {"t": "Human Body", "f": "The dark-adapted human eye can detect a single photon.", "w": "If we can see single photons, why is night vision still so poor?"}, {"t": "Human Body", "f": "Goosebumps are a leftover reflex from when humans had full body fur.", "w": "What other reflexes are evolutionary leftovers?"}, {"t": "Human Body", "f": "Your brain runs on about 20 watts - enough to power a dim light bulb.", "w": "How does 20 watts outperform supercomputers at some tasks?"}, {"t": "Human Body", "f": "Babies are born with about 300 bones; adults have 206.", "w": "Which bones fuse together, and why start with more?"}, {"t": "Human Body", "f": "Your nose can remember about 50,000 different scents.", "w": "Why is smell the sense most tied to memory?"}, {"t": "Earth & Nature", "f": "The Sahara was green and full of lakes just 6,000 years ago.", "w": "What flipped the Sahara from green to desert?"}, {"t": "Earth & Nature", "f": "Lake Natron in Tanzania can calcify animals that die in its waters.", "w": "What chemistry turns a lake into a stone-maker?"}, {"t": "Earth & Nature", "f": "Antarctica is the largest desert in the world.", "w": "How can a desert be made of ice?"}, {"t": "Earth & Nature", "f": "The Amazon produces about 6 percent of the world's oxygen - not 20 percent as often claimed.", "w": "If not the Amazon, where does our oxygen actually come from?"}, {"t": "Earth & Nature", "f": "There are about 3 trillion trees on Earth - more trees than stars in the Milky Way.", "w": "How do scientists count 3 trillion trees?"}, {"t": "Earth & Nature", "f": "The deepest part of the ocean is deeper than Everest is tall.", "w": "What lives at the bottom of the deepest trench?"}, {"t": "Earth & Nature", "f": "Lightning strikes Earth about 100 times every second.", "w": "What separates the charges to make lightning at all?"}, {"t": "Earth & Nature", "f": "Parts of the Atacama Desert have never recorded rainfall.", "w": "What makes one strip of coast the driest place on Earth?"}, {"t": "Earth & Nature", "f": "Mount Everest grows about 4 mm taller every year.", "w": "What tectonic collision is still pushing it up?"}, {"t": "Animals", "f": "Octopuses have three hearts and blue blood.", "w": "Why did evolution give them three hearts?"}, {"t": "Animals", "f": "Tardigrades have survived the vacuum of space.", "w": "How does anything survive hard vacuum?"}, {"t": "Animals", "f": "The mantis shrimp's punch is as fast as a bullet.", "w": "What happens to water when something moves through it that fast?"}, {"t": "Animals", "f": "Crows can recognize human faces and hold grudges for years.", "w": "How do crows teach their young which humans to distrust?"}, {"t": "Animals", "f": "Axolotls can regrow entire limbs, including bones and nerves.", "w": "Why can't humans regrow limbs if axolotls can?"}, {"t": "Animals", "f": "The immortal jellyfish can revert to its juvenile stage indefinitely.", "w": "What would it take to trigger that reversal in other organisms?"}, {"t": "Animals", "f": "Honeybees can recognize human faces.", "w": "How does such a tiny brain do face recognition?"}, {"t": "Animals", "f": "Sea cucumbers breathe through their anuses.", "w": "What evolutionary path leads to breathing that way?"}, {"t": "Animals", "f": "Polar bear fur is transparent, not white.", "w": "How does transparent fur look white?"}, {"t": "History", "f": "The Great Pyramid was the tallest human-made structure for 3,800 years.", "w": "What finally beat it in the 1300s?"}, {"t": "History", "f": "Oxford University is older than the Aztec Empire.", "w": "What was being taught at Oxford when Tenochtitlan was founded?"}, {"t": "History", "f": "Nintendo was founded in 1889 as a playing-card company.", "w": "What did Nintendo make before video games?"}, {"t": "History", "f": "The Eiffel Tower was originally intended for Barcelona.", "w": "Why did Barcelona reject it?"}, {"t": "History", "f": "The London Underground opened in 1863, while the American Civil War was raging.", "w": "What did the first subway look like?"}, {"t": "History", "f": "Harvard was founded before calculus was invented.", "w": "What did Harvard teach before modern science existed?"}, {"t": "History", "f": "The fax machine was invented in 1843 - before the telephone.", "w": "How did a fax work without phone lines as we know them?"}, {"t": "History", "f": "The University of al-Qarawiyyin, founded in 859 AD, is the oldest existing university.", "w": "What was studied there in the 800s?"}, {"t": "History", "f": "The first university degrees were awarded in the 1100s.", "w": "What did the first graduates study?"}, {"t": "Physics", "f": "Time moves slower at your feet than at your head, due to gravity.", "w": "Has anyone actually measured the difference across a human body?"}, {"t": "Physics", "f": "Glass is neither a true solid nor a liquid - it is an amorphous solid.", "w": "Do old church windows really flow downward over the centuries?"}, {"t": "Physics", "f": "Hot water can freeze faster than cold water - the Mpemba effect.", "w": "What mechanism could possibly explain that?"}, {"t": "Physics", "f": "You are 99.9999999 percent empty space.", "w": "If atoms are nearly all empty, why can't we walk through walls?"}, {"t": "Physics", "f": "Quantum particles can be in two places at once until observed.", "w": "What counts as an 'observation' in quantum mechanics?"}, {"t": "Physics", "f": "The speed of light is the same for all observers, no matter how fast they move.", "w": "What breaks in physics if the speed of light were not constant?"}, {"t": "Physics", "f": "Absolute zero can never be reached - only approached.", "w": "What law of physics forbids reaching it?"}, {"t": "Physics", "f": "Sound travels about 4.3 times faster in water than in air.", "w": "Why does density speed sound up but slow light down?"}, {"t": "Physics", "f": "Magnets lose their magnetism when heated past the Curie point.", "w": "What is happening inside the metal at that temperature?"}, {"t": "Technology", "f": "The first computer bug was a real moth, found in 1947.", "w": "Who found it, and is the logbook page real?"}, {"t": "Technology", "f": "QR codes were invented for tracking car parts.", "w": "What limitation of barcodes forced the invention?"}, {"t": "Technology", "f": "The first webcam watched a coffee pot at Cambridge.", "w": "Whose coffee was worth inventing the webcam for?"}, {"t": "Technology", "f": "GPS satellites must correct for relativity, or they would drift kilometers daily.", "w": "How big would the positioning error be without the correction?"}, {"t": "Technology", "f": "The QWERTY layout was designed to slow typists down.", "w": "What problem were jamming typewriter keys causing?"}, {"t": "Technology", "f": "The first domain name ever registered was Symbolics.com, in 1985.", "w": "What happened to Symbolics?"}, {"t": "Technology", "f": "Your phone has more computing power than NASA had for Apollo 11.", "w": "How did they reach the Moon with less computing than a phone?"}, {"t": "Technology", "f": "The 'save' icon is a floppy disk most users have never seen.", "w": "What other interface fossils survive from dead technology?"}, {"t": "Technology", "f": "Email existed before the World Wide Web.", "w": "What network carried the first emails?"}, {"t": "Numbers", "f": "A sheet of paper folded 103 times would exceed the observable universe.", "w": "How can 103 folds beat the entire universe?"}, {"t": "Numbers", "f": "The number zero was invented independently in multiple civilizations.", "w": "How did mathematics work without zero?"}, {"t": "Numbers", "f": "A 'jiffy' is a real unit of time: one hundredth of a second in computing.", "w": "Who needed a word for a hundredth of a second?"}, {"t": "Numbers", "f": "The word 'hundred' once meant 120 in some Germanic counting systems.", "w": "What was the 'long hundred' used for?"}, {"t": "Numbers", "f": "111,111,111 times 111,111,111 equals 12,345,678,987,654,321.", "w": "What pattern makes that multiplication work?"}, {"t": "Numbers", "f": "Many buildings skip the 13th floor.", "w": "Do the elevators really skip it, or just rename it?"}, {"t": "Numbers", "f": "A 'googol' (10 to the 100th) is bigger than the number of atoms in the universe.", "w": "Why did a search company name itself after it?"}, {"t": "Numbers", "f": "The Fibonacci sequence appears in sunflower spirals and pinecones.", "w": "What is the plant actually optimizing?"}, {"t": "Numbers", "f": "Pi has been computed to over 200 trillion digits.", "w": "Why compute digits that nobody will ever use?"}];
var MAXDEPTH=8;
var SOURCE='public';
function walkChain(seed,depth,topic){
  var rnd=prng(seed), order=perm(NODES.length,rnd), used={}, chain=[];
  var start=order[0];
  if(topic){ for(var k=0;k<order.length;k++){ if(NODES[order[k]].t===topic){ start=order[k]; break; } } }
  chain.push(start); used[start]=1;
  while(chain.length<depth){
    var curT=NODES[chain[chain.length-1]].t, nxt=-1, i, id;
    for(i=0;i<order.length;i++){ id=order[i]; if(!used[id]&&NODES[id].t===curT){ nxt=id; break; } }
    if(nxt<0){ for(i=0;i<order.length;i++){ id=order[i]; if(!used[id]){ nxt=id; break; } } }
    if(nxt<0) break;
    chain.push(nxt); used[nxt]=1;
  }
  return chain;
}
function chainProse(chain,seed){
  var parts=[];
  for(var k=0;k<chain.length;k++){
    var n=NODES[chain[k]];
    parts.push(k===0?('Start here: '+n.f):('The answer pulls you deeper: '+n.f));
    if(k<chain.length-1) parts.push((k===0?'That raises the question: ':'Which makes you wonder: ')+n.w);
  }
  parts.push('Follow the chain far enough and every answer becomes a doorway. That is the Infinite Curiosity method: never stop at the answer - ask what it opens. (Seed '+seed+'.)'+(SOURCE==='signature'?' The Signature treatment compounds each link: simple wonder first, deeper mechanism later.':''));
  return parts.join('\n\n');
}
function demoProgram(chain){
  var lines=chain.map(function(id,k){return '    print("  '+(k+1)+'. '+NODES[id].f.replace(/"/g,"'")+'")';});
  return '# Infinite Curiosity Generator - live chain\nLINKS = [\n'+chain.map(function(id){return '    "'+NODES[id].t+': '+NODES[id].f.replace(/"/g,"'")+'",';}).join('\n')+'\n]\ndef main():\n    print("CURIOSITY CHAIN")\n'+lines.join('\n')+'\n    print("chain length: %d links" % len(LINKS))\n    print("OK: curiosity chain of %d links generated" % len(LINKS))\nif __name__ == "__main__":\n    main()\n';
}
function generate(seed,opts,rnd){
  opts=opts||{};
  var depth=Math.min(MAXDEPTH,Math.max(3,opts.depth|0||5));
  var field=(opts.field&&TOPICS.indexOf(opts.field)>=0)?opts.field:null;
  var chain=walkChain(seed>>>0||1,depth,field);
  var firstT=NODES[chain[0]].t;
  var hook0=NODES[chain[0]].f.slice(0,64);
  var hook=hook0.slice(0,Math.max(1,hook0.lastIndexOf(' ')));
  var title='Curiosity Chain (live): '+hook+'...'+(SOURCE==='signature'?' (Signature Edition)':'');
  var desc=chainProse(chain,seed>>>0||1);
  var id=PREFIX+String(seed>>>0||1).padStart(6,'0');
  return {
    id:id,
    name:title+' — '+firstT,
    title:title,
    description:'GENERATED CHAIN (live generator output - clearly labeled). '+desc,
    field:firstT,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Live generator output - not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'python',language:'python',program:demoProgram(chain),note:'Live chain demo program.'},
    _seed:seed>>>0||1, chain:chain
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(TOPICS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.chain||!r.chain.length)e.push('chain');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-gen-infinite-curiosity-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:TOPICS,nodes:NODES,walkChain:walkChain,maxDepth:MAXDEPTH};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-infinite-curiosity',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
