(function(){'use strict';
/* JAH Signature Backgammon Database generator — jahdb-backgammon-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BACKGAM-SIG";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The Signature backgammon ladder", "Signature pip-count drills", "The Signature opening-roll flashcards", "Signature blot-avoidance practice", "Signature cube-first thinking", "The Signature anchor habit", "Signature bearoff counting", "Signature match-score awareness", "Signature backgammon game journaling", "The Signature error autopsy", "Signature daily rollout review"], "Compounded": ["The Northgate checker-play method", "The Harborlight priming system", "The Keystone anchor plan", "The Ridgeline blitz library", "The Fairwind back-game system", "The Stonebridge holding method", "The Thornfield cube lab", "The Beacon bearoff system", "The Millrace backgammon play", "The Cinderline backgammon defense", "The Gullwing racing plan", "The Foxglove contact plan"], "Advanced": ["Signature Position Study No. 1: The Harbor Prime (original composition)", "Signature Position Study No. 2: The Northgate Cube (original composition)", "Signature Position Study No. 3: The Lantern Blitz (original composition)", "Signature Position Study No. 4: The Tidewater Back Game (original composition)", "Signature Position Study No. 5: The Quarry Bearoff (original composition)", "Signature Position Study No. 6: The Falcon Race (original composition)", "Signature Position Study No. 7: The Millstone Anchor (original composition)", "Signature Position Study No. 8: The Beacon Timing (original composition)", "Signature Position Study No. 9: The Cinder Gammon (original composition)", "Signature Position Study No. 10: The Gullwing Redouble (original composition)", "Signature Position Study No. 11: The Meridian (original composition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# backgammon-pip-count-demo \u2014 "+safe+"\n"
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
    name:topic+' \u2014 backgammon record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A backgammon record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"backgammon-pip-count-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-backgammon-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('backgammon-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
