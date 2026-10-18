(function(){'use strict';
/* JAH The Most Expensive vs. Most Affordable Signature Database generator — jahdb-db-most-expensive-vs-most-affordable-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MEVMAS-";
var FIELDS=["Cost Foundations","Luxury vs Thrift","Value Verdicts"];
var TOPICS={
 "Cost Foundations": [
  "Yacht vs Kayak: Watercraft Cost (Signature Edition) - Cost Foundations",
  "Caviar vs Beans: Protein Cost (Signature Edition) - Cost Foundations",
  "Mansion vs Tiny House: Home Cost (Signature Edition) - Cost Foundations",
  "First Class vs Economy: Flight Cost (Signature Edition) - Cost Foundations",
  "Designer Bag vs Tote: Carry Cost (Signature Edition) - Cost Foundations",
  "Truffle vs Mushroom: Fungi Cost (Signature Edition) - Cost Foundations",
  "Champagne vs Sparkling Water: Bubbles (Signature Edition) - Cost Foundations",
  "Sports Car vs Bicycle: Commute Cost (Signature Edition) - Cost Foundations",
  "Hotel Suite vs Hostel: Sleep Cost (Signature Edition) - Cost Foundations",
  "Watch vs Phone Time: Time Cost (Signature Edition) - Cost Foundations",
  "Suit vs Jeans: Clothing Cost (Signature Edition) - Cost Foundations",
  "Private Jet vs Bus: Travel Cost (Signature Edition) - Cost Foundations"
 ],
 "Luxury vs Thrift": [
  "Wagyu vs Ground Beef: Meat Cost (Signature Edition) - Luxury vs Thrift",
  "Penthouse vs Studio: City Living (Signature Edition) - Luxury vs Thrift",
  "Grand Piano vs Keyboard: Music Cost (Signature Edition) - Luxury vs Thrift",
  "Safari vs Backyard Camping: Adventure Cost (Signature Edition) - Luxury vs Thrift",
  "Diamond vs Cubic Zirconia: Sparkle Cost (Signature Edition) - Luxury vs Thrift",
  "Espresso Machine vs French Press: Coffee Cost (Signature Edition) - Luxury vs Thrift",
  "Tesla vs Used Corolla: Car Value (Signature Edition) - Luxury vs Thrift",
  "Spa Day vs Hot Bath: Relaxation Cost (Signature Edition) - Luxury vs Thrift",
  "Art Original vs Print: Wall Cost (Signature Edition) - Luxury vs Thrift",
  "Golf Club vs Park: Green Cost (Signature Edition) - Luxury vs Thrift"
 ],
 "Value Verdicts": [
  "Wedding vs Courthouse: Celebration Cost (Signature Edition) - Value Verdicts",
  "College vs Library: Education Cost (Signature Edition) - Value Verdicts",
  "Gym vs Bodyweight: Fitness Cost (Signature Edition) - Value Verdicts",
  "Therapist vs Journal: Mind Cost (Signature Edition) - Value Verdicts",
  "New Phone vs Old Phone: Tech Cost (Signature Edition) - Value Verdicts",
  "Organic vs Conventional: Food Cost (Signature Edition) - Value Verdicts",
  "House Cleaner vs DIY: Time Cost (Signature Edition) - Value Verdicts",
  "Lawyer vs Legal Aid: Justice Cost (Signature Edition) - Value Verdicts",
  "Concert vs Street Music: Music Cost (Signature Edition) - Value Verdicts",
  "Fine Dining vs Food Truck: Meal Cost (Signature Edition) - Value Verdicts",
  "Business Class vs Premium Economy: Middle Path (Signature Edition) - Value Verdicts",
  "New Car vs Certified Used: Smart Money (Signature Edition) - Value Verdicts"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Expensive Vs Affordable Study — "+safe+"\n"
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
    name:topic+' — cost comparison record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A cost comparison record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"expensive-vs-affordable-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-most-expensive-vs-most-affordable-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-most-expensive-vs-most-affordable-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
