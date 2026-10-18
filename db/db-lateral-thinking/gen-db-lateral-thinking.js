(function(){'use strict';
/* JAH The Lateral Thinking Database Database generator — jahdb-db-lateral-thinking-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LATTHI-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Lateral: A man lives on the 10th floor. Every day he takes th...",
  "Lateral: A man is found dead in a field, with a coal lump, a...",
  "Lateral: A man hanged himself from a ceiling beam, but there...",
  "Lateral: A woman shoots her husband, holds him underwater for...",
  "Lateral: A rooster lays an egg on a peaked roof. Which way do...",
  "Lateral: How many months have 28 days...",
  "Lateral: A man shaves every day but keeps his beard long. How...",
  "Lateral: Two men play five games of chess. Each wins three. N...",
  "Lateral: The music stopped and she died. What happened...",
  "Lateral: What goes up and down but never moves...",
  "Lateral: A cowboy rides into town on Friday, stays three days..."
 ],
 "Compounded": [
  "Lateral: A man married twenty women but never divorced and br...",
  "Lateral: A truck is stuck under a low bridge, wedged tight. H...",
  "Lateral: A surgeon refuses to operate on a boy, saying 'he is...",
  "Lateral: A man is found dead in a desert wearing a backpack...",
  "Lateral: Two mothers and two daughters go fishing and catch t...",
  "Lateral: A man predicts the score of a game before it starts...",
  "Lateral: A man drinks the water, then dies. Another man drink...",
  "Lateral: What has keys but no locks, space but no room...",
  "Lateral: How can you throw a ball and have it come back to yo...",
  "Lateral: A cabin in the woods: everyone inside is dead. What...",
  "Lateral: A man walks into a bar and asks for water. The barte...",
  "Lateral: What belongs to you but others use it more than you..."
 ],
 "Advanced": [
  "Lateral: Three switches outside, three bulbs inside one room...",
  "Lateral: 100 prisoners, one light bulb, one room. They must d...",
  "Lateral: Two doors: one leads to freedom, one to doom. One gu...",
  "Lateral: 12 balls, one heavier-or-lighter. A balance scale, 3...",
  "Lateral: Fox, chicken, and grain must cross a river; the boat...",
  "Lateral: Four people must cross a bridge at night with one to...",
  "Lateral: Three boxes labeled APPLES, ORANGES, MIXED - all lab...",
  "Lateral: A 4-minute and a 7-minute hourglass: measure exactly...",
  "Lateral: Blue-eyed islanders: all perfect logicians, all leav...",
  "Lateral: You have 10 red and 10 blue hats... (hat guessing, o...",
  "Lateral: Three gods: True, False, Random. One question each..."
 ]
};
var DEMOKIND="twist-proof";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Lateral Thinking Study — "+safe+"\n"
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
    name:topic+' — lateral thinking record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A lateral thinking record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-db-lateral-thinking-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-lateral-thinking',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
