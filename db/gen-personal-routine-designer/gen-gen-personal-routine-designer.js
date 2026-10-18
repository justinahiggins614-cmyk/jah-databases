(function(){'use strict';
/* The The Personal Routine Designer generator — jahdb-gen-personal-routine-designer-pub-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-PERSONAL-ROUTINE-DESIGNER-PUB-";
var GENVER="jahdb-gen-personal-routine-designer-pub-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The 3-Anchor Morning",
  "Evening Shutdown Ritual",
  "The Lunch Break Reset",
  "Weekend Anchor Routine",
  "The 5-Minute Tidy Anchor",
  "Hydration Habit Stack",
  "The Commute Upgrade",
  "Single-Tasking Practice",
  "The Bedtime Phone Boundary",
  "Morning Light Protocol",
  "The 2-Minute Evening Prep",
  "Gratitude in 60 Seconds"
 ],
 "Compounded": [
  "The Deep Work Day",
  "The Parent\u2019s Survival Routine",
  "Shift Worker\u2019s Rhythm",
  "The Student\u2019s Study Rhythm",
  "Freelancer\u2019s Flexible Framework",
  "The Fitness-Integrated Day",
  "Digital Sunset Routine",
  "The Weekly Planning Hour",
  "Energy-Mapped Scheduling",
  "The Couple\u2019s Shared Rhythm",
  "The Night Owl\u2019s Routine",
  "The New Parent\u2019s Anchors"
 ],
 "Advanced": [
  "The Ideal Week Template",
  "Ultradian Performance Design",
  "The Seasonal Routine",
  "Crisis-Proof Routines",
  "The Maker\u2019s Marathon Routine",
  "Executive Energy Architecture",
  "The One-Year Routine Experiment",
  "Teaching Routines to Others",
  "The Lifetime Rhythm",
  "Masterclass: Habit Science Applied"
 ]
};
var BLURBS={
 "The 3-Anchor Morning": "Wake, move, plan: three anchors that hold any morning together.",
 "Evening Shutdown Ritual": "A 20-minute sequence that tells your brain the day is done. Sleep comes faster.",
 "The Lunch Break Reset": "Twenty minutes that split the day in two: eat, walk, breathe. Afternoons revive.",
 "Weekend Anchor Routine": "Two anchors keep weekends restorative without rigidity. Rest, structured lightly.",
 "The 5-Minute Tidy Anchor": "Attach tidying to an existing habit. Order maintains itself.",
 "Hydration Habit Stack": "Water with every existing routine: coffee, meals, desk arrival. Hydrated by habit.",
 "The Commute Upgrade": "Turn travel time into learning, planning, or true rest - your choice, on purpose.",
 "Single-Tasking Practice": "One thing at a time, timer on. Attention is the real productivity app.",
 "The Bedtime Phone Boundary": "A charging station outside the bedroom ends the scroll and starts the rest.",
 "Morning Light Protocol": "Bright light within an hour of waking sets the whole day\u2019s energy clock.",
 "The 2-Minute Evening Prep": "Lay out tomorrow\u2019s essentials tonight. Mornings on autopilot.",
 "Gratitude in 60 Seconds": "Three good things before sleep. Small practice, outsized mood effect.",
 "The Deep Work Day": "Two 90-minute focus blocks protected like appointments. Output that surprises you.",
 "The Parent\u2019s Survival Routine": "Anchors that survive school runs and chaos: flexible, forgiving, functional.",
 "Shift Worker\u2019s Rhythm": "Routines that rotate with shifts: sleep anchors that move but never break.",
 "The Student\u2019s Study Rhythm": "Study blocks, active recall, and real breaks: grades follow the rhythm.",
 "Freelancer\u2019s Flexible Framework": "Client work, admin, and creation in a self-directed day that still ends on time.",
 "The Fitness-Integrated Day": "Movement woven in: walks, workouts, and mobility without a gym membership required.",
 "Digital Sunset Routine": "Screens dim and dock an hour before bed. Evenings get quieter and sleep gets deeper.",
 "The Weekly Planning Hour": "Sunday setup: calendar, priorities, meals. The week starts before Monday.",
 "Energy-Mapped Scheduling": "Hard tasks at peak energy, easy tasks in the dip. Work with the brain\u2019s tide.",
 "The Couple\u2019s Shared Rhythm": "Two schedules, one shared anchor: dinner, walk, or wind-down together daily.",
 "The Night Owl\u2019s Routine": "A rhythm for late chronotypes: honoring biology.",
 "The New Parent\u2019s Anchors": "Micro-routines that survive baby chaos: the essentials.",
 "The Ideal Week Template": "Design the perfect week on paper, then negotiate it into reality one block at a time.",
 "Ultradian Performance Design": "90-minute cycles with real recovery: the science-backed high-output day.",
 "The Seasonal Routine": "Routines that shift with daylight and seasons instead of fighting them.",
 "Crisis-Proof Routines": "The minimum viable day: when life explodes, three anchors keep you human.",
 "The Maker\u2019s Marathon Routine": "Long creative days with protected flow: how artists structure deep creative time.",
 "Executive Energy Architecture": "A leader\u2019s day: decisions batched, meetings fenced, thinking time sacred.",
 "The One-Year Routine Experiment": "Evolve one routine quarterly for a year. Documented self-experimentation.",
 "Teaching Routines to Others": "Turn your best routine into a teachable system for family or team.",
 "The Lifetime Rhythm": "A philosophy of days: how decades of good routines compound into a good life.",
 "Masterclass: Habit Science Applied": "Cues, cravings, rewards, and environment design - the full behavioral toolkit."
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
    name:topic+' — routine design record',
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

var BUILD_ROUTINE=(function(){
return function(inp){
  var wake=inp.wake||'07:00', sleep=inp.sleep||'23:00';
  function mins(t){var p=t.split(':');return (+p[0])*60+(+p[1]);}
  function fmt(m){m=((m%1440)+1440)%1440;var h=(m/60)|0,mm=m%60;return (h<10?'0':'')+h+':'+(mm<10?'0':'')+mm;}
  var w=mins(wake), s=mins(sleep); if(s<=w)s+=1440;
  var day=s-w, focusH=parseFloat(inp.focus)||2;
  var blocks=[
    ['Wake + light + water', 20],
    ['Move (walk, stretch, or workout)', 30],
    ['Deep focus block 1', Math.round(focusH*60/2)],
    ['Lunch + true break (no screens ideally)', 45],
    ['Deep focus block 2', Math.round(focusH*60/2)],
    ['Errands / life admin', 30],
    ['Wind-down: dim lights, prep tomorrow', 30]
  ];
  var t=w, items=blocks.map(function(b){var o=fmt(t)+' – '+b[0]+' ('+b[1]+' min)';t+=b[1];return o;});
  items.push(fmt(s-30)+' – In bed, screens off');
  return {title:'Personal routine: '+wake+' to '+sleep,
    intro:'A flexible day built around '+focusH+' focused hours across a '+Math.round(day/60)+'h waking day. Move blocks freely — the order matters more than the clock.',
    sections:[{h:'Your day, block by block',items:items},{h:'Rules that make it stick',items:['Anchor the routine to wake time, not bedtime.','One missed block never cancels the day — resume at the next.','Review weekly: keep what gave energy, cut what drained it.']}]};
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
gen.builderId="routine";
gen.builderFields=[["wake", "Wake time", "time", "07:00"], ["sleep", "Bedtime", "time", "23:00"], ["focus", "Deep focus hours", "number", "2"], ["seed", "Seed (optional)", "number", "7"]];
gen.build=BUILD_ROUTINE;

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-personal-routine-designer',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();