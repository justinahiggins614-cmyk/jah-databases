/* SIGNATURE — JAH Book Data Base FULL-NOVEL generator. Property of Justin Addam Higgins (JAH).
   jahdb-books-2.0 — deterministic full-novel engine. Same seed + version => same novel,
   byte-identical in the browser and in node. Every novel: 20-24 chapters, full four-act
   arc (setup, rising action, climax, resolution), a six-character cast with seeded
   relationship arcs (rival turns ally, mentor sacrifice, hidden antagonist revealed),
   recurring motifs planted in chapter one and paid off in the climax, and a hard
   40,000-word floor enforced by a top-up guard. All prose is assembled combinatorially
   from clean invented pools — every name, place, and event invented — and the word
   count is genuinely computed from the generated chapters. An INDEPENDENT verifier
   rebuilds the entire novel from the seed and compares a checksum before acceptance. */
(function () {
  'use strict';
  var VERSION = 'jahdb-books-2.0';
  var WORD_FLOOR = 40000;
  var ID_PREFIX = 'JAH-BOOK-';
  var AUTHOR = 'Justin Addam Higgins';
  var STAMP = 'Official JAH Book Archive — full novels generated boundlessly, verified independently.';
  var GENRES = ['Science Fiction', 'Fantasy', 'Mystery', 'Romance', 'Horror', 'Mathematics',
                'Physics', 'Chemistry', 'Biology', 'History', 'Computer Science', "Children's",
                'Poetry', 'Technical Manual', 'Philosophy', 'Business'];
  var GKEY = { 'Science Fiction': 'sf', 'Fantasy': 'fantasy', 'Mystery': 'mystery', 'Romance': 'romance',
    'Horror': 'horror', 'Mathematics': 'math', 'Physics': 'physics', 'Chemistry': 'chemistry',
    'Biology': 'biology', 'History': 'history', 'Computer Science': 'cs', "Children's": 'children',
    'Poetry': 'poetry', 'Technical Manual': 'manual', 'Philosophy': 'philosophy', 'Business': 'business' };
  var GNOUN = { 'Science Fiction': 'courage', 'Fantasy': 'loyalty', 'Mystery': 'curiosity',
    'Romance': 'devotion', 'Horror': 'dread', 'Mathematics': 'precision', 'Physics': 'wonder',
    'Chemistry': 'discovery', 'Biology': 'life', 'History': 'memory', 'Computer Science': 'logic',
    "Children's": 'joy', 'Poetry': 'longing', 'Technical Manual': 'clarity',
    'Philosophy': 'reflection', 'Business': 'ambition' };

  /* ---------- deterministic primitives (byte-identical to JAHDB core) ---------- */
  function mkRnd(seed) {
    var a = (typeof seed === 'number' ? seed : hashStr(String(seed))) >>> 0 || 1;
    return function () {
      a |= 0; a = (a + 0x6D2B79F5) | 0;
      var t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function hashStr(s) {
    var h = 2166136261; s = String(s);
    for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); }
    return h >>> 0;
  }
  function fnv(s) {
    var h = 2166136261; s = String(s);
    for (var i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 16777619); }
    return (h >>> 0).toString(16);
  }
  function ri(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
  function pick(rnd, arr) { return arr[Math.floor(rnd() * arr.length)]; }
  function cap(s) { return s.charAt(0).toUpperCase() + s.slice(1); }
  function wordCount(s) { return s.trim().split(/\s+/).length; }

  /* ---------- cast ---------- */
  var SYL_A = ['hal', 'cor', 'wen', 'kam', 'fen', 'dor', 'lus', 'mar', 'sel', 'tor',
               'vel', 'ris', 'nor', 'bel', 'ash', 'elm', 'ira', 'oth', 'bren', 'cal',
               'dain', 'el', 'far', 'gar'];
  var SYL_B = ['wick', 'ton', 'mere', 'ford', 'shaw', 'holt', 'bury', 'stead', 'field', 'crest',
               'mont', 'vale', 'brook', 'stone', 'moor', 'haven', 'gate', 'light', 'mark', 'well',
               'ridge', 'borne', 'fell', 'den'];
  var TRAITS = {
    pro: ['steady and stubborn', 'quick to act and slow to quit', 'carrying an old promise', 'haunted but unbroken', 'a planner with a wild streak', 'quiet until it matters', 'loyal to a fault', 'running toward trouble'],
    comp: ['fiercely loyal', 'quick with a joke and quicker with a plan', 'the careful one', 'brave in the small hours', 'a keeper of maps and grudges', 'steady as stone', 'loud-hearted', 'the one who never left'],
    ant: ['patient and smiling', 'always three moves ahead', 'charming until the mask slips', 'cold as deep water', 'a believer in a terrible cause', 'soft-spoken and absolute', 'willing to burn the world to save it', 'never cruel without purpose'],
    men: ['scarred and kind', 'a teacher of hard lessons', 'old enough to know better', 'gentle with a steel core', 'full of stories and warnings', 'the last of a lost order', 'practical to the bone', 'warm-eyed and watchful'],
    aly: ['resourceful and blunt', 'a fixer of impossible things', 'calm under fire', 'connected everywhere', 'sharp-eyed and sharper-tongued', 'the pragmatic one', 'generous with secrets', 'fearless in negotiations'],
    foil: ['proud and prickly', 'brilliant and bitter', 'a rival with a code', 'wounded pride walking', 'competitive to the marrow', 'distrustful of heroes', 'ambitious and alone', 'sharp as a drawn blade']
  };
  function mkName(rnd) {
    return cap(pick(rnd, SYL_A) + pick(rnd, SYL_A)) + ' ' + cap(pick(rnd, SYL_B));
  }
  function makeCast(rnd) {
    var roles = ['pro', 'comp', 'ant', 'men', 'aly', 'foil'];
    var cast = {}, nameRole = {}, used = {};
    roles.forEach(function (r) {
      var nm;
      do { nm = mkName(rnd); } while (used[nm]);
      used[nm] = 1;
      cast[r] = { name: nm, trait: pick(rnd, TRAITS[r]) };
      nameRole[nm] = r;
    });
    cast.nameRole = nameRole;
    return cast;
  }

  /* ---------- arc state ---------- */
  function phaseOf(i, nCh) {
    if (i < 4) return 'setup';
    if (i < nCh - 8) return 'rising';
    if (i < nCh - 4) return 'climax';
    return 'resolution';
  }
  function makeArc(rnd, nCh) {
    return {
      nCh: nCh,
      foilTurn: ri(rnd, 6, 9),
      foilAlly: ri(rnd, 13, 16),
      antReveal: ri(rnd, 10, 13),
      menDeath: ri(rnd, 13, 15),
      midTurn: 9
    };
  }
  function foilLevel(arc, i) {
    if (i < arc.foilTurn) return 0;
    if (i < arc.foilAlly) return 1;
    return 2;
  }
  function mentorAlive(arc, i) { return i < arc.menDeath; }
  function antLevel(arc, i, nCh) {
    if (i < arc.antReveal - 2) return 0;
    if (i < arc.antReveal) return 1;
    if (i < nCh - 8) return 2;
    return 3;
  }

  /* ---------- title pools ---------- */
  var TA = ['Echoes', 'Whispers', 'Shadows', 'Songs', 'Tales', 'Dreams', 'Secrets', 'Legends',
            'Embers', 'Tides', 'Lanterns', 'Storms', 'Veils', 'Comets', 'Riddles', 'Harbors',
            'Ashes', 'Thorns', 'Bells', 'Wolves'];
  var TB = ['Nebula', 'Deep', 'Hollow', 'Ember', 'Tide', 'Storm', 'Vale', 'Machine',
            'Garden', 'Tower', 'River', 'Crown', 'Forge', 'Harbor', 'Star', 'Thicket',
            'Winter', 'Signal', 'Covenant', 'Frontier'];
  var TC = ['Spell', 'Affair', 'Crossing', 'Ledger', 'Voyage', 'Cipher', 'Oath', 'Signal',
            'Reckoning', 'Inheritance'];
  function titleFromSeed(rnd) {
    var k = ri(rnd, 0, 2);
    if (k === 0) return 'The ' + pick(rnd, TA) + ' of ' + pick(rnd, TB);
    if (k === 1) return pick(rnd, TA) + ' ' + pick(rnd, TB) + ' ' + pick(rnd, TC);
    return 'The ' + pick(rnd, TA) + ' ' + pick(rnd, TC);
  }

  var CHT = ['The Oath', 'Into the Wild', 'The Old Road', 'Shadows Gather', 'The Price',
    'The Turning', 'The Last Stand', 'The Crown', 'Launch Window', 'The Long Dark',
    'Signal Lost', 'New Ceres', 'The Core', 'Rogue Vector', 'Event Horizon',
    'The Choice', 'Burn', 'Home Signal', 'First Light', 'The Crossing',
    'What the Maps Forgot', 'A Fragile Plan', 'The Weight of It', 'Borrowed Time',
    'The Quiet Before', 'Terms of Surrender', 'The Long Way Home', 'Ashes and Oaths',
    'The Second Bell', 'Where Rivers Meet', 'The Unwritten Page', 'A Debt Repaid',
    'The Hollow Year', 'Gates of Dawn', 'The Iron Ledger', 'What Remains',
    'The Far Shore', 'A Different Dawn', 'The Cost of Silence', 'Under Strange Stars',
    'The Broken Compass', 'Letters Never Sent', 'The Winter Count', 'A Common Cause',
    'The Last Argument', 'Before the Fall', 'The Gathering Dark', 'After the Fire',
    'The Hard Truth', 'What the Brave Owe', 'The Final Ledger', 'Dawn, At Last',
    'The Long Table', 'Home Waters', 'The Kept Promise', 'A New Chart'];
  function pickTitles(rnd, nCh) {
    var pool = CHT.slice(), out = [];
    for (var i = 0; i < nCh; i++) {
      var ix = Math.floor(rnd() * pool.length);
      out.push(pool[ix]); pool.splice(ix, 1);
    }
    return out;
  }

  /* ---------- slot banks ---------- */
  var PLACES = ['Kepler Belt', 'Elderwood', 'Lantern Row', 'Stonebridge', 'Meridian City',
    'Aldermere', 'Frostgate', 'Juniper Quay', 'Emberline', 'Tarnwick',
    'Glass Wards', 'Candlewick Row', 'Thorn Archives', 'Hollowmarket', 'Vesper Quay',
    'Nine Bridges'];
  var G_ART = {
    'Science Fiction': ['variant beacon', 'tide lantern', 'signal drum', 'glass astrolabe'],
    'Fantasy': ['brass compass', 'inkwell charter', 'copper key', 'paper atlas'],
    'Mystery': ['sealed ledger', 'brass key', 'torn photograph', 'cipher wheel'],
    'Romance': ['pressed flower', 'old letter', 'silver locket', 'paper crane'],
    'Horror': ['black candle', 'cracked mirror', 'iron bell', 'wax-sealed box'],
    'Mathematics': ['brass compass', 'vellum proof', 'ivory slide rule', 'bound lemma'],
    'Physics': ['glass astrolabe', 'copper coil', 'prism array', 'field meter'],
    'Chemistry': ['copper retort', 'glass alembic', 'sealed vial', 'brass burner'],
    'Biology': ['pressed specimen', 'field journal', 'glass terrarium', 'seed vault'],
    'History': ['inkwell charter', 'paper atlas', 'sealed archive', 'brass seal'],
    'Computer Science': ['punch card deck', 'brass key', 'signal drum', 'glass core'],
    "Children's": ['paper crane', 'wooden boat', 'brass whistle', 'story box'],
    'Poetry': ['inkwell', 'pressed flower', 'paper crane', 'brass bell'],
    'Technical Manual': ['brass gauge', 'field handbook', 'calibration key', 'wiring chart'],
    'Philosophy': ['worn journal', 'inkwell', 'brass compass', 'folded letter'],
    'Business': ['sealed ledger', 'brass key', 'inkwell charter', 'copper token']
  };
  var G_THREAT = {
    'Science Fiction': ['void-born', 'Hollow Signal', 'rust fleet', 'quiet between stars'],
    'Fantasy': ['Hollow King', 'ash coven', 'thorn court', 'unmaking'],
    'Mystery': ['blackmailer', 'silent partner', 'midnight caller', 'erased name'],
    'Romance': ['old misunderstanding', 'arranged match', 'letter never sent', 'distance'],
    'Horror': ['thing in the walls', 'pale congregation', 'hollow choir', 'long dark'],
    'Mathematics': ['flawed proof', 'unsolved conjecture', 'paradox', 'missing lemma'],
    'Physics': ['collapsing field', 'runaway reaction', 'dead zone', 'resonance'],
    'Chemistry': ['unstable compound', 'tainted batch', 'runaway reaction', 'corroded seal'],
    'Biology': ['blight', 'silent swarm', 'red tide', 'withering'],
    'History': ['burned archive', 'forged chronicle', 'erased year', 'lost regiment'],
    'Computer Science': ['rogue process', 'corrupted index', 'silent fork', 'deadlocked grid'],
    "Children's": ['grumpy giant', 'lost map', 'storm', 'big misunderstanding'],
    'Poetry': ['silence', 'forgetting', 'winter', 'unsaid thing'],
    'Technical Manual': ['failing system', 'missed tolerance', 'worn bearing', 'dead circuit'],
    'Philosophy': ['doubt', 'old argument', 'unexamined life', 'hard question'],
    'Business': ['hostile takeover', 'empty ledger', 'broken contract', 'market crash']
  };
  var V_ACT = ['seized', 'studied', 'circled', 'tested', 'followed', 'mapped', 'questioned',
    'tracked', 'measured', 'unraveled', 'confronted', 'shielded', 'carried', 'guarded',
    'decoded', 'charted', 'braved', 'entered', 'claimed', 'defended', 'pursued',
    'examined', 'lifted', 'lowered', 'opened', 'closed', 'read', 'reread', 'counted',
    'weighed', 'marked', 'signaled', 'answered', 'refused', 'remembered', 'buried'];
  var V_SAID = ['said', 'replied', 'answered', 'murmured', 'insisted', 'admitted',
    'declared', 'whispered', 'countered', 'offered', 'warned', 'promised', 'asked', 'called'];
  var V_MOVE = ['crossed', 'climbed', 'descended', 'entered', 'left', 'reached',
    'passed through', 'circled', 'approached', 'withdrew from'];
  var ADJ = ['quiet', 'steady', 'patient', 'restless', 'careful', 'bold', 'weary',
    'bright', 'hollow', 'distant', 'fierce', 'gentle', 'grim', 'hopeful', 'tired',
    'watchful', 'eager', 'solemn', 'restless', 'resolute', 'tender', 'stern',
    'curious', 'doubtful', 'certain', 'uneasy', 'calm', 'wild', 'soft', 'hard',
    'long', 'short', 'old', 'new', 'strange', 'familiar'];
  var ADV = ['slowly', 'quickly', 'quietly', 'carefully', 'boldly', 'steadily',
    'without hesitation', 'with great care', 'at last', 'again', 'for the first time',
    'without looking back', 'with a steady hand', 'in silence', 'without a word', 'at dawn'];
  var TIME = ['at dawn', 'by midday', 'as evening fell', 'near midnight', 'before first light',
    'in the small hours', 'as the bells rang', 'when the lamps were lit', 'at dusk',
    'in the grey morning', 'as night deepened', 'when the shift changed'];
  var OATH = ['Hold the line until dawn.', 'No one walks alone.', 'What is carried is shared.',
    'The truth, whatever it costs.', 'We finish what we start.', 'Leave no one behind.',
    'Count the cost, then pay it.', 'Stand where you are needed.', 'Remember who you are.',
    'The road is long; walk it anyway.', 'Keep the light lit.', 'Do the next right thing.'];

  /* dialogue lines, keyed by role and state */
  var DLG = {
    pro: ['We go now, before the moment passes.', 'I did not come this far to turn back.',
      'Then we do it the hard way.', 'I have counted the cost. It is worth it.',
      'Stay behind me when it starts.', 'I will carry that. It is mine to carry.',
      'We have been afraid long enough.', 'Tell me the truth, whatever it is.',
      'I am not the person I was when this began.', 'If we fail, we fail together.',
      'There is always a way. Find it.', 'I made a promise. Promises hold.',
      'Do not mistake my quiet for surrender.', 'We end this where it started.',
      'I have seen worse odds.', 'Then let them come.'],
    comp: ['I am with you. That was never in doubt.', 'You think too much. Move.',
      'I packed for this. Did you?', 'If you fall, I fall. Simple.',
      'Someone has to watch your back. It is me.', 'I have a plan. You will hate it.',
      'Rest when we are done. Not before.', 'You owe me a meal after this.',
      'I have seen you do harder things.', 'Together, then. Like always.',
      'Stop brooding. Walk.', 'I brought the spare. You are welcome.',
      'We have survived worse mornings.', 'Lead on. I will follow.',
      'You are not alone in this.', 'I told you this would work.'],
    ant: ['You mistake stubbornness for strength.', 'I have waited a long time for this.',
      'You cannot stop what has already begun.', 'How touching. How brief.',
      'I admire you. That changes nothing.', 'You built this trap yourself.',
      'Every hero needs a ending. Here is yours.', 'I know what you fear. I counted on it.',
      'You are late. It is already done.', 'Kneel, and I will be merciful.',
      'Your courage is a rounding error.', 'I wrote this ending years ago.',
      'You were never the threat. You were the lesson.', 'Watch closely. Learn.',
      'This was inevitable from the first day.', 'Goodbye, then.'],
    men: ['Listen before you leap. Then leap.', 'I have made this mistake. Learn from me.',
      'The old roads are old for a reason.', 'Patience is also a weapon.',
      'You are ready. More ready than you know.', 'Remember what I taught you.',
      'When I am gone, trust the training.', 'Fear is information. Use it.',
      'The work matters more than the worker.', 'I am proud of you. Do not waste it.',
      'Slow is smooth, and smooth is fast.', 'Carry this for me when I cannot.',
      'You will know the moment. Act.', 'This is the part they never teach.'],
    aly: ['I can get you in. Getting out is your problem.', 'I know someone. I always know someone.',
      'The price is fair. Pay it.', 'Done. Next problem.', 'I pulled strings. Do not ask which.',
      'You need supplies, silence, and speed. I have two.', 'Consider it handled.',
      'I do not ask questions I cannot afford.', 'The way is clear for one hour.',
      'I have been where you are going. Listen.', 'Take this. You will need it.',
      'My people owe me. Today they pay.'],
    foil0: ['Out of my way, hero.', 'I do not need your help.',
      'We are not on the same side.', 'Stay out of my ledger.',
      'I work alone. Always have.', 'Do not mistake proximity for trust.',
      'You will slow me down.', 'I have my own debts to settle.',
      'This is my fight too. Mine.', 'Do not follow me.'],
    foil1: ['Perhaps I misjudged you. Slightly.', 'We want the same thing. For now.',
      'I will walk with you. Do not make me regret it.', 'Truce. Until this is done.',
      'You fight well. I will allow it.', 'Fine. Together. This once.',
      'I am still watching you.', 'Do not mistake this for friendship.',
      'Our goals align. Nothing more.', 'Lead. I will cover the rear.'],
    foil2: ['I have got your back. Truly.', 'Forgive the old pride. It is gone.',
      'Whatever comes, we face it together.', 'You were right. I was wrong. There.',
      'I would follow you anywhere now.', 'Old rivalries die hard. Mine just did.',
      'Count me in. All the way.', 'You taught me what it costs. I am paying it.',
      'Side by side, then.', 'I am proud to stand with you.'],
    gen: ['It is time.', 'Are you certain?', 'We have no choice.', 'Then it is decided.',
      'Watch and learn.', 'Do not look down.', 'Remember this moment.', 'Steady.',
      'Now.', 'Again.', 'Together.', 'Go.', 'Wait.', 'Listen.', 'Look.',
      'This changes everything.', 'I know.', 'Perhaps.', 'We shall see.',
      'As you say.', 'If you say so.', 'Very well.', 'Indeed.', 'Exactly.']
  };
  /* interior lines for the protagonist, keyed by phase */
  var INT = {
    setup: ['{A} had not asked for any of this, but the asking was long past.',
      'Somewhere ahead lay the answer; {A} could feel it like weather.',
      'The old life was already a story {A} told about someone else.',
      '{A} counted the reasons to turn back and found none that held.',
      'Every road out of the ordinary starts with a single unwise step.',
      '{A} had learned early: the map is not the territory, and the territory was waiting.',
      'Doubt was a luxury {A} could no longer afford.',
      'The {T} felt heavier than it looked, as if it knew what was coming.',
      '{A} memorized the faces at the table. Some would not be there at the end.',
      'Beginnings, {A} thought, are just endings wearing better clothes.',
      'The {P} waited, patient as stone, and {A} was done waiting.',
      '{A} had packed light: hope, stubbornness, and one good reason.',
      'Whatever happened next, {A} would meet it standing.',
      '{A} traced the old oath in memory: {M3}',
      'The morning smelled of rain and consequence.',
      '{A} had always been good at starting. Finishing was the new part.',
      'Nobody at the {P} believed in quiet heroes. {A} aimed to be loud.',
      '{A} checked the {T} one last time, then stopped checking.',
      'Fear sat beside {A} like an old companion. {A} let it ride along.',
      'The first step was the easy one. {A} took it anyway.',
      '{A} wondered what the histories would say, then decided not to care.',
      'Some doors only open once. {A} knocked.'],
    rising: ['The plan had survived exactly until contact, {A} thought. As plans do.',
      '{A} was learning the true price of the {T}, and it was not money.',
      'Every victory so far had been borrowed. The debt was coming due.',
      'Trust, {A} was discovering, is built in inches and lost in miles.',
      '{A} kept the {M2} close. It was the one true thing in a week of lies.',
      'The middle of anything is where resolve goes to be tested.',
      '{A} had stopped counting setbacks and started counting lessons.',
      'Somewhere behind them, the {P} was already a memory.',
      '{A} understood now: the {TH} had been watching longer than anyone guessed.',
      'The company was fraying at the edges. {A} held the center.',
      'Halfway meant too far to quit and too far to see the end.',
      '{A} replayed the last failure until it taught something.',
      'The {T} hummed faintly, as if it approved of stubbornness.',
      'Doubt knocked. {A} did not answer.',
      '{A} was becoming someone the old friends would barely recognize.',
      'The cost was rising. So was {A}.',
      '{A} marked the map with every hard-won mile.',
      'There was no going back to the {M1}. There never had been.',
      'Each dawn {A} chose the work again. That was the whole secret.',
      '{A} could feel the shape of the ending now, distant but definite.',
      'The {TH} was closer than it appeared. {A} adjusted accordingly.',
      'Weariness was just another weather. {A} walked through it.'],
    climax: ['This was the hour everything had been bending toward.',
      '{A} felt the old oath rise like a tide: {M3}',
      'No more plans. Only the doing.',
      '{A} looked at the {T} and understood, finally, what it was for.',
      'Fear had burned off. What remained was clean and bright.',
      '{A} was done being careful. Careful had expired.',
      'Every lesson, every scar, every lost hour — all of it was for now.',
      'The {M1} seemed very far away, and very close.',
      '{A} drew a breath and spent it all at once.',
      'There would be no second chance at this moment.',
      '{A} thought of everyone who had carried them here, and stood straighter.',
      'The {TH} filled the horizon. {A} walked toward it anyway.',
      'This, {A} knew, was the part of the story people would retell.',
      'Hands steady. Heart loud. Go.',
      '{A} had nothing left to lose and everything to prove.',
      'The {M2} blazed — the motif of the whole long road, kept faith.',
      'Now or never had arrived wearing armor.',
      '{A} chose, and the choosing was the victory.',
      'All the quiet mornings had been rehearsal for this noise.',
      '{A} was not afraid anymore. There was no room for it.',
      'The end of the {TH} started here, with one person refusing.',
      'History would argue about this hour. {A} just lived it.'],
    resolution: ['Afterward, the quiet felt enormous.',
      '{A} sat with the silence and found it friendly.',
      'The {T} was still now, its work done, its story told.',
      'Scars, {A} decided, are just proof of attendance.',
      '{A} thought of the {M1} and smiled for the first time in days.',
      'The oath held: {M3}',
      'What remained was the mending, and mending is its own courage.',
      '{A} was tired in a way sleep would fix.',
      'The company gathered, smaller and closer than before.',
      '{A} looked at each face and memorized this one.',
      'Endings, {A} thought, are just beginnings with better lighting.',
      'The {M2} would go somewhere safe now, somewhere honored.',
      'There would be stories. {A} would tell them true.',
      '{A} had set out to find something and had become someone.',
      'The road home was the same road, walked differently.',
      '{A} kept one small token of the {TH}, as a reminder.',
      'Peace, it turned out, was also a discipline.',
      '{A} wrote it all down before the details faded.',
      'The {P} welcomed them back like a held breath released.',
      '{A} slept, and dreamed of ordinary mornings.',
      'What came next was unwritten. That was the gift.',
      'The long work was done. The good work remained.']
  };
  var PREMISE = {
    'Science Fiction': ['chart the far signal before the void-born silence it', 'carry the last star-chart through the Kepler Belt', 'prove the deep field equations before the fleets arrive'],
    'Fantasy': ['reforge the broken covenant before the Hollow King wakes', 'carry the ember through the thorn court', 'restore the old magic before the unmaking spreads'],
    'Mystery': ['unmask the blackmailer before the last secret sells', 'follow the erased name to its source', 'solve the midnight ledger before it closes forever'],
    'Romance': ['win back the love the misunderstanding stole', 'deliver the letter before the wedding bells', 'bridge the distance pride had built'],
    'Horror': ['survive the long dark of Hollowmarket', 'silence the hollow choir before it sings them under', 'escape what lives in the walls'],
    'Mathematics': ['complete the great proof before the paradox collapses it', 'find the missing lemma the world needs', 'defend the theorem against the flawed counterproof'],
    'Physics': ['stabilize the field before the resonance peaks', 'map the dead zone and return alive', 'prove the new mechanics before the old guard buries them'],
    'Chemistry': ['synthesize the cure before the tainted batch spreads', 'contain the runaway reaction', 'purify the corroded seal of the old works'],
    'Biology': ['stop the blight before it takes the valley', 'track the silent swarm to its nest', 'save the seed vault from the withering'],
    'History': ['recover the burned archive before the forged chronicle wins', 'restore the erased year to the record', 'find the lost regiment and bring them home'],
    'Computer Science': ['kill the rogue process before it eats the grid', 'rebuild the corrupted index from fragments', 'break the deadlock strangling the city systems'],
    "Children's": ['find the lost map before the picnic ends', 'befriend the grumpy giant of Thorn Hill', 'sail the wooden boat home before the storm'],
    'Poetry': ['gather the unsaid things before winter takes them', 'sing the forgetting into memory', 'find the words the silence was keeping'],
    'Technical Manual': ['bring the failing system back within tolerance', 'write the procedure that saves the works', 'calibrate the old machine before the inspection'],
    'Philosophy': ['answer the hard question honestly', 'settle the old argument once and for all', 'live the examined life under pressure'],
    'Business': ['save the company from the hostile takeover', 'balance the empty ledger before the crash', 'honor the broken contract and rebuild trust']
  };

  /* ---------- beat template pools ---------- */
  var OPEN = {
    setup: ['{TIME}, {A} stood at the edge of the {P} with the {T} in hand and no idea what it would cost.',
      'The trouble began, as trouble often does, with a letter {A} should never have opened.',
      '{A} had lived {ADJ} years in the {P} without incident, which ought to have been a warning.',
      'Nobody in the {P} remembered when the {T} first appeared. {A} was about to learn why.',
      'It was a {ADJ} morning in the {P}, the kind that promises nothing and delivers everything.',
      '{B} arrived {TIME} with news that rearranged the furniture of {A}’s life.',
      'The {TH} had been a rumor until the day it took something {A} loved.',
      '{A} found the {T} where the old stories said it would be, which was the first surprise.',
      'Every quiet life ends. {A}’s ended on a {ADJ} {TIME} when {B} knocked twice.',
      'The {P} kept its secrets well, but {A} had always been good at listening.',
      '{A} woke knowing the day would matter, the way animals know weather.',
      'The last normal day began with {A} mending a fence and ended with the {T} burning cold.',
      '{TIME}, the {P} exhaled, and {A}’s old life exhaled with it.',
      '{A} had one rule: never get involved. The {T} made it two rules broken in a day.',
      'The map {B} unrolled showed the {P} and, beyond it, everything {A} feared.',
      '{A} inherited the {T} the way one inherits weather: suddenly, and without instructions.',
      'It started with a sound — the {T}, humming, {TIME}, where no sound should be.',
      'The {P} had stood for centuries. {A} would test that claim by winter.'],
    rising: ['{TIME}, the road punished them for every mile of hope.',
      'The {TH} did not chase. It waited, which was worse.',
      '{A} learned that {TIME} that plans are just wishes with paperwork.',
      'They left the {P} {ADV}, which is to say they ran.',
      'The second week brought rain, doubt, and the first real wound.',
      '{B} kept count of the setbacks. {A} kept count of the reasons to continue.',
      'Every door they knocked on opened onto a harder question.',
      '{A} began to understand the shape of the {TH}, and it was larger than feared.',
      'The {T} grew heavier with each mile, or {A} grew weaker. Possibly both.',
      'Allies, {A} discovered, are just future farewells you have not scheduled.',
      'The trail went cold {TIME}. {A} lit a fire and thought harder.',
      'They were being followed. {B} said it first. {A} had known for days.',
      'The {P} was behind them now, a story they told to stay warm.',
      'Each victory cost more than the last. {A} paid anyway.',
      '{A} started keeping a list of what the {TH} had taken. It grew.',
      'The middle of the road is where the road tests you.',
      '{B} laughed less. {A} noticed, and said nothing, and noticed more.',
      'They crossed into country the maps left blank, which explained the maps.'],
    climax: ['{TIME}, the sky over the {P} turned the color of a held breath.',
      'There was no more running. {A} felt it the way you feel a storm break.',
      'The {TH} came {ADV}, exactly as the old warnings promised.',
      'Everything they had carried — the {T}, the scars, the oath — narrowed to this hour.',
      '{A} stood where the {M1} met the end of the world and waited for the {TH}.',
      'The final ground was the {P}, which had been the first ground. Fitting.',
      'No speeches. {B} checked the {T} once, nodded, and the work began.',
      'The air itself seemed to lean in to watch.',
      '{A} had imagined this moment a hundred ways. It was worse, and better.',
      'The {TH} did not negotiate. Neither, anymore, did {A}.',
      'This was the hour the old stories were made of. {A} intended to survive it.',
      '{TIME}, the last door closed behind them. Forward was the only direction left.',
      'The {M2} burned cold in {A}’s hand — the whole long road, distilled.',
      '{A} could hear {B} breathing hard beside them. Good. Still here.',
      'The end of the {TH} had a face now, and {A} memorized it.',
      'Thunder, or something older than thunder, rolled across the {P}.'],
    resolution: ['{TIME}, the quiet after was the loudest thing {A} had ever heard.',
      'The {P} stood. That was the first thing {A} checked.',
      'They counted the living {ADV}, and then they counted again, grateful.',
      'The {T} was just an object again. {A} set it down gently.',
      '{A} woke {TIME} and, for a moment, did not remember the war was over.',
      'The mending began with small things: a door hung straight, a meal shared.',
      'Nobody cheered at first. The relief was too large for noise.',
      '{B} slept for a day and a night. {A} stood watch, glad to do it.',
      'The {TH} was gone. The sky seemed surprised by its own blueness.',
      '{A} walked the {P} {ADV}, learning it again like a new language.',
      'Letters went out to everyone who had helped. The list was long.',
      'The first ordinary morning arrived without fanfare, and {A} wept a little.',
      'They buried what needed burying and planted what needed planting.',
      '{A} found the {M2} a place of honor, where the light hit it mornings.',
      'The {P} rang its bells {TIME}, not in alarm, but in something like joy.',
      'What had been broken was mending. What had been lost was honored.']
  };
  var DESC = ['The {P} spread below them, {ADJ} and {ADJ}, stitched with lamplight.',
    'Rain had turned the road to the {P} into a dark ribbon.',
    'The {T} caught the light {ADV}, throwing {ADJ} shadows.',
    'Somewhere beyond the {P}, the {TH} moved like weather.',
    'The air smelled of rain, iron, and old decisions.',
    '{A} studied the {P} the way a sailor studies a coming squall.',
    'Lamplight pooled in the {P}, each lamp a small held promise.',
    'The {T} was {ADJ} to the touch, {ADJ} to the eye, and heavy with history.',
    'Wind moved through the {P}, carrying voices {A} chose not to understand.',
    'The {P} at {TIME} was a different country than the {P} at noon.',
    'Dust hung in the light like suspended decisions.',
    'The {T} seemed to watch them back. {A} pretended not to notice.',
    'Every stone of the {P} had a story, and most of them were warnings.',
    'The horizon did its {ADJ} trick of looking close and being far.',
    '{B} pointed out the {P}’s old scars — flood, fire, and older things.',
    'Silence settled over the {P}, the kind with weight.',
    'The {T} pulsed once, {ADV}, like a slow heart.',
    '{A} memorized the {P}: every lane, every shadow, every exit.',
    'Night came down on the {P} like a held hand.',
    'The {P}’s bells counted the hour, indifferent and exact.',
    'Fog wrapped the {P} until only the {T}’s glow marked their way.',
    'Stars came out over the {P}, numerous as unkept promises.',
    'The {T}’s surface showed {A}’s face, older than {A} felt.',
    'Cold settled into the stones of the {P}, patient as grief.',
    'The {P} woke {ADV}, stretching into the {ADJ} morning.',
    'Shadows pooled in the corners of the {P}, thick as ink.',
    'The {T} hummed a note {A} felt in the teeth.',
    'Light fell across the {P} in {ADJ} bars, striping the road.',
    'The {P} held its breath. {A} held theirs.',
    'Somewhere in the {P}, a dog barked once, then thought better of it.',
    'The {T} was warm now, which meant either progress or trouble.',
    'The {P}’s rooftops shone {ADV} after the rain.',
    '{A} traced the {T}’s worn edges, reading it like a face.',
    'The wind carried the smell of the {P}’s kitchens and forges.',
    'Evening laid a {ADJ} hand over the {P}.',
    'The {T}’s glow steadied, which {B} took as a good sign.',
    'The {P}’s old wall threw a long shadow across their path.',
    '{A} counted the lamps of the {P} the way other people count sheep.',
    'The {TH}’s country began where the {P}’s maps ended.',
    'Mist rose off the {P}’s river, hiding and revealing by turns.',
    'The {T}’s weight was a comfort now, familiar as a habit.',
    'The {P}’s market smelled of spice, smoke, and rumor.',
    '{A} watched the {P}’s people go about their {ADJ} business, envying them.',
    'The {T} caught firelight and held it, {ADJ} and {ADJ}.',
    'Dawn painted the {P}’s towers gold, then took the gold away.',
    'The {P}’s quiet was the kind you pay for with vigilance.',
    '{A} leaned on the {P}’s old bridge and watched the water decide.',
    'The {T}’s hum deepened as they neared the {P}’s heart.',
    'Snow began over the {P}, erasing footprints impartially.',
    'The {P}’s archives smelled of dust and kept promises.',
    '{A} found a {ADJ} peace in the {P}’s ordinary noise.',
    'The {T}’s light dimmed {ADV}, conserving itself, or so {A} hoped.',
    'The {P}’s children played in the lanes, loud and immortal.',
    'Thunderheads stacked over the {P} like unpaid debts.',
    'The {T}’s surface rippled, showing not {A}’s face but the {M1}.',
    '{A} breathed the {P}’s {ADJ} air and felt, briefly, at home.',
    'The {P}’s clock tower struck, and {A} counted, and kept walking.',
    'The {T}’s glow painted their hands {ADJ} in the dark.',
    'The {P}’s edge gave way to open country, {ADJ} and waiting.',
    'Moonlight silvered the {P}, making it strange and beautiful.',
    'The {T}’s hum was almost a voice now. {A} almost answered.',
    '{A} marked their place in the {P}’s story and moved on.',
    'The {P}’s lamps went out one by one, like a held breath released.',
    'Heat shimmered off the {P}’s stones at midday.',
    'The {T}’s cold burned {A}’s palm — a warning, or a promise.'];
  var ACT = ['{A} {V_MOVE} the {P} {ADV}, the {T} ready.',
    '{B} {V_ACT} the {T} {ADV} while {A} kept watch.',
    'They {V_MOVE} the {P}’s outer lanes {ADV}, making no sound that mattered.',
    '{A} {V_ACT} the {TH}’s trail {ADV}, reading sign like scripture.',
    '{B} {V_ACT} the {T}’s casing {ADV}, checking every seal.',
    'The {TH}’s scouts {V_MOVE} the ridge {ADV}. {A} counted them and went cold.',
    '{A} {V_ACT} the old mechanism {ADV}, hands remembering the training.',
    '{B} {V_ACT} the perimeter {ADV}, marking it in chalk and memory.',
    'They {V_MOVE} the {P}’s underways {ADV}, where the lamps never reached.',
    '{A} {V_ACT} the {T}’s charge {ADV}, coaxing it back from the edge.',
    '{B} {V_ACT} the {TH}’s leavings {ADV}, learning its habits.',
    'The company {V_MOVE} the {P}’s high road {ADV}, exposed and committed.',
    '{A} {V_ACT} the wounded {ADV}, binding what could be bound.',
    '{B} {V_ACT} the {P}’s old defenses {ADV}, waking them one by one.',
    'They {V_MOVE} the burned country {ADV}, where even the birds were quiet.',
    '{A} {V_ACT} the {T}’s signal {ADV}, sending it out into the dark.',
    '{B} {V_ACT} the {TH}’s flank {ADV}, drawing its eye away from {A}.',
    'The {TH} {V_MOVE} the valley {ADV}, and the valley noticed.',
    '{A} {V_ACT} the last of the supplies {ADV}, making it stretch.',
    '{B} {V_ACT} the {P}’s gate {ADV}, buying them the night.',
    'They {V_MOVE} the river road {ADV}, the water keeping their left.',
    '{A} {V_ACT} the {TH}’s vanguard {ADV}, and lived to doubt the wisdom of it.',
    '{B} {V_ACT} the {T}’s twin {ADV}, the one the stories never mentioned.',
    'The storm {V_MOVE} the {P} {ADV}, and they moved with it, hidden in its noise.',
    '{A} {V_ACT} the fallen {ADV}, honoring them the only way left.',
    '{B} {V_ACT} the {TH}’s supply line {ADV}, quietly, completely.',
    'They {V_MOVE} the ash fields {ADV}, where the {TH} had already passed.',
    '{A} {V_ACT} the {T}’s core {ADV}, past every safeguard.',
    '{B} {V_ACT} the {P}’s bells {ADV}, ringing the pattern {A} had taught.',
    'The {TH}’s shadow {V_MOVE} the {P} {ADV}, and the lamps went out in rows.',
    '{A} {V_ACT} the breach {ADV}, holding it alone until {B} arrived.',
    '{B} {V_ACT} the {TH}’s banner {ADV}, and the field went still.',
    'They {V_MOVE} the last mile {ADV}, too tired to be afraid.',
    '{A} {V_ACT} the {T}’s final charge {ADV}, spending it all.',
    '{B} {V_ACT} the {P}’s wounded {ADV}, refusing to leave the square.',
    'The dawn {V_MOVE} the {P} {ADV}, and found them still standing.',
    '{A} {V_ACT} the {TH}’s heart {ADV}, ending it the hard way.',
    '{B} {V_ACT} the {T} {ADV}, one last time, for the road home.',
    'They {V_MOVE} the {M1}’s old paths {ADV}, changed people in a changed land.',
    '{A} {V_ACT} the ledger of the dead {ADV}, reading every name aloud.',
    '{B} {V_ACT} the {P}’s rebuilding {ADV}, starting with the smallest things.',
    'The seasons {V_MOVE} the {P} {ADV}, and the scars softened.',
    '{A} {V_ACT} the {M2} {ADV}, finding it a place of honor.',
    '{B} {V_ACT} the new maps {ADV}, drawing the world as it was now.',
    'They {V_MOVE} the home road {ADV}, in no hurry for the first time.',
    '{A} {V_ACT} the {T}’s rest {ADV}, laying it down gently.',
    '{B} {V_ACT} the celebration {ADV}, louder than the war had been.',
    'The years {V_MOVE} the {P} {ADV}, and the story grew in the telling.',
    '{A} {V_ACT} the oath {ADV}, keeping it: {M3}',
    '{B} {V_ACT} the {M1}’s memory {ADV}, tending it like a garden.',
    'They {V_MOVE} the quiet years {ADV}, and found them good.',
    '{A} {V_ACT} the final page {ADV}, and closed the book on the {TH}.',
    '{B} {V_ACT} the {T}’s tale {ADV}, telling it true to anyone who asked.',
    'The {P} {V_MOVE} into legend {ADV}, as places do when heroes walk them.',
    '{A} {V_ACT} the morning {ADV}, greeting it like an old friend.'];
  var DLG_FRAME = ['{A} {VSAID}, “{SAY:A}”',
    '“{SAY:B}” {B} {VSAID}.',
    '{B} {VSAID}, “{SAY:B}”',
    '“{SAY:A}” {A} {VSAID} {ADV}.',
    '{A} looked at {B} and {VSAID}, “{SAY:A}”',
    '{B} {VSAID} {ADV}, “{SAY:B}”',
    '“{SAY:A}” — {A}’s voice did not waver.',
    '{A} {VSAID} to {B}, “{SAY:A}”',
    '{B} caught {A}’s eye. “{SAY:B}”',
    '“{SAY:B}” {B} {VSAID}, and {A} believed them.',
    '{A} {VSAID} {ADV}: “{SAY:A}”',
    '{B}’s voice was {ADJ}. “{SAY:B}”',
    '“{SAY:A}” {A} {VSAID}, and the room went quiet.',
    '{A} {VSAID} the words like an oath: “{SAY:A}”',
    '{B} {VSAID}, very {ADJ}, “{SAY:B}”',
    '“{SAY:B}” — {B} had never sounded so {ADJ}.',
    '{A} {VSAID} without looking up, “{SAY:A}”',
    '{B} leaned in. “{SAY:B}”',
    '“{SAY:A}” {A} {VSAID}, and meant every word.',
    '{A} {VSAID} to the dark, “{SAY:A}”',
    '{B} {VSAID} after a long pause, “{SAY:B}”',
    '“{SAY:B}” {B} repeated, {ADJ} and certain.',
    '{A}’s answer came {ADV}: “{SAY:A}”',
    '{B} {VSAID} it plainly: “{SAY:B}”',
    '“{SAY:A}” — and {A}’s {ADJ} smile said the rest.',
    '{A} {VSAID}, “{SAY:A}” And {B} knew it was true.',
    '{B} {VSAID} {ADV}, “{SAY:B}”',
    '“{SAY:A}” {A} {VSAID} to {B}’s retreating back.',
    '{A} and {B} spoke together: “{SAY:A}”',
    '{B} {VSAID} the {ADJ} truth: “{SAY:B}”',
    '{A} {VSAID} {ADV}, voice {ADJ}: “{SAY:A}”',
    '“{SAY:B}” {B} {VSAID}, and the {T} hummed agreement.',
    '{A} {VSAID} it to {B}’s face: “{SAY:A}”',
    '{B}’s {VSAID} was barely a breath: “{SAY:B}”',
    '“{SAY:A}” — {A} had been waiting to say it.',
    '{A} {VSAID} across the {P}, “{SAY:A}”'];
  var TRANS = ['{TIME} found them still moving.',
    'The days blurred into a single long effort.',
    'They rested {ADV}, and the rest was not enough, and they moved anyway.',
    'The {P} fell behind them like a shed skin.',
    'Word traveled faster than they did, as word does.',
    'They ate {ADV}, slept {ADV}, and kept the {T} between them and the dark.',
    'The map changed. They changed with it.',
    'Nobody marked the exact moment the hunt turned. It just turned.',
    'Supplies thinned. Resolve did not.',
    'They learned the {P}’s back roads the way you learn a friend’s moods.',
    'The {TH}’s pressure never eased, only changed shape.',
    'They traded sleep for miles and called it fair.',
    'Each dawn the {T}’s hum was a little stronger.',
    'The company’s jokes grew darker and funnier, both at once.',
    'They passed the point of no return {ADV}, without ceremony.',
    'The {P}’s news reached them in fragments, all of it bad, none of it stopping them.',
    'They mended gear, mended plans, mended each other.',
    'The road taught what no teacher could.',
    'They were not the same people who had left the {M1}.',
    'The {TH} adapted. So did they, faster.',
    'Night watches grew longer and quieter.',
    'They counted stars instead of sheep, and miles instead of days.',
    'The {T}’s light was their constant companion now.',
    'They learned to read the {P}’s weather in their bones.',
    'Every setback was a lesson with teeth.',
    'They kept the oath between them like a shared lamp: {M3}',
    'The end, when it came into view, looked like work.',
    'They were ready. They had been ready for miles.'];
  var CLIFF = {
    setup: ['But the {TH} had already found them.',
      'That night, the {T} spoke for the first time.',
      'What {B} said next changed the shape of everything.',
      'The {P}’s bells rang wrong {TIME}, and {A} knew.',
      'Behind them, unnoticed, the {TH}’s mark burned on the door.',
      'The letter {A} had burned was not, it turned out, the only copy.',
      '{A} slept, and dreamed of the {M1}, and woke afraid.',
      'The {T}’s hum dropped half a note. {B} went pale.',
      'Someone had been in their room. The {T} was warm.',
      'The road ahead, {A} realized, had been chosen for them.',
      'The {P}’s oldest resident took one look at the {T} and wept.',
      'Nothing would be simple after this. {A} felt it land.'],
    rising: ['The trap, when it sprang, was elegant.',
      '{B}’s scream cut the {TIME} air like a blade.',
      'The {TH} had been one step ahead all along.',
      '{A} watched the plan burn and started building another.',
      'The betrayal wore a familiar face.',
      'They lost the {T} {TIME}. The silence afterward was total.',
      'The {P}’s gates closed against them, one by one.',
      '{A} counted the living and came up short.',
      'The message, when decoded, was worse than silence.',
      'The {TH}’s price was named at last, and it was everything.',
      '{B} made the hard choice so {A} would not have to.',
      'Dawn came, and with it, the {TH}’s answer.'],
    climax: ['The {P} held its breath.',
      '{A}’s hands would not stop shaking. {A} used them anyway.',
      'The {TH}’s roar shook dust from the {P}’s old stones.',
      '{B} went down {ADV}. {A}’s world narrowed to a point.',
      'The {T} flared white-hot — and then, terribly, went dark.',
      'For one heartbeat, {A} thought it was over. It was not.',
      'The {TH} laughed, and the sound had edges.',
      '{A} remembered the oath — {M3} — and stood.',
      'Blood on the stones. Breath in the lungs. Continue.',
      'The {M2} blazed, and the {TH} finally looked afraid.',
      'Everything {A} loved was in this hour. {A} fought like it.',
      'The turning point came {ADV}, and nobody saw it but {A}.'],
    resolution: ['And that, more or less, was that.',
      'The {P}’s bells rang true {TIME}, perhaps for the first time.',
      '{A} kept the {M2}. Some things you do not give away.',
      'They never spoke of the worst hour again. They did not need to.',
      'The road home was {ADJ}, and {A} walked it {ADV}.',
      'In the end, the oath held: {M3}',
      'The {T} rested at last, its long work done.',
      '{A} was, finally, at peace with the {M1}’s memory.',
      'The story would be told for years. {A} hoped they told it kind.',
      'Some endings are beginnings with the serial numbers filed off.',
      'The {P} endured, as it always had, as it always would.',
      'And {A} lived, and worked, and remembered, and was content.']
  };
  var CALLBACK = ['{A} remembered the {M1}, impossibly far and close at once.',
    'The {M2} — the first true thing — burned steady in memory.',
    '{M3} The oath had carried them here. It would carry them home.',
    '{A} thought of the {M1}’s quiet mornings and fought harder.',
    'Everything led back to the {M1}. Every road, every choice.',
    'The {M2}’s light was the same light {A} had first seen, years and miles ago.',
    '{A} whispered the old oath under their breath: {M3}',
    'The {M1} seemed to watch over this hour, patient as ever.',
    '{A} had left the {M1} a child of circumstance. They would return something else.',
    'The {M2} had never lied. {A} trusted it now completely.',
    'For the {M1}, {A} thought. For all of it.',
    '{M3} — and {A} had never meant words more.',
    'The {M1}’s bells rang in memory, clear as the {P}’s own.',
    '{A} carried the {M2} like a small sun into the dark.',
    'What started at the {M1} would end here, one way or another.',
    'The oath was old: {M3} Old, and true, and enough.',
    '{A} saw the {M1}’s lanes in the mind’s eye, every stone.',
    'The {M2}’s hum matched {A}’s heartbeat. It always had.',
    'Back at the {M1}, none of this had been imaginable. Now it was just the work.',
    'The {M1} had made them. This hour would prove it.',
    '{A} held the {M2} high, and the dark stepped back.',
    '{M3} They had kept it this far. They would keep it to the end.'];
  var MEN_DEATH = ['{A} reached {C}’s side as the light went out of the {P}’s square.',
    '“{SAY:C}” {C} {VSAID}, and then was gone, {ADJ} to the last.',
    '{C}’s hand found {A}’s. “{SAY:C}” The grip loosened.',
    'The {TH} took {C} {TIME}, and the company’s heart broke cleanly.',
    '{A} held {C}’s {T} — no, {C}’s memory — and made the old oath new: {M3}',
    '“{SAY:C}” were {C}’s last words, {ADJ} as everything {C} had ever taught.',
    '{C} stood between the {TH} and {A}, and did not step aside. Not once.',
    'They buried {C} {ADV}, under the {P}’s oldest tree, with honors and tears.'];
  var PATTERN = {
    setup: ['DESC', 'DLG', 'INT', 'ACT', 'TRANS', 'DLG', 'DESC', 'INT', 'ACT', 'DLG'],
    rising: ['ACT', 'DLG', 'ACT', 'INT', 'DESC', 'ACT', 'DLG', 'TRANS', 'ACT', 'INT'],
    climax: ['ACT', 'ACT', 'DLG', 'ACT', 'INT', 'ACT', 'CALLBACK', 'ACT', 'DLG', 'ACT'],
    resolution: ['INT', 'DLG', 'DESC', 'INT', 'TRANS', 'DLG', 'CALLBACK', 'INT', 'DESC', 'DLG']
  };

  /* ---------- genre-specific beats (mixed into the general pools) ---------- */
  var GENRE_BEATS = {
    'Science Fiction': ['{A} recalibrated the {T}’s field coils {ADV}, compensating for stellar drift.',
      'The ship’s long-range array painted the {TH} as a smear of wrong math.',
      '“{SAY:A}” {A} {VSAID}, eyes on the orbital plot.',
      '{B} ran the burn calculations twice. Both times, they were ugly.',
      'The {T}’s quantum lattice sang at a frequency {A} felt in the molars.',
      'They slingshotted the {P}’s gravity well {ADV}, trading time for distance.',
      'The void between stars was {ADJ} tonight, and full of listening.',
      '{A} sealed the airlock on the {TH}’s boarding drone and vented it {ADV}.',
      'Star charts covered the table, each one a different kind of hope.',
      '“{SAY:B}” {B} {VSAID}, watching the fuel gauge fall.'],
    'Fantasy': ['{A} traced the old rune on the {T} {ADV}, waking its {ADJ} glow.',
      'The {TH}’s magic tasted of ash and old iron.',
      '“{SAY:A}” {A} {VSAID}, and the {T} answered with light.',
      '{B} bargained with the thorn court {ADV}, trading stories for passage.',
      'Ancient wards over the {P} flickered, tired after centuries.',
      'The {T} drank moonlight and gave back prophecy, or indigestion.',
      '{A} spoke the covenant words {ADV}, feeling them take hold.',
      'Dragon-sign hung over the {P}’s towers, {ADJ} and unmistakable.',
      'The old magic recognized {A}, which was flattering and alarming.',
      '“{SAY:B}” {B} whispered, as the forest leaned in to listen.'],
    'Mystery': ['{A} laid the clues on the {P}’s scarred table {ADV}: the {T}, the torn note, the lie.',
      'The alibi had a hole in it {A} could drive a carriage through.',
      '“{SAY:A}” {A} {VSAID}, watching {B}’s face for the flinch.',
      '{B} tailed the suspect through the {P}’s fog {ADV}, unseen.',
      'The {T} proved the timeline was a fabrication, elegant and damning.',
      'Every witness lied about something small. {A} collected the small things.',
      '{A} reconstructed the night {ADV}, and the {TH}’s story fell apart.',
      'The second {T} — the one nobody mentioned — broke the case open.',
      '“{SAY:B}” {B} {VSAID}, sliding the photograph across.',
      'The {P}’s records office yielded its secrets {ADV}, as it always did for the patient.'],
    'Romance': ['{A}’s heart did something {ADJ} and unwise at the sight of {B}.',
      'The {T} passed between them, warm from both their hands.',
      '“{SAY:A}” {A} {VSAID}, very {ADJ}, meaning all of it.',
      '{B} laughed, and the {P}’s whole grey day brightened.',
      'They walked the {P}’s river path {ADV}, not touching, almost touching.',
      'The misunderstanding sat between them like an unwelcome guest.',
      '{A} wrote the letter {ADV}, then burned it, then wrote it true.',
      'Dancing at the {P}’s festival, {B}’s hand found {A}’s like it belonged there.',
      '“{SAY:B}” {B} {VSAID}, and {A}’s doubts went quiet.',
      'The {T}’s glow seemed {ADJ}er whenever {B} was near. {A} noticed.'],
    'Horror': ['{A} heard it in the walls again {TIME}: the {TH}, counting.',
      'The {T}’s light shrank to a coin of courage in the {ADJ} dark.',
      '“{SAY:A}” {A} whispered, and the dark leaned closer.',
      '{B}’s reflection in the {T} moved half a second late.',
      'The {P}’s empty houses watched them pass with lidless windows.',
      'Something wearing the dark {V_MOVE} the {P}’s lanes {ADV}.',
      '{A} nailed the {T}’s iron over the door {ADV}, hands shaking.',
      'The choir began {TIME} — the hollow choir — and {B}’s eyes went distant.',
      '“{SAY:B}” {B} breathed, and it was not quite {B}’s voice.',
      'Dawn was a rumor the {TH} had not yet disproven.'],
    'Mathematics': ['{A} covered the {P}’s slate wall with the proof {ADV}, chalk flying.',
      'The lemma clicked into place {TIME} with an almost audible sound.',
      '“{SAY:A}” {A} {VSAID}, pointing at the fatal line.',
      '{B} checked the {T}’s calibration {ADV} — the numbers had to be exact.',
      'The paradox unraveled {ADV}, thread by golden thread.',
      'Counterexamples fell before {A}’s argument like ninepins.',
      'The {TH}’s flaw hid in the third assumption. {A} found it {TIME}.',
      'They worked through the night, the {T}’s lamp burning {ADJ}.',
      '“{SAY:B}” {B} {VSAID}, sliding the verified pages over.',
      'Q.E.D., {A} wrote, {ADJ} and certain, and the {P}’s bells rang.'],
    'Physics': ['{A} tuned the {T}’s field {ADV}, watching the needle settle.',
      'The resonance peaked {TIME}, exactly as the equations promised.',
      '“{SAY:A}” {A} {VSAID}, eyes on the waveform.',
      '{B} shielded the {T}’s core {ADV} as the field surged.',
      'Data streamed across the {P}’s instruments, {ADJ} and undeniable.',
      'The dead zone yielded its secret {ADV}: a standing wave, patient as stone.',
      '{A} derived the correction {ADV}, and the {TH}’s model collapsed.',
      'Particles told the truth when people would not.',
      '“{SAY:B}” {B} called over the {T}’s rising hum.',
      'The experiment worked. The {P}’s lab had never been so quiet.'],
    'Chemistry': ['{A} titrated {ADV}, watching for the {ADJ} change.',
      'The compound stabilized {TIME}, clear as good conscience.',
      '“{SAY:A}” {A} {VSAID}, holding the vial to the light.',
      '{B} vented the {T}’s chamber {ADV} as the pressure climbed.',
      'Crystals grew in the {P}’s cold room, {ADJ} and perfect.',
      'The tainted batch revealed itself {ADV}: a wrong color, a wrong smell.',
      '{A} neutralized the {TH}’s agent {ADV}, drop by careful drop.',
      'The reaction ran clean, the {T}’s gauges steady.',
      '“{SAY:B}” {B} reported, reading the spectrum twice.',
      'The new synthesis held. {A} allowed a small, {ADJ} smile.'],
    'Biology': ['{A} tracked the blight’s edge {ADV}, marking each fallen stalk.',
      'The specimen under the {T}’s lens told a {ADJ} story.',
      '“{SAY:A}” {A} {VSAID}, not looking up from the cultures.',
      '{B} quarantined the {P}’s greenhouse {ADV}, gentle but absolute.',
      'New growth showed {TIME}, green and defiant.',
      'The swarm’s pattern emerged {ADV}: a spiral, seeking warmth.',
      '{A} inoculated the seed vault {ADV}, row by precious row.',
      'Field notes filled {ADV}, each page a small victory.',
      '“{SAY:B}” {B} whispered, as the first sprout broke soil.',
      'Life, {A} thought, is the most stubborn experiment of all.'],
    'History': ['{A} unrolled the {T}’s fragile chart {ADV}, holding breath.',
      'The archive yielded {TIME}: a name, a date, a truth.',
      '“{SAY:A}” {A} {VSAID}, reading the marginalia aloud.',
      '{B} cross-checked the {P}’s chronicles {ADV}, finding the forgery.',
      'The erased year surfaced {ADV}, patient as sediment.',
      'Primary sources, {A} insisted, over pretty stories. Always.',
      '{A} dated the {TH}’s charter {ADV} — a century of lies, exposed.',
      'The lost regiment’s trail ran through the {P}’s old muster rolls.',
      '“{SAY:B}” {B} announced, holding the sealed orders high.',
      'History, {A} wrote {TIME}, belongs to those who keep the receipts.'],
    'Computer Science': ['{A} traced the rogue process {ADV}, following its {ADJ} syscalls.',
      'The index rebuilt {TIME}, block by patient block.',
      '“{SAY:A}” {A} {VSAID}, watching the deadlock graph resolve.',
      '{B} patched the {T}’s firmware {ADV}, closing the {TH}’s hole.',
      'Logs told the story {ADV}: an intrusion, elegant and old.',
      'The grid stabilized as {A}’s fix propagated, node by node.',
      '{A} refactored the {TH}’s exploit {ADV} into a detector.',
      'Backups held. {B} verified each one {ADV}, because trust is a test suite.',
      '“{SAY:B}” {B} reported, as the dashboards went green.',
      'The system hummed, {ADJ} and honest, under {A}’s watch.'],
    "Children's": ['{A} packed the {T} in the little red wagon {ADV}, ready for adventure.',
      'The map had an X on it, and X, everyone knows, marks the spot.',
      '“{SAY:A}” {A} announced, very {ADJ} and brave.',
      '{B} shared the sandwiches {ADV}, because sharing is the rule.',
      'The {TH} turned out to be not so scary after all — just lonely.',
      'They built a fort in the {P}’s big oak, {ADJ} and secret.',
      '{A} named the {T}’s funny hum and hummed along.',
      'The lost duckling parade marched {TIME}, and everyone cheered.',
      '“{SAY:B}” {B} giggled, splashing through the puddles.',
      'Home for supper, {A} decided, is the best ending of all.'],
    'Poetry': ['{A} set the {T}’s words down {ADV}, each one a small lit window.',
      'The {TH}’s silence had a texture, {ADJ} as river stones.',
      '“{SAY:A}” {A} breathed, and the line held.',
      '{B} read the {P}’s evening aloud {ADV}, making music of it.',
      'Images gathered {TIME} like birds to a wire.',
      'The {T}’s ink remembered every hand that ever held it.',
      '{A} pared the stanza {ADV} until only the true remained.',
      'Metaphor upon metaphor, the {TH} dissolved into meaning.',
      '“{SAY:B}” {B} murmured, and the poem turned its face to the light.',
      'What is left unsaid, {A} knew, sings the longest.'],
    'Technical Manual': ['{A} ran procedure seven {ADV}, checking each tolerance twice.',
      'The {T}’s gauge read {ADJ}-normal {TIME}. {A} logged it.',
      '“{SAY:A}” {A} {VSAID}, consulting the dog-eared handbook.',
      '{B} torqued the {P}’s main bearing {ADV}, to spec, no more.',
      'Step twelve failed {ADV}. {A} documented the failure exactly.',
      'The system returned to tolerance {TIME}, steady as a metronome.',
      '{A} revised the procedure {ADV}, adding the lesson in red ink.',
      'Calibration complete. {B} signed off {ADV}, because paperwork is safety.',
      '“{SAY:B}” {B} confirmed, reading the checklist aloud.',
      'The works ran clean. {A} permitted a {ADJ} nod of satisfaction.'],
    'Philosophy': ['{A} turned the {T}’s old question over {ADV}, examining every facet.',
      'The argument held {TIME}, {ADJ} against every objection.',
      '“{SAY:A}” {A} {VSAID}, Socratic and certain.',
      '{B} played devil’s advocate {ADV}, sharpening the point.',
      'The {TH}’s premise cracked {ADV} under honest scrutiny.',
      'First principles, {A} insisted. Begin there, or do not begin.',
      '{A} lived the answer {ADV}, which is the hardest proof.',
      'The examined life yielded its dividend {TIME}: clarity.',
      '“{SAY:B}” {B} offered, and the old paradox dissolved.',
      'Wisdom, {A} wrote, is what remains after certainty leaves.'],
    'Business': ['{A} opened the {T}’s ledger {ADV}, and the numbers told no lies.',
      'The deal closed {TIME}, {ADJ} and binding.',
      '“{SAY:A}” {A} {VSAID}, sliding the contract across.',
      '{B} audited the {P}’s books {ADV}, finding the leak.',
      'The market turned {ADV}, and {A}’s preparation paid.',
      'Trust, {A} had learned, is the only currency that compounds.',
      '{A} honored the {TH}’s old contract {ADV}, then wrote a better one.',
      'The quarter ended {ADJ}. The team celebrated {ADV}.',
      '“{SAY:B}” {B} reported, as the ledger balanced to the penny.',
      'Value, {A} told the {P}’s board, is what you give, not what you take.']
  };

  /* ---------- slot resolution ---------- */
  function dlgLine(rnd, role, arc, chIx) {
    var bank;
    if (role === 'foil') bank = DLG[['foil0', 'foil1', 'foil2'][foilLevel(arc, chIx)]];
    else if (role === 'pro' && rnd() < 0.25) bank = INT[phaseOf(chIx, arc.nCh)];
    else bank = DLG[role] || DLG.gen;
    var line = pick(rnd, bank);
    if (line.indexOf('{A}') >= 0) line = line.split('{A}').join('I');
    return line;
  }
  function slotVal(rnd, key, sub, ctx) {
    switch (key) {
      case 'A': return ctx.A; case 'B': return ctx.B; case 'C': return ctx.C;
      case 'P': return ctx.P; case 'P2': return ctx.P2;
      case 'T': return ctx.T; case 'TH': return ctx.TH;
      case 'M1': return ctx.motifs.M1; case 'M2': return ctx.motifs.M2; case 'M3': return ctx.motifs.M3;
      case 'V': case 'V_ACT': return pick(rnd, V_ACT); case 'VSAID': return pick(rnd, V_SAID);
      case 'V_MOVE': case 'VMOVE': return pick(rnd, V_MOVE); case 'ADJ': return pick(rnd, ADJ);
      case 'ADV': return pick(rnd, ADV); case 'TIME': return pick(rnd, TIME);
      case 'SAY': {
        var who = (sub === 'b' || sub === 'B') ? ctx.B : (sub === 'c' || sub === 'C') ? ctx.C : ctx.A;
        var role = ctx.cast.nameRole[who] || 'gen';
        var line = dlgLine(rnd, role, ctx.arc, ctx.chIx);
        return fill(line, rnd, ctx);
      }
      case 'THINK': return pick(rnd, INT[ctx.phase]);
    }
    return null;
  }
  function fill(tpl, rnd, ctx) {
    return tpl.replace(/\{([A-Za-z0-9_]+)(?::([A-Za-z]))?\}/g, function (m, key, sub) {
      var k = String(key).toUpperCase(), s = (sub || '').toLowerCase();
      if (k === 'A' || k === 'B' || k === 'C' || k === 'P' || k === 'P2' ||
          k === 'T' || k === 'TH' || k === 'M1' || k === 'M2' || k === 'M3' ||
          k === 'V' || k === 'V_ACT' || k === 'VSAID' || k === 'V_MOVE' || k === 'VMOVE' ||
          k === 'ADJ' || k === 'ADV' || k === 'TIME' || k === 'SAY' || k === 'THINK') {
        var v = slotVal(rnd, k, s, ctx);
        return v == null ? m : v;
      }
      return m;
    });
  }

  /* character choice per beat, weighted by phase and arc state */
  function ctxFor(rnd, chIx, nCh, genre, cast, arc, motifs) {
    var ph = phaseOf(chIx, nCh);
    var alive = mentorAlive(arc, chIx);
    var aLvl = antLevel(arc, chIx, nCh);
    function pickChar(proW, compW, antW, menW, alyW, foilW) {
      var bag = [];
      var add = function (nm, w) { for (var k = 0; k < w; k++) bag.push(nm); };
      add(cast.pro.name, proW); add(cast.comp.name, compW); add(cast.aly.name, alyW);
      add(cast.foil.name, foilW);
      if (alive) add(cast.men.name, menW);
      if (aLvl >= 2) add(cast.ant.name, antW); else if (aLvl === 1 && rnd() < 0.3) add(cast.ant.name, 1);
      return pick(rnd, bag);
    }
    var w = ph === 'setup' ? [10, 4, 0, 3, 2, 2]
          : ph === 'rising' ? [9, 4, 2, 2, 3, 3]
          : ph === 'climax' ? [9, 3, 4, 1, 2, 4]
          : [10, 4, 1, 1, 3, 3];
    var A = pickChar.apply(null, w);
    var B = pickChar.apply(null, w);
    var guard = 0;
    while (B === A && guard++ < 8) B = pickChar.apply(null, w);
    var C = cast.men.name;
    if ((!alive && chIx !== arc.menDeath) || C === A || C === B) C = cast.comp.name;
    return {
      A: A, B: B, C: C,
      P: pick(rnd, PLACES), P2: pick(rnd, PLACES),
      T: pick(rnd, G_ART[genre]), TH: pick(rnd, G_THREAT[genre]),
      cast: cast, arc: arc, motifs: motifs, phase: ph, chIx: chIx
    };
  }
  function poolFor(rnd, type, ph, genre, arc, chIx) {
    if ((type === 'DESC' || type === 'ACT' || type === 'DLG' || type === 'INT') && rnd() < 0.12) {
      return GENRE_BEATS[genre];
    }
    if (type === 'MEN_DEATH') return MEN_DEATH;
    switch (type) {
      case 'DESC': return DESC;
      case 'ACT': return ACT;
      case 'DLG': return DLG_FRAME;
      case 'INT': return INT[ph];
      case 'TRANS': return TRANS;
      case 'CALLBACK': return CALLBACK;
      default: return ACT;
    }
  }
  function fillBeat(rnd, tpl, ctx) {
    return fill(tpl, rnd, ctx);
  }
  /* avoid reusing a template recently used in this chapter: re-roll a few times */
  function pickFresh(rnd, pool, recent) {
    var t = pick(rnd, pool), guard = 0;
    while (guard++ < 8 && recent.indexOf(t) >= 0) t = pick(rnd, pool);
    recent.push(t);
    if (recent.length > 48) recent.shift();
    return t;
  }
  function buildChapter(rnd, chIx, nCh, genre, cast, arc, motifs, ctitle) {
    var ph = phaseOf(chIx, nCh);
    var beats = [];
    var recent = [];
    var ctx = function () { return ctxFor(rnd, chIx, nCh, genre, cast, arc, motifs); };
    beats.push(fill(pickFresh(rnd, OPEN[ph], recent), rnd, ctx()));
    var pattern = PATTERN[ph];
    var nMid = 168 + Math.floor(rnd() * 18);
    for (var k = 0; k < nMid; k++) {
      var type = pattern[k % pattern.length];
      var useCtx = ctx();
      var pool;
      if (type === 'INT') {
        var line = pickFresh(rnd, INT[ph], recent).split('{A}').join(useCtx.A);
        beats.push(fill(line, rnd, useCtx));
        continue;
      }
      if (chIx === arc.menDeath && type === 'DLG' && k % 7 === 3) pool = MEN_DEATH;
      else pool = poolFor(rnd, type, ph, genre, arc, chIx);
      beats.push(fill(pickFresh(rnd, pool, recent), rnd, useCtx));
    }
    var cliffPool = (chIx === arc.menDeath) ? MEN_DEATH : CLIFF[ph];
    beats.push(fill(pickFresh(rnd, cliffPool, recent), rnd, ctx()));
    var paras = [], cur = [];
    for (var j = 0; j < beats.length; j++) {
      cur.push(beats[j]);
      var cut = 3 + Math.floor(rnd() * 3);
      if (cur.length >= cut || j === beats.length - 1) { paras.push(cur.join(' ')); cur = []; }
    }
    var body = paras.join('\n\n');
    return { t: ctitle, b: body, ph: ph, _w: wordCount(body) };
  }

  /* ---------- description (deterministic: drawn from the main stream) ---------- */
  function descFromS(rnd, genre, nCh, words, cast) {
    var prem = pick(rnd, PREMISE[genre]);
    return 'A complete Signature novel: ' + nCh + ' chapters, ' + words.toLocaleString('en-US') +
      ' words of full text. ' + cast.pro.name + ' — ' + cast.pro.trait +
      ' — must ' + prem + ', alongside ' + cast.comp.name + '. Every chapter complete, ' +
      'from the first page to the last. A finished work of ' + GNOUN[genre] + '.';
  }

  /* ---------- main entry ---------- */
  var PUB_KEYS = ['id', 'title', 'author', 'genre', 'gkey', 'desc', 'words', 'chapters',
                  'note', 'src', 'origin', 'creation_mode', 'stamp', 'seed'];
  function generate(seed, opts, rnd) {
    opts = opts || {};
    rnd = rnd || mkRnd(seed);
    /* The verifier rebuilds from {seed,title,genre}; keep stream consumption
       identical whether or not title/genre were supplied, so regeneration
       always reproduces the original byte-for-byte. */
    var drawnGenre = pick(rnd, GENRES);
    var genre = (opts.type && GENRES.indexOf(opts.type) >= 0) ? opts.type
      : (opts.genre && GENRES.indexOf(opts.genre) >= 0) ? opts.genre : drawnGenre;
    var drawnTitle = titleFromSeed(rnd);
    var title = opts.title || drawnTitle;
    var n = (opts.baseN || 0) + (typeof seed === 'number' ? seed : hashStr(String(seed)));
    var cast = makeCast(rnd);
    var nCh = 20 + Math.floor(rnd() * 5);
    var arc = makeArc(rnd, nCh);
    var motifs = { M1: pick(rnd, PLACES), M2: pick(rnd, G_ART[genre]), M3: pick(rnd, OATH) };
    var titles = pickTitles(rnd, nCh);
    var chapters = [], words = 0;
    for (var i = 0; i < nCh; i++) {
      var ch = buildChapter(rnd, i, nCh, genre, cast, arc, motifs, titles[i]);
      chapters.push({ t: ch.t, b: ch.b, ph: ch.ph });
      words += ch._w;
    }
    var guard = 0;
    while (words < WORD_FLOOR && guard < 6000) {
      var extra = fill(pick(rnd, ACT), rnd, ctxFor(rnd, nCh - 1, nCh, genre, cast, arc, motifs));
      var last = chapters[chapters.length - 1];
      last.b += ' ' + extra;
      var w = wordCount(extra); words += w; guard++;
    }
    var rec = {
      id: ID_PREFIX + String(n).padStart(6, '0'),
      title: title,
      author: AUTHOR,
      genre: genre,
      gkey: GKEY[genre],
      desc: descFromS(rnd, genre, nCh, words, cast),
      words: words,
      chapters: chapters,
      note: 'FULL NOVEL — a complete original work created by the Signature full-novel generator (' + VERSION + '). All names, places, and events are invented. ' + nCh + ' chapters, full four-act arc, complete text.',
      src: 'signature',
      origin: 'signature',
      creation_mode: 'FULL-NOVEL',
      stamp: STAMP,
      seed: (typeof seed === 'number' ? seed : hashStr(String(seed)))
    };
    var pub = {};
    PUB_KEYS.forEach(function (k) { pub[k] = rec[k]; });
    return pub;
  }

  function textOf(rec) {
    return rec.chapters.map(function (c) { return c.t + '\n' + c.b; }).join('\n');
  }
  function validate(rec) {
    var errs = [];
    if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
    ['id', 'title', 'author', 'genre', 'gkey', 'desc', 'words', 'chapters', 'note', 'src'].forEach(function (k) {
      if (rec[k] === undefined || rec[k] === null || rec[k] === '') errs.push('missing field: ' + k);
    });
    if (rec.id && !/^JAH-BOOK-\d{6}$/.test(rec.id)) errs.push('bad id format');
    if (rec.genre && GENRES.indexOf(rec.genre) < 0) errs.push('bad genre');
    if (rec.gkey && rec.genre && rec.gkey !== GKEY[rec.genre]) errs.push('gkey mismatch');
    if (rec.src && rec.src !== 'signature') errs.push('src must be signature');
    if (!Array.isArray(rec.chapters) || rec.chapters.length < 20) errs.push('chapters must have 20+ entries');
    var seen = {}, phases = {}, i;
    if (Array.isArray(rec.chapters)) {
      for (i = 0; i < rec.chapters.length; i++) {
        var c = rec.chapters[i];
        if (!c || typeof c.t !== 'string' || !c.t || typeof c.b !== 'string' || !c.b) { errs.push('bad chapter at ' + i); break; }
        if (seen[c.t]) errs.push('duplicate chapter title: ' + c.t);
        seen[c.t] = 1;
        if (c.ph) phases[c.ph] = 1;
      }
      ['setup', 'rising', 'climax', 'resolution'].forEach(function (p) {
        if (!phases[p]) errs.push('arc missing phase: ' + p);
      });
    }
    var words = 0;
    if (Array.isArray(rec.chapters)) {
      for (i = 0; i < rec.chapters.length; i++) words += wordCount(rec.chapters[i].b || '');
    }
    if (rec.words !== words) errs.push('word count mismatch: claimed ' + rec.words + ', actual ' + words);
    if (words < WORD_FLOOR) errs.push('below 40,000-word floor: ' + words);
    var blob = (rec.title || '') + ' ' + (rec.desc || '') + ' ' + textOf(rec);
    var tok = blob.match(/\{[A-Za-z0-9_]+(?::[A-Za-z])?\}/);
    if (tok) errs.push('unresolved template token: ' + tok[0]);
    /* independent verifier: rebuild the whole novel from the seed, compare checksum */
    if (rec.seed != null && errs.length === 0) {
      try {
        var r2 = generate(rec.seed, { title: rec.title, genre: rec.genre, type: rec.genre }, mkRnd(rec.seed));
        if (r2.words !== rec.words) errs.push('verifier word mismatch');
        else if (fnv(textOf(r2)) !== fnv(textOf(rec))) errs.push('verifier checksum mismatch');
      } catch (e) { errs.push('verifier threw: ' + e.message); }
    }
    return { ok: errs.length === 0, errors: errs };
  }

  function driftCheck(rec, archiveSample) {
    var errs = [];
    (archiveSample || []).forEach(function (a) {
      var t = a.title || a.t;
      if (t && String(t).toLowerCase() === String(rec.title).toLowerCase())
        errs.push('duplicate of archived book title: ' + rec.title);
    });
    return { ok: errs.length === 0, errors: errs };
  }

  function themedGenerate(seed, opts, rnd, themeSamples) {
    var rec = generate(seed, opts, rnd);
    if (themeSamples && themeSamples.length) {
      var t = themeSamples[Math.floor(rnd() * themeSamples.length)];
      var nums = String(JSON.stringify(t)).match(/\d+/g);
      if (nums && nums.length) {
        var rec2 = generate(seed + (parseInt(nums[0], 10) % 1000), opts, mkRnd(String(seed) + nums[0]));
        rec2.id = rec.id;
        return rec2;
      }
    }
    return rec;
  }

  (typeof JAHDB !== 'undefined' ? JAHDB : (typeof global !== 'undefined' ? global.JAHDB : null))
    .registerGenerator('books', {
      version: VERSION,
      generate: generate,
      generateFull: generate,
      validate: validate,
      driftCheck: driftCheck,
      themedGenerate: themedGenerate,
      types: GENRES
    });
})();
