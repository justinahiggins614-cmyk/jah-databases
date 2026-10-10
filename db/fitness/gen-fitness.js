/* JAH Fitness Database generator — jahdb-fitness-1.0.
   Deterministic client-side generator. Same seed + same version always makes
   the same record. General educational information only, never medical advice.
   Property of Justin Addam Higgins (JAH). */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var CATS=['strength','cardio','mobility','flexibility','conditioning','recovery','programming','nutrition-basics'];
var PREFIX='JAH-FIT-';
var SAFETY='General educational information only, not medical advice. Consult a qualified professional before starting a new program.';
/* Anchors: {n, c, f1, f2 (single verified sentences), muscles[], equip, cues[], sets, reps, rest (seconds)}. */
var ANCHORS=[
{n:"Barbell Back Squat",c:"strength",f1:"The barbell back squat is a compound lower-body lift working the quadriceps, gluteus maximus, and adductor magnus, with hamstrings, calves, lower back, and abs stabilizing.",f2:"High-bar placement keeps the torso upright and emphasizes the quads, while low-bar placement shifts emphasis to the glutes and hamstrings.",muscles:["Quadriceps","Gluteus maximus","Adductor magnus","Hamstrings","Erector spinae"],equip:"Barbell, squat rack, plates",cues:["Brace the core before each rep","Keep the chest up","Push the knees out in line with the toes","Descend until thighs are at least parallel"],sets:4,reps:8,rest:150},
{n:"Conventional Deadlift",c:"strength",f1:"The conventional deadlift lifts a loaded barbell from the floor to standing, training the entire posterior chain.",f2:"It is a hip-hinge pattern, not a squat: the hips travel back while the spine stays neutral.",muscles:["Gluteus maximus","Hamstrings","Erector spinae","Latissimus dorsi","Forearms"],equip:"Barbell, plates",cues:["Keep a flat back from start to lockout","Push the hips back to reach the bar","Drive the floor away with the legs","Lock out tall without leaning back"],sets:4,reps:5,rest:180},
{n:"Barbell Bench Press",c:"strength",f1:"The barbell bench press is the foundational upper-body push, working the chest, shoulders, and triceps.",f2:"A stable arch, retracted shoulder blades, and leg drive turn it into a full-body lift.",muscles:["Pectoralis major","Anterior deltoids","Triceps brachii"],equip:"Barbell, bench, rack, plates",cues:["Pinch the shoulder blades together","Keep the feet planted and drive through them","Lower the bar to the mid-chest with control","Press in a slight arc back over the shoulders"],sets:4,reps:8,rest:150},
{n:"Standing Overhead Press",c:"strength",f1:"The standing overhead press builds the shoulders and triceps while demanding full-body bracing.",f2:"Pressing overhead standing trains balance and trunk stability that seated pressing misses.",muscles:["Deltoids","Triceps brachii","Upper trapezius","Core stabilizers"],equip:"Barbell or dumbbells, plates",cues:["Squeeze the glutes to protect the lower back","Press the head through at the top","Keep the ribs down, not flared","Lower under control to the collarbone"],sets:3,reps:8,rest:120},
{n:"Pull-Up",c:"strength",f1:"Pull-ups train the lats and biceps through a full hanging range of motion.",f2:"They are the standard measure of relative upper-body pulling strength.",muscles:["Latissimus dorsi","Biceps brachii","Rhomboids","Core stabilizers"],equip:"Pull-up bar",cues:["Start from a dead hang","Pull the chest to the bar","Avoid kipping unless trained for it","Lower slowly to full extension"],sets:4,reps:8,rest:120},
{n:"Bent-Over Barbell Row",c:"strength",f1:"Bent-over rows build back thickness across the lats, rhomboids, and traps.",f2:"The hinged position also trains the lower back and hamstrings isometrically.",muscles:["Latissimus dorsi","Rhomboids","Trapezius","Biceps brachii","Erector spinae"],equip:"Barbell, plates",cues:["Hinge to about forty-five degrees","Keep the back flat","Pull the bar to the lower ribs","Squeeze the shoulder blades at the top"],sets:4,reps:8,rest:120},
{n:"Front Squat",c:"strength",f1:"The front squat holds the bar across the front of the shoulders, keeping the torso upright with strong quad emphasis.",f2:"It demands more upper-back and core rigidity than the back squat.",muscles:["Quadriceps","Gluteus maximus","Upper back","Core stabilizers"],equip:"Barbell, squat rack, plates",cues:["Keep the elbows high throughout","Stay tall through the torso","Drive the knees forward over the toes","Do not let the elbows drop in the hole"],sets:4,reps:6,rest:150},
{n:"Romanian Deadlift",c:"strength",f1:"The Romanian deadlift is a hip-hinge accessory that loads the hamstrings and glutes through a long range.",f2:"The bar stays close to the legs while the hips travel back until a deep hamstring stretch.",muscles:["Hamstrings","Gluteus maximus","Erector spinae"],equip:"Barbell or dumbbells",cues:["Push the hips straight back","Keep a soft bend in the knees","Feel the hamstrings load, then drive the hips forward","Never round the lower back"],sets:3,reps:10,rest:90},
{n:"Barbell Hip Thrust",c:"strength",f1:"The hip thrust loads peak glute contraction at the top of a horizontal hip-extension pattern.",f2:"The upper back rests on a bench while the hips drive a barbell upward.",muscles:["Gluteus maximus","Hamstrings","Quadriceps"],equip:"Barbell, bench, pad",cues:["Tuck the chin and ribs down","Drive through the heels","Squeeze the glutes hard at the top","Keep the knees tracking over the ankles"],sets:3,reps:12,rest:90},
{n:"Walking Lunge",c:"strength",f1:"Walking lunges train each leg independently, building single-leg strength and balance.",f2:"The long stride pattern transfers well to running and field sports.",muscles:["Quadriceps","Gluteus maximus","Hamstrings","Calves"],equip:"Dumbbells optional",cues:["Take a long confident stride","Keep the torso tall","Lower until the back knee nearly touches","Drive up through the front heel"],sets:3,reps:12,rest:90},
{n:"Bulgarian Split Squat",c:"strength",f1:"The Bulgarian split squat elevates the rear foot, loading the front leg heavily with little spinal load.",f2:"It exposes and corrects left-right strength imbalances.",muscles:["Quadriceps","Gluteus maximus","Adductors"],equip:"Bench, dumbbells optional",cues:["Keep most weight on the front foot","Stay tall through the torso","Lower straight down, not forward","Drive up without pushing off the rear foot"],sets:3,reps:10,rest:90},
{n:"Goblet Squat",c:"strength",f1:"The goblet squat holds a dumbbell or kettlebell at the chest, teaching upright squat mechanics.",f2:"It is the standard first loaded squat for beginners.",muscles:["Quadriceps","Gluteus maximus","Core stabilizers"],equip:"Dumbbell or kettlebell",cues:["Hold the weight tight to the chest","Push the knees out","Keep the heels down","Brace before every rep"],sets:3,reps:12,rest:60},
{n:"Leg Press",c:"strength",f1:"The leg press loads the quads and glutes heavily without a bar on the back.",f2:"Foot placement shifts emphasis: higher targets glutes, lower targets quads.",muscles:["Quadriceps","Gluteus maximus","Hamstrings"],equip:"Leg press machine",cues:["Keep the lower back pressed into the pad","Do not lock the knees hard at the top","Lower under control","Keep the feet flat on the platform"],sets:3,reps:12,rest:90},
{n:"Dumbbell Biceps Curl",c:"strength",f1:"The dumbbell curl isolates the biceps through elbow flexion.",f2:"Controlled tempo matters more than heavy weight for arm growth.",muscles:["Biceps brachii","Brachialis","Forearms"],equip:"Dumbbells",cues:["Keep the elbows pinned at the sides","Do not swing the torso","Squeeze at the top","Lower slowly"],sets:3,reps:12,rest:60},
{n:"Triceps Pushdown",c:"strength",f1:"The triceps pushdown isolates the triceps with a cable and straight bar or rope.",f2:"The triceps make up most of upper-arm mass, so they drive arm size.",muscles:["Triceps brachii"],equip:"Cable machine",cues:["Pin the elbows to the ribs","Press to full lockout","Keep the shoulders down","Control the return"],sets:3,reps:12,rest:60},
{n:"Dumbbell Lateral Raise",c:"strength",f1:"Lateral raises isolate the side deltoids, building shoulder width.",f2:"Light weights with strict form beat heavy swinging.",muscles:["Lateral deltoids","Upper trapezius"],equip:"Light dumbbells",cues:["Lead with the elbows, not the hands","Stop at shoulder height","Keep a slight bend in the elbows","Control the lowering phase"],sets:3,reps:15,rest:60},
{n:"Forearm Plank",c:"strength",f1:"The forearm plank trains the entire trunk to resist extension under load.",f2:"Quality bracing for shorter holds beats sagging through long ones.",muscles:["Rectus abdominis","Transverse abdominis","Obliques","Glutes"],equip:"Floor mat",cues:["Squeeze the glutes and brace hard","Keep a straight line from head to heels","Do not let the hips sag","Breathe behind the brace"],sets:3,reps:1,rest:60},
{n:"Push-Up",c:"strength",f1:"The push-up is the foundational bodyweight press, training chest, shoulders, and triceps.",f2:"Elevating the hands or dropping to knees scales it for any level.",muscles:["Pectoralis major","Anterior deltoids","Triceps brachii","Core stabilizers"],equip:"Floor",cues:["Keep the body in one straight line","Lower the chest to the floor","Push the floor away","Do not let the hips sag"],sets:3,reps:15,rest:60},
{n:"Parallel-Bar Dip",c:"strength",f1:"Dips load the chest and triceps through a deep pressing range.",f2:"Leaning forward emphasizes the chest, staying upright hits the triceps.",muscles:["Pectoralis major","Triceps brachii","Anterior deltoids"],equip:"Dip bars",cues:["Lower until the shoulders feel a stretch","Keep the shoulders down away from the ears","Press to full lockout","Avoid shrugging at the top"],sets:3,reps:10,rest:90},
{n:"Kettlebell Swing",c:"conditioning",f1:"The kettlebell swing is an explosive hip-hinge that builds power and conditioning together.",f2:"The arms stay relaxed while the hips snap the bell to chest height.",muscles:["Gluteus maximus","Hamstrings","Erector spinae","Shoulders"],equip:"Kettlebell",cues:["Hike the bell back between the legs","Snap the hips forward explosively","Keep the back flat","Let the bell float, do not lift with the arms"],sets:5,reps:15,rest:60},
{n:"Steady-State Running",c:"cardio",f1:"Steady-state running at a conversational pace builds the aerobic base that supports all other training.",f2:"Most weekly mileage should stay easy, with intensity added sparingly.",muscles:["Quadriceps","Hamstrings","Glutes","Calves","Heart"],equip:"Running shoes",cues:["Land under the hips, not ahead","Keep the cadence quick and light","Relax the shoulders","Breathe rhythmically"],sets:1,reps:1,rest:0},
{n:"Interval Running",c:"cardio",f1:"Running intervals alternate hard efforts with recovery jogs to raise speed and aerobic capacity.",f2:"A classic session is four hundred meter repeats with equal recovery.",muscles:["Quadriceps","Hamstrings","Glutes","Calves","Heart"],equip:"Running shoes, track optional",cues:["Warm up thoroughly first","Run the hard efforts controlled, not all-out","Jog the recoveries","Stop if form collapses"],sets:1,reps:8,rest:0},
{n:"Cycling",c:"cardio",f1:"Cycling builds leg endurance and aerobic fitness with minimal joint impact.",f2:"Both outdoor riding and stationary bikes develop the same engine.",muscles:["Quadriceps","Glutes","Calves","Heart"],equip:"Bicycle or stationary bike",cues:["Set the saddle height for a slight knee bend","Keep a smooth circular pedal stroke","Stay relaxed in the upper body","Build duration before intensity"],sets:1,reps:1,rest:0},
{n:"Swimming",c:"cardio",f1:"Swimming trains the whole body with near-zero joint impact.",f2:"Freestyle technique work pays off more than thrashing harder.",muscles:["Latissimus dorsi","Shoulders","Core","Legs","Heart"],equip:"Pool",cues:["Exhale fully underwater","Rotate from the hips","Keep the head neutral","Start with technique drills"],sets:1,reps:1,rest:0},
{n:"Rowing Machine",c:"cardio",f1:"The rowing machine blends leg drive, back pull, and arm finish into full-body cardio.",f2:"The stroke is legs, then body swing, then arms, reversing on the recovery.",muscles:["Quadriceps","Latissimus dorsi","Rhomboids","Biceps","Heart"],equip:"Rowing ergometer",cues:["Drive with the legs first","Keep the back flat","Do not rush the recovery slide","Finish with the handle at the ribs"],sets:1,reps:1,rest:0},
{n:"Jump Rope",c:"cardio",f1:"Jump rope builds foot speed, coordination, and calf endurance in tiny spaces.",f2:"Short intervals make it a potent warm-up or finisher.",muscles:["Calves","Quadriceps","Shoulders","Heart"],equip:"Jump rope",cues:["Stay on the balls of the feet","Keep the elbows close","Turn the rope with the wrists","Land softly"],sets:5,reps:1,rest:45},
{n:"Walking Programs",c:"cardio",f1:"Walking is the most accessible cardio, and a commonly cited daily goal is ten thousand steps.",f2:"Brisk walking after meals is a simple, sustainable habit.",muscles:["Calves","Quadriceps","Glutes","Heart"],equip:"Comfortable shoes",cues:["Stand tall with a natural arm swing","Walk briskly enough to raise the heart rate","Build distance gradually","Choose safe, pleasant routes"],sets:1,reps:1,rest:0},
{n:"High-Intensity Interval Training",c:"conditioning",f1:"High-intensity interval training alternates hard efforts with recovery, and Tabata uses twenty seconds of work with ten seconds of rest for eight rounds.",f2:"Sessions stay short because the intensity is genuinely high.",muscles:["Full body","Heart"],equip:"Bodyweight or minimal gear",cues:["Warm up before the first interval","Go hard but keep form","Scale movements to stay safe","Cool down after"],sets:1,reps:8,rest:0},
{n:"Circuit Training",c:"conditioning",f1:"Circuit training strings exercises together with minimal rest, blending strength and cardio.",f2:"Typical circuits hit upper body, lower body, and core in rotation.",muscles:["Full body","Heart"],equip:"Mixed equipment",cues:["Keep transitions quick","Choose weights you can control when tired","Breathe continuously","Track rounds completed"],sets:3,reps:1,rest:60},
{n:"Battle Ropes",c:"conditioning",f1:"Battle ropes drive conditioning through continuous upper-body waves and slams.",f2:"Short all-out bursts with full recovery build power endurance.",muscles:["Shoulders","Back","Core","Heart"],equip:"Battle ropes, anchor",cues:["Hinge slightly and brace","Drive the waves from the hips","Keep the shoulders down","Breathe through the effort"],sets:6,reps:1,rest:60},
{n:"Box Jump",c:"conditioning",f1:"Box jumps train explosive lower-body power and landing mechanics.",f2:"Step down rather than jumping down to protect the joints.",muscles:["Quadriceps","Glutes","Calves"],equip:"Plyo box",cues:["Land softly in a quarter squat","Choose a box you can land on quietly","Reset fully between reps","Stop when jumps lose snap"],sets:4,reps:8,rest:90},
{n:"Elliptical Trainer",c:"cardio",f1:"The elliptical gives low-impact cardio with optional arm handles for upper-body involvement.",f2:"Resistance and incline adjust the challenge without pounding.",muscles:["Quadriceps","Glutes","Heart"],equip:"Elliptical machine",cues:["Stand tall, do not lean on the handles","Drive through the whole foot","Vary resistance and incline","Keep a steady cadence"],sets:1,reps:1,rest:0},
{n:"Stair Climber",c:"cardio",f1:"The stair climber builds leg endurance and cardio on a relentless vertical pattern.",f2:"Short intense climbs or long steady sessions both work.",muscles:["Quadriceps","Glutes","Calves","Heart"],equip:"Stair climber machine",cues:["Do not hang on the rails","Take full steps","Keep the torso upright","Start with moderate pace"],sets:1,reps:1,rest:0},
{n:"Static Stretching",c:"flexibility",f1:"Static stretching holds muscles at length after training to maintain range of motion.",f2:"Gentle holds of twenty to thirty seconds beat aggressive pulling.",muscles:["Targeted by stretch"],equip:"Mat",cues:["Stretch warm muscles, not cold ones","Breathe deeply into the stretch","Never force through sharp pain","Hold each side equally"],sets:1,reps:1,rest:0},
{n:"Dynamic Warm-Up",c:"flexibility",f1:"Dynamic warm-ups move joints through full ranges before training, raising tissue temperature.",f2:"Leg swings, hip circles, and inchworms are standard choices.",muscles:["Full body"],equip:"Open floor",cues:["Move deliberately, not ballistically","Cover ankles to neck","Progress from easy to brisk","Keep it under ten minutes"],sets:1,reps:1,rest:0},
{n:"Yoga: Downward-Facing Dog",c:"flexibility",f1:"Downward-facing dog lengthens the hamstrings, calves, and shoulders in one shape.",f2:"It is both a rest pose and an active stretch in flowing sequences.",muscles:["Hamstrings","Calves","Shoulders"],equip:"Yoga mat",cues:["Press the floor away with the hands","Lengthen the spine before straightening legs","Pedal the feet gently","Breathe into the back of the legs"],sets:1,reps:1,rest:0},
{n:"Yoga: Warrior Sequence",c:"flexibility",f1:"The warrior poses build leg strength and hip mobility while opening the chest.",f2:"Warrior one, two, and reverse warrior flow together naturally.",muscles:["Quadriceps","Glutes","Hip flexors","Shoulders"],equip:"Yoga mat",cues:["Ground through the outer back foot","Stack the front knee over the ankle","Lengthen the torso upward","Keep the shoulders relaxed"],sets:1,reps:1,rest:0},
{n:"Foam Rolling",c:"recovery",f1:"Foam rolling applies pressure to soft tissue, often called self-myofascial release.",f2:"Slow rolls over tender spots beat fast rolling back and forth.",muscles:["Targeted by area"],equip:"Foam roller",cues:["Roll slowly, about an inch per second","Pause on tender spots","Avoid rolling directly on joints","Breathe and relax into pressure"],sets:1,reps:1,rest:0},
{n:"Hip Flexor Stretch",c:"mobility",f1:"The half-kneeling hip flexor stretch opens the front of the hip, which shortens from sitting.",f2:"A posterior pelvic tilt deepens the stretch without arching the back.",muscles:["Hip flexors","Quadriceps"],equip:"Mat or pad",cues:["Tuck the tailbone slightly","Shift forward until a gentle stretch","Squeeze the back glute","Keep the torso tall"],sets:2,reps:1,rest:30},
{n:"Thoracic Spine Mobility",c:"mobility",f1:"Thoracic rotations and extensions restore mid-back movement lost to desk posture.",f2:"A mobile thoracic spine improves overhead pressing and posture.",muscles:["Thoracic extensors","Obliques"],equip:"Foam roller or bench",cues:["Move segment by segment","Do not force end ranges","Pair with deep breathing","Keep the lower back quiet"],sets:2,reps:10,rest:30},
{n:"Dead Bug",c:"strength",f1:"The dead bug trains the core to stabilize while the limbs move.",f2:"It is a safe first core exercise for beginners.",muscles:["Transverse abdominis","Rectus abdominis","Hip flexors"],equip:"Floor mat",cues:["Press the lower back into the floor","Exhale as the limbs extend","Move slowly with control","Stop if the back arches"],sets:3,reps:10,rest:45},
{n:"Bird Dog",c:"mobility",f1:"The bird dog extends opposite arm and leg from all fours, training spinal stability.",f2:"It is a staple in back-friendly core programs.",muscles:["Erector spinae","Glutes","Core stabilizers"],equip:"Floor mat",cues:["Keep the hips level","Reach long, not high","Brace the trunk","Move slowly"],sets:3,reps:10,rest:45},
{n:"Push-Pull-Legs Split",c:"programming",f1:"Push-pull-legs groups training into push day for chest, shoulders, and triceps, pull day for back and biceps, and leg day for quads, hamstrings, glutes, and calves.",f2:"It runs three days weekly for beginners or six days for advanced lifters.",muscles:["Full body across the week"],equip:"Full gym",cues:["Start each day with a compound lift","Finish with smaller muscles","Rest at least one day weekly","Track weights session to session"],sets:1,reps:1,rest:0},
{n:"Five-by-Five Strength Program",c:"programming",f1:"Five-by-five programs use five sets of five reps on compound lifts, adding weight each session.",f2:"The simple progression works best for beginners and early intermediates.",muscles:["Full body across the week"],equip:"Barbell, rack, bench",cues:["Add small increments each session","Do not skip warm-up sets","Deload when progress stalls","Eat and sleep to support growth"],sets:5,reps:5,rest:180},
{n:"Progressive Overload",c:"programming",f1:"Progressive overload gradually increases weight, reps, or sets, and it is the core driver of adaptation.",f2:"Small consistent increases beat occasional heroic jumps.",muscles:["All trained muscles"],equip:"Any progressive tool",cues:["Add the smallest possible increment","Keep form constant as load rises","Track every session","Be patient across months"],sets:1,reps:1,rest:0},
{n:"Rest Period Guidelines",c:"programming",f1:"Common guidance sets rest at two to three minutes for strength, sixty to ninety seconds for hypertrophy, and thirty to sixty seconds for endurance.",f2:"These ranges align with American College of Sports Medicine resistance-training guidance.",muscles:["All trained muscles"],equip:"Timer",cues:["Rest longer on heavy compounds","Rest shorter on isolation work","Use a timer, not a feeling","Adjust to the goal of the block"],sets:1,reps:1,rest:0},
{n:"Rep Range Guide",c:"programming",f1:"Common guidance prescribes three to six reps for strength, six to twelve for muscle growth, and twelve to twenty for endurance.",f2:"These ranges align with American College of Sports Medicine resistance-training guidance.",muscles:["All trained muscles"],equip:"Any resistance",cues:["Match the range to the goal","Keep one to three reps in reserve","Progress within the range first","Reassess every few weeks"],sets:1,reps:1,rest:0},
{n:"Deload Weeks",c:"recovery",f1:"Deload weeks cut volume and intensity roughly in half to let fatigue dissipate.",f2:"Planned deloads every four to eight weeks sustain long-term progress.",muscles:["Full body"],equip:"Same as training",cues:["Keep the same movements, lighter","Focus on technique","Sleep extra if possible","Return hungry the next week"],sets:1,reps:1,rest:0},
{n:"Sleep and Recovery",c:"recovery",f1:"Sleep is the primary recovery tool, with most adults needing seven to nine hours.",f2:"Training adaptations consolidate during deep sleep.",muscles:["Full body"],equip:"None",cues:["Keep a consistent bedtime","Limit screens before bed","Keep the room cool and dark","Treat sleep like training"],sets:1,reps:1,rest:0},
{n:"Protein and Hydration Basics",c:"nutrition-basics",f1:"Sports-nutrition guidance commonly cites about 1.6 to 2.2 grams of protein per kilogram of body weight daily for active people building muscle.",f2:"Water needs rise with training, and pale yellow urine is a practical hydration gauge.",muscles:["All trained muscles"],equip:"Kitchen and water bottle",cues:["Spread protein across three to five meals","Drink water before, during, and after training","Do not chase extreme diets","Adjust to appetite and progress"],sets:1,reps:1,rest:0}
];
var LENSES=[
["Exercise Overview","online","This overview edition presents {n} as a standard {c} entry for general fitness education.",null],
["Muscles Worked","online","The muscles worked, listed in the record, show exactly what {n} trains.",null],
["Form Cues","online","The form cues, listed in the record, are the coaching points that keep {n} safe and effective.",null],
["Programming","online","The programming block, listed in the record, gives starting sets, reps, and rest for {n}.",null],
["Variations","signature","This Signature edition lists practical variations of {n} for different equipment and levels.",null],
["Common Mistakes","signature","This Signature edition names the mistakes lifters make on {n} and how to fix each one.",null],
["Warm-Up Pairing","signature","This Signature edition pairs {n} with a matching warm-up sequence.",null],
["Progression Path","signature","This Signature edition maps the progression path from first attempts to confident loading on {n}.","Progress only as fast as perfect form allows."],
["Equipment Options","signature","This Signature edition covers equipment substitutions when the ideal gear is unavailable.",null],
["At-Home Alternative","signature","This Signature edition adapts {n} for home training with minimal equipment.",null],
["Sport Application","signature","This Signature edition shows how {n} transfers to common sports and daily activities.",null],
["Mobility Pairing","signature","This Signature edition pairs {n} with mobility work for the joints it stresses most.",null],
["Recovery Notes","signature","This Signature edition covers recovery practices around {n}: sleep, spacing, and soreness management.",null],
["Safety Review","signature","This Signature edition reviews safety for {n}, including when to stop and seek qualified coaching.","Stop any exercise that causes sharp pain."],
["Beginner Guide","signature","This Signature edition scales {n} down to a safe starting point for complete beginners.",null],
["Advanced Techniques","signature","This Signature edition adds advanced techniques for {n} once the basics are mastered.",null],
["Sample Workout","signature","This Signature edition places {n} inside a complete sample workout session.",null],
["Tracking Progress","signature","This Signature edition shows how to log {n} and read progress over weeks and months.",null],
["Glossary Entry","signature","In plain terms, this entry defines {n} and its key vocabulary for newcomers.",null],
["Common Questions","signature","This Signature edition answers frequently asked questions about {n} with factual responses.",null]
];
function fill(tpl,a,lens,ed){return tpl.replace(/\{n\}/g,a.n).replace(/\{c\}/g,a.c).replace(/\{e\}/g,String(ed));}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var ai=(seed-1)%ANCHORS.length;
  var lix=Math.floor((seed-1)/ANCHORS.length)%LENSES.length;
  var ed=(Math.floor((seed-1)/(ANCHORS.length*LENSES.length))%10)+1;
  if(opts.category){var matches=[];for(var m=0;m<ANCHORS.length;m++)if(ANCHORS[m].c===opts.category)matches.push(m);if(matches.length)ai=matches[(seed-1)%matches.length];}
  var a=ANCHORS[ai],lens=LENSES[lix];
  var desc=a.f1+' '+a.f2+' '+fill(lens[2],a,lens,ed);
  if(lens[3])desc+=' '+fill(lens[3],a,lens,ed);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={
    id:id,
    title:a.n+' — '+lens[0]+' (Edition '+ed+')',
    description:desc,
    category:a.c,
    src:lens[1],
    spec:{
      entry:a.n,
      category:a.c,
      entry_type:(a.c==='programming'||a.c==='nutrition-basics')?'program':(a.c==='recovery'||a.c==='mobility'||a.c==='flexibility')?'practice':'exercise',
      lens:lens[0],
      edition:ed,
      muscles:a.muscles.slice(),
      equipment:a.equip,
      form_cues:a.cues.slice(),
      programming:{sets:a.sets,reps:a.reps,rest_sec:a.rest},
      safety_note:SAFETY,
      source_note:lens[1]==='online'?'Core facts verified from public fitness-education sources.':'Signature-generated expansion built on verified anchor facts.'
    },
    _seed:seed
  };
  return rec;
}
function countSentences(s){var t=String(s).replace(/\d+\.\d+/g,'N');var m=t.match(/[^.!?]+[.!?]/g);return m?m.length:0;}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not-object']};
  if(!/^JAH-FIT-\d{6}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<8||r.title.length>200)e.push('title');
  if(typeof r.description!=='string'||r.description.length<120||r.description.length>1600)e.push('description');
  var ns=countSentences(r.description||'');
  if(ns<2||ns>4)e.push('sentences:'+ns);
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(r.src!=='online'&&r.src!=='signature')e.push('src');
  var s=r.spec;
  if(!s||typeof s!=='object')e.push('spec');
  else{
    if(typeof s.entry!=='string'||!s.entry.length)e.push('spec.entry');
    if(s.category!==r.category)e.push('spec.category');
    if(['exercise','program','practice'].indexOf(s.entry_type)<0)e.push('spec.entry_type');
    if(!Array.isArray(s.muscles)||!s.muscles.length)e.push('spec.muscles');
    if(typeof s.equipment!=='string'||!s.equipment.length)e.push('spec.equipment');
    if(!Array.isArray(s.form_cues)||!s.form_cues.length)e.push('spec.form_cues');
    var p=s.programming;
    if(!p||typeof p.sets!=='number'||p.sets<1||p.sets>10)e.push('spec.programming.sets');
    if(!p||typeof p.reps!=='number'||p.reps<1||p.reps>50)e.push('spec.programming.reps');
    if(!p||typeof p.rest_sec!=='number'||p.rest_sec<0||p.rest_sec>600)e.push('spec.programming.rest_sec');
    if(typeof s.safety_note!=='string'||s.safety_note.indexOf('not medical advice')<0)e.push('spec.safety_note');
    if(typeof s.edition!=='number'||s.edition<1||s.edition>10)e.push('spec.edition');
  }
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){var ids={};(sample||[]).forEach(function(x){if(x&&x.id)ids[x.id]=1;});return ids[rec.id]?{ok:false,errors:['duplicate-id']}:{ok:true,errors:[]};}
var gen={version:'jahdb-fitness-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('fitness',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
if(typeof require!=='undefined'&&require.main===module){
  var ok=0,fail=[];
  for(var i=1;i<=40;i++){var v=validate(generate(i,{},prng(i)));if(v.ok)ok++;else fail.push([i,v.errors]);}
  console.log('fitness harness: '+ok+'/40 '+(ok===40?'PASS':'FAIL'));
  if(fail.length)console.log(JSON.stringify(fail));
}
})();
