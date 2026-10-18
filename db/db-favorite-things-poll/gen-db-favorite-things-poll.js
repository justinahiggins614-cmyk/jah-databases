(function(){'use strict';
/* The The Favorite Things Poll Database generator — jahdb-db-favorite-things-poll-pub-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-FAVORITE-THINGS-POLL-PUB-";
var GENVER="jahdb-db-favorite-things-poll-pub-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "Best Film",
  "Best Song",
  "Best Game",
  "Best Book",
  "Best Character",
  "Best Villain",
  "Best Couple",
  "Best Quote",
  "Best Scene",
  "Best Season",
  "Best Ending",
  "Best Opening"
 ],
 "Compounded": [
  "Best Album",
  "Best Series",
  "Best Hero",
  "Best Plot Twist",
  "Best World",
  "Best Soundtrack",
  "Best Adaptation",
  "Best Comeback",
  "Best Debut",
  "Best Finale",
  "Best Crossover",
  "Best Remake"
 ],
 "Advanced": [
  "Best of the Decade",
  "Best of All Time",
  "The Hall of Fame Vote",
  "The People\u2019s Choice",
  "The Critics\u2019 Pick",
  "The Legacy Vote",
  "The Global Vote",
  "The Ultimate Bracket",
  "Teaching Poll Design",
  "Masterclass: Collective Taste"
 ]
};
var BLURBS={
 "Best Film": "The movie vote: the classic.",
 "Best Song": "The anthem: the soundtrack.",
 "Best Game": "The interactive: the champion.",
 "Best Book": "The literary: the beloved.",
 "Best Character": "The icon: the favorite.",
 "Best Villain": "The menace: the loved-to-hate.",
 "Best Couple": "The ship: the romance.",
 "Best Quote": "The line: the memorable.",
 "Best Scene": "The moment: the unforgettable.",
 "Best Season": "The arc: the peak.",
 "Best Ending": "The finale: the satisfying.",
 "Best Opening": "The hook: the arrival.",
 "Best Album": "The full listen: the cohesive.",
 "Best Series": "The show: the binge.",
 "Best Hero": "The protagonist: the admirable.",
 "Best Plot Twist": "The shock: the gasp.",
 "Best World": "The setting: the immersive.",
 "Best Soundtrack": "The score: the emotional.",
 "Best Adaptation": "Page to screen: the faithful.",
 "Best Comeback": "The return: the triumphant.",
 "Best Debut": "The arrival: the promising.",
 "Best Finale": "The goodbye: the perfect.",
 "Best Crossover": "The meeting: the epic.",
 "Best Remake": "The reimagined: the worthy.",
 "Best of the Decade": "Ten years: the retrospective.",
 "Best of All Time": "The ultimate: the pantheon.",
 "The Hall of Fame Vote": "Immortalized: the eternal.",
 "The People\u2019s Choice": "The democratic best: the beloved.",
 "The Critics\u2019 Pick": "The expert best: the acclaimed.",
 "The Legacy Vote": "Enduring greatness: the timeless.",
 "The Global Vote": "Worldwide favorites: the universal.",
 "The Ultimate Bracket": "64 contenders: the mega-tournament.",
 "Teaching Poll Design": "Show others: the democracy mentor.",
 "Masterclass: Collective Taste": "How groups decide best: the sociology of favorites."
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
    name:topic+' — favorites poll record',
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

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-favorite-things-poll',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();