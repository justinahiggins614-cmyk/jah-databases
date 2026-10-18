(function(){'use strict';
/* The The Try Something New Database Signature generator — jahdb-db-try-something-new-signature-sig-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-TRY-SOMETHING-NEW-SIG-";
var GENVER="jahdb-db-try-something-new-signature-sig-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The New Food",
  "The New Route",
  "The New Genre",
  "The New Greeting",
  "The New Hobby Hour",
  "The New Seat",
  "The New Skill, Tiny",
  "The New Neighbor",
  "The New Morning",
  "The New Shop",
  "The New Walk",
  "The New Compliment"
 ],
 "Compounded": [
  "The Class",
  "The Solo Outing",
  "The Volunteer Shift",
  "The Performance",
  "The Day Trip",
  "The Conversation",
  "The Tech Try",
  "The Sport",
  "The Craft",
  "The Language Lesson",
  "The Night Shift",
  "The Interview"
 ],
 "Advanced": [
  "The Solo Journey",
  "The Big Leap",
  "The Career Experiment",
  "The Move",
  "The Deep Dive Year",
  "The Fear Conquered",
  "The Creation",
  "The Reinvention",
  "Teaching Newness",
  "Masterclass: Neophilia"
 ]
};
var BLURBS={
 "The New Food": "One dish you\u2019ve never tried: the delicious frontier.",
 "The New Route": "A different way to the usual place: the tiny adventure.",
 "The New Genre": "A book, film, or song outside your taste: the expanded palate.",
 "The New Greeting": "Learn hello in a new language: the small bridge.",
 "The New Hobby Hour": "Try a hobby for one hour: the low-stakes test.",
 "The New Seat": "Sit somewhere different: the perspective shift.",
 "The New Skill, Tiny": "One micro-skill: the 15-minute new.",
 "The New Neighbor": "Introduce yourself: the social new.",
 "The New Morning": "A different first hour: the day, remixed.",
 "The New Shop": "The store you\u2019ve never entered: the commercial safari.",
 "The New Walk": "A street you\u2019ve never strolled: the adjacent new.",
 "The New Compliment": "Praise something unusual: the kind new.",
 "The Class": "A real class in something foreign: the structured new.",
 "The Solo Outing": "Dinner or a film alone: the independent new.",
 "The Volunteer Shift": "Serve somewhere new: the meaningful new.",
 "The Performance": "Open mic, karaoke, stage: the brave new.",
 "The Day Trip": "Somewhere you\u2019ve never been: the geographic new.",
 "The Conversation": "Talk to a stranger (kindly, safely): the human new.",
 "The Tech Try": "A new tool or app, mastered: the digital new.",
 "The Sport": "A sport you\u2019ve never played: the physical new.",
 "The Craft": "Make something with your hands: the maker new.",
 "The Language Lesson": "A real first lesson: the polyglot seed.",
 "The Night Shift": "Experience your town at 3am (safely): the nocturnal new.",
 "The Interview": "Ask someone fascinating for coffee: the curious new.",
 "The Solo Journey": "Travel alone: the transformative new.",
 "The Big Leap": "The thing you\u2019ve dreamed for years: the defining new.",
 "The Career Experiment": "Shadow or try a new field: the professional new.",
 "The Move": "A new city or country: the ultimate new.",
 "The Deep Dive Year": "A year devoted to one new mastery: the committed new.",
 "The Fear Conquered": "Face the big one, safely guided: the liberating new.",
 "The Creation": "Birth the project: the legacy new.",
 "The Reinvention": "Become someone new, deliberately: the profound new.",
 "Teaching Newness": "Guide others to their edge: the generous new.",
 "Masterclass: Neophilia": "The science of loving novelty: the curious brain."
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
    name:topic+' — new experience record',
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

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-try-something-new-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();