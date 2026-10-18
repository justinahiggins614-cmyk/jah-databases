(function(){'use strict';
/* JAH Signature Chess Tactics Database generator — jahdb-chess-tactics-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CHESSTAC-SIG";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The Signature motif-first method", "Signature tactics pattern flashcards", "The Signature three-scan board check", "Signature forcing-move drills", "Signature capture-sequencing", "The Signature loose-piece audit", "Signature mate-pattern immersion", "Signature calculation journaling", "The Signature tactics blunder autopsy", "Signature time-pressure tactics", "Signature puzzle-rating plan"], "Compounded": ["The Northgate tactics method", "The Harborlight combination system", "The Keystone calculation plan", "The Ridgeline pattern library", "The Fairwind forcing-move system", "The Stonebridge defense-tactics flip", "The Thornfield sacrifice lab", "The Beacon mate-net system", "The Millrace practical tactics", "The Cinderline counter-tactics", "The Gullwing initiative system", "The Foxglove quiet-move lab"], "Advanced": ["Signature Tactics Puzzle No. 1: The Harbor Fork (original composition)", "Signature Tactics Puzzle No. 2: The Northgate Pin (original composition)", "Signature Tactics Puzzle No. 3: The Lantern Skewer (original composition)", "Signature Tactics Puzzle No. 4: The Tidewater Discovery (original composition)", "Signature Tactics Puzzle No. 5: The Quarry Zwischenzug (original composition)", "Signature Tactics Puzzle No. 6: The Falcon Windmill (original composition)", "Signature Tactics Puzzle No. 7: The Millstone Smother (original composition)", "Signature Tactics Puzzle No. 8: The Beacon Anastasia (original composition)", "Signature Tactics Puzzle No. 9: The Cinder Desperado (original composition)", "Signature Tactics Puzzle No. 10: The Gullwing Quiet (original composition)", "Signature Tactics Puzzle No. 11: The Meridian (original composition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# chess-tactics-motif-demo \u2014 "+safe+"\n"
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
    name:topic+' \u2014 chess tactic record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A chess tactic record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"chess-tactics-motif-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-chess-tactics-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('chess-tactics-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
