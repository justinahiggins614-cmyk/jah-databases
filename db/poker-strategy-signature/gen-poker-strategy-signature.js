(function(){'use strict';
/* JAH Signature Poker Strategy Database generator — jahdb-poker-strategy-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-POKSTR-SIG";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The Signature poker ladder", "Signature range-visualization drills", "The Signature outs-counting habit", "Signature position-awareness practice", "Signature pot-odds fluency", "The Signature story-check method", "Signature opponent profiling", "Signature bankroll journaling", "The Signature tilt protocol", "The Signature poker blunder autopsy", "Signature poker daily hand review"], "Compounded": ["The Northgate preflop system", "The Harborlight postflop system", "The Keystone 3-bet plan", "The Ridgeline c-bet library", "The Fairwind tournament system", "The Stonebridge ICM method", "The Thornfield bluff lab", "The Beacon value system", "The Millrace fast-fold system", "The Cinderline comeback system", "The Gullwing Omaha plan", "The Foxglove heads-up plan"], "Advanced": ["Signature Hand Study No. 1: The Harbor Bluff (original composition)", "Signature Hand Study No. 2: The Northgate Call (original composition)", "Signature Hand Study No. 3: The Lantern Value (original composition)", "Signature Hand Study No. 4: The Tidewater Fold (original composition)", "Signature Hand Study No. 5: The Quarry 3-bet (original composition)", "Signature Hand Study No. 6: The Falcon's Draw (original composition)", "Signature Hand Study No. 7: The Millstone ICM (original composition)", "Signature Hand Study No. 8: The Beacon's Range (original composition)", "Signature Hand Study No. 9: The Cinder Shove (original composition)", "Signature Hand Study No. 10: The Gullwing Nuts (original composition)", "Signature Poker Hand Study No. 11: The Meridian (original composition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# poker-odds-demo \u2014 "+safe+"\n"
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
    name:topic+' \u2014 poker strategy record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A poker strategy record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"poker-odds-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-poker-strategy-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('poker-strategy-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
