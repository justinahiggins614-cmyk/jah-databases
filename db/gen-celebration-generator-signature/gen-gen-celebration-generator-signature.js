(function(){'use strict';
/* The The Celebration Generator Signature generator — jahdb-gen-celebration-generator-signature-sig-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-CELEBRATION-GENERATOR-SIG-";
var GENVER="jahdb-gen-celebration-generator-signature-sig-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The Un-Birthday",
  "Taco Tuesday Party",
  "The Promotion Toast",
  "First Day of Season",
  "The Friday Finale",
  "New Home Toast",
  "The Pet\u2019s Gotcha Day",
  "Half-Birthday",
  "The Clean Slate",
  "Sunshine Day",
  "The Thank-You Party",
  "Small Win Wednesday"
 ],
 "Compounded": [
  "The Milestone Birthday",
  "Graduation Gala",
  "The Anniversary, Reimagined",
  "Retirement Roast (Kind)",
  "The House Milestone",
  "Decade Party",
  "The Reunion",
  "Baby\u2019s First Everything",
  "The Business Launch",
  "The Finish Line",
  "The Citizenship Celebration",
  "The Recovery Milestone"
 ],
 "Advanced": [
  "The Once-a-Decade Bash",
  "The Destination Celebration",
  "The Legacy Gala",
  "The 50th Anniversary",
  "The Community Festival",
  "The Surprise of the Decade",
  "The Vow Renewal",
  "The Heritage Celebration",
  "The Annual Tradition Gala",
  "Masterclass: The Art of Gathering"
 ]
};
var BLURBS={
 "The Un-Birthday": "Celebrate no reason at all: the purest party.",
 "Taco Tuesday Party": "The weekly ritual, elevated: the recurring celebration.",
 "The Promotion Toast": "Mark the win properly: achievement, acknowledged.",
 "First Day of Season": "Greet spring, summer, fall, winter: the calendar\u2019s parties.",
 "The Friday Finale": "End the week with ceremony: the small, sweet ritual.",
 "New Home Toast": "Bless the new place: the housewarming, heartfelt.",
 "The Pet\u2019s Gotcha Day": "Celebrate the furry family: the joyful silly.",
 "Half-Birthday": "The six-month mark: twice the cake per year.",
 "The Clean Slate": "Mark a fresh start: the intentional new chapter.",
 "Sunshine Day": "Celebrate a perfect-weather day: the spontaneous festival.",
 "The Thank-You Party": "Honor the helpers: gratitude, catered.",
 "Small Win Wednesday": "Weekly tiny victories, toasted: the momentum party.",
 "The Milestone Birthday": "The big-number birthday, done right: the legend.",
 "Graduation Gala": "The achievement, celebrated: caps, cheers, future.",
 "The Anniversary, Reimagined": "Year one or fifty: love, marked.",
 "Retirement Roast (Kind)": "Honor the career with laughter and love.",
 "The House Milestone": "Mortgage burned, renovation done: the home victory.",
 "Decade Party": "The 20s, 30s, 40s send-off: eras, celebrated.",
 "The Reunion": "Years apart, one night together: the time machine.",
 "Baby\u2019s First Everything": "The tiny milestones: celebrated enormously.",
 "The Business Launch": "Open the doors with fanfare: the brave beginning.",
 "The Finish Line": "Race, degree, project done: the earned party.",
 "The Citizenship Celebration": "The new chapter, nationally: welcome, officially.",
 "The Recovery Milestone": "Mark the hard-won win: the courageous celebration.",
 "The Once-a-Decade Bash": "The party they will talk about for years: the epic.",
 "The Destination Celebration": "Take the party on the road: the traveling festival.",
 "The Legacy Gala": "Honor a life or a cause: the meaningful grand.",
 "The 50th Anniversary": "Half a century of us: the gold standard.",
 "The Community Festival": "A celebration for the whole neighborhood: the big tent.",
 "The Surprise of the Decade": "The perfectly executed surprise: the legend.",
 "The Vow Renewal": "Say it again, mean it more: the romantic epic.",
 "The Heritage Celebration": "Honor roots and ancestors: the deep party.",
 "The Annual Tradition Gala": "The yearly event everyone plans around: the institution.",
 "Masterclass: The Art of Gathering": "Why we celebrate: the anthropology of parties."
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
    name:topic+' — celebration plan record',
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

var BUILD_CELEBRATION=(function(){
var THEMES=['Backwards day (dessert first)','Decade throwback','Color party (everyone wears one color)','Tiny awards night','Around-the-world snacks','Un-birthday for no reason','First-day-of-season festival','Achievement unlocked party'];
var ACTS=['Two-minute toast circle','DIY photo booth with props','Group playlist — everyone adds 3 songs','Trivia about the guest of honor','Time-capsule notes for next year','Dance-off, judged by applause'];
return function(inp){
  var r=prng(inp.seed||9);
  var theme=pick(THEMES,r), acts=shuffle(ACTS,r).slice(0,3);
  var budget=parseInt(inp.budget,10)||50, people=parseInt(inp.people,10)||6;
  return {title:'Celebration: '+theme,intro:'A small celebration for about '+people+' people on roughly $'+budget+' — because ordinary days deserve ceremonies too.',
    sections:[{h:'Theme',text:theme+'. Decor: one statement piece (banner, balloons, or lights) beats ten small ones.'},{h:'Run of show',items:acts},{h:'Budget sketch',items:['Food + drink: $'+Math.round(budget*0.6),'Decor: $'+Math.round(budget*0.25),'Wildcard fun: $'+Math.round(budget*0.15)]},{h:'The rule',text:'Someone takes photos; the host stays in at least three of them.'}]};
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
gen.builderId="celebration";
gen.builderFields=[["occasion", "Occasion", "select", ["just because", "milestone", "seasonal", "achievement", "reunion"]], ["people", "People", "number", "6"], ["budget", "Budget ($)", "number", "50"], ["seed", "Seed (optional)", "number", "9"]];
gen.build=BUILD_CELEBRATION;

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-celebration-generator-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();