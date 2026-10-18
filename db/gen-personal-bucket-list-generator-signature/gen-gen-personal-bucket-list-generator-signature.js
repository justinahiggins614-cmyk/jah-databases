(function(){'use strict';
/* The The Personal Bucket List Generator Signature generator — jahdb-gen-personal-bucket-list-generator-signature-sig-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-PERSONAL-BUCKET-LIST-GENERATOR-SIG-";
var GENVER="jahdb-gen-personal-bucket-list-generator-signature-sig-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "First Five Dreams",
  "The Weekend-Sized Dream",
  "The Free Dream",
  "Learn-One-Thing Wish",
  "The Kindness Wish",
  "Taste Adventure Wish",
  "The Nature Wish",
  "Reconnect Wish",
  "The Tiny Dare",
  "Create-Once Wish",
  "The Local Wonder",
  "The Rest Dream"
 ],
 "Compounded": [
  "The Big Trip Wish",
  "Master-a-Skill Wish",
  "The Performance Wish",
  "Build Something Real",
  "The Language Wish",
  "Serve Deeply Wish",
  "The Wild Challenge",
  "Meet Your Hero",
  "The Creative Milestone",
  "Home Dream Wish",
  "The Tradition Wish",
  "Forgive and Free Wish"
 ],
 "Advanced": [
  "The Lifetime Quest",
  "The Legacy Wish",
  "Seven Continents Dream",
  "The Mastery Decade",
  "Write the Book Wish",
  "The Giving Fortune",
  "The Impossible Wish",
  "The Completed List",
  "Passing the List On",
  "Masterclass: Designing a Life"
 ]
};
var BLURBS={
 "First Five Dreams": "Write the first five wishes that come to mind. No judging, just capturing. The list begins.",
 "The Weekend-Sized Dream": "One dream doable this weekend: proof the list is for living, not shelving.",
 "The Free Dream": "A wish costing nothing: sunrise, letters, stargazing. Priceless counts.",
 "Learn-One-Thing Wish": "A skill wish for this month: the list teaches as well as thrills.",
 "The Kindness Wish": "A dream about giving: the list is not only about you.",
 "Taste Adventure Wish": "A food dream: the dish, the city, the kitchen to learn it in.",
 "The Nature Wish": "A wild-place wish: the trail, the water, the sky you need to see.",
 "Reconnect Wish": "A person you miss: the call, the visit, the letter the list demands.",
 "The Tiny Dare": "A two-minute courage wish: the small brave that trains the big brave.",
 "Create-Once Wish": "Make one thing this month: the list as muse.",
 "The Local Wonder": "Something amazing within an hour: wonder does not require airfare.",
 "The Rest Dream": "A wish for deep rest: the list honors recovery too.",
 "The Big Trip Wish": "The journey of a lifetime, planned in stages: dreaming with a map.",
 "Master-a-Skill Wish": "A year-long skill quest: the list as curriculum.",
 "The Performance Wish": "Stage, mic, or gallery: the wish to be witnessed.",
 "Build Something Real": "A physical creation wish: the list you can touch.",
 "The Language Wish": "Hold a real conversation in a new tongue: the wish that opens worlds.",
 "Serve Deeply Wish": "A service wish with real commitment: the list that gives back.",
 "The Wild Challenge": "A physical feat wish: the body\u2019s entry on the list.",
 "Meet Your Hero": "The encounter wish: planned, respectful, unforgettable.",
 "The Creative Milestone": "Finish the book, album, or film: the wish with a deadline.",
 "Home Dream Wish": "The dwelling wish: designed, saved for, earned.",
 "The Tradition Wish": "Start something worth repeating: the wish that outlives you.",
 "Forgive and Free Wish": "The inner wish: what the list asks you to release.",
 "The Lifetime Quest": "One wish so big it organizes decades: the north star entry.",
 "The Legacy Wish": "What outlives you: the wish for after.",
 "Seven Continents Dream": "The ultimate travel arc: planned across a lifetime.",
 "The Mastery Decade": "Ten years, one craft, true mastery: the list as life\u2019s work.",
 "Write the Book Wish": "Your story, bound: the wish that tells it all.",
 "The Giving Fortune": "A philanthropy wish at scale: the list that changes other lists.",
 "The Impossible Wish": "The one they said couldn\u2019t be done: the list\u2019s beautiful defiance.",
 "The Completed List": "What finishing looks like: the list as a life, well-lived.",
 "Passing the List On": "Teach someone to dream on paper: the wish that multiplies.",
 "Masterclass: Designing a Life": "From bucket list to life architecture: the full philosophy."
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
    name:topic+' — bucket list record',
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

var BUILD_BUCKET_LIST=(function(){
var CATS={'Create':['Finish a 30-day creative streak','Make something and gift it','Learn one party trick well'],'Learn':['Hold a 5-minute conversation in a new language','Take a free online course to completion','Read 12 books in a year'],'Explore':['Watch sunrise from a high place','Visit a town you cannot pronounce','Take a train with no plan'],'Connect':['Host a dinner for old friends','Write letters to three people','Volunteer for one full day'],'Dare':['Perform on a stage once','Try the food that scares you','Do one thing that makes your hands shake (safely)']};
return function(inp){
  var r=prng(inp.seed||11);
  var interests=(inp.interests||'Create,Learn,Explore').split(',').map(function(s){return s.trim();});
  var cats=interests.filter(function(c){return CATS[c];});
  if(!cats.length)cats=['Create','Learn','Explore'];
  var sections=cats.map(function(c){
    return {h:c+' — pick one this season',items:shuffle(CATS[c],r).slice(0,2)};
  });
  sections.push({h:'How the list stays alive',items:['Review every 3 months; done items get a date and a story.','One item must scare you a little — comfort never made a memory.','Share the list with one person who will hold you to it.']});
  return {title:'Your evolving bucket list',intro:'Built around '+(inp.timeframe||'the next year')+' on a '+(inp.budget||'flexible')+' budget. The list grows as you do — check, add, repeat.',sections:sections};
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
gen.builderId="bucket-list";
gen.builderFields=[["interests", "Interests (comma separated)", "text", "Create,Learn,Explore"], ["timeframe", "Timeframe", "select", ["the next year", "the next 5 years", "lifetime"]], ["budget", "Budget", "select", ["tight", "flexible", "generous"]], ["seed", "Seed (optional)", "number", "11"]];
gen.build=BUILD_BUCKET_LIST;

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-personal-bucket-list-generator-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();