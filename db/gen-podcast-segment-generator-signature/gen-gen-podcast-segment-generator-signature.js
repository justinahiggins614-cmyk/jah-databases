(function(){'use strict';
/* The The Podcast Segment Generator Signature generator — jahdb-gen-podcast-segment-generator-signature-sig-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-PODCAST-SEGMENT-GENERATOR-SIG-";
var GENVER="jahdb-gen-podcast-segment-generator-signature-sig-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The Cold Open",
  "The Intro",
  "The Headlines",
  "The Question",
  "The Game",
  "The Mailbag",
  "The Tip",
  "The Story",
  "The Debate",
  "The Recommendation",
  "The Fail",
  "The Good Thing"
 ],
 "Compounded": [
  "The Deep Dive",
  "The Interview",
  "The Panel",
  "The Field Report",
  "The History",
  "The Science",
  "The Culture",
  "The Craft",
  "The Money",
  "The Health",
  "The Tech",
  "The Arts"
 ],
 "Advanced": [
  "The Live Show",
  "The Documentary",
  "The Series",
  "The Special",
  "The Crossover",
  "The Anniversary",
  "The Finale",
  "The Legacy",
  "Teaching Segment Design",
  "Masterclass: The Audio Craft"
 ]
};
var BLURBS={
 "The Cold Open": "The hook: the grabber.",
 "The Intro": "Welcome ritual: the familiar.",
 "The Headlines": "What\u2019s new: the update.",
 "The Question": "One big question: the thinker.",
 "The Game": "Play along: the fun.",
 "The Mailbag": "Listener letters: the connection.",
 "The Tip": "One useful thing: the value.",
 "The Story": "A tale told: the narrative.",
 "The Debate": "Two sides: the lively.",
 "The Recommendation": "Try this: the trusted.",
 "The Fail": "What went wrong: the humble.",
 "The Good Thing": "End warm: the closer.",
 "The Deep Dive": "One topic, deeply: the substantial.",
 "The Interview": "The guest: the conversation.",
 "The Panel": "Many voices: the roundtable.",
 "The Field Report": "Out in the world: the adventurous.",
 "The History": "The backstory: the context.",
 "The Science": "The evidence: the empirical.",
 "The Culture": "The moment: the relevant.",
 "The Craft": "How it\u2019s made: the process.",
 "The Money": "The business: the practical.",
 "The Health": "The body: the caring.",
 "The Tech": "The future: the curious.",
 "The Arts": "The beautiful: the inspired.",
 "The Live Show": "In front of crowds: the event.",
 "The Documentary": "The prestige episode: the cinematic.",
 "The Series": "Multi-part: the saga.",
 "The Special": "The occasion: the celebration.",
 "The Crossover": "Shows unite: the network.",
 "The Anniversary": "The milestone: the retrospective.",
 "The Finale": "The goodbye: the graceful.",
 "The Legacy": "The definitive: the classic.",
 "Teaching Segment Design": "Show others: the audio mentor.",
 "Masterclass: The Audio Craft": "Why podcasts work: the intimacy science."
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
    name:topic+' — podcast segment record',
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

var BUILD_PODCAST_SEGMENTS=(function(){
var SEGS=['Cold open: 60-second hook from the best moment','Listener mail: one question, real answer','The Deep Cut: 10 minutes on one idea','Game break: trivia, drafts, or debates','Hotline: voice notes from the audience','One Good Thing: end warm, every time'];
return function(inp){
  var r=prng(inp.seed||41);
  var mins=Math.min(180,Math.max(15,parseInt(inp.length,10)||45));
  var picks=shuffle(SEGS,r);
  var plan=[['Cold open',2],['Main topic 1',Math.round(mins*0.3)],['Game break',8],['Main topic 2',Math.round(mins*0.3)],['Listener mail',Math.round(mins*0.15)],['One Good Thing',3]];
  return {title:'Podcast lineup: '+(inp.theme||'your show'),intro:'A '+mins+'-minute episode structure with recurring segments listeners can love.',
    sections:[{h:'The rundown',items:plan.map(function(p){return p[0]+' — '+p[1]+' min';})},{h:'Segment bank (rotate weekly)',items:picks.slice(0,4)},{h:'Production rules',items:['Record the cold open LAST — steal it from the best moment.','One segment per episode is allowed to flop; two is a format problem.','Name segments like a local would: specific beats clever.']}]};
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
gen.builderId="podcast-segments";
gen.builderFields=[["theme", "Show theme", "text", "your show"], ["length", "Episode minutes", "number", "45"], ["seed", "Seed (optional)", "number", "41"]];
gen.build=BUILD_PODCAST_SEGMENTS;

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-podcast-segment-generator-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();