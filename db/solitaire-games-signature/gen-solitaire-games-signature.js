(function(){'use strict';
/* JAH Signature Solitaire Card Games Database generator — jahdb-solitaire-games-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SOLIT-SIG";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The Signature solitaire ladder", "Signature tableau-reading drills", "The Signature empty-column habit", "Signature stock-cycling practice", "Signature suit-sequencing fluency", "The Signature uncover-first method", "Signature dead-card recognition", "Signature patience pacing", "Signature solitaire game journaling", "The Signature solitaire blunder autopsy", "Signature daily deal review"], "Compounded": ["Harborlight Solitaire: a Signature solitaire game", "Northgate Solitaire: a Signature solitaire game", "Keystone Solitaire: a Signature solitaire game", "Ridgeline Solitaire: a Signature solitaire game", "Fairwind Solitaire: a Signature solitaire game", "Stonebridge Solitaire: a Signature solitaire game", "Thornfield Solitaire: a Signature solitaire game", "Beacon Solitaire: a Signature solitaire game", "Millrace Solitaire: a Signature solitaire game", "Cinderline Solitaire: a Signature solitaire game", "Gullwing Solitaire: a Signature solitaire game", "Foxglove Solitaire: a Signature solitaire game"], "Advanced": ["Signature Solitaire Game No. 1: The Meridian Deal (original design)", "Signature Solitaire Game No. 2: The Tidal Tableau (original design)", "Signature Solitaire Game No. 3: The Forge Foundation (original design)", "Signature Solitaire Game No. 4: The Mirror Deal (original design)", "Signature Solitaire Game No. 5: The Labyrinth Tableau (original design)", "Signature Solitaire Game No. 6: The Phoenix Pile (original design)", "Signature Solitaire Game No. 7: The Eclipse Stock (original design)", "Signature Solitaire Game No. 8: The Constellation (original design)", "Signature Solitaire Game No. 9: The Hourglass Deal (original design)", "Signature Solitaire Game No. 10: The Tapestry Tableau (original design)", "Signature Solitaire Game No. 11: The Signature Game (original design)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# solitaire-stock-demo \u2014 "+safe+"\n"
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
    name:topic+' \u2014 solitaire game record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A solitaire game record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"solitaire-stock-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-solitaire-games-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('solitaire-games-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
