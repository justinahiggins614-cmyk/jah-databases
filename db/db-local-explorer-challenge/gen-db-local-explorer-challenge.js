(function(){'use strict';
/* The The Local Explorer Challenge generator — jahdb-db-local-explorer-challenge-pub-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-LOCAL-EXPLORER-CHALLENGE-PUB-";
var GENVER="jahdb-db-local-explorer-challenge-pub-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The Unvisited Landmark",
  "The New Park",
  "The Local Cafe",
  "The History Plaque Tour",
  "The Farmers Market",
  "The Library Branch",
  "The Viewpoint",
  "The Water Spot",
  "The Main Street Walk",
  "The Community Board",
  "The New Cuisine",
  "The Sunset Spot"
 ],
 "Compounded": [
  "The Hidden Gem Hunt",
  "The 10-Mile Challenge",
  "The Local Legend",
  "The Festival Circuit",
  "The Volunteer Tour",
  "The Food Tour, Local",
  "The Art Hunt",
  "The Nature Within",
  "The Night Map",
  "The Maker Visits",
  "The Sports Local",
  "The Neighbor Interview"
 ],
 "Advanced": [
  "The 50-Mile Conquest",
  "The Town Guide",
  "The Annual Pilgrimage",
  "The Newcomer Welcome",
  "The Preservation Push",
  "The Deep History",
  "The 100-Spot List",
  "The Legacy Map",
  "Teaching Local Exploration",
  "Masterclass: The Sense of Place"
 ]
};
var BLURBS={
 "The Unvisited Landmark": "The attraction you\u2019ve never entered: the obvious, finally.",
 "The New Park": "A park you\u2019ve never picnicked: the green unknown.",
 "The Local Cafe": "The independent spot: the community\u2019s living room.",
 "The History Plaque Tour": "Read them all: the town\u2019s story, posted.",
 "The Farmers Market": "The weekly ritual: the town\u2019s table.",
 "The Library Branch": "Visit every branch: the free university tour.",
 "The Viewpoint": "The highest public spot: the town, surveyed.",
 "The Water Spot": "The nearest water: the blue escape.",
 "The Main Street Walk": "Store by store: the downtown, truly seen.",
 "The Community Board": "Read every flyer: the town\u2019s bulletin, decoded.",
 "The New Cuisine": "The restaurant from a cuisine you\u2019ve never tried: the delicious unknown.",
 "The Sunset Spot": "Find your town\u2019s best sunset: the daily show\u2019s venue.",
 "The Hidden Gem Hunt": "Ask five locals, visit all five answers: the insider\u2019s map.",
 "The 10-Mile Challenge": "Visit somewhere new within 10 miles weekly: the conquest.",
 "The Local Legend": "Research the town\u2019s strangest story, then visit the site.",
 "The Festival Circuit": "Every local festival this year: the town\u2019s calendar, lived.",
 "The Volunteer Tour": "Serve at five different places: the town, from inside.",
 "The Food Tour, Local": "The definitive local eats list, completed: the delicious quest.",
 "The Art Hunt": "Murals, galleries, studios: the creative map.",
 "The Nature Within": "The wild pockets inside city limits: the secret green.",
 "The Night Map": "The town after dark, safely: the second city.",
 "The Maker Visits": "Workshops and studios open to visitors: the hands-on map.",
 "The Sports Local": "The minor team, the park league: the hometown cheer.",
 "The Neighbor Interview": "Learn the street\u2019s stories: the human atlas.",
 "The 50-Mile Conquest": "Everything worth seeing in 50 miles: the regional mastery.",
 "The Town Guide": "Write the guide you wish existed: the explorer\u2019s gift.",
 "The Annual Pilgrimage": "The local wonder, visited yearly: the rooted ritual.",
 "The Newcomer Welcome": "Show new arrivals your map: the generous local.",
 "The Preservation Push": "Advocate for a local gem: the explorer as guardian.",
 "The Deep History": "Archives, elders, old maps: the town\u2019s deep past.",
 "The 100-Spot List": "A hundred local spots, checked off: the ultimate quest.",
 "The Legacy Map": "Your map, passed on: the gift of place.",
 "Teaching Local Exploration": "Lead the tour: the ambassador\u2019s joy.",
 "Masterclass: The Sense of Place": "Why rootedness matters: the geography of belonging."
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
    name:topic+' — local exploration record',
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

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-local-explorer-challenge',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();