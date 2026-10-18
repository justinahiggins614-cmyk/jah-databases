(function(){'use strict';
/* JAH Signature Checkers and Draughts Database generator — jahdb-checkers-draughts-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CHECKDR-SIG";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The Signature checkers ladder", "Signature capture-vision drills", "The Signature forced-capture habit", "Signature king-path practice", "Signature checkers opposition training", "The Signature shot-first method", "Signature checkers endgame counting", "Signature opening flashcards", "Signature checkers game journaling", "The Signature checkers blunder autopsy", "Signature daily position review"], "Compounded": ["The Northgate draughts method", "The Harborlight International system", "The Keystone opening plan", "The Ridgeline shot library", "The Fairwind king system", "The Stonebridge checkers defense method", "The Thornfield checkers attack lab", "The Beacon checkers endgame system", "The Millrace checkers play", "The Cinderline checkers counter-system", "The Gullwing Russian-draughts plan", "The Foxglove Pool-checkers plan"], "Advanced": ["Signature Shot Puzzle No. 1: The Harbor Shot (original composition)", "Signature Shot Puzzle No. 2: The Northgate King (original composition)", "Signature Shot Puzzle No. 3: The Lantern Jump (original composition)", "Signature Shot Puzzle No. 4: The Tidewater Block (original composition)", "Signature Shot Puzzle No. 5: The Quarry Sacrifice (original composition)", "Signature Shot Puzzle No. 6: The Falcon's Flight (original composition)", "Signature Shot Puzzle No. 7: The Millstone Majority (original composition)", "Signature Shot Puzzle No. 8: The Beacon's Opposition (original composition)", "Signature Shot Puzzle No. 9: The Cinder Comeback (original composition)", "Signature Shot Puzzle No. 10: The Gullwing Sweep (original composition)", "Signature Shot Puzzle No. 11: The Meridian (original composition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# checkers-capture-demo \u2014 "+safe+"\n"
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
    name:topic+' \u2014 checkers record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A checkers record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"checkers-capture-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-checkers-draughts-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('checkers-draughts-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
