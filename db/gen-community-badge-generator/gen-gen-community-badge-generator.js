(function(){'use strict';
/* The The Community Badge Generator generator — jahdb-gen-community-badge-generator-pub-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-COMMUNITY-BADGE-GENERATOR-PUB-";
var GENVER="jahdb-gen-community-badge-generator-pub-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The First Badge",
  "The Week One",
  "The Helper",
  "The Regular",
  "The Creator",
  "The Cheerleader",
  "The Learner",
  "The Explorer",
  "The Friend",
  "The Early Bird",
  "The Night Owl",
  "The Comeback"
 ],
 "Compounded": [
  "The Milestone 10",
  "The Mentor",
  "The Organizer",
  "The Artist",
  "The Historian",
  "The Peacemaker",
  "The Marathoner",
  "The Innovator",
  "The Generous",
  "The Veteran",
  "The Champion",
  "The Storyteller"
 ],
 "Advanced": [
  "The Legend",
  "The Founder",
  "The Decade",
  "The Hall of Fame",
  "The Mythic",
  "The Guardian",
  "The Legacy",
  "The Grandmaster",
  "Teaching Badge Design",
  "Masterclass: The Status Science"
 ]
};
var BLURBS={
 "The First Badge": "The welcome badge: the beginning.",
 "The Week One": "Seven days in: the commitment.",
 "The Helper": "First help given: the kindness.",
 "The Regular": "Showing up: the reliable.",
 "The Creator": "First creation shared: the maker.",
 "The Cheerleader": "Positivity recognized: the uplifter.",
 "The Learner": "First lesson completed: the student.",
 "The Explorer": "Tried something new: the brave.",
 "The Friend": "Made a connection: the social.",
 "The Early Bird": "First to arrive: the dedicated.",
 "The Night Owl": "Last to leave: the loyal.",
 "The Comeback": "Returned after absence: the welcomed.",
 "The Milestone 10": "Ten of something: the decimal.",
 "The Mentor": "Guided a newcomer: the teacher.",
 "The Organizer": "Ran an event: the leader.",
 "The Artist": "Beautiful contribution: the creative.",
 "The Historian": "Documented the lore: the keeper.",
 "The Peacemaker": "Resolved conflict: the diplomat.",
 "The Marathoner": "The long haul: the enduring.",
 "The Innovator": "New idea implemented: the visionary.",
 "The Generous": "Gave significantly: the benefactor.",
 "The Veteran": "A year of belonging: the rooted.",
 "The Champion": "Won the tournament: the victorious.",
 "The Storyteller": "Shared the saga: the bard.",
 "The Legend": "The rarest honor: the immortal.",
 "The Founder": "There at the start: the origin.",
 "The Decade": "Ten years: the institution.",
 "The Hall of Fame": "The pantheon: the eternal.",
 "The Mythic": "Beyond legend: the transcendent.",
 "The Guardian": "Protected the community: the shield.",
 "The Legacy": "Impact beyond tenure: the enduring.",
 "The Grandmaster": "Mastery recognized: the pinnacle.",
 "Teaching Badge Design": "Show others: the recognition mentor.",
 "Masterclass: The Status Science": "Why badges motivate: the psychology of recognition."
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
    name:topic+' — community badge record',
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

var BUILD_BADGE_GEN=(function(){
return function(inp){
  var r=prng(inp.seed||31);
  var miles=(inp.milestones||'First stream,10 streams,1 year,Helper,Creator').split(',').map(function(s){return s.trim();});
  var shapes=['shield','star','coin','ribbon','gem','laurel'];
  var badges=miles.map(function(m,i){return m+': '+shapes[i%shapes.length]+' badge, tier '+(1+((i/3)|0))+' — earned, never bought';});
  return {title:'Community badge set',intro:badges.length+' meaningful badges for contributions and milestones — status people actually want.',
    sections:[{h:'The badges',items:badges},{h:'Design rules',items:['Milestone badges get fancier with tenure.','Contribution badges name the deed, not the donor.','Retire badges rarely; scarcity is earned over years, not manufactured.']}]};
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
gen.builderId="badge-gen";
gen.builderFields=[["milestones", "Milestones (comma separated)", "text", "First stream,10 streams,1 year,Helper,Creator"], ["seed", "Seed (optional)", "number", "31"]];
gen.build=BUILD_BADGE_GEN;

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-community-badge-generator',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();