(function(){'use strict';
/* The The Personal Tradition Creator generator — jahdb-gen-personal-tradition-creator-pub-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-PERSONAL-TRADITION-CREATOR-PUB-";
var GENVER="jahdb-gen-personal-tradition-creator-pub-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The Weekly Walk",
  "The Monthly Dinner",
  "The Birthday Call",
  "The Sunday Check-In",
  "The Seasonal Outing",
  "The Game Night",
  "The Gratitude Share",
  "The Walk-and-Talk",
  "The Recipe Exchange",
  "The Book Swap",
  "The Morning Coffee",
  "The Evening Stroll"
 ],
 "Compounded": [
  "The Annual Trip",
  "The Holiday Invention",
  "The Project Tradition",
  "The Letter Tradition",
  "The Volunteer Day",
  "The Skill Share",
  "The Feast",
  "The Adventure Day",
  "The Remembrance",
  "The Milestone Mark",
  "The Quiet Retreat",
  "The Giving Tradition"
 ],
 "Advanced": [
  "The Decade Tradition",
  "The Generational Handoff",
  "The Pilgrimage",
  "The Legacy Ritual",
  "The Community Tradition",
  "The Reunion",
  "The Vow",
  "The Archive",
  "Teaching Tradition-Making",
  "Masterclass: The Anthropology of Ritual"
 ]
};
var BLURBS={
 "The Weekly Walk": "Same route, same day: the simplest tradition.",
 "The Monthly Dinner": "One table, once a month: the anchor meal.",
 "The Birthday Call": "Never miss it: the small, sacred habit.",
 "The Sunday Check-In": "A weekly call or text round: the connection ritual.",
 "The Seasonal Outing": "One adventure per season: the year\u2019s quarters.",
 "The Game Night": "Cards, boards, laughter: the recurring play.",
 "The Gratitude Share": "A monthly exchange of thanks: the warm ritual.",
 "The Walk-and-Talk": "Movement plus conversation: the healthy habit.",
 "The Recipe Exchange": "Share one recipe monthly: the delicious chain.",
 "The Book Swap": "Pass the finished book on: the literary loop.",
 "The Morning Coffee": "The standing date: the week\u2019s warm start.",
 "The Evening Stroll": "The daily descent: the shared wind-down.",
 "The Annual Trip": "One journey yearly: the tradition with luggage.",
 "The Holiday Invention": "Your own holiday: the calendar\u2019s new star.",
 "The Project Tradition": "Build something yearly: the compounding creation.",
 "The Letter Tradition": "Annual letters to each other: the archive of love.",
 "The Volunteer Day": "Serve together yearly: the meaningful ritual.",
 "The Skill Share": "Teach each other yearly: the growing circle.",
 "The Feast": "The big annual meal: the delicious institution.",
 "The Adventure Day": "One bold day yearly: the legend, recurring.",
 "The Remembrance": "Honor who came before: the sacred annual.",
 "The Milestone Mark": "Celebrate the year\u2019s wins: the annual toast.",
 "The Quiet Retreat": "A yearly pause together: the deep reset.",
 "The Giving Tradition": "Give together yearly: the generous ritual.",
 "The Decade Tradition": "Ten years running: the institution.",
 "The Generational Handoff": "Pass it to the kids: the tradition\u2019s future.",
 "The Pilgrimage": "The journey that defines the group: the sacred road.",
 "The Legacy Ritual": "What outlives the founders: the eternal flame.",
 "The Community Tradition": "The whole neighborhood joins: the big circle.",
 "The Reunion": "The scattered, regathered: the time machine, annual.",
 "The Vow": "The promise renewed: the deepest ritual.",
 "The Archive": "The documented history: the tradition\u2019s memory.",
 "Teaching Tradition-Making": "Show others the craft: the multiplying gift.",
 "Masterclass: The Anthropology of Ritual": "Why humans ritualize - and how to do it well."
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
    name:topic+' — tradition design record',
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

var BUILD_TRADITION=(function(){
return function(inp){
  var who=inp.who||'friends', freq=inp.freq||'monthly', values=inp.values||'laughter and good food';
  var r=prng(inp.seed||13);
  var anchors=['First '+freq+' Friday','The same weekend every '+freq.replace('ly','')+' (pick a number and defend it)','The day the season changes','Whoever-hosts-chooses-the-theme rotation'];
  return {title:'A new '+freq+' tradition',intro:'A recurring ritual for '+who+', built on '+values+'. Traditions are just planned nostalgia.',
    sections:[{h:'The tradition',text:'“'+pick(['The Long Table','Second Sunday Supper','The Walk-and-Talk','Game Night Royale'],r)+'” — '+who+' gather '+freq+', same anchor date, no re-planning each time.'},{h:'Anchor it',items:[pick(anchors,r),'One standing group chat, one standing date.','A tiny ritual that repeats: same toast, same playlist opener, same silly trophy.']},{h:'Keep it alive 5 years',items:['Miss twice and it dies — protect the streak.','Let it evolve; the third year will not look like the first.','Document it: one photo per gathering, same album.']}]};
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
gen.builderId="tradition";
gen.builderFields=[["who", "Who gathers", "text", "friends"], ["freq", "How often", "select", ["weekly", "monthly", "seasonally", "yearly"]], ["values", "Built on", "text", "laughter and good food"], ["seed", "Seed (optional)", "number", "13"]];
gen.build=BUILD_TRADITION;

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-personal-tradition-creator',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();