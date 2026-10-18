(function(){'use strict';
/* The The Life Adventure Generator generator — jahdb-gen-life-adventure-generator-pub-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-LIFE-ADVENTURE-GENERATOR-PUB-";
var GENVER="jahdb-gen-life-adventure-generator-pub-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The Hour Mission",
  "The Afternoon Escape",
  "The $0 Adventure",
  "The Food Mission",
  "The View Hunt",
  "The History Hour",
  "The Park Circuit",
  "The Photo Mission",
  "The Coffee Crawl",
  "The Bookstore Day",
  "The Sunset Mission",
  "The Rainy Pivot"
 ],
 "Compounded": [
  "The Full Day Quest",
  "The City Deep Dive",
  "The Nature Day",
  "The Cultural Day",
  "The $100 Day",
  "The Friend Adventure",
  "The Solo Quest",
  "The Night Adventure",
  "The Water Day",
  "The Mountain Day",
  "The Small Town",
  "The Festival Day"
 ],
 "Advanced": [
  "The Weekend Epic",
  "The 7-Day Quest",
  "The $300 Expedition",
  "The Group Expedition",
  "The Solo Pilgrimage",
  "The Annual Adventure",
  "The Impossible Itinerary",
  "The Legacy Journey",
  "Teaching Adventure Design",
  "Masterclass: The Adventure Mindset"
 ]
};
var BLURBS={
 "The Hour Mission": "Sixty minutes, one mission: the pocket adventure.",
 "The Afternoon Escape": "Four free hours, fully designed: the classic.",
 "The $0 Adventure": "No budget, full fun: the proof of concept.",
 "The Food Mission": "Eat your way through the day: the delicious plan.",
 "The View Hunt": "Chase the best views: the scenic mission.",
 "The History Hour": "One historic site, deeply: the time-travel lite.",
 "The Park Circuit": "Three parks, one day: the green tour.",
 "The Photo Mission": "A shot list and a route: the artistic outing.",
 "The Coffee Crawl": "Three cafes, one afternoon: the caffeinated quest.",
 "The Bookstore Day": "Browse, read, repeat: the literary adventure.",
 "The Sunset Mission": "Engineered golden hour: the day\u2019s finale, planned.",
 "The Rainy Pivot": "The indoor version: the weatherproof plan.",
 "The Full Day Quest": "Dawn to dusk, mission-driven: the legendary day.",
 "The City Deep Dive": "One neighborhood, fully: the urban expedition.",
 "The Nature Day": "Trail, water, sky: the wild reset.",
 "The Cultural Day": "Museums, food, performance: the civilized adventure.",
 "The $100 Day": "A hundred dollars, maximized: the budget epic.",
 "The Friend Adventure": "Designed for the crew: the shared legend.",
 "The Solo Quest": "Alone and glorious: the personal epic.",
 "The Night Adventure": "After dark, safely: the city\u2019s second shift.",
 "The Water Day": "Built around water: the blue plan.",
 "The Mountain Day": "Up and down: the vertical adventure.",
 "The Small Town": "One town, fully explored: the micro-travel.",
 "The Festival Day": "A full festival, strategically: the joyful marathon.",
 "The Weekend Epic": "Two days, one saga: the mini-odyssey.",
 "The 7-Day Quest": "A week-long themed journey: the true adventure.",
 "The $300 Expedition": "Real budget, real distance: the serious trip.",
 "The Group Expedition": "The crew\u2019s grand plan: the shared epic.",
 "The Solo Pilgrimage": "Alone with a purpose: the transformative journey.",
 "The Annual Adventure": "The year\u2019s centerpiece trip: the tradition.",
 "The Impossible Itinerary": "The dream trip, planned: the someday, scheduled.",
 "The Legacy Journey": "The trip they\u2019ll tell stories about: the legend.",
 "Teaching Adventure Design": "Plan for others: the guide\u2019s craft.",
 "Masterclass: The Adventure Mindset": "Living adventurously: the philosophy of the quest."
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
    name:topic+' — adventure plan record',
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

var BUILD_ADVENTURE_PLAN=(function(){
var HOOKS=['Follow the water: rivers, lakes, or coast.','Chase the high ground: hills, towers, rooftops (legal ones).','Eat your way through it: one dish per stop.','Hunt the weird: odd museums, strange statues, local legends.','Go analog: paper map, no GPS, ask humans.'];
return function(inp){
  var r=prng(inp.seed||17);
  var time=inp.time||'a free afternoon', budget=inp.budget||'$30';
  return {title:'Your life adventure: '+pick(HOOKS,r),intro:'A personalized plan for '+time+' on about '+budget+', tuned to '+(inp.interests||'curiosity')+'.',
    sections:[{h:'The mission',text:pick(HOOKS,r)+' Give the day a name — named days get remembered.'},{h:'The plan',items:['Hour 0: set out with one rule (e.g. turn left at every choice).','Midpoint: the meal stop — sit down, no rushing.','Hour X-1: the wildcard — ask a local for one recommendation and do it.','End: the debrief — best moment, funniest moment, one photo.']},{h:'Pack list',items:['Water + one snack more than you think','Charged phone + a little cash','Comfortable shoes (non-negotiable)']}]};
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
gen.builderId="adventure-plan";
gen.builderFields=[["time", "Time available", "select", ["an hour", "a free afternoon", "a full day", "a whole weekend"]], ["budget", "Budget", "select", ["$0", " $30", "$100", "$300"]], ["interests", "Interests", "text", "food, views, history"], ["seed", "Seed (optional)", "number", "17"]];
gen.build=BUILD_ADVENTURE_PLAN;

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-life-adventure-generator',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();