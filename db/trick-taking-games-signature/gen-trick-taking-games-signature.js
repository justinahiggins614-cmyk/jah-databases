(function(){'use strict';
/* JAH Signature Trick-Taking Card Games Database generator — jahdb-trick-taking-games-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TRICKTK-SIG";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The Signature trick-taking ladder", "Signature trick-taking counting drills", "The Signature lead-with-a-plan habit", "Signature trump-management practice", "Signature partnership signals", "The Signature moonshot method", "Signature nil-bid training", "Signature prediction scoring", "Signature trick-taking game journaling", "The Signature trick-taking blunder autopsy", "Signature trick-taking daily hand review"], "Compounded": ["Harborlight: a Signature trick-taking game", "Northgate: a Signature trick-taking game", "Keystone: a Signature trick-taking game", "Ridgeline: a Signature trick-taking game", "Fairwind: a Signature trick-taking game", "Stonebridge: a Signature trick-taking game", "Thornfield: a Signature trick-taking game", "Beacon: a Signature trick-taking game", "Millrace: a Signature trick-taking game", "Cinderline: a Signature trick-taking game", "Gullwing: a Signature trick-taking game", "Foxglove: a Signature trick-taking game"], "Advanced": ["Signature Trick-Taking Game No. 1: The Meridian Bid (original design)", "Signature Trick-Taking Game No. 2: The Tidal Trump (original design)", "Signature Trick-Taking Game No. 3: The Forge Partnership (original design)", "Signature Trick-Taking Game No. 4: The Mirror Nil (original design)", "Signature Trick-Taking Game No. 5: The Labyrinth Lead (original design)", "Signature Trick-Taking Game No. 6: The Phoenix Trick (original design)", "Signature Trick-Taking Game No. 7: The Eclipse Bid (original design)", "Signature Trick-Taking Game No. 8: The Constellation (original design)", "Signature Trick-Taking Game No. 9: The Hourglass (original design)", "Signature Trick-Taking Game No. 10: The Tapestry (original design)", "Signature Trick-Taking Game No. 11: The Signature Game (original design)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# trick-winner-demo \u2014 "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record \u2014 structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' \u2014 trick-taking game record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A trick-taking game record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"trick-winner-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-trick-taking-games-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('trick-taking-games-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
