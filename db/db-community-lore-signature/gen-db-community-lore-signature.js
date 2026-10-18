(function(){'use strict';
/* The The Community Lore Database Signature generator — jahdb-db-community-lore-signature-sig-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-COMMUNITY-LORE-SIG-";
var GENVER="jahdb-db-community-lore-signature-sig-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The Origin Story",
  "The First Joke",
  "The Nicknames",
  "The Catchphrases",
  "The First Event",
  "The Mascot Tale",
  "The Traditions",
  "The Heroes",
  "The Funny Fails",
  "The Comebacks",
  "The Records",
  "The Quotes"
 ],
 "Compounded": [
  "The Wiki",
  "The Timeline",
  "The Hall of Fame",
  "The Sagas",
  "The Rivalries",
  "The Alliances",
  "The Eras",
  "The Artifacts",
  "The Songs",
  "The Memes",
  "The Legends",
  "The Newcomer Guide"
 ],
 "Advanced": [
  "The Documentary",
  "The Museum",
  "The Anniversary",
  "The Reunion",
  "The Canon Vote",
  "The Prequel",
  "The Legacy",
  "The Handoff",
  "Teaching Lore Keeping",
  "Masterclass: Collective Memory"
 ]
};
var BLURBS={
 "The Origin Story": "How it all began: the genesis.",
 "The First Joke": "The inside joke\u2019s birth: the classic.",
 "The Nicknames": "How everyone got named: the christening.",
 "The Catchphrases": "Words only we say: the dialect.",
 "The First Event": "The legendary first: the milestone.",
 "The Mascot Tale": "How the mascot arrived: the beloved.",
 "The Traditions": "What we always do: the rituals.",
 "The Heroes": "The standout members: the celebrated.",
 "The Funny Fails": "The glorious disasters: the humble.",
 "The Comebacks": "The great returns: the resilient.",
 "The Records": "The unbeaten: the legendary stats.",
 "The Quotes": "Things actually said: the scripture.",
 "The Wiki": "The documented canon: the archive.",
 "The Timeline": "History in order: the chronicle.",
 "The Hall of Fame": "The immortal: the honored.",
 "The Sagas": "Multi-part epics: the mythology.",
 "The Rivalries": "The friendly wars: the drama.",
 "The Alliances": "The great friendships: the bonds.",
 "The Eras": "Distinct periods: the ages.",
 "The Artifacts": "Physical mementos: the relics.",
 "The Songs": "The anthems: the soundtrack.",
 "The Memes": "The visual lore: the gallery.",
 "The Legends": "Larger than life: the mythic.",
 "The Newcomer Guide": "Lore for the new: the welcome.",
 "The Documentary": "The filmed history: the epic.",
 "The Museum": "The curated past: the institution.",
 "The Anniversary": "The lore celebrated: the tradition.",
 "The Reunion": "The legends return: the homecoming.",
 "The Canon Vote": "What\u2019s official: the democratic.",
 "The Prequel": "Before the beginning: the origins.",
 "The Legacy": "The enduring story: the forever.",
 "The Handoff": "Lore keepers, next generation: the succession.",
 "Teaching Lore Keeping": "Show others: the historian mentor.",
 "Masterclass: Collective Memory": "How groups remember: the sociology of lore."
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
    name:topic+' — community lore record',
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

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-community-lore-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();