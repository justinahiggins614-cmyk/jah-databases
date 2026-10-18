(function(){'use strict';
/* The The No-Money Fun Database Signature generator — jahdb-db-no-money-fun-signature-sig-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-NO-MONEY-FUN-SIG-";
var GENVER="jahdb-db-no-money-fun-signature-sig-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The Park Perfect Day",
  "Library Deep Dive",
  "The Walking Tour (Self-Guided)",
  "Kitchen Creation",
  "Stargazing, Free",
  "The Swap Meet",
  "People-Watching Prime",
  "The Free Concert Hunt",
  "Trail Discovery",
  "Game Night, Owned Games",
  "The Sunset Ritual",
  "Volunteer Taster"
 ],
 "Compounded": [
  "The Free Festival Day",
  "Museum Free Day",
  "The Beach/Lake Day",
  "Community Class Sampler",
  "The Big Hike",
  "The Photo Project",
  "Sports Spectating",
  "The Garden Volunteer",
  "Open Mic Night",
  "The Historical Hunt",
  "Fishing (Where Free)",
  "The Potluck Party"
 ],
 "Advanced": [
  "The Zero-Dollar Weekend",
  "The Free City Guide",
  "The Skill Exchange",
  "The 30-Day Free Challenge",
  "Community Building",
  "The Free Travel Hack",
  "The Abundance Audit",
  "Teaching Free Fun",
  "Legacy: The Free Tradition",
  "Masterclass: The Economics of Enough"
 ]
};
var BLURBS={
 "The Park Perfect Day": "Blanket, book, ball: the park provides, you enjoy.",
 "Library Deep Dive": "An afternoon among the stacks: free books, free quiet, free wonder.",
 "The Walking Tour (Self-Guided)": "Free online guides turn your town into a museum.",
 "Kitchen Creation": "Cook with what is there: the challenge is the fun.",
 "Stargazing, Free": "A dark spot and upward eyes: the universe charges nothing.",
 "The Swap Meet": "Trade books, clothes, or games with friends: new-to-you, free.",
 "People-Watching Prime": "A busy bench and an hour: the best show is unscripted.",
 "The Free Concert Hunt": "Parks, churches, and plazas host free music: find it.",
 "Trail Discovery": "The nearest trail you have never walked: adventure, adjacent.",
 "Game Night, Owned Games": "The shelf of shame becomes the hall of fame.",
 "The Sunset Ritual": "A daily free show: pick your spot, keep the habit.",
 "Volunteer Taster": "Try volunteering once: meaningful, social, free.",
 "The Free Festival Day": "Street fairs and cultural festivals: full days for zero dollars.",
 "Museum Free Day": "Monthly free days: world-class art, no ticket.",
 "The Beach/Lake Day": "Public shores: pack food, stay all day.",
 "Community Class Sampler": "Free intro classes: dance, language, crafts - try everything.",
 "The Big Hike": "A real trail day: pack lunch, earn views.",
 "The Photo Project": "A themed photo series around town: art from attention.",
 "Sports Spectating": "Free local games: school, amateur, park leagues - pure joy.",
 "The Garden Volunteer": "Community gardens welcome hands: learn, harvest, belong.",
 "Open Mic Night": "Free to watch, brave to try: the cheapest theater.",
 "The Historical Hunt": "Research and visit local history: free time travel.",
 "Fishing (Where Free)": "A borrowed rod and a public pier: patience, rewarded.",
 "The Potluck Party": "Everyone brings a dish: feast for the cost of one.",
 "The Zero-Dollar Weekend": "48 hours, $0 spent: the ultimate proof of concept.",
 "The Free City Guide": "Become the expert on your city\u2019s free offerings: then share it.",
 "The Skill Exchange": "Trade skills with neighbors: free learning, real community.",
 "The 30-Day Free Challenge": "A month of free-only fun: the habit that changes spending forever.",
 "Community Building": "Start the free club, walk, or game night: the gift that multiplies.",
 "The Free Travel Hack": "Volunteer travel, housesitting: see the world on $0.",
 "The Abundance Audit": "List everything free you already have: wealth, inventoried.",
 "Teaching Free Fun": "Show others the $0 life: the most generous curriculum.",
 "Legacy: The Free Tradition": "A yearly free-only celebration: the tradition of enough.",
 "Masterclass: The Economics of Enough": "Why free fun beats bought fun: the science of satisfaction."
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
    name:topic+' — free activity record',
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

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-no-money-fun-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();