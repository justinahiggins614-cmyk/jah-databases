(function(){'use strict';
/* JAH The General Knowledge Quiz Database generator — jahdb-quiz-general-knowledge-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-QZGK-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "General Knowledge Quiz: Easy World Capitals - Foundations",
  "General Knowledge Quiz: Animal Kingdom Basics - Foundations",
  "General Knowledge Quiz: Colors, Shapes and First Numbers - Foundations",
  "General Knowledge Quiz: Days, Months and Seasons - Foundations",
  "General Knowledge Quiz: Easy Arithmetic - Foundations",
  "General Knowledge Quiz: Famous Landmarks - Foundations",
  "General Knowledge Quiz: Food and Fruit Facts - Foundations",
  "General Knowledge Quiz: The Human Body Basics - Foundations",
  "General Knowledge Quiz: Sports Basics - Foundations",
  "General Knowledge Quiz: Music Basics - Foundations",
  "General Knowledge Quiz: Continents and Oceans - Foundations",
  "General Knowledge Quiz: Space Basics - Foundations",
  "General Knowledge Quiz: World Capitals Challenge - Foundations",
  "General Knowledge Quiz: History Milestones - Foundations",
  "General Knowledge Quiz: Everyday Science - Foundations",
  "General Knowledge Quiz: Riddles and Wordplay Starter Set - Foundations"
 ],
 "Compounded": [
  "General Knowledge Quiz: Literature Basics - Compounded",
  "General Knowledge Quiz: Rivers, Mountains and Deserts - Compounded",
  "General Knowledge Quiz: Inventions and Inventors - Compounded",
  "General Knowledge Quiz: Flags and Nations - Compounded",
  "General Knowledge Quiz: The Living World - Compounded",
  "General Knowledge Quiz: Art and Artists - Compounded",
  "General Knowledge Quiz: Logic Puzzles - Compounded",
  "General Knowledge Quiz: Math Word Problems - Compounded",
  "General Knowledge Quiz: History Dates and Events - Compounded",
  "General Knowledge Quiz: Chemistry and Physics - Compounded"
 ],
 "Advanced": [
  "General Knowledge Quiz: Geography Mixed Challenge - Advanced",
  "General Knowledge Quiz: Wordplay Masters - Advanced",
  "General Knowledge Quiz: Literature Quotes and Authors - Advanced",
  "General Knowledge Quiz: Technology and Computers - Advanced",
  "General Knowledge Quiz: Advanced General Knowledge - Advanced",
  "General Knowledge Quiz: Lateral Thinking Masters - Advanced",
  "General Knowledge Quiz: Science The Deep Dive - Advanced",
  "General Knowledge Quiz: The Ultimate General Knowledge Final - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# General Knowledge Quiz — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — quiz record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A quiz record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"quiz-runner-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-quiz-general-knowledge-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('quiz-general-knowledge',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;

/* Group-0 expansion: 30 archive records (infinite-quiz / knowledge-showdown / universal-quiz-creator). */
TOPICS["Advanced"].push("The Endless Question Engine - Advanced", "Seeded Randomness, Fair Quizzes - Advanced", "Difficulty Ladders That Never End - Advanced", "Topic Weaving: Mixing Subjects - Advanced", "The Question Bank as a Living Archive - Advanced", "Anti-Repetition: Never the Same Quiz Twice - Advanced", "Adaptive Quizzes That Read the Player - Advanced", "Generating Wrong Answers That Teach - Advanced", "Timed Rounds and Streak Scoring - Advanced", "Quiz Generation for Classrooms - Advanced");
TOPICS["Compounded"].push("Head-to-Head Quiz Formats - Compounded", "Buzzer Rounds and Reaction Play - Compounded", "Team Showdown Strategy - Compounded", "The Final Wager Round - Compounded", "Sudden-Death Tiebreakers - Compounded", "Audience Play-Along Rounds - Compounded", "Category Draft: Picking Your Battles - Compounded", "Comeback Mechanics - Compounded", "Showdown Hosting: The Quizmaster’s Craft - Compounded", "Scoring Systems Compared - Compounded");
TOPICS["Foundations"].push("Designing Your First Quiz - Foundations", "Writing Unambiguous Questions - Foundations", "Balancing Easy, Medium and Hard - Foundations", "Answer Keys That Can’t Be Argued With - Foundations", "Themed Quiz Nights (Vol. 2) - Foundations", "Picture and Audio Rounds (Vol. 2) - Foundations", "Quizzes for Kids - Foundations", "Pub Quiz Architecture - Foundations", "Testing Your Quiz Before Game Night - Foundations", "Sharing and Remixing Quizzes - Foundations");
var ARCHIVE_BANK=[
{"g":"infinite-quiz","title":"The Endless Question Engine","description":"How a quiz generator produces fresh questions forever without repeating itself. The engine combines a topic model, a difficulty ladder, and a memory of every question it has already asked.","key_points":["An infinite quiz is a loop: pick topic, pick difficulty, instantiate, deduplicate.", "Deduplication memory is what makes it feel infinite rather than repetitive.", "Difficulty ladders keep long sessions engaging instead of flat.", "Templates plus fresh facts beat pure randomness for question quality.", "The engine should log every question it emits for later review."]},
{"g":"infinite-quiz","title":"Seeded Randomness, Fair Quizzes","description":"Why deterministic seeds make generated quizzes fair, replayable, and debuggable. The same seed always deals the same quiz, so disputes can be settled and sessions replayed.","key_points":["A seed is a promise: same seed, same quiz, every time.", "Tournament play should publish seeds so results are auditable.", "Seeded generation turns bug reports into reproducible cases.", "Rotate seeds between sessions so players cannot memorize sequences."]},
{"g":"infinite-quiz","title":"Difficulty Ladders That Never End","description":"Designing difficulty as an open-ended ladder so an infinite quiz can keep challenging experts. Each rung adds a new kind of thinking, not just harder facts.","key_points":["Difficulty is kinds of thinking, not just obscure facts.", "Each rung should name the thinking skill it tests.", "Open-ended ladders add rungs instead of capping out.", "Players should see which rung they are on."]},
{"g":"infinite-quiz","title":"Topic Weaving: Mixing Subjects","description":"How to blend subjects inside one quiz so players stay alert. Weaving geography into history into science keeps the brain switching gears.","key_points":["Alternating subjects keeps attention high across long sessions.", "A short topic memory prevents accidental clustering.", "Related-subject pairs test deeper understanding than isolated facts.", "Weave density is tunable: gentle alternation or aggressive mixing."]},
{"g":"infinite-quiz","title":"The Question Bank as a Living Archive","description":"Treating the question bank as an archive that grows, gets pruned, and improves. Every generated question is a record with lineage.","key_points":["Every question carries lineage: seed, template, date.", "Usage statistics separate strong questions from weak ones.", "Retirement is healthy: banks improve by pruning.", "Variants of strong questions multiply value cheaply."]},
{"g":"infinite-quiz","title":"Anti-Repetition: Never the Same Quiz Twice","description":"Techniques that keep generated quizzes feeling fresh across hundreds of sessions. Repetition is the silent killer of quiz apps.","key_points":["Fingerprints let the generator recognize repeats without storing full text.", "Per-player history personalizes the freshness guarantee.", "Template parameter space must exceed plausible lifetime play.", "Graceful fallback: when the space is exhausted, say so honestly."]},
{"g":"infinite-quiz","title":"Adaptive Quizzes That Read the Player","description":"How an infinite quiz adjusts difficulty to the player in real time. Get one right and the next gets harder; stumble and it eases off.","key_points":["Adaptation keeps every player in the productive struggle zone.", "Skill estimates must update fast enough to feel responsive.", "The target rung sits just above demonstrated skill.", "Show players their estimated level to motivate climbing."]},
{"g":"infinite-quiz","title":"Generating Wrong Answers That Teach","description":"The craft of writing distractors — wrong answers that reveal misconceptions instead of just being wrong. Good distractors make a quiz educational.","key_points":["Distractors should diagnose, not just deceive.", "Tie every distractor to one named misconception.", "Feedback on a wrong pick is the real lesson.", "Plausible but fair: tempting, never tricky."]},
{"g":"infinite-quiz","title":"Timed Rounds and Streak Scoring","description":"Designing time pressure and streak bonuses for generated quizzes. Speed adds excitement; streaks reward consistency.","key_points":["Time bonuses reward confident knowledge, not guessing.", "Streak multipliers make consistency pay.", "Round length should fit the question difficulty.", "Leaderboards need identical timing rules to be fair."]},
{"g":"infinite-quiz","title":"Quiz Generation for Classrooms","description":"Using infinite quiz generators as teaching tools. Teachers get endless practice sets tuned to the week’s lesson.","key_points":["Seeded sets let teachers replay and share exact quizzes.", "Topic selection ties generation to the curriculum.", "Class analytics turn quiz results into teaching insight.", "Low-stakes practice mode encourages repetition."]},
{"g":"knowledge-showdown","title":"Head-to-Head Quiz Formats","description":"The classic duel: two players, one question set, fastest correct answer wins. Formats compared, from buzzer duels to alternating turns.","key_points":["Buzzer duels reward speed plus knowledge.", "Alternating turns reward depth without speed pressure.", "Simultaneous answers reward consistency.", "Format choice changes which player wins — choose deliberately."]},
{"g":"knowledge-showdown","title":"Buzzer Rounds and Reaction Play","description":"The anatomy of a buzzer round: reading speed, anticipation, and the courage to buzz. Reaction play is a skill you can train.","key_points":["Buzzing on partial information is high-risk, high-reward.", "Lockout rules punish reckless buzzing.", "Recovery drills stop one miss from becoming five.", "Reading speed matters as much as knowledge."]},
{"g":"knowledge-showdown","title":"Team Showdown Strategy","description":"How teams win quiz showdowns: role assignment, conferring rules, and playing to each member’s strengths.","key_points":["Role assignment beats raw knowledge.", "Budget conferring time by question value.", "Route each question to the owning specialist.", "A designated guesser breaks ties fast."]},
{"g":"knowledge-showdown","title":"The Final Wager Round","description":"The dramatic finish: players wager points on one last question. Strategy, psychology, and math collide in the wager round.","key_points":["Wagers turn a points lead into a strategic position.", "Leaders protect; trailers attack — the math differs.", "Secret wagers add psychology to the arithmetic.", "The final question must be genuinely hard."]},
{"g":"knowledge-showdown","title":"Sudden-Death Tiebreakers","description":"When scores tie, sudden death decides. Designing tiebreakers that are fast, fair, and dramatic.","key_points":["Matched pairs keep tiebreaks fair.", "Escalating difficulty ends ties fast.", "Alternate answers so neither player gets an easier slot.", "Spare pairs prevent dead air."]},
{"g":"knowledge-showdown","title":"Audience Play-Along Rounds","description":"Letting the crowd play along turns spectators into participants. Play-along rounds fill the gaps between head-to-head battles.","key_points":["Play-along converts dead time into engagement.", "Separate audience scoring keeps the main duel clean.", "Simple response mechanics beat fancy ones.", "Recognize the top audience player."]},
{"g":"knowledge-showdown","title":"Category Draft: Picking Your Battles","description":"Before the showdown, players draft the categories they will face. Drafting adds strategy before a single question is asked.","key_points":["Drafting lets players shape the battlefield.", "Snake order balances pick advantage.", "Category bans remove feel-bad subjects.", "The draft is theater — play it up."]},
{"g":"knowledge-showdown","title":"Comeback Mechanics","description":"Rules that keep losing players in the game: multipliers, steal rounds, and the mercy rule done right. A showdown needs hope.","key_points":["Trailing players need a path back or they check out.", "High-value rounds must be earned or scheduled, not gifted.", "Bounded hope: comebacks possible, early leads still matter.", "Announce comeback rounds in advance for drama."]},
{"g":"knowledge-showdown","title":"Showdown Hosting: The Quizmaster’s Craft","description":"The host makes the showdown: pacing, rulings, and theater. A great quizmaster is part referee, part performer.","key_points":["Pace is everything: brisk, never rushed.", "Identical reads keep questions fair.", "Published ruling standards settle disputes fast.", "Neutral narration keeps trust."]},
{"g":"knowledge-showdown","title":"Scoring Systems Compared","description":"Points, Elo, handicaps: how showdown scoring shapes behavior. The scoring system is the game beneath the game.","key_points":["Scoring shapes strategy as much as questions do.", "Elo rewards strength of opposition.", "Handicaps enable mixed-skill play.", "Publish the system before the season."]},
{"g":"universal-quiz-creator","title":"Designing Your First Quiz","description":"A complete walkthrough for creating your first quiz from scratch: theme, questions, answers, and game-night flow.","key_points":["One theme, one audience: focus beats sprawl.", "Twelve questions across three bands is the starter sweet spot.", "Always include a tiebreaker.", "Testing on two people catches most flaws."]},
{"g":"universal-quiz-creator","title":"Writing Unambiguous Questions","description":"The core skill of quiz creation: questions with exactly one defensible answer. Ambiguity is the enemy of fun.","key_points":["One question, one defensible answer.", "Specify granularity: city, country, or person.", "Pin the frame: according to which standard.", "Hunt loopholes like your cleverest player."]},
{"g":"universal-quiz-creator","title":"Balancing Easy, Medium and Hard","description":"How to distribute difficulty so every player gets moments of glory. A well-balanced quiz has a ramp, not a wall.","key_points":["Easy openers build confidence and momentum.", "The medium middle is where games are won.", "Hard closers create legends.", "30-50-20 is the starter balance."]},
{"g":"universal-quiz-creator","title":"Answer Keys That Can’t Be Argued With","description":"Building answer keys that settle disputes before they start: accepted variants, sources, and ruling notes.","key_points":["Accept all reasonable variants of each answer.", "Cite sources for contested facts.", "Ruling notes preempt the tricky disputes.", "A key should settle arguments in thirty seconds."]},
{"g":"universal-quiz-creator","title":"Themed Quiz Nights (Vol. 2)","description":"Designing a whole evening around one theme: movies, decades, science, or pure chaos. Themes turn quizzes into events.","key_points":["Deep-bench themes sustain a full evening.", "Theme the round types, not just the questions.", "Light decoration plus themed snacks beat heavy production.", "A themed prize makes winning memorable."]},
{"g":"universal-quiz-creator","title":"Picture and Audio Rounds (Vol. 2)","description":"Beyond text: identifying faces, places, songs, and sounds. Multimedia rounds wake up different kinds of memory.","key_points":["Pictures test visual memory that text cannot.", "Five-second audio clips are the sweet spot.", "Test all playback before game night.", "Always have a no-tech backup round."]},
{"g":"universal-quiz-creator","title":"Quizzes for Kids","description":"Writing quizzes children love: short, visual, encouraging, and sneakily educational.","key_points":["Short rounds match young attention spans.", "Movement answers burn energy and build memory.", "Celebrate loudly; correct gently.", "Team scores protect young feelings."]},
{"g":"universal-quiz-creator","title":"Pub Quiz Architecture","description":"The anatomy of a great pub quiz: rounds, pacing, and the economics of a Tuesday night.","key_points":["Six by eight across ninety minutes is the classic shape.", "Score between rounds to keep flow.", "Variety rounds break up the text.", "A season leaderboard builds regulars."]},
{"g":"universal-quiz-creator","title":"Testing Your Quiz Before Game Night","description":"Playtesting: the unglamorous step that separates good quizzes from great ones. Test, fix, then host with confidence.","key_points":["Two test players catch most flaws.", "Time the test under real conditions.", "Hesitations mark questions to fix.", "Cut the weakest two questions."]},
{"g":"universal-quiz-creator","title":"Sharing and Remixing Quizzes","description":"How quizzes travel: licensing your questions, sharing sets, and remixing others’ work with credit.","key_points":["Clear licensing lets quizzes travel.", "Credit the original author on remixes.", "Note your changes when you remix.", "Report back what played well."]}
];
function generateArchive(seed,opts){
  opts=opts||{};
  var s=(Math.abs(seed)||1);
  var b=ARCHIVE_BANK[s%ARCHIVE_BANK.length];
  var id=PREFIX+String(s).padStart(6,'0');
  return {id:id,t:b.title,g:b.g,name:b.title,title:b.title,description:b.description,
    how_it_works:"Archive record. "+b.description,
    key_points:b.key_points,
    requirements:["Study the key points in order.","Apply the record's guidance to a real quiz.","Review the standards before publishing."],
    standards:["Archive completeness: all fields present.","Content originality: Signature-authored."],
    citations:["Signature canon (2026).","Assessment-design literature."],
    src:"signature",
    demo:{kind:"python",language:"python",program:demoProgram(b.title,b.g)},
    ladder_rank:11+(s%30),ladder_tier:"advanced",_seed:s};
}
function validateArchive(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!/^JAH-QZGK-\d{6}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(!Array.isArray(r.key_points)||r.key_points.length<3)e.push('key_points');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(r.src!=='signature')e.push('src');
  return{ok:!e.length,errors:e};
}
gen.generateArchive=generateArchive;gen.validateArchive=validateArchive;

})();
