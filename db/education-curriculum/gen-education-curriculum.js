(function(){'use strict';
/* JAH Education Database generator — deterministic, every record validated.
   Signature-generated lessons: full learning records, never stubs. Compact JSON. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['math','science','language','history','arts','assessment'];
var PREFIX='JAH-EDU-';
var GRADES=['K-2','3-5','6-8','9-12','college'];
var GMAX={'K-2':2,'3-5':3,'6-8':4,'9-12':5,'college':5};
var SUBJECT={math:'Mathematics',science:'Science',language:'Language Arts',history:'History & Social Studies',arts:'Arts & Music',assessment:'Assessment & Study Skills'};
var TOPICS={
 math:[['Mental math sprints','addition and subtraction fluency'],['Fraction kitchens','adding fractions'],['Decimal market day','multiplying decimals'],['Ratio recipes','proportions'],['Geometry of origami','angles and symmetry'],['Probability carnivals','likelihood'],['Algebra tile puzzles','one-step equations'],['Data detectives','mean, median, mode'],['Measurement Olympics','unit conversions'],['Pattern architects','sequences'],['Percent discount labs','percent of a quantity'],['Coordinate treasure maps','ordered pairs']],
 science:[['Volcano in a bottle','chemical reactions'],['Water cycle journeys','evaporation and condensation'],['Magnet explorers','poles and attraction'],['Simple machine workshops','levers and pulleys'],['Ecosystem jars','food chains'],['Rock cycle hikes','rock types'],['Shadow clocks','Earth rotation'],['Circuit builders','series and parallel'],['Plant growth trials','experiment variables'],['Weather station week','measuring weather'],['Fossil dig simulations','evidence of past life'],['Star story nights','constellations']],
 language:[['Sentence surgeons','fixing fragments'],['Metaphor kitchens','comparisons'],['Debate clubs','persuasive structure'],['Poetry slams','rhythm and imagery'],['Root word gardens','prefixes and suffixes'],['Dialogue workshops','punctuating speech'],['Story mountain climbs','plot structure'],['Editorial boards','thesis and evidence'],['Vocabulary vaults','context clues'],['Letter writing labs','tone and audience']],
 history:[['Timeline tapestry','ordering eras'],['Artifact mysteries','inferring from objects'],['Map skill quests','reading historical maps'],['Biography snapshots','lives that shaped events'],['Debate the decision','historical dilemmas'],['Newspaper time travel','period headlines'],['Culture fairs','customs across civilizations'],['Cause and effect chains','why events unfolded'],['Primary source labs','letters and diaries'],['Monument studies','memory in stone']],
 arts:[['Color wheel kitchens','mixing primaries'],['Perspective hallways','one-point drawing'],['Rhythm circles','beat and tempo'],['Texture rubbings','surface in art'],['Portrait studios','face proportion'],['Mural planning','composition'],['Instrument petting zoos','sound families'],['Dance phrase labs','movement sequences'],['Printmaking stations','relief techniques'],['Design challenges','form and function']],
 assessment:[['Exit ticket routines','formative checks'],['Rubric builders','clear criteria'],['Self-assessment mirrors','student reflection'],['Peer review circles','specific feedback'],['Portfolio curation','growth over time'],['Quiz design studios','fair items'],['Study plan workshops','spaced practice'],['Test calm toolkits','managing anxiety'],['Note-taking systems','Cornell and sketchnote'],['Goal conferences','one-on-one targets']]
};
var SCI_FACTS=[['How many planets orbit the Sun?',8],['At what temperature does water boil at sea level, in degrees Celsius?',100],['How many legs does an insect have?',6],['How many days are in a leap year?',366],['How many bones are in the adult human body?',206],['How many chambers does the human heart have?',4],['How many colors are in a rainbow?',7],['How many moons does Mars have?',2],['How many strings does a standard violin have?',4],['How many sides does a hexagon have?',6],['How many minutes are in one hour?',60],['How many players are on a soccer team on the field?',11]];
var CONCEPTS={
 language:[['Which part of speech names a person, place, or thing?','noun'],['What do we call a word that describes a noun?','adjective'],['What punctuation ends a question?','a question mark'],['What is a comparison using like or as?','a simile'],['What is the main idea sentence of a paragraph?','the topic sentence'],['Which part of speech shows action?','a verb'],['What is a word with a similar meaning?','a synonym'],['What are words that sound alike but are spelled differently?','homophones']],
 history:[['In which year did the Western Roman Empire fall?','476 CE'],['On what date did Apollo 11 land on the Moon?','July 20, 1969'],['When did the French Revolution begin?','1789'],['In what years was World War II fought?','1939 to 1945'],['In which year was the Magna Carta signed?','1215'],['When did Columbus reach the Americas?','1492'],['In which year was US independence declared?','1776'],['On what date did the Berlin Wall fall?','November 9, 1989']],
 arts:[['Which three colors are the traditional primaries?','red, yellow, and blue'],['What is the complement of blue?','orange'],['What symbol raises a note a half step?','a sharp'],['How many beats does a whole note get in 4/4?','four'],['What is three-dimensional art called?','sculpture'],['Which family is the violin in?','the strings'],['What creates depth illusion in drawing?','perspective'],['What is the speed of the beat called?','tempo']],
 assessment:[['What is a formative assessment?','a check during instruction'],['What is a rubric for?','making criteria clear'],['What is spaced practice?','study spread over time'],['What is an exit ticket?','a short end-of-lesson check'],['What makes feedback effective?','specific, timely, actionable'],['What is self-assessment?','judging own work vs criteria'],['What is a portfolio?','a collection showing growth'],['What is a diagnostic assessment?','finding what learners know first']]
};
var ARITH_Q=[['A baker makes {a} loaves, then {b} more. How many in all?','+'],['A shelf holds {a} books. {b} are borrowed. How many remain?','-'],['Each box holds {a} crayons. There are {b} boxes. How many?','*'],['A garden has {a} rows of {b} plants. How many plants?','*'],['A class collects {a} cans, then {b} more. Total?','+'],['A train carries {a} riders. {b} get off. How many left?','-']];
var STEP_T=['Hook: pose "{t}" and collect first ideas.','Model "{t}" with one worked example.','Pairs practice "{t}" with the materials.','Apply "{t}" to a fresh situation.','Probe understanding of "{t}" mid-lesson.','Learners summarize "{t}" in own words.'];
var OBJ_T=['Explain {t} in own words.','Apply {t} to a new problem.','Compare two examples of {t}.','Create an original example of {t}.','Judge a peer example of {t} vs criteria.'];
var MAT_POOL=['whiteboard and markers','printed handouts','rulers and pencils','colored paper','scissors and glue','shared tablets','index cards','timers','chart paper','manipulative kits'];
function makeExercises(rnd,cat){
  var ex=[],n=2,i;
  if(cat==='math'){
    for(i=0;i<n;i++){
      var q=pick(ARITH_Q,rnd),op=q[1],a=ri(rnd,3,49),b=ri(rnd,3,49);
      if(op==='-'){var mx=Math.max(a,b),mn=Math.min(a,b);a=mx;b=mn;}
      var ans=op==='+'?a+b:(op==='-'?a-b:a*b);
      ex.push({question:q[0].replace('{a}',a).replace('{b}',b),kind:'arithmetic',a:a,b:b,op:op,answer:ans});
    }
  }else if(cat==='science'){
    var used={};
    for(i=0;i<n;i++){var f=pick(SCI_FACTS,rnd);if(used[f[0]]){i--;continue;}used[f[0]]=1;
      ex.push({question:f[0],kind:'numeric-fact',answer:f[1]});}
  }else{
    var pool=CONCEPTS[cat]||CONCEPTS.assessment,used2={};
    for(i=0;i<n;i++){var c=pick(pool,rnd);if(used2[c[0]]){i--;continue;}used2[c[0]]=1;
      ex.push({question:c[0],kind:'concept',answer:c[1]});}
  }
  return ex;
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var tp=pick(TOPICS[cat],rnd);
  var topic=tp[0],focus=tp[1];
  var grade=pick(GRADES,rnd);
  var diff=ri(rnd,1,GMAX[grade]);
  var dur=ri(rnd,3,12)*10;
  var id=PREFIX+String(seed).padStart(7,'0');
  var objectives=[],steps=[],i;
  for(i=0;i<3;i++)objectives.push(pick(OBJ_T,rnd).replace('{t}',topic.toLowerCase()));
  for(i=0;i<3;i++)steps.push(pick(STEP_T,rnd).replace(/\{t\}/g,topic));
  var mats=[],seen={};
  while(mats.length<3){var m=pick(MAT_POOL,rnd);if(!seen[m]){seen[m]=1;mats.push(m);}}
  var ex=makeExercises(rnd,cat);
  return {
    id:id,lesson_id:id,
    title:'Lesson: '+topic,
    category:cat,subject:SUBJECT[cat],grade_level:grade,topic:topic,
    summary:'A '+dur+'-minute '+grade+' '+SUBJECT[cat].toLowerCase()+' lesson on '+topic.toLowerCase()+' ('+focus+'), moving from guided examples to independent practice with '+ex.length+' exercises.',
    objectives:objectives,materials:mats,lesson_steps:steps,exercises:ex,
    assessment:{method:pick(['quiz','project rubric','checklist','exit tickets','peer review'],rnd),items:ex.map(function(x){return x.question;}),duration_minutes:ri(rnd,10,30)},
    duration_minutes:dur,difficulty:diff,
    standards:'Grade-band '+grade+' goals for '+focus+'.',
    source:'signature',creation_mode:'SIGNATURE-GENERATED',_seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-EDU-\d{7}$/.test(r.id||''))e.push('id');
  if(r.lesson_id!==r.id)e.push('lesson_id');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(r.subject!==SUBJECT[r.category])e.push('subject');
  if(GRADES.indexOf(r.grade_level)<0)e.push('grade_level');
  if(typeof r.difficulty!=='number'||r.difficulty<1||r.difficulty>5)e.push('difficulty');
  else if(r.difficulty>GMAX[r.grade_level])e.push('difficulty>grade-band max');
  if(typeof r.duration_minutes!=='number'||r.duration_minutes<15||r.duration_minutes>180)e.push('duration');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.topic!=='string'||!r.topic.length)e.push('topic');
  if(typeof r.summary!=='string'||r.summary.length<40)e.push('summary');
  if(!Array.isArray(r.objectives)||r.objectives.length<2)e.push('objectives');
  if(!Array.isArray(r.materials)||r.materials.length<2)e.push('materials');
  if(!Array.isArray(r.lesson_steps)||r.lesson_steps.length<2)e.push('lesson_steps');
  if(!Array.isArray(r.exercises)||r.exercises.length<2)e.push('exercises');
  else r.exercises.forEach(function(x){
    if(typeof x.question!=='string'||x.question.charAt(x.question.length-1)!=='?')e.push('exercise-question');
    if(x.kind==='arithmetic'){
      if(['+','-','*'].indexOf(x.op)<0)e.push('exercise-op');
      var exp=x.op==='+'?x.a+x.b:(x.op==='-'?x.a-x.b:x.a*x.b);
      if(exp!==x.answer)e.push('exercise-answer-recompute');
    }else if(x.kind==='numeric-fact'){if(typeof x.answer!=='number')e.push('exercise-numeric');}
    else if(x.kind==='concept'){if(typeof x.answer!=='string'||!x.answer.length)e.push('exercise-concept');}
    else e.push('exercise-kind');
  });
  var as=r.assessment;
  if(!as||typeof as.method!=='string'||!as.method.length)e.push('assessment-method');
  else if(!Array.isArray(as.items)||as.items.length<2)e.push('assessment-items');
  if(typeof r.standards!=='string'||!r.standards.length)e.push('standards');
  if(r.source==='signature'){
    if(r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
  }else if(r.source==='online'){
    if(typeof r.source_ref!=='string'||!/^https?:\/\//.test(r.source_ref))e.push('source_ref');
  }else e.push('source');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-education-curriculum-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('education-curriculum',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
