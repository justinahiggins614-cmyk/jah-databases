(function(){'use strict';
/* JAH Signature Mancala Database generator — jahdb-mancala-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MANCALA-SIG";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The Signature mancala ladder", "Signature sowing drills", "The Signature count-ahead habit", "Signature capture-vision practice", "Signature free-turn planning", "The Signature seed-triangle method", "Signature mancala endgame counting", "Signature variant-tasting tour", "Signature mancala game journaling", "The Signature mancala blunder autopsy", "Signature daily sowing review"], "Compounded": ["The Northgate Kalah method", "The Harborlight Oware system", "The Keystone sowing plan", "The Ridgeline capture library", "The Fairwind tempo system", "The Stonebridge mancala defense method", "The Thornfield mancala attack lab", "The Beacon mancala endgame system", "The Millrace mancala play", "The Cinderline mancala counter-system", "The Gullwing Bao plan", "The Foxglove Dakon plan"], "Advanced": ["Signature Sowing Puzzle No. 1: The Harbor Chain (original composition)", "Signature Sowing Puzzle No. 2: The Northgate Loop (original composition)", "Signature Sowing Puzzle No. 3: The Lantern Free Turn (original composition)", "Signature Sowing Puzzle No. 4: The Tidewater Sweep (original composition)", "Signature Sowing Puzzle No. 5: The Quarry Capture (original composition)", "Signature Sowing Puzzle No. 6: The Falcon Relay (original composition)", "Signature Sowing Puzzle No. 7: The Millstone Feed (original composition)", "Signature Sowing Puzzle No. 8: The Beacon's Count (original composition)", "Signature Sowing Puzzle No. 9: The Cinder Sacrifice (original composition)", "Signature Sowing Puzzle No. 10: The Gullwing Tuz (original composition)", "Signature Sowing Puzzle No. 11: The Meridian (original composition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# mancala-sowing-demo \u2014 "+safe+"\n"
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
    name:topic+' \u2014 mancala record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A mancala record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"mancala-sowing-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-mancala-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('mancala-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
