(function(){'use strict';
/* Public Audiobooks Database generator — jahdb-public-audiobooks-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   Each record carries the COMPLETE original text (a full short work) plus a
   read-aloud demo program — a full file, never a stub.
   src:"signature-generated-sample" = Signature-authored original, clearly labeled. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
var PREFIX='JAH-ABK-';
var GENRES=['fiction','mystery','science-fiction','adventure','fable','essay','poetry-collection','memoir'];
var WORKS=[
 {t:'The Clockwork Garden',g:'fiction',text:'Mira found the garden on the Tuesday the clocks stopped. Every timepiece in Bellweather — the church tower, the station clock, her grandfather\'s pocket watch — halted at 7:14, and in the silence she heard it: a ticking from beneath the old greenhouse floor.\n\nShe pried up a flagstone and found stairs wound with brass vines. Down she went, lamp in hand, into a garden where flowers opened and closed like shutters, where bees hummed in perfect four-four time, and where a gardener of copper and glass tended rows of blossoming gears.\n\n"You\'re early," the gardener said, without looking up. "The garden only blooms when time stands still, and time only stands still when someone needs it to."\n\nMira thought of her grandfather\'s hospital bed, the doctors\' careful voices, the way her mother kept checking a watch that no longer moved. "I need it to," she whispered.\n\nThe gardener handed her a seed — a tiny, warm cog. "Plant this where he sleeps. It won\'t give you more time. Nothing does. But it will make the time you have run true."\n\nShe ran all the way home. The clocks resumed at 7:15, as if nothing had happened. But in her pocket the cog was warm, and that evening, when she tucked it beneath her grandfather\'s pillow, his breathing eased into a rhythm like a lullaby, and he smiled in his sleep.\n\nMira never found the greenhouse stairs again. She didn\'t need to. Every garden she planted afterward grew a little out of season and exactly on time.'},
 {t:'The Cartographer of Small Hours',g:'mystery',text:'Detective Inspector Halloran did his best thinking between 3 and 4 a.m., which is why the call about the Merriweather Museum didn\'t wake him — he was already awake, mapping.\n\nHe mapped everything: the milk bottles on his step, the constellations of moths around the streetlamp, the precise order of his neighbor\'s coughs. It was a habit from the war, when maps were the difference between breakfast and burial.\n\nThe museum\'s night guard swore the east wing\'s new exhibit — a 12th-century astrolabe — had moved six inches left overnight. No break-in. No fingerprints. Just six inches.\n\nHalloran measured. Five and three-quarter inches, actually. He mapped the room: the guard\'s chair, the thermos ring on the desk, the window latch, slightly bent.\n\n"The latch," he said. "Someone opened it from inside."\n\nThe curator paled. The astrolabe was a replica — the real one, worth a fortune, had been swapped weeks ago, and tonight someone had come back for the copy too, to complete the set of lies.\n\nThey found the thief\'s map in the guard\'s locker: the museum\'s floor plan, annotated in a careful hand, with one room circled and labeled in the small hours\' ink: "the room where nobody looks."\n\nHalloran looked. Case closed by sunrise.'},
 {t:'Signal in the Static',g:'science-fiction',text:'Dr. Amara Vance had listened to the static of deep space for eleven years before it listened back.\n\nThe array at Kestrel Point caught it first: a pulse, 1.4 seconds, repeating — the hydrogen line, but modulated, shaped, deliberate. Not a beacon. A question.\n\nAmara\'s team spent four months proving it wasn\'t a satellite, a glitch, or wishful thinking. Then they spent a year deciding whether to answer. The debates were fierce and familiar: the hopeful, the fearful, the ones who quoted history like a warning label.\n\nIn the end Amara answered alone, at 3 a.m., with the transmitter aimed at the coordinates and her hand shaking on the key. She sent the hydrogen line back — the same pulse, the same shape — and then, because she was a scientist and also a person, she sent one more thing: the first four notes of the lullaby her grandmother used to sing.\n\nThe reply came 214 days later. The pulse. The lullaby, returned note for note. And underneath, a new pattern — longer, complex, patient.\n\n"It\'s a map," whispered her grad student, tears on his face. "No," said Amara, smiling for the first time in a year. "It\'s an invitation."\n\nThey are still translating it. Some invitations take generations to RSVP to.'},
 {t:'The Last Lighthouse Keeper\'s Apprentice',g:'adventure',text:'When the letter came, Jonah was mending nets in a harbor that had forgotten his name.\n\n"Greyrock Light seeks an apprentice," it read. "Must not fear heights, weather, or solitude. Must be able to learn." He could learn. He\'d been learning to be invisible for years.\n\nThe keeper, Elias Vane, was seventy-four and made of rope and weather. He taught Jonah the lamp first: the great Fresnel lens, the clockwork rotation, the oil, the wicks trimmed like prayers.\n\n"Why keep it burning?" Jonah asked one gale-torn night. "Ships have radar now. Satellites."\n\nElias pointed at the black water. "See that? Nothing out there knows your name. The light doesn\'t care. It burns for whoever needs it. That\'s the whole job. That\'s the whole of every job worth doing."\n\nIn Jonah\'s third winter, the automation crew came with their solar panels and sensors. Elias retired to a cottage with a view of the light. Jonah stayed on as the last keeper\'s apprentice — the boy who tended a flame the world said it didn\'t need.\n\nOn foggy nights, sailors still radio their thanks to Greyrock. Jonah answers every time. "Light\'s on," he says. "Always."'},
 {t:'The Ant and the Avalanche',g:'fable',text:'High in the mountains, where the snow piled deeper than houses, lived an ant named Pella who was famous for carrying twice her weight.\n\n"Why do you work so hard?" asked the grasshopper, who lived for the summer concerts. "The mountain provides."\n\n"The mountain provides," agreed Pella, "and the mountain takes away. I carry for the taking-away days."\n\nThe other insects laughed. Then came the winter of the great avalanche, when the snow buried every storehouse and the mountain took away exactly as Pella had said.\n\nOne by one, the hungry came to her door. The grasshopper, thin as a whisper. The beetle, who had mocked her loudest. Pella fed them all, though her own stores shrank to a crumb.\n\n"Why do you share?" asked the grasshopper, ashamed. "We laughed at you."\n\n"Because," said Pella, "I didn\'t carry twice my weight to be twice as safe. I carried it so there would be enough."\n\nSpring came. The insects rebuilt together, and this time every one of them carried a little extra — not from fear, but from Pella.\n\nThe mountain still provides, and still takes away. But the valley below it has never gone hungry since.'},
 {t:'In Praise of Maintenance',g:'essay',text:'We celebrate the inventor and forget the maintainer, the one who keeps the bridge standing long after the ribbon is cut.\n\nConsider the water engineer who walks the same mains every Tuesday for thirty years, listening for the leak that would flood a neighborhood. No statue will be raised. The reward is negative space: the disaster that didn\'t happen, the morning the taps ran clear.\n\nOur culture has a bias for beginnings. We fund the launch, not the upkeep; we applaud the groundbreaking, not the repointing of the bricks. Yet civilization is not a series of beginnings. It is maintenance, all the way down.\n\nThe librarian who mends the binding. The nurse who checks the chart at 2 a.m. The open-source contributor who patches the dependency nobody notices until it breaks. These are the load-bearing people.\n\nTo praise maintenance is not to diminish invention. It is to complete the story. Every bright new thing survives only because someone, somewhere, tends it in the dark.\n\nSo here is to the maintainers: may your checklists be short, your tools stay sharp, and may someone notice — just once — the quiet miracle of things continuing to work.'},
 {t:'Small Hours: Poems',g:'poetry-collection',text:'I. 3 A.M.\nThe refrigerator hums its one-note song.\nThe house has settled into its bones.\nSomewhere a truck changes gears on the highway —\nthe world\'s quietest parade, passing without me.\n\nII. LAUNDROMAT\nRows of portholes to small, warm oceans.\nSocks perform their slow ballet.\nA woman folds a fitted sheet perfectly —\nI have witnessed a miracle and paid $4.50.\n\nIII. FIRST SNOW\nIt doesn\'t fall. It considers.\nEach flake negotiates with the wind,\nlands like a decision made kindly.\nBy morning, the whole street has agreed\nto be beautiful for a while.\n\nIV. MAINTENANCE CLOSET\nMop, bucket, the smell of lemon and effort.\nSomeone keeps this building standing\none wrung-out mop at a time.\nI have never learned their name.\nTonight, I am grateful anyway.'},
 {t:'What the River Kept',g:'memoir',text:'My grandmother never learned to swim, which never stopped her from wading into the river every August with her skirt hitched up and her eyes closed.\n\n"It remembers," she\'d say, when I asked what she was doing. "Stand still long enough and it tells you."\n\nI thought it was one of her sayings, like "butter first, then jam" or "never trust a man who won\'t eat pie." It took me forty years to understand it was instructions.\n\nLast summer I went back to that river. I hitched up my trousers, closed my eyes, and stood still. The water moved around my ankles, cold and certain, and I felt it: the particular tug of that bend, where the current slows and drops what it carries.\n\nI opened my eyes and looked down. Half-buried in the silt: a marble, cats-eye, the exact one I\'d lost there at age nine and cried over for a week.\n\nThe river had kept it. All those years. Waiting for someone to stand still long enough to be told.\n\nI keep the marble on my desk now. When work feels urgent and meaningless, I hold it and remember: some things are only found by standing still.'}
];
function generate(seed,opts){
 opts=opts||{}; var s=prng(seed);
 var genre=opts.genre&&GENRES.indexOf(opts.genre)>=0?opts.genre:null;
 var pool=genre?WORKS.filter(function(w){return w.g===genre;}):WORKS;
 var w=pick(pool.length?pool:WORKS,s);
 var vol=seed;
 var title=w.t+' — Signature Audio Original, Ed. '+pad(vol);
 var words=w.text.split(/\s+/).length;
 var mins=Math.max(2,Math.round(words/150));
 var program='(function(){\n var text=document.getElementById("abk-text").innerText;\n var u=new SpeechSynthesisUtterance(text);\n u.rate=1; u.pitch=1;\n speechSynthesis.cancel(); speechSynthesis.speak(u);\n})();\n// Paste into a page containing the full text in #abk-text, or run the text through any TTS engine.\n// Estimated listening time: about '+mins+' minutes at conversational pace.';
 return {
  id:PREFIX+pad(seed),
  title:title,
  author:'Signature Audio Workshop',
  narrator:'Signature Ensemble (sample)',
  description:'A complete original short work, "'+w.t+'", presented as a Signature sample audiobook (Ed. '+vol+'). The FULL TEXT is included below — about '+words+' words, roughly '+mins+' minutes read aloud. A Signature-authored sample, clearly labeled, never presented as a harvested public-domain recording.',
  genre:w.g, type:'audiobook',
  chapters:['Complete work — single-sitting listen ('+mins+' min)'],
  full_text:w.text,
  word_count:words, estimated_minutes:mins,
  audio_note:'Sample audiobook — the complete text is the work itself; use the read-aloud demo program for audio.',
  license:'Signature sample — original work, property of Justin Addam Higgins',
  demo:{kind:'read-aloud',program:program,note:'Browser read-aloud program: speaks the full text via the Web Speech API. Runs as-is on any PC browser.'},
  src:'signature-generated-sample', _seed:seed
 };
}
function validate(r){
 var e=[];
 if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
 if(!/^JAH-ABK-\d{6}$/.test(r.id||''))e.push('id');
 if(typeof r.title!=='string'||r.title.length<8)e.push('title');
 if(typeof r.description!=='string'||r.description.length<60)e.push('description');
 if(GENRES.indexOf(r.genre)<0)e.push('genre');
 if(typeof r.full_text!=='string'||r.full_text.length<400)e.push('full_text');
 if(!r.demo||typeof r.demo.program!=='string')e.push('demo');
 if(r.src!=='signature-generated-sample')e.push('src');
 return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
 var dups=(sample||[]).filter(function(r){return r&&(r.t===record.title||r.title===record.title);});
 return dups.length?{ok:false,errors:['duplicate title in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-public-audiobooks-1.0',generate:generate,validate:validate,driftCheck:driftCheck,genres:GENRES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-audiobooks',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
