(function(){'use strict';
/* The The Audience Poll Generator Signature generator — jahdb-gen-audience-poll-generator-signature-sig-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-AUDIENCE-POLL-GENERATOR-SIG-";
var GENVER="jahdb-gen-audience-poll-generator-signature-sig-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The Quick Vote",
  "This or That",
  "Rate It",
  "The Funny Option",
  "Pick the Next",
  "The Hot Take Check",
  "The Preference Map",
  "The Prediction Poll",
  "The Tier Vote",
  "The Yes/No",
  "The Emoji Vote",
  "The Straw Poll"
 ],
 "Compounded": [
  "The Content Direction",
  "The Tournament Bracket",
  "The Name Vote",
  "The Schedule Poll",
  "The Tier List Vote",
  "The Award Vote",
  "The Feedback Poll",
  "The Challenge Vote",
  "The Guest Vote",
  "The Charity Poll",
  "The Merch Vote",
  "The Lore Poll"
 ],
 "Advanced": [
  "The Constitutional Poll",
  "The Annual Awards",
  "The Direction Referendum",
  "The Hall of Fame",
  "The Succession Poll",
  "The Merger Vote",
  "The Legacy Poll",
  "The Global Poll",
  "Teaching Poll Craft",
  "Masterclass: Collective Intelligence"
 ]
};
var BLURBS={
 "The Quick Vote": "One question, 60 seconds: the pulse check.",
 "This or That": "Binary choices, maximum opinions: the classic.",
 "Rate It": "Scale of 1-5: the instant feedback.",
 "The Funny Option": "Always include one joke: the turnout trick.",
 "Pick the Next": "Audience chooses upcoming content: the power poll.",
 "The Hot Take Check": "Agree or disagree: the opinion thermometer.",
 "The Preference Map": "Favorites revealed: the community portrait.",
 "The Prediction Poll": "Bet on outcomes: the oracle game.",
 "The Tier Vote": "Rank the options: the nuanced poll.",
 "The Yes/No": "The simplest democracy: the binary.",
 "The Emoji Vote": "React to vote: the frictionless poll.",
 "The Straw Poll": "Test the waters: the informal gauge.",
 "The Content Direction": "Major votes on series and formats: the steering poll.",
 "The Tournament Bracket": "Community-voted brackets: the saga poll.",
 "The Name Vote": "Name the thing together: the christening.",
 "The Schedule Poll": "When should we meet? The practical democracy.",
 "The Tier List Vote": "Rank everything: the definitive ranking.",
 "The Award Vote": "Community awards: the ceremony, voted.",
 "The Feedback Poll": "What\u2019s working? The honest mirror.",
 "The Challenge Vote": "Pick the next challenge: the dare democracy.",
 "The Guest Vote": "Who should join? The casting poll.",
 "The Charity Poll": "Where should we give? The generous vote.",
 "The Merch Vote": "What should we make? The product poll.",
 "The Lore Poll": "Shape the story: the narrative democracy.",
 "The Constitutional Poll": "Community rules, voted: the founding document.",
 "The Annual Awards": "The year\u2019s best, decided: the institution.",
 "The Direction Referendum": "Big pivots, community-approved: the mandate.",
 "The Hall of Fame": "Immortalize the legends: the honored vote.",
 "The Succession Poll": "Who leads next? The democratic future.",
 "The Merger Vote": "Join forces? The historic decision.",
 "The Legacy Poll": "What endures? The timeless vote.",
 "The Global Poll": "Many communities, one question: the united vote.",
 "Teaching Poll Craft": "Show others: the democratic mentor.",
 "Masterclass: Collective Intelligence": "Why groups decide well: the wisdom of crowds."
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
    name:topic+' — audience poll record',
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

var BUILD_POLL_GEN=(function(){
return function(inp){
  var topic=inp.topic||'tonight\u2019s stream';
  var r=prng(inp.seed||23);
  var sets=[
    ['Which should we do first?',['Option A: the safe pick','Option B: the spicy pick','Option C: chat decides live']],
    ['Rate my last '+topic+':',['10/10 flawless','Solid 7','Needs work','Chaotic (affectionate)']],
    ['You choose the next '+topic+':',['The fan favorite','The underdog','Something brand new']],
    ['Hot take check:',['Agree strongly','Agree a little','Disagree','Fighting words']]
  ];
  var sections=shuffle(sets,r).slice(0,3).map(function(s){return {h:s[0],items:s[1]};});
  sections.push({h:'Poll craft rules',items:['Two to four options — more splits the vote into noise.','Always include one funny option; humor drives turnout.','Close the loop on stream: announce the winner and DO it.']});
  return {title:'Audience polls: '+topic,intro:'Polls tuned for '+(inp.platform||'stream chat')+' — built to pull lurkers into participants.',sections:sections};
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
gen.builderId="poll-gen";
gen.builderFields=[["topic", "Topic", "text", "tonight\u2019s stream"], ["platform", "Platform", "select", ["stream chat", "Discord", "YouTube", "X/Twitter"]], ["seed", "Seed (optional)", "number", "23"]];
gen.build=BUILD_POLL_GEN;

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-audience-poll-generator-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();