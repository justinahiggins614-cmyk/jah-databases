(function(){'use strict';
/* JAH Signature Mahjong Database generator — jahdb-mahjong-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MAHJONG-SIG";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The Signature mahjong ladder", "Signature tile-fluency drills", "The Signature yaku-first mindset", "Signature discard-reading practice", "Signature efficiency counting", "The Signature defense habit", "Signature push-fold scoring", "Signature table-awareness training", "Signature mahjong game journaling", "The Signature mahjong blunder autopsy", "Signature mahjong daily hand review"], "Compounded": ["The Northgate efficiency method", "The Harborlight yaku system", "The Keystone mahjong defense plan", "The Ridgeline suji library", "The Fairwind dora system", "The Stonebridge betaori method", "The Thornfield mahjong attack lab", "The Beacon yakuman-hunting system", "The Millrace mahjong play", "The Cinderline mahjong counter-system", "The Gullwing sanma plan", "The Foxglove variants plan"], "Advanced": ["Signature Hand Study No. 1: The Harbor Efficiency (original composition)", "Signature Hand Study No. 2: The Northgate Defense (original composition)", "Signature Hand Study No. 3: The Lantern Push (original composition)", "Signature Hand Study No. 4: The Tidewater Dora (original composition)", "Signature Hand Study No. 5: The Quarry Yakuman (original composition)", "Signature Hand Study No. 6: The Falcon's Read (original composition)", "Signature Hand Study No. 7: The Millstone Patience (original composition)", "Signature Hand Study No. 8: The Beacon's Wait (original composition)", "Signature Hand Study No. 9: The Cinder Comeback (original composition)", "Signature Hand Study No. 10: The Gullwing Damaten (original composition)", "Signature Mahjong Hand Study No. 11: The Meridian (original composition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# mahjong-yaku-demo \u2014 "+safe+"\n"
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
    name:topic+' \u2014 mahjong record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A mahjong record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"mahjong-yaku-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-mahjong-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('mahjong-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
