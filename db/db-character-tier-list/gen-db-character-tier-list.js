(function(){'use strict';
/* The The Character Tier List Database generator — jahdb-db-character-tier-list-pub-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-CHARACTER-TIER-LIST-PUB-";
var GENVER="jahdb-db-character-tier-list-pub-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The Power Ranking",
  "The Favorite List",
  "The Design Tier",
  "The Funny Tier",
  "The Cool Tier",
  "The Relatable Tier",
  "The Villain Tier",
  "The Sidekick Tier",
  "The Growth Tier",
  "The Quote Tier",
  "The Outfit Tier",
  "The Entrance Tier"
 ],
 "Compounded": [
  "The Writing Tier",
  "The Impact Tier",
  "The Complexity Tier",
  "The Consistency Tier",
  "The Chemistry Tier",
  "The Redemption Tier",
  "The Tragedy Tier",
  "The Comedy Duo Tier",
  "The Mentor Tier",
  "The Rival Tier",
  "The Ensemble Tier",
  "The Legacy Tier"
 ],
 "Advanced": [
  "The Definitive Ranking",
  "The Cross-Universe",
  "The All-Time",
  "The Community Vote",
  "The Expert Panel",
  "The Data Tier",
  "The Decade Tier",
  "The Hall of Fame",
  "Teaching Tier Craft",
  "Masterclass: The Ranking Mind"
 ]
};
var BLURBS={
 "The Power Ranking": "Who\u2019d win? The strength tier.",
 "The Favorite List": "Pure love: the heart tier.",
 "The Design Tier": "Looks and style: the aesthetic.",
 "The Funny Tier": "Comedy gold: the laugh rank.",
 "The Cool Tier": "Style points: the swagger.",
 "The Relatable Tier": "Seen yourself? The mirror.",
 "The Villain Tier": "Best baddies: the menace.",
 "The Sidekick Tier": "The supports: the loyal.",
 "The Growth Tier": "Best arcs: the development.",
 "The Quote Tier": "Best lines: the memorable.",
 "The Outfit Tier": "Fashion: the runway.",
 "The Entrance Tier": "Best introductions: the arrival.",
 "The Writing Tier": "Best written: the craft.",
 "The Impact Tier": "Story influence: the pivotal.",
 "The Complexity Tier": "Depth and nuance: the literary.",
 "The Consistency Tier": "Never out of character: the reliable.",
 "The Chemistry Tier": "Best dynamics: the pairs.",
 "The Redemption Tier": "Best turnarounds: the forgiven.",
 "The Tragedy Tier": "Saddest fates: the tearjerker.",
 "The Comedy Duo Tier": "Best pairs: the double act.",
 "The Mentor Tier": "Best guides: the wise.",
 "The Rival Tier": "Best rivalries: the clash.",
 "The Ensemble Tier": "Best casts: the team.",
 "The Legacy Tier": "Enduring icons: the timeless.",
 "The Definitive Ranking": "The final word: the canon tier.",
 "The Cross-Universe": "Characters across worlds: the ultimate.",
 "The All-Time": "History\u2019s greatest: the pantheon.",
 "The Community Vote": "The people\u2019s ranking: the democratic.",
 "The Expert Panel": "Critics weigh in: the authoritative.",
 "The Data Tier": "Stats-driven: the analytical.",
 "The Decade Tier": "Ten years of characters: the retrospective.",
 "The Hall of Fame": "Immortalized: the eternal.",
 "Teaching Tier Craft": "Show others: the ranking mentor.",
 "Masterclass: The Ranking Mind": "Why we rank: the psychology of lists."
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
    name:topic+' — tier list record',
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

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-character-tier-list',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();