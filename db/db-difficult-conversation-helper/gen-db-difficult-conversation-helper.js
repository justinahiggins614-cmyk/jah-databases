(function(){'use strict';
/* JAH The Difficult Conversation Helper Database Database generator — jahdb-db-difficult-conversation-helper-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DIFCONHEL-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Hard talk: Telling a friend they hurt your feelings...",
  "Hard talk: Asking a roommate to clean up...",
  "Hard talk: Declining extra work politely...",
  "Hard talk: Telling someone their joke offended you...",
  "Hard talk: Asking for a raise...",
  "Hard talk: Ending a subscription or commitment...",
  "Hard talk: Telling a friend you need space...",
  "Hard talk: Giving gentle feedback...",
  "Hard talk: Saying no to a favor...",
  "Hard talk: Addressing lateness...",
  "Hard talk: Talking about money with friends..."
 ],
 "Compounded": [
  "Hard talk: Confronting a partner about distance...",
  "Hard talk: Telling your boss you're overwhelmed...",
  "Hard talk: Discussing a parent's driving...",
  "Hard talk: Addressing a friend's drinking...",
  "Hard talk: Negotiating with a difficult client...",
  "Hard talk: Telling family about a big decision...",
  "Hard talk: Apologizing sincerely...",
  "Hard talk: Setting boundaries with in-laws...",
  "Hard talk: Discussing chores with a partner...",
  "Hard talk: Firing someone kindly...",
  "Hard talk: Talking to kids about divorce...",
  "Hard talk: Addressing gossip..."
 ],
 "Advanced": [
  "Hard talk: Ending a long friendship...",
  "Hard talk: Confronting infidelity...",
  "Hard talk: Intervention for addiction...",
  "Hard talk: Discussing end-of-life wishes...",
  "Hard talk: Reporting wrongdoing...",
  "Hard talk: Leaving a faith community...",
  "Hard talk: Confronting abuse...",
  "Hard talk: Negotiating a divorce...",
  "Hard talk: Telling the truth after years...",
  "Hard talk: Quitting a dream gracefully...",
  "Hard talk: Asking for help when proud..."
 ]
};
var DEMOKIND="talk-proof";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Difficult Conversation Study — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — conversation guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A conversation guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-difficult-conversation-helper-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-difficult-conversation-helper',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
