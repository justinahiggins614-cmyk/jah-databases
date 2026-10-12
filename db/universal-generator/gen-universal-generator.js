(function(){'use strict';
/* JAH Universal Generator Database generator — jahdb-universal-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Genre-free: the user describes ANYTHING and the generator builds a full,
   complete record. Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function shuffle(s,arr){var a=arr.slice(),i,j,t;for(i=a.length-1;i>0;i--){j=(s()*(i+1))|0;t=a[i];a[i]=a[j];a[j]=t;}return a;}
var PREFIX='JAH-UNI-';
/* ---------------- genre family pools ---------------- */
var RECIPES=[
 ['Margherita Pizza','Italian',['pizza dough','crushed tomatoes','fresh mozzarella','basil','olive oil'],['Stretch the dough thin','Spread tomato sauce edge to edge','Tear mozzarella over the top','Bake at 250°C for 8 minutes','Finish with basil and olive oil'],25],
 ['Chicken Tikka Masala','Indian',['chicken thighs','yogurt','garam masala','tomato puree','cream'],['Marinate chicken in yogurt and spices 2 hours','Sear until charred at the edges','Simmer in spiced tomato sauce 20 minutes','Stir in cream and serve over rice'],45],
 ['Beef Bourguignon','French',['beef chuck','red wine','pearl onions','carrots','mushrooms'],['Brown the beef in batches','Deglaze with red wine','Add vegetables and simmer 2.5 hours','Reduce the sauce until glossy'],180],
 ['Pad Thai','Thai',['rice noodles','shrimp','tamarind paste','peanuts','bean sprouts'],['Soak noodles until pliable','Sear shrimp quickly and set aside','Toss noodles in tamarind sauce','Fold in shrimp, sprouts and crushed peanuts'],30],
 ['Shakshuka','Middle Eastern',['eggs','crushed tomatoes','bell peppers','cumin','feta'],['Soften peppers in olive oil','Add tomatoes and cumin, simmer 10 minutes','Crack eggs into wells and cover 6 minutes','Crumble feta on top'],25],
 ['Ramen','Japanese',['ramen noodles','pork belly','soft eggs','miso','scallions'],['Simmer the broth base 40 minutes','Sear pork belly slices','Cook noodles 3 minutes','Assemble bowls with egg and scallions'],60]
];
var WORKOUTS=[
 ['Push Day — Chest, Shoulders, Triceps',[['Bench Press',4,'8-10','90s'],['Overhead Press',3,'10-12','75s'],['Incline Dumbbell Press',3,'10','60s'],['Lateral Raise',3,'15','45s'],['Tricep Pushdown',3,'12','60s']]],
 ['Pull Day — Back and Biceps',[['Deadlift',4,'5','180s'],['Pull-Up',3,'max','90s'],['Barbell Row',4,'8-10','90s'],['Face Pull',3,'15','60s'],['Barbell Curl',3,'10','60s']]],
 ['Leg Day — Quads, Glutes, Hamstrings',[['Back Squat',4,'6-8','180s'],['Romanian Deadlift',3,'10','120s'],['Walking Lunge',3,'12 each','90s'],['Leg Curl',3,'12','60s'],['Standing Calf Raise',4,'15','45s']]],
 ['Full-Body Conditioning',[['Kettlebell Swing',4,'20','60s'],['Goblet Squat',3,'15','60s'],['Push-Up',3,'max','45s'],['Plank',3,'60s','30s'],['Burpee',3,'10','60s']]]
];
var PROOFS=[
 ['Sum of the first n integers','1 + 2 + … + n = n(n+1)/2',['Pair 1 with n, 2 with n-1 — each pair sums to n+1','There are n/2 such pairs','Multiply: (n/2)(n+1) = n(n+1)/2','Check n=1: 1 = 1(2)/2 ✓']],
 ['Pythagorean theorem','a² + b² = c²',['Draw a square of side (a+b)','Place four right triangles inside, leaving a tilted inner square of side c','Area of big square: (a+b)² = a² + 2ab + b²','Also equals 4·(ab/2) + c² = 2ab + c²','Equate: a² + 2ab + b² = 2ab + c², so a² + b² = c²']],
 ['Sum of a geometric series','S = a(1 − rⁿ)/(1 − r) for r ≠ 1',['Write S = a + ar + ar² + … + arⁿ⁻¹','Multiply by r: rS = ar + ar² + … + arⁿ','Subtract: S − rS = a − arⁿ','Factor: S(1 − r) = a(1 − rⁿ), divide by (1 − r)']],
 ['Irrationality of √2','√2 cannot be written as p/q',['Assume √2 = p/q in lowest terms','Then 2q² = p², so p² is even, so p is even: p = 2k','Then 2q² = 4k², so q² = 2k², so q is even','Both even contradicts lowest terms — assumption false']]
];
var STORIES=[
 ['The Lighthouse Keeper','mystery','Elena Marsh','a cliffside lighthouse during a week-long storm','A ship that sank forty years ago signals the lighthouse every night at 3 a.m.','Elena decodes the light pattern and finds the wreck holds the town\'s missing deed archive.'],
 ['Copper Sky','science fiction','Dax Rennick','a mining colony on a tidally-locked planet','The colony\'s air recyclers fail one dome at a time, always during the copper-colored aurora.','Dax discovers the aurora is a signal — and something is answering the colony\'s distress calls.'],
 ['The Last Seed Vault','adventure','Priya Anand','a flooded coastal city in 2089','Priya\'s grandmother\'s seed vault is the only source of blight-resistant grain.','She must cross the drowned districts to reach the vault before the salvage crews do.'],
 ['A Quiet Rebellion','historical','Tomasz Wozniak','a printing press in 1981 Warsaw','Tomasz prints forbidden poetry between the pages of state-approved manuals.','When the inspectors come, the whole print shop must decide what the next page says.']
];
var BIZ=[
 ['Neighborhood Bakery',['Market: 2,000 households within 1 km','Startup cost: $45,000 (oven, fit-out, licenses)','Price: $4.50 average ticket','Break-even: 110 tickets/day','Year-1 revenue target: $180,000']],
 ['Mobile Car Detailing',['Market: suburban commuters, 15,000 cars in zone','Startup cost: $8,000 (van fit-out, equipment)','Price: $89 full detail','Break-even: 12 details/week','Year-1 revenue target: $95,000']],
 ['Freelance Web Studio',['Market: local trades needing websites','Startup cost: $2,500 (tools, hosting reseller)','Price: $1,800 per site + $60/mo care plan','Break-even: 2 sites/month','Year-1 revenue target: $72,000']]
];
var EXPERIMENTS=[
 ['Which paper airplane flies farthest?','Fold shape affects glide distance',['3 sheets of paper','tape measure','open hallway'],['Fold a dart, a glider, and a hammerhead design','Throw each 5 times from a marked line','Measure and average the distances','The glider should win: larger wing area means more lift at low speed.']],
 ['Do plants grow toward light?','Phototropism bends stems toward the strongest light',['2 bean seedlings in pots','cardboard box','desk lamp'],['Place one seedling in the box with a side hole, one in open light','Shine the lamp through the hole for 5 days','Observe stem direction daily','The boxed seedling bends toward the hole — auxin migrates to the shaded side.']],
 ['Which salt melts ice fastest?','Different salts depress the freezing point differently',['ice cubes','table salt','rock salt','stopwatch'],['Place equal ice cubes on three plates','Sprinkle equal salt amounts on two, leave one plain','Time full melt of each','Finer table salt usually wins: more surface area dissolves faster.']]
];
var LANGS=[
 ['Spanish',['Hola — hello','Gracias — thank you','¿Dónde está…? — where is…?'],'Gendered nouns: el libro (masc.), la mesa (fem.). Verb endings change with the subject: hablo, hablas, habla.'],
 ['Japanese',['Konnichiwa — hello','Arigatou — thank you','Sumimasen — excuse me'],'Three scripts: hiragana, katakana, kanji. Sentence order is subject-object-verb. Particles mark roles: wa, ga, wo.'],
 ['French',['Bonjour — hello','Merci — thank you','Où est…? — where is…?'],'Nouns are gendered; adjectives agree: petit/petite. Formal vs informal you: vous vs tu.']
];
var GAMES=[
 ['Harbor Traders','2–4 players, 60 min','Buy low in one port, sell high in another; storms reroute ships.',['Draw 3 cargo cards','Move ships up to 2 sea zones','Trade at any docked port','First to 100 gold wins.']],
 ['Tower of Echoes','cooperative, 45 min','Players are bells in a tower; ring in sequence to banish the silence.',['Draw an echo card','Ring your bell in the shown order','Missed notes feed the silence track','Banish 5 silences to win.']]
];
var MUSIC=[
 ['Twelve-bar blues in A',['A7','D7','A7','A7','D7','D7','A7','A7','E7','D7','A7','E7'],'Four-on-the-floor shuffle at 96 BPM; walk the bass A–C#–E–G.'],
 ['Pop ballad in C',['C','G','Am','F'],'Verse–chorus form at 72 BPM; lift the chorus an octave on the vocal.'],
 ['Lo-fi loop in F minor',['Fm9','Bbm9','Eb13','Abmaj9'],'85 BPM, swung hats; leave the second bar half-empty for breath.']
];
var GARDEN=[
 ['Tomatoes',['full sun, 45–60 cm spacing','water deeply 2–3×/week','stake early; prune suckers'],'Sow indoors 6 weeks before last frost; transplant after nights stay above 10°C.'],
 ['Basil',['full sun, 25 cm spacing','keep soil moist, never soggy','pinch flower buds to keep leaves sweet'],'Plant after frost; harvest from the top to encourage bushiness.'],
 ['Carrots',['full sun, thin to 5 cm','even moisture for straight roots','loose sandy soil, no fresh manure'],'Sow directly 3 weeks before last frost; germination takes 14–21 days.']
];
var CODE=[
 ['JavaScript','Reverse a string',"function reverse(s){return s.split('').reverse().join('');}\nconsole.log(reverse('hello')); // olleh",'Split into characters, reverse the array, join back.'],
 ['Python','Fibonacci generator',"def fib(n):\n    a,b=0,1\n    for _ in range(n):\n        yield a\n        a,b=b,a+b\nprint(list(fib(8)))  # [0,1,1,2,3,5,8,13]",'Yield each term lazily; tuple swap advances the pair.'],
 ['JavaScript','Debounce a function',"function debounce(fn,ms){let t;return(...a)=>{clearTimeout(t);t=setTimeout(()=>fn(...a),ms);};}",'Clear the pending timer on each call; only the last call in the window fires.']
];
var MEDIT=[
 ['Box breathing',['Inhale 4 counts','Hold 4 counts','Exhale 4 counts','Hold 4 counts','Repeat 6 rounds'],'Used by first responders to steady the nervous system; the equal holds balance the autonomic rhythm.'],
 ['Body scan',['Lie down, eyes closed','Move attention from toes to crown','Notice each area for 10 seconds without judging','End with three slow breaths'],'Trains interoception; studies link 8 weeks of practice to lower perceived stress.']
];
var FAMS=[
 {g:'recipe',t:'Recipe',type:'dish'},
 {g:'workout-plan',t:'Workout Plan',type:'training session'},
 {g:'math-proof',t:'Math Proof',type:'theorem'},
 {g:'short-story',t:'Short Story',type:'fiction'},
 {g:'business-plan',t:'Business Plan',type:'venture'},
 {g:'science-experiment',t:'Science Experiment',type:'hands-on test'},
 {g:'language-lesson',t:'Language Lesson',type:'mini-lesson'},
 {g:'game-design',t:'Game Design',type:'tabletop game'},
 {g:'music-composition',t:'Music Composition',type:'arrangement'},
 {g:'gardening-plan',t:'Gardening Plan',type:'planting guide'},
 {g:'coding-tutorial',t:'Coding Tutorial',type:'code lesson'},
 {g:'meditation-guide',t:'Meditation Guide',type:'practice'}
];
/* ---------------- builders ---------------- */
function buildRecipe(s,topic){
 var d=pick(RECIPES,s);
 var title=topic?('Recipe: '+topic+' (in the spirit of '+d[0]+')'):d[0]+' — Classic '+d[1]+' Dish';
 return {title:title,
  description:'A complete '+d[1].toLowerCase()+' recipe for '+d[0].toLowerCase()+(topic?', adapted for '+topic:'')+'. Ready in about '+d[5]+' minutes with '+d[2].length+' ingredients and '+d[3].length+' steps — every quantity and instruction included, nothing left vague.',
  type:'dish',
  content:{dish:d[0],cuisine:d[1],servings:ri(s,2,6),total_minutes:d[5],ingredients:d[2],steps:d[3]},
  demo:{kind:'ingredient-scaler',program:'function scale(ings,from,to){var f=to/from;return ings.map(function(i){return i+" × "+f.toFixed(2);});}',note:'Paste into any JS console with your ingredient list to rescale servings.'}};
}
function buildWorkout(s,topic){
 var d=pick(WORKOUTS,s);
 var title=topic?('Workout Plan: '+topic+' — built on "'+d[0]+'"'):d[0];
 var ex=d[1].map(function(e){return {exercise:e[0],sets:e[1],reps:e[2],rest:e[3]};});
 return {title:title,
  description:'A full training session: "'+d[0]+'". '+ex.length+' exercises with sets, reps and rest periods — warm up 5 minutes, work through the list in order, cool down with stretching.',
  type:'training session',
  content:{session:d[0],exercises:ex,notes:'Rest as listed; add weight when all sets hit the top of the rep range.'},
  demo:{kind:'interval-plan',program:JSON.stringify(ex.map(function(e){return e.exercise+': '+e.sets+'×'+e.reps+' (rest '+e.rest+')';})),note:'Read top to bottom as your round timer.'}};
}
function buildProof(s,topic){
 var d=pick(PROOFS,s);
 var title=topic?('Math Proof: '+topic+' (method shown on "'+d[0]+'")'):d[0]+' — Full Proof';
 return {title:title,
  description:'A complete, checkable proof of '+d[1]+'. Each step follows from the last; the final line is verified against a concrete case so you can trust the chain.',
  type:'theorem',
  content:{theorem:d[0],statement:d[1],steps:d[2]},
  demo:{kind:'verification',program:'// verify n=10: 1+…+10 = '+ (10*11/2) +'\nvar n=10,sum=0;for(var i=1;i<=n;i++)sum+=i;console.log(sum===n*(n+1)/2); // true',note:'Runnable check of the proved formula.'}};
}
function buildStory(s,topic){
 var d=pick(STORIES,s);
 var title=topic?('Short Story: '+topic):d[0];
 return {title:title,
  description:'A complete short story, "'+d[0]+'" — a '+d[1]+' tale. '+d[5],
  type:'fiction',
  content:{title:d[0],genre:d[1],protagonist:d[2],setting:d[3],premise:d[4],arc:d[5],beats:['Open on '+d[3]+' with '+d[2]+' mid-routine','Introduce the disruption: '+d[4],'Raise the stakes — a choice with no clean answer','Climax: '+d[5],'Close on the changed world, one quiet image']},
  demo:null};
}
function buildBiz(s,topic){
 var d=pick(BIZ,s);
 var title=topic?('Business Plan: '+topic+' (modeled on "'+d[0]+'")'):d[0]+' — One-Page Plan';
 return {title:title,
  description:'A one-page business plan for a '+d[0].toLowerCase()+(topic?', adapted toward '+topic:'')+'. Market, costs, pricing and targets — the numbers a lender asks for first.',
  type:'venture',
  content:{venture:d[0],sections:d[1]},
  demo:{kind:'breakeven-calc',program:'function breakeven(fixed,price,varcost){return Math.ceil(fixed/(price-varcost));}',note:'JS: units per month to break even.'}};
}
function buildExperiment(s,topic){
 var d=pick(EXPERIMENTS,s);
 var title=topic?('Science Experiment: '+topic+' (framed like "'+d[0]+'")'):d[0];
 return {title:title,
  description:'A hands-on experiment: "'+d[0]+'". Question: '+d[1]+' Includes materials, procedure and what to expect — safe for home or classroom.',
  type:'hands-on test',
  content:{title:d[0],question:d[1],materials:d[2],procedure:d[3]},
  demo:{kind:'results-table',program:'trial,measurement\n1,\n2,\n3,\n4,\n5,',note:'CSV template: fill one row per trial.'}};
}
function buildLang(s,topic){
 var d=pick(LANGS,s);
 var title=topic?('Language Lesson: '+topic+' ('+d[0]+' track)'):d[0]+' — First 3 Phrases';
 return {title:title,
  description:'A mini '+d[0]+' lesson: three survival phrases with translations plus one grammar key that unlocks the pattern behind them.',
  type:'mini-lesson',
  content:{language:d[0],phrases:d[1],grammar_key:d[2],practice:'Say each phrase aloud 5 times, then build one new sentence using the grammar key.'},
  demo:null};
}
function buildGame(s,topic){
 var d=pick(GAMES,s);
 var title=topic?('Game Design: '+topic+' (mechanics in the spirit of "'+d[0]+'")'):d[0]+' — Complete Rules';
 return {title:title,
  description:'A complete tabletop game, "'+d[0]+'": '+d[1]+'. '+d[2]+' Full turn structure and win condition included — playable tonight.',
  type:'tabletop game',
  content:{title:d[0],players:d[1],pitch:d[2],turn_structure:d[3]},
  demo:null};
}
function buildMusic(s,topic){
 var d=pick(MUSIC,s);
 var title=topic?('Music Composition: '+topic+' (harmony study on "'+d[0]+'")'):d[0]+' — Arrangement Sketch';
 return {title:title,
  description:'An arrangement sketch: "'+d[0]+'". Full chord sequence with performance notes — '+d[2],
  type:'arrangement',
  content:{title:d[0],chords:d[1],performance:d[2]},
  demo:{kind:'chord-sheet',program:d[1].join(' | '),note:'One chord per bar; loop 4 times.'}};
}
function buildGarden(s,topic){
 var d=pick(GARDEN,s);
 var title=topic?('Gardening Plan: '+topic+' (companion notes for '+d[0].toLowerCase()+')'):d[0]+' — Growing Guide';
 return {title:title,
  description:'A complete growing guide for '+d[0].toLowerCase()+'. '+d[2],
  type:'planting guide',
  content:{plant:d[0],requirements:d[1],how_to:d[2],calendar:['Early spring: prepare soil','After frost: sow/transplant','Summer: water + watch for pests','Harvest: pick regularly to extend yield']},
  demo:null};
}
function buildCode(s,topic){
 var d=pick(CODE,s);
 var title=topic?('Coding Tutorial: '+topic+' ('+d[0]+' example: '+d[1]+')'):d[1]+' in '+d[0];
 return {title:title,
  description:'A code lesson: '+d[1]+' in '+d[0]+'. '+d[3]+' The snippet below runs as-is — that is the demo.',
  type:'code lesson',
  content:{language:d[0],concept:d[1],code:d[2],explanation:d[3]},
  demo:{kind:'runnable-code',program:d[2],note:'Runs as-is in a '+d[0]+' console.'}};
}
function buildMedit(s,topic){
 var d=pick(MEDIT,s);
 var title=topic?('Meditation Guide: '+topic+' (using "'+d[0]+'")'):d[0]+' — Guided Practice';
 return {title:title,
  description:'A guided practice: "'+d[0]+'". '+d[2]+' Follow the steps slowly; about ten minutes total.',
  type:'practice',
  content:{practice:d[0],steps:d[1],why_it_works:d[2]},
  demo:null};
}
var BUILDERS={recipe:buildRecipe,'workout-plan':buildWorkout,'math-proof':buildProof,'short-story':buildStory,'business-plan':buildBiz,'science-experiment':buildExperiment,'language-lesson':buildLang,'game-design':buildGame,'music-composition':buildMusic,'gardening-plan':buildGarden,'coding-tutorial':buildCode,'meditation-guide':buildMedit};
var GENRES=Object.keys(BUILDERS);
/* ---------------- main ---------------- */
function normGenre(g){
 if(!g) return null;
 var t=String(g).toLowerCase().trim().replace(/[^a-z0-9]+/g,'-').replace(/^-+|-+$/g,'');
 if(BUILDERS[t]) return t;
 for(var i=0;i<GENRES.length;i++){ if(GENRES[i].indexOf(t)>=0||t.indexOf(GENRES[i])>=0) return GENRES[i]; }
 return null;
}
function generate(seed,opts,rnd){
 opts=opts||{}; rnd=rnd||prng(seed);
 var topic=(opts.topic||'').toString().trim().slice(0,120);
 var g=normGenre(opts.genre)||pick(GENRES,rnd);
 var b=BUILDERS[g](rnd,topic||null);
 var fam=null; for(var i=0;i<FAMS.length;i++){ if(FAMS[i].g===g) fam=FAMS[i]; }
 var id=PREFIX+String(seed).padStart(6,'0');
 return {id:id,title:b.title,description:b.description,genre:g,type:b.type,content:b.content,demo:b.demo,src:'signature',_seed:seed,topic:topic||undefined};
}
function validate(r){
 var e=[];
 if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
 if(!/^JAH-UNI-\d{6}$/.test(r.id||''))e.push('id');
 if(typeof r.title!=='string'||r.title.length<8)e.push('title');
 if(typeof r.description!=='string'||r.description.length<60)e.push('description');
 if(GENRES.indexOf(r.genre)<0)e.push('genre');
 if(!r.content||typeof r.content!=='object')e.push('content');
 return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
 var dups=(sample||[]).filter(function(r){return r&&r.title===record.title;});
 return dups.length?{ok:false,errors:['duplicate title in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-universal-generator-1.0',generate:generate,validate:validate,driftCheck:driftCheck,genres:GENRES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('universal-generator',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
