(function(){'use strict';
/* The The Personal Challenge Calendar generator — jahdb-gen-personal-challenge-calendar-pub-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-PERSONAL-CHALLENGE-CALENDAR-PUB-";
var GENVER="jahdb-gen-personal-challenge-calendar-pub-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The 7-Day Starter",
  "The Kindness Week",
  "The Tidy Seven",
  "The Gratitude Week",
  "The Walk Week",
  "The Read Week",
  "The Water Week",
  "The Compliment Week",
  "The Early-Bed Week",
  "The No-Complaint Week",
  "The Sketch Week",
  "The Stretch Week"
 ],
 "Compounded": [
  "The 14-Day Fitness",
  "The 21-Day Habit",
  "The Creative Fortnight",
  "The Declutter Fortnight",
  "The Mindful 14",
  "The Savings Sprint",
  "The Social 14",
  "The Learning Fortnight",
  "The Cooking 14",
  "The Outdoor 14",
  "The Writing Fortnight",
  "The Music 14"
 ],
 "Advanced": [
  "The 30-Day Transformation",
  "The 75-Day Hard-ish",
  "The 100-Day Project",
  "The Year-Long Quest",
  "The Team Challenge",
  "The Charity Challenge",
  "The Comeback Calendar",
  "The Mastery Year",
  "Designing Challenges for Others",
  "Masterclass: The Streak Science"
 ]
};
var BLURBS={
 "The 7-Day Starter": "One week, one tiny daily challenge: the streak begins.",
 "The Kindness Week": "Seven days of small kindnesses: the challenge that gives back.",
 "The Tidy Seven": "One zone a day for a week: the visible transformation.",
 "The Gratitude Week": "Daily gratitudes, escalating: the mood challenge.",
 "The Walk Week": "A daily walk, growing longer: the simplest streak.",
 "The Read Week": "Ten pages daily: the book finishes itself.",
 "The Water Week": "Hydration tracked daily: the foundational challenge.",
 "The Compliment Week": "One genuine compliment daily: the social streak.",
 "The Early-Bed Week": "In bed by ten, seven nights: the sleep reset.",
 "The No-Complaint Week": "Catch and reframe complaints: the mindset challenge.",
 "The Sketch Week": "One daily doodle: the creativity streak.",
 "The Stretch Week": "Five minutes of stretching daily: the body\u2019s thank-you.",
 "The 14-Day Fitness": "Two weeks of escalating movement: the body wakes up.",
 "The 21-Day Habit": "Three weeks to wire a new habit: the classic formation.",
 "The Creative Fortnight": "Daily making for fourteen days: the portfolio sprint.",
 "The Declutter Fortnight": "A zone a day, deeper: the home transformation.",
 "The Mindful 14": "Daily mindfulness, growing: the calm streak.",
 "The Savings Sprint": "Fourteen days of no-spend creativity: the money challenge.",
 "The Social 14": "Reach out daily: the connection challenge.",
 "The Learning Fortnight": "Daily lessons in one skill: the competence sprint.",
 "The Cooking 14": "A new dish every two days: the delicious challenge.",
 "The Outdoor 14": "Daily time outside: the nature prescription.",
 "The Writing Fortnight": "Daily pages: the book\u2019s beginning.",
 "The Music 14": "Daily practice: the audible progress.",
 "The 30-Day Transformation": "A full month, one focus: the legendary challenge.",
 "The 75-Day Hard-ish": "Seventy-five days of discipline, humanized: the epic streak.",
 "The 100-Day Project": "A hundred days of making: the masterpiece marathon.",
 "The Year-Long Quest": "365 days, one theme: the ultimate calendar.",
 "The Team Challenge": "A group calendar: shared streaks, shared glory.",
 "The Charity Challenge": "Daily actions for a cause: the meaningful streak.",
 "The Comeback Calendar": "Rebuild after a slump: the compassionate restart.",
 "The Mastery Year": "Twelve monthly challenges, escalating: the curriculum of you.",
 "Designing Challenges for Others": "Build calendars for friends: the coach\u2019s skill.",
 "Masterclass: The Streak Science": "Why calendars work: the psychology of don\u2019t-break-the-chain."
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
    name:topic+' — challenge calendar record',
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

var BUILD_CHALLENGE_CALENDAR=(function(){
var THEMES={fitness:['10 push-ups','15-min walk','30-sec plank','20 squats','Stretch routine','Rest + hydrate'],creative:['Sketch for 10 min','Write 200 words','Photo of the day','Hum a melody','Doodle challenge','Share your work'],mindful:['No-phone first hour','5-min breathing','Gratitude list x3','Compliment a stranger','Digital sunset','Journal one page'],tidy:['One drawer','Desktop clear','Closet 10 items out','Fridge clean','Inbox 20 archived','Whole-room reset']};
return function(inp){
  var days=Math.min(31,Math.max(3,parseInt(inp.days,10)||14));
  var theme=inp.theme||'fitness';
  var bank=THEMES[theme]||THEMES.fitness;
  var r=prng(inp.seed||5);
  var items=[];
  for(var d=1;d<=days;d++){items.push('Day '+d+': '+bank[(d-1)%bank.length]+(d%7===0?' (rest day — half effort counts)':''));}
  return {title:days+'-day '+(inp.theme||'personal')+' challenge',intro:'One small daily challenge at '+(inp.difficulty||'easy')+' difficulty. Miss a day? Never miss twice.',
    sections:[{h:'Your calendar',items:items},{h:'Rules',items:['Check off each day where you will see it.','Halve the task rather than skipping it.','Day '+(days)+' gets a real reward you choose now.']}]};
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
gen.builderId="challenge-calendar";
gen.builderFields=[["theme", "Theme", "select", ["fitness", "creative", "mindful", "tidy"]], ["days", "Days", "number", "14"], ["difficulty", "Difficulty", "select", ["easy", "medium", "spicy"]], ["seed", "Seed (optional)", "number", "5"]];
gen.build=BUILD_CHALLENGE_CALENDAR;

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-personal-challenge-calendar',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();