(function(){'use strict';
/* JAH The Nail Art Universe generator — jahdb-db-nail-art-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NLARS-";
var FIELDS=["Nail Art Foundations", "Design Library", "Nail Art Mastery"];
var TOPICS={"Nail Art Foundations": ["Nail Anatomy Basics", "The Perfect Base Coat", "Polish Application 101", "The Top Coat Seal", "Cuticle Care Ritual", "Filing and Shaping", "Polish Removal Without Damage", "Nail Strength Basics", "The Clean Canvas", "Solid Color Mastery", "Matte Versus Gloss"], "Design Library": ["The French Manicure", "Polka Dot Play", "Stripes and Lines", "The Ombr\u00e9 Fade", "Marble Effects", "Floral Nail Art", "Geometric Designs", "Glitter Placement", "Stamping Art", "Hand-Painted Details", "Chrome and Metallic", "Negative Space Art"], "Nail Art Mastery": ["Salon-Quality at Home", "Gel Polish Basics", "Acrylic and Extensions", "Nail Art Photography", "The Business of Nails", "Seasonal Collections", "Repairing Breaks", "Nail Health Recovery", "Competition Nail Art", "Teaching Nail Art", "Your Signature Nail Style"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# minibot — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — nail art record',
    title:topic,
    description:"SAMPLE RECORD (generated — structural Signature sample). A Signature-original nail art record sample of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated Signature sample record — not an archive record. Seeded Signature records are the authoritative entries.',
    demo:{kind:"topic-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-db-nail-art-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("db-nail-art-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
