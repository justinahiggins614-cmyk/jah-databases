(function(){'use strict';
/* The The Next Big Community Idea Database generator — jahdb-db-next-big-community-idea-pub-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-NEXT-BIG-COMMUNITY-IDEA-PUB-";
var GENVER="jahdb-db-next-big-community-idea-pub-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The New Ritual",
  "The Mini Event",
  "The Challenge",
  "The Project",
  "The Game",
  "The Club",
  "The Series",
  "The Swap",
  "The Tour",
  "The Feast",
  "The Show",
  "The Cause"
 ],
 "Compounded": [
  "The Festival",
  "The League",
  "The Incubator",
  "The Expedition",
  "The Residency",
  "The Summit",
  "The Campaign",
  "The Platform",
  "The Network",
  "The Lab",
  "The Studio",
  "The Archive"
 ],
 "Advanced": [
  "The Movement",
  "The Institution",
  "The Franchise",
  "The Global",
  "The Legacy",
  "The Renaissance",
  "The Utopia",
  "The Legend",
  "Teaching Foresight",
  "Masterclass: Community Evolution"
 ]
};
var BLURBS={
 "The New Ritual": "A fresh tradition: the heartbeat.",
 "The Mini Event": "Small gathering: the intimate.",
 "The Challenge": "A new contest: the exciting.",
 "The Project": "Make together: the creative.",
 "The Game": "Play together: the fun.",
 "The Club": "A sub-group: the belonging.",
 "The Series": "Recurring content: the anticipated.",
 "The Swap": "Exchange talents: the generous.",
 "The Tour": "Explore together: the adventurous.",
 "The Feast": "Eat together: the delicious.",
 "The Show": "Perform together: the brave.",
 "The Cause": "Unite for good: the meaningful.",
 "The Festival": "The big gathering: the epic.",
 "The League": "Ongoing competition: the thrilling.",
 "The Incubator": "Ideas funded: the innovative.",
 "The Expedition": "Journey together: the adventurous.",
 "The Residency": "Create together: the artistic.",
 "The Summit": "Gather the minds: the insightful.",
 "The Campaign": "The coordinated push: the strategic.",
 "The Platform": "Build the home: the infrastructural.",
 "The Network": "Connect groups: the federated.",
 "The Lab": "Experiment together: the scientific.",
 "The Studio": "The creative home: the productive.",
 "The Archive": "Preserve it all: the historic.",
 "The Movement": "Beyond community: the historic.",
 "The Institution": "The permanent: the legacy.",
 "The Franchise": "The replicable: the scalable.",
 "The Global": "Worldwide: the universal.",
 "The Legacy": "The enduring: the forever.",
 "The Renaissance": "The rebirth: the revitalized.",
 "The Utopia": "The ideal: the aspirational.",
 "The Legend": "The mythic: the unforgettable.",
 "Teaching Foresight": "Show others: the futurist mentor.",
 "Masterclass: Community Evolution": "How groups grow: the sociology of together."
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
    name:topic+' — community idea record',
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

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-next-big-community-idea',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();