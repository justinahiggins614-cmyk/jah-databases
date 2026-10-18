(function(){'use strict';
/* The The Fan Theory Playground generator — jahdb-gen-fan-theory-playground-pub-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-FAN-THEORY-PLAYGROUND-PUB-";
var GENVER="jahdb-gen-fan-theory-playground-pub-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The Hidden Identity",
  "The Prophecy",
  "The Connection",
  "The Motive",
  "The Timeline",
  "The Symbol",
  "The Foreshadow",
  "The Red Herring",
  "The Cameo",
  "The Title Theory",
  "The Color Code",
  "The Number Game"
 ],
 "Compounded": [
  "The Loop",
  "The Unreliable Narrator",
  "The Simulation",
  "The Dream",
  "The Time Travel",
  "The Multiverse",
  "The Secret War",
  "The Bloodline",
  "The Artifact",
  "The Prophecy Twist",
  "The Villain\u2019s Reason",
  "The Endgame"
 ],
 "Advanced": [
  "The Unified Theory",
  "The Author\u2019s Intent",
  "The Cultural Theory",
  "The Mythic Parallel",
  "The Definitive Ranking",
  "The Canon Reconciliation",
  "The Sequel Prediction",
  "The Legacy Theory",
  "Teaching Theory Craft",
  "Masterclass: Narrative Theory"
 ]
};
var BLURBS={
 "The Hidden Identity": "The minor character\u2019s secret: the classic.",
 "The Prophecy": "What\u2019s foretold: the destined.",
 "The Connection": "Two things are one: the merge.",
 "The Motive": "Why they did it: the psychology.",
 "The Timeline": "When it happened: the chronology.",
 "The Symbol": "What it means: the reading.",
 "The Foreshadow": "The hint planted: the detective.",
 "The Red Herring": "The deliberate mislead: the trick.",
 "The Cameo": "Who\u2019s hiding: the spotter.",
 "The Title Theory": "The name\u2019s secret: the linguistic.",
 "The Color Code": "Hues with meaning: the visual.",
 "The Number Game": "Digits that matter: the pattern.",
 "The Loop": "Events repeat: the cycle.",
 "The Unreliable Narrator": "The liar\u2019s tale: the twist.",
 "The Simulation": "It\u2019s all staged: the meta.",
 "The Dream": "None of it\u2019s real: the philosophical.",
 "The Time Travel": "The past changed: the paradox.",
 "The Multiverse": "Every choice branches: the infinite.",
 "The Secret War": "The hidden conflict: the epic.",
 "The Bloodline": "The hidden heir: the dynastic.",
 "The Artifact": "The object\u2019s power: the MacGuffin.",
 "The Prophecy Twist": "The foretold, subverted: the clever.",
 "The Villain\u2019s Reason": "The other side: the sympathetic.",
 "The Endgame": "How it ends: the bold prediction.",
 "The Unified Theory": "Everything connects: the grand.",
 "The Author\u2019s Intent": "What they meant: the meta-read.",
 "The Cultural Theory": "What it says about us: the scholarly.",
 "The Mythic Parallel": "The ancient pattern: the archetypal.",
 "The Definitive Ranking": "Theories, scored: the leaderboard.",
 "The Canon Reconciliation": "Making it all fit: the harmonizer.",
 "The Sequel Prediction": "What\u2019s next: the oracle.",
 "The Legacy Theory": "The enduring reading: the classic.",
 "Teaching Theory Craft": "Show others: the speculation mentor.",
 "Masterclass: Narrative Theory": "How stories work: the poetics of plot."
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
    name:topic+' — fan theory record',
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

var BUILD_THEORY=(function(){
return function(inp){
  var uni=inp.universe||'your favorite series';
  return {title:'Fan theory playground: '+uni,intro:'A structured way to build, compare, and stress-test theories about '+uni+'.',
    sections:[{h:'Theory templates',items:['The Hidden Identity: a minor character is secretly major — evidence, motive, reveal moment.','The Loop: events repeat with a twist — map the cycles and the break point.','The Unreliable Lens: the narrator is wrong — what changes if you flip one assumption?','The Merge: two separate threads are one — find the connecting scene.']},{h:'Score each theory',items:['Evidence (1-5): scenes that support it','Elegance (1-5): simplest explanation wins ties','Falsifiability (1-5): what would prove it wrong?']},{h:'Playground rules',items:['Steel-man the theory you dislike before attacking it.','One theory per thread; compare scores side by side.','Canon updates re-score everything — theories are living documents.']}]};
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
gen.builderId="theory";
gen.builderFields=[["universe", "Universe / story", "text", "your favorite series"], ["seed", "Seed (optional)", "number", "7"]];
gen.build=BUILD_THEORY;

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-fan-theory-playground',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();