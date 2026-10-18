(function(){'use strict';
/* JAH Soccer Skills Signature Database generator — jahdb-soccer-skills-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SOCSKS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["First Touch (Signature Edition)", "Passing with the Inside of the Foot (Signature Edition)", "The Instep Drive (Signature Edition)", "Dribbling with the Laces (Signature Edition)", "Close Control in Traffic (Signature Edition)", "Receiving Across the Body (Signature Edition)", "Shielding the Ball (Signature Edition)", "The Push Pass Under Pressure (Signature Edition)", "Heading Fundamentals (Signature Edition)", "Throw-In Technique (Signature Edition)", "Goalkeeper Ready Stance (Signature Edition)"], "Compounded": ["The Cruyff Turn (Signature Edition)", "The Step-Over (Signature Edition)", "Driven Crosses (Signature Edition)", "The Volley (Signature Edition)", "Chipping the Goalkeeper (Signature Edition)", "Long Passing (Switching Play) (Signature Edition)", "One-Touch Combinations (Wall Pass) (Signature Edition)", "Sliding Tackle Timing (Signature Edition)", "Curling with the Inside Foot (Signature Edition)", "The Block Tackle (Signature Edition)", "Goalkeeper Diving Technique (Signature Edition)", "Penalty Kick Technique (Signature Edition)"], "Advanced": ["The Elastico (Flip-Flap) (Signature Edition)", "The Rabona (Signature Edition)", "Set-Piece Delivery (Corners) (Signature Edition)", "Free-Kick Curling and the Knuckleball (Signature Edition)", "First-Time Finishing Under Pressure (Signature Edition)", "The Backheel (Signature Edition)", "Sweeper-Keeper Distribution (Signature Edition)", "Aerial Duels Technique (Signature Edition)", "Pressing as a Skill Set (Signature Edition)", "The Scorpion Kick (Signature Edition)", "Match-Tempo Dribbling (Signature Edition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# soccer-drill-demo \u2014 "+safe+"\n"
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
    name:topic+' \u2014 soccer skill record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A soccer skill record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"soccer-drill-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-soccer-skills-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('soccer-skills-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
