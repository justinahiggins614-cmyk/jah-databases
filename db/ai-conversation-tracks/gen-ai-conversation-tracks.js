(function(){'use strict';
/* AI Conversation Tracks Database generator — jahdb-ai-conversation-tracks-1.0.
   Property of Justin Addam Higgins (JAH).
   Whole example conversations the AI references to stay coherent and helpful,
   especially in longer conversations. Each track: full conversation + guidance.
   Deterministic: same seed, same record. src:"signature" = Signature-authored original. */
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-ACT-';
var SRC='signature';
var RECORD_KIND='conversation track';
var ANGLES=['full-track','coachs-notes','quick-reference'];
var CATS=['greeting','common-question','long-conversation','follow-up','difficult-topic','confusion-recovery','topic-shift','closing','encouragement','technical-help'];
var TECHS={
 'greeting':["learn name early","one open question","match energy","no interrogation"],
 'common-question':["analogy first","check understanding","one step at a time","honest about limits"],
 'long-conversation':["track details","reference earlier points","summarize progress","revisit open loops"],
 'follow-up':["one question at a time","build on last answer","genuine curiosity","ask what they're avoiding"],
 'difficult-topic':["empathy first","honest not harsh","offer path forward","normalize feelings"],
 'confusion-recovery':["own mistakes fast","try new angle","clarify before charging ahead","blame explanation not user"],
 'topic-shift':["use bridges","follow user lead","brief acknowledge","offer to return"],
 'closing':["summarize wins","leave door open","warm not abrupt","accept thanks simply"],
 'encouragement':["validate difficulty","remind of progress","concrete next step","no toxic positivity"],
 'technical-help':["see the code","reason aloud","teach not just fix","layer complexity"]
};
var GUIDANCE={
 'greeting':"Make the first moment warm and easy. Learn their name, ask one open question, match their energy.",
 'common-question':"Answer clearly with an analogy, check understanding, go one step at a time. Never condescend.",
 'long-conversation':"Keep a mental model of everything said. Reference earlier details, summarize progress, revisit open loops.",
 'follow-up':"Ask one good question at a time, each building on the last answer. Show genuine curiosity.",
 'difficult-topic':"Lead with empathy, be honest without harshness, offer a path forward. Normalize their feelings.",
 'confusion-recovery':"Own mistakes immediately. If they didn't get it, try a completely different angle. Clarify before charging ahead.",
 'topic-shift':"Use natural bridges. Follow the user's lead — don't resist shifts. Offer to return to dropped topics.",
 'closing':"Summarize what was accomplished, leave the door open, end warm. Accept thanks simply.",
 'encouragement':"Validate the difficulty first — toxic positivity backfires. Remind them of progress, give one concrete next step.",
 'technical-help':"Diagnose before prescribing. Reason aloud so they learn. Layer complexity — simple first, deeper on request."
};
var TOPIC_SEEDS={
 'greeting':["first hello","returning user","shy newcomer","curious tester","busy visitor","nervous first-timer","skeptical professional"],
 'common-question':["explain simply","step-by-step how-to","compare options","health question","math help","history question","science question","interview prep"],
 'long-conversation':["remembering details","building an idea","wedding planning","novel writing","fitness journey","language learning","road trip plan"],
 'follow-up':["digging deeper","creative project","career change","startup validation","relationship clarity","big goal breakdown"],
 'difficult-topic':["bad news gently","sensitive personal","disagreement","job loss","ethical dilemma","apology coaching","grief support","anxiety help"],
 'confusion-recovery':["owning a mistake","untangling confusion","clarifying request","fixing recommendation","breaking a loop"],
 'topic-shift':["natural bridge","abrupt change","returning to topic"],
 'closing':["satisfying end","gracious thanks","pausing a project","honest pause"],
 'encouragement':["through doubt","celebrating wins","sticking with it","creative block","failing forward"],
 'technical-help':["debugging code","explaining concepts","wifi troubleshooting","phone fixes","api explained"]
};
function buildConversation(cat,topic,rnd){
  var g=(GUIDANCE[cat]||"").split('. ')[0];
  var conv=[
    {speaker:'user',text:'(Opening on: '+topic+')'},
    {speaker:'ai',text:'Warm, engaged opening that invites the user in. '+g+'.'},
    {speaker:'user',text:'(User responds — the AI listens for the real need beneath the words.)'},
    {speaker:'ai',text:'Reflects understanding, then moves the conversation forward with a clear next step or a thoughtful question.'},
    {speaker:'user',text:'(User engages deeper — trust is building.)'},
    {speaker:'ai',text:'Builds on everything said so far. References earlier details to show attentiveness.'},
    {speaker:'user',text:'(A twist — a follow-up, a doubt, or a new angle.)'},
    {speaker:'ai',text:'Handles the twist gracefully using the track guidance: '+GUIDANCE[cat]},
    {speaker:'user',text:'(User responds positively — the track is working.)'},
    {speaker:'ai',text:'Closes the loop warmly, summarizes value, leaves the door open.'}
  ];
  return conv;
}
function defaultDemo(){
  return{kind:'track-walkthrough',
    program:"// track walkthrough — run with: node demo.js\n// (place the record JSON next to this file as record.json)\nconst track = JSON.parse(require('fs').readFileSync('record.json', 'utf8'));\nconsole.log('TRACK: ' + track.title + ' (' + track.turn_count + ' turns)');\n(track.conversation||[]).forEach(function(t, i) {\n  console.log('\\n[' + (i+1) + '] ' + String(t.speaker).toUpperCase() + ': ' + t.text);\n});\nconsole.log('\\nGuidance: ' + track.guidance);",
    note:'A runnable walkthrough of this conversation track. Save as demo.js, save the record JSON as record.json beside it, and run with node.'};
}
function generate(seed,opts){
  opts=opts||{};
  var s=(seed>>>0)||1, rnd=prng(s);
  var cat=opts.genre&&CATS.indexOf(opts.genre)>=0?opts.genre:pick(CATS,rnd);
  var angle=opts.angle&&ANGLES.indexOf(opts.angle)>=0?opts.angle:pick(ANGLES,rnd);
  var topics=TOPIC_SEEDS[cat]||['general'];
  var topic=opts.topic?String(opts.topic).trim().slice(0,120):pick(topics,rnd);
  var id=PREFIX+pad(s);
  var title=topic.charAt(0).toUpperCase()+topic.slice(1)+' — '+cat.replace(/-/g,' ')+' track';
  if(angle!=='full-track')title+=' ('+angle.replace(/-/g,' ')+')';
  var conv=buildConversation(cat,topic,rnd);
  if(angle==='coachs-notes'){
    var techs=TECHS[cat]||[], out=[], ti=0;
    conv.forEach(function(t){
      out.push(t);
      if(t.speaker==='ai'){out.push({speaker:'coach',text:'[Technique: '+(techs[ti%techs.length]||'stay helpful')+']'});ti++;}
    });
    conv=out;
  }else if(angle==='quick-reference'){
    conv=[conv[0],conv[1],{speaker:'coach',text:'[... conversation develops ...]'},conv[6],conv[7],{speaker:'coach',text:'[... closing ...]'},conv[8],conv[9]];
  }
  return{
    id:id,
    title:title,
    description:'A Signature conversation track for '+cat.replace(/-/g,' ')+' ('+topic+'). Generated sample — seeded archive tracks carry full hand-written conversations.',
    genre:cat,
    type:RECORD_KIND,
    track_angle:angle,
    track_purpose:'Give the AI a reference conversation so it always has an idea what to say.',
    guidance:GUIDANCE[cat]||'',
    turn_count:conv.length,
    conversation:conv,
    key_techniques:TECHS[cat]||[],
    demo:defaultDemo(),
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample track — seeded archive tracks are the authoritative hand-written entries.',
    _seed:s
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(typeof r.id!=='string'||r.id.indexOf(PREFIX)!==0||!/\d{6}$/.test(r.id))e.push('id');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(typeof r.description!=='string'||r.description.length<20)e.push('description');
  if(CATS.indexOf(r.genre)<0)e.push('genre');
  if(ANGLES.indexOf(r.track_angle)<0)e.push('track_angle');
  if(!Array.isArray(r.conversation)||r.conversation.length<4)e.push('conversation');
  if(typeof r.guidance!=='string'||!r.guidance.length)e.push('guidance');
  if(!r.demo||typeof r.demo!=='object')e.push('demo');
  if(!r.src)e.push('src');
  return{ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  for(var i=0;i<sample.length;i++){if(sample[i]&&sample[i].t===rec.title)return{ok:false,errors:['duplicate title in archive sample']};}
  return{ok:true,errors:[]};
}
var gen={version:'jahdb-ai-conversation-tracks-1.0',generate:generate,validate:validate,driftCheck:driftCheck,genres:CATS,angles:ANGLES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('ai-conversation-tracks',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
