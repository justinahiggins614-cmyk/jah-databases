(function(){'use strict';
/* JAH Signature Rummy Card Games Database generator — jahdb-rummy-games-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-RUMMY-SIG";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The Signature rummy ladder", "Signature meld-vision drills", "The Signature discard-reading habit", "Signature deadwood-counting fluency", "Signature knock-timing practice", "The Signature draw-or-take method", "Signature defensive discarding", "Signature score-race awareness", "Signature rummy game journaling", "The Signature rummy blunder autopsy", "Signature rummy daily hand review"], "Compounded": ["Harborlight Rummy: a Signature rummy game", "Northgate Rummy: a Signature rummy game", "Keystone Rummy: a Signature rummy game", "Ridgeline Rummy: a Signature rummy game", "Fairwind Rummy: a Signature rummy game", "Stonebridge Rummy: a Signature rummy game", "Thornfield Rummy: a Signature rummy game", "Beacon Rummy: a Signature rummy game", "Millrace Rummy: a Signature rummy game", "Cinderline Rummy: a Signature rummy game", "Gullwing Rummy: a Signature rummy game", "Foxglove Rummy: a Signature rummy game"], "Advanced": ["Signature Rummy Game No. 1: The Meridian Meld (original design)", "Signature Rummy Game No. 2: The Tidal Draw (original design)", "Signature Rummy Game No. 3: The Forge Meld (original design)", "Signature Rummy Game No. 4: The Mirror Gin (original design)", "Signature Rummy Game No. 5: The Labyrinth Layoff (original design)", "Signature Rummy Game No. 6: The Phoenix Hand (original design)", "Signature Rummy Game No. 7: The Eclipse Knock (original design)", "Signature Rummy Game No. 8: The Constellation Meld (original design)", "Signature Rummy Game No. 9: The Hourglass Rummy (original design)", "Signature Rummy Game No. 10: The Tapestry Meld (original design)", "Signature Rummy Game No. 11: The Signature Game (original design)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# rummy-meld-demo \u2014 "+safe+"\n"
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
    name:topic+' \u2014 rummy game record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A rummy game record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"rummy-meld-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-rummy-games-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('rummy-games-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
