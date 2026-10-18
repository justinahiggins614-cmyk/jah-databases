(function(){'use strict';
/* The The Content Calendar Generator Signature generator — jahdb-gen-content-calendar-generator-signature-sig-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-CONTENT-CALENDAR-GENERATOR-SIG-";
var GENVER="jahdb-gen-content-calendar-generator-signature-sig-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The 2-Post Week",
  "The Pillar Pick",
  "The Batch Day",
  "The Buffer Build",
  "The Repurpose Rule",
  "The Theme Week",
  "The Rest Day",
  "The Idea Bank",
  "The 30-Minute Post",
  "The Review Ritual",
  "The Seasonal Plan",
  "The Flex Slot"
 ],
 "Compounded": [
  "The Multi-Platform Week",
  "The Series Calendar",
  "The Launch Calendar",
  "The Collab Calendar",
  "The Event Calendar",
  "The Evergreen Bank",
  "The Trend Response",
  "The Community Week",
  "The Deep Work Month",
  "The Analytics Review",
  "The Sabbatical Plan",
  "The Team Calendar"
 ],
 "Advanced": [
  "The 90-Day Campaign",
  "The Annual Calendar",
  "The Franchise Calendar",
  "The Global Calendar",
  "The Legacy Library",
  "The Succession Calendar",
  "The Data-Driven Year",
  "The Creative Sabbatical",
  "Teaching Calendar Design",
  "Masterclass: Consistency Science"
 ]
};
var BLURBS={
 "The 2-Post Week": "Two quality posts: the sustainable start.",
 "The Pillar Pick": "Choose your three formats: the foundation.",
 "The Batch Day": "One day, many posts: the efficiency hack.",
 "The Buffer Build": "Bank two spare posts: the safety net.",
 "The Repurpose Rule": "One to many: the multiplier.",
 "The Theme Week": "One theme, many angles: the deep dive.",
 "The Rest Day": "Scheduled off: the protected pause.",
 "The Idea Bank": "Capture everything: the never-empty well.",
 "The 30-Minute Post": "Fast formats for busy weeks: the sprint.",
 "The Review Ritual": "Monthly look-back: the learning loop.",
 "The Seasonal Plan": "Quarterly themes: the big rhythm.",
 "The Flex Slot": "Room for trends: the agile gap.",
 "The Multi-Platform Week": "One idea, many platforms: the distribution.",
 "The Series Calendar": "Recurring series scheduled: the appointment viewing.",
 "The Launch Calendar": "Product or project launches: the campaign.",
 "The Collab Calendar": "Coordinated with partners: the shared schedule.",
 "The Event Calendar": "Streams and premieres: the tentpoles.",
 "The Evergreen Bank": "Timeless content, scheduled: the compounding library.",
 "The Trend Response": "Fast-turnaround slots: the relevant.",
 "The Community Week": "Audience-driven content: the participatory.",
 "The Deep Work Month": "One big project: the focused arc.",
 "The Analytics Review": "Data-driven planning: the informed.",
 "The Sabbatical Plan": "Planned breaks: the sustainable.",
 "The Team Calendar": "Coordinated creators: the organized.",
 "The 90-Day Campaign": "A quarter-long arc: the strategic.",
 "The Annual Calendar": "The year, themed: the master plan.",
 "The Franchise Calendar": "Multiple shows, one brand: the network.",
 "The Global Calendar": "Time zones and cultures: the worldwide.",
 "The Legacy Library": "Content that compounds for years: the asset.",
 "The Succession Calendar": "The brand beyond you: the enduring.",
 "The Data-Driven Year": "Fully optimized: the scientific.",
 "The Creative Sabbatical": "Planned renewal: the artist\u2019s year.",
 "Teaching Calendar Design": "Show others: the systems mentor.",
 "Masterclass: Consistency Science": "Why showing up wins: the compounding of cadence."
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
    name:topic+' — content calendar record',
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

var BUILD_CONTENT_CALENDAR=(function(){
return function(inp){
  var perWeek=Math.min(14,Math.max(1,parseInt(inp.perweek,10)||4));
  var pillars=(inp.pillars||'Teach,Entertain,Community').split(',').map(function(s){return s.trim();});
  var platforms=(inp.platforms||'video,shorts,stream').split(',').map(function(s){return s.trim();});
  var days=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'];
  var items=[];
  for(var i=0;i<perWeek;i++){items.push(days[i%days.length]+': '+pillars[i%pillars.length]+' → '+platforms[i%platforms.length]);}
  return {title:'Content calendar: '+perWeek+'/week',intro:'A sustainable rhythm across '+platforms.join(', ')+'. Batch, buffer, breathe.',
    sections:[{h:'The week',items:items},{h:'System rules',items:['One buffer slot per week — life happens.','Repurpose rule: every big piece becomes 3 small ones.','Monthly review: double what worked, drop what drained.']}]};
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
gen.builderId="content-calendar";
gen.builderFields=[["platforms", "Platforms (comma separated)", "text", "video,shorts,stream"], ["perweek", "Posts per week", "number", "4"], ["pillars", "Content pillars (comma separated)", "text", "Teach,Entertain,Community"], ["seed", "Seed (optional)", "number", "3"]];
gen.build=BUILD_CONTENT_CALENDAR;

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-content-calendar-generator-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();