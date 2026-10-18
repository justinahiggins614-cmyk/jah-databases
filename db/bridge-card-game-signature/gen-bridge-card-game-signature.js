(function(){'use strict';
/* JAH Signature Bridge Card Game Database generator — jahdb-bridge-card-game-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BRIDGE-SIG";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The Signature bridge ladder", "Signature bridge trick-counting drills", "The Signature bid-with-a-plan habit", "Signature dummy-play visualization", "Signature suit-combination flashcards", "The Signature count-the-hand method", "Signature tempo in bidding", "Signature partnership language", "Signature bridge game journaling", "The Signature bridge blunder autopsy", "Signature bridge daily hand review"], "Compounded": ["The Northgate bidding method", "The Harborlight declarer system", "The Keystone bridge defense plan", "The Ridgeline finesse library", "The Fairwind slam-try system", "The Stonebridge signal method", "The Thornfield endplay lab", "The Beacon duplicate system", "The Millrace bridge play", "The Cinderline bridge counter-system", "The Gullwing preempt plan", "The Foxglove balancing plan"], "Advanced": ["Signature Play Problem No. 1: The Harbor Finesse (original composition)", "Signature Play Problem No. 2: The Northgate Endplay (original composition)", "Signature Play Problem No. 3: The Lantern Squeeze (original composition)", "Signature Play Problem No. 4: The Tidewater Ruff (original composition)", "Signature Play Problem No. 5: The Quarry Defense (original composition)", "Signature Play Problem No. 6: The Falcon's Slam (original composition)", "Signature Play Problem No. 7: The Millstone Entry (original composition)", "Signature Play Problem No. 8: The Beacon's Count (original composition)", "Signature Play Problem No. 9: The Cinder Falsecard (original composition)", "Signature Play Problem No. 10: The Gullwing Preempt (original composition)", "Signature Play Problem No. 11: The Meridian (original composition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# bridge-hcp-demo \u2014 "+safe+"\n"
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
    name:topic+' \u2014 bridge record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A bridge record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"bridge-hcp-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-bridge-card-game-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('bridge-card-game-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
